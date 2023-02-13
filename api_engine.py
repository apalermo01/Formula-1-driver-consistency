from typing import Union, Dict
from psycopg2 import connect, sql
import psycopg2 as pg
import pandas as pd
from common import DatabaseConnector
from textwrap import dedent
import time
import numpy as np
import logging
import requests
import json
import os

logger = logging.getLogger(__name__)

# requirements: don't call more than 4 times per second or 200 times in 1 hour
COOLDOWN_PERIOD_S = 20

TABLE_SCHEMA = {
    'seasons': {
        'colnames': ['year', 'url']
    }
}

class APIEngine:

    def __init__(self,
                 login_info: Dict):
        self.login_info = login_info
        self.connector = DatabaseConnector(postgres_login_info=login_info)
        logger.debug("API engine initialized")

    def make_call(self,
                  tablename: str,
                  call_params: Union[None, Dict] = None) -> Union[None, pd.DataFrame]:

        logger.debug(f"calling table {tablename} with params {call_params}")

        # input validation
        if call_params is None:
            call_params = {}

        # check if we've cached the results
        response = self._pull_cache(tablename, call_params)
        if response:
            logger.debug("returning cached response")
        else:
            response = self._do_live_call(tablename, call_params)

        # update staging table
        self._update_table(response)

        # update meta table with call results

        # return results

    def _do_live_call(self,
                      tablename: str,
                      call_params: Union[None, Dict] = None):

        # check that the cooldown period has passed
        if not self.check_cooldown(tablename=tablename):
            logger.error(f"tried to call {tablename} api before cooldown period")
            return

        # update the meta table with the last call time
        # note that the current call time is being recorded BEFORE the call is
        # attempted
        try:
            query = dedent("""
            INSERT INTO meta (table_name, last_call)
            VALUES (%(table)s, %(timestamp)s);
            """)
            now = int(np.datetime64('now').astype(int))
            vars = {
                    "table": tablename,
                    "timestamp": now
            }
            self.connector.execute_query(query, vars)
            logger.debug(f"updated meta table with last call: table={tablename}, time={now}")

        except Exception as e:
            logger.error(e)
            return

        # make the call
        url = self.make_url(tablename, call_params)
        response = self._call(url)

        self._update_cache(response, tablename, call_params)


    @staticmethod
    def _get_path_for_cache(tablename: str, call_params: Dict) -> str:
        param_list = ''.join([f"_{key}={call_params[key]}" for key in call_params])
        filename = f"{tablename}{param_list}.json"
        path = os.path.join(".cache", filename)
        return path

    def _update_cache(self,
                      response: requests.Response,
                      tablename: str,
                      call_params: Dict):
        if response.status_code == 200:
            path = self._get_path_for_cache(tablename, call_params)
            logger.debug(f"updating cache, path = {path}")
            with open(path, "w") as f:
                json.dump(response.json(), f)

    def _pull_cache(self,
                    tablename: str,
                    call_params: Dict) -> Union[None, Dict]:

        path = self._get_path_for_cache(tablename, call_params)
        if os.path.exists(path):
            with open(path, "r") as f:
                response = json.load(f)
            return response
        else:
            return None

    def _update_table(self, call_results):
        # update the staging table with data pulled from api call
        logger.debug(f"recieved call results: {call_results['MRData'].keys()}")

        # hardcoded table data for development purposes
        table = 'SeasonTable'
        table_key = 'Seasons'
        tablename = 'seasons'

        colnames = call_results['MRData'][table][table_key][0].keys()
        data = call_results['MRData'][table][table_key]
        nrows = len(data)
        # TODO: put number of columns recieved in meta table
        logger.debug(f"recieved call results: {colnames}")
        logger.debug(f"recieved {nrows} rows")

        colnames = TABLE_SCHEMA[tablename]['colnames']

        params = {
            'table': sql.Identifier(tablename),
            'collist': sql.SQL(',').join([sql.Identifier(c) for c in colnames])
        }

        query = dedent("""
        INSERT INTO {table}({collist}) VALUES %s
        """)

        data_tuple = [tuple(row.values()) for row in data]

        rows_affected = self.connector.execute_insert(
            query, data_tuple, params=params
        )
        logger.warning(f"updated {rows_affected} rows in table {tablename}")
    def check_cooldown(self, tablename: str) -> bool:
        # check that the cooldown for the api has passed

        ### get the last time the API was called
        query = dedent("""
        SELECT last_call
        FROM meta
        WHERE table_name = %(tablename)s
        ORDER BY last_call DESC
        LIMIT 1;
        """)

        vars = {'tablename': tablename}

        res = self.connector.execute_query(query, vars, ret=True)
        if len(res) < 1:
            return True
        last_call = res['last_call'].values[0]

        ### Since this is only one API, don't worry about pulling the cooldown period from antoher table, just hardcode it.
        now = np.datetime64('now')
        delta = int((now - last_call).astype(int))
        return delta > COOLDOWN_PERIOD_S

    def make_url(self, tablename, call_params) -> str:
        # take the requested query parameters and build the url to submit to the api call
        url = "http://ergast.com/api/f1/"
        if tablename == 'seasons':
            url += 'seasons.json'
        else:
            raise NotImplementedError("can only call seasons table, method is still under development")
        return url

    def _call(self, url):
        # make the actual api call
        response = requests.get(url)
        return response

    def load_cache(self, ) -> pd.DataFrame:
        # load the saved data from an api call
        pass

    def save_to_cache(self, data, params: Dict):
        # take the results of an api call and save it to the cache

        pass

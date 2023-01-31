from typing import Union, Dict
from psycopg2 import connect, sql
import pandas as pd
from common import DatabaseConnector
from textwrap import dedent
import time
import numpy as np
import logging

logger = logging.getLogger(__name__)
# requirements: don't call more than 4 times per second or 200 times in 1 hour
COOLDOWN_PERIOD_S = 20


class APIEngine:

    def __init__(self,
                 login_info: Dict):
        self.login_info = login_info
        self.connector = DatabaseConnector(postgres_login_info=login_info)

    def make_call(self,
                  tablename: str,
                  call_params: Union[None, Dict] = None) -> Union[None, pd.DataFrame]:

        # input validation
        if call_params is None:
            call_params = {}

        # check that the cooldown period has passed
        if not self.check_cooldown(tablename=tablename):
            logger.error(f"tried to call {tablename} api before cooldown period")
            return

        # update the meta table with the last call time
        # note that the current call time is being recorded BEFORE the call is
        # attempted
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
        # make the call

        # update staging table

        # update meta table with call results

        # return results


    def update_table(self):
        # update the staging table with data pulled from api call
        pass

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

    def load_cache(self, ) -> pd.DataFrame:
        # load the saved data from an api call
        pass

    def save_to_cache(self, data, params: Dict):
        # take the results of an api call and save it to the cache

        pass

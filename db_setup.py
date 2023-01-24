### initialize f1 database

import numpy as np
import pandas as pd
import os
import shutil
from psycopg2 import connect, extensions, sql
import csv
import sys
import traceback
from io import StringIO
from datetime import datetime, timedelta
from zipfile import ZipFile
import logging
from postgres_login_info import login_info as postgres_login_info


logging.basicConfig(filename='logfile.log', level=logging.DEBUG)
logger = logging.getLogger(__name__)



# def test_db_connection(conn_info=connect_info):
#     with connect(conn_info) as conn, conn.cursor() as cur:
#         autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
#         conn.set_isolation_level(autocommit)

def query_postgres_db(query: str, ret: bool = False):
    """Query the master database.

    :param query: query to run
    :type query: str
    :param ret: if true, returns the results of the query as a dataframe
    :type ret: bool
    """

    conn = connect(dbname='postgres',
                 user=postgres_login_info['user'],
                 password=postgres_login_info['password'],
                 host=postgres_login_info['host'],
                 port=postgres_login_info['port'],
                 )
        #autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
        #conn.set_isolation_level(autocommit)
        #conn.autocommit = True
    conn.set_session(autocommit=True)
    with conn.cursor() as cur:
        query = sql.SQL(query)
        cur.execute(query)

        if ret:
            res = pd.DataFrame(cur.fetchall(), columns = [desc[0] for desc in cur.description])
    conn.close()
    if ret:
        return res


def create_f1_database():
    """Create the f1 database if it doesn't already exist"""

    ### check that the database doesn't already exist
    query = """SELECT datname FROM pg_database;"""
    databases = query_postgres_db(query, ret=True)
    databases = databases.datname.values

    if 'f1_stats' not in databases:
        logger.warn("f1_stats database not found, creating databse")
        create_query = """CREATE DATABASE f1_stats;"""
        query_postgres_db(create_query)
    else:
        logger.warn("f1_stats database found, doing nothing")

def main():
    create_f1_database()

if __name__ == '__main__':
    main()

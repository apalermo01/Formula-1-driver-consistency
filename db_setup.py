### initialize f1 database

import numpy as np
import pandas as pd
import os
import shutil
from datetime import datetime, timedelta
from zipfile import ZipFile
import logging
from postgres_login_info import login_info as postgres_login_info
from common import DatabaseConnector, load_query_from_file

logging.basicConfig(filename='logfile.log', level=logging.DEBUG)
logger = logging.getLogger(__name__)


connector = DatabaseConnector(postgres_login_info = postgres_login_info)

def create_f1_database():
    """Create the f1 database if it doesn't already exist"""

    ### check that the database doesn't already exist
    query = """SELECT datname FROM pg_database;"""
    databases = connector.execute_query(query, ret=True, dbname='postgres')
    databases = databases.datname.values

    if 'f1_stats' not in databases:
        logger.warning("f1_stats database not found, creating databse")
        create_query = """CREATE DATABASE f1_stats;"""
        connector.execute_query(create_query,
                                ret=False,
                                dbname='postgres',
                                no_transact=True)
    else:
        logger.warning("f1_stats database found, doing nothing")


if __name__ == '__main__':
    create_f1_database()
    create_tables_query = load_query_from_file("schema.sql")
    queries = create_tables_query.split(";")
    for q in queries:
        if len(q) == 0:
            continue
        query_to_execute = q + ";"
        connector.execute_query(query_to_execute)

import pandas as pd
from psycopg2 import connect, extensions, sql
from typing import Union, Dict

### constants
DBNAME = "f1-project"
DBUSER = 'postgres'

def load_query_from_file(fname: str) -> str:
    with open(fname, "r") as f:
        query = f.read()

    return query

class DatabaseConnector:

    def __init__(self,
            postgres_login_info: Dict,):
        self.login_info = postgres_login_info

    def execute_query(self,
                      query: str,
                      vars: Union[Dict, None] = None,
                      ret: bool = False,
                      no_transact: bool = False,
                      dbname: Union[str, None] = None) -> Union[None, pd.DataFrame]:
        """execute_query.

        Parameters
        ----------
        query : str
            query
        ret : bool
            ret
        dbname : Union[str, None]
            dbname
        """

        if dbname is None:
            dbname = self.login_info['dbname']

        if vars is None:
            vars = {}

        res = None
        conn = connect(dbname = dbname,
                       user = self.login_info['user'],
                       password = self.login_info['password'],
                       host = self.login_info['host'],
                       port = self.login_info['port'],)
        if no_transact:
            conn.autocommit = True

        try:
            with conn.cursor() as cur:
                query = sql.SQL(query )
                cur.execute(query, vars)

                if ret:
                        res = pd.DataFrame(cur.fetchall(),
                                  columns = [desc[0] for desc in cur.description])
                if not no_transact:
                    conn.commit()
                conn.close()
        except Exception as e:
            conn.close()
            raise e
        return res

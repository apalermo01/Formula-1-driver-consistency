import pandas as pd
from psycopg2 import connect, extensions
import subprocess

### constants
DBNAME = "f1-project"
DBUSER = 'postgres'

def start_postgres_service():
    """Start postgresql service"""

    

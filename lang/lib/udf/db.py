

import json
import pandas as pd
from sqlalchemy import create_engine
import psycopg2

ds = json.load(open("./resource/cfg/ds.json"))
def query(sql,db):
    connect = create_engine(ds[db])
    df = pd.read_sql(sql, connect)
    connect.dispose()
    return df

def hello():
    print("I'm fine")
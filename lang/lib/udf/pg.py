import json
import pandas as pd
from sqlalchemy import create_engine
import psycopg2


class Pg:
    def __init__(self, cfg):
        self.cfg = cfg
        self.ds = json.load(open(cfg))

    def query(self, sql, db):
        connect = create_engine(self.ds[db])
        df = pd.read_sql(sql, connect)
        connect.dispose()
        return df


import json
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import psycopg2
from abc import ABCMeta, abstractmethod


class Pg:
    def __init__(self, cfg):
        self.cfg = cfg
        self.ds = json.load(open(cfg))

    def query(self, sql, db):
        connect = create_engine(self.ds[db])
        df = pd.read_sql(sql, connect)
        connect.dispose()
        return df

    def queryall(self, idSeries, sb, db, eachSize=1000):
        ids = idSeries.to_numpy()
        count = int(ids.size / eachSize)
        subIds = np.array_split(ids, count)
        df = pd.DataFrame()
        for v in subIds:
            tmp = self.query(sb.sql(v.tolist()), db)
            df=pd.concat([df,tmp])
        return df


class ISubQ(metaclass=ABCMeta):
    @abstractmethod
    def sql(self, ids):
        raise NotImplementedError()

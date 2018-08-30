import os
import pandas as pd
import redis
import requests


#  CSVFILE = BASE_DIR + '/EQ060618_CSV/EQ060618.CSV'
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

r = redis.StrictRedis(host='localhost', port=6379, db=1)

def populate_data_into_redis(csv_file, date):
    self.df = pd.read_csv(csv_file)
    self.data = self.df.T.loc[['SC_CODE','SC_NAME','OPEN','HIGH', 'LOW', 'CLOSE']].to_dict()
    for d in self.data.values():
        code, nm = d.get('SC_CODE'), d.get('SC_NAME')
        key = '%s:%s' %(code, nm and nm.strip())
        r.hmset(key, d)


import os
import pandas as pd
import redis


BASE_DIR = os.path.dirname(os.path.realpath(__file__))

r = redis.StrictRedis(host="redis", port=6379, db=1)


def populate_data_into_redis(csv_file: str):
    df = pd.read_csv(csv_file)
    data = df.T.loc[["SC_CODE", "SC_NAME", "OPEN", "HIGH", "LOW", "CLOSE"]].to_dict()
    for d in data.values():
        code, nm = d.get("SC_CODE"), d.get("SC_NAME")
        key = f"{code}:{nm and nm.strip()}"
        r.hmset(key, d)

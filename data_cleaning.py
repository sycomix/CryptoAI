import pandas as pd
import datetime
import numpy as np


data = pd.read_csv("data/trade_data.csv")


def datetime_to_timestamp(date_str):
    year = int(date_str[:4])
    month = int(date_str[5:7])
    day = int(date_str[8:10])
    hour = int(date_str[11:13])
    minute = int(date_str[14:16])
    return datetime.datetime(year, month, day, hour, minute).timestamp()


data.drop("symbol", axis=1, inplace=True)
data["timestamp"] = data["timestamp"].map(arg=datetime_to_timestamp)
data["ohlc"] = (data["open"]+data["high"]+data["low"]+data["close"])/4

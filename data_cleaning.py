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


# Remove symbol column
data.drop("symbol", axis=1, inplace=True)

# Convert timestamp from string to timevalue integer
data["timestamp"] = data["timestamp"].map(arg=datetime_to_timestamp)

data["ohlc"] = (data["open"]+data["high"]+data["low"]+data["close"])/4

# Replace VWAP NaN values with OHLC
data["vwap"] = data["vwap"].fillna(value=data["ohlc"])

# Replace lastSize NaN values with 0
data["lastSize"] = data["lastSize"].fillna(value=0)

data.drop("vwap", axis=1, inplace=True)

data = data[["timestamp", "volume", "ohlc"]]
data_formats = {
    "2m": data.iloc[::2, :],
    "5m": data.iloc[::5, :],
    "15m": data.iloc[::15, :],
    "30m": data.iloc[::30, :],
    "1h": data.iloc[::60, :],
    "2h": data.iloc[::120, :],
    "3h": data.iloc[::180, :],
    "6h": data.iloc[::360, :],
    "12h": data.iloc[::720, :],
    "1d": data.iloc[::1440, :],
    "3d": data.iloc[::4320, :],
    "1w": data.iloc[::10080, :]}

for timedelta, dataset in data_formats.items():
    dataset.to_csv(path_or_buf=f"data/trades_{timedelta}.csv", index=False)

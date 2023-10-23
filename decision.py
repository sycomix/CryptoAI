import pandas as pd
import numpy as np
import os


def optimal_decision(dataframe):
    data = dataframe.copy()
    ohlc = data["ohlc"].values
    decision = np.zeros(len(ohlc))
    for i in range(len(decision) - 1):
        if ohlc[i + 1] > ohlc[i]:
            decision[i] = 1
        elif ohlc[i + 1] < ohlc[i]:
            decision[i] = 2
    data["decision"] = decision
    return data


for timedelta in os.listdir("./data/trades"):
    dataframe = pd.read_csv(f"./data/trades/{timedelta}")[
        ["timestamp", "volume", "ohlc", "decision"]
    ]
    dataframe = optimal_decision(dataframe)
    dataframe.to_csv(f"./data/trades/{timedelta}", index=False)

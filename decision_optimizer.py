import pandas as pd
import matplotlib.pyplot as plt
import random
import numpy as np
data = pd.read_csv("data/trades_1h.csv")

# Buy, Sell, Hold
decisions = [-1, 1, 0]

data["change"] = np.append(
    (data["ohlc"][1:].values-data["ohlc"][:-1].values), 0)


def optimal_solution(changes):
    decisions = []
    bought = False
    for i in range(len(changes)):
        if changes[i] > 0:
            # Buy, or hold if bought
            if bought:
                decisions.append(0)
            else:
                decisions.append(-1)
            bought = True

        elif changes[i] <= 0:
            # Sell, or hold if not bought
            if bought:
                decisions.append(1)
            else:
                decisions.append(0)
            bought = False
    return decisions


data["decisions"] = optimal_solution(data["change"])

data["profit"] = data["ohlc"]*data["decisions"]

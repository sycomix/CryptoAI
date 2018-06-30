import time
import csv
import os
import time
import datetime
from routes import get_trades_bucketed
from requests import Session
from config import API_ID

session = Session()

start_datetime = (datetime.datetime.fromtimestamp(int(time.time())))
file_name = f"{start_datetime.month}-{start_datetime.day}_{start_datetime.hour}{start_datetime.minute}"

# Initialize counter for console logging
request_count = 0
trades_start_count = 1

while True:
    # start_time for performance tracking
    start_time = time.time()

    # fetch trade data
    trade_data = get_trades_bucketed(
        session=session, count=500, start=trades_start_count, partial=True)
    trades_start_count += 500
    request_count += 1

    duration = round(1000*(time.time()-start_time))

    with open("data/6-30_132.csv", "a", newline="") as file_object:
        writer = csv.writer(file_object)
        # if request_count == 1:
        #     writer.writerow(trade_data[0].keys())
        writer.writerows([trade_data[x].values()
                          for x in range(len(trade_data))])
    current_datetime = datetime.datetime.fromtimestamp(round(start_time))
    print("Last trade datetime: {}, Request took : {} ms".format(
        trade_data[-1]['timestamp'], duration))
    time.sleep(2)

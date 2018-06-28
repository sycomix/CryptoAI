import time, csv, os, time, datetime
from routes import *
from requests import Session
from config import API_ID

session = Session()


def weighted_price(orderbook):
    # calculate total volume and total value:= SUM(Price_i * Volume_i)
    volume = sum([entry['size'] for entry in orderbook])
    value = sum([entry['price']*entry['size'] for entry in raw_orderbook])
    return round(value/volume,4)


# Write csv headers if file does not exist yet
if not (os.path.isfile("data/orderbook_depth1.csv")):
    with open("data/orderbook_depth1.csv","a",newline="") as file_object:
        writer = csv.writer(file_object)
        writer.writerow(['timestamp', 'size_Sell', 'price_Sell', 'size_Buy', 'price_Buy'])


# Initialize counter for console logging
request_count = 0


while True:
    # start_time for performance tracking
    start_time = time.time()

    # fetch orderbook, initialize with timestamp
    raw_orderbook = get_orderbook(session)
    orderbook = {"timestamp":round(time.time())}

    # duration for performance tracking
    duration = round(1000*(time.time()-start_time))

    # update orderbook with buy/sell side data
    for entry in raw_orderbook:
        orderbook["size_"+entry["side"]]=entry["size"]
        orderbook["price_"+entry["side"]]=entry["price"]

    # calculate weighted price for console logging
    price = weighted_price(raw_orderbook)

    with open("data/orderbook_depth1.csv","a",newline="") as file_object:
        writer = csv.writer(file_object)
        writer.writerow(orderbook.values())
    
    request_count+=1
    if request_count%720==0:
        current_datetime = datetime.datetime.fromtimestamp(round(start_time))
        print("{}, Price: {}, Request took : {} ms".format(current_datetime, price, duration))
    time.sleep(5)







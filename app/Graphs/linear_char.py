import random
import radar

import datetime

import numpy as np
import pandas as pd


def generate_data(n: int, start: datetime, end: datetime):
    listdata = []
    str_start = start.strftime('%Y-%m-%d')
    str_end = end.strftime('%Y-%m-%d')
    delta = end - start
    for _ in range(n):
        date = radar.random_datetime(start=str_start, stop=str_end).strftime("%Y-%m-%d")
        price = round(random.uniform(900, 1000), 4)
        listdata.append([date, price])

    # Create dataframe from listdata add columns date and price
    df = pd.DataFrame(listdata, columns=['Date', 'Price'])
    # Convert date in type datetime
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
    df = df.groupby(by='Date').mean()

    return df


def load_data():
    start = datetime.datetime(2019, 8, 1)
    end = datetime.datetime(2019, 8, 30)

    return generate_data(50,start,end)



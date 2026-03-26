from datetime import datetime, timedelta

import pandas as pd
from matplotlib import dates as mpl_dates
from matplotlib import pyplot as plt

plt.style.use("seaborn-v0_8-dark")

dates = [
    datetime(2019, 5, 24),
    datetime(2019, 5, 25),
    datetime(2019, 5, 26),
    datetime(2019, 5, 27),
    datetime(2019, 5, 28),
    datetime(2019, 5, 29),
    datetime(2019, 5, 30),
]

#  dates = pd.to_datetime(dates)
dates = mpl_dates.date2num(dates)

y = [0, 1, 3, 4, 6, 5, 7]

plt.plot_date(dates, y, linestyle="solid")

plt.gcf().autofmt_xdate()

date_format = mpl_dates.DateFormatter("%b, %d %Y")

plt.gca().xaxis.set_major_formatter(date_format)

# data = pd.read_csv('data_time_series.csv')
# price_date = data['Date']
# price_close = data['Close']

# plt.title('Bitcoin Prices')
# plt.xlabel('Date')
# plt.ylabel('Closing Price')

plt.tight_layout()

plt.show()

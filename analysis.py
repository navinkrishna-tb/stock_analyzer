
import pandas_datareader.data as web
import datetime as dt
from datetime import date
#import matplotlib.pyplot as plt
from matplotlib import rcParams
import plotly.express as px





start = dt.datetime(2020,1,1)
end = date.today()
def get_stock():
    tick = input("Enter the ticker :")
    tick = tick+".ns"
    tick = tick.upper()
    df = web.DataReader(tick,'yahoo',start,end)
    return df





def moving_average(df):
    ma_day = [15, 30, 45]

    for ma in ma_day:
            column_name = f"MA for {ma} days"
            df[column_name] = df["Adj Close"].rolling(ma).mean()
    return df





df = get_stock()
ma_df = moving_average(df)





ma_df.dropna(inplace=True)


# In[29]:

#### MOVING AVERAGE  ######
'''
rcParams["figure.figsize"] = 15,5
plt.plot(ma_df["MA for 15 days"], label="15 day")
plt.plot(ma_df["MA for 30 days"], label="30 day")
plt.plot(ma_df["MA for 45 days"], label="45 day")
plt.legend()
plt.show()


'''
##################################################

from returns import returns

returns(ma_df)



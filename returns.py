import matplotlib.pyplot as plt
from matplotlib import rcParams
import pandas as pd

def returns(df):
    rcParams["figure.figsize"] = 15,5
    period = int(input("Enter no of period:"))
    column_name = f"pct_change {period} days"
    df[column_name] = df["Close"].pct_change(periods=period)
    df.dropna(inplace=True)
    df[column_name].plot()
    plt.axhline(y=0,color="black")
    return plt.show()
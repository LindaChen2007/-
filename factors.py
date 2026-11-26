import pandas as pd

VOL_RATIO_MIN = 1.2

def add_signal(df):
    df = df.copy()
    df["ma20"] = df["收盘"].rolling(20).mean()
    df["vol_ma5"] = df["成交量"].rolling(5).mean()
    df["vol_ratio"] = df["成交量"] / df["vol_ma5"]
    df["昨收"] = df["收盘"].shift(1)
    df["昨MA20"] = df["ma20"].shift(1)
    df["放量"] = df["vol_ratio"] > VOL_RATIO_MIN
    df["信号"] = (
        (df["昨收"] < df["昨MA20"]) &
        (df["收盘"] > df["ma20"]) &
        df["放量"]
    )
    return df
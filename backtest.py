import pandas as pd

def backtest(sig_df, fee=0.0003):
    sig_df = sig_df.reset_index(drop=True)
    rows = []
    for i in range(len(sig_df) - 2):
        if sig_df.loc[i, "信号"]:
            buy = sig_df.loc[i + 1, "开盘"]
            sell = sig_df.loc[i + 2, "开盘"]
            ret = (sell - buy) / buy - fee * 2
            rows.append({
                "信号日": sig_df.loc[i, "日期"],
                "买入日": sig_df.loc[i + 1, "日期"],
                "买入价": buy,
                "卖出价": sell,
                "收益率": ret,
                "股票": sig_df.loc[i, "股票"],
                "代码": sig_df.loc[i, "代码"],
            })
    return pd.DataFrame(rows)
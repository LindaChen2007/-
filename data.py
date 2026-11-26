import akshare as ak

START = "20230101"
END = "20241231"

def fetch_data(code):
    return ak.stock_zh_a_hist(
        symbol=code,
        period="daily",
        start_date=START,
        end_date=END,
        adjust="qfq"
    )
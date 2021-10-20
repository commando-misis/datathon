from datetime import datetime
from dateutil.relativedelta import relativedelta


def convert_binance_time_to_normal(time: int) -> str:
    return (datetime.fromtimestamp(time/1000) - relativedelta(hours=3)).strftime('%Y-%m-%d %H:%M:%S')


def convert_normal_time_to_binance(time: str) -> int:
    return int((datetime.strptime(time, '%Y-%m-%d %H:%M:%S') - relativedelta(hours=3)).timestamp() * 1000)

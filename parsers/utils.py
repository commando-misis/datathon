from datetime import datetime, timedelta


def convert_binance_time_to_normal(timestamp: int) -> str:
    return (datetime.fromtimestamp(timestamp/1000) - timedelta(hours=3)).strftime('%Y-%m-%d')


def convert_normal_time_to_binance(date: str) -> int:
    return int((datetime.strptime(date, '%Y-%m-%d') - timedelta(hours=3)).timestamp() * 1000)


def minus_one_day(date: str) -> str:
    return (datetime.strptime(date, '%Y-%m-%d') - timedelta(days=1)).strftime('%Y-%m-%d')


def add_one_day(date: str) -> str:
    return (datetime.strptime(date, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')


def get_days_count(date_from: str, date_to: str) -> int:
    dates_diff = datetime.strptime(date_to, '%Y-%m-%d') - datetime.strptime(date_from, '%Y-%m-%d')
    return dates_diff.days + 1

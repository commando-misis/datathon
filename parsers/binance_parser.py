import requests

from urllib.parse import urlencode
from parsers.utils import convert_binance_time_to_normal, convert_normal_time_to_binance


def get_currency_data(currency_code: str, year: int) -> [dict]:
    request_url = 'https://api.binance.com/api/v3/klines?'

    year_start = str(year) + '-01-01 00:00:00'
    year_end = str(year + 1) + '-01-01 00:00:00'

    request_params = {
        'symbol': currency_code + 'USDT',
        'interval': '1d',
        'startTime': convert_normal_time_to_binance(year_start),
        'endTime': convert_normal_time_to_binance(year_end)
    }

    response = requests.get(request_url + urlencode(request_params))

    if response.status_code != 200:
        print(response.text)
        return None

    result = []
    for day_data in response.json():
        date = convert_binance_time_to_normal(day_data[0])
        price = day_data[4]

        result.append({
            'date': date,
            currency_code: price
        })

    return result

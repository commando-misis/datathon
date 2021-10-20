import requests

from urllib.parse import urlencode
from parsers.utils import convert_binance_time_to_normal, convert_normal_time_to_binance


def get_currency_data(currency_code: str, date_from: str, date_to: str) -> [dict] or None:
    request_url = 'https://api.binance.com/api/v3/klines?'

    request_params = {
        'symbol': currency_code + 'USDT',
        'interval': '1d',
        'startTime': convert_normal_time_to_binance(date_from),
        'endTime': convert_normal_time_to_binance(date_to)
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
            currency_code + '_price_USD': price
        })

    return result

import requests

from urllib.parse import urlencode
from parsers.utils import minus_one_day


def get_currency_id(currency_code: str) -> int or None:
    request_url = f'https://web-api.coinmarketcap.com/v1/cryptocurrency/map?symbol={currency_code}'
    response = requests.get(request_url)

    if response.status_code == 200:
        response_data = response.json()
        if len(response_data['data']) > 0:
            return response_data['data'][0]['id']

    return None


def get_currency_data(currency_code: str, date_from: str, date_to: str, convert_list: [str] = None) -> [dict] or None:
    if convert_list is None:
        convert_list = ['USD']

    currency_id = get_currency_id(currency_code)

    if currency_id is None:
        return None

    request_url = 'https://web-api.coinmarketcap.com/v1/cryptocurrency/ohlcv/historical?'
    request_params = {
        'id': currency_id,
        'convert': ','.join(convert_list),
        'time_start': minus_one_day(date_from),
        'time_end': date_to
    }

    response = requests.get(request_url + urlencode(request_params))

    if response.status_code != 200:
        print(response.text)
        return None

    result = []
    for day_data in response.json()['data']['quotes']:

        result_dict = {
            'date': day_data['time_open'].split('T')[0]
        }

        for convert in convert_list:
            result_dict[currency_code + '_price_' + convert] = day_data['quote'][convert]['close']
            result_dict[currency_code + '_volume_' + convert] = day_data['quote'][convert]['volume']
            result_dict[currency_code + '_market_cap_' + convert] = day_data['quote'][convert]['market_cap']

        result.append(result_dict)

    return result

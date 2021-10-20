import requests

from urllib.parse import urlencode


def get_currency_id(currency_code: str) -> int or None:
    request_url = f'https://web-api.coinmarketcap.com/v1/cryptocurrency/map?symbol={currency_code}'
    response = requests.get(request_url)

    if response.status_code == 200:
        response_data = response.json()
        if len(response_data['data']) > 0:
            return response_data['data'][0]['id']

    return None


def get_currency_data(currency_code: str, year: int) -> [dict] or None:
    currency_id = get_currency_id(currency_code)

    if currency_id is None:
        return None

    request_url = 'https://web-api.coinmarketcap.com/v1/cryptocurrency/ohlcv/historical?'
    request_params = {
        'id': currency_id,
        'convert': 'USD',
        'time_start': str(year) + '-01-01',
        'time_end': str(year) + '-12-31'
    }

    response = requests.get(request_url + urlencode(request_params))

    if response.status_code != 200:
        print(response.text)
        return None

    result = []
    for day_data in response.json()['data']['quotes']:
        result.append({
            'date': day_data['time_open'].replace('T', ' ').replace('.000Z', ''),
            currency_code: day_data['quote']['USD']['close']
        })

    return result

import requests

from urllib.parse import urlencode
from datetime import datetime, timedelta
from time import sleep
from parsers.utils import get_days_count, add_one_day
from config import currency_codes_x_names_dict


def get_reddit_mentions(currency_code: str, date_from: str, date_to: str) -> [dict]:
    request_url = 'https://api.pushshift.io/reddit/comment/search/?'

    # iterations by day
    result = []
    for date in (datetime.strptime(date_from, '%Y-%m-%d') + timedelta(days)
                 for days in range(get_days_count(date_from, date_to))):

        date_str = date.strftime('%Y-%m-%d')

        request_params = {
            'q': currency_codes_x_names_dict[currency_code],
            'after': date_str,
            'before': add_one_day(date_str),
            'metadata': True,
            'size': 0
        }

        # limit for api.pushshift.io is 200 requests per minute
        # that means we should use at least 0.3 sec timeout between requests
        # but empirically we can see 0.3 sec is not enough and some of requests getting 429 status
        # set sleep to 0.5 sec to minimize 429 errors
        response = requests.get(request_url + urlencode(request_params))
        sleep(0.5)

        if response.status_code != 200:
            print(response.status_code)
            result.append({
                'date': date_str,
                currency_code + '_reddit_mentions': None
            })
        else:
            result.append({
                'date': date_str,
                currency_code + '_reddit_mentions': response.json()['metadata']['total_results']
            })

    return result

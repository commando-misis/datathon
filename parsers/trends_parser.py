import pandas as pd

from pytrends import dailydata
from datetime import datetime
from config import currency_codes_x_names_dict


def get_trends_values(currency_code: str, date_from: str, date_to: str) -> pd.DataFrame:
    date_from = datetime.strptime(date_from, '%Y-%m-%d')
    date_to = datetime.strptime(date_to, '%Y-%m-%d')
    keyword = currency_codes_x_names_dict[currency_code]

    trends_df = dailydata.get_daily_data(
        keyword,
        start_year=date_from.year,
        start_mon=date_from.month,
        stop_year=date_to.year,
        stop_mon=date_to.month,
        geo='',
        wait_time=10.0  # from docs: don't go too fast or Google will send 429s
    )

    trends_df.drop(labels=['isPartial', 'scale', keyword + '_monthly', keyword + '_unscaled'], axis=1, inplace=True)
    trends_df.reset_index(inplace=True)
    trends_df.rename(columns={keyword: currency_code + '_google_trends'}, inplace=True)
    trends_df['date'] = trends_df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))

    return trends_df

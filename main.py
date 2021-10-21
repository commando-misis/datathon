import os
import pandas as pd

from parsers import coinmarketcap_parser
from glob import glob
from datetime import datetime, timedelta
from config import *


def save_df_to_csv(df: pd.DataFrame, filename: str) -> None:
    df.to_csv(filename, index=False)


# now uses coinmarketcup data
def create_currencies_datasets(
        currency_codes: [str],
        date_from: str,
        date_to: str,
        convert_codes: [str] = None
) -> None:

    if convert_codes is None:
        convert_codes = ['USD']

    for currency in currency_codes:
        currency_df = pd.DataFrame()
        currency_data = coinmarketcap_parser.get_currency_data(currency, date_from, date_to, convert_codes)
        if currency_data is not None:
            currency_df = currency_df.append(pd.DataFrame(currency_data), ignore_index=True)

        filename = 'data/coinmarketcap_' + currency + '_' + date_from + '_' + date_to + '.csv'
        save_df_to_csv(currency_df, filename)


if not os.path.exists('data'):
    os.makedirs('data')

create_currencies_datasets(global_currency_codes, global_date_from, global_date_to, global_convert_codes)


final_df = pd.DataFrame(columns=['date'])
dates_diff = datetime.strptime(global_date_to, '%Y-%m-%d') - datetime.strptime(global_date_from, '%Y-%m-%d')
dates = [
    datetime.strptime(global_date_from, '%Y-%m-%d') + timedelta(days=x)
    for x in range(dates_diff.days + 1)
]
final_df['date'] = dates

for dataset_file in glob('data/coinmarketcap_*.csv'):
    tmp_df = pd.read_csv(dataset_file)
    if not tmp_df.empty:
        tmp_df['date'] = pd.to_datetime(tmp_df['date'], format='%Y-%m-%d')
        final_df = final_df.merge(tmp_df, how='left', on='date')

save_df_to_csv(final_df, 'data/final_' + global_date_from + '_' + global_date_to + '.csv')

import os
import pandas as pd

from parsers import coinmarketcap_parser
from glob import glob
from datetime import datetime, timedelta


global_currency_codes = ['BTC', 'ETH', 'BNB', 'ADA', 'USDT', 'XRP', 'SOL']
global_convertation_codes = ['USD', 'RUB', 'BTC']
global_date_from = '2020-05-01'
global_date_to = '2020-05-31'


def save_df_to_csv(df: pd.DataFrame, filename: str) -> None:
    df.to_csv(filename, index=False)


# now uses coinmarketcup data
def create_currencies_datasets(
        currency_codes: [str],
        date_from: str,
        date_to: str,
        convertation_codes: [str] = ['USD']
) -> None:

    for currency in currency_codes:
        for convertation in convertation_codes:
            currency_df = pd.DataFrame()
            currency_year_data = coinmarketcap_parser.get_currency_data(currency, date_from, date_to, convertation)
            if currency_year_data is not None:
                current_year_df = pd.DataFrame(currency_year_data)
                currency_df = currency_df.append(current_year_df, ignore_index=True)
            filename = 'data/coinmarketcap_' + currency + '_' + convertation + '_' + date_from + '_' + date_to + '.csv'
            save_df_to_csv(currency_df, filename)


if not os.path.exists('data'):
    os.makedirs('data')

create_currencies_datasets(global_currency_codes, global_date_from, global_date_to, global_convertation_codes)


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

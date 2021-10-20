import pandas as pd

from parsers import binance_parser, coinmarketcap_parser


global_currency_codes = ['BTC', 'ETH']


def save_df_to_csv(df: pd.DataFrame, filename: str) -> None:
    df.to_csv(filename)


def create_currencies_datasets(currency_codes: [str], year_from: int, year_to: int) -> None:
    for currency in currency_codes:
        currency_df = pd.DataFrame()

        for year in range(year_from, year_to + 1):
            currency_year_data = coinmarketcap_parser.get_currency_data(currency, year)
            if currency_year_data is not None:
                current_year_df = pd.DataFrame(currency_year_data)
                currency_df = currency_df.append(current_year_df, ignore_index=True
                                                 )
        save_df_to_csv(currency_df, 'data/' + currency + '_' + str(year_from) + '-' + str(year_to) + '.csv')


create_currencies_datasets(global_currency_codes, 2015, 2021)

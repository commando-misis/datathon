import pandas as pd

from parsers import binance_parser, coinmarketcap_parser


global_currency_codes = ['BTC', 'ETH']
global_convertation_codes = ['USD', 'RUB', 'BTC']


def save_df_to_csv(df: pd.DataFrame, filename: str) -> None:
    df.to_csv(filename)


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


create_currencies_datasets(global_currency_codes, '2020-01-01', '2020-01-31', global_convertation_codes)

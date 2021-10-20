from parsers import binance_parser


currency_codes = ['BTC', 'ETH']

print(binance_parser.get_currency_data('BTC', 2020))

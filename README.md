# Исторические данные о цене криптовалют и их упоминаниях в социальных сетях
## Команда «Commando»
Состав: Протасов Егор, Ершов Иван, Шишканов Георгий, Катюшин Илья, Барков Вячеслав, Смирнов Александр, Недоливко Алексей

## Описание датасета
В датасете содержится информация об исторических курсах криптовалют и их упоминаниях в социальных сетях. Данные в датасете представлены в виде файла .csv.
Датасет может быть использован для анализа рынка криптовалют, включая построение финансовых моделей, принятие долгосрочных и краткосрочных инвестиционных решений, анализ зависимостей пар криптовалют, корелляция популярности валюты с ее курсом.

## Источники
В датасете используются следующие источники:
* [Binance API](https://binance-docs.github.io/apidocs/spot/en/#change-log)
* [Coinmarketcap API](https://coinmarketcap.com/api/)
* [Twitter API](https://developer.twitter.com/en/docs)

## Методы сбора и обработки
В качестве основы датасета были взяты данные, полученные при использовании Coinmarketcap API. Собраны данные за последние несколько лет по семи криптовалютам с наибольшей капитализацией на момент сбора данных, а именно:  Bitcoin, Ethereum, Binance Coin, Cardano, Tether, XRP, Solana. Данные включают в себя цену закрытия в рублях, долларах и относительно Bitcoin, как самой крупной криптовалюты. Также включены объем торгов, объем капитализации в рублях и долларах. Собраны данные о количествах упоминаний валют в Twitter используя Twitter API. Данные собраны и объединены в единый датасет.

## Структура датасета
Датасет находится в репозитории Github и называется dataset.csv.
[Ссылка на файл в репозитории](dataset.csv)

|№| **Название** | **Описание** | **Тип** |
| ------ | ------ | ------ | ------ | 
| 1 | **date** | Дата торгов | datetime |
| 2 | **BTC_price_USD** | Цена Bitcoin к закрытию торгов в долларах США| float |
| 3 | **BTC_price_RUB** | Цена Bitcoin к закрытию торгов в рублях | float |
| 4 | **BTC_price_BTC** | Цена Bitcoin к закрытию торгов в Bitcoin | float |
| 5 | **BTC_volume** | Объем торгов | float |
| 6 | **BTC_market_cap_USD** | Капитализация Bitcoin в долларах США | float |
| 7 | **BTC_market_cap_RUB** | Капитализация Bitcoin в долларах США | float |
| 8 | **BTC_twitter_mentions** | Количество упоминаний в Twitter | int |
| 9 | **ETH_price_USD** | Цена Ethereum к закрытию торгов в долларах США| float |
| 10 | **ETH_price_RUB** | Цена Ethereum к закрытию торгов в рублях | float |
| 11 | **ETH_price_BTC** | Цена Ethereum к закрытию торгов в Bitcoin | float |
| 12 | **ETH_volume** | Объем торгов | float |
| 13 | **ETH_market_cap_USD** | Капитализация Ethereum в долларах США | float |
| 14 | **ETH_market_cap_RUB** | Капитализация Ethereum в долларах США | float |
| 15 | **ETH_twitter_mentions** | Количество упоминаний в Twitter | int |
| 16 | **BNB_price_USD** | Цена Binance Coin к закрытию торгов в долларах США| float |
| 17 | **BNB_price_RUB** | Цена Binance Coin к закрытию торгов в рублях | float |
| 18 | **BNB_price_BTC** | Цена Binance Coin к закрытию торгов в Bitcoin | float |
| 19 | **BNB_volume** | Объем торгов | float |
| 20 | **BNB_market_cap_USD** | Капитализация Binance Coin в долларах США | float |
| 21 | **BNB_market_cap_RUB** | Капитализация Binance Coin в долларах США | float |
| 22 | **BNB_twitter_mentions** | Количество упоминаний в Twitter | int |
| 23 | **ADA_price_USD** | Цена Cardano к закрытию торгов в долларах США| float |
| 24 | **ADA_price_RUB** | Цена Cardano к закрытию торгов в рублях | float |
| 25 | **ADA_price_BTC** | Цена Cardano к закрытию торгов в Bitcoin | float |
| 26 | **ADA_volume** | Объем торгов | float |
| 27 | **ADA_market_cap_USD** | Капитализация Cardano в долларах США | float |
| 28 | **ADA_market_cap_RUB** | Капитализация Cardano в долларах США | float |
| 29 | **ADA_twitter_mentions** | Количество упоминаний в Twitter | int |
| 30 | **USDT_price_USD** | Цена Tether к закрытию торгов в долларах США| float |
| 31 | **USDT_price_RUB** | Цена Tether к закрытию торгов в рублях | float |
| 32 | **USDT_price_BTC** | Цена Tether к закрытию торгов в Bitcoin | float |
| 33 | **USDT_volume** | Объем торгов | float |
| 34 | **USDT_market_cap_USD** | Капитализация Tether в долларах США | float |
| 35 | **USDT_market_cap_RUB** | Капитализация Tether в долларах США | float |
| 36 | **USDT_twitter_mentions** | Количество упоминаний в Twitter | int |
| 37 | **XRP_price_USD** | Цена XRP к закрытию торгов в долларах США| float |
| 38 | **XRP_price_RUB** | Цена XRP к закрытию торгов в рублях | float |
| 39 | **XRP_price_BTC** | Цена XRP к закрытию торгов в Bitcoin | float |
| 40 | **XRP_volume** | Объем торгов | float |
| 41 | **XRP_market_cap_USD** | Капитализация XRP в долларах США | float |
| 42 | **XRP_market_cap_RUB** | Капитализация XRP в долларах США | float |
| 43 | **XRP_twitter_mentions** | Количество упоминаний в Twitter | int |
| 44 | **SOL_price_USD** | Цена Solana к закрытию торгов в долларах США| float |
| 45 | **SOL_price_RUB** | Цена Solana к закрытию торгов в рублях | float |
| 46 | **SOL_price_BTC** | Цена Solana к закрытию торгов в Bitcoin | float |
| 47 | **SOL_volume** | Объем торгов | float |
| 48 | **SOL_market_cap_USD** | Капитализация Solana в долларах США | float |
| 49 | **SOL_market_cap_RUB** | Капитализация Solana в долларах США | float |
| 50 | **SOL_twitter_mentions** | Количество упоминаний в Twitter | int |
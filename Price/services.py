import requests
from django.core.cache import cache

def get_price(currency, nobitex_data, tgju_data):

    if currency.source == "nobitex":

        market = f"{currency.symbol}-rls"
        price = nobitex_data.get(market)

        if not price:
            return None

        return {
            "name": currency.name,
            "symbol": currency.symbol,
            "latest": price["latest"],
            "bestBuy": price["bestBuy"],
            "bestSell": price["bestSell"],
            "dayChange": price["dayChange"],
        }

    if currency.source == "tgju":

        price = tgju_data.get(currency.symbol)

        if not price:
            return None

        return {
            "name": currency.name,
            "symbol": currency.symbol,
            "latest": price["p"],
            "bestBuy": None,
            "bestSell": None,
            "dayChange": price["dp"],
        }

    return None


def get_price_detail(currency):

    if currency.source == "nobitex":

        data = get_nobitex_stats()

        market = f"{currency.symbol}-rls"
        price = data.get(market)

        if not price:
            return None

        return {
            "name": currency.name,
            "symbol": currency.symbol,
            "latest": price["latest"],
            "bestBuy": price["bestBuy"],
            "bestSell": price["bestSell"],
            "dayChange": price["dayChange"],
            "dayLow": price["dayLow"],
            "dayHigh": price["dayHigh"],
            "dayOpen": price["dayOpen"],
        }

    if currency.source == "tgju":

        data = get_tgju_stats([currency.symbol])
        price = data.get(currency.symbol)

        if not price:
            return None

        return {
            "name": currency.name,
            "symbol": currency.symbol,
            "latest": price["p"],
            "bestBuy": None,
            "bestSell": None,
            "dayChange": price["dp"],
            "dayLow": price["l"],
            "dayHigh": price["h"],
            "dayOpen": price["o"],
        }

    return None


def get_nobitex_stats():

    cache_key = "nobitex_stats"
    data = cache.get(cache_key)

    if data is not None:
        return data

    response = requests.get(
        "https://apiv2.nobitex.ir/market/stats",
        timeout=10
    )

    response.raise_for_status()

    data = response.json()["stats"]

    cache.set(cache_key, data, 10)

    return data

def get_tgju_stats(keys):
    cache_key = f"tgju_stats:{','.join(sorted(keys))}"
    data = cache.get(cache_key)
    if data is not None:
        return data
    response = requests.get(
        "https://api.tgju.org/v1/widget/tmp",
        params={"keys": ",".join(keys)},
        timeout=10
    )

    response.raise_for_status()

    indicators = response.json()["response"]["indicators"]

    data = {
        item["name"]: item
        for item in indicators
    }
    cache.set(cache_key, data, 10)
    return data
import httpx

BASE_URL = "https://api.coingecko.com/api/v3"


def search_coin(query: str):
    url = f"{BASE_URL}/search"

    params = {
        "query": query
    }

    response = httpx.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    return data["coins"][:5]


def get_market_data(coin_id: str):
    url = f"{BASE_URL}/coins/markets"

    params = {
        "vs_currency": "usd",
        "ids": coin_id,
    }

    response = httpx.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    if not data:
        return None

    return data[0]


def get_price_history(coin_id: str, days: int = 30):
    url = f"{BASE_URL}/coins/{coin_id}/market_chart"

    params = {
        "vs_currency": "usd",
        "days": days,
    }

    response = httpx.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    return data["prices"]
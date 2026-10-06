import pandas as pd


def calculate_market_metrics(market_data: dict):
    return {
        "current_price": market_data["current_price"],
        "market_cap": market_data["market_cap"],
        "market_cap_rank": market_data["market_cap_rank"],
        "change_24h": market_data["price_change_percentage_24h"],
    }


def analyze_price_history(prices: list):
    # Convert CoinGecko price data into a DataFrame
    df = pd.DataFrame(
        prices,
        columns=["timestamp", "price"]
    )

    # Convert timestamp to datetime
    df["date"] = pd.to_datetime(
        df["timestamp"],
        unit="ms"
    )

    # Create daily price data
    daily_df = (
        df.set_index("date")
        .resample("1D")
        .last()
        .dropna()
        .reset_index()
    )

    # Start and end prices
    start_price = daily_df["price"].iloc[0]
    end_price = daily_df["price"].iloc[-1]

    # 30-day return
    return_30d = (
        (end_price - start_price)
        / start_price
        * 100
    )

    # Daily percentage returns
    daily_df["daily_return"] = (
        daily_df["price"].pct_change()
    )

    # Daily volatility during the 30-day period
    volatility_30d = (
        daily_df["daily_return"].std()
        * 100
    )

    metrics = {
        "return_30d": return_30d,
        "high_30d": daily_df["price"].max(),
        "low_30d": daily_df["price"].min(),
        "volatility_30d": volatility_30d,
        "start_price": start_price,
    }

    return daily_df, metrics


def calculate_position_metrics(
    holdings: float,
    current_price: float,
    start_price: float
):
    current_value = holdings * current_price
    start_value = holdings * start_price

    value_change_30d = (
        current_value - start_value
    )

    return {
        "current_value": current_value,
        "value_change_30d": value_change_30d,
    }
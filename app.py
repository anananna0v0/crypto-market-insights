import streamlit as st
import plotly.express as px

from services.coingecko import (
    search_coin,
    get_market_data,
    get_price_history,
)

from analysis.market_analysis import (
    calculate_market_metrics,
    analyze_price_history,
    calculate_position_metrics,
)


st.title("Crypto Market Insights")


# -------------------------
# User Input
# -------------------------

token = st.text_input(
    "Token symbol",
    placeholder="e.g. BTC, ETH, SOL"
)

holdings = st.number_input(
    "Holdings (optional)",
    min_value=0.0,
    value=0.0,
    step=0.1
)


if token:
    coins = search_coin(token)

    if not coins:
        st.warning("No matching token found.")

    else:
        options = {
            f"{coin['name']} ({coin['symbol'].upper()})": coin["id"]
            for coin in coins
        }

        selected_label = st.selectbox(
            "Select the token",
            options.keys()
        )

        selected_id = options[selected_label]

        if st.button("Analyze"):

            # -------------------------
            # Get data from CoinGecko
            # -------------------------

            market_data = get_market_data(
                selected_id
            )

            prices = get_price_history(
                selected_id
            )

            # -------------------------
            # Data Analysis
            # -------------------------

            metrics = calculate_market_metrics(
                market_data
            )

            price_df, history_metrics = (
                analyze_price_history(prices)
            )

            # -------------------------
            # Market Overview
            # -------------------------

            st.subheader("Market Overview")

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Current Price",
                f"${metrics['current_price']:,.2f}"
            )

            col2.metric(
                "Market Cap",
                f"${metrics['market_cap']:,.0f}"
            )

            col3.metric(
                "24h Change",
                f"{metrics['change_24h']:.2f}%"
            )

            st.write(
                "Market Cap Rank:",
                metrics["market_cap_rank"]
            )

            # -------------------------
            # 30-Day Analysis
            # -------------------------

            st.subheader("30-Day Analysis")

            col1, col2, col3, col4 = (
                st.columns(4)
            )

            col1.metric(
                "30-Day Return",
                f"{history_metrics['return_30d']:.2f}%"
            )

            col2.metric(
                "30-Day High",
                f"${history_metrics['high_30d']:,.2f}"
            )

            col3.metric(
                "30-Day Low",
                f"${history_metrics['low_30d']:,.2f}"
            )

            col4.metric(
                "Daily Volatility",
                f"{history_metrics['volatility_30d']:.2f}%"
            )

            # -------------------------
            # Position Analysis
            # -------------------------

            if holdings > 0:

                position = (
                    calculate_position_metrics(
                        holdings,
                        metrics["current_price"],
                        history_metrics["start_price"]
                    )
                )

                st.subheader("Your Position")

                col1, col2, col3 = (
                    st.columns(3)
                )

                col1.metric(
                    "Holdings",
                    (
                        f"{holdings:g} "
                        f"{market_data['symbol'].upper()}"
                    )
                )

                col2.metric(
                    "Current Value",
                    f"${position['current_value']:,.2f}"
                )

                col3.metric(
                    "30-Day Value Change",
                    (
                        f"${position['value_change_30d']:,.2f}"
                    )
                )

            # -------------------------
            # Data Visualization
            # -------------------------

            st.subheader(
                "30-Day Price Trend"
            )

            fig = px.line(
                price_df,
                x="date",
                y="price",
                labels={
                    "date": "Date",
                    "price": "Price (USD)"
                }
            )

            fig.update_layout(
                xaxis_title="Date",
                yaxis_title="Price (USD)"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )
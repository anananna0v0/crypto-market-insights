```markdown
# Crypto Market Insights

An interactive cryptocurrency market analysis application built with Python and Streamlit.

🔗 **Live Demo:** https://crypto-market-insights-189425757048.europe-west3.run.app/

## Overview

Crypto Market Insights retrieves real-time and historical cryptocurrency data from the CoinGecko REST API and transforms it into interactive market insights.

Users can search for a cryptocurrency, analyze recent market performance, and evaluate the value of their holdings.

## Features

- Search and select cryptocurrencies
- Retrieve market data through the CoinGecko REST API
- Analyze 30-day price performance
- Calculate return, high, low, and daily volatility
- Analyze cryptocurrency holdings and value changes
- Visualize historical price trends interactively

## Tech Stack

- **Python**
- **Streamlit**
- **Pandas**
- **Plotly**
- **httpx**
- **REST API**
- **Docker**
- **Google Cloud Run**

## Architecture

```text
User
  ↓
Streamlit
  ↓
CoinGecko REST API
  ↓
Data Analysis
  ↓
Interactive Visualization
```

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Docker

Build the Docker image:

```bash
docker build -t crypto-market-insights .
```

Run the container:

```bash
docker run -p 8080:8080 -e PORT=8080 crypto-market-insights
```

Then open:

```text
http://localhost:8080
```

## Deployment

The application is deployed on **Google Cloud Run** using a Docker container.
```
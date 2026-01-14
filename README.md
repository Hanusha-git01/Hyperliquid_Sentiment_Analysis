# Analysis of Trader Behavior vs. Market Sentiment (Hyperliquid)

## Project Overview
This project explores the relationship between market sentiment (Bitcoin Fear & Greed Index) and the actual performance of traders on the Hyperliquid exchange. By analyzing over 184,000 trade logs, this study identifies how emotional market cycles influence profitability and trading frequency.

## Key Insights
* **Peak Profitability:** Trading during "Greed" cycles resulted in the highest average PnL ($87.89), outperforming "Fear" cycles by ~75%.
* **Volume Paradox:** The highest volume of trades occurred during "Fear" regimes (over 133k trades), yet these trades were significantly less profitable on average than those in "Greed" regimes.
* **Neutral Deadzone:** Performance was at its lowest during "Neutral" market sentiment, suggesting that traders struggle to find edge in non-trending markets.

## Technical Implementation
* **Data Cleaning:** Handled high-precision Unix timestamps (microseconds to datetime conversion).
* **Data Integration:** Performed a temporal join between high-frequency trade data and daily sentiment metrics.
* **Exploratory Data Analysis (EDA):** Used Pandas for aggregation and Seaborn/Matplotlib for trend visualization.

## How to Run
1. Ensure `historical_trader_data.csv` and `bitcoin_sentiment.csv` are in the working directory.
2. Run the provided Jupyter Notebook/Google Colab file.

## Conclusion & Strategy
The data suggests a "Sentiment-Aware" trading strategy: capital should be concentrated during "Greed" cycles while trading activity should be significantly reduced during "Neutral" periods to minimize capital erosion.

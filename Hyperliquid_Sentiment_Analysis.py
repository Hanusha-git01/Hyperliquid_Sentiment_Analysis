#!/usr/bin/env python
# coding: utf-8

# Project: Trader Behavior & Market Sentiment Analysis
# 
# Objective: Analyze the relationship between Hyperliquid trader performance and the Bitcoin Fear & Greed Index.
# 
# Candidate: Hanusha Palangthod
# 
# 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import gdown
# visualization style
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)


# Data Loading & Cleaning

historical_data_id = '1IAfLZwu6rJzyWKgBToqwSmmVYU6VbjVs'
sentiment_data_id = '1PgQC0tO8XN-wqkNyghWc_-mnrYv_nhSf'


# Download files
gdown.download(f'https://drive.google.com/uc?id={historical_data_id}', 'historical_trader_data.csv', quiet=False)
gdown.download(f'https://drive.google.com/uc?id={sentiment_data_id}', 'bitcoin_sentiment.csv', quiet=False)


# Load datasets
df_trader = pd.read_csv('historical_trader_data.csv')
df_sentiment = pd.read_csv('bitcoin_sentiment.csv')


# Convert Timestamps (Using 'ms' for the 13-digit Hyperliquid timestamps)
df_trader['time'] = pd.to_datetime(df_trader['Timestamp'], unit='ms')# Correcting 13-digit Unix timestamp (milliseconds) to standard datetime.
df_trader['trade_date'] = df_trader['time'].dt.date


# Convert Sentiment Dates
df_sentiment['date'] = pd.to_datetime(df_sentiment['date']).dt.date


# Handle Numeric Data
df_trader['Closed PnL'] = pd.to_numeric(df_trader['Closed PnL'], errors='coerce')
df_trader['Size USD'] = pd.to_numeric(df_trader['Size USD'], errors='coerce')


# Merge the datasets
df_merged = pd.merge(df_trader, df_sentiment, left_on='trade_date', right_on='date', how='inner')


print(f"Dataset successfully merged. Total records: {len(df_merged)}")


# Exploratory Data Analysis

# Define logical order for sentiment
sentiment_order = ['Fear', 'Neutral', 'Greed', 'Extreme Greed']


# Calculate Performance Metrics
performance_summary = df_merged.groupby('classification').agg({
    'Closed PnL': ['mean', 'sum', 'count'],
    'Size USD': 'mean'
}).reindex(sentiment_order)


# Flatten columns for readability
performance_summary.columns = ['Avg_PnL', 'Total_PnL', 'Trade_Count', 'Avg_Trade_Size']
print(performance_summary)


# Visualizations

# Create a multi-panel visualization
fig, ax = plt.subplots(1, 2, figsize=(18, 6))

# Plot 1: Average Profitability
sns.barplot(data=performance_summary, x='classification', y='Avg_PnL',
            hue='classification', palette='coolwarm', ax=ax[0], legend=False)
ax[0].set_title('Average Profit/Loss by Market Sentiment', fontsize=15)
ax[0].set_ylabel('USD Profit')

# Plot 2: Trading Activity (Frequency)
sns.barplot(data=performance_summary, x='classification', y='Trade_Count',
            hue='classification', palette='magma', ax=ax[1], legend=False)
ax[1].set_title('Frequency of Trading by Market Sentiment', fontsize=15)
ax[1].set_ylabel('Number of Trades')

plt.tight_layout()
plt.show()


# Executive Summary:After cleaning and merging the Hyperliquid trade data with the Fear & Greed Index, the results are quite surprising. It turns out that the way traders behave is heavily influenced by the "mood" of the market.
# 
# 1. The "Fear" Paradox: Busy but not Profitable.
# The data shows that traders are incredibly active when the market is in Fear
# (over 133,000 trades). It seems that when prices drop, everyone jumps in to try and "buy the dip" or scalp quick moves. However, this is actually their least efficient time,they make significantly less per trade here than during Greed. It’s a lot of work for a smaller reward.
# 
# 2. "Greed" is the Real Profit Driver
# While common advice says to be careful when the market is greedy, the data shows that for these traders, Greed is actually the most profitable regime. Average profits jump to $87.89 per trade. This suggests that these traders are likely "trend followers",they perform best when there is strong upward momentum and everyone is feeling optimistic.
# 
# 3. The "Neutral" Danger Zone
# When the market has no clear direction (Neutral), performance drops to its lowest point ($22.22$ avg PnL). This is a huge insight: it means that without a strong emotional trend in the market, these traders lose their edge and mostly just "churn" their accounts.
# 
# The "Smarter" Trading Strategy
# If we were to turn these insights into a business strategy, here is what I would recommend:Filter the Noise: Drastically reduce trading frequency during
# 
# Filter the Noise: Drastically reduce trading frequency during Neutral sentiment. The "choppy" market isn't worth the risk.
# 
# Quality over Quantity in Fear: Since Fear is the busiest time but has lower margins, traders should focus on fewer, high-conviction entries rather than high-frequency scalping.
# 
# Maximize the Greed Cycle: When the index moves into Greed, it’s time to be aggressive. This is statistically the best window for capturing large moves.
# 
# 
# 







import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
stock_data = pd.read_csv('sphist.csv')

# Ensure the 'Date' column is in datetime format
stock_data['Date'] = pd.to_datetime(stock_data['Date'])

# Sort the data by date
stock_data = stock_data.sort_values('Date')

# Line Plot
plt.figure(figsize=(10, 5))
plt.plot(stock_data['Date'], stock_data['Close'], label='Close Price')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Stock Closing Prices Over Time')
plt.legend()
plt.show()

# Histogram
plt.figure(figsize=(10, 5))
sns.histplot(stock_data['Close'], bins=30, kde=True)
plt.xlabel('Closing Price')
plt.ylabel('Frequency')
plt.title('Distribution of Closing Prices')
plt.show()

# Box Plot
plt.figure(figsize=(10, 5))
sns.boxplot(x=stock_data['Close'])
plt.xlabel('Closing Price')
plt.title('Box Plot of Closing Prices')
plt.show()

# Scatter Plot
plt.figure(figsize=(10, 5))
plt.scatter(stock_data['Volume'], stock_data['Close'])
plt.xlabel('Volume')
plt.ylabel('Closing Price')
plt.title('Volume vs. Closing Price')
plt.show()

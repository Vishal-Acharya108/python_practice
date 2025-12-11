import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
stock_price = [100, 102, 105, 103, 108]

plt.figure(figsize=(8, 4))
plt.plot(days, stock_price, marker='o', color='blue', linestyle='--')
plt.title('Stock Price Trend')
plt.xlabel('Day')
plt.ylabel('Price ($)')
plt.grid(True)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

x = []
y = []

for i in range(len(df)):
    x.append(df["date"][i])
    y.append(int(df["prize"][i]))

plt.bar(x,y)
plt.ylim(35000, 60000)

for i, value in enumerate(y):
    plt.text(i, value + 5, str(value), ha='center')

plt.ylabel("price")
plt.xlabel("date")
plt.title("Flipkart Price Tracker")

plt.show()
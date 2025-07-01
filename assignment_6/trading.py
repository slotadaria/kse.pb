import yfinance
import pandas as pd
import matplotlib.pyplot as plt
bitcoin = yfinance.Ticker("BTC-USD")
bitcoin_data = bitcoin.history(period='100mo')
df_with_dividents = pd.DataFrame(bitcoin_data)
df = df_with_dividents.drop(columns=["Dividends", "Stock Splits"])
df = df.reset_index()
df.columns = ["Дата", "Ціна відкриття","Максимум","Мінімум" ,"Ціна закриття", "Обсяг товарів"]
df_mean = df[["Дата", "Ціна закриття"]].copy()
df_mean["MA100"] = df["Ціна закриття"].rolling(window=100).mean()
df_mean["MA15"] = df["Ціна закриття"].rolling(window=15).mean()
df_end = df_mean.dropna()
x_axis = df_end["Дата"]
y_axis_ma15 = df_end["MA15"]
y_axis_ma100 = df_end["MA100"]
plt.plot(x_axis, y_axis_ma15)
plt.plot(x_axis, y_axis_ma100)
plt.show()
sign = []
for i in range (len(df_end)-1):
  if df_end["MA15"].iloc[i+1] < df_end["MA100"].iloc[i+1] and df_end["MA15"].iloc[i] > df_end["MA100"].iloc[i]:
    sign.append("sell")
  elif df_end["MA15"].iloc[i+1] > df_end["MA100"].iloc[i+1] and df_end["MA15"].iloc[i] < df_end["MA100"].iloc[i]:
    sign.append("buy")
  else:
    sign.append("do nothing")
sign.append("don't know what to do")
df_profit = df_end.dropna()
df_profit["Signals"] = sign
df_profit
profit = 0
for i in range(len(df_profit) -1):
 if df_profit["Signals"].iloc[i] == "buy":
  profit -= df_profit["Ціна закриття"].iloc[i]
 elif df_profit["Signals"].iloc[i] == "sell":
  profit += df_profit["Ціна закриття"].iloc[i]
 else:
  pass
print(df)
print(df_profit)
print("Your profit is:", profit)

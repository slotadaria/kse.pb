import requests
import pandas as pd
responce = requests.get("https://api.open-meteo.com/v1/forecast?latitude=50.4547&longitude=30.5238&hourly=temperature_2m,wind_speed_10m")
data_forecast = responce.json()
df = pd.DataFrame(data_forecast)
#display(df)
table = df["hourly"] 
time = table.loc["time"]
temperature = table.loc["temperature_2m"]
wind = table.loc["wind_speed_10m"]
df = {"Time": time,
      "Temperature": temperature,
      "Wind" : wind
}

df_table = pd.DataFrame(df)

print(df_table)
table_for_3_days = df_table.loc[0:71, ["Time", "Temperature", "Wind"]]
min_temp = table_for_3_days["Temperature"].min()
max_temp = table_for_3_days["Temperature"].max()
aver_temp = table_for_3_days["Temperature"].mean()
print("Мінімальна температура за наступні 3 дні становить: ", min_temp,"\n Максимальна температура за наступні 3 дні становить: ", max_temp,"\n Середня температура за наступні 3 дні становить: ", aver_temp )

aver_wind = float(table_for_3_days["Wind"].mean())
table_with_wind_more_aver = table_for_3_days[table_for_3_days["Wind"] > (aver_wind)]
#display(table_with_wind_more_aver)
table_with_wind_more_aver.shape[0]
print(table_with_wind_more_aver.shape[0], "годин швидкість вітру перевищує загальну середню швидкість за 3 дні")
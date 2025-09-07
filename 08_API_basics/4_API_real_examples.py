# 4_API_real_examples.py
# Day 4: Real Public APIs

import requests
import json

# ========== WEATHER (Open-Meteo) ==========
weather_url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 3.1390,     # Kuala Lumpur, Malaysia
    "longitude": 101.6869,
    "hourly": "temperature_2m",
    "timezone": "Asia/Kuala_Lumpur"
}

resp = requests.get(weather_url, params=params, timeout=8)
if resp.ok:
    data = resp.json()
    print("Weather API success!")
    # Print first 3 hourly readings
    for t, temp in zip(data['hourly']['time'][:3], data['hourly']['temperature_2m'][:3]):
        print(f"{t} → {temp}°C")
else:
    print("Weather API failed:", resp.status_code)


# ========== JOKE (icanhazdadjoke) ==========
joke_url = "https://icanhazdadjoke.com/"
headers = {"Accept": "application/json"}

resp = requests.get(joke_url, headers=headers, timeout=5)
if resp.ok:
    joke_data = resp.json()
    print("\n Joke of the day:", joke_data["joke"])
else:
    print("Joke API failed")


# ========== CURRENCY (Frankfurter API, no key required) ==========
currency_url = "https://api.frankfurter.app/latest"
params = {"from": "USD", "to": "MYR,PKR"}

resp = requests.get(currency_url, params=params, timeout=6)

if resp.ok:
    data = resp.json()
    print("\nCurrency API success!")
    print("Base currency:", data["base"])
    for cur, rate in data["rates"].items():
        print(f"1 {data['base']} = {rate} {cur}")
else:
    print("Currency API failed:", resp.status_code)


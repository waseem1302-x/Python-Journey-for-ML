# 2_API_requests_basics.py
# Day 2: Using params and headers with requests

import requests

# Base API endpoint (Open-Meteo provides free weather data without an API key)
url = "https://api.open-meteo.com/v1/forecast"

# Step 1: Define query parameters (latitude & longitude for Tokyo)
params = {
    "latitude": 35.0,
    "longitude": 139.0,
    "hourly": "temperature_2m",   # ask for hourly temperature
    "timezone": "Asia/Tokyo"
}

# Step 2: Send GET request with params
response = requests.get(url, params=params, timeout=8)

# Step 3: Handle response
if response.status_code == 200:
    data = response.json()  # Convert JSON to Python dict
    print("Success! Keys in response:", list(data.keys()))

    # Print first 5 timestamps & temperatures
    print("\nFirst 5 hourly readings:")
    for t, temp in zip(data['hourly']['time'][:5], data['hourly']['temperature_2m'][:5]):
        print(f"{t} → {temp}°C")
else:
    print("❌ Failed with status code:", response.status_code)



# Example 2: Joke API (icanhazdadjoke.com requires Accept header)
url = "https://icanhazdadjoke.com/"
headers = {"Accept": "application/json"}

resp = requests.get(url, headers=headers, timeout=5)
if resp.ok:
    joke_data = resp.json()
    print("\n😂 Joke of the day:", joke_data["joke"])

import requests

url = "https://api.frankfurter.app/latest"  # Currency API

try:
    resp = requests.get(url, timeout=5)   # if it takes >5s → error
    resp.raise_for_status()  # Raises HTTPError for 4xx/5xx
    data = resp.json()
    print("Success! Data received:", data)
except requests.exceptions.Timeout:
    print("Timeout! API took too long to respond.")
except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)
except requests.exceptions.RequestException as e:
    print("General Request Error:", e)


# Example: safely reading exchange rates
if "rates" in data:
    print("Rates:", data["rates"])
else:
    print("'rates' key missing in API response")



weather_url = "https://api.open-meteo.com/v1/forecast"
params = {"latitude": 3.1390, "longitude": 101.6869, "hourly": "temperature_2m"}

try:
    resp = requests.get(weather_url, params=params, timeout=5)
    resp.raise_for_status()
    data = resp.json()

    if "hourly" in data and "temperature_2m" in data["hourly"]:
        temps = data["hourly"]["temperature_2m"][:5]
        times = data["hourly"]["time"][:5]
        print("\nWeather Data (first 5 hours):")
        for t, temp in zip(times, temps):
            print(f"{t} → {temp}°C")
    else:
        print("Weather data missing expected keys")

except requests.exceptions.RequestException as e:
    print("Weather API request failed:", e)

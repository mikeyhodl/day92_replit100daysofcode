import requests

def get_weather(city):
  url = "https://api.open-meteo.com/v1/weather"
params = { "q": city }
response = requests.get(url, params=params)
data = response.json()
temperature = data["temperature"]
condition = data["condition"]
if condition == "clear sky":
    emoji = "☀️"
elif condition == "few clouds":
    emoji = "⛅️"
elif condition == "scattered clouds":
    emoji = "☁️"
elif condition == "broken clouds":
    emoji = "⛅️"
elif condition == "shower rain":
    emoji = "🌧"
elif condition == "rain":
    emoji = "🌧"
elif condition == "thunderstorm":
    emoji = "⛈️"
elif condition == "snow":
    emoji = "❄️"
elif condition == "mist":
    emoji = "🌫"
  
return f"The weather in {city} is currently {temperature}°C with {condition} {emoji}"
print(get_weather("Eldoret"))

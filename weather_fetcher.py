import requests

API_KEY = "your_api_key_here"  # Get from OpenWeatherMap
city = input("🌍 Enter city name: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
weather_data = response.json()

if response.status_code == 200:
    print(f"🌡️ Temperature: {weather_data['main']['temp']}°C")
    print(f"☁️ Condition: {weather_data['weather'][0]['description']}")
else:
    print("❌ City not found.")

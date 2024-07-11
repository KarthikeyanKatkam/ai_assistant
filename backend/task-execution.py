# backend/task_execution.py
import requests

def get_weather(city):
    api_key = "your_api_key"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(base_url)
    data = response.json()
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        return f"The temperature in {city} is {main['temp']}°K with {weather['description']}."
    else:
        return "City not found."

print(get_weather("New York"))

import requests
from config import WEATHER_API_KEY

def get_weather_impact(region='West'):
    """Fetch weather data for fusion."""
    if WEATHER_API_KEY:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={region}&appid={WEATHER_API_KEY}"
        response = requests.get(url).json()
        weather = response.get('weather', [{}])[0].get('main', 'Clear')
        return f"Weather: {weather} (Rain may lower sales)."
    return "No weather data."
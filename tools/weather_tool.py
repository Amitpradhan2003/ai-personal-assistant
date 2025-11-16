# tools/weather_tool.py
import requests
from langchain.tools import tool

@tool("weather")
def weather_tool(city: str) -> str:
    """Get current weather info for a city using Open-Meteo."""
    try:
        # Step 1: geocode city to lat/long using Open-Meteo geocoding
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
        geo = requests.get(geo_url, timeout=10).json()
        if not geo.get("results"):
            return f"Could not geocode city: {city}"
        lat = geo["results"][0]["latitude"]
        lon = geo["results"][0]["longitude"]

        # Step 2: fetch current weather
        url = (f"https://api.open-meteo.com/v1/forecast?"
               f"latitude={lat}&longitude={lon}&current_weather=true")
        data = requests.get(url, timeout=10).json()
        curr = data.get("current_weather")
        if not curr:
            return "Could not fetch current weather data."

        temp = curr.get("temperature")
        wind = curr.get("windspeed")
        condition = curr.get("weathercode")  # we may map codes to text if needed

        return (f"Weather in {city} (lat {lat:.2f}, lon {lon:.2f}): "
                f"{temp}°C, wind {wind} km/h (code {condition})")

    except requests.RequestException as e:
        return f"Network error when fetching weather: {str(e)}"
    except Exception as e:
        return f"Unexpected error in weather tool: {str(e)}"

# import requests
# import json
import weather_check

# API Key - aeb23a1310ca2a5a2afe2202437dc509
# End point - https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

api_key = "aeb23a1310ca2a5a2afe2202437dc509"
city = "colombo"


if __name__ == "__main__":
    print("Starting dynamic wallpaper")
    weather_engine = weather_check.WeatherCheck(api_key, city, 1)
    weather_engine.start()
    weather_engine.join()

from threading import Thread
from multiprocessing import Process
import requests
import json
import time


class WeatherCheck(Process):
    def __init__(self, api_key, city, quaries, delay=5):
        super(WeatherCheck, self).__init__()
        self.api_key = api_key
        self.city = city
        self.quaries = quaries
        self.delay = delay

    def run(self):
        while True:
            weather = self.__get_weather_report(self.api_key, self.city)
            # self.__update_weather_object(weather)
            self.quaries.put(weather)

            # print("Weather is", weather)

            time.sleep(self.delay)

    def __update_weather_object(self, weather):
        for attr in ["id", "main", "description", "icon"]:
            self.weather[attr] = weather[attr]

    def __get_weather_report(self, api_key, city):
        url = (
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        )
        response = requests.get(url)

        if response.status_code == 200:
            json_content = json.loads(response.content)
            weather = json_content["weather"]
            if weather:
                return weather[0]

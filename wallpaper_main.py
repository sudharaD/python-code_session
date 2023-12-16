import weather_check
import image_downloader
from multiprocessing import Queue
import time
import engine

# Unsplash key - 5jxcmVNCwLqlUG2J49-c4MZJjZT5uNQOPGFQvqclQCM

api_key = "aeb23a1310ca2a5a2afe2202437dc509"
city = "colombo"

quaries = Queue()
images = Queue()
weather = {}

if __name__ == "__main__":
    print("Starting dynamic wallpaper")
    weather_engine = weather_check.WeatherCheck(api_key, city, quaries)
    weather_engine.start()

    downloader = image_downloader.ImageDownloader(quaries, images)
    downloader.start()

    engine = engine.Engine(images)
    engine.start()

    weather_engine.join()
    downloader.join()
    engine.join()

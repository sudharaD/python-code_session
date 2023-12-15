from collections.abc import Callable, Iterable, Mapping
from threading import Thread
from typing import Any
import requests


class ImageDownloder(Thread):
    def __init__(self, image_id, name, urls):
        super(ImageDownloder, self).__init__()
        self.id = image_id
        self.name = name
        self.urls = urls

    def run(self):
        for i, url in enumerate(self.urls):
            self.image_downloder(url, f"{self.id}-{i}")

    def image_downloder(self, url, image_number):
        r = requests.get(url, stream=True)

        if r.status_code == 200:
            r.raw.decode_content = True
            file_name = f"images/{image_number}.jpg"
            with open(file_name, "wb") as file:
                file.write(r.content)

                print(f"Image {image_number} successfully downloaded")
        else:
            print(f"Image {image_number} couldn't be retrived")

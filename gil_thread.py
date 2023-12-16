# from collections.abc import Callable, Iterable, Mapping
# from threading import Thread
# from typing import Any
import requests
from multiprocessing import Process


class ImageDownloder(Process):
    def __init__(self, image_id, name, urls, my_list):
        super(ImageDownloder, self).__init__()
        self.id = image_id
        self.name = name
        self.urls = urls
        self.success_count = 0
        self.results = my_list

    def run(self):
        for i, url in enumerate(self.urls):
            if self.image_downloder(url, f"{self.id}-{i}"):
                self.success_count += 1
        self.results.put(self.success_count)

    def image_downloder(self, url, image_number):
        r = requests.get(url, stream=True)

        if r.status_code == 200:
            r.raw.decode_content = True
            file_name = f"images/{image_number}.jpg"
            with open(file_name, "wb") as file:
                file.write(r.content)

                print(f"Image {image_number} successfully downloaded")
                return True
        else:
            print(f"Image {image_number} couldn't be retrived")
            return False

from threading import Thread
from multiprocessing import Process
import requests
import json
import time


class ImageDownloader(Process):
    def __init__(self, quaries, images):
        super(ImageDownloader, self).__init__()
        self.quaries = quaries
        self.previous_query = None
        self.images = images

    def run(self):
        query = self.quaries.get()
        print("Quary", query)
        while query is not None:
            if self.previous_query == query:
                print("Same query requested")
                query = self.quaries.get()
                continue

            url = f"https://unsplash.com/napi/search/photos?query={query}"

            r = requests.get(url)

            if r.status_code == 200:
                response_json = json.loads(r.content)
                results = response_json["results"]
                if len(results) > 0:
                    self.__download_image(results[0])
            else:
                print("Image couldn't be retrived")

            query = self.quaries.get()
            self.previous_query = query

    def __download_image(self, image):
        urls = image["urls"]
        raw = urls["raw"]
        print(raw)

        res = requests.get(raw, stream=True)

        if res.status_code == 200:
            res.raw.decode_content = True

            """
            https://images.unsplash.com/photo-1687360440094-949b8fe71c8c?
            ixid=M3wxMjA3fDB8MXxzZWFyY2h8MXx8JTdCJTI3aWQlMjclM0ElMjA4MDQlM
            kMlMjAlMjdtYWluJTI3JTNBJTIwJTI3Q2xvdWRzJTI3JTJDJTIwJTI3ZGVzY3J
            pcHRpb24lMjclM0ElMjAlMjdvdmVyY2FzdCUyMGNsb3VkcyUyNyUyQyUyMCUyN
            2ljb24lMjclM0ElMjAlMjcwNG4lMjclN0R8ZW58MHx8fHwxNzAyNzM4NzQ0fDA&ixlib=rb-4.0.3
            """

            x = raw.split("?")
            image_name = x[0].split("/")[-1]

            file_name = f"images/{image_name}.jpg"
            with open(file_name, "wb") as file:
                file.write(res.content)

            self.images.put(file_name)

            print(f"Image {image_name} successfully downloaded")
        else:
            print(f"Image {image_name} couldn't be retrived")

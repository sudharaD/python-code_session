from multiprocessing import Process
import os
import ctypes
import time

SPI_SETDESKWALLPAPER = 20


class Engine(Process):
    def __init__(self, images):
        super(Engine, self).__init__()
        self.images = images

    def run(self):
        image = self.images.get()

        while True:
            ctypes.windll.user32.SystemParametersInfoW(
                SPI_SETDESKWALLPAPER, 0, image, 0
            )
            print("Wallpaper set to ", image)
            time.sleep(5)
            image = self.images.get()

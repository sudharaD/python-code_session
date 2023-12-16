import requests
import time
from threading import Thread
import my_thread
from queue import Queue


def get_urls(count):
    if count <= 0:
        print("Invalid Count")
        return

    for i in range(0, count):
        url = f"https://picsum.photos/id/{i}/100/150"
        yield url


start = time.time_ns()

urls = list(get_urls(100))

urls_list = []
num_of_threads = 10

for i in range(0, len(urls), num_of_threads):
    l = urls[i : i + num_of_threads]
    urls_list.append(l)

threads = []
my_list = Queue()

for i in range(0, num_of_threads):
    thread = my_thread.ImageDownloder(i, f"Thread-{i}", urls_list[i], my_list)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

total = 0

while not my_list.empty():
    total += my_list.get()

print("Total image downloaded", total)

# for i, url in enumerate(urls):
#     image_downloder(url, i)

diff = time.time_ns() - start

print(f"Duration: {diff/1000000}ms")

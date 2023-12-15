import requests
import time
import my_thread


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

for i in range(0, num_of_threads):
    thread = my_thread.ImageDownloder(i, f"Thread-{i}", urls_list[i])
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

# for i, url in enumerate(urls):
#     image_downloder(url, i)

diff = time.time_ns() - start

print(f"Duration: {diff/1000000}ms")

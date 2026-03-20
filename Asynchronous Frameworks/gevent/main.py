from gevent import monkey
monkey.patch_all()

import requests
import gevent

def fetch(url):
    try:
        response = requests.get(url, verify=False)  # temporary fix
        print(response.status_code)
    except Exception as e:
        print("Error:", e)

jobs = [gevent.spawn(fetch, "https://example.com") for _ in range(5)]
gevent.joinall(jobs)
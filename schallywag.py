import threading
import requests
import random

def spam():
    threading.Timer(0.01, spam).start()
    requests.get("http://api.xgenstudios.com/?method=xgen.stats.get&username=weathernowdays")
spam()

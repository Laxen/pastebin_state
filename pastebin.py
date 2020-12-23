import time
import requests

URL = "https://pastebin.com/raw/Nh8D7mCc"

while True:
    state = requests.get(URL).content.decode("utf-8")

    with open("state.txt", "r+") as f:
        prev_state = f.read()

        if state == prev_state:
            print("datorn sätts INTE på")
        else:
            print("datorn sätts på")

        f.seek(0)
        f.truncate()
        f.write(state)

    time.sleep(3)

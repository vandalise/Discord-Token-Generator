#you dont need to run this if u dont want to its just more random bios for the accounts
import httpx, threading, random

proxylist = []
for proxy in open("proxies.txt", "r").read().splitlines():
    proxylist.append(proxy)

def get_bio():
    proxy = random.choice(proxylist)
    proxies = {
        "http://": f"http://{proxy}",
        "https://": f"http://{proxy}",
    }
    with httpx.Client(proxies=proxies) as client:
        while True:
            try:
                r = client.get("https://www.twitterbiogenerator.com/generate")
                print(f"Bio generated: {r.text}")
                open("bios.txt", "a").write(f"{r.text}\n")
            except Exception as e:
                print(e)
                continue

for i in range(10):
    threading.Thread(target=get_bio).start()

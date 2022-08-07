#This discord token generator was developed by King Herod
#Dont be skidding my shit acting like you made it
from turtle import update
from colorama import Fore
import threading
import websocket
import requests
import random
import base64
import httpx
import json
import time
import sys
import os

print(f"{Fore.YELLOW}|/| Loading capmonster{Fore.RESET}")
try:
    captchaKey = json.loads(open("config.json", "r").read())["capmonster_key"]
except:
    print(f"  {Fore.WHITE}|>|{Fore.RED} Error loading capmonster key from config.json")
    time.sleep(3)
    sys.exit()
try:
    get_balance_resp = httpx.post(f"https://api.capmonster.cloud/getBalance", json={"clientKey": captchaKey}).text
    captchas_balance = json.loads(get_balance_resp)["balance"]
except Exception as e:
    print(f"  {Fore.WHITE}|>|{Fore.RED} Capmonster API is down or the key is invalid!!")
    time.sleep(3)
    sys.exit()
print(f"{Fore.YELLOW}|/| Loading proxies{Fore.RESET}")
try:
    proxylist = []
    proxycount = 0
    for proxy in open("proxies.txt", "r").read().splitlines():
        proxylist.append(proxy)
        proxycount +=1
except:
    print(f"  {Fore.WHITE}|>|{Fore.RED} Error loading proxies from proxies.txt")
    time.sleep(3)
    sys.exit()
print(f"{Fore.YELLOW}|/| Loading names from names.txt{Fore.RESET}")
try:
    users = []
    for user in open("names.txt", "r").read().splitlines():
        users.append(user)
except:
    print(f"  {Fore.WHITE}|>|{Fore.RED} No usernames found in names.txt (this is optional)")
    time.sleep(3)
    pass
print(f"{Fore.YELLOW}|/| Loading avatars{Fore.RESET}")
try:
    pfps = []
    pfpcount = 0
    for pfp in os.listdir("Avatars"):
        imgg = base64.b64encode(open(f"Avatars/{pfp}", "rb").read()).decode('ascii')
        pfps.append(imgg)
        pfpcount+=1 
except:
    print(f"  {Fore.WHITE}|>|{Fore.RED} Error loading pfps from the 'Avatars' folder, make sure you have your png images in that folder.")
    time.sleep(3)
    sys.exit()
print(f"{Fore.YELLOW}|/| Loading bios{Fore.RESET}")
try:
    bios = []
    biocount = 0
    for bio in open("bios.txt", "r").read().splitlines():
        bios.append(bio)
        biocount+=1
except:
    print(f"  {Fore.WHITE}|>|{Fore.RED} Error loading bios from bios.txt make sure you have a list of bios for the accounts")
    time.sleep(3)
    sys.exit()


def get_ws():
    games = ['Minecraft', 'Rust', 'VRChat', 'reeeee', 'MORDHAU', 'Fortnite', 'Apex Legends', 'Escape from Tarkov', 'Rainbow Six Siege', 'Counter-Strike: Global Offense', 'Sinner: Sacrifice for Redemption', 'Minion Masters', 'King of the Hat', 'Bad North', 'Moonlighter', 'Frostpunk', 'Starbound', 'Masters of Anima', 'Celeste', 'Dead Cells', 'CrossCode', 'Omensight', 'Into the Breach', 'Battle Chasers: Nightwar', 'Red Faction Guerrilla Re-Mars-tered Edition', 'Spellforce 3', 'This is the Police 2', 'Hollow Knight', 'Subnautica', 'The Banner Saga 3', 'Pillars of Eternity II: Deadfire', 'This War of Mine', 'Last Day of June', 'Ticket to Ride', 'RollerCoaster Tycoon 2: Triple Thrill Pack', '140', 'Shadow Tactics: Blades of the Shogun', 'Pony Island', 'Lost Horizon', 'Metro: Last Light Redux', 'Unleash', 'Guacamelee! Super Turbo Championship Edition', 'Brutal Legend', 'Psychonauts', 'The End Is Nigh', 'Seasons After Fall', 'SOMA', 'Trine 2: Complete Story', 'Trine 3: The Artifacts of Power', 'Trine Enchanted Edition', 'Slime-San', 'The Inner World', 'Bridge Constructor', 'Bridge Constructor Medieval', 'Dead Age', 'Risk of Rain', "Wasteland 2: Director's Cut", 'The Metronomicon: Slay The Dance Floor', 'TowerFall Ascension + Expansion', 'Nidhogg', 'System Shock: Enhanced Edition', 'System Shock 2', "Oddworld:New 'n' Tasty!", 'Out of the Park Baseball 18', 'Hob', 'Destiny 2', 'Torchlight', 'Torchlight 2', 'INSIDE', 'LIMBO', "Monaco: What's Yours Is Mine", 'Tooth and Tail', 'Dandara', 'GoNNER', 'Kathy Rain', 'Kingdom: Classic', 'Kingdom: New Lands', 'Tormentor X Punisher', 'Chaos Reborn', 'Ashes of the Singularity: Escalation', 'Galactic Civilizations III', 'Super Meat Boy', 'Super Hexagon', 'de Blob 2', 'Darksiders II Deathinitive Edition', 'Darksiders Warmastered Edition', 'de Blob', 'Red Faction 1', 'Dungeon Defenders']
    mobile = {
        "op": 2,
        "d": {
            "token": "",
            "properties": {
                "$os": "Android",
                "$browser": "Discord Android",
                "$device": "Android 12"
            },
        }
    }
    game = random.choice(games)
    pc = {
        "op": 2,
        "d": {
            "token": "",
            "capabilities": 125,
            "properties": {
                "$os": "Windows",
                "$browser": "Chrome",
                "$device": "Windows Device",
                "system_locale": "en-US",
                "browser_user_agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
                "browser_version": "96.0.4664.45",
                "os_version": "10",
                "referrer": "",
                "referring_domain": "",
                "referrer_current": "",
                "referring_domain_current": "",
                "release_channel": "stable",
                "client_build_number": 105691,
                "client_event_source": None
            },
            "presence": {
                "status": random.choice(["online", "dnd", "idle"]),
                "game": {"name": game, "type": 0},
                "since": 0,
                "activities": [],
                "afk": False
            },
            "compress": False,
            "client_state": {
                "guild_hashes": {},
                "highest_last_message_id": "0",
                "read_state_version": 0,
                "user_guild_settings_version": -1,
                "user_settings_version": -1
            }
        },
        "s": None,
        "t": None
    }
    return pc, mobile

def create_websocket(token):
    while True:
        try:
            ws = websocket.WebSocket()
            ws.connect("wss://gateway.discord.gg/?encoding=json&v=6")
            mobile, pc = get_ws()
            mobile["d"]["token"] = token
            pc["d"]["token"] = token
            ws.send(json.dumps(random.choice([pc, mobile])))
            heartbeat = json.loads(ws.recv())['d']['heartbeat_interval']
            time.sleep(heartbeat / 1000)
            ws.send(json.dumps({"op": 1, "d": None}))
        except Exception as e:
            continue

def get_captcha_result(captchaKey):
    payload = {
        "clientKey": f"{captchaKey}",
        "task": {
            "type": "HCaptchaTaskProxyless",
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73",
            "websiteKey": f"4c672d35-0701-42b2-88c3-78380b0db560",
            "websiteURL": f"https://discord.com/"
        }
    }
    while True:
        try:
            tempreqx = httpx.post(f"https://api.capmonster.cloud/createTask", json=payload).text
            taskid = json.loads(tempreqx)["taskId"]
            break
        except:
            continue
    payload1 = {
        "clientKey": f"{captchaKey}",
        "taskId": taskid
    }
    while True:
        r = httpx.post(f"https://api.capmonster.cloud/getTaskResult", json=payload1).text
        status = json.loads(r)["status"]
        if status == "processing":
            continue
        elif status == "ready":
            data = json.loads(r)
            break
    return data["solution"]["gRecaptchaResponse"]

def get_fingerprint(proxies):
    with httpx.Client(proxies=proxies) as client:
        try:
            r = client.get("https://discordapp.com/api/v9/experiments").json()
            return r["fingerprint"]
        except:
            return get_fingerprint(proxies)

def join_vc(token, guildid, channelid):
    while True:
        try:
            ws = websocket.WebSocket()
            ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")
            ws.send(json.dumps({"op": 2,"d": {"token": token, "properties": {"$os": "windows","$browser": "Discord","$device": "desktop"}}}))
            ws.send(json.dumps({"op": 4,"d": {"guild_id": guildid,"channel_id": channelid, "self_mute": True,"self_deaf": True}}))
            ws.close()
        except:
            continue

verified = 0
captchas = 0
proxyerror = 0
captchaerror = 0
def generateToken(proxylist, username, invite, captchaKey, crash, guildid=None, channelid=None):
    global verified, captchas, proxyerror, captchaerror, users
    while True:
        try:
            proxy = random.choice(proxylist)
            proxies = {
                "http://": f"http://{proxy}",
                "https://": f"http://{proxy}",
            }
            with httpx.Client(cookies={"locale": "en-US"}, headers={"Accept": "*/*", "Accept-Language": "en-US", "Connection": "keep-alive", "Content-Type": "application/json", "DNT": "1", "Host": "discord.com", "Referer": f"https://discord.com/invite/{invite}", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "TE": "trailers", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36", "X-Track": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2Ojk0LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTQuMCIsImJyb3dzZXJfdmVyc2lvbiI6Ijk0LjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTk5OSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="}, proxies=proxies) as client:
                test_proxy = client.get("https://discord.com")
                if test_proxy.status_code == 200:
                    client.headers['Cookie'] = f"locale=fr; __dcfduid={test_proxy.cookies.get('__dcfduid')}; __sdcfduid={test_proxy.cookies.get('__sdcfduid')}"
                    client.cookies.set('locale', 'fr', 'discord.com')
                    pass
                else:
                    break
                client.headers["X-Fingerprint"] = get_fingerprint(proxies)
                client.headers["Origin"] = "https://discord.com"
                solvedCaptcha = get_captcha_result(captchaKey)
                captchas+=1 
                if username == "random":
                    while True:
                        try:
                            username = httpx.get("https://story-shack-cdn-v2.glitch.me/generators/username-generator?").json().get("data").get("name")
                            break
                        except:
                            continue
                elif username == "list":
                    username = random.choice(users)
                payload = {"consent": True, "fingerprint": client.headers["X-Fingerprint"], "username": str(username), "captcha_key": str(solvedCaptcha), "invite":  invite }
                client.headers['Content-Length'] = str(len(json.dumps(payload)))
                create_account_resp = client.post("https://discord.com/api/v9/auth/register", json=payload, timeout=5)
                verified += 1
                if "token" in create_account_resp.text:
                    token = create_account_resp.json()["token"]
                    pass
                elif "retry_after" in create_account_resp.text:
                    delay = create_account_resp.json()["retry_after"]
                    proxyerror+=1
                    continue
                elif "invalid-response" or "invalid-input-response" in create_account_resp.text:
                    captchaerror+=1
                    continue
                else:
                    print(create_account_resp.text)
                client.headers["Authorization"] = token
                client.headers["Origin"] 
                client.headers["Referer"] = "https://discord.com/register"
                client.headers["X-Debug-Options"] = "bugReporterEnabled"
                del client.headers["X-Track"]
                client.headers["X-Discord-Locale"] = "en-US"
                client.headers["X-Super-Properties"] = "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk3LjAuNDY5Mi43MSBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTcuMC40NjkyLjcxIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjExMTMzMCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
                imgg = random.choice(pfps)
                bio = random.choice(bios)
                client.patch("https://canary.discord.com/api/v6/users/@me", json={"avatar": f"data:image/png;base64,{imgg}", "bio": bio})
                client.post('https://discord.com/api/v9/hypesquad/online', json={'house_id': random.randint(1, 3)})
                myData = client.get("https://discord.com/api/v9/users/@me")
                if myData.status_code == 200:
                    open("tokens.txt", "a").write(f"{token}\n")
                    threading.Thread(target=create_websocket, args=(token,)).start()
                if crash == "y":
                    join_vc(token=token, guildid=guildid, channelid=channelid)
        except Exception as e:
            proxyerror += 1
            continue
        threading.Thread(target=generateToken, args=(proxylist, username, invite, captchaKey, crash, guildid, channelid,)).start()

def main():
    global verified, locked, valid, captchas, proxyerror, captchaerror
    os.system("cls||clear")
    print(f"""{Fore.MAGENTA}
  {Fore.WHITE}╔{Fore.MAGENTA}█████{Fore.WHITE}╗{Fore.MAGENTA} ██{Fore.WHITE}╗{Fore.MAGENTA}      █████{Fore.WHITE}╗{Fore.MAGENTA} ███████{Fore.WHITE}╗{Fore.MAGENTA}████████{Fore.WHITE}╗{Fore.MAGENTA} ██████{Fore.WHITE}╗{Fore.MAGENTA} ██████{Fore.WHITE}╗{Fore.MAGENTA} ██████{Fore.WHITE}╗{Fore.MAGENTA} ██████{Fore.WHITE}╗{Fore.MAGENTA} 
  {Fore.WHITE}║{Fore.MAGENTA}█{Fore.WHITE}╔══{Fore.MAGENTA}██{Fore.WHITE}╗{Fore.MAGENTA}██{Fore.WHITE}║{Fore.MAGENTA}     ██{Fore.WHITE}╔══{Fore.MAGENTA}██{Fore.WHITE}╗{Fore.MAGENTA}██{Fore.WHITE}╔════╝╚══{Fore.MAGENTA}██{Fore.WHITE}╔══╝{Fore.MAGENTA}██{Fore.WHITE}╔════╝{Fore.MAGENTA}██{Fore.WHITE}╔═══{Fore.MAGENTA}██{Fore.WHITE}╗{Fore.MAGENTA}██{Fore.WHITE}╔══{Fore.MAGENTA}██{Fore.WHITE}╗{Fore.MAGENTA}██{Fore.WHITE}╔══{Fore.MAGENTA}██{Fore.WHITE}╗{Fore.MAGENTA}
  {Fore.WHITE}║{Fore.MAGENTA}█████{Fore.WHITE}╔╝{Fore.MAGENTA}██{Fore.WHITE}║{Fore.MAGENTA} :)  ███████{Fore.WHITE}║{Fore.MAGENTA}███████{Fore.WHITE}╗{Fore.MAGENTA}   ██{Fore.WHITE}║{Fore.MAGENTA}   ██{Fore.WHITE}║{Fore.MAGENTA}     ██{Fore.WHITE}║{Fore.MAGENTA}   ██{Fore.WHITE}║{Fore.MAGENTA}██████{Fore.WHITE}╔╝{Fore.MAGENTA}██{Fore.WHITE}║{Fore.MAGENTA}  ██{Fore.WHITE}║{Fore.MAGENTA}
  {Fore.WHITE}║{Fore.MAGENTA}█{Fore.WHITE}╔══{Fore.MAGENTA}██{Fore.WHITE}╗{Fore.MAGENTA}██{Fore.WHITE}║{Fore.MAGENTA}     ██{Fore.WHITE}╔══{Fore.MAGENTA}██{Fore.WHITE}║╚════{Fore.MAGENTA}██{Fore.WHITE}║{Fore.MAGENTA}   ██{Fore.WHITE}║{Fore.MAGENTA}   ██{Fore.WHITE}║{Fore.MAGENTA}     ██{Fore.WHITE}║{Fore.MAGENTA}   ██{Fore.WHITE}║{Fore.MAGENTA}██{Fore.WHITE}╔══{Fore.MAGENTA}██{Fore.WHITE}╗{Fore.MAGENTA}██{Fore.WHITE}║{Fore.MAGENTA}  ██{Fore.WHITE}║{Fore.MAGENTA}
  {Fore.WHITE}║{Fore.MAGENTA}█████{Fore.WHITE}╔╝{Fore.MAGENTA}███████{Fore.WHITE}╗{Fore.MAGENTA}██{Fore.WHITE}║{Fore.MAGENTA}  ██{Fore.WHITE}║{Fore.MAGENTA}███████{Fore.WHITE}║{Fore.MAGENTA}   ██{Fore.WHITE}║   ╚{Fore.MAGENTA}██████{Fore.WHITE}╗╚{Fore.MAGENTA}██████{Fore.WHITE}╔╝{Fore.MAGENTA}██{Fore.WHITE}║{Fore.MAGENTA}  ██{Fore.WHITE}║{Fore.MAGENTA}██████{Fore.WHITE}╔╝{Fore.MAGENTA}
  {Fore.WHITE}╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ {Fore.WHITE}
                     Proxies: [{proxycount}]  Captchas: [${captchas_balance}]
                         Avatars: [{pfpcount}]    Bios: [{biocount}] {Fore.MAGENTA}
                ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                ┃{Fore.WHITE}               downcord.org{Fore.MAGENTA}                ┃
                ┃{Fore.WHITE}          Discord Account Generator     {Fore.MAGENTA}   ┃
                ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
""")
    option = input(f"{Fore.WHITE}|?|{Fore.MAGENTA} Custom user (1) Random users (2) Users from names.txt (3){Fore.WHITE}: ")
    if option not in("1", "2", "3"):
        main()
    if option == "1":
        username = input(f"{Fore.WHITE}|?|{Fore.MAGENTA} Usernames{Fore.WHITE}: ")
    elif option == "2":
        username = "random"
    elif option == "3":
        username = "list"
    invite = input(f"{Fore.WHITE}|?|{Fore.MAGENTA} Invite{Fore.WHITE}: ")
    threadAmount = input(f"{Fore.WHITE}|?|{Fore.MAGENTA} Threads{Fore.WHITE}: ")
    crash = input(f"{Fore.WHITE}|?|{Fore.MAGENTA} Crash VC? (y, n){Fore.WHITE} (this can term the server): ")
    if crash not in("y", "n"):
        main()
    elif crash == "y":
        guildid = input(f"{Fore.WHITE}|?|{Fore.MAGENTA} Guild ID: ")
        channelid = input(f"{Fore.WHITE}|?|{Fore.MAGENTA} VC CHANNEL ID: ")
        for x in range(int(threadAmount)):
            threading.Thread(target=generateToken, args=(proxylist, username, invite, captchaKey, crash, guildid, channelid,)).start()
    elif crash =="n":
        for x in range(int(threadAmount)):
            threading.Thread(target=generateToken, args=(proxylist, username, invite, captchaKey, crash,)).start()
    os.system("cls||clear")
    print(f"""{Fore.MAGENTA}
  {Fore.WHITE}╔{Fore.MAGENTA}█████{Fore.WHITE}╗{Fore.MAGENTA} ██{Fore.WHITE}╗{Fore.MAGENTA}      █████{Fore.WHITE}╗{Fore.MAGENTA} ███████{Fore.WHITE}╗{Fore.MAGENTA}████████{Fore.WHITE}╗{Fore.MAGENTA} ██████{Fore.WHITE}╗{Fore.MAGENTA} ██████{Fore.WHITE}╗{Fore.MAGENTA} ██████{Fore.WHITE}╗{Fore.MAGENTA} ██████{Fore.WHITE}╗{Fore.MAGENTA} 
  {Fore.WHITE}║{Fore.MAGENTA}█{Fore.WHITE}╔══{Fore.MAGENTA}██{Fore.WHITE}╗{Fore.MAGENTA}██{Fore.WHITE}║{Fore.MAGENTA}     ██{Fore.WHITE}╔══{Fore.MAGENTA}██{Fore.WHITE}╗{Fore.MAGENTA}██{Fore.WHITE}╔════╝╚══{Fore.MAGENTA}██{Fore.WHITE}╔══╝{Fore.MAGENTA}██{Fore.WHITE}╔════╝{Fore.MAGENTA}██{Fore.WHITE}╔═══{Fore.MAGENTA}██{Fore.WHITE}╗{Fore.MAGENTA}██{Fore.WHITE}╔══{Fore.MAGENTA}██{Fore.WHITE}╗{Fore.MAGENTA}██{Fore.WHITE}╔══{Fore.MAGENTA}██{Fore.WHITE}╗{Fore.MAGENTA}
  {Fore.WHITE}║{Fore.MAGENTA}█████{Fore.WHITE}╔╝{Fore.MAGENTA}██{Fore.WHITE}║{Fore.MAGENTA} :)  ███████{Fore.WHITE}║{Fore.MAGENTA}███████{Fore.WHITE}╗{Fore.MAGENTA}   ██{Fore.WHITE}║{Fore.MAGENTA}   ██{Fore.WHITE}║{Fore.MAGENTA}     ██{Fore.WHITE}║{Fore.MAGENTA}   ██{Fore.WHITE}║{Fore.MAGENTA}██████{Fore.WHITE}╔╝{Fore.MAGENTA}██{Fore.WHITE}║{Fore.MAGENTA}  ██{Fore.WHITE}║{Fore.MAGENTA}
  {Fore.WHITE}║{Fore.MAGENTA}█{Fore.WHITE}╔══{Fore.MAGENTA}██{Fore.WHITE}╗{Fore.MAGENTA}██{Fore.WHITE}║{Fore.MAGENTA}     ██{Fore.WHITE}╔══{Fore.MAGENTA}██{Fore.WHITE}║╚════{Fore.MAGENTA}██{Fore.WHITE}║{Fore.MAGENTA}   ██{Fore.WHITE}║{Fore.MAGENTA}   ██{Fore.WHITE}║{Fore.MAGENTA}     ██{Fore.WHITE}║{Fore.MAGENTA}   ██{Fore.WHITE}║{Fore.MAGENTA}██{Fore.WHITE}╔══{Fore.MAGENTA}██{Fore.WHITE}╗{Fore.MAGENTA}██{Fore.WHITE}║{Fore.MAGENTA}  ██{Fore.WHITE}║{Fore.MAGENTA}
  {Fore.WHITE}║{Fore.MAGENTA}█████{Fore.WHITE}╔╝{Fore.MAGENTA}███████{Fore.WHITE}╗{Fore.MAGENTA}██{Fore.WHITE}║{Fore.MAGENTA}  ██{Fore.WHITE}║{Fore.MAGENTA}███████{Fore.WHITE}║{Fore.MAGENTA}   ██{Fore.WHITE}║   ╚{Fore.MAGENTA}██████{Fore.WHITE}╗╚{Fore.MAGENTA}██████{Fore.WHITE}╔╝{Fore.MAGENTA}██{Fore.WHITE}║{Fore.MAGENTA}  ██{Fore.WHITE}║{Fore.MAGENTA}██████{Fore.WHITE}╔╝{Fore.MAGENTA}
  {Fore.WHITE}╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ {Fore.WHITE}
                    Threads: [{threadAmount}] Invite: [{invite}]{Fore.MAGENTA}
                ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                ┃{Fore.WHITE}               downcord.org{Fore.MAGENTA}                ┃
                ┃{Fore.WHITE}          Discord Account Generator     {Fore.MAGENTA}   ┃
                ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")
    while True:
        try:
            print(f"{Fore.MAGENTA}                  Generated: [{verified}] Captchas solved: [{captchas}]")
            print(f"{Fore.RED}                  Proxy errors: [{proxyerror}] Captcha errors: [{captchaerror}]")
            time.sleep(0.1)
            for i in range(2):
                sys.stdout.write("\x1b[1A\x1b[2K")
        except KeyboardInterrupt:
            print(f"{Fore.WHITE}|>|{Fore.GREEN} Finished generating {verified} accounts")
            sys.exit()


main()
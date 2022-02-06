import sys
from random import choice
import httpx
import requests
from colorama import Fore,init
init(convert=True)
print(Fore.GREEN+"""
╭╮╭╮╭┳━━━┳━━╮╭╮╱╭┳━━━┳━━━┳╮╭━╮╭━━━┳━━━┳━━━┳━╮╭━┳━╮╭━┳━━━┳━━━╮
┃┃┃┃┃┃╭━━┫╭╮┃┃┃╱┃┃╭━╮┃╭━╮┃┃┃╭╯┃╭━╮┃╭━╮┃╭━╮┃┃╰╯┃┃┃╰╯┃┃╭━━┫╭━╮┃
┃┃┃┃┃┃╰━━┫╰╯╰┫╰━╯┃┃╱┃┃┃╱┃┃╰╯╯╱┃╰━━┫╰━╯┃┃╱┃┃╭╮╭╮┃╭╮╭╮┃╰━━┫╰━╯┃
┃╰╯╰╯┃╭━━┫╭━╮┃╭━╮┃┃╱┃┃┃╱┃┃╭╮┃╱╰━━╮┃╭━━┫╰━╯┃┃┃┃┃┃┃┃┃┃┃╭━━┫╭╮╭╯
╰╮╭╮╭┫╰━━┫╰━╯┃┃╱┃┃╰━╯┃╰━╯┃┃┃╰╮┃╰━╯┃┃╱╱┃╭━╮┃┃┃┃┃┃┃┃┃┃┃╰━━┫┃┃╰╮
╱╰╯╰╯╰━━━┻━━━┻╯╱╰┻━━━┻━━━┻╯╰━╯╰━━━┻╯╱╱╰╯╱╰┻╯╰╯╰┻╯╰╯╰┻━━━┻╯╰━╯
                              -https://github.com/Terminal1337""")


proxy = ""
with open("proxies.txt",'r') as f:
    proxy = "http://" + choice(f.readlines()).strip()

webhook = input(Fore.RED+"Enter the Webhook Url: ")
msg = input(Fore.CYAN+"Enter the message: ")
tyme = int(input(Fore.BLUE+"Enter the number of times to spam: "))


def proxy_spam():
        req = httpx.post(webhook, json={'content': msg},proxies=proxy)
        if req.status_code == 204:
            print(Fore.GREEN+"Message Sent Successfully")
        else:
            print(Fore.WHITE+"Bad proxies or webhook")
            sys.exit()
def proxyless_spam():
        req = httpx.post(webhook, json={'content': msg})
        if req.status_code == 204:
            print(Fore.GREEN+"Message Sent Successfully")
        else:
            print(Fore.WHITE+"Bad proxies or webhook")
            sys.exit()

support = input(Fore.LIGHTYELLOW_EX+"Do you want to enable proxy mode?(Y/n): ")

if support == "Y":
    for i in range(tyme):
        proxy_spam()
elif support == "n":
    for i in range(tyme):
        proxyless_spam()
else:
    sys.exit()

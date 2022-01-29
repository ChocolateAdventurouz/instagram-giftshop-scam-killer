"""
Instagram GiftShop Scam Killer

Protect your Instagram account from the giftshop phising site

Made with Love from SecurityRaven
"""
import os
from socket import socket
import time
import sys
from urllib import request
import requests
import requests
from requests.adapters import HTTPAdapter
local = "127.0.0.1"
hosts = "C:/Windows/System32/drivers/etc/hosts"
i = 0000
file_in = open("temp.txt", "w+")

os.system("cls")
print("Instagram GiftShop Scam Killer")
for i in range(9999):
    i = i+1
    url = "giftshop"+ str(i) + ".buzz "
    f = url.split()
    with open(hosts,'r+') as file:
        content = file.read()
        for site in f:
            if site in content:
                pass
            else:
                file.write(local+"  "+site+"\n")
print("Finished!")
sys.exit()
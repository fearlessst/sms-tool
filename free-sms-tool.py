#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from os import system as s



banner = """
    TR "Türkçe"
| İstediginiz telefon adresine hergun 1 defa mesaj atma hakkınız vardır 
| Mesajınız karakter sayısı sınırlı bunu mesajınızı yazdıktan sonra görüceksiniz.
| Tel adresinizi Doğru girmezseniz hata alabilrsiniz.
| Star atmayı Unutmayın.

    En "English
| You have the right to send a message to the phone address you want once a day.
| Your message is limited in number of characters, you will see this after you write your message.
| If you do not enter your phone address correctly, you may receive an error.
| Don't forget to throw stars.
"""

print(banner)

sor = input("Tel adresi Örn:+905555555555 >>> ")

mesaj = input("Mesajınız >>> ")

arlk = mesaj[0:70]

print("\n| Mesajınızın Gönderilebilecek kısmı aşagıdaki gibidir.\n"+arlk)

drlm = input("\n| Mesajınız Gönderilsinmi?[y/n] >>> ")

if drlm == "y" or drlm == "Y":
    print("\n"+sor+"\n"+arlk+"\n")
    resp = requests.post('https://textbelt.com/text', {
  'phone': sor,
  'message': arlk,
  'key': 'textbelt',
    })
    print(resp.json())

elif drlm == "n" or drlm == "N":
    quit()
else:
    print("\n|Hata yaptınız.")


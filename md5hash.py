#!/usr/bin/env python

from termcolor import colored
import hashlib

def tryOpen(wordlist):
    global pass_file
    try:
        pass_file = open(wordlist, "r")
    except:
        print(colored("[!!] Dosya Konumu yanlış..", "red"))
        quit()

hashGir = input("String girin: ")
wordlist = input("wordlist Konumu girin: ")

tryOpen(wordlist)

for word in pass_file:
    print(colored("[?] Uğraşıyorum: " + word.strip("\n"), "red"))
    enc_word = word.encode("latin-1")
    md5Digest = hashlib.md5(enc_word.strip()).hexdigest()
    if md5Digest == hashGir:
        print(colored(f"[+] Password: {word}", "green"))
        exit()
print("[!!] Dosyada Şifre bulunmadı...")
#!/usr/bin/env python3

import requests
import sys

#Replace "list.txt"with the path for the wordlist that you want to use.
wordlist = open("list.txt").read()
subdomains = wordlist.splitlines()

for i in subdomains:
        url = f"http://{i}.{sys.argv[1]}"
        print("Testing: " + url)

        try:
                requests.get(url)
        except requests.ConnectionError:
                pass

        else:
                print("Subdomain found: " + url)

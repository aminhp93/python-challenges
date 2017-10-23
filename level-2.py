data = open('resources/level-3.txt').read()

import urllib.request
import re

html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().decode()

data = re.findall("<!--(.*?)-->", html, re.DOTALL)[-1]


result = re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data)

print("".join(result))
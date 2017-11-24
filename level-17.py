# from urllib.request import urlopen
# from urllib.parse import unquote_plus, unquote_to_bytes
# import re, bz2

# num = '12345'
# info = ''
# while(True):
#     h = urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='+num)
#     raw = h.read().decode("utf-8")
#     print(raw)
#     cookie = h.getheader("Set-Cookie")
#     info += re.search('info=(.*?);', cookie).group(1)
#     match = re.search('the next busynothing is (\d+)', raw)
#     if match == None: 
#         break
#     else:
#         num = match.group(1)
# res = unquote_to_bytes(info.replace("+", " "))
# print(res)
# print(bz2.decompress(res).decode())

# from xmlrpc.client import ServerProxy

# conn = ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")

# print(conn.phone("Leopold"))

from urllib.request import Request, urlopen
from urllib.parse import quote_plus

url = "http://www.pythonchallenge.com/pc/stuff/violin.php"
msg = "the flowers are on their way"
req = Request(url, headers = { "Cookie": "info=" + quote_plus(msg)})

print(urlopen(req).read().decode())
from urllib.request import urlopen
raw = urlopen("http://www.pythonchallenge.com/pc/def/banner.p").read()
# print(raw)

import pickle
data = pickle.load(urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))

for line in data:
	print("".join([k * v for k, v in line]))
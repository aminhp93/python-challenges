import re
import requests
from io import BytesIO
from PIL import Image

img = Image.open(BytesIO(requests.get('http://www.pythonchallenge.com/pc/def/oxygen.png').content))

# img.width
# img.height
# img.getpixel((0, 0))

row = [img.getpixel((x, img.height/2)) for x in range(img.width)]

row = row[::7]

ords = [r for r, g, b, a in row if r == g == b]

nums = re.findall("\d+", "".join(map(chr, ords)))

result = "".join(map(chr, map(int, nums)))

print(result)
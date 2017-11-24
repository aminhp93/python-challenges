# from PIL import Image, ImageChops

# image = Image.open("resources/mozart.gif")

# max(enumerate(image.histogram()), key=lambda x: x[1])

# tmp = image.copy()
# tmp.frombytes(bytes([60] * (tmp.height * tmp.width)))
# tmp.show()

# [x for x in image.histogram() if x % image.height == 0 and x != 0]

# image.histogram().index(2400)

# tmp.frombytes(bytes([195] * (tmp.height * tmp.width)))
# tmp.show()

# import numpy as np
# shifted = [bytes(np.roll(row, -row.tolist().index(195)).tolist()) for row in np.array(image)]

# Image.frombytes(image.mode, image.size, b"".join(shifted)).show()

from PIL import Image, ImageChops
import numpy as np
image = Image.open("resources/mozart.gif")
shifted = [bytes(np.roll(row, -row.tolist().index(195)).tolist()) for row in np.array(image)]
Image.frombytes(image.mode, image.size, b"".join(shifted)).show()
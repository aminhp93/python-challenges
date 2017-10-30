data = open("resources/evil2.gfx", "rb").read()

for i in range(5):
	open('resources/%d.jpg' % i, 'wb').write(data[i::5])

# Result: disproportional

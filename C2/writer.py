file = open('map.dat','w')
text = ""
map = []
for i in xrange(0,8):
	map.append([])
	for n in xrange(0,8):
		map[i].append(raw_input("N" + str(i) + "," + str(n)))
file.write(str(map))
file.close()

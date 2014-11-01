file = open('mapGraph2.dat','w')
#map = file.read()
text = ""
map = [[[0,0],[0,1]]]
while raw_input("More") == "":
	map.append(input("Vertex:"))
file.write(str(map))
file.close()

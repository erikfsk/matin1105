def f():
	with open("test.txt","r") as infile:
		#automatic closing of infile
		#2
		print(infile.readlines())
		for line in infile:
		#2
			print(line)
			for word in line.split():
				print(word)

	print("alternativ")
	infile = open("test.txt","r")

	#2
	lines = infile.readlines()
	print(lines)
	#2
	for line in lines:
		print(line)
		words = line.split()
		for word in words:
			print(word)
	#not automatic closing of infile
	infile.close()


f()
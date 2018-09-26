def f():
	with open("test.txt","r") as infile:
		#automatic closing of infile
		
		# print(infile.readlines())
		# #infile du e på linje -1
		#2
		for line in infile:
		#2
			print(line)
			for word in line.split():
				print(word)

	print("alternativ")
	infile = open("test.txt","r")

	#2
	infile.readline()
	infile.readline()
	lines = infile.readlines()
	print(lines)
	for line in lines:
	#2
		print(line)
		words = line.split(" ")
		print(words)
		for word in words:

			print(type(float(word)),word)

	# print(dir(infile))
	#not automatic closing of infile
	infile.close()




from numpy import * 
v0 = 1
g = 1
t = 1
a = ones(10)*v0 + g*t
print(a)


a = [1,2,3]
print(a*5)
for i in range(10):
	a.append(12)

print(a)






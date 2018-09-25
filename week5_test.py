def f():
	with open("test.txt","r") as infile:
		#automatic closing of infile
		#2
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
	for line in lines:
	#2
		print(line)
		words = line.split()
		for word in words:
			print(type(word),word)

	# print(dir(infile))
	#not automatic closing of infile
	infile.close()
f()
from numpy import * 
a = ones(10)
print(a*10 + 2)


a = []
for i in range(10):
	a.append(12)

print(a)
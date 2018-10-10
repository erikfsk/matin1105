# for i in range(2, 5):
# 	print(i, end = ' ') 
# 	#i = 2,3,4    
# 	for j in range(i-1, i+1):
# 		#i = 2, j = 1
# 		#i = 3, j = 2
# 		#i = 4, J = 3
# 		# 2 1 3 2 4 3
# 		if  i != j:
# 			# range(5) = range(0,5,1)
# 			# print(j) = print(j,end="\n")
# 			print(j, end = ' ')

# s = -2
# for k in range(2):
# 	#k = 0,1
# 	#s = -2, 0 2
# 	s += 2
# print(s)


# import numpy as np

 

# def fibonacci(N=3):
# 	# N = 2
#     x = np.zeros(N+1, int) # [0 0 0]
#     x[0] = 1 # [1 0 0]
#     x[1] = 1 # [1 1 0]
#     for n in range(2,3):
#     	#n = 2 
#         x[n] = x[n-1] + x[n-2] #[1 1 2]
#     return n, x[n] # n = 2, x[n] = 2

 

# print(fibonacci(N=2))

# import numpy
# print(len(numpy.ones(3)+numpy.ones(3)))
# # Adding two Numpy arrays of length n will result in an array of length 2n.
# print(numpy.sin(2))
# # The call numpy.sin(2) will give an error message, since 2 is not an array.
# # !for
# # Vectorization means to avoid explicit for-loops in the code.

# # Numpy arrays can only be used for storing numbers.

# print(type(numpy.array(["erik"])))




# [0]*5 = [0]+[0]+[0]+[0]+[0] = [0,0,0,0,0]
# list(range(2))+list(range(3)) = [0,1] + [0,1,2] = [0,1,0,1,2]
# [2,3]+[0,2,3] = [2,3,0,2,3]
# [e**2 for e in range(1,5)] = range(1,5) = [1,2,3,4] = [1,4,9,16]

# import numpy as np

# a = np.linspace(0, 5, 1) # a =  [0]


# a_new = np.zeros(len(a)+1) #a_new = [0,0]
# for i in range(len(a)): #range(len(a)) = range(1)
# 	#i = 0
# 	a_new[i] = a[i] #[1,0]
# a_new[-1] = 6.0 # a_new = [1,6.0]
# a.append(6.0)

# # print(a)
# # # #
# # # # 
# #				0		1		2		3
# dna_list = ['GGTAG', 'GGTAC', 'GGTGC']
# #len(dna_list) = 3
# print(dna_list[len(dna_list)])


from math import *

def num_diff(f,x,h=1e-6):
	x =  pi # lokal_x = pi
	return (f(x+h)-f(x))/h

# d = num_diff(sin(),pi,h=1e-6) # ->  missing argument
d = num_diff(sin,pi) 			# ->  RIGHT  
# d = num_diff(sin(x),pi,1e-6)	# ->  x is an unknown variable 
# d = num_diff(sin(pi)) 		# ->  missing argument

# Select one alternative:

# None of them.
# d = num_diff(sin(),pi,h=1e-6)
# d = num_diff(sin,pi)
# d = num_diff(sin(x),pi,1e-6)
# d = num_diff(sin(pi))

# print(0.0000000000000000001 * 10**20)
# q = -0.15
# print("%.1f" % q)

# for i in range(-2, 6, 3):
# 	#i -2,1,4
# 	# i -1 = -3,0,3 
# 	print(i-1)
# print(i-1)



# a = 11
# b = 10/a + 1
# print(b) #= 1.9090909090909090


# A = [-1, 1, 5] + ["plot1.eps", "plot2.png"] # = [-1, 1, 5, "plot1.eps", "plot2.png"]
# del A[1]  									# = [-1, 5, "plot1.eps", "plot2.png"]
# print(type(A)) 								# = [-1, 5, "plot1.eps", "plot2.png"]


# #.    0  1. 2. 3  4   5.   6 
# #.    -7 -6 -5 -4 -3 -2 -1 
# A = [-1, 9, 2, 5, 19, 21, 33] # [5,19]
# print(A[3:-2])


# integers = []
# value = 0
# stop = 1
# increment = 1
# while value <= stop: #value <= 1
# 	#value = 0, 1
# 	integers.append(value) # = [0,1]
# 	value += increment
# for v in integers:
# 	print(v) # 0 \n1


# print([0.2*(i+1) for i in range(2)])

# x = []
# for i in range(2):
# 	# i = 0,1
# 	# 0.2*(i+1) = 0.2,0.4
# 	x.append(0.2*(i+1)) # [0.2] [0.2,0.4]

# print(x) # [0.2,0.4]


# from math import sqrt
# def f(x):
# 	return a*sqrt(x)
# x = 6; a = -2
# print("%g" % 200000)




# for i in range(2, 4):
# 	#i = 2,3
# 	for j in range(2,5):
# 		#i = 2, j = 3,4
# 		#i = 3, j = 2,4
# 		if i != j:
# 			print(i, j+1)
# 			#i = 2, j = 1,3
# 			#i = 3, j = 2,4
# 			#2 2
# 			#2 4
# 			#3 3 
# 			#3 5


def func1(x, y):
	if x > 0:
		print("quadrant I or IV")
	if y > 0:
		print("quadrant I or II")
def func2(x, y):
	if x > 0:
		print("quadrant I or IV")
	elif y > 0:
		print("quadrant II")

for x, y in (-1, 1), (1, 1):
	func1(x,y)
	
	func2(x,y)
	#"quadrant I or II"
	#"quadrant II"
	#"quadrant I or IV"
	#"quadrant I or II"
	#"quadrant I or IV"




























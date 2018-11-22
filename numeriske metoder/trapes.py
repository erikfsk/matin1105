# -*- coding=utf-8 -*-
from numpy import *

#notice that higher numbers give an integral closer to exact, see second part :) 
delintervaller = 4

def f(x):
	return x**3

#calculate all the values
x_array = linspace(0,2,delintervaller+1)
y_array = f(x_array)

#do you like numpy? 
integral = sum(x_array[1]*(y_array[1::]+y_array[:-1:])/2)
print(integral)

#important part for exam
#maybe lists are more your thing? 
integral = 0
for i in range(len(y_array)-1):
	integral += x_array[1]*(y_array[i]+y_array[i+1])/2
print(integral)



#second part: just for nørds
def trapes(delintervaller,f=f):
	#calculate all the values
	x_array = linspace(0,2,delintervaller+1)
	y_array = f(x_array)

	#do you like numpy? YES
	integral = sum(x_array[1]*(y_array[1::]+y_array[:-1:])/2)
	return integral

print("%-3s %-10s %s" % ("n","approx","error"))
for i in range(4,53,12):
	print("%-3d %-10.7f %.7f"%(i,trapes(i),abs(trapes(i)-4)))

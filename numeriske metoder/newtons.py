from numpy import * 
from matplotlib.pyplot import *

def f(x):
	return sin(x)

def df(x):
	return cos(x)

#notice that pi/2 will not give an answer, why? 
#notice that our answer is 4 pi, while the closest zero is at pi, why?
#how can we get pi? HINT: better starting point, aka closer to the zero point
x_start = pi/1.9
x_n = x_start

#variables for while loop
n = 100; i = 0; exact = pi; tol = 1e-15


#important part for exam
while i < n and abs(x_n%exact) > tol:
	x_n -= (f(x_n)/df(x_n))
	i +=1
	print("%-4d %-7.2f %.2f" % (i,x_n,abs(x_n%exact)))
print("%-4d %-7.2f %.2f" % (i,x_n,abs(x_n%exact)))


x_list = linspace(0,4.5*pi,1000)
plot(x_n,0,"o",label="Newton")
plot(x_start,f(x_start),"o",label="Start")
plot(x_list,f(x_list),label="exact function")
legend(loc="best")
show()
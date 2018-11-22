from math import factorial
from numpy import * 
from matplotlib.pyplot import *

def df(x,n):
	#pick a nice function with repeating df
	if (n-1)%4 == 0:
		return cos(x)
	elif (n-2)%4 == 0:
		return -sin(x)
	elif (n-3)%4 == 0:
		return -cos(x)
	elif n%4 == 0:
		return sin(x)

#important for the exam!
def taylor(x,a,n,df=df):
	taylor_sum = 0
	for k in range(n):
		taylor_sum += (df(a,k)/factorial(k))*(x-a)**k
	return taylor_sum


#exact solution
x = linspace(0,2*pi,1000)
y_exact = sin(x)

#just to show the result
for n in range(3,10,1):
	y_taylor_approx = taylor(x,pi/2,n)
	plot(x,y_taylor_approx,label="Taylor n=%d" % n)
plot(x,y_exact,label="Exact")
ylim(-1.2,1.2)
legend(loc="best")
show()
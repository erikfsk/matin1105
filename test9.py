from numpy import *
from matplotlib.pyplot import *


def f(t,x):
	return (-x*sin(t))+sin(t)

def eulers(t_k1,x_k,h):
	return x[-1]+h*f(t_i-h,x[-1])

def eulers_midpoint(t_k1,x_k,h):
	x_midpoint_value = x_k+0.5*h*f(t_k1-h,x_k)
	return x_k+h*f(t_k1-0.5*h,x_midpoint_value)

for n in [1,2,5,10]:
	#t values
	t = linspace(0,2*pi,n+1)
	
	#initial values
	h = t[1]; x0 = 2 + exp(1)
	
	#starting solution lists
	x_midt = [x0];x = [x0];
	for t_i in t[1::]:
		#euler
		x.append(eulers(x[-1],t_i,h))
		#eulers midtpunkt
		x_midt.append(eulers_midpoint(t_i,x_midt[-1],h))

	#plot both results
	plot(t,x,label="n=%d"%n)
	if n == 1 or n == 5:
		plot(t,x_midt,label="n=%d midpoint"%n)

legend()
ylim(1,5)
show()
from numpy import *
from matplotlib.pyplot import *


def f(t,x):
	return (-x*sin(t))+sin(t)

def eulers(t_k,x_k,h):
	return x_k+h*f(t_k,x[-1])

def eulers_midpoint(t_k,x_k,h):
	x_midpoint_value = x_k+0.5*h*f(t_k,x_k)
	return x_k+h*f(t_k+0.5*h,x_midpoint_value)

for n in [1,2,5,10]:
	#t values
	t = linspace(0,2*pi,n+1)
	
	#initial values
	h = t[1]; x0 = 2 + exp(1)
	
	#starting solution lists
	x_midt = [x0];x = [x0];
	for t_k in t[:-1:]:
		#euler
		x.append(eulers(t_k,x[-1],h))
		#eulers midtpunkt
		x_midt.append(eulers_midpoint(t_k,x_midt[-1],h))

	#plot both results
	print("-"*40)
	plot(t,x,label="n=%d"%n)
	print("%-15s n=%-10d f_eval=%-10d" % ("euler",n,n))
	if n == 1 or n == 5:
		plot(t,x_midt,label="n=%d midpoint"%n)
		print("%-15s n=%-10d f_eval=%-10d" % ("midpoint",n,2*n))

legend()
ylim(1,5)
show()
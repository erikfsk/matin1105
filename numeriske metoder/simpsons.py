from numpy import *


delintervaller = 4
#function to integrate
def f(x):
	return x**3

#calculate all the values
x_array = linspace(0,2,2*delintervaller+1)
y_array = f(x_array)

#do you like numpy? 
#integral = f(a) + f(b) + sum(4*f(x_2i)) + sum(2*f(x_2i-1))
integral = y_array[0] + y_array[-1] + sum(4*y_array[1:-1:2])+sum(2*y_array[2:-1:2])
integral = (x_array[1]/3)*integral
print(integral)

#important part for exam
#maybe lists are more your thing? 
integral = (y_array[0]+y_array[-1])
for i in range(1,len(y_array)-3,2):
	integral += (4*y_array[i]+2*y_array[i+1])
integral += (4*y_array[-2])
integral *= (x_array[1]/3)
print(integral)



#second part: nørds only
def simpsons(delintervaller,a=0,b=2,f=f):
	#calculate all the values
	x_array = linspace(a,b,2*delintervaller+1)
	y_array = f(x_array)

	#do you like numpy? 
	#integral = f(a) + f(b) + sum(4*f(x_2i)) + sum(2*f(x_2i-1))
	integral = y_array[0] + y_array[-1] + sum(4*y_array[1:-1:2])+sum(2*y_array[2:-1:2])
	integral = (x_array[1]/3)*integral
	return integral


#example with cos, page 315 in the compendium
exact = sin(1)
print("%-3s %-10s %s" % ("n","approx","error"))
for i in range(4,53,12):
	print("%-3d %-10.7f %.7f"%(i,simpsons(i,f=cos,b=1),abs(simpsons(i,f=cos,b=1)-exact)))



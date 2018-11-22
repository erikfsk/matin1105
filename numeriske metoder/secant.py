from numpy import * 
from matplotlib.pyplot import *

def f(x):
	return sin(x)

#notice that pi/2 will not give an answer, why? 
#notice that our answer is 4 pi, while the closest zero is at pi, why?
#how can we get pi? HINT: better starting point, aka closer to the zero point

x_start = pi/2
x_start2 = 3.5*pi/2
x_n = x_start
x_n1 = x_start2

#variables for while loop
n = 100; i = 0; exact = pi; tol = 1e-15

steps = []
y_steps = []
#important part for exam
while i < n and abs(x_n%exact) > tol:
	x_term = x_n1 - ((x_n1-x_n)/(f(x_n1)-f(x_n)))*f(x_n1)

	#change the one with the same sign -+
	if f(x_term) < 0:
		x_n1 = x_term
	elif f(x_term) > 0:
		x_n = x_term
	i +=1
	steps.append(x_term)
	y_steps.append(f(x_term))
	print("%-4d %-7.2f %.2f" % (i,x_n1,abs(x_n-pi)))


x_list = linspace(0,2*pi,1000)
ax = subplot(111)
for axis in ['top','bottom','left','right']:
	ax.spines[axis].set_linewidth(1.5)
plot([x_start,x_start2],[f(x_start),f(x_start2)],"o",label="Start")
#showing the first step visually
plot([x_start,x_start2],[f(x_start),f(x_start2)],"--",color="orange")
plot([steps[0],steps[0]],[0,f(steps[0])],"--",color="orange")
plot([0,2*pi],[0,0],"--",color="orange",label="First step")
plot([steps[0]],[0],"*",color="red")
#exact solution
plot(x_list,f(x_list),"g--",label="exact function")
#all the steps
plot(steps,y_steps,"ro",label="steps")
#final step
plot(x_n1,0,"go",label="Final point")
tick_params(labelsize=20, direction='in',top=True,right=True,left=True,bottom=True,length=5)
legend(loc="best",fontsize=15)
yticks(fontsize=20)
xticks(fontsize=20)
tight_layout()
show()
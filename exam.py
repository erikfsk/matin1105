print("---------------------")
print("1a)")
a = 4
b = a
a = a+b
print(a) # 8 

print("---------------------")
print("1b)")
A = [[-1,0,1],[0,0,0],[10,9,8]]
print(A[1][-1]) # 0

print("---------------------")
print("1c)")
x = 6
y = -2
c = x >= 10 or y != -2
print(c) #False

print("---------------------")
print("1d)")
import numpy as np
a = [1,2,3]
a_np = np.array(a)
print(a*2) # [1,2,3,1,2,3]
print(a_np*2) # [2,4,6]

print("---------------------")
print("1e)")
S = 0
for i in range(3):
    S += i**2
print(S) #5

print("---------------------")
print("1f)")
import sys
A = [['-1','0','1'],['0','0','0'],['10','9','8']]
try:
    b = int(A[2])
except IndexError:
    print('A has length %d' %len(A))
    # sys.exit(1)
except TypeError:
    print('Cannot convert %s to int' %A[2])
    #sys.exit(1)
#print(b)

print("---------------------")
print("1g)")
def poly(x,k):
    s = 0
    for i in range(3):
        s = s+2.0**i
    return s
 
def test_poly():
    k = 2
    x = 2.0
    
    tol = 1e-14
    success = abs(poly(2.0,2)-7.0) < tol
    assert success
 
test_poly()

print("---------------------")
print("1h")
success = True
if success:
    None
else:
    raise AssertionError

assert success

print("---------------------")
print("2a")

infile = open("data.txt","r")
infile.readline()
year = []
mean_t = []
min_t = []
max_t = []
for line in infile:
    words = line.split()
    year.append(int(words[1]))
    mean_t.append(float(words[2]))
    min_t.append(float(words[3]))
    max_t.append(float(words[4]))



print("---------------------")
print("2b")

import matplotlib.pyplot as plt
plt.plot(year,mean_t,label="mean")
plt.plot(year,min_t, label="min")
plt.plot(year,max_t,label="max")
plt.legend()
plt.xlabel("Year")
plt.ylabel("T (degrees)")
#plt.show()


print("---------------------")
print("3a")

def piecewise(x,a,b):
    if x < a:
        return 0.0
    elif x < b:
        return (x-a)/(b-a)
    else:
        return 1.0


print("---------------------")
print("3b")

def test_piecewise():
    a = 0.0; b = 1.0;
    x1 = -1; x2 = 0.5; x3 = 1.5
    e1 = 0.0; e2 = 0.5; e3 = 1.0
    tol = 1.0e-10
    success1 = abs(piecewise(x1,a,b) - e1) < tol
    success2 = abs(piecewise(x2,a,b) - e2) < tol
    success3 = abs(pieceswise(x3,a,b) - e3) < tol
    assert success1 and success2 and success3



print("---------------------")
print("3c")

import sys
try:
    x, a, b = sys.argv[1:]
    x = float(x)
    a = float(a)
    b = float(b)
except IndexError:
    print("You need to provide three command line arguments.")
    #sys.exit(1)
except ValueError:
    print("The command line arguments must be numbers.")
    #sys.exit(1)
# print(piecewise(x,a,b))


print("---------------------")
print("4a")
def pi_approx(n):
    s=0
    for k in range(1,n+1):
        s+=4*(-1)**(k+1)/(2.*k-1)
    return s
print(pi_approx(10))
print(pi_approx(100))

print("---------------------")
print("4b")
from numpy import*
from matplotlib.pyplot import*
n_verdier=[i for i in range(1,51)]
x=array(n_verdier)
#y=pi_approx(x)
y=[pi_approx(i) for i in x]
plot(x,y,'r-')
legend(['pi_approx'])
xlabel('n')
ylabel('pi_approx')
#show()
print("---------------------")









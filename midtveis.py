#tenk igjennom hva du tror dette programmet skriver ut.  

print("----------a--------")
for i in range(5):
	print(i,end="")

for i in range(0,5,1):
	print(i,end="")
print()
print("----------a--------")




print("----------b--------")
i = 0
while i < 5:
	print(i)
	i += 1
print("----------b--------")


print("----------c--------")
if 1 == 1:
	print(True)
elif 1 > 2:
	print(False)
print("----------c--------")


print("----------d--------")
success = True #False
assert True
assert 1 == 1
print("----------d--------")



print("----------e--------")
try:
	assert False
	print("Hei")
	assert 1 == 2 # blir denne brukt?
except AssertionError:
	print("AssertionError")
print("----------e--------")




print("----------f--------")
argument_global	= 500
argument = 500

def test_funksjon(argument_lokal,argument):
	argument = 50
	def hjelp_func():
		for i in range(100):
			if i == 10:
				argument_lokal2 = "10"*i
	hjelp_func()
	try:
		print(argument_lokal2)
	except NameError:
		print("TULLING")
	return argument

print(test_funksjon(100,100))


print(argument)  # hvilken verdi har argument? 
print(argument_global)
print("----------f--------")





print("----------g--------")
try:
	print(argument_lokal)
except NameError:
	print("argument_lokal er en lokal variabel som kun eksisterer i test_funksjon")
print("----------g--------")





print("----------h--------")
x = range(1, 17, 5) #[1,6,11,16]
y = x 				#[1,6,11,16]	

if_statement_og_x_y_verdier = [[x_ != y_ and x_ > y_ + 1, [x_,y_]]\
										 for x_ in [6,11] for y_ in [6,11]]


print("\n\n")
print("\n\n")
print("\n\n")
listen_min = []
for i in range(6,16,5):
	for j in range(6,16,5):
		print("i=",i,"j=",j)
		listen_min.append([i != j and i > j + 1, [i,j]])

print(listen_min)

print("\n\n")
print("\n\n")
print("\n\n")
min_liste = [i for i in range(3)]
print(if_statement_og_x_y_verdier)
print("----------h--------")




print("----------i--------")
from numpy import *
x = zeros(1)
x = ones(10)
print(x)
print(e**x[0],x*2)
x = linspace(0,5,6)
print(x)
print("----------i--------")




print("----------j--------")
outfile = open("test_test.txt","w")
outfile.write("hello world 3")
outfile.close()
if type(outfile)==type(1337):
	print(outfile)
	print(test_funksjon)
print("----------j--------")




print("----------k--------")
with open("test_test.txt","r") as infile:
	words = infile.readline().split()
	print(words[2])
print("----------k--------")



print("----------l--------")
try:
	infile.read()
	print(True)
except:
	None
print("----------l--------")





print("----------m--------")
x = [i for i in range(3)]
y = [2*j for j in x]
print(x + y)
print("----------m--------")




print("----------n--------")
from numpy import *
x = linspace(0,2,3)
y = linspace(0,4,3) 

print(x + y)
print("----------n--------")



print("----------o--------")
def h(x): return 1 if x >= 0 else 0

x = [0,-1,-2]
y = [0,1,2]

for x_i,y_i in zip(x,y):
	print(h(x_i),h(y_i))
	# 1 1 
	# 0 1
	# 0 1
print("----------o--------")



print("----------p--------")
if True == True: print(True,True)
if True == False: print(True,False)
if False == True: print(False,True)
if False == False: print(False, False)
print("----------p--------")


print("----------q--------")
success_1 = 1337 < 117
success_2 = 2 == abs(-2)
success_3 = type(1337.0) == type(117)
success_4 = type(1337) == type(117)

if success_2 == success_4: print("success_2 %s, success_4 %s" % (success_2,success_4))
if success_2 == success_3: print("success_2 %s, success_3 %s" % (success_2,success_3))
if success_1 == success_4: print("success_1 %s, success_4 %s" % (success_1,success_4))
if success_1 == success_3: print("success_1 %s, success_3 %s" % (success_1,success_3))
print("----------q--------")


#s,d,g,f,....

#s --> string
#g --> 20 = 2 * 10**1
#d --> digit 2.2 2
#f --> float 
print("%d %10g %s %-50.2f" % (2.5,2000000.0,"Erik",10.1234567890))
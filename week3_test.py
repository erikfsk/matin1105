def f1(x):
	if x == 0:
		return 0
	else:
		return 1

def f2(x):
	return [0,1][x!=0]

def f3(x):
	if x == 0:
		return 0
	return 1

print(1!=0)
print(True,1)
print("erik"*(True+True))

def test_f():
	assert f1(1) == 1
	assert f2(0) == 0
	assert f3(3) == 1

#....
test_f()
test_f
print(test_f())
print(test_f)
for i in range(3):
	print(f2(i))







# b = sys.argv[1] --> "1"
# b+b --> "11"
# b = float(sys.argv[1]) --> 1.0
# print(b+b) --> 2.0
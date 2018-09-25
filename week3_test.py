def f(x):
	if x == 0:
		return 0
	else:
		return 1

def f2(x):
	return [0,1][0]

print(1!=0)
print(True,1)
print("erik"*(True+True))


def f3(x):
	if x == 0:
		return 0
	return 1

def test_f():
	assert f(1) == 1
	assert f2(0) == 0
	assert f3(3) == 1

#....
test_f()







# b = sys.argv[1] --> "1"
# b+b --> "11"
# b = float(sys.argv[1]) --> 1.0
# print(b+b) --> 2.0
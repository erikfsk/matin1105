def f(x):
	if x <= 0:
		return 1
	return x*f(x-1)

for i in range(10):
	print(i,f(i))

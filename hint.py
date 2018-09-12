from math import pi

def func(x,n=5):
	c_list = [1]
	for i in range(1,n):
		term = -c_list[-1]*((x*x)/(2*i*(2*i - 1)))
		c_list.append(term)
	return sum(c_list)


def table():
	print("%-7s %-16d %-16d %-16d %-16d %d" % ("x",5,25,50,100,200))
	for x in [2,4,6,8,10]:
		print("%-7.3f" % (pi*x), end ='')
		for n in [5,25,50,100,200]:
			print(" %-15.3f " % func(x*pi,n), end ='')
		print()


if __name__ == '__main__':
	table()



from math import pi

def func(x,n=5):
	c_list = [1]
	for i in range(1,n):
		term = -c_list[-1]*((x*x)/(2*i*(2*i - 1)))
		c_list.append(term)
	return c_list


def table():
	print("%-7s %-16d %-16d %-16d %-16d %d" % ("x",5,25,50,100,200))
	for x in [2,4,6,8,10]:
		print("%-7.3f" % (pi*x), end ='')
		c_list_x = func(pi*x,200)
		for n in [5,25,50,100,200]:
			print(" %-15.3f " % sum(c_list_x[:n:]), end ='')
		print()


if __name__ == '__main__':
	table()

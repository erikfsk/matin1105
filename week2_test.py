def func():
	return True + True + False


# 0 1 2 3 4 .... max(python)
# 0.000000000000000009002

# 1.0000000000000000000003231
def test_func():
	assert 2 == func() #func = 1
	print("vi har testet!")

a = test_func
print(func())
a()

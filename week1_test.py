test_float = 10.0
test_int = 10
test_list = [10]
test_string = "erik"
print(test_string*test_int)
print(test_int*test_list)

a = 1.123456789
print("%.2f" % a,"euro") #NEI
print("%g euro" % a) #NEI, fordi dette ikke gir riktig antall desimaler
print("%.2f euro" % a) #JA



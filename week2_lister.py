t = [i for i in range(11)]
y = [i*i for i in t]


ty1 = [t,y]
ty2 = [[i,j] for i,j in zip(t,y)]


print( "t",t)
print( "y",y)
print( "ty1",ty1)
print( "ty2",ty2)
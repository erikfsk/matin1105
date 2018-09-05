t = [[1,2],[3,4],[5,6]]

for i in range(0,3,1):
	for j in range(2):
		print(t[i][j])

#------------------------------------------------------
#EKVIVALENT JEG HAR DYSLEKSI VÆR SNILL #2
t1 = [i for i in range(3)]


#EKVIVALENT JEG HAR DYSLEKSI VÆR SNILL #2
t2 = []
for i in range(1,4):
	t2.append(i)
#------------------------------------------------------



# print(t1,t2)
t1_t2_listen = [t1,t2]
t1_t2_listen_listen = [t1_t2_listen]
print(t1_t2_listen_listen)
print(t1_t2_listen_listen[0])
print(t1_t2_listen_listen[0][1])




#------------------------------------------------------
#EKVIVALENT JEG HAR DYSLEKSI VÆR SNILL #1
for i in range(3):
	print(t1_t2_listen_listen[0][0][i],t1_t2_listen_listen[0][1][i])

#EKVIVALENT JEG HAR DYSLEKSI VÆR SNILL #1
print(t1_t2_listen_listen[0][0][0],t1_t2_listen_listen[0][1][0])
print(t1_t2_listen_listen[0][0][1],t1_t2_listen_listen[0][1][1])
print(t1_t2_listen_listen[0][0][2],t1_t2_listen_listen[0][1][2])
#------------------------------------------------------






# t = [i for i in range(11)]
# y = [i*i for i in t]


# ty1 = [t,y]
# ty2 = [[t_i,y_i] for t_i,y_i in zip(t,y)]


# print( "t",t)
# print( "y",y)
# print( "ty1",ty1)
# print( "ty2",ty2)


# for i in range(len(ty1[0])):
# 	print(ty1[0][i],ty1[1][i])


# for i in range(len(ty2)):
# 	print(ty2[i][0],ty2[i][1])







"""

"""
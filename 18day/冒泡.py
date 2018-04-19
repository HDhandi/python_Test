list = [3,5,8,18,20,40,50,60]


for i in range(len(list)):
	for j in range(i+1,len(list)):
		if list[i]> list[j]:
			list[i],list[j] = list[j],list[i]

print(list)

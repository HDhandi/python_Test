list = [1,3,5,8,10,20,21,30,34,47,90]

key = 21

center = int(len(list)/2)

if key in list:
	while True:
		if list[center] > key:
			center = center - 1
		elif list[center] < key:
			center = center + 1
		elif list[center] == key:
			print('查找的数字是%d在索引的%d'%(key,center))
			break

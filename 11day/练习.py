a = '小李,小王,小青,小白蛇'
b = input('请输入一个名字')
if b in a :
	print('小白蛇在')
else:
	print('不在')



if b not in list(a):
	print('不在')
else:
	print('在')

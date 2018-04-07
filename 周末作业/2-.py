import random
a = random.randint(1,100)
for i in range(1,11):
	x = int(input('请输入一个数字'))
	if x>a:
		print('猜大了')
	elif x<a:
		print('猜小了')
	else:
		print('正确')
		break

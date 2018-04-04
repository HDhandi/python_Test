import random
c = random.randint(1,100)
i = 1
while i<=10:
	a = int(input('请输入猜测数字'))
	if a>c:
		print('超出范围')
	elif a<c:
		print('低于范围')
	else:
		print('猜对了！！')
		break
	i+=1

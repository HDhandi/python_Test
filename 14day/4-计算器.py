dAef jsq(a,b,c):
	if c == '+':
		z = a+b
		print('和是%0.2f'%z)
		
	elif c == '-':
		z = a-b
		print('差是%0.2f'%z)
	elif c == '*':
		z = a*b
		print('积是%0.2f'%z)
	elif c == '/':
		if b !=0:
			c = x/b
			print('商是%0.2f'%z)
		else:
			print('输入错误')


while True:


	a = float(input('请输入一个数字'))
	b = float(input('请再输入一个数字'))
	c = input('请输入+ - * /')
	jsq(a,b,c)





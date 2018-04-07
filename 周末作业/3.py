a = '123456'
b = '123456'
while True:
	x = input('请输入账号')
	y = input('请输入密码')
	if x==a and y==b:
		print('登录成功')
		break
	else:
		print('输入错误')
		

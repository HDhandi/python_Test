zhanghao = input('请输入账号')
mima = input('请输入密码')

if zhanghao == "123456" and mima == "abc":
    print("登录成功")


elif zhanghao != '123456' and mima == 'abc':
	print('账号错误，请重新输入')

elif zhanghao =='123456'and mima != 'abc':
	print('密码错误，请重新输入')
else:
	print('请重新输入账号和密码')

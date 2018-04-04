accout = '123456'
passwd = '123456'
money = '200000'

zhanghao = input('请输入账号')
mima = input ('请输入密码')
if (zhanghao == accout) and (mima == passwd):
    a_money = float(input('请输入取款金额'))
		qian = 200000 - a_money
    if money <= 0:
	print'您的账户余额不足'
	else:
	print('取款%f元，余额%f元'%(money,qian))
else:
	print'您输入的账户有误'


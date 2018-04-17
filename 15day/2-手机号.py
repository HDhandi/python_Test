def s_phone(phone):
	if phone.startswith('1') and len(phone) == 11:
		return True
	else:
		return False
	
phone = input('请输入手机号码')
result = check_phone(phone)
if result == False:
	print('手机号输入错误')
'''
phone2 = input('请输入手机号码')
result = check_phone(phone2)
if result = False:
	print('手机号输入错误')
'''

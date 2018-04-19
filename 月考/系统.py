list = []
def print_menu():
	#欢迎语
	print('欢迎使用本公司产品'.center(30,' '))
		
	#系统菜单
	print('超市管理系统HD1.0版本'.center(30,'*'))
	print('1.商品录入'.center(30,' '))
	print('2.商品查询'.center(30,' '))
	print('3.商品修改'.center(30,' '))
	print('4.商品删除'.center(30,' '))
	print('5.全部商品'.center(30,' '))
	print('6.退出系统'.center(30,' '))


def input_xm():
	while True:
		xm_number = int(input('请输入操作项目'))
		if xm_number == 1:
			add_num()
		elif xm_number ==2:
			find_num()
		elif xm_number == 3:
			update_num()
		elif xm_number == 4:
			del_num()
		elif xm_number == 5:
			all_num()
		else:
			break
		
def add_num():
	number = {}
	name = input('请输入商品名称')
	coding = int(input('请输入商品编码'))
	weight = float(input('请输入商品重量'))
	price = float(input('输入商品价格'))
	number['name'] = name
	number['coding'] = coding
	number['weight'] = weight
	number['price'] = price
	list.append(number)
	print('商品添加成功')


def find_num():
	coding =int( input('请输入要查询的商品编码'))
	flag = 0
	for temp in list:
		if coding == temp['coding']:
			print('商品名称:%s\n商品编码:%s\n商品重量%0.2f公斤\n商品价格%0.2f元\n'%(temp['name'],temp['coding'],temp['weight'],temp['price']))
			flag = 1
	if flag == 0:
		print('查无此商品')




def update_num():
	coding = int(input('请输入要修改的商品编码'))
	flag = 0 
	for temp in list:
		if coding == temp['coding']:
			flag = 1
			print('1.修改商品名称')
			print('2.修改商品编码')
			print('3.修改商品重量')
			print('4.修改商品价格')
			update_num = int(input('请输入要修改商品的编码'))			
			if update_num == 1:
				new_name = input('请输入新的商品名称')
				temp['name'] = new_name
			elif update_num == 2:
				new_coding = int(input('请输入新的商品编码'))
				temp['coding'] = new_coding
			elif update_num ==3:
				new_weight = float(input('请输入新的商品重量'))
				temp['weight'] = new_weight
			elif update_num == 4:
				new_price = float(input('请输入新的商品价格'))
				temp['price'] = new_price
			else:
				print('input is error')
	if flag == 0:
		print('没有此商品无需修改')



def del_num():
	coding =int(input('请输入要删除的商品编码'))
	flag = 0 
	for temp in list:
		if coding == temp['coding']:
			flag = 1
			list.remove(temp)
	if flag ==0:
		print('没有此商品无需删除')



	
print_menu()
input_xm()

find_num()

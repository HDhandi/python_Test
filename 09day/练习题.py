i = int(input('请输入一个数字'))
j = int(input('请输入一个数字'))
sum = 0
if i < j:
	for b in range (i,j+1):
		print(b)
		sum = sum+b

else:
	print('输入有误')

print(sum)

sum1 = 0
while i <= j:
	sum1 = sum1 + i
	i+=1

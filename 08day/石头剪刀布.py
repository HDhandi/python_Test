'''
1:石头
2.剪刀
3.布
'''
import random
while computer = random.randint(1,3)
	player = int(input('请输入1：石头 2：剪刀 3：步'))
   
	if (player==1 and computer==2) or (player==2 and computer==3) or (player==3 and computer==1):
	 print('手下败将')
	elif (player == computer):
     print('继续')
	elif (player==3 and computer==2) or (player==2 and computer==1) or (player==1 and computer==3):
     print('算你厉害')
  

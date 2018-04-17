import time
def play_game():
	for i in range(10):
		print('跑一百米')
		time.sleep(1)
	print('爸爸来了')
	result = kill()
	if result == '爸爸给你加油':
		print('赢得了比赛')
	else:
		print('go on play competition')



def kill():
	print('妈妈来了')

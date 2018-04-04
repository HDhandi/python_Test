money = float(input('请输入身价'))
nice = int(input('请输入颜值'))
high = float(input('请输入身高'))

if high>=180 or money>=1000000 or nice>=99:
    print('高富帅')

elif high<=180 or money>=1000000 or nice>=99:
    print('富帅')

elif high<=180 or money<=1000000 or nice>=99:
    print('帅')

elif high<=160 or money<=100 or nice<=60:
    print('矮矬穷')

import random
start=input('請輸入預設值開頭')
end=input('請輸入預設值結尾')
start=int(start)
end=int(end)
r=random.randint(start,end)
y=0
while True:
	y=y+1
	x=input('請猜數字')
	x=int(x)
	if r==x:
		print('猜對了喔')
		print('你總共花了',y,'次')
		break
	elif r<x:
		print('數字還更小點')
		print('你已經花了',y,'次')
	elif r>x:
		print('數字還更大點')
		print('你已經花了',y,'次')
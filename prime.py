#Prime Number

num =2
flag =0
for i in range(2,num):
	if num%i==0:
		flag=0
		break
	else:
		flag=1

if flag:
	print("Yes It's Prime number")
else:
	print("It's not a prime numner")

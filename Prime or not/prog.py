#Checking whether a number is Prime or not
n = int(input("Enter the number to be checked : "))
flag = 0

for i in range(2,n) :
	if n%i == 0 :
		print('\nGiven number is not a Prime Number!!')
		flag = 1
		break

if flag == 0 :
	print("\nGiven number is a Prime number!!")




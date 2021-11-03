#Check whether given number is an Armstrong Number

n     = int(input('Enter the number : '))
org_n = n 
Sum   = 0

while (n > 0) :
	lastDigit =  n%10
	Sum       += lastDigit*lastDigit*lastDigit
	n = n//10

if (Sum == org_n) :
	print('Yess!! You found a Armstrong Number.\n')
else :
	print('Noo..The number is not a Armstrong Number.\n')


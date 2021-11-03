#Reversing a given number
n = int(input("Enter the number : "))
rev = 0

while(n>0) :
	lastDigit = n%10
	rev = rev*10 + lastDigit
	n = n//10

print('The reversed number is : ', rev)


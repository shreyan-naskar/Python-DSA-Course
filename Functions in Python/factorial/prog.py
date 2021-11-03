#Calculating the Factorial
def Fact( n ) :
	factorial = 1

	if n == 0 :
		return 1

	else :
		for i in range(1,n+1):
			factorial = factorial*i

	return factorial

n = int(input("Enter the number : "))


print('\nThe Factorial of' , n , 'is : ', Fact(n))
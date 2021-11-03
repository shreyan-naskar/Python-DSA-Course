#Calculating the Binary-Coefficient
def Fact( n ) :
	factorial = 1

	if n == 0 :
		return 1

	else :
		for i in range(1,n+1):
			factorial = factorial*i

	return factorial

n    = int(input("Enter the Superscript : "))
r    = int(input("Enter the Subscript : "))

ans  = Fact(n)//(Fact(r)*Fact(n-r))

print('\nThe Binary Coefficient is : ', ans)
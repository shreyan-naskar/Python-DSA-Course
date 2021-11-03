#Generating a Pascal's Triangle
#Calculating the Factorial
def Fact( n ) :
	factorial = 1

	if n == 0 :
		return 1
	else :
		for i in range(1,n+1):
			factorial = factorial*i

	return factorial

n = int(input('Enter the number of rows : '))

print("Here's the Pascal's Triangle :\n")

for i in range(0,n+1) :
	for j in range(0,i+1) :
		print(Fact(i)//(Fact(j)*Fact(i-j)) , end = ' ')
	print('\n')


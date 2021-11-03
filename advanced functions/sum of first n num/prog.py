#Function to find the sun of first n Naturnal Numbers
def SumofN( n ) :
	Sum = 0

	for i in range(1 , n+1) :
		Sum += i
	return Sum

N = int(input('Enter the number : '))
print(SumofN( N ))


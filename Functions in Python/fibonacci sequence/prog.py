#Finding Fibonacci Sequence upto n terms.
def Fib( n ) :
	T1 		 = 0
	T2 		 = 1
	List_Fib = []
	for i in range(1 , n+1) :

		List_Fib.append(T1)

		nxtTerm = T1 + T2
		T1      = T2
		T2      = nxtTerm

	return(List_Fib)

n = int(input('Enter the number of terms to be generated : '))

print('\nList of Fibonacci Numbers', Fib(n))
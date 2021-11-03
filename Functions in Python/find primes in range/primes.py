#Finding all primes in a given range.
def isPrime( n ) :
	count = 0
	for i in range(2,n) :
		if n%i == 0 :
			count = 0
			break
		else :
			count = 1

	if count == 1 :
		return True
	else :
		return False


n = int(input('Enter the upper limit of Range : '))
List_of_Primes = []

for i in range(1,n+1) :
	if isPrime(i) :
		List_of_Primes.append(i)

print('\nList of prime numbers in the range 1 to', n, 'is : ', List_of_Primes)

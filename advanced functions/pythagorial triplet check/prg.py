#Function to check whether 3 given numbers form a Pythagorian Triplet
def CheckPT( a , b , c) :
	if ( (a*a == (b*b + c*c)) or (b*b == (a*a + c*c)) or (c*c == (a*a + b*b)) ) :
		return True
	else :
		return False

A = int(input('Enter a number : '))
B = int(input('Enter a number : '))
C = int(input('Enter a number : '))

print('\n')
if (CheckPT( A , B , C )) :
	print('Given numbers form a Pythagorian Triplet!!')
else :
	print('Given numbers do not form a Pythagorian Triplet!!')
print('\n')


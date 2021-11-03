#Generating a star pattern
n = int(input('Enter a number : '))

print("The Star would look like :\n")
for i in range(1,n+1) :
	for j in range(1,n-i+1) :
		print(' ',' ', end = '')
	for j in range(i,0,-1) :
		print('*',' ', end = '')
	for j in range(2,i+1) :
		print('*',' ', end = '')
	print('\n')


for i in range(n-1,0,-1) :
	for j in range(1,n-i+1) :
		print(' ',' ', end = '')
	for j in range(i,0,-1) :
		print('*',' ', end = '')
	for j in range(2,i+1) :
		print('*',' ', end = '')
	print('\n')

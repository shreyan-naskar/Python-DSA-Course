#Generating Half Pyramid Mirror
n = int(input('Enter the number of rows : '))

print('The Pattern would look like :\n')
for i in range(n,0,-1) :
	for j in range(1,i) :
		print(' ', end = ' ')

	for k in range(1,n-i+2) :
		print('*', end = ' ')

	print('\n')
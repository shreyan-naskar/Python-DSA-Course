#Generating a Rhombus
n = int(input('Enter the number of rows : '))

print('The Rhombus looks like :\n')
for i in range(1,n+1) :
	for j in range(1,n-i+1) :
		print(' ', end = '')
	for j in range(1,n+1) :
		print('*',' ', end = '')
	print('\n')

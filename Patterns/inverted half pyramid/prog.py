#Generating the Inverted Half Pyramid
n = int(input('Enter the number of rows : '))

print('Enter Inverted Half Pyramid looks like :\n')
for i in range(n,0,-1) :
	for j in range(1,i+1) :
		print('*', end = '')
	print('\n')
#Generating the Inverted half Number Pyramid
n = int(input('Enter the number of rows : '))

print('Enter Inverted Half Number Pyramid looks like :\n')
for i in range(n,0,-1) :
	for j in range(1,i+1) :
		print(j, end = '')
	print('\n')
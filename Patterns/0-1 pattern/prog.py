#Generating the 0-1 Pattern
n = int(input('Enter the number of rows : '))

print('The pattern looks like :\n')
for i in range(1,n+1) :
	for j in range(1,i+1) :
		if (i+j)%2 == 0 :
			print('1' , end = ' ')
		else :
			print('0' , end = ' ')
	print('\n')


#Generating a Zig-Zag pattern
n = int(input('Enter the number of rows :'))

print('The zig zag pattern looks like :\n')
for i in range(1,4) :
	for j in range(1,n+1) :
		if ((i+j)%4 == 0) :
			print('*',' ', end = '')
		elif (i == 2 and j%4 == 0) :
			print('*',' ', end = '')
		else :
			print(' ', end = '')

	print('\n')
#Generating a Hollow Rectangle
row = int(input('Enter the number of rows : '))
col = int(input('Enter the number of columns : '))

print("The Hollow Triangle look s like :\n")
for i in range(1,row+1) :

	for j in range(1,col+1) :
		if i == 1 or i == row :
			print("*", end = '')

		elif  j == 1 or j == col :
			print("*", end = '')

		else :
			print(" ", end = '')
	print('\n')
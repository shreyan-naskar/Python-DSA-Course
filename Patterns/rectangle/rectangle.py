#Generating a rectangle
row = int(input('Enter the number of rows : '))
col = int(input('Enter the number of columns : '))

print("The Triangle looks like :\n")
for i in range(1,row+1) :
	for j in range(1,col+1) :
		print('*', end = '\t')
	print('\n')
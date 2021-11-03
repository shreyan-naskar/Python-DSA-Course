#Generating the Floyd Triangle
n = int(input("Enter the number of rows : "))
v = 1

print('The Floyd Triangle would look like :\n')
for i in range(1,n+1) :
	for j in range(1,i+1) :
		print(v , end = ' ')
		v = v + 1 
	print('\n')
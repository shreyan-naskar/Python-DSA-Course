#Generating a Butterfly Pattern.
n = int(input('Enter : '))

print('The Butterfly Pattern would look like :\n')
for i in range(1,n+1) :
	for j in range(1,i+1) :
		print('*' , end = '\t')

	space = (2*n - 2*i)
	for j in range(1,space+1) :
		print(' ' , end = '\t')

	for j in range(1,i+1) :
		print('*' , end = '\t')
	
	print('\n')


for i in range(n,0,-1) :
	for j in range(1,i+1) :
		print('*' , end = '\t')

	space = (2*n - 2*i)
	for j in range(1,space+1) :
		print(' ' , end = '\t')

	for j in range(1,i+1) :
		print('*' , end = '\t')
	
	print('\n')


#Finging the largest number in a number string
n = input("Enter the number : ")
max_digit = 0

for i in n :
	if int(i) > max_digit :
		max_digit = int(i)

print(max_digit)

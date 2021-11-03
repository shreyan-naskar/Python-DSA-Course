'''
Palindrome: Given a string s, on reversing the string we get the same string we
call that string is a palindrome.

Algorithm:
1) Let the length of the character array be n.
2) Keep a boolean variable ans to store the result and initialize it with true.
2) Iterate over the string and check if i

th character is equal to (n-i-1)
th
, there can be

2 cases
a) If equal, then do nothing
b) If unequal, then put ans = false
3) When the loop ends, if ans is true, then the string is palindrome else it is not a
palindrome.
'''

n    = int(input('Enter the number : '))
List = []

for i in range(len(str(n))):
	List.append(str(n)[i])

check = 1
m     = len(List)

for i in range( m ) :
	if List[i] != List[m-1-i] :
		check = 0
		break

if check :
	print('Given is a Palindrome!!')
else :
	print('Given is not a Palindrome!!')
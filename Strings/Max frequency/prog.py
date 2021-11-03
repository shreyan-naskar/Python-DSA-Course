'''
Given a string s of latin characters, your task is to output the character which has
maximum frequency.

Approach:-
Maintain frequency of elements in a separate array and iterate over the array and
find the maximum frequency character.
'''

s = input("Enter the string : ")
D = {}
Freq_char = ''
Freq = 0

for i in s :
	if i not in D.keys() :
		D[i] = 1
	else :
		D[i] += 1

for i in D.keys() :
	if D[i] > Freq :

		Freq      = D[i]
		Freq_char = i

print("Most frequent character : ", Freq_char)
print("Frequency : ", Freq)




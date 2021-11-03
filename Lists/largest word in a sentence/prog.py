#Finding the largest in a given sentance
Sentance        = input('Enter the sentance : ')[0:-1]
List_of_words   = Sentance.split()
Max_len, Max_Ind = 0, 0

for i in range(len(List_of_words)) :
	if len(List_of_words[i]) > Max_len :
		
		Max_len = len(List_of_words[i])
		Max_Ind = i

print('Largest word in the sentance is : ', List_of_words[Max_Ind])
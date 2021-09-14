def minion_game(string):
    # your code goes here
	input_string1 = []
	input_string2 = []
	score1= []
	score2= []
	scorefor1 = 1
	x=10
	#input values in list
	#PLAYER 1 TURN:
	for x in range(0,10):
		g = input('Stuart: Enter substrings starting with vowels: ' + string + " ")
		input_string1.append(g)
		print('list: ', input_string1)
		#if first alphabet is vowel, 1 score is added..
		if g[0] == "a" or g[0] == "e" or g[0] == "i" or g[0] == "u" or g[0] == "u":
			score1.append(scorefor1)
			print("Score Player 1: " , score1)
			#else no score is added
		else:
			print("Not a vowel")




	#PLAYER 2 TURN
	for x in range(0,10):
		c = input('Kevin: Enter Vowels for ' + string + " ")
		input_string2.append(c)
		print('list: ', input_string2)

				#if first alphabet is constant, 1 score is added..
		if c[0] != "a" or c[0] != "e" or c[0] != "i" or c[0] != "u" or c[0] != "u":
			score2.append(scorefor1)
			print("Score Player 2: " , score2)
			#else no score is added
		else:
			print("Not a value ")

	print("Player 1 Score: ", sum(score1), "		Player 2 Score: ", sum(score2))

if __name__ == '__main__':
	
	minion_game("BANANA")
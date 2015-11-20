#Program for validating the weight and Height guesses

#Logical Schema

#First check for the legitimacy of the guesses in the form of non-Zero Inputs

#Then divide it to 3 blocks for the possible values of H and to make the logic exhaustive

#check for the weight conditions with in the H block and print the accuracy of the guesses

# Height and weight values are input
H = 176
W = 145
# User interface for the weight and height to be guessed
Gh = input('Enter your height guess: ')
Gw = input('Enter your weight guess: ')
# Initial block Initialization to check guess legitimacy(Close if Weight or height =0)
if Gh > 0:
	if Gw > 0:
	# Logical block 1 for checking if Guess for Height is more and for all possibilities
	# of weight within
		if Gh > H:
			if Gw > W:
				print("Both are Higher")
			elif Gw < W:
				print("One is Higher One is Lower")
			else:
				print("One is right One is not")
	# Logical block 2 for checking if Guess for Height is less and for all possibilities
	# of weight within
		elif Gh < H:
			if Gw < W:			
				print("Both are Lower")
			elif Gw > W:
				print("One is Higher One is Lower")
			else:
				print("One is right One is not")
	# Logical block 2 for checking if Guess for Height is less and for all possibilities
	# of weight within
		elif Gh == H:
			if Gw == W:
				print("Bingo")
			elif Gw > W:
				print("One is Higher One is Lower")
			else:
				print("One is right One is not")
				
	else:
		print("Game Over")
else:
	print("Game Over")
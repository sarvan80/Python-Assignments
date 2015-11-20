# Assignment 2

H = 176
W = 145

Gh = input('Enter your height guess: ')
Gw = input('Enter your weight guess: ')



# if (Gh == 0 / Gw == 0)/(Gh == 0 & Gw == 0):
if Gh > 0:
	if Gw > 0:
		if Gh > H & Gw > W:
			print("Both are Higher")
		elif Gh < H & Gw < W:			
			print("Both are Lower")	
		elif (Gh < H & Gw > W)/(Gh > H & Gw < W):
		    print("One is Lower")			
	else:
		print("Game Over")
else:
	print("Game Over")
       
# Alternative
Gh = input('Enter your height guess: ')
Gw = input('Enter your weight guess: ')
if Gh > 0:
	if Gw > 0:
		if Gh > H:
			if Gw > W:
				print("Both are Higher")
			elif Gw < W:
				print("One is Higher One is Lower")
			else:
				print("One is right One is not")
		elif Gh < H:
			if Gw < W:			
				print("Both are Lower")
			elif Gw > W:
				print("One is Higher One is Lower")
			else:
				print("One is right One is not")
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



# if var < 200:
  # print "Expression value is less than 200"
   #if var == 150:
    #  print "Which is 150"
  # elif var == 100:
   #   print "Which is 100"
  # elif var == 50:
   #   print "Which is 50"
# elif var < 50:
  # print "Expression value is less than 50"
# else:
  # print "Could not find true expression"

# print "Good bye!"
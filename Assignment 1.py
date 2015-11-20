
# Practise
print("Hello")
a=2
b=3
print("a+b",a+b)
# Program 1
# I = input('Enter your number of Inches: ')

print("b/a",b//a)

# Assignment 1
# Inches to miles,Yards,Feet

# Logical Framework-Convert Miles,Yards and Feet to Inches and then report the Inches 
# with the highest priority to the largest divisor(Miles in this case)

#Explanation - If the entered value is 100000;1st it is divided by 63360 and the quotient
# is reported as miles(Since there are 633690 Inches in a Mile) then the remainder is
# divided by 36 and reported as Yards(Since there are 36 Inches in a Yard) and then Finally
# the remainder is divided by 12 and reported as Feet(Since 12 inches are there in a feet)
# and the remaining inches are reported as Inches

# Key Aspect-Finding remainders in each step

 
# Get the input in terms of Inches
a = input('Enter your number of Inches: ')
# a=63365
M=a//63360
MR=a-M*63360

Y=MR//36
YR=MR-Y*36

F=YR//12
FR=YR-F*12

print('The Resulting Miles,Yards,Feet and Inches in the',a,'Inches is',M,Y,F,FR)


# Assignment 2

H = 176
W = 145

Gh = input('Enter your height guess: ')
Gw = input('Enter your weight guess: ')




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














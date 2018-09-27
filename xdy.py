import random

#use this program to roll any number of dice with any number of sides using the xdy format
#where x is the number of dice and y is any number of faces to those dice
 
x = int(input("How many die do you want to roll?  ") )
y = int(input("How many sides does your dice have?  ") )
 
for i in range(1,x+1):
    print(random.randint(1,y))

#This is my code for girl scout   

import turtle

#print ("HI") 

savannah=turtle.Turtle()
savannah.color("blue")
savannah.shape ("turtle")
barb=turtle.Turtle()
barb.color("pink")
barb.shape ("turtle")
counter=0

#forever loop
while True:
    #Draw Square
    savannah.forward(100+counter*2)
    savannah.right(90)
    barb.forward(100+counter*2)
    barb.right(90)
    counter=counter+1



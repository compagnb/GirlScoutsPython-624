#This is my code for Girl Scouts
import turtle
img="Leya.gif"
#print("Hi")
wn=turtle.Screen()
wn.register_shape(img)


mike=turtle.Turtle()
mike.color("orange")
mike.shape(img)

counter=0

#forever loop
while True:
    mike.forward(100+counter*2)
    mike.right(90)
    counter=counter+1
    
    

#mike.forward(100)
#mike.right(90)
#mike.backward(100)
#mike.left(90)

#Draw Square
##mike.forward(100)
##mike.right(90)
##mike.forward(100)
##mike.right(90)
##mike.forward(100)
##mike.right(90)
##mike.forward(100)
##mike.right(90)








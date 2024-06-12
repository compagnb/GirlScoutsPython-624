#This is my code for girl Scouts
import turtle
img="isabella.gif"
#print("hi")
wn=turtle.Screen()
wn.register_shape(img)


lucy=turtle.Turtle()
lucy.color("pink")
lucy.shape(img)


counter=0
#forever loop
while True:
     lucy.forward(100+counter*2)
     lucy.right(90)
     counter=counter+1







#Draw Square
lucy.forward(100)
lucy.right(90)
lucy.forward(100)
lucy.right(90)
lucy.forward(100)
lucy.right(90)
lucy.forward(100)
lucy.right(90)

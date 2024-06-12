#i just sneezed
import turtle
img="lord farquad bridget.gif"
#print ("Hi")
wn=turtle.Screen()
wn.register_shape(img)

lordFarquad=turtle.Turtle()
lordFarquad.color("green")
lordFarquad.shape(img)
#lordFarquad.forward(100)
#lordFarquad.right(90)
#lordFarquad.backward(100)
#lordFarquad.left(90)

#Draw Square
lordFarquad.forward(100)
lordFarquad.right(90)
lordFarquad.forward(100)
lordFarquad.right(90)
lordFarquad.forward(100)
lordFarquad.right(90)
lordFarquad.forward(100)
lordFarquad.right(90)

counter=0

#forever loop
while True:
    lordFarquad.forward(100+counter*2)
    lordFarquad.right(90)
    counter=counter+1

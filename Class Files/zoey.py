import turtle

print("Hi")

mike=turtle.Turtle()
mike.color("orange")
mike.shape("turtle")

#mike.forward(100)
#mike.right(90)
#mike.backward(100)
#mike.left(90)

#Draw Square

mike.forward(100)
mike.right(90)
mike.backward(100)
mike.left(90)
mike.forward(100)
mike.right(90)
mike.backward(100)
mike.left(90)

#forever loop
while True:
    mike.forward(100+counter*2)
    mike.right(90)
    counter=counter+1

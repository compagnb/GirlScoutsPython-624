
import turtle

qiqi=turtle.Turtle()
qiqi.color("black")
qiqi.shape("turtle")


#Square
#qiqi.forward(50)
#qiqi.right(90)
#qiqi.forward(50)
#qiqi.right(90)
#qiqi.forward(50)
#qiqi.right(90)
#qiqi.forward(50)

counter=0
while True:
    qiqi.speed(0)
    qiqi.forward(100+counter*2)
    qiqi.right(90)
    counter=counter+1

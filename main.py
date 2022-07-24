import turtle
#4 20 
BODY_COLOR = 'red'
GLASS_COLOR = 'skyblue'

t = turtle.Turtle()  

def body():
    t.pensize(30)
    t.fillcolor(BODY_COLOR)

    t.begin_fill()

    t.right(90)
    t.forward(50)
    t.right(180)
    t.circle(40, -180)
    t.right(180)
    t.forward(200)

    t.up()
    t.left(90)
    t.forward(10)
    t.right(90)
    t.down()



body()
#glass()
#backpack()


turtle.done() 


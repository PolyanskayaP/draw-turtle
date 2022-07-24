import turtle
#4 20 
BODY_COLOR = 'skyblue'
GLASS_COLOR = 'red'

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
    for i in range(2):
        t.right(90)
        t.forward(170)

        t.left(90)
        t.forward(90)

    t.end_fill()



body()
#glass()
#backpack()


turtle.done() 


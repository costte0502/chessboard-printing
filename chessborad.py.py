import turtle
pox = -200
poy = 200
size = 40
turtle.speed(9)
turtle.up()
turtle.goto(pox,poy)
turtle.down()

def draw_square():
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.forward(size)

for i in range(8):
    for j in range(8):
        if i % 2 ==0:
            if j % 2 ==1:
                turtle.fillcolor("gray")
                turtle.begin_fill()
                draw_square()
                turtle.end_fill()
            else:
                draw_square()
        else:
            if j % 2 == 0:
                turtle.fillcolor("gray")
                turtle.begin_fill()
                draw_square()
                turtle.end_fill()
            else:
                draw_square()
    
    turtle.up()
    poy -=size
    turtle.goto(pox,poy)
    turtle.down()
turtle.done()
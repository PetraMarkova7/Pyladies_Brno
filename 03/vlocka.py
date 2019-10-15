from turtle import forward, left, right, penup, pendown, exitonclick
for _ in range (8):
    for _ in range(4):
        right(25)
        forward(50)
        left(140)
        forward(50)
        right(25)
    left(45)
    
penup()
left(20)
forward(180)
pendown()

for _ in range (8):
    for _ in range(5):
        right(24)
        forward(50)
        left(120)
        forward(50)
        right(24)
    left(45)

left(130)
forward(180)

for _ in range (8):
    for _ in range(6):
        right(30)
        forward(30)
        left(120)
        forward(30)
        right(30)
    left(45)
    

exitonclick()
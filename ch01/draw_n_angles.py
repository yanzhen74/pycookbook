import turtle

n_edge = int(input("Enter edge number:"))
angle = 180 - ((n_edge - 2) * 180) / n_edge

color = input("Enter color name:")

turtle.fillcolor(color)
turtle.begin_fill()

for i in range(n_edge):
    turtle.forward(100)
    turtle.right(angle)
turtle.end_fill()

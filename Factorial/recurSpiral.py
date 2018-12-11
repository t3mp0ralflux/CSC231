import turtle

def drawSpiral(linelen, t):
    if (linelen > 0):
        t.forward(linelen)
        t.right(90)
        drawSpiral(linelen - 5, t)


def main():
    ben=turtle.Turtle()
    drawSpiral(100,ben)


main()

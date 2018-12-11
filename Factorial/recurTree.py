import turtle
def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen - 15, t)
        t.left(40)
        tree(branchLen -10, t)
        t.right(20)
        t.backward(branchLen)

def main():
    ben = turtle.Turtle()
    ben.penup()
    ben.setx(0)
    ben.sety(-150)
    ben.setheading(90)
    ben.pendown()
    tree(90,ben)

main()

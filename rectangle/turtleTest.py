import turtle

def main():
    # Although we can create a window, ifwe create a turtle, 
    # a window is automatically be created.
                                
    tess = turtle.Turtle()      # Create tess and set some attributes
    tess.pencolor("hotpink")    # pen color
    tess.pensize(5)             # pen size is 5 (default is 1)

    tess.forward(80)            # Make tess draw equilateral triangle
    tess.left(120)
    tess.forward(80)
    tess.left(120)
    tess.forward(80)
    tess.left(120)              # Complete the triangle

    alex = turtle.Turtle()      # Create alex
    alex.penup()                # We need to move alex without making any marks
    alex.goto(-100,200)
    alex.color("purple")        # this sets BOTH pencolor and fillcolor
    alex.pendown()              # start drawing
    alex.begin_fill()           # When alex completes a shape, it will be filled
                                # with this color

    for i in range(5):          # draw a pentagon
        alex.forward(100)
        alex.right(360//5)
        
    alex.end_fill()             # pentegon is finished so fill in the color

main()

import random
from myRect import myRectangle

def main():
    sqr = myRectangle()
    colors=["Red","Blue","Green","Pink","Orange","Black"]
    for i in range(8):
        sqr.setX(random.randint(-200, 200))
        sqr.setY(random.randint(-200, 200))
        sqr.setWidth(random.randint(1, 150))
        sqr.setColor(random.choice(colors))
        x = sqr.getX()
        y = sqr.getY()
        w = sqr.getWidth()
        h = sqr.getWidth()
        c = sqr.getColor()
        sqr.draw(x, y, w, h, c)

main()

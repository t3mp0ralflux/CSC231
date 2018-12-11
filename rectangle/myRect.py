import turtle
import random

class myRectangle:
    def __init__(self):
        self.__width= 0
        self.__height= 0
        self.__color= None
        self.__x= 0
        self.__y= 0


    def getX(self):
        return self.__x

    def setX(self,x):
        self.__x=x

    def getY(self):
        return self.__y

    def setY(self, y):
        self.__y = y

    def getWidth(self):
        return self.__width

    def setWidth(self,width):
        self.__width = width

    def getHeight(self):
        return self.__height

    def setHeight(self,height):
        self.__height = height

    def getColor(self):
        return self.__color

    def setColor(self,color):
        colors = ["Red", "Blue", "Green", "Pink", "Orange", "Black"]
        color = random.choice(colors)
        self.__color = color

    def draw(self,x,y,width,height,color):
        ben = turtle.Turtle()
        ben.penup()
        ben.goto(x,y)
        ben.setheading(0)
        ben.color(color)
        ben.pendown()
        ben.begin_fill()
        ben.forward(width)
        ben.left(90)
        ben.forward(height)
        ben.left(90)
        ben.forward(width)
        ben.left(90)
        ben.forward(height)
        ben.end_fill()

#def main():
#    rect = myRectangle()
#    colors = ["Blue", "Black", "Pink", "Orange", "Red", "Green", "Purple"]
#    for i in range(6):
#        rect.setX(random.randint(-200,200))
##        rect.setY(random.randint(-200,200))
#        rect.setWidth(random.randint(1,150))
#        rect.setHeight(random.randint(1,150))
#        rect.setColor(random.choice(colors))
#        x=rect.getX()
#        y=rect.getY()
#        w=rect.getWidth()
#        h=rect.getHeight()
#        c=rect.getColor()
#        rect.draw(x,y,w,h,c)
#        print(x,y,w,h,c)
#        rect.setX(y)
#        rect.setY(x)
#        rect.setWidth(h)
#        rect.setHeight(w)
#        x = rect.getX()
#        y = rect.getY()
#        w = rect.getWidth()
#        h = rect.getHeight()
#        rect.draw(x,y,w,h,c)
#        print(x,y,w,h,c)
#main()
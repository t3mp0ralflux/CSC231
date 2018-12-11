import random

class myStack:
    def __init__(self):
        self.__items = []

    def push(self,x):
        self.__items.append(x)

    def pop(self):
        if (self.isEmpty()):
            return "Empty"
        else:
            return self.__items.pop()

    def peek(self):
        if (self.isEmpty()):
            return "Empty"
        else:
            return self.__items[self.size()-1]

    def size(self):
        return len(self.__items)

    def isEmpty(self):
        return self.size()==0

def main():
    a=0
    Queue = myStack()
    while a !=10:
        x=random.randint(-100,100)
        print(x, end=" ")
        Queue.push(x)
        a=a+1
    print("Is the queue empty?",Queue.isEmpty())
    print("Last Entry is:",Queue.peek())
    print("Size of stack is:",Queue.size())

    a=10
    while a!=0:
        print(Queue.peek(), end=" ")
        Queue.pop()
        a=a-1


main()
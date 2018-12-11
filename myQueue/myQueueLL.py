import random
import time
from myList import myList

class myQueue:
    def __init__(self):
        self.__items = []

    def enQueue(self,x):
        for b in range(x):
            y = random.randint(-100, 100)
            self.__items.append(y)

    def deQueue(self):
        if (self.isEmpty()):
            return "Empty"
        else:
            return self.__items.pop(0)

    def peek(self):
        if (self.isEmpty()):
            return "Empty"
        else:
            return self.size()

    def size(self):
        return len(self.__items)

    def isEmpty(self):
        return self.size() == 0


def main():
    Queue = myList()
    start = time.time()
    for x in range(10001):
        y = random.randint(-100,100)
        Queue.insert(0,y)
    end = time.time()
    print("\t{0:d}\t{1:.6f}\tseconds".format(x, (end - start)))
    start = time.time()
    for x in range(10001):
        Queue.pop()
    end = time.time()
    print("\t{0:d}\t{1:.6f}\tseconds".format(x, (end - start)))
    start = time.time()
    for x in range(10001):
        y = random.randint(-100,100)
        Queue.revinsert(y)
    end = time.time()
    print("\t{0:d}\t{1:.6f}\tseconds".format(x, (end - start)))
    start = time.time()
    for x in range(10001):
        Queue.revpop()
    end = time.time()
    print("\t{0:d}\t{1:.6f}\tseconds".format(x, (end - start)))

main()
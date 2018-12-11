import random
import time

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
            return self.__items[0]

    def size(self):
        return len(self.__items)

    def isEmpty(self):
        return self.size() == 0


def main():
    Queue = myQueue()
    start = time.time()
    for x in range(10001):
        Queue.enQueue(x)
    end = time.time()
    print("\t{0:d}\t{1:.6f}\tseconds".format(x, (end - start)))
    start = time.time()
    for x in range(10001):
        Queue.deQueue()
    end = time.time()
    print("\t{0:d}\t{1:.6f}\tseconds".format(x, (end - start)))


main()
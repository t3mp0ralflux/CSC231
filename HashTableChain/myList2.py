class listNode:

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next


class myList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, i, x):
    #Inserts x into the list at position i

    # list is empty, i doesn't matter.
        if (self.isEmpty()):
            self.head = listNode(x)
            self.tail = self.head

    # inserting before the head
        elif (i <= 0):
            self.head = listNode(x, self.head)

    # inserting after the tail
        elif (i >= self.size):
            self.tail.setNext(listNode(x))
            self.tail = self.tail.getNext()

    # inserting someplace in between

        else:
    # We need to traverse the list until we get to the (i-1)st one.
            current = self.head
            count = 0

    # We need to stop at the node previous to i to make
    # it point around the ith one.
            while (current != None and count < i-1):
                count += 1
                current = current.getNext()
            current.setNext(listNode(x, current.getNext()))

        self.size += 1

    def pop(self,i=None):

        if (self.isEmpty()):
            return None

        else:
            if (i==None):
                i=self.size-1

        if i<=0:
            x = self.head.getData()
            self.head = self.head.getNext()
            self.size -= 1
            if (self.head == None):
                self.tail = None
            return x

        else:
            current = self.head
            count = 0

            while (current != None and count < i-2):
                count += 1
                current = current.getNext()
            if (current == None):
                return None
            x=current.getNext().getData()
            current.setNext(current.getNext().getNext())
        self.size-=1

        if(current.getNext() == None):
            self.tail=current
        return x

    def size(self):
    # By keeping track of the size as we go, we don't have to
    # count the number of nodes, which would be O(N).
        return self._size

    def isEmpty(self):
    # Could return self.size == 0
        return self.head == None

    def index(self, x):
        current = self.head
        position = 1
        while (current != None):
            if current.getData() == x:
                return current.getData()
            else:
                current = current.getNext()
                position += 1


    def __str__(self):
        ''' Returns a string of the values in the list
        '''
        result = ""
        current = self.head
        while(current != None):
            result = result + " " + str(current.getData())
            current = current.getNext()
        return result


    def revinsert(self, x):
        # Inserts x into the list at position i

        # list is empty, i doesn't matter.
        if (self.isEmpty()):
            self.head = listNode(x)
            self.tail = self.head

        else:
            self.tail.setNext(listNode(x))
            self.tail = self.tail.getNext()
        self.size += 1

    def revpop(self, i=None):

        if (self.isEmpty()):
            return None

        else:
            if (i == None):

                x = self.head.getData()
                self.head = self.head.getNext()
                self.size -= 1
                if (self.head == None):
                    self.tail = None
                return x

        self.size -= 1

        if (current.getNext() == None):
            self.tail = current
        return x

#def main():
#    bob = myList()
#    bob.insert(0,5)
#    bob.insert(0,6)
#    bob.insert(0,12)
#    bob.insert(0, 24)
#    bob.insert(0, 55)
#    bob.insert(0, 2)
#    bob.insert(0, 18)
#    bob.insert(0, 3)
#    bob.revinsert(66)
#    print(bob)
#    bob.pop(0)
#    print(bob)
#    print(bob.index(18))
#    print(bob.front())
#    print(bob.back())
#    bob.remove(6)
#    print(bob)

#main()

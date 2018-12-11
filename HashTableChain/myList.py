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

#    def __repr__(self):
#        return str(self)


    def insert(self, data):
        new=listNode(data, self.head)
        self.head = new


#        temp = self.head
#        self.head = listNode(data)
#        self.head.next = temp


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

    def index(self,x):
        current = self.head
        position = 1
        while (current != None):
            if current.getData() == x:
                return current.getData()
            else:
                current = current.getNext()
                position +=1
        print("-1")

    def front(self):
        if (self.isEmpty()):
            return None
        else:
            return self.head.getData()

    def back(self):
        if (self.isEmpty()):
            return None
        else:
            return self.tail.getData()

    def remove(self,a):
        x=self.index(a)
        self.pop(x)

    def __str__(self):
        ''' Returns a string of the values in the list
        '''
        result = ""
        current = self.head
        while(current != None):
            result = str(current.getData()) + " -> "
            current = current.getNext()
        return result


    def append(self, x):
        # Inserts x into the list at position i

        # list is empty, i doesn't matter.
        if (self.isEmpty()):
            self.head = listNode(x)
            self.tail = self.head

        else:
            self.tail.setNext(listNode(x))
            self.tail = self.tail.getNext()
#        self.size += 1

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

def main():
    list = myList()
    list.insert(5)
    list.insert(7)
    print(list)

main()
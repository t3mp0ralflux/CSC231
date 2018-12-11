import random

class minHeap:
    def __init__(self):
        self.size = 0
        # This is not an empty list.  It is a list with one thing in
        # it that happens to be "None".
        self.theHeap = [None]

    def getSize(self):
        return self.size

    def getValue(self, x):
        if x != None and x <= self.size:
            return self.theHeap[x]
        else:
            return None
        
    def getParent(self, x):
        if x != None and x >= 2:
            return x // 2
        else:
            return None

    def getLeftChild(self, x):
        if x != None and x * 2 <= self.size:
            return x * 2
        else:
            return None

    def getRightChild(self, x):
        if x != None and x * 2 + 1 <= self.size:
            return x * 2 + 1
        else:
            return None

    def isEmpty(self):
        return self.size == 0
        
    def put(self, value):
        self.size += 1
        self.theHeap.append(value)
        self.percolateUp(self.size)

    def get(self):
        value = self.getValue(1)
        if value == None:
            return value
        # Move the last value into the 1st position and decrement the size
        self.theHeap[1] = self.theHeap[self.size]
        self.size -= 1
        # percolate the new value at 1 (which is a large value) down.
        self.percolateDn(1)
        return value

    def percolateUp(self, x):
        parent = self.getParent(x)
        while (parent != None):
            if (self.theHeap[parent] > self.theHeap[x]):
                self.swap(parent, x)
            x = parent
            parent = self.getParent(x)

    def percolateDn(self, x):
        lChild = self.getLeftChild(x)
        rChild = self.getRightChild(x)

        # Because a Heap is a complete tree, if there is no left child,
        # then there is no right child either, so we don't have to check
        # for that.  If there is at least a left child, then we COULD
        # percolate
        while (lChild != None):
            # Either right child doesn't exists or left child is smaller
            if (rChild == None or
                self.theHeap[rChild] >= self.theHeap[lChild]):

                # Is x bigger the lChild?
                if (self.theHeap[x] > self.theHeap[lChild]):
                    self.swap(x, lChild)
                    x = lChild
                else:
                    # We can stop b/c we didn't move it down
                    x = None

            # The negation of the above if statement is:
            #    Right child exists AND right child is smaller
            else:
                # Is x bigger the rChild?
                if (self.theHeap[x] > self.theHeap[rChild]):
                    self.swap(x, rChild)
                    x = rChild
                else:
                    # We can stop b/c we didn't move it down
                    x = None
                    
            lChild = self.getLeftChild(x)
            rChild = self.getRightChild(x)

    def swap(self, x, y):
        if (x >= 1 and x <= self.size and
            y >= 1 and y <= self.size):
            temp = self.theHeap[x]
            self.theHeap[x] = self.theHeap[y]
            self.theHeap[y] = temp

    def isHeap(self):
        if (len(self.theHeap) > self.size and self.isHeap_rec(1)):
            return True
        else:
            return False

    def isHeap_rec(self, x):
        if (x == None):
            return True
        else:
            lChild = self.getLeftChild(x)
            rChild = self.getRightChild(x)

            if (lChild != None and self.theHeap[lChild] < self.theHeap[x]):
                return False
            
            if (rChild != None and self.theHeap[rChild] < self.theHeap[x]):
                return False

        return self.isHeap_rec(lChild) and self.isHeap_rec(rChild)

    def __str__(self):
        result = ""
        for i in range(1, self.size + 1):
            result += " " + str(self.theHeap[i])
        return result

    def heapify(self, newList):
        for i in range(len(newList)):
            self.theHeap.append(newList[i])
            self.size += 1
        x = self.getParent(self.size)
        while x >= 1:
            self.percolateDn(x)
            x -= 1

    def heapSort(self):
        originalSize = self.size
        x = self.size
        while (x > 1):
            self.swap(1, x)
            self.size -= 1
            self.percolateDn(1)
            x -= 1
        self.size = originalSize

    def getAll(self):
        return self.theHeap[1:self.size+1]

# The maxHeap is just a minHeap, but we reverse the direction. The only
# function we need to override are those that do the comparisons to
# reverse the direction.
class maxHeap(minHeap):
    def percolateUp(self, x):
        # This is the same as the percolateUp with the minHeap except
        # that all > has been changed to <.
        parent = self.getParent(x)
        while (parent != None):
            if (self.theHeap[parent] < self.theHeap[x]):
                self.swap(parent, x)
            x = parent
            parent = self.getParent(x)

    def percolateDn(self, x):
        # This is the same as the percolateDn with the minHeap except
        # that all > has been changed to <.

        lChild = self.getLeftChild(x)
        rChild = self.getRightChild(x)

        # Because a Heap is a complete tree, if there is no left child,
        # then there is no right child either, so we don't have to check
        # for that.  If there is at least a left child, then we COULD
        # percolate
        while (lChild != None):
            # Either right child doesn't exists or left child is smaller
            if (rChild == None or
                self.theHeap[rChild] <= self.theHeap[lChild]):

                # Is x bigger the lChild?
                if (self.theHeap[x] < self.theHeap[lChild]):
                    self.swap(x, lChild)
                    x = lChild
                else:
                    # We can stop b/c we didn't move it down
                    x = None

            # The negation of the above if statement is:
            #    Right child exists AND right child is smaller
            else:
                # Is x bigger the rChild?
                if (self.theHeap[x] < self.theHeap[rChild]):
                    self.swap(x, rChild)
                    x = rChild
                else:
                    # We can stop b/c we didn't move it down
                    x = None
                    
            lChild = self.getLeftChild(x)
            rChild = self.getRightChild(x)

    def isHeap_rec(self, x):
        # This is the same as the isHeap_rec with the minHeap except
        # that all < has been changed to >.
        if (x == None):
            return True
        else:
            lChild = self.getLeftChild(x)
            rChild = self.getRightChild(x)

            if (lChild != None and self.theHeap[lChild] > self.theHeap[x]):
                return False
            
            if (rChild != None and self.theHeap[rChild] > self.theHeap[x]):
                return False

        return self.isHeap_rec(lChild) and self.isHeap_rec(rChild)




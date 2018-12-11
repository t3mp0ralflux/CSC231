from BinaryTree import BinaryTree
from BinarySearchTree import BinarySearchTree
import time
import random
from person import Person

class AVLTree(BinarySearchTree):
    def __init__(self, data = None, leftChild = None, rightChild = None):
        BinarySearchTree.__init__(self, data, leftChild, rightChild)
        if (self.data != None):
            self.height = 0
        else:
            self.height = -1

    def setData(self, data):
        BinaryTree.setData(self, data)
        if (self.getHeight() < 0):
            self.setHeight(0)

    def getHeight(self):
        return self.height

    def setHeight(self, h):
        self.height = h

    def computeHeight(self):
        height = -1
        if (self.getLeftChild() != None):
            height = max(height, self.getLeftChild().getHeight())
        if (self.getRightChild() != None):
            height = max(height, self.getRightChild().getHeight())
        self.height = height + 1

    def balanced(self):
        ''' Returns True if tree is unbalanced '''
        if (self.getLeftChild() != None):
            lHeight = self.getLeftChild().getHeight()
        else:
            lHeight = -1
            
        if (self.getRightChild() != None):
            rHeight = self.getRightChild().getHeight()
        else:
            rHeight = -1

        return (abs(lHeight - rHeight) < 2)

    def put(self, value):

        if (self.isEmpty()):
            self.setData(value)
            self.setHeight(0)
            return self

        elif (value < self.data):
            if (self.getLeftChild() == None):
                # There is no left subtree
                self.setLeftChild(AVLTree(value))
                self.computeHeight()
                return self
            
            else:
                # Recursively put into left subtree
                self.setLeftChild(self.getLeftChild().put(value))

                # We have an imbalance
                if (not self.balanced()):
                    
                    # Case 1: Single rotate with Left Child
                    if (value < self.getLeftChild().getData()):
                        return (self.rotateWithLeftChild())

                    # Case 2: Double rotation
                    else:
                        self.setLeftChild(self.getLeftChild().rotateWithRightChild())
                        return(self.rotateWithLeftChild())
                    
                self.computeHeight()
                return self
            
        else: # value >= self.data
            if (self.getRightChild() == None):
                # There is no right subtree
                self.setRightChild(AVLTree(value))
                self.computeHeight()
                return self
            else:
                # Recursively put into right subtree
                self.setRightChild(self.getRightChild().put(value))

                # We have an imbalance
                if (not self.balanced()):
                    
                    # Case 4: Single rotate with Right Child
                    if (value >= self.getRightChild().getData()):
                        return (self.rotateWithRightChild())

                    # Case 3: Double rotation
                    else:
                        self.setRightChild(self.getRightChild().rotateWithLeftChild())
                        return(self.rotateWithRightChild())

                self.computeHeight()
                return self
                
                    


    def rotateWithLeftChild(self):
        k = self.getLeftChild()
        self.setLeftChild(k.getRightChild()) # Move B from k to left of self
        k.setRightChild(self)
        
        self.computeHeight()
        k.computeHeight()
        return k

    def rotateWithRightChild(self):
        k = self.getRightChild()
        self.setRightChild(k.getLeftChild())
        k.setLeftChild(self)
        
        self.computeHeight()
        k.computeHeight()
        return k

    def isAVLTree(self):
        if (self.isEmpty()):
            return True
        if (not self.isBST()):
            return False
        if (not self.balanced()):
            return False
        if (self.getLeftChild() != None and not self.getLeftChild().isAVLTree()):
            return False
        if (self.getRightChild() != None and not self.getRightChild().isAVLTree()):
            return False
        return True
        
        
    def __str__(self):
        ''' This function produces an inorder traversal of the tree. '''
        #print("__str__(): self.root.getData = " + str(self.root.getData()))
        if (self.isEmpty()):
            return "Empty"

        else:
            result = ""

            if (self.getLeftChild() != None):
                result += self.getLeftChild().__str__()

            result += " " + str(self.getData()) + "(" + str(self.getHeight()) + ")"

            if (self.getRightChild() != None):
                result += " " + self.getRightChild().__str__()

            return result

def AVLmain():
    startTime = time.time()
    file = open("Cohortsorted_900.txt", "r")
    myTable = AVLTree()
    #print(myTable)
    for line in file:
        key, name = line.strip().split(",")
        #print("key = " + key + " name =" + name)
        p = Person(int(key), name)
        #print(p)
        myTable=myTable.put(p)

    file.close()
    endTime = time.time()
    print("Number of seconds to build the database = {0:.2f}".format(endTime - startTime))
    #print(myTable)

    searchPeople = []
    file = open("searchKeys_500.txt", "r")
    for line in file:
        key = line.strip().split(",")
        searchPeople.append(Person(int(key[0])))
    file.close()

    startTime = time.time()
    for person in searchPeople:
        searchPerson = myTable.get(person)
        #print (searchPerson)
    endTime = time.time()
    print("Number of seconds for search = {0:.2f}".format(endTime - startTime))

#def main():
#        tree = AVLTree()
#        tree.put(15)
#        print(tree)
##        tree.put(50)
#        print(tree)
#        tree.put(80)
#        print(tree)
#        tree.put(60)
#        print(tree)
#        tree.put(1)
#        print(tree)
#       tree.put(14)
#        print(tree)
#        tree.put(100)
#        print(tree)
#        print(tree.isAVLTree())

#main()
AVLmain()

'''
I used the full Cohort list and a search key list of 500 during these experiments with an unsorted list.

Binary Search tree took 14.88 seconds to load the file and build the tree.
BST took 0.10 seconds to complete the search.

The AVL tree took 28.63 seconds to read and build the tree
AVL took 0.08 seconds to complete the search.

After running these tests on an unsorted list, the conclusion I have come to is that despite the AVL tree taking almost
twice as long to build, it was faster to search for the values in the search keys.

I have changed the Cohort list to the sorted 900 for the next two experiments.

The BST on the sorted Cohort list of 900 took 2.42 seconds to build the database, but 3.83 seconds to search it.

The AVL tree on the sorted list took just 0.04 seconds to read and build the databse and 0.01 seconds to search.

The final conclusion between the AVL at full load and the BST at 900 is that the BST may be faster in some regards,
but the AVL tree is the real work horse here.  I can only conclude that the BST maxes out at 900 due to having such an
imbalanced load on one or more branches that to search them all hits a recursion check in Python, rendering the BST useless
with very large databases.  The balanced AVL keeps things from getting too deep down one specific rabbit hole.
'''
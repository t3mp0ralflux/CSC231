from BinaryTree import BinaryTree
from person import Person
import time
import random


class BinarySearchTree(BinaryTree):

    def put(self,value):
        if (self.isEmpty()):
            self.setData(value)

        elif (value < self.getData()):
            if(self.leftChild == None):
                self.setLeftChild(BinarySearchTree(value))

            else:
                self.leftChild.put(value)
        else:
            if(self.rightChild == None):
                self.setRightChild(BinarySearchTree(value))
            else:
                self.rightChild.put(value)


    def get(self,value):
        if(self.isEmpty()):
            return "Empty"
        if (value == self.getData()):
            return self.getData()

        elif(value < self.getData()):
                if self.leftChild:
                    return self.getLeftChild().get(value)
                else:
                    return False
        else:
            if self.rightChild:
                return self.getRightChild().get(value)


#def BSTmain():
#    startTime = time.time()
#    file = open("Cohort.txt", "r")
#    myTable = BinarySearchTree()
#    #print(myTable)
#    for line in file:
#        key,name = line.strip().split(",")
        #print("key = " + key + " name =" + name)
#        p = Person (int(key),name)
#        #print(p)
#        myTable.put(p)

#    file.close()
#    endTime = time.time()
#    print("Number of seconds to build the database = {0:.2f}".format(endTime - startTime))
    #print(myTable)

#    searchPeople = []
#    file = open("searchKeys_500.txt", "r")
#    for line in file:
#        key = line.strip().split(",")
#        searchPeople.append(Person(int(key[0])))
#    file.close()


#    startTime = time.time()
#    for person in searchPeople:
#        searchPerson = myTable.get(person)
        #print (searchPerson)
#    endTime = time.time()
#    print ("Number of seconds for search = {0:.2f}".format(endTime - startTime))

#def main():
#    cat = BinarySearchTree()
#    cat.put(Person(850404362,"Brent"))
#    cat.put(Person(850404363, "Heidi"))
#    cat.put(Person(850404361, "Cindy"))
#    print(cat)
#main()

#BSTmain()



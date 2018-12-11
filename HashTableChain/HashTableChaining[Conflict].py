from myList2 import myList
from person import Person
import random
import time

class HashTable:
    def __init__(self, size = None):

        if (size != None):
            self.size = size

        else:
            self.size = 11

        self.bucket = [ ] * self.size
        for i in range(self.size):
            self.bucket.append(myList())

    def hash(self,key):
        return key % self.size

    def put(self, key, name):
        index = self.hash(key)
        self.bucket[index] = myList.revinsert(Person.setName(name))

    def get(self,key):
        index = self.hash(key)
        while (self.bucket[index] != None):
            if (self.bucket[index] == Person.getKey(key)):
                return self.bucket.getData()
            else:
                myList.index(key)



def main():
    myTable = HashTable(7)
    print(myTable)

main()
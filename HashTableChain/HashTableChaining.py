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

        self.bucket = []
        for i in range(self.size):
            self.bucket.append(myList())

#    def __repr__(self):
#        return str(self.bucket)

    def hash(self,key):
        return key % self.size

    def put(self, name):
        key_hash = self.hash(name.getKey())
        self.bucket[key_hash].revinsert(name)
        return

    def get(self,key):
        key_hash = self.hash(key.getKey())
        if (self.bucket[key_hash] != None):
           return self.bucket[key_hash].index(key)


    def __str__(self):
        print(self.bucket[0])
        result = ""
        for i in range(self.size):
            result = result + "\n" + str(self.bucket[i])
        return result

#def main():
#    myTable = HashTable(7)
#    p = Person(1,Brenton)
#    print(myTable)
#    myTable.put(p)
#    print(myTable)
#    n = Person(2,"Heidi")
#    myTable.put(n)
#    print(myTable)
#    p = Person(3, "Joe")
#    myTable.put(p)
#    print(myTable)
#    p = Person(8, "Steve")
#    myTable.put(p)
#    print(myTable)
#    p = Person(15, "Cindy")
#    myTable.put(p)
#    print(myTable)
#    p = Person(22, "Dami")
#    myTable.put(p)
#    print(myTable)
#    p = Person(29, "Travis")
#    myTable.put(p)
#    print(myTable)
#    print(myTable.get(22))


def main():
    file = open("Cohort.txt", "r")
    myTable = HashTable(11027)
    # print(myTable)
    for line in file:
        key, name = line.strip().split(",")
        # print("key = " + key + " name = " + name)
        p = Person(int(key), name)
        # print(p)
        myTable.put(p)

    file.close()
    #print(myTable)

    searchPeople = []
    file = open("searchKeys3.txt", "r")
    for line in file:
        key = line.strip().split(",")
        searchPeople.append(Person(int(key[0])))
    file.close()

    startTime = time.time()
    for person in searchPeople:
        searchPerson = myTable.get(person)
        # print(searchPerson)
    endTime = time.time()
    print("Number of seconds = {0:.2f}".format(endTime - startTime))

main()

'''
Persistance pays off and I finally think I have it.  With a table size of 7, the find time was 7.11 seconds on my home rig.

When increasing the table size to 17, the time was 40.79 seconds.

I see a pattern approaching and fear the higher numbers at this point.

When increased to 127 for the bucket size, the time was 0.47 seconds.  An interested result and I'm not sure why that might be.

When increased to 1117, the time was 0.05 seconds, which makes me really wonder why 17 was so bad.

The final step of 11027 proved to take almost a constant amount.

I'm not exactly sure why 17 would be so terrible, but I think it might have something to do with the number of items in the list and the number of slots lining up just right to cause the slow down.
If not, I'm not exactly sure why 17 would be the errant case while it seems that the more buckets, the faster the time.'''
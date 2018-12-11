import random
import time

class HashTableProbe:
    def __init__(self, size = None):
        if (size != None):
            self.size=size
        else:
            self.size=11

        self.bucket = [None]*self.size
        self.skip=3

    def hash(self,value):
        return value % self.size

    def rehash(self,old_hash):
        return(old_hash+self.skip) % self.size

    def get(self,value):
        index = self.hash(value)
        old_index = self.hash(value)
        while(self.bucket[index] != None):
            if(self.bucket[index] == value):
                return self.bucket[index]
            else:
                self.rehash(index)
                if (index==old_index):
                    return None

    def put(self,value):
        index = self.hash(value)
        old_index = self.hash(value)
        if(self.bucket[index] == None):
            self.bucket[index]= value
        else:
            while self.bucket[index] !=None:
                index = self.rehash(index)
                if (index == old_index):
                    return None
            self.bucket[index]=value



def main():
    probe = HashTableProbe(17)
#    probe.put(5)
#    probe.put(7)
#    probe.put(9)
#    print(probe.get(5))
#    print(probe.get(7))
#    print(probe.get(9))
    N = 18
    x = 50
    for i in range(N):
        probe.put(random.randint(40, 50))

    startTime = time.time()
    print(probe.get(x))
    endTime = time.time()
    print("Time to find " + str(x) + " among " + str(N), end=" ")
    print("using a linear probe was " + "{0:.4f}".format(endTime - startTime) + " seconds.")

main()

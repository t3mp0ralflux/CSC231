class Person:
    def __init__(self,key = None,name = None):
        self.key = key
        self.name = name

#    def __repr__(self):
#        return str(self.key + self.name)

    def getKey(self):
        return self.key

    def getName(self):
        return self.name

    def setKey(self,key):
        self.key = key

    def setName(self,name):
        self.name = name

    def __eq__(self, other):
        if (other == None):
            return False
        return (self.key == other.key)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return(str(self.key) + ", " + str(self.name))

    def __cmp__(self, other):
        if (other == None):
            return -1
        else:
            return self.key - other.key

    def __lt__(self, other):
        return (self.__cmp__(other)<0)

    def __le__(self, other):
        return self.__cmp__(other) <= 0

    def __gt__(self, other):
        return self.__cmp__(other) > 0

    def __ge__(self, other):
        return self.__cmp__(other) >= 0


#def main():
#    test = Person()
#    test.setKey(4)
#    test.setName("Brent")
#    print(test)

#main()

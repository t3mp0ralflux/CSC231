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
        return (self.key == other)

    def __ne__(self, other):
        return (self.key != other.key)

    def __str__(self):
        return(str(self.key) + ", " + str(self.name))


#def main():
#    test = Person()
#    test.setKey(4)
#    test.setName("Brent")
#    print(test)

#main()

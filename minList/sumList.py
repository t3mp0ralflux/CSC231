import random

def mySum(myList):
    if (len(myList)==1):
        return myList[0]

    a = mySum(myList[0: len(myList)//2])
    b = mySum(myList[len(myList)//2: len(myList)])

    return a+b

def main():
    N = 100
    myList = [random.randint(-500,500) for i in range(N)]

    print(myList)
    print(mySum(myList))


main()
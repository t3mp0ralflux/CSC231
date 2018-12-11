import random

def myMin(myList):
    if (len(myList)==1):
        return myList[0]

    a = myMin(myList[0: len(myList)//2])
    b = myMin(myList[len(myList)//2: len(myList)])

    return min(a,b)

def main():
    N = 100
    myList = [random.randint(-500,500) for i in range(N)]

    print(myList)
    print(myMin(myList))

main()

#big-O is Nlog2N
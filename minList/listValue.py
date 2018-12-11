import random
import time

def myFindRecursive(haystack,needle):
    #Base case 1 is never used unless list is initially empty
    if(len(haystack) <= 0):
        return None

    if(len(haystack) == 1):
        if needle == haystack[0]:
            return 0
        else:
            return None

    a = myFindRecursive(haystack[0:len(haystack)//2],needle)
    if (a != None):
        return a
    b = myFindRecursive(haystack[len(haystack)//2:len(haystack)],needle)
    if (b !=None):
        return b + len(haystack)//2

    return None

def binarySearch(haystack, needle):
    if (len(haystack) <= 0):
        return None

    if (len(haystack) == 1):
        if needle == haystack[0]:
            return 0
        else:
            return None
    if needle <= haystack[len(haystack)//2]:
        a = binarySearch(haystack[0:len(haystack) // 2], needle)
        return a
    else:
        b = binarySearch(haystack[len(haystack)//2:len(haystack)],needle)
        return b



def linSearch(haystack,needle):
    for i in range(len(haystack)):
        if (i == needle):
            return i
    return None

def linSearchGT(haystack,needle):
    for i in range(len(haystack)):
        if (i == needle):
            return i
        if (i > needle):
            return None
    return None


def main():
    N = 1000000
    myList = []
    x = 500000
    for i in range(N):
        myList.append(random.randint(0,1000000))

    # The list is unordered

    #print(myList)

    startTime = time.time()
    print(myFindRecursive(myList,x))
    endTime = time.time()
    print("Time to find "+ str(x) + " recursively among " + str(N), end=" ")
    print("unsorted items was " + "{0:.4f}".format(endTime-startTime) + " seconds.")
    startTime = time.time()
    print(linSearch(myList,x))
    endTime = time.time()
    print("Time to find " + str(x) + " linear among " + str(N), end=" ")
    print("unsorted items was " + "{0:.4f}".format(endTime - startTime) + " seconds.")
    mySortedList = sorted(myList)
    startTime = time.time()
    print(binarySearch(mySortedList, x))
    endTime = time.time()
    print("Time to find " + str(x) + " recursively among " + str(N), end=" ")
    print("sorted items was " + "{0:.4f}".format(endTime - startTime) + " seconds.")
    startTime = time.time()
    print(linSearchGT(mySortedList, x))
    endTime = time.time()
    print("Time to find " + str(x) + " linear among " + str(N), end=" ")
    print("sorted items was " + "{0:.4f}".format(endTime - startTime) + " seconds.")

main()
import random
import time

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def copyList(a, b, N):
    for i in range(N):
        b.append(a[i])

def isListSorted(a):
    N = len(a)
    for i in range(0,N-1):
        if a[i] > a[i+1]:
            return False

    return True
    
def insertionSort(a):
    N = len(a)
    for i in range(1,N):
        k = i
        while k > 0 and a[k] < a[k-1]:
            swap(a,k,k-1)
            k-=1
    #assertion a[0...i] is sorted
    return


def bubbleSort(a):
    N = len(a)
    for i in range(N-1,0, -1):
        sorted = True
        for j in range(0,i):
            if (a[j] > a[j+1]):
                swap(a,j,j+1)
                sorted = False
        if (sorted):
            break
    return

def mergeSort_rec(a, left, right):
    if (right <= left):
        return

    if (right - left == 1):
        if (a[left]>a[right]):
            swap(a,left,right)
        return

    center = (left + right)//2

    mergeSort_rec(a,left,center-1)
    mergeSort_rec(a,center,right)
    i = left
    j = center
    b = []
    while (i < center and j < right+1):
        if (a[i] <= a[j]):
            b.append(a[i])
            i+=1
        else:
            b.append(a[j])
            j+=1

    while (i < center):
        b.append(a[i])
        i+=1

    while (j < right+1):
        b.append(a[j])
        j+=1
    j=0
    for i in range(left,right+1):
        a[i]=b[j]
        j+=1
    return


def mergeSort(a):
    mergeSort_rec(a, 0, len(a) - 1)

def quickSort(a):
    quickSort_rec(a,0,len(a)-1)

def quickSort_rec(a,left,right):
    if(right <= left):
        return

    if(right-left == 1):
        if(a[left] > a[right]):
            swap(a,left,right)
        return

    pivot = a[left]
    i = left+1
    j = right
    done = False
    while (not done):
        while (i <= j and a[i] <= pivot):
            i+=1
        while (j>=i and a[j] >= pivot):
            j-=1
        if(j < i):
            done = True
        else:
            swap(a,i,j)
    swap(a,left,j)
    quickSort_rec(a,left,j-1)
    quickSort_rec(a,j+1,right)
    return





def main():
    N = 4000
    myList = [random.randint(-500, 500) for i in range(N)]
    myList.sort()

    sortingList = []    
    copyList(myList, sortingList, len(myList))
#    print("The unsorted list:")
#    print(sortingList)
#    print("\n")

    startTime = time.time()
    bubbleSort(sortingList)
    endTime = time.time()
    print("Time to bubble sort a list of " + str(N), end="")
    print(" values was " + "{0:.4f}".format(endTime-startTime) + " seconds")
    
#    print("After bubble sort, the list is:")
#    print(sortingList)
    print("List is sorted: " + str(isListSorted(sortingList)))
    print("\n")
          
    sortingList = []    
    copyList(myList, sortingList, len(myList))
#    print("The unsorted list:")
#    print(sortingList)
#    print("\n")
    
    startTime = time.time()
    insertionSort(sortingList)
    endTime = time.time()
    print("Time to insertion sort a list of " + str(N), end="")
    print(" values was " + "{0:.4f}".format(endTime-startTime) + " seconds")
    
#    print("After insertion sort, the list is:")
#    print(sortingList)
    print("List is sorted: " + str(isListSorted(sortingList)))
    print("\n")

    sortingList = []    
    copyList(myList, sortingList, len(myList))
#    print("The unsorted list:")
#    print(sortingList)
#    print("\n")

    startTime = time.time()
    mergeSort(sortingList)
    endTime = time.time()
    print("Time to merge sort a list of " + str(N), end="")
    print(" values was " + "{0:.4f}".format(endTime-startTime) + " seconds")
    
#    print("After merge sort, the list is:")
#    print(sortingList)
    print("List is sorted: " + str(isListSorted(sortingList)))
    print("\n")

    sortingList = []
    copyList(myList, sortingList, len(myList))
    #    print("The unsorted list:")
    #    print(sortingList)
    #    print("\n")

    startTime = time.time()
    quickSort(sortingList)
    endTime = time.time()
    print("Time to quick sort a list of " + str(N), end="")
    print(" values was " + "{0:.4f}".format(endTime - startTime) + " seconds")

    #    print("After merge sort, the list is:")
    #    print(sortingList)
    print("List is sorted: " + str(isListSorted(sortingList)))
    print("\n")

main()

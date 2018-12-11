import random
import time

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
    
def sort1(a):
    for i in range(len(a) - 1):
        for j in range(i+1, len(a)):
            if (a[i] > a[j]):
                swap(a, i, j)
            
    return

def sort2_rec(a, left, right):
    if (right <= left):
        return
    if (right - left == 1):
            if (a[left] > a[right]):
                swap(a, left, right)
            return

    center = (left + right) // 2
    sort2_rec(a, left, center-1)
    sort2_rec(a, center, right)

    # Merge two halves into b
    i = left
    j = center
    b = []
    while (i < center and j < right + 1):
        if (a[i] <= a[j]):
            b.append(a[i])
            i += 1
        else:
            b.append(a[j])
            j += 1
    while (i < center):
        b.append(a[i])
        i += 1
    while (j < right + 1):
        b.append(a[j])
        j += 1

    # Copy b back into a
    j = 0
    for i in range(left,right+1):
        a[i] = b[j]
        j += 1

    return

def sort2(a):
    sort2_rec(a,0, len(a)-1)
    return

def main():

    N = 10000
    original = [random.randint(-100,100) for i in range(N)]
    a = [x for x in original]

    '''
    print("original = ", end = "")
    for x in original:
        print(x, end=" ")
    print()
    '''

    print("\n\nSort 1\n")
    start = time.time()

    sort1(a)
    
    end = time.time()

    '''
    for x in a:
        print(x, end=" ")
    print()
    '''
    
    print ("\t{0:.6f}\tseconds".format(end - start))

    # Reset a
    a = [x for x in original]

    print("\n\nSort 2\n")
    start = time.time()

    sort2(a)

    end = time.time()

    '''
    for x in a:
        print(x, end=" ")
    print()
    '''
    
    print ("\t{0:.6f}\tseconds".format(end - start))


main()

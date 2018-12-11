import random
import time

def maxSubSum1(a):
    maxSum = 0

    for i in range (len(a)):
        for j in range (i, len(a)):
            thisSum = 0
            start = i
            end = j
            
            for k in range(i, j+1):
                thisSum += a[k]
                if (thisSum > maxSum):
                    maxSum = thisSum
                    maxStart = start
                    maxEnd = end
                    
    return maxSum, maxStart, maxEnd

def maxSubSum2(a):
    maxSum = 0

    for i in range(len(a)):

        thisSum = 0
        start = i
        for j in range (i, len(a)):
            
            thisSum += a[j]
            if (thisSum > maxSum):
                maxSum = thisSum
                maxStart = start
                maxEnd = j

    return maxSum, maxStart, maxEnd
            
        
def maxSubSum4(a):
    maxSum, thisSum = 0, 0
    start, maxStart, maxEnd = 0, 0, 0

    for i in range(len(a)):
        
        thisSum += a[i]
        if (thisSum > maxSum):
            maxSum = thisSum
            maxStart = start
            maxEnd = i
        elif (thisSum < 0):
            thisSum = 0
            start = i + 1

    return maxSum, maxStart, maxEnd

        
def main():
    N = 1000
    a = [random.randint(-100,100) for i in range(N)]

    
    print("a = ", end = "")
    for i in a:
        print(i, end = " ")


    print("\n\nMaxSubSum1\n")
    
    startTime = time.time()
    maxSum, start, end = maxSubSum1(a)
    endTime = time.time()
    print("max subsequence sum =", maxSum)
    print("The sequence starts at", start, "and ends at", end)
    print ("\t{0:.6f}\tseconds".format(endTime - startTime))

    print("\n\nMaxSubSum2\n")
    startTime = time.time()
    maxSum, start, end = maxSubSum2(a)
    endTime = time.time()
    print("max subsequence sum =", maxSum)
    print("The sequence starts at", start, "and ends at", end)
    print ("\t{0:.6f}\tseconds".format(endTime - startTime))

    print("\n\nMaxSubSum4\n")
    startTime = time.time()
    maxSum, start, end = maxSubSum4(a)
    endTime = time.time()
    print("max subsequence sum =", maxSum)
    print("The sequence starts at", start, "and ends at", end)
    print ("\t{0:.6f}\tseconds".format(endTime - startTime))
    
main()

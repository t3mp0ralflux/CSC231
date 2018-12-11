import time

def loop1(n):
    A=[]
    for i in range(n):
        A.append(0)
        for j in range(n):
            A[i]+=i*j
        for k in range(n):
            A[i]=k
            if(A[i]<0):
                A[i]=0

def loop2(n):
    A=[]
    for i in range(n):
        A.append([])
        for j in range(i+1,n):
            A[i].append(i*j)
'''
def loop3(n):
    sum = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                sum = k
'''
def main():

    print ("\n\nLoop1\n")
    for n in range(100, 1001, 100):
        start = time.time()
        loop1(n)
        end = time.time()
        print ("\t{0:d}\t{1:.6f}\tseconds".format(n, (end - start)))

    print ("\n\nLoop2\n")
    for n in range(100, 1001, 100):
        start = time.time()
        loop2(n)
        end = time.time()
        print ("\t{0:d}\t{1:.6f}\tseconds".format(n, (end - start)))

'''
    print ("\n\nLoop3\n")
    for n in range(100, 1001, 100):
        start = time.time()
        loop3(n)
        end = time.time()
        print ("\t{0:d}\t{1:.6f}\tseconds".format(n, (end - start)))
'''
main()

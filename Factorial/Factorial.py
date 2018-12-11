def factorial(n):
    if (n<=1):
        return 1
    else:
        a=factorial(n-1)
        b=a*n
        return b

def main():
    print(factorial(6))

main()
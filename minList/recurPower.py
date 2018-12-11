def powerraise(x,n):
    if n <= 0:
        return 1

    elif n == 1:
        return x
    temp = powerraise(x, n/2)
    if n%2 == 0:
        return temp*temp
    else:
        return x*temp*temp

def main():
    print(powerraise(2,6))

main()
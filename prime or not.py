def check(n, div = None):
    if div is None:
        div = n - 1
    while div >= 2:
        if n % div == 0:
            print("Number not prime")
            return 
        else:
            return check(n, div-1)
    else:
        print("Number is prime")
        return 
n=int(input("Enter number: "))
check(n)

def prime():
    a = int(input("enter a number: "))
    for i in range(2,a):
        if (a % i == 0):
            print(a , "is not a prime")
            break
    else:
        print(a , " is a prime number")


prime()            
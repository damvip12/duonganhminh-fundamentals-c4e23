n = int(input("n?"))
factorial = 1
if n == 0:
    print("The factorial of 0 is 1")
elif n < 0:
    print("There is no factorial for negative numbers")
else :
    for i in range(1,n+1):
        factorial = factorial*(i)
    print("The factorial of",n,"is",factorial)
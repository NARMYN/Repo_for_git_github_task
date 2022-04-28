
def fib(n):
    if (n==0 or n==1):
        result = n
        return result
    else:
        result = fib(n-1) + fib(n-2)
        return result
x = int(input("enter the number"))
for x in range(x):
    print("\n", fib(x))

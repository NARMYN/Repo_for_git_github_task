num1 = 0
num2 = 1
x = int(input('Enter a number'))
n=1
while n<=x:
    if n==1:
        print(num1, "\n")
        n = n+1
    else:
        temp = num2
        num2 = num1 + num2
        num1 = temp
        n = n+1
        print(num1, "\n")


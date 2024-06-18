# Write a python program that calculates the factorial of a given number
fact = 1
n = int(input("enter number:"))
if n> 0:
    for i in range(1,n+1,1):
        fact = fact*i
    print(fact,"is factorial")
elif n == 0:
    print(1,"is the factorial")
else:
    pass
# Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.
x = int(input("enter number 1(should be the greater number)"))
y = int(input("enter number 2"))
print("1 for + , 2 for -,3 for *, 4 for /")
ch = int(input("enter ur choice:"))
if ch == 1:
    print(x+y)
elif ch == 2:
    print(x-y)
elif ch == 3:
    print(x*y)
else:
    print(x/y)


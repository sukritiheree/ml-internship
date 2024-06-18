# Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.
print("1 for c and 2 for f")
t = int(input("1 or 2?"))
if t == 1:
    f = (t*9/5)+32
    print("temp in fahrenheit:",f)
else:
    c =( t-32)*5/9
    print("temp in celsius:",c)
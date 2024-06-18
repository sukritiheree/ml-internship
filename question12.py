#  Write a python program that calculates the sum of the digits of a given 
# number.
n = int(input("enter the number:"))
sum=0
digit = 0
while n!=0:
    d = n%10
    sum = sum + d
    n = n//10
    digit = digit +1
print("number of digits:",digit)
print("sum of digits:", sum)
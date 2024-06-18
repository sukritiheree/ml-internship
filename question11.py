# Write a python program that generates the first n numbers in the 
# Fibonacci sequence.
n=int(input("enter value of n:"))
first =0
second = 1
print(first,second,end= " ")
for i in range(2 , n):
    next = first+ second
    first = second
    second = next
    print(next,end = " ")
print()
    

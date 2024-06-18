# Write a python program that counts the occurrences of a specific element in a list.
l=[]
n = int(input("enter no of values to be entered into the list:"))
for i in range(0,n):
    v = int(input("enter value to be added:"))
    l.append(v)
search = int(input("enter the value u want to search for:"))
print("frequency:",l.count(search))
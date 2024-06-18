# Write a python program that checks if a substring is present in a given 
# string.
bigS = input("enter string:")
smallS = input("enter substring to check:")
if smallS in bigS:
    print("substring found in super string")
else:
    print("substring not found")
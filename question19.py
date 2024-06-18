# Write a python program that removes all punctuation from a given string
string = input("enter a string:")
s = ""
for i in string:
    if i.isalnum() == True:
        s = s+i
print(s)
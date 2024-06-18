#  Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.
string = input("enter string:")
suffix = input("enter suffix to check:")
prefix = input("enter prefix to check:")
if string.startswith(prefix) == True:
    print(prefix," is prefix of", string)
elif string.endswith(suffix)== True:
    print(suffix," is suffix of", string)
else:
    print("neither suffix nor prefix found")
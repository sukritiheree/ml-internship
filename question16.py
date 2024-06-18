#  Write a program in python that counts the frequency of each character in 
# a string.
string =input("enter string:")
for i in string:
    n=string.count(i)
    if n> 1:
        
        string.replace(i," ")
        print(i,"frequency:",n)
    else:
        print(i,"frequency: 1")  
    
    
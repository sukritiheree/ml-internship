# Write a program that takes a string input from the user and writes it to a 
# text file

f = open("myfile.txt", "w")
str = input("enter a string of words:")
f.write(str)
f.close()
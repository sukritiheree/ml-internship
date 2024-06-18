# Write a program that reads multiple lines of input from the user until they 
# enter an empty line, then prints all the lines.
data = ""
string= input("enter a line:")
while string != "":
    data = data +" "+ string
    string = input("enter another line:")
print(data)
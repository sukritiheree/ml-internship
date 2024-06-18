# Write a program that copies the contents of one text file to another.
f1 = open("myfile.txt","r")
r = f1.read()
f1.close
f2 = open("newfile.txt", "w")
f2.write(r)
f2.close()
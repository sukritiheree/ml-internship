# Write a program that reads data from a CSV file and prints it to the 
# console.
import csv
with open("data.csv",newline=" ") as data:
    c = csv.writer(data)
    c.writerow( ['name','address','job'] )
    the_list = [
    ['Alice', 'Gainesville, Florida', 'chef'],
    ['Bob', 'Chicago, Illinois', 'writer'],
    ['Ted', 'Miami, Florida', 'driver'],
    ['Carol', 'Portland, Oregon', 'executive']
]
    for item in the_list:
        c.writerow(item)
    c = csv.reader(data)
    for row in c:
      print( row[1] + ", " + row[5])
    data.close()
    

    

#write mode creates a file through python
file = open("file.txt","w")
file.write("content")

#read mode enables user to read any file
#open("file.txt","r")
#print(file.read())

#append mode creates an editable file
open("file.txt","a")
file.write("appended content")



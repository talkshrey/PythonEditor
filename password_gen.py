import random

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = "!@#$%^&*()_+*/-?"
finallist = uppercase + lowercase + numbers + symbols
key = ""

field = input("Enter your field: ")
n = int(input("Set length of the password: "))

for i in range(0,n):
    key = key + random.choice(finallist)

print(key)

file = open("/Users/HP/OneDrive/Documents/Passwords.txt","a")
file.write("\n"+field+":"+key)
file.close()
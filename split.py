import time
num = str(input("Enter a list of numbers with each number separated by a space: "))
myList = num.split(' ')
print("Your list of numbers is:",myList)
#24,12
i = 0
x = 0
a = len(myList)-1
while i<=a :
    y = int(myList[i])
    x = x + y
    i = i + 1
time.sleep(3)
avg = 0.0
print(x)
while True:
    choice = str(input("Do you want to calculate the average of these numbers [yes/no]?: "))
    if choice=="yes":
        avg = float(x/(len(myList)))
        print("The average of numbers you entered is: ", avg)
        break
    elif choice =="no":
        print("Thank you")
        break
    else:
        print("Invalid input")


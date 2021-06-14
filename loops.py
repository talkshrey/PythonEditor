i = 1
while i <= 5:
    j = 0
    while j <= i-1:
        print("*", end=" ")
        j = j+1
    print("")
    i = i+1

for i in range(0, 5):
    j = 0
    for j in range(0, i+1):
        print("*", end=" ")
        j = j+1
    print("")
    i = i+1


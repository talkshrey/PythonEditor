num = []
while True:
    x = int(input("input a number:\t"))
    num.append(x)
    print("current list: ",num)
    c = str(input("do you want to continue (y/n):\t"))
    if c=="y":
        continue
    elif c=="n":
        print("thank you")
        break
    else :
        print("invalid input")
        continue

c2 = str(input("do you want to find max or min (max/min):\t"))
grt_num = 0
i = 0
y = int(len(num))

if c2=="max":
    while i<y:
        grt_num = max(grt_num,num[i])
        i = i+1
    print("maximum value: ",grt_num)

elif c2=="min":
    while i<y:
        sml_num = min(num[0],num[i])
        i = i+1
    print("minimum value: ",sml_num)
else :
    print("invalid input")
    #23,45,34,12
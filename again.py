rows_of_stars= 10
for i in range(0,rows_of_stars):
    print("*",end="")
    for j in range(0,rows_of_stars-i-1):
        if rows_of_stars-i-1 % 5 == 0:
            print("#",end="")
        else:
            print("*",end="")      
    print("")
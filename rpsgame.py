import random

while(True) :
    x = str(input("Choose rock(r), paper(p), scissors(s): "))
    myDict1 = {"r":"rock","p":"paper","s":"scissors"}
    option = str(myDict1.get(x))
    print("You chose ",x," which is ",option)
    n = random.choice(['r','p','s'])
    print("Computer option:", n)
    if x==n:
        print('Tie :|')
    elif x=='r':
        if n=='p':
            print("You lose :(")
        elif n=='s' :
            print("You win :)")
    elif x=='p':
        if n=='r':
            print("You win :)")
        elif n=='s' :
            print("You lose :(")
    elif x=='s':
        if n=='r':
            print("You lose :(")
        elif n=='p':
            print("You win :)")
    g = str(input("Do you want to continue[y/n]: "))
    if g == "y":
        continue
    else :
        print("Game over")
        break







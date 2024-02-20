import math



def check():
    wyraz = str(input("\nGiveme a n input and I'll tell you if that's a palindrome: "))
    length = math.floor(len(wyraz)/2)
    
    for i in range(length):
        if wyraz[i-1] != wyraz[-i]:
            print("Not a palindrome")
            another() # adds an option to rerun for ease of checking, you can remo
            return
    print("Palindrome.")
    another() # adds an option to rerun for ease of checking
    return


def another():
        if (answer:=input("Another one? y/n: ")) == "y":
            check()
        elif answer == "n":
            return
        else:
            print("That's not an answer")
            another()

check()

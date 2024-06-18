import math

'''
take in a bunch of user inputs
make a nested 10 if-else statement
use a list, a tuple, and a dictionary
use a bunch of math operators and functions
use walrus operator
use a lambda function
generate a geometrical shape using loops
'''


print("Hello, welcome to my little exam in Python basics\n\n")


# add list, tuple,dictionary
list = []
dict = {}
tuple = (10,20,2)


def listing():
    print("==========\nFirst some lists\n==========")
    # ask for user input
    for i in range(1,5):
        list.append(input(f"Name list item {i}/4: "))
    print(f"List contains {len(list)}/5 items")
    if len(list)%5 != 0: # ask for a 5th input
        list.append(input("One more list item please: "))
    
    print("Thanks, here's your list: ", list)

def dictionary():
    print("\n==========\nNow time for a dictionary\n==========")
    if len(dict) == 0: # fill in the dictionary with 5 key-value pairs
        print("Dictionary is empty")

        # ask for user input
        while len(dict) < 3:
            i = len(dict) + 1
            key = input(f"Name key {i}/3: ")
            value = input(f"Name the value for key {i}/3: ")
            dict[key] = value
        
        print("Here's your dictionary", dict)




def meth():
    print("\n==========\nNow time for some math\n==========")
    ints = []
    # ask for user input
    iterations = 0
    while iterations < 5:
        a = input("Give me an integer: ")
        if a.isdigit(): # perform a simple check whether it received a number
            ints.append(a)
            iterations += 1
        else:
            print("That's not an integer!")

    
    print("\nBased on your inputs I have come to the conclusion that...\n")
    print(f"The biggest integer is {max(ints)}")
    if int(ints[0]) % int(ints[1]) == 0:
        print(f"{ints[0]} is divisible by {ints[1]}")
    elif int(ints[1]) % int(ints[2]) == 0:
        print(f"{ints[1]} is divisible by {ints[2]}")
    elif int(ints[2]) % int(ints[3]) == 0:
        print(f"{ints[2]} is divisible by {ints[3]}")
    elif int(ints[3]) % int(ints[4]) == 0:
        print(f"{ints[3]} is divisible by {ints[4]}")
    else: print(f"{ints[3]} to the power of {ints[4]} equals", b:=math.pow(int(ints[3]), int(ints[4])))
    
    if int(ints[1]) + int(ints[3]) > int(ints[0]):
        print(f"The sum of {ints[1]} and {ints[3]} is greater than {ints[0]}")
    else: print(f"{ints[0]} is greater than the sum of {ints[1]} and {ints[3]}")
    if int(ints[2]) % int(ints[4]) != 0:
        print(f"The remainder of {ints[2]} divided by {ints[4]} is", int(ints[2]) % int(ints[4]))
        print(f"The quotient of {ints[3]} divided by {ints[1]} is", int(ints[3]) // int(ints[1]))


def whatif():
    if "What" == "if": print("What equals if")
    elif len(tuple) == 0: print("The tuple is a lie")
    elif "if" == "What": print("if equals what?")
    elif "who am i" and "who are you?" < "How are you?": print("What is this?")
    elif "time" == "wasted": print("Not True")
    elif "Why cobble here?" in "Why cobble here is a very good quesiton": "Wh-"
    elif "Why" and not "cobble here": print("Where is here?")
    elif "Why am I here?" < "Who am I to judge why the cobble is there": "Why are you here?"
    elif "whatif" == "maybe": print("mayhaps")
    elif "python" == "passed": print("Congrats!")
    else: print("\n\n\n If you're reading this, that means I have passed the test!\nYou can look through the file contents for more interesting stuff")

def square(side):
    square = ""
    for eachrow in range(side):
        for numberoftiles in range(side-1): square += "█ "
        square += "█\n"
    print(square)
    



def start():
    listing()
    dictionary()
    meth()
    square(int(input("Size of square: ")))
    whatif()

start()

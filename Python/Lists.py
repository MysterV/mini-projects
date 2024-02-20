def start():
    data()
    if input("repeat? y/n ") == "y":
        start()
    else:
        print("Alright. See ya!")
    
def data():
    list = ["a", 7.1255, "igm3igg34mg", 1]
    list.append(input("give me something ^-^ "))
    print("Whole list: ", list)
    print("Starting from index 2: ", list[2:])
    print("Ending at 2", list[:2])
    

start()

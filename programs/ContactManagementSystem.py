def ask():
    print("What do you want to do?")
    print("1. Initialize a list")
    print("2. Add to a list")
    print("3. Display an Item")
    print("4. Quit")


def initialize_list():
    global list1
    answer = input("Are you sure you want to initialize list? (y/n): ")
    if answer == "y":
        list1 = []


def add_list():
    global list1
    thing = input("Type in name: ")
    list1.append(thing)


def find_list():
    global list1
    found = False
    answer = input("What do you want to find in the list: ")
    for i in list1:
        if i == answer:
            found = True
    if found:
        print()
        print("Found %s!" % answer)
    else:
        print()
        print("NOT FOUND!")


def report_all_items():
    global list1
    length = len(list1)
    if length > 0:
        for item in list1:
            print(item)
    else:
        print("You have no items!")


finished = True
while finished:
    print()
    ask()
    userInput = input("Choice: ")
    print()
    if userInput == "1":
        initialize_list()
    elif userInput == "2":
        add_list()
    elif userInput == "3":
        find_list()
    elif userInput == "4":
        report_all_items()
    else:
        finished = False

low = input("What is the lower bound of the range?: ")
high = input("What is the higher bound of the range?: ")
print()
print()

intLow = int(low)-1
intHigh = int(high)

match = True

while match:
    guess = round((intLow + intHigh) / 2)
    print("Computer's Guess: ", guess)
    correct = input("Is the matching number? (low, correct, high): ")
    print()
    if correct == "low":
        intLow = guess
    elif correct == "high":
        intHigh = guess
    elif correct == "correct":
        print()
        print("I guessed your number:", guess)
        match = False
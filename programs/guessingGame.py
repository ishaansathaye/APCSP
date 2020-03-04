# from tkinter import *
#
# root = Tk()
# root.title("Computer Guessing Game")
# root.geometry("500x500")
# lowVar = StringVar()
# highVar = StringVar()
# labelVar = StringVar()
# guessVar = StringVar()
#
# def range():
#     lowLabel = Label(root, textvariable=lowVar)
#     lowVar.set("What is the lower bound of the range?: ")
#     lowLabel.place(x=0, y=10)
#     text1 = Text(root, height=1.05, width=10)
#     text1.place(x=250, y=10)
#
#     highLabel = Label(root, textvariable=highVar)
#     highVar.set("What is the higher bound of the range?: ")
#     highLabel.place(x=0, y=40)
#     text2 = Text(root, height=1.05, width=10)
#     text2.place(x=250, y=40)
#
#
# # lBound, hBound = range()
# # lowBound = str(lBound-1)
# # highBound = str(hBound)
#
# randomLabel = Label(root, textvariable=labelVar)
# labelVar.set("Computer Guess: ")
# randomLabel.place(x=150, y=250)
#
# randomLabel = Label(root, textvariable=guessVar)
# guessVar.set("None")
# randomLabel.place(x=260, y=250)
#
# def math()
#
#
# newMatch = True
# while newMatch:
#     guessVar.set(text1.get)
#     root.mainloop()




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
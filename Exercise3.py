# Guess the Number Game
"""
# n = 34
# choice = 3
# print("Welcome to the guess the number game!!")
# print("Try your luck!!")
# print("You will get 3 choices!!")
# print("Good Luck!!")
n = 34
while (n) :
    # n = 34
    choice = 3
    print("Welcome to the guess the number game!!")
    print("Try your luck!!")
    print("You will get 3 choices!!")
    print("Good Luck!!")
    print("Enter a number : ")
    if n < 100 or n >= 80 :
        print("Try Again !!")
        choice = choice -1
        continue
    elif n >= 50 or n < 80:
        print("Try Again !!")
        choice = choice - 1
        continue
    elif n >= 20 or n <= 40 :
        print("So Close !!")
        choice = choice - 1
        continue
    elif n == 34 :
        print("You won the Game !!")
        break
"""


choice = 4
print("Welcome to the guess the number game!! \n")
print("Try your luck!! \n")
print("You will get 5 choices!! \n")
print("Enter a number between 1 to 100")
print("Good Luck!! \n")
n = 34
while(choice < 5):
    n = int(input("Enter the number : "))
    if choice == 0:
        # print("Number of choices left", choice)
        print("Game Over !!")
        print("Sorry you ran out of chances")
        print("Number of choices left", choice)
        break
        # print("Number of choices left", choice)
    # n = int(input("Enter the number : "))
    if n <= 100 and n >= 40:
        print("Try Again !! \n")
        choice = choice - 1
        print("Number of choices left", choice)
        # continue
        # break
    elif n >= 35 and n <= 40:
        print("So Close !! \n")
        choice = choice - 1
        print("Number of choices left", choice)
        # continue
        # break
    elif n >= 0 and n <= 33:
        print("So Close !!\n")
        choice = choice - 1
        print("Number of choices left", choice)
        # continue
        # break
    elif n == 34:
        print("You Won !!\n")
        choice = choice - 1
        print("Number of choices left",choice)
        break
    # elif choice == 0:
        # print("Sorry you ran out of choices !!", choice)
       # break





    """
n = int(input("Enter a number to start the Game : "))
for item in n :
    if n < 100 or n >= 80 :
        print("Try Again !!")
        choice = choice -1
    elif n >= 50 or n < 80:
        print("Try Again !!")
        choice = choice - 1
    elif n >= 20 or n <= 40 :
        print("So Close !!")
        choice = choice - 1
    elif n == 34 :
        print("You won the Game !!")
    """




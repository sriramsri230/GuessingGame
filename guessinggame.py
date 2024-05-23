import random

lower= int(input("Enter the Start Number: "))
higher= int(input("Enter the End Number: "))

x= random.randint(lower,higher)

print("I have guessed some random number ","Try to find it!")

while True:
    guess= int(input("Guess that number: "))
    if guess==x:
        print("Wow! That's amazing, You Found the Correct Number")
    elif guess<x:
        print("Sorry! you guessed smaller number")
    else:
        print("Sorry! you guessed Larger Number")
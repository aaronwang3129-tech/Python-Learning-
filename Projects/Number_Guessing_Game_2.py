import random

answer = random.randint(1,10)
lives = 0

print("Welcome to Number Guessing Game!")
print("You have 3 chances to guess a number 1-10!")

while lives < 3:
    guess = int(input("Guess: "))
    if guess != answer and guess <= 10:
        lives = lives + 1
        if lives == 1:
            print("Incorrect! You have 2 more chances to guess")
        elif lives == 2:
            print("Incorrect! You have 1 more chance to guess")
        elif lives == 3:
            print("Incorrect! You lose!")
            print("The answer was " + str(answer) + "!")
            while True:
                rounds = input("Type 'Yes' to play again or 'No' to exit: ").lower()
                if rounds == "yes":
                    lives = 0
                    print("Welcome to Number Guessing Game!")
                    print("You have 3 chances to guess a number 1-10!")
                    answer = random.randint(1, 10)
                    break
                elif rounds == "no":
                    print("Thank you for playing!")
                    break
                else:
                    print("Please type a valid response (Yes/No)")
    elif guess > 10:
        print("Please type a valid response")
    else:
        print("Correct!")
        while True:
            rounds = input("Type 'Yes' to play an another round or 'No' to exit: ").lower()
            if rounds == "yes":
                lives = 0
                print("Welcome to Number Guessing Game!")
                print("You have 3 chances to guess a number 1-10!")
                answer = random.randint(1, 10)
                break
            elif rounds == "no":
                print("Thank you for playing!")
                break
            else:
                print("Please type a valid response")




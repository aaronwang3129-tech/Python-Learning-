import random

print("Guess a number 1-100!")
print("Keep guessing until you get the right number.")
print("I will tell you if it is too high or too low.")
answer = random.randint(1,100)
guess = 0
attempt = 0

while guess != answer:
    guess = int(input("Guess: "))
    if guess < answer:
        attempt = attempt + 1
        print("Too low!")
    elif guess > answer:
        attempt = attempt + 1
        print("Too high!")
    else:
        print("Correct!")
        print("You guessed the right number in " + str(attempt) + " attempts!")
        while True:
            rounds = input("Would you like to play again? (Yes/No): ").lower()
            if rounds == "yes":
                print("Guess a number 1-100!")
                print("Keep guessing until you get the right number.")
                print("I will tell you if it is too high or too low.")
                answer = random.randint(1, 100)
                attempt = 0
                break
            elif rounds == "no":
                print("Thank you for playing!")
                break
            else:
                print("Type a valid option")


import random

print("Welcome to the Rock Paper Scissors game!")
def main():
    while True:
        play_game()
        while True:
            again = input("Do you want to play again? (y/n): ").lower()
            if again == "y" or again == "yes":
                break
            elif again == "n" or again == "no":
                print("Thank you for playing!")
                return
            else:
                print("Please type a valid response")
def play_game():
    user_lives = 5
    computer_lives = 5
    rounds = 0
    while True:
        print("----------------------------------------------")
        if user_lives == 0:
            print("You Lose the Rock Paper Scissors Game!")
            return
        elif computer_lives == 0:
            print("You Win the Rock Paper Scissors Game!")
            return
        print("Round " + str(rounds + 1))
        user_move = input("Type your move (Rock, Paper, or Scissors): ").lower()
        computer_move = random.choice(["Rock", "Paper", "Scissors"])
        print("I choose " + computer_move + "!")
        if ((user_move == "rock" or user_move == "r" and computer_move == "Scissors") or
                (user_move == "paper" or user_move == "p" and computer_move == "Rock") or
                (user_move == "scissors" or user_move == "s" and computer_move == "Paper")):
            rounds += 1
            computer_lives -= 1
            print("You Win Round " + str(rounds) + "!")
        elif ((user_move == "rock" or user_move == "r" and computer_move == "Paper") or
              (user_move == "paper" or user_move == "p" and computer_move == "Scissors") or
              (user_move == "scissors" or user_move == "s" and computer_move == "Rock")):
            rounds += 1
            user_lives -= 1
            print("You Lose Round " + str(rounds) + "!")
        elif ((user_move == "rock" or user_move == "r" and computer_move == "Rock") or
              (user_move == "paper" or user_move == "p" and computer_move == "Paper") or
              (user_move == "scissors" or user_move == "s" and computer_move == "Scissors")):
            rounds += 1
            print("It's a Tie!")
        else:
            print("Please type a valid response")
        print("Your lives: " + str(user_lives))
        print("Computer lives: " + str(computer_lives))
main()








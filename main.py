# Define Functions Under This
import random


def RPS():
    choices = ['rock', 'paper', 'scissors']
    print("Rock, Paper, Scissors!")
    guess = input("Enter your choice: ") # asks to enter choice in console
    computer_guess = random.choice(choices) # picks a random choice from the list called choices

    print("The computer picked " + computer_guess)
    if (computer_guess == guess):
        print("Its a tie!")
    elif (guess == "rock" and computer_guess == "scissors"):
        print("You win:)")
    elif (guess == "paper" and computer_guess == "rock"):
        print("You win :)")
    elif (guess == "scissors" and computer_guess == "paper"):
        print("You win:)")
    elif (guess == "rock" and computer_guess == "paper"):
        print("You lose:(")
    elif (guess == "paper" and computer_guess == "scissors"):
        print("You lose:(")
    elif (guess == "scissors" and computer_guess == "rock"):
        print("You lose:(")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    RPS()

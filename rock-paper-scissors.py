############## ROCK-PAPER-SCISSORS GAME BY ATHIGAN SINNATHURAI ###################

import random

print("Let's play rock-paper-scissors! First to 3 wins!")


def play():
    options = ["rock", "paper", "scissors"]
    yourScore = 0
    computerScore = 0
    while yourScore < 3 and computerScore < 3:
        selection = input("Choose: rock, paper, scissors?\n\n")
        computer = random.choice(options)

        if selection.lower() == computer:
            print(f"Draw: both chose {computer}.")
        elif selection.lower() == "paper":
            if computer == "rock":
                print("Win! Paper beats rock!")
                yourScore += 1
            else:
                print("Lose: Scissors beat paper")
                computerScore += 1
        elif selection.lower() == "rock":
            if computer == "scissors":
                print("Win! Rock beats scissors")
                yourScore += 1
            else:
                print("Lose: Paper beat rock")
                computerScore += 1
        elif selection.lower() == "scissors":
            if computer == "paper":
                print("Win! Scissors beat paper")
                yourScore += 1
            else:
                print("Lose: Rock beats scissors")
                computerScore += 1
        else:
            print("Invalid input")

    if yourScore > computerScore:
        print(f"Congratulation! You win the game by a score of {yourScore} to {computerScore}!")
    else:
        print(f"The computer wins the game by a score of {computerScore} to {yourScore}")

    decision = input("Would you like to play again? [Yes/No]")

    while True:
        if decision.lower() == "yes":
            play()
        elif decision.lower() == "no":
            print("Thank you for playing rock-paper-scissors!")
            break
        else:
            decision = input("Invalid answer! Please try again. \nWould you like to play again? [Yes/No]")

play()

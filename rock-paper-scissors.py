############## ROCK-PAPER-SCISSORS GAME BY ATHIGAN SINNATHURAI ###################
import random

print("Let's play rock-paper-scissors! First to 3 wins!")


def play():
    options = ["rock", "paper", "scissors"]
    your_score = 0
    computer_score = 0
    while your_score < 3 and computer_score < 3:
        selection = input("Choose: rock, paper, scissors?\n\n")
        computer = random.choice(options)

        if selection.lower() == computer:
            print(f"Draw: both chose {computer}.")
        elif selection.lower() == "paper":
            if computer == "rock":
                print("Win! Paper beats rock!")
                your_score += 1
            else:
                print("Lose: Scissors beat paper")
                computer_score += 1
        elif selection.lower() == "rock":
            if computer == "scissors":
                print("Win! Rock beats scissors")
                your_score += 1
            else:
                print("Lose: Paper beat rock")
                computer_score += 1
        elif selection.lower() == "scissors":
            if computer == "paper":
                print("Win! Scissors beat paper")
                your_score += 1
            else:
                print("Lose: Rock beats scissors")
                computer_score += 1
        else:
            print("Invalid input")

    if your_score > computer_score:
        print(f"Congratulation! You win the game by a score of {your_score} to {computer_score}!")
    else:
        print(f"The computer wins the game by a score of {computer_score} to {your_score}")

    decision = input("Would you like to play again? [Yes/No]")

    while True:
        if decision.lower() == "yes":
            play()
        elif decision.lower() == "no":
            exit(1)
        else:
            decision = input("Invalid answer! Please try again.\nWould you like to play again? [Yes/No]")


play()

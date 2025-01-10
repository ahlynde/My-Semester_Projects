#Amelie Lynde
#1/6/25
#Rock Paper Scissors
#Int
import random
player_score = 0 #Global
computer_score = 0 #Global
#Funtions
#Main
def game():
    global player_score
    global computer_score
    while True:
        #Player's Choice
        print("Please select one of the three options")
        player = input("Selection: ")
        #Computer's Choice
        computer = random.randint(1,3)
        if computer == 1:
            computer = "rock"
        elif computer == 2:
            computer = "paper"
        elif computer == 3:
            computer = "scissors"
        #Determine the outcome
        if player == "rock" and computer == "rock":
            print("tie, computer chose rock")
            player_score = player_score
            computer_score = computer_score
            print("Your score is ", player_score)
            print("Computer's score is", computer_score)
        elif player == "rock" and computer == "paper":
            print("You won, computer chose paper")
            player_score = player_score + 1
            computer_score = computer_score
            print("Your score is ", player_score)
            print("Computer's score is", computer_score)
        elif player == "rock" and computer == "scissors":
            print("You lost, computer chose scissors")
            player_score = player_score
            computer_score = computer_score + 1
            print("Your score is ", player_score)
            print("Computer's score is", computer_score)
        if player == "paper" and computer == "rock":
            print("You won!")
            player_score = player_score + 1
            computer_score = computer_score
            print("Your score is ", player_score)
            print("Computer's score is", computer_score)
        elif player == "paper" and computer == "paper":
            print("tie")
            player_score = player_score
            computer_score = computer_score
            print("Your score is ", player_score)
            print("Computer's score is", computer_score)
        elif player == "paper" and computer == "scissors":
            print("You lost")
            player_score = player_score
            computer_score = computer_score + 1
            print("Your score is ", player_score)
            print("Computer's score is", computer_score)
        if player == "scissors" and computer == "rock":
            print("You lost")
            player_score = player_score
            computer_score = computer_score + 1
            print("Your score is ", player_score)
            print("Computer's score is", computer_score)
        elif player == "scissors" and computer == "paper":
            print("You won!")
            player_score = player_score + 1
            computer_score = computer_score
            print("Your score is ", player_score)
            print("Computer's score is", computer_score)
        elif player == "scissors" and computer == "scissors":
            print("tie")
            player_score = player_score
            computer_score = computer_score
            print("Your score is ", player_score)
            print("Computer's score is", computer_score)
        #Ask player if they want to continue
        playagain = input("Would you like to play again")
        if playagain == "yes":
            print("Restarting...")
        elif playagain == "no":
            print("Ok, thanks for playing")
            break
print("Welcome to Rock, Paper, Scissors")
game()

import random

def rps(turns):
    wins=0
    loss=0
    for turn in range(turns):
        options=["rock", "paper", "scissors"]
        computer_choice=random.choice(options)
        user_choice=""
        while True:    
            play_choice=input("\nWhat do you play, rock, paper, or scissors? ")
            user_choice=play_choice.lower()
            if user_choice=="rock" or user_choice=="paper" or user_choice=="scissors":
                print("Rock, paper, scissors, shoot!")
                print(f"Computer played {computer_choice}")

            if user_choice=="rock":
                if computer_choice=="scissors":
                    print("You won!")
                    wins+=1
                    break
                elif computer_choice=="paper":
                    print("You lost!")
                    loss+=1
                    break
                else:
                    print("Draw!")
                    wins+=.5
                    loss+=.5
                    break
            elif user_choice=="paper":
                if computer_choice=="rock":
                    print("You won!")
                    wins+=1
                    break
                elif computer_choice=="scissors":
                    print("You lost!")
                    loss+=1
                    break
                else:
                    print("Draw!")
                    wins+=.5
                    loss+=.5
                    break
            elif user_choice=="scissors":
                if computer_choice=="paper":
                    print("You won!")
                    wins+=1
                    break
                elif computer_choice=="rock":
                    print("You lost!")
                    loss+=1
                    break
                else:
                    print("Draw!")
                    wins+=.5
                    loss+=.5
                    break
            else:
                print("Input only rock, paper, or scissors.")
        print(f"The score is: {wins} - {loss}")
        if wins>turns/2:
            print("You won the entire match!")
            break
        elif loss>turns/2:
            print("The computer won the entire match!")
            break
    if wins==loss:
        print("It's a draw!")

turns=int(input("How many matches? "))
rps(turns)
import random

human = input("Choose one: rock, paper, or scissors ").upper()
computer = random.randint(1,3)

if computer == 1:
    computer = "ROCK"
elif computer == 2:
    computer = "PAPER"
elif computer == 3:
    computer = "SCISSORS"
        
print("Computer chooses " + computer)


if computer == "ROCK" and human == "PAPER":
    print("User wins")
elif computer == "PAPER" and human == "ROCK":
    print("Computer wins")
elif computer == "SCISSORS" and human == "PAPER":
    print("Computer wins")
elif computer == "PAPER" and human == "SCISSORS":
    print("User wins")
elif computer == "ROCK" and human == "SCISSORS":
    print("Computer wins")
elif computer == "SCISSORS" and human == "ROCK":
    print("User wins")
else:
    print("Tie")
    
        
        
    

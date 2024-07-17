import random

choice = [ "rock", "paper", "scissor"]

computer = random.choice(choice)
you = input("enter rock , paper or scissor :" ).lower()

if you not in choice :
    print("invalid ")

print(f"computer chose : {computer}")
print(f"you chose :{you}")

if(computer == you) :
    print("its a tie")

elif(you== "rock" and computer == "scissor" or\
     you== "paper" and computer == "rock" or\
     you== "scissor" and computer == "paper" ) :
    print("congrats !!!! you won :)!!!")
    
else :
    print("computer won!! better luck next time :( ")



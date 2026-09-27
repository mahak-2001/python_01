import random

'''
Stone, Paper, Scissor Game
stone = 1
paper = -1
scissor = 0
'''

def play_game():

    # Score variables
    your_score = 0
    computer_score = 0

    while True:

        print("\n========================== ROCK PAPER SCISSORS ==========================")
        print("\n1. Stone 🪨 (1)")
        print("2. Paper 📄 (-1)")
        print("3. Scissors ✂️ (0)\n")

        you = int(input("Enter Your Choice: "))

        # Computer randomly chooses
        computer = random.choice([1, -1, 0])

        if computer == you:
            print("\nIt's a Draw (=).")

        elif computer == 1 and you == -1:
            print("\nYou chose = Paper 📄")
            print("Computer chose = Stone 🪨")
            print("You win 🎉")

            your_score += 1

        elif computer == 1 and you == 0:
            print("\nYou chose = Scissor ✂️")
            print("Computer chose = Stone 🪨")
            print("You lose, Computer wins 🎉")

            computer_score += 1

        elif computer == -1 and you == 1:
            print("\nYou chose = Stone 🪨")
            print("Computer chose = Paper 📄")
            print("You lose, Computer wins 🎉")

            computer_score += 1

        elif computer == -1 and you == 0:
            print("\nYou chose = Scissor ✂️")
            print("Computer chose = Paper 📄")
            print("You win 🎉")

            your_score += 1

        elif computer == 0 and you == 1:
            print("\nYou chose = Stone 🪨")
            print("Computer chose = Scissor ✂️")
            print("You win 🎉")

            your_score += 1

        elif computer == 0 and you == -1:
            print("\nYou chose = Paper 📄")
            print("Computer chose = Scissor ✂️")
            print("You lose, Computer wins 🎉")

            computer_score += 1

        else:
            print("Something went wrong.")

        # Scoreboard
        print("\n==================== SCOREBOARD ====================")
        print("Your Score     :", your_score)
        print("Computer Score :", computer_score)
        print("====================================================")

        # Ask for another round
        again = input("\nDo you want to play another round? (yes/no): ")

        if again.lower() != "yes":
            print("\n==================== FINAL SCORE ====================")
            print("Your Score     :", your_score)
            print("Computer Score :", computer_score)
            print("====================================================")
            print("\nThanks for playing! 👋")
            break


play_game()


# '''
# stone,paper,scissor game
# stone=1
# paper=-1
# scissor=0
# '''
# def play_game(computer=1):
#  print("\n==========================ROCK PAPER SCISSORS==========================")
#  print("\n1.stone 🪨 (1)")
#  print("2.paper 📄 (-1)")
#  print("3.scissors ✂️ (0)\n")

#  you=int(input("Enter Your Choice: "))
#  dict={
#     "stone":1,
#     "paper":-1,
#     "scissor":0
#     }
#  if(computer==you):
#     print(" It's a Draw (=).")
#  elif(computer==1 and you==-1):
#     print("\n You chose= Paper📄.\n Computer chose= Stone🪨\n")
#     print("You win.🎉")
#  elif(computer==1 and you==0):
#     print("\n You chose= Scissor✂️\n Computer chose= Stone🪨\n")
#     print("You lose,computer win🎉.")
#  elif(computer==-1 and you==1):
#     print("\n You chose= Stone🪨.\n Computer chose= Paper📄\n")
#     print("You lose,Computer win🎉.")
#  elif(computer==-1 and you==0):
#     print("\n You chose= Scissor✂️.\n Computer chose= Paper📄\n")
#     print("You win.🎉")
#  elif(computer==0 and you==1):
#     print("\n You chose= Stone🪨.\n Computer chose= Scissor✂️\n")
#     print("You win.🎉")
#  elif(computer==0 and you==-1):
#     print("\n You chose= Paper📄.\n Computer chose= Scissor✂️\n")
#     print("You lose,Computer win🎉.")
#  else:
#     print("Something went wrong.")

# print("=======================================================================")
# play_game()
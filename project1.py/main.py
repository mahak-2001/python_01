'''
stone,paper,scissor game
stone=1
paper=-1
scissor=0
'''
def play_game(computer=1):
 print("\n==========================ROCK PAPER SCISSORS==========================")
 print("\n1.stone 🪨 (1)")
 print("2.paper 📄 (-1)")
 print("3.scissors ✂️ (0)\n")

 you=int(input("Enter Your Choice: "))
 dict={
    "stone":1,
    "paper":-1,
    "scissor":0
    }
 if(computer==you):
    print(" It's a Draw (=).")
 elif(computer==1 and you==-1):
    print("\n You chose= Paper📄.\n Computer chose= Stone🪨\n")
    print("You win.🎉")
 elif(computer==1 and you==0):
    print("\n You chose= Scissor✂️\n Computer chose= Stone🪨\n")
    print("You lose,computer win🎉.")
 elif(computer==-1 and you==1):
    print("\n You chose= Stone🪨.\n Computer chose= Paper📄\n")
    print("You lose,Computer win🎉.")
 elif(computer==-1 and you==0):
    print("\n You chose= Scissor✂️.\n Computer chose= Paper📄\n")
    print("You win.🎉")
 elif(computer==0 and you==1):
    print("\n You chose= Stone🪨.\n Computer chose= Scissor✂️\n")
    print("You win.🎉")
 elif(computer==0 and you==-1):
    print("\n You chose= Paper📄.\n Computer chose= Scissor✂️\n")
    print("You lose,Computer win🎉.")
 else:
    print("Something went wrong.")

print("=======================================================================")
play_game()
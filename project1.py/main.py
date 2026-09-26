'''
stone,paper,scissor game
stone=1
paper=-1
scissor=0
'''
computer=1
you=int(input("enter your choise: "))
dict={
    "stone":1,
    "paper":-1,
    "scissor":0
    }
if(computer==you):
    print("it's a draw.")
elif(computer==1 and you==-1):
    print("you choose=paper,computer choose=stone")
    print("you win.")
elif(computer==1 and you==0):
    print("you choose=scissor,computer choose=stone")
    print("you lose,computer win.")
elif(computer==-1 and you==1):
    print("you choose=stone,computer choose=paper")
    print("you lose,computer win.")
elif(computer==-1 and you==0):
    print("you choose=scissor,computer choose=paper")
    print("you win.")
elif(computer==0 and you==1):
    print("you choose:stone,computer choose=scissor")
    print("you win.")
elif(computer==0 and you==-1):
    print("you choose=paper,computer choose=scissor")
    print("you lose,computer win.")
else:
    print("something went wrong.")
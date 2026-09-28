# find the word and check it present or not.and
f=open("poem.txt","r",encoding="utf-8")
data = f.read()
if "Yes" in data:
    print("word is present")
else:
    print("not present")


import random
def game():
    print("you are playing a game..")
    score = random.randint(1,62)
    #fetch the hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"your score: {score}")
    if(score>hiscore):
    #write this hiscore to the file
      with open("hiscore.txt","w") as f:
        f.write(str(score))
        
    return score
game()

# #table for 1 to 20:
# n=int(input("enter a no."))
# print(f"table of {n}")
# for i in range(1,11):
#     print(f"{n*i}")
    
# def genterateTable(n):
#     table = ""
#     for i in range(1,11):
#         table += f"{n}*{i}={n*i}\n"
#     with open(f"tables/table_{n}","w") as f:
#         f.write(table)

# for i in range(2,21):
#         genterateTable(i)
        
        
word = "No"
with open("poem.txt","r") as f:
    content = f.read()
    
contentNew =content.replace(word,"######")

with open("poem.txt","w") as f:
    f.write(contentNew)
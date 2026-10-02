# find the word and check it present or not.and
f=open("poem.txt","r",encoding="utf-8")
data = f.read()
if "Yes" in data:
    print("word is present")
else:
    print("not present")

#create a game:
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


#table for 1 to 20:
n=int(input("enter a no."))
print(f"table of {n}")
for i in range(1,11):
    print(f"{n*i}")
    
#create table file:
def genterateTable(n):
    table = ""
    for i in range(1,11):
        table += f"{n}*{i}={n*i}\n"
    with open(f"tables/table_{n}","w") as f:
        f.write(table)
for i in range(2,21):
        genterateTable(i)
        
#replace word:
word = "Johny"
with open("poem.txt","r") as f:
    content = f.read()
contentNew =content.replace(word,"##")
with open("poem.txt","w") as f:
    f.write(contentNew)
    
#replace words:
words = ["Ha","No"]
with open("poem.txt","r") as f:
    content = f.read()
for word in words:
   content =content.replace(words,"#" * len(word))
with open("poem.txt","w") as f:
    f.write(content)
    
#check the word is presented or not:
with open("log.txt","r") as f:
    content =f.read()
if ("python" in content):
    print("python is present.")
else:
    print("python is not present.")

#check the word is in which line no located:
with open("log.txt","r") as f:
      lines =f.readlines()
lineno=1
for line in lines:
    if ("python" in line):
      print(f"python is present in line no.{lineno}")
      break
    lineno += 1 
else:
    print("python is not present.")
    
#create copy of file:
with open("this.txt") as f:
    content = f.read()
with open("this_copy.txt","w") as f:
    f.write(content)
    
#check both are identical or not:
with open("this.txt") as f:
    content = f.read()
with open("poem.txt") as f:
    content1 = f.read()
if content==content1 :
    print("Yes! both files are identical.")
else:
    print("No! both files are not identical.")

#clear text:
with open("this_copy.txt") as f:
    content = f.read()
with open("this_copy.txt","w") as f:
    f.write(content)

#rename the file:
with open("this.txt") as f:
    content = f.read()
with open("renamed_by_pyhton.txt","w") as f:
    f.write(content)
#read a file:
f=open("01_first.py")
data = f.read()
print(data)
f.close()

#write a file:
st="this is file written program."
file=open("file.txt","w")
file.write(st)
f.close()

#add line in last
st="have a good day!"
f=open("file.txt","a")
f.write(st)
f.close()

#read lines of a file:
f = open("file.txt")
lines = f.readlines()
print(lines, type(lines))
line1 = f.readline()
print(line1, type(line1))
line2 = f.readline()
print(line2)
f.close()

#with statement (close file automatically):
f=open("file.txt")
print(f.read())
f.close()
#the same can be written using the statement like this:
with open("file.txt") as f:
    f.read()
    
    
with open("tupple.py","r",encoding="utf-8") as file:
    print(file.read())
    file.close()
print(file.closed)

with open("trying.py","r",encoding="utf-8") as file:
    first_ten=file.read(10)
print(first_ten)

file=open("test.py","r",encoding="utf-8")
print(file.read())
file.close()
print(file.closed)

#for reading a single line
with open("test1.py","r") as file: 
 first_line=file.readline()
 first_second=file.readline()
print(first_line)
print(first_second)

#for reading all lines individually.
with open("test2.py","r") as file: 
 lines=file.readlines()
print(lines)

#counting lines
line_count=0
with open("test2.py","r") as file: 
   for line in file:
      line_count +=1
print("number of lines:",line_count)
      
#countingwords and characters
with open("test2.py","r") as file: 
   content=file.read()
character_count=len(content)
word_count=len(content.split())

with open("tupple.py","r",encoding="utf-8") as file:
    print(file.read())
    
#WRITING MULTIPLE LINES
with open("message.txt","w",encoding="utf-8") as file:
    file.write("hello this is my python class.\n")
    file.write("hello this is my python 2nd class.")

# add and make new file.
lines=[
    "apple\n",
    "banana\n",
    "mango"
]
with open("fruits.txt","w",encoding="utf-8") as file:
    file.writelines(lines)

#set formatted
fruits=[
    "apple\n",
    "banana\n",
    "mango"
]
with open("fruits.txt","w",encoding="utf-8") as file:
    for fruit in fruits:
        file.write(f"{fruit}\n")

#append with 'a' mode

with open("activity.log","a",encoding="utf-8") as file:
    file.write("user logged in.\n")

#x mode to make new file.x mode create a new file.

#file pointer: when they read any word for where they want.they tell the cursor position from where they start.
with open("tupple.py","r",encoding="utf-8") as file:
    print(file.read(5))
    print(file.read(10))


#finding the current position with 'tell()'
with open("tupple.py","r",encoding="utf-8") as file:
    print(file.tell())
    print(file.read(5))
    print(file.tell())
    print(file.read(10))

#change the position with 'seek()'
with open("tupple.py","r",encoding="utf-8") as file:
    print(file.read(5))
    file.seek(0)
    print(file.read(10))
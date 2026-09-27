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

#with statement:
f=open("file.txt")
print(f.read())
f.close()
#the same can be written using the statement like this:
with open("file.txt") as f:
    f.read()
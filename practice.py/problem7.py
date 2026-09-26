#greater no. out of 3 no.
def greater(a,b,c):
    if(a>b and a>c):
     print(f"a is greater no.:{a}")
    elif(b>a and b>c):
        print(f"b is greater no.:{b}")
    else:
     print(f"c is greater no.:{c}")
greater(45,67,99)

#convert celcius to fahernheit.
def celcius(a):
    f=(a*1.8)+32
    print(f"{a} celcius={round(f,2)} fahernhiet")
celcius(34)
print("thank you",end=" ")
print("nxt program :->>")
    
#convert inch to cm.
def inch(a):
    cm=2.54*a
    print(f"{a} inch = {cm} cm")
inch(56)

#sum of no.
def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n
print(sum(6))

#print a pattern.
def pattern(n):
    if(n==0):
        return 0
    print("*"*n)
    pattern(n-1)
print(pattern(4))

#table of a no.
def table():
    for i in range(1,11):
        print(f"{n}*{i}={n*i}")
     
n=int(input("enter a no.: "))
table()

#function to remove a given word from a list and strip it at the same time.
def list():
    l1=["mahak","jiya","bhumi","sonu"]
    l1.remove("jiya")
    # l1.strip()
    print(l1)
list()
    
        
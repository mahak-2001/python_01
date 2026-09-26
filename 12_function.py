a=int(input("enter a no.: "))
b=int(input("enter a no.: "))
c=int(input("enter a no.: "))
average=((a+b+c)/3)
print(average)

#function defination.
def avg():
    a=int(input("enter a no.: "))
    b=int(input("enter a no.: "))
    c=int(input("enter a no.: "))   
    average=((a+b+c)/3)
    print(average)
avg() #function call
print("thank you")
# avg()

def greet():
    name="mahak"
    print(f"Good Day!{name}")
greet()

def greet(name,ending):
    print(f"Good Day!{name}")
    print(ending)
greet("harry","thank you")
greet("mohan","thank you")
greet("divya","thanks")

def greet(name):
    gr="hello"+name
    return gr
a=greet ("mahak")
# a will contain hello mahak.

def goodDay(name,ending="thank you"):
    print(f"good day ,{name}")
    print(ending)
goodDay("harry","thanks")
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
    
        # #ques.1
# def calculate (a,b=5):
#      return a+b,a*b
# x,y=calculate(4)
# print(x,y)#9,20
# print(calculate(4,2)[1])

# #ques.2
# def display(a,b,c=10):
#      print(a,b,c)
# display(1,c=3,b=2)
# display(4,5)

# #ques.3
# def calculate(number):
#      if number%2==0:
#           return number//2
     
#      print("odd number")
#      return number*3
# print(calculate(8))
# print(calculate(5))

# #ques.4
# def add_item(item,container=[]):
#      container.append(item)
#      return container
# print(add_item(1))
# print(add_item(2))
# print(add_item(3,[]))
# print(add_item(4))

# #ques.5
# def analyse(first,*values):
#      return first,max(values),sum(values[::2])
# print(analyse(10,3,8,5,2))

# #ques.6
# def build_record(**data):
#      data["total"]=sum(
#           value
#           for value in data.values()
#           if isinstance(value,int)
#           )
#      return sorted(data.items())
# print(build_record(a=2,b=3,name="X"))

# #ques.7
# def calculate(a,b,c):
#      return a+b*c
# values=(2,3)
# options={"c":4}
# print(calculate(*values,**options))

# #ques.8
# def report(name,*,score=0,passed=True):
#      return f"{name}:{score}:{passed}"
# print(report("Riya",score=88))
# print(report("kabir",passed=False,score=40))

# #ques.9
# def change(number): 
#     number += 10 
#     return number 
# value = 5 
# print(change(value), value) 

# #ques.10
# def update(data): 
#     data[0] += 5 
#     data.append(sum(data)) 
# numbers = [1, 2, 3] 
# update(numbers) 
# print(numbers) 
 
#  #ques.11
# def update(data): 
#     data = data + [4] 
#     data[0] = 99 
#     return data 
# numbers = [1, 2, 3] 
# new_numbers = update(numbers) 
# print(numbers) 
# print(new_numbers) 
 
# #ques.12
# def update(record): 
#     record["b"] = record.get("b", 0) + 2 
#     record = {"c": 3} 
#     return record 
# data = {"a": 1, "b": 4} 
# result = update(data) 
# print(data) 
# print(result) 
 
# #ques.13
# def modify(data): 
#     data[1].append(30) 
#     return data + ("done",) 
# values = (10, [20]) 
# result = modify(values) 
# print(values) 
# print(result) 
# x = 10 

# #QUES.14 
# # x=10 #by default
# def outer(): 
#     x = 20 
#     def inner(): 
#         global x 
#         x += 5 
#         print(x) 
#     inner() 
#     print(x) 
# outer() 
# print(x) 
 
# #ques.15
# def outer(): 
#     number = 1 
#     def inner(): 
#         nonlocal number 
#         number *= 3 
#         return number 
#     print(inner(), inner()) 
# outer() 
 
# #ques.16
# def create_power(exponent): 
#     def calculate(number): 
#         return number ** exponent 
#     return calculate 
# square = create_power(2) 
# cube = create_power(3) 
# print(square(4) + cube(2)) 
 
# #ques.17
# functions = [] 
# for number in range(3): 
#     functions.append(lambda: number) 
# print([function() for function in functions]) 
 
# #ques.18
# functions = [] 
# for number in range(3): 
#     functions.append(lambda number=number: number) 
# print([function() for function in functions]) 
  
# #ques.19
# def apply(function, values): 
#     return [ 
#         function(value) 
#         for value in values 
#         if function(value) > 5 
#     ] 
# def transform(number): 
#     return number * number - 1 
# print(apply(transform, [1, 2, 3, 4])) 
 
# #ques.20
# numbers = [1, 2, 3, 4, 5] 
 
# result = list( 
#     map( 
#         lambda number: number * 2, 
#         filter(lambda number: number % 2 == 1, numbers) 
#     ) 
# ) 
# print(result) 
 
# #ques.21
# def add(a, b): 
#     return a + b 
# def multiply(a, b): 
#     return a * b 
# operations = { 
#     "addition": add, 
#     "multiplication": multiply 
# } 
# result = ( 
#     operations["addition"](2, 3) 
#     + operations["multiplication"](2, 3) 
# ) 
# print(result) 
 
 
# # ques.22
# def calculate(number): 
#     if number <= 1: 
#         return 1 
#     return number + calculate(number - 2) 
# print(calculate(6)) 
 
# #ques.23
# def trace(number): 
#     if number == 0: 
#         return 
#     print(number, end=" ") 
#     trace(number - 1) 
#     print(number, end=" ") 
# trace(3) 
 
# #ques.24
# def flatten(data): 
#     result = [] 
 
#     for item in data: 
#         if isinstance(item, list): 
#             result.extend(flatten(item)) 
#         else: 
#             result.append(item) 
 
#     return result 
# values = [1, [2, [3, 4]], 5] 
# print(flatten(values))

#ques.25
def sequence(number):
    while number>0:
        yield number
        number-=2
result=sequence(5)
print(next(result))
print(list(result))  

#ques.26
def combine(a:int,b:int)->int:
    return str(a)+str(b)
result=combine(2,3)
print(result)
print(type(result).__name__)

##ques.27 -it shows error
# x=10
# def display():
#     print(x)
#     x=20
# display()

#ques.28
def modify(values):
    for index,value in enumerate(values):
        if value%2==0:
            values[index]=value//2
        else:
            values[index]=value*3+1
        return tuple(reversed(values))
numbers=[1,2,3,4]
result=modify(numbers)
print(numbers)
print(result)








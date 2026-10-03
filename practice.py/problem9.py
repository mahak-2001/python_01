class programmer:
   company="Microsoft"
   def __init__(self,name,salary,pin):
      self.name=name
      self.salary=salary
      self.pin=pin
      
p=programmer("mahak",1200000,123027)
print(p.name,p.salary,p.pin,p.company)
p=programmer("rohan",190000,123567)
print(p.name,p.salary,p.pin,p.company)


class calculator:
   def __init__(self,num,num1):
      self.num=num*num
      self.num1=num1*num1*num1
@staticmethod
def greet():
   print("Hello")
greet()
p.calculator=calculator(5,10)
print(p.calculator.num)
print(p.calculator.num1)


class a:
   def init__(self,name):
      self.name="meow"
b=a("mahak")
print(b.name)


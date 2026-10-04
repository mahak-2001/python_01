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


# class calculator:
#    def __init__(self,num,num1):
#       self.num=num*num
#       self.num1=num1*num1*num1
# @staticmethod
# def greet():
#    print("Hello")
# greet()
# p.calculator=calculator(5,10)
# print(p.calculator.num)
# print(p.calculator.num1)


class calculator:
   def __init__(self,n):
      self.n = n
      
   @staticmethod
   def greet():
      print("hello!")   
   greet()
      
   def square(self):
      print(f"the square is {self.n*self.n}")
      
   def cube(self):
      print(f"the cube is {self.n*self.n*self.n}")
      
   def squareroot(self):
      print(f"the squareroot is {self.n**1/2}")
a=calculator(4)
a.square()
a.cube()
a.squareroot()



class demo():
   a=4
o=demo()
print(o.a) #print the class attribute becaus instance attribute is not present.
o.a=0 #instance attribute is set.
print(o.a)#print the instance attribute becaus instance attribute is not present.
print(demo.a)# print class  attribute



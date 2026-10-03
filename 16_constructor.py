class employee:
    language = "py" #class attributes
    salary = 200000
    
    def __init__(self): # dunder method which is automatically called.
        print("i am creating an object")

    def getInfo(self):
        print(f"This Language is {self.language}. The Salary is {self.salary}")
                 
    @staticmethod
    def greet():
        print("good morning")
        
rohan =employee()
rohan.name="rohan"
print(rohan.name,rohan.salary)


#init method
class employee:
    language = "py" #class attributes
    salary = 200000
    
    def __init__(self,name,salary,language): # dunder method which is automatically called.
        self.name=name
        self.salary=salary
        self.language=language
        print("i am creating an object")
        
rohan =employee("rohan",100000,"java")
# rohan.name="rohan"
print(rohan.name,rohan.salary,rohan.language)
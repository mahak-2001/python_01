#class refers to blueprint of object.

class employee:
    language = "py" #class attributes
    salary = 200000
mahak =employee()
print(mahak.language,mahak.salary)
rohan =employee()
rohan.name="rohan" #object attribute.
print(rohan.name,rohan.salary,rohan.language)
# here name is object/instance attribute and salary and language
#  are class attributes as they directly belong to the class.


#instance attribute get preference over object.
class employee:
    language = "py" #class attributes
    salary = 200000
rohan =employee()
rohan.language="javascript" #instance attribute.
print(rohan.salary,rohan.language)


class employee:
    language = "py" 
    salary = 200000
    
    def getInfo(self):
        print(f"This Language is {self.language}. The Salary is {self.salary}")
        
rohan =employee()
rohan.language="javascript"
rohan.getInfo()


@staticmethod
def greet():
    print("hii")
greet()



class employee:
    company="ITC"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")
        
        
class programmer:
    company="ITC Infotech"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")    
        
    def showLanguage(self):
        print(f"the name is {self.name} and the salary is {self.language}")
        
a = employee()
b = programmer()
print(a.company,b.company)
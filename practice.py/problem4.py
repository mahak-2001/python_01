# lang={
#     "namaste":"hello",
#     "naam":"name",
#     "kursi":"chair"
# }
# words= input("Enter the word you want meaning of: ")
# print(lang[words])

# s=set()

# n=int(input("enter no.1: "))
# s.add(n)
# n=int(input("enter no.2: "))
# s.add(n)
# n=int(input("enter no.3: "))
# s.add(n)
# n=int(input("enter no.4: "))
# s.add(n)
# n=int(input("enter no.5: "))
# s.add(n)
# n=int(input("enter no.6: "))
# s.add(n)
# n=int(input("enter no.7: "))
# s.add(n)
# n=int(input("enter no.8: "))
# s.add(n)
# print(s)

from operator import le


_set=("18",18)
print(_set)

s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(s,len(s)) # 20 and 20.0 are considered the same in a set, so only one of them is stored. '20' is a string, so it is stored separately.

s={}
print(type(s)) # This will print <class 'dict'> because {} creates an empty dictionary, not a set.
# s.update({"mahak": "python","jiya": "java","rohan": "c++","mohan": "html"})
# s1= input("enter the name you want to search: ")
# print(s.get(s1, "Name not found")) 
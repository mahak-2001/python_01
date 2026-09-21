#tuple is immutable.

a=(1)
print(type(a))
a=(1,)# denote a single tuple
print(type(a))

a=(1,45,"hii","mahak",4785.3,True,45)
print(a)
print(a.count(45))
print(a.index("mahak"))

print(a[1:5])

fruits=("apple","banana","grapes","orange")
a,b,c,d=fruits
print(a)
print(b,d)
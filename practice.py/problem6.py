#table of a no.
n=int(input("enter no.: "))
for i in range(1,11):
    print(f"{n}*{i}={n*i}")
    
# greet the name start with...
l=["harry","sohan","sachin","rohan"]
for name in l:
    if(name.startswith("s")):
     print(f"congratulation {name}")

#table of a no.
n=int(input("enter no.: "))
i=1
while(i<11):
    print(n*i)
    i+=1

#prime or not.
n=int(input("enter no.: "))
for i in range(2,n):
 if(n%i)==0:
    print(f"it' not a prime no. {n}")
    break
else:
    print(f"no. is prime {n}")

#sum of natural no.
n=int(input("enter no.: "))
i=1
sum=0
while(i<=n):
    sum+=i
    i+=1
print(sum)
   
#factorial of a no.
n=int(input("enter no.: "))
product = 1
for i in range(1, n+1):
    product = product*i
print(f"the factorial of {n} is {product}")

#program for making pattern
'''
for n=3
  *
 ***
*****
'''
n=int(input("enter no.: "))
for i in range(1,n+1):
    print(" "*(n-1))
    print("*"* (2*i-1),end="")
    print("\n")
    
    
#call itself again and again.
def fact(n):
    if(n==1 or n==0):
      return 1
    return n*fact(n-1)
n=int(input("enter a no.: "))
print(f"factorail of {n} is : {fact(n)}")
print(f"factorail of {n} is : {fact(n)}")
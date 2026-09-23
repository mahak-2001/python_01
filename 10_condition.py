# if elif else ladder.
a=int(input("enter your age: "))
#multipe if statement:
if(a%2==0):
    print("it is even no.")
    
if(a>=18):
    print("you are eligible for vote.")
elif(a<0):
    print("you are entering invalid age.")
elif(a==0):
    print("you are entering 0 which is not valid age.")
else:
    print("you are not eligible for vote.") 
    
print("program end here.")

    
    

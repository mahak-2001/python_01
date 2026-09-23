# find greater no. in 4 inputs.
a=int(input("enter the no.1: "))
a1=int(input("enter the no.2: "))
a2=int(input("enter the no.:3 "))
a3=int(input("enter the no.:4"))
if(a>a1 and a>a2 and a>a3):
    print("a is greater:",a)
elif(a1>a and a1>a2 and a1>a3):
    print("a is greater:",a1)
elif(a2>a1 and a2>a and a2>a3):
    print("a is greater:",a2)
else:
    print("a3 is greater:",a3)
    
# # another method:
# greatest = a
# if a1>greatest:
#     greatest=a1
# if a2>greatest:
#     greatest=a2
# if a3>greatest:
#     greatest=a3
# print("greatest no. is:",greatest)

#find out student passed or failed:
mark1=int(input("enter the no.1: "))
mark2=int(input("enter the no.2: "))
mark3=int(input("enter the no.:3 "))
total_percentage = (100*(mark1+mark2+mark3))/300

if(total_percentage>=40 and mark1>33 and mark2>33 and mark3>33):
    print("you are passed:",total_percentage)
else:
    print("you are failed,try again next year!")
    

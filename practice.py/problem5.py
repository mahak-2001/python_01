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

#check spam comments in text,detect the spams.
p1="makes a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"
message=input("enter your comment:")
if(p1 in message or p2 in message or p3 in message or p4 in message):
    print("this is a spam.")
else:
    print("this is not a spam.")

#program to find given username contains less than 10 characters or not.
username=input("enter name: ")
if(len(username)<10):
    print("username contain less than 10 characters.")
else:
    print("username contain more than 10 characters.")

#find given name is present in list or not.
l1=["mahak","jiya","teena","neha"]
name=input("enter name:")
if(name in l1):
    print("name present in list.")
else:
    print("name is not present in list.")

#calculate grade of a student from the marks.
marks=int(input("enter marks: "))
if(marks<=100 and marks>=90):
    print("grade excellent.")
elif(marks<90 and marks>=80):
    print("grade A.")
elif(marks<80 and marks>=70):
    print("grade B.")
elif(marks<70 and marks>=60):
    print("grade C.")
elif(marks<60 and marks>=50):
    print("grade D.")
else:
    print("FAIL")

#check given post is talking about name or not.
post="hey mhk is good mahak is very good and mahak is great."
if("mahak" in post):
    print("post is talk about mahak.")
else:
    print("post is not talk about mahak.")

# find the word and check it present or not.and
f=open("poem.txt","r",encoding="utf-8")
data = f.read()
if "Yes" in data:
    print("word is present")
else:
    print("not present")



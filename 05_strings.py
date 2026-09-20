name="mahak rajput"

print(name[1:4])
print(name[-4:-1])
print(name[1:8])
print(name[1:8:2])

print(len(name))
print(name.endswith("put"))
print(name.startswith("Mah"))
print(name.capitalize())
print(name.upper())
print(name.find("rajput")) #this function finds a word and return the index of first occurance of that what in the string.
print(name.replace("mahak","mikku"))
print(name.title()) #capitalize each word
print(name.split()) #split into a list
print(name.isalpha()) #checks all character are letter

a="mahak is good girl.\nbut not a bad girl"
print(a)
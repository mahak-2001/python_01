name=input("enter your name:")
print(f"good afternoon, {name}")

letter='''Dear <|name|>
you are selected!
<|date|>'''
print(letter.replace("<|name|>","mahak").replace("<|date|>","18 dec.2025"))            

name="my name  is mahak"
print(name.find("  "))
print(name.replace("  "," "))

letter="dear mahak,\n\t this python course is nice.\n thanks!"
print(letter)
with open("file.txt") as f:
    c=f.read()
    if "yes" in c:
        print("word is present")
    else:
        print("not present")

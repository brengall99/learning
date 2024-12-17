# Hello Visual Studio Code

editor = ""
while editor != "Visual Studio Code":
    editor = str(input("Editor: ").lower())
    if editor == "word":
        print("awful")
    elif editor == "visual studio code":
        print("an excellent choice!")
        break
    else: 
        print("not good")


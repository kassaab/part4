while True:
    editor = input("Editor: ")
    if editor.lower() == 'visual studio code':
        break
    if editor.lower() == 'word' or editor.lower() == 'notepad':
        print("awful")
    else:
        print("not good")
print("an excellent choice!")
random = ' '
i = 0
while True:
    word = input("Word: ")
    if (' ' + word + ' ') in random:
        break
    else:
        random += word + ' '
        i += 1
print(f"You typed in {i} different words")
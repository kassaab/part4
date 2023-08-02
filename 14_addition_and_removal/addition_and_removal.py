list = []

i = 1
while True:
    print(f"The list is now {list}")
    action = input("a(d)d, (r)emove or e(x)it: ").lower()
    if action == 'x':
        break
    elif action == 'd':
        list.append(i)
        i += 1
    elif action == 'r':
        list.pop(i-2)
        i -= 1
print("Bye!")
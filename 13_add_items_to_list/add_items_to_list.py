list = []
items = int(input("How many items: "))

#i = 0
while items > 0:
    item = int(input("Item: "))
    list.append(item)
    items -= 1
print(list)
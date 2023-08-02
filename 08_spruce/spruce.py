def spruce(size):
    print("a spruce!")
    i = 1
    j = 1
    space = size - 1
    while i <= size:
        print(space * " "+j * '*')
        i += 1
        j += 2
        space -= 1
    print((size - 1) * " "+"*")

if __name__ == "__main__":
    spruce(5)
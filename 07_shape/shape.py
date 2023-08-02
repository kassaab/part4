def line(number, string):
    if string == "":
        print("*" * number)
    else:
        print(string[0] * number)

def shape(size, Tchar, height, Rchar):
    i = 1
    while i <= size:
        line(i, Tchar)
        i += 1
    while height > 0:
        line(size, Rchar)
        height -= 1

if __name__ == "__main__":
    shape(5, "x", 2, "o")
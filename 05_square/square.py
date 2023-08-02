def line(number, string):
    if string == "":
        print("*" * number)
    else:
        print(string[0] * number)

def square(size, character):
    i = 0
    while i < size:
        line(size, character)
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")
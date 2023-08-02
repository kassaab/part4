def line(number, string):
    if string == "":
        print("*" * number)
    else:
        print(string[0] * number)

def triangle(size):
    i = 1
    while i <= size:
        line(i, "#")
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)

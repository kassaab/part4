def line(number, string):
    if string == "":
        print("*" * number)
    else:
        print(string[0] * number)

if __name__ == "__main__":
    line(5, "x")
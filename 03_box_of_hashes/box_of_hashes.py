def line(number, string):
    if string == "":
        print("*" * number)
    else:
        print(string[0] * number)

def box_of_hashes(height):
    while height > 0:
        line(10, "#")
        height -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)

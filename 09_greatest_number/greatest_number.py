def greatest_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    elif c >= a and c >= b:
        return c


if __name__ == "__main__":
    greatest = greatest_number(11, 1, 9)
    print(greatest)
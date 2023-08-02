def shortest(names: list):
    shoe = 50
    word = ''
    for name in names:
        if len(name) < shoe:
          shoe = len(name)
          word = name
 
    return word

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh",]

    result = shortest(my_list)
    print(result)
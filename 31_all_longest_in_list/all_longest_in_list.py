def all_the_longest(names: list):
    longest = 0
    for name in names:
        if len(name) > longest:
          longest = len(name)
    new = []
    for name in names:
        if len(name) >= longest:
          new.append(name)
          longest = len(name)

    return new

if __name__ == "__main__":
    my_list = ["first", "seco", "fourth", "eleventh", "AbrahamK"]
    print(all_the_longest(my_list))
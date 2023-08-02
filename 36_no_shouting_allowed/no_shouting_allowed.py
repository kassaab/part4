def no_shouting(my_list: list): #list of str
    result = []
    for word in my_list:
        if not word.isupper():
            result.append(word)
    return result


if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)
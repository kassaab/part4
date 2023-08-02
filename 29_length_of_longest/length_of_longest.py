def length_of_longest(my_list):
    longest = len(my_list[0])
    i = 1
    while i < len(my_list):
        if len(my_list[i]) > longest:
            longest = len(my_list[i])
        i += 1
    return longest

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = length_of_longest(my_list)
    print(result)
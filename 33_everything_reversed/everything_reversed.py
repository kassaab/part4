def everything_reversed(my_list):
    result = []
    for string in my_list:
        result.append(string[::-1])
    return result[::-1]


if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
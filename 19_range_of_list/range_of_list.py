def range_of_list(list):
    range = max(list) - min(list)
    return range

if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)
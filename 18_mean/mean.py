def mean(list):
    mean = sum(list) / len(list)
    return mean

if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)
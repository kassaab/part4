def distinct_numbers(my_list):
    my_list.sort()
    new = []
    for i in my_list:
        if i not in new:
            new.append(i)
    return new

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list))
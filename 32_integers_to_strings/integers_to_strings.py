def formatted(my_list):
    i = 0
    new_list = []
    while i < len(my_list):
        new_list.append(f"{my_list[i]:.2f}")
        i += 1
    return new_list



if __name__ == "__main__":
    # my_list = [1.234, 0.3333, 0.11111, 3.446]
    my_list = [0.123, 1.23, 0.0234]
    print(my_list)
    print(formatted(my_list))
    print(my_list)
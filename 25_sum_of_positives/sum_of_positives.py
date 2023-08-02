def sum_of_positives(my_list):
    result = 0
    for i in my_list:
        if i > 0:
            result += i
    return result

if __name__ == "__main__":
    print(sum_of_positives())
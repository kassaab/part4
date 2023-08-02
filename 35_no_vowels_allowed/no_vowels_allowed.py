def no_vowels(my_string: str):
    for char in my_string:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            my_string = my_string.replace(char, '')
    return my_string


if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))
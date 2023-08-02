def most_common_character(string):
    result = 0
    char = ''
    for letter in string:
        if result == 0 or string.count(letter) > result:
            result = string.count(letter)
        
    for letter in string:
        if string.count(letter) >= result:    
            char = letter
            break
    return char

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))


    second_string = "exemplaryelementary"
    print(most_common_character(second_string))
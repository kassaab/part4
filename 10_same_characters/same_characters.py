def same_chars(string, a, b):
    if a >= len(string) or b >= len(string):
        return False    
    if string[a] == string[b]:
        return True
    return False

if __name__ == "__main__":
    print(same_chars("coder", 1, 20))

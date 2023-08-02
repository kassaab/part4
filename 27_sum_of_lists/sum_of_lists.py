def list_sum(a, b):
    new =[]
    i = 0
    while i < len(a):
        new.append(a[i] + b[i])
        i += 1
    return new

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [1, 2, 3]
    print(list_sum(a, b))
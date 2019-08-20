
def numbers(list):
    num = []
    for b in list:
        if b % 2 == 0:
            num.append(b)
    return num
print(numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))
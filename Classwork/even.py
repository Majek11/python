def get_sum(x)-> int:
    total = 0
    for char in x:
        if char.isnumeric():
            temp = int(char)
        if temp % 2 == 0:
            total += temp
    return total

anything = input("Enter nonsense: ")
sense = get_sum(anything)
print(sense)

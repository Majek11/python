def get_sum_of_numbers(number)-> int:
    total = 0
    for char in number:
        if char.isnumeric():
            temp = int(char)
            total += temp
    return total

anything = input("Enter nonsense: ")
sense = get_sum_of_numbers(anything)
print(sense)















  
    

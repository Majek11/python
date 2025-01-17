def get_search_number(number, search)-> int:
    counter = 0
    search_number = str(num)  
    search = 4
    for y in number:
        if search == int(y):
            counter += 1
    return counter

anything = input("Enter nonsense: ")
sense = get_search_number(anything)
print(sense)    
    
    
    
    
    










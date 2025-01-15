def get_cube(number):
    if type(number) == str:
        return 'invalid data'
    return round((number ** 3), 3)
    
    
def get_dollar(number):
    if type(number) == str:
        return 'Not a number'
    return round((number),3)

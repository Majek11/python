integer = int(input('Enter an integer between (0 - 1000): '))

extract_first_number = integer % 10
integer /= 10

extract_second_number = integer % 10
integer /= 10

extract_third_number = integer % 10
integer /= 10

total = extract_first_number + extract_second_number + extract_third_number
print(f'Sum of numbers:  {total}')













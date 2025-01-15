import random

for number in range(2):
    print(random.randrange(1, 101), end=' ')
print(input("\nEnter the sum of two numbers: "))

sum = 0
sum += number

if number != sum:
    print('Incorrect')
else:
    print('Correct')
    

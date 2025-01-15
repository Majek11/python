grade = 7

#if grade >= 60:
#    print("Passed")
#else:
#    print("Failed")

#while grade <= 1000:
 #   grade = grade * 7
  #  print(grade)
  
#for character in 'Programming':
 #   print(character, end=' ')

#total = 0 
#for number in [2, -3, 0, 17, 9]:
#    total = total + number
#    print(total)

#for counter in range(10):
#    print(counter, end=' ')

#total = 0
#for number in range(100001):
#    total += number 
#    print(total)

#total = 0
#grade_counter = 0
#grades = [98, 40, 50, 24, 85, 34, 49, 123, 10, 88]
#for grade in grades:
#    total += grade
#    grade_counter += 1
#average = total / grade_counter
#print(f'Class average is {average}')

total = 0
grade_counter = 0

grade = int(input('Enter grade, -1 to end: '))

while grade != -1:
    total += grade
    grade_counter += 1
    grade = int(input('Enter grade, -1 to end: '))
    
if grade_counter != 0:
    average = total / grade_counter
    print(grade, ' ')
    print(f'Class average is {average:.2f}')
else:
    print('No grades were entered')

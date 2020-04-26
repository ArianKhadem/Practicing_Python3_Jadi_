max_divisor = 0
min_divisor = 1
min_divisor_number = 0
for i in range (1, 6):
    numbers = int(input('Please enter 20 numbers: '))
    divisor = 0
    for j in range (1, numbers + 1):

        div = (numbers % j)
        if div == 0:
            divisor = divisor + 1
        if divisor > max_divisor:
            max_divisor = divisor
            max_divisor_number = numbers
print('The number of divisor of', max_divisor_number, 'is:', max_divisor)
print('Max divisor number is :', max_divisor_number)

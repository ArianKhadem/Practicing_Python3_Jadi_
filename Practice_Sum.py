def get_numbers():
    numbers_for_sum = input('Please enter the numbers: ')
    return numbers_for_sum


def input_condition_checker(add_expression):
    one = ''
    two = ''
    three = ''
    for character in add_expression:
        if character != '+':
            if character == '1':
                one = character + '+' + one
            if character == '2':
                two = character + '+' +  two
            if character == '3': 
                three = character + '+' + three
    sort_numbers = one + two + three
    if sort_numbers[-1] == '+':
        sort_numbers = sort_numbers[:-1]
    return sort_numbers


def main_program():
    print(input_condition_checker(get_numbers()))


main_program()
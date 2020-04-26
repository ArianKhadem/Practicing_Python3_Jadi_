def get_numbers():
    numbers = input('Please enter the age of members : ')
    numbers = input_type_recognizer(numbers)
    return numbers


def input_type_recognizer(Input):
    try:
        testing = int(Input)
        return Input
    except ValueError:
        try:
            testing = float(Input)
            print_results('float', Input)
        except ValueError:
            print_results('not_number', Input)
        get_numbers()

def input_condition_checker(numbers):
    numbers = int(numbers)
    if ((numbers < 10) or (numbers > 90)) and (numbers != -1):
        print_results('input_failed', 'just_a_word')
        get_numbers()
    else:
        return numbers
    return numbers


def print_results(text, results):
    if text == 'total_score':
        print('The total score of Sepidrood in this league is :', results)
    elif text == 'input_failed':
        print('Please just input the ages of members between 10-90')
        print('                                               ')
    elif text == 'old':
        print('The oldest member has',results,'years old!!')
        print('                                               ')
    elif text == 'young':
        print('The Youngest member has',results,'years old!!')
        print('                                               ')
    elif text == 'not_number':
        print('Please just enter the number not Characters!!')
        print('                                               ')
    elif text == 'float':
        print('Please just enter the integer numbers not float!!')
        print('                                               ')


for i in range(21):
    the_number = get_numbers()
    # the_number = int(the_number)
    print(type(the_number), the_number)
    numbers = input_condition_checker(the_number)


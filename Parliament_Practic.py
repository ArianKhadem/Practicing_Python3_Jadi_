def get_ages():
    age = input('Please enter the age of members : ')
    return age


def input_type_recognizer(Input):
    try:
        testing = int(Input)
        return str(Input)
    except ValueError:
        try:
            testing = float(Input)
            print_results('float', Input)
            main_program(10)
        except ValueError:
            print_results('not_number', Input)
            main_program(10)
    print(Input)
    input_type_recognizer(main_program(10))

def input_condition_checker(age):
    age = int(age)
    if ((age < 10) or (age > 90)) and (age != -1):
        print_results('input_failed', 'just_a_word')
        main_program(10)
    else:
        return age
    return age


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


def oldest_member_checker(main_age, oldest, youngest):
    if main_age >= oldest:
        oldest = main_age
        youngest = youngest_member_checker(youngest, main_age)
        main_program(youngest)
        return oldest, youngest
    else:
        return main_age, oldest


def youngest_member_checker(age, youngest):
    if age <= youngest:
        youngest = age
        return youngest
    else:
        age = main_program(10)
        return age


def main_program(main_age):
    oldest = 10
    youngest = 90
    while (main_age != -1):
        main_age = get_ages()
        age = input_type_recognizer(main_age)
        age = input_condition_checker(main_age)
        oldest, youngest = oldest_member_checker(main_age, oldest, youngest)
        return oldest, youngest
    print(oldest, youngest)


oldest, youngest = main_program(10)
print_results('old', oldest)
print_results('young', youngest)
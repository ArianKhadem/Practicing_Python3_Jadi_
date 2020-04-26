def get_strings():
    string = input('Please enter the strings: ')
    return string


def input_condition_checker(string_for_check):
    old_string = '.'
    for letter in string_for_check:
        if (letter == 'e') or (letter == 'a') or (letter == 'i') or (letter == 'o') or (letter == 'u'):
            new_string = '.'
        else:
            letter = '.' + letter + old_string
            old_string = letter
    return letter


def main_program():
    print(input_condition_checker(get_strings()))

    
main_program()

def get_name():
    input_names = input('Please enter the names: ')
    return input_names


def input_condition_checker():
    name = get_name()
    say_hello = ''
    for character in name:
        if (character == 'h'):
            say_hello = say_hello + character
        elif (character == 'e'):
            say_hello = say_hello + character
        elif (character == 'l'):
            say_hello = say_hello + character 
        elif (character == 'L'):
             say_hello = say_hello + character
        elif (character == 'o'):
            say_hello = say_hello + character
        if (say_hello == 'hello'):
            return 'Yes'
    return 'No'

def main_program():
    print(input_condition_checker())


main_program()
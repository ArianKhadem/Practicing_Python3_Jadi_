def get_name():
    input_names = input('Please enter the names: ')
    return input_names


def input_condition_checker():
    name = get_name()
    lower_counter = 0
    upper_counter = 0
    crawler_digit = 0
    for character in name:
        if (character == name[crawler_digit].lower()):
            lower_counter = lower_counter + 1
            crawler_digit = crawler_digit + 1
        elif (character == name[crawler_digit].upper()):
            upper_counter = upper_counter + 1
            crawler_digit = crawler_digit + 1
    if lower_counter > upper_counter:
        print(name.lower())
    elif lower_counter < upper_counter:
        print(name.upper())
    else:
        Divid_2 = int((len(name)//2))
        print(name[:Divid_2].lower()+name[Divid_2:].upper())


def main_program():
    input_condition_checker()


main_program()
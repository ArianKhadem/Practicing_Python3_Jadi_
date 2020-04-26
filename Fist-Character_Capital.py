def get_name():
    input_names = input('Please enter the names: ')
    return input_names


def input_condition_checker():
    for i in range(0, 11):
        name = get_name().lower()
        first_ch = name[0]
        correct_name = first_ch.upper() + name[1:]
        print(correct_name)


def main_program():
    input_condition_checker()


main_program()
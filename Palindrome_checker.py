def get_name():
    input_names = input('Please enter the names: ')
    return input_names


def input_condition_checker():
    name = get_name()
    inverse = ''
    crawler_digit = -1
    for character in name:
        if character == name[crawler_digit]:
            inverse = inverse + character
        crawler_digit = crawler_digit - 1
    if inverse == name:
        return 'Palindrome' 
    return 'Not palindrome'


def check_palindrom(str): 
    i = 0
    j = len(str) - 1
    while(i <= j): 
        if str[i] != str[j]: 
            return False
        i = i + 1
        j = j - 1
    return True


def main_program():
    print(input_condition_checker())
    print(check_palindrom(get_name()))


main_program()     
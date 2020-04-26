def get_data():
    input_number_of_laptops = int(input('Please enter the number of laptops: '))
    input_price_quality = []
    for counter in range(input_number_of_laptops):
        input_price_quality.append(input('Please enter the price and quality(put space between them): '))
    return input_number_of_laptops, input_price_quality


def input_condition_checker(string):
    result, counter = input_checker_AB_or_BA(string, 'a', 'b', 0)
    if (result == 'Yes'):
        if (input_checker_AB_or_BA(string, 'b', 'a', counter) == 'Yes', counter):
            return 'Yes'
    elif (input_checker_AB_or_BA(string, 'b', 'a',counter) == 'Yes', counter):
        if (input_checker_AB_or_BA(string, 'a', 'b',counter) == 'Yes', counter):
            return 'Yes'
    return 'No'


def input_checker_AB_or_BA(string, check_AorB, check_BorA, counter):
    if len(string) >= 4:
        for counter in range(counter, len(string)):
            if (string[counter] == check_AorB) and (string[counter + 1] == check_BorA):
                return 'Yes', counter
    return 'No', counter


def main_program():
    string = get_data()
    # print(input_condition_checker(string))


main_program()
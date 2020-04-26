def get_input():
    input_distances = input('Please enter the distances between your homes: ')
    input_distances = input_distances.split()
    return input_distances


def input_condition_checker(distances):
    distances = char_to_number_converter(distances)
    distances.sort()
    middle_number = distances[int(len(distances)//2)]
    return max(distances), middle_number, min(distances)


def meeting_distance_calculator(max, mid, small):
    result = (max-mid)+(mid-small)
    return result


def char_to_number_converter(list):
    
    for digit in range(0, len(list)):
        poped = int(list.pop(0))
        list.append(poped)
    return list


def main_program():
    max, mid, small = input_condition_checker(get_input())
    print('This is the bigger: ',max)
    print('This is the Middle: ', mid)
    print('This is the smaller:', small)
    print('This is the lowest route that possible:',meeting_distance_calculator(max, mid, small))
    

main_program()
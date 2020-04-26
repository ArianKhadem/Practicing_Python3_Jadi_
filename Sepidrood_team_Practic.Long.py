def The_Number_of_Matches() :
    number_of_Matches = int(input('Please enter the number of Matches: '))
    Recognize_input_character(number_of_Matches, 'Number')
    return number_of_Matches
def Recognize_input_character(characters, check) :
    if check == 'get' :
        if (characters != 0) and (characters != 1) and (characters != 3):
            Print_results('input_failed', 'just_a_word')
            get_score()
        else:    
            return int(characters)
    elif check == 'Number' :
        Type = type(characters)
        if Type != int:
            Print_results('number_matches', 'just_a_word')
            The_Number_of_Matches()
        else:
            return int(characters)
def get_score () :
    score = int(input('Please enter the scores : '))
    Recognize_input_character(score, 'get')
    return int(score)
def sum_total_score (score, temp) :
    score = The_Number_of_Matches()
    if (score != 0) or (score == 3) or (score == 1) :
        print(score, temp)
        total_score = score + temp
        temp = total_score
        return total_score
def Calculate_results (score) :
    if type(score) == int:
        if score == 0 :
            return 1, 'loose'
        elif score == 1 :
            return 1, 'equal'
        elif score == 3 :
            return 1, 'win'
def Print_results(text, results) :
    if text == 'loose' :
        print('The Sepidrood has',results,'LOOSE in this league! ' )
    elif text == 'equal' :
        print('The Sepidrood has',results,'EQUAL in this league! ' )
    elif text == 'win' :
        print('The Sepidrood has',results,'WIN in this league! ' )
    elif text == 'total_score' :
        print('The total score of Sepidrood in this league is :',results)
    elif text == 'input_failed' :
        print('Please just input the result of match')
        print('"0" for loose')
        print('"1" for equal')
        print('"3" for win: ')
    elif text == 'number_matches' :
        print('Please just type the numbers of Sepidrood matches in the league!')
def Main_Program() :
    score = 0
    temp = 0
    loose = 0
    win = 0
    equal = 0
    Counter = int(The_Number_of_Matches())
    for i in range(Counter) :
        score = get_score()
        total_score = temp + score
        temp = total_score
        calc_result, text_result = Calculate_results(score)
        if i == Counter-1 :
            Print_results('total_score', total_score)
        if (text_result == 'loose') :
            loose = loose + calc_result
        elif text_result == 'equal' :
            equal = equal + calc_result
        elif text_result == 'win' :
            win = win + calc_result
        if i == Counter-1 :
            Print_results('win', win)
        if i == Counter-1 :
            Print_results('equal', equal)
        if i == Counter-1 :
            Print_results ('loose', loose)

Main_Program()
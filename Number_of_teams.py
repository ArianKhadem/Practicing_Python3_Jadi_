def get_input():
    input_players_number = int(input('Please enter the number of players: '))
    input_game_played = input('Please enter the number of games that players, played till now: ')
    input_game_played = input_game_played.split()
    return input_players_number, input_game_played


def input_condition_checker():
    plyers_number, game_played = get_input()
    for digit in range(0, len(game_played)):
        temp = int(game_played.pop(0))
        if temp <= 2:
            game_played.append(temp)
    # count_zero = game_played.count(0)
    # count_one = game_played.count(1)
    # count_two = game_played.count(2)
    # game_played.sort()
    answer = (len(game_played)//3)
    return answer
    # # for i in range(0, count_zero):
    # #     index_0 = game_played.index(0)
    # #     if 0 in team_1 == False:
    # #         team_1 = [game_played.pop(index_0)]
    # #     elif 0 in team_2 == False:
    # #         team_2 = [game_played.pop(index_0)]
    # #     elif 0 in team_3 == False:
    # #         team_3 = [game_played.pop(index_0)]
    # #     for j in range(0, count_one):
    # #         index_1 = game_played.index(1)
    # #         team_1.append(game_played.pop(index_1))
    # #         for k in range(0, count_two):
    # #             index_2 = game_played.index(2)
    # #             team_1.append(game_played.pop(index_2))
    #     team_2 = [game_played.pop(index_0)]
    #     team_3 = [game_played.pop(index_0)]


def main_program():
    print(input_condition_checker())


main_program()
player_one = []
player_two = []
board_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
winning = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
is_winner = False
player_tour = 1

def print_board():
    print(' '+str(board_values[0])+' | '+str(board_values[1])+' | '+str(board_values[2])+' \n-----------\n '
          +str(board_values[3])+' | '+str(board_values[4])+' | '+str(board_values[5])+' \n-----------\n '
          +str(board_values[6])+' | '+str(board_values[7])+' | '+str(board_values[8])+' ')

one_name = input('Player one name is? ')
two_name = input('Player two name is? ')

while is_winner is False:
    print_board()

    if player_tour == 1:
        field = int(input('%s its your move! which field you choose? ' % one_name))
        if field not in player_one and field not in player_two:
            player_one.append(field)
            ind = board_values.index(field)
            board_values.remove(field)
            board_values.insert(ind, 'X')
            for value in winning:
                if value == sorted(player_one):
                    is_winner = True

            player_tour = 2
        else:
            print('This field is already taken, choose another!')

    elif player_tour == 2:
        field = int(input('%s its your move! which field you choose? ' % two_name))
        if field not in player_one and field not in player_two:
            player_two.append(field)
            ind = board_values.index(field)
            board_values.remove(field)
            board_values.insert(ind, 'O')
            for value in winning:
                if value == sorted(player_two):
                    is_winner = True

            player_tour = 1
        else:
            print('This field is already taken, choose another!')

    if is_winner is True:
        print_board()
        if player_tour == 1:
            print('And the winner is: %s!!!' % two_name)
        elif player_tour == 2:
            print('And the winner is: %s!!!' % one_name)

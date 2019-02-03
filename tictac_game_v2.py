fields = [[], []]
marks = [' ']*9
rounds = 0
winner = 0
board = 0
player = 0


def print_board():
    print(' ' + marks[0] + ' | ' + marks[1] + ' | ' + marks[2] + '           1 | 2 | 3')
    print('-'*11 + '         ' + '-'*11)
    print(' ' + marks[3] + ' | ' + marks[4] + ' | ' + marks[5] + '           4 | 5 | 6')
    print('-'*11 + '         ' + '-'*11)
    print(' ' + marks[6] + ' | ' + marks[7] + ' | ' + marks[8] + '           7 | 8 | 9')


def find_winner(player_num):
    winner_is = 0
    if player_num == 1:
        mark = 'X'
    else:
        mark = 'O'

    if ((marks[0] == mark and marks[1] == mark and marks[2] == mark) or
        (marks[3] == mark and marks[4] == mark and marks[5] == mark) or
        (marks[6] == mark and marks[7] == mark and marks[8] == mark) or
        (marks[0] == mark and marks[3] == mark and marks[6] == mark) or
        (marks[1] == mark and marks[4] == mark and marks[7] == mark) or
        (marks[2] == mark and marks[5] == mark and marks[8] == mark) or
        (marks[0] == mark and marks[4] == mark and marks[8] == mark) or
        (marks[2] == mark and marks[4] == mark and marks[6] == mark)):
        winner_is = player_num
        print('WOW! player %i won!' % player_num)

    return winner_is


def full_board():
    board_full = 0
    if sorted(fields[0]+fields[1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print('Board is full! End of the game! There is no winner')
        board_full = 1
    return board_full


print('This is Tic Tac Toe Game! Welcome :)')
print('Pass first player name: ')
name1 = input()
print('Hello %s as first player you have X' % name1)
print('Pass second player name: ')
name2 = input()
print('Hello %s as second player you have O' % name2)
print_board()

while winner == 0 and board == 0:
    if rounds % 2 == 0:
        player = 1
        name = name1
    else:
        player = 2
        name = name2

    print('Player %s round! Pass a field number!' % name)
    field_num = int(input())
    if field_num > 9:
        print('Num out of range! Try one more time!')
    elif marks[field_num-1] != ' ':
        print('No! This field is already taken! Choose another one!')
    else:
        fields[player-1].append(field_num)
        if player == 1:
            marks[field_num-1] = 'X'
        else:
            marks[field_num-1] = 'O'

        winner = find_winner(player)
        board = full_board()
        rounds += 1

    print_board()




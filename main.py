
board = [' ' for x in range(10)]


def insert_letter(letter, position):
    board[position] = letter


def space_is_free(position):
    return board[position] == ' '


def print_board(board):
    print('   |    |')
    print(' ' + board[1] + ' | ' + board[2] + '  | ' + board[3])
    print('   |    |')
    print('------------')
    print('   |    |')
    print(' ' + board[4] + ' | ' + board[5] + '  | ' + board[6])
    print('   |    |')
    print('------------')
    print('   |    |')
    print(' ' + board[7] + ' | ' + board[8] + '  | ' + board[9])
    print('   |    |')


def is_winner(bo, le):
    return


def player_move():
    pass


def comp_move():
    pass


def select_random(board):
    pass


def is_bord_full(board):
    pass


def main():
    pass

main()

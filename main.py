
board = [' ' for x in range(10)]


def insert_letter(letter, position):
    """
    insert  X or O in free position in board
    :param letter: x or O
    :param position:  form 1 to 9
    :return: None
    """
    board[position] = letter


def space_is_free(position):
    """
    This function checks Is this position is empty or not ?
    :param position: from 1 to 9
    :return: position
    """
    return board[position] == ' '


def print_board(board):
    """
    Just draw board of game
    """
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
    """
    :param bo:
    :param le:
    :return:
    """
    pass


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

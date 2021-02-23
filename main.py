
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
    # write function with for
    # with for:
    # for row in bo:
    #     if bo[row] == le:
    #         print("Win")
    #         # for diagonals
    #     for col in bo:
    #         if row == col:
    #             if bo[row][col] == le:
    #                 print("win")

    # FIX
    # Given a board and a player’s letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don’t have to type as much.

    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal


# def emty_position():
#     emply_position_list = [1, 2, 5]
#     return emply_position_list


def player_move():
    # This function checks for nums which enter player
    run = True
    while run:
        move = input("Select a position (1-9): ")
        # empty_p = emty_position()

        # make sure that move = int(move)
        try:
            move = int(move)
            if move > 0 and move < 10:
                if space_is_free(move):
                    run = False
                    # and insert X in the position(move)
                    insert_letter('X', move)
                # но если это место уже занято то выведи ошибку вставления елемента
                else:
                    print("We can't insert element in this position ")
                    print("Sorry, this space is occupaid !")
            else:
                print("Please enter only num from 1 to 9")

        except:
            print("Please type a number !")




def comp_move():
    pass


def select_random(board):
    pass


def is_bord_full(board):
    """
    this function checks if there are empty spaces
    :return: True if have have empty position
    """
    if board.count(' ') > 1:
        return True
    else:
        return False


def main():
    print("Tic Tac Toe game")
    print_board(board)
    while not is_bord_full(board):
        # for winning of o (here is playing a player)
        if not is_winner(board, 'o'):
            player_move()
            print_board(board)
        else:
            print("O\'s won this time !")
            break

        # for winning of X (here is playing a computer )
        if not is_winner(board, 'X'):
            comp_move()
            print_board(board)
        else:
            print("X\'s won this time !")
            break

    if is_bord_full(board):
        print("Stop")


main()

board = [" " for i in range(9)]


def print_board():
    row1 = "|{}|{}|{}|".format(board[0], board[1], board[2])
    row2 = "|{}|{}|{}|".format(board[3], board[4], board[5])
    row3 = "|{}|{}|{}|".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()


def is_victory(symbol):
    global game
    w_combo = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6},
               {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {2, 4, 6}]
    current_moves = set([i for i, x in enumerate(board) if x == symbol])
    for w in w_combo:
        if(current_moves.issuperset(w)):
            game = False


print_board()
symbol = 'X'
moves = []
game = True

while game:
    print('Enter your move player {} (1-9)'.format(symbol))
    choice = int(input('------->').strip()) - 1
    if(not choice in moves):
        board[choice] = symbol
        moves.append(choice)
    else:
        print('Move already played')
        continue
    is_victory(symbol)
    if(not game):
        print('='*20)
        print(symbol + ' you have won!')
        print('='*20)
    if(symbol == 'X'):
        symbol = 'O'
    else:
        symbol = 'X'
    if(len(moves) > 8):
        game = False
        print('='*20)
        print('Game is a draw!')
        print('='*20)
    print_board()

row1 = ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜']
row2 = ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟']
row3 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
row4 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
row5 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
row6 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
row7 = ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙']
row8 = ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']

board = [row1, row2, row3, row4, row5, row6, row7, row8]


def insert():
    coords = input('\ngive me chessboard coordinates (e.g. B6): ').casefold()

    y = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'].index(coords[0])
    x = int(coords[1])-1

    board[x][y] = input('what would you like to put here? ')
    print(f'\n{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n')
    
    if input('another? y/n: ') == 'y': insert()


insert()

# get row/col from position
# - pos: position. e.g., a1, d2
# - return value (tuple)
#   - row, col (both zero based index)
def pos2rc(pos):
    row = None
    col = None
    if (ord('a') <= ord(pos[0]) <= ord('h')):
        if (ord('1') <= ord(pos[1]) <= ord('8')):
            col = ord(pos[0]) - ord('a')
            row = ord(pos[1]) - ord('1')
    return row, col

class EChess():
    def __init__(self):
        # board starts with row 1 to row 8
        self.board = [
            # row 1: a -> h
            # Naming convension: wR white Rook, bK black King, etc.
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
            # row 2
            ['wP', 'wP', 'wp', 'wP', 'wP', 'wP', 'wP', 'wP'],
            # row 3
            ['', '', '', '', '', '', '', ''],
            # row 4
            ['', '', '', '', '', '', '', ''],
            # row 5
            ['', '', '', '', '', '', '', ''],
            # row 6
            ['', '', '', '', '', '', '', ''],
            # row 7
            ['bP', 'bP', 'bp', 'bP', 'bP', 'bP', 'bP', 'bP'],
            # row 3
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR']]

    def print(self):
        # print heading
        print('    a  b  c  d  e  f  g  h')

        for row in reversed(range(8)):
            print(row+1, ':', end=' ') # print row num
            for col in range(8):
                if (self.board[row][col] == ''):
                    print('  ', end=' ')
                else:
                    print(self.board[row][col], end=' ')
            print()

    # move a piece
    # - sp: start position. e.g., a1, d2
    # - ep:   end position.
    def move(self, sp, ep):
        srow, scol = pos2rc(sp) # start row/col
        if (srow == None or scol == None):
            print('Error: Invalid start position')
            return False
        if (self.board[srow][scol] == ''):
            print('Error: No piece in start position')
            return False

        erow, ecol = pos2rc(ep) # end row/col
        if (erow == None or ecol == None):
            print('Error: Invalid end position')
            return False
        if (self.board[erow][ecol] == ''):
            self.board[erow][ecol] = self.board[srow][scol];
            self.board[srow][scol] = ''
        else:
            if (self.board[srow][scol][0] == self.board[erow][ecol][0]):
                print('Error: End position already has same colored piece')
                return False
            else:
                self.board[erow][ecol] = self.board[srow][scol];
                self.board[srow][scol] = ''

        return True

# test code
chess = EChess()
chess.print()

chess.move('e2', 'e4')
chess.print()

chess.move('e2', 'd1')
chess.print()

chess.move('e4', 'd1')
chess.print()

chess.move('h2', 'h7')
chess.print()


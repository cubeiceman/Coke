import pygame
pygame.init()


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

def rc2pos(r, c):
    pos = ''
    pos += chr(ord('a') + c)
    pos += chr(ord("1") + r)
    return pos

def coord2rc(x, y, square_width, square_height):
    r = 7 - int(y / square_height)
    c = int(x / square_width)
    return r, c

def get_image(piece):
    image = pygame.image.load(".\\" + piece + ".png")
    return image

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

    def check_square(self, pos):
        row, col = pos2rc(pos)
        return self.board[row][col]

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



WIDTH, HEIGHT = 800, 800
surface = pygame.display.set_mode([WIDTH, HEIGHT])
WHITE = (255, 255, 255)



class Board:
    def __init__(self, width, height, surface):
        self.surface = surface
        self.width = width
        self.height = height

        self.square_width = self.width / 8
        self.square_height = self.height / 8
        
        self.square_color = [[0,1,0,1,0,1,0,1],
                             [1,0,1,0,1,0,1,0],
                             [0,1,0,1,0,1,0,1],
                             [1,0,1,0,1,0,1,0],
                             [0,1,0,1,0,1,0,1],
                             [1,0,1,0,1,0,1,0],
                             [0,1,0,1,0,1,0,1],
                             [1,0,1,0,1,0,1,0]]

        self.font = pygame.font.Font("freesansbold.ttf", 20)
        self.echess = EChess()

        self.start_pos = None


    def handle_click(self, x, y):
        r, c = coord2rc(x, y, self.square_width, self.square_height)
        pos = rc2pos(r, c)
        if self.start_pos == None:
            self.start_pos = pos
        else:
            self.echess.move(self.start_pos, pos)
            self.start_pos = None


    def draw(self):
        # Draw the board itself
        for row in range(8):
            for col in range(8):
                top_x = col * self.square_width
                top_y = HEIGHT - ((row+1) * self.square_height)
                if self.square_color[row][col] == 0:
                    color = (100,100,100) # black
                else:
                    color = (200,200,200) # white
                pygame.draw.rect(self.surface, color, pygame.Rect(top_x, top_y, self.square_width, self.square_height))
                if self.start_pos != None:
                    if pos2rc(self.start_pos) == (row, col):
                        pygame.draw.rect(self.surface, (200, 200, 0), pygame.Rect(top_x, top_y, self.square_width, self.square_height))

                
                
                piece = self.echess.check_square(rc2pos(row, col))
                if piece != "":
                    self.surface.blit(get_image(piece), (top_x, top_y))
                #text = self.font.render(piece, True, (200, 0, 0))
                #self.surface.blit(text, (top_x, top_y))


        pygame.display.flip()

board = Board(WIDTH, HEIGHT, surface)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            board.handle_click(mx, my)
    board.draw()

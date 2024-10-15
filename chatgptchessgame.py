class Piece:
    def __init__(self, color):
        self.color = color
        self.symbol = ' '

    def valid_moves(self, board, start_pos):
        return []

    def __repr__(self):
        return self.symbol


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'P' if color == 'white' else 'p'

    def valid_moves(self, board, start_pos):
        # Simplified move logic for pawn
        direction = 1 if self.color == 'white' else -1
        moves = []
        start_row, start_col = start_pos
        next_pos = (start_row + direction, start_col)
        if board.is_empty(next_pos):
            moves.append(next_pos)
        return moves


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'R' if color == 'white' else 'r'


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'N' if color == 'white' else 'n'


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'B' if color == 'white' else 'b'


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'Q' if color == 'white' else 'q'


class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'K' if color == 'white' else 'k'


class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_board()

    def setup_board(self):
        # Setup pawns
        for i in range(8):
            self.board[1][i] = Pawn('white')
            self.board[6][i] = Pawn('black')

        # Setup rooks
        self.board[0][0] = self.board[0][7] = Rook('white')
        self.board[7][0] = self.board[7][7] = Rook('black')

        # Setup knights
        self.board[0][1] = self.board[0][6] = Knight('white')
        self.board[7][1] = self.board[7][6] = Knight('black')

        # Setup bishops
        self.board[0][2] = self.board[0][5] = Bishop('white')
        self.board[7][2] = self.board[7][5] = Bishop('black')

        # Setup queens
        self.board[0][3] = Queen('white')
        self.board[7][3] = Queen('black')

        # Setup kings
        self.board[0][4] = King('white')
        self.board[7][4] = King('black')

    def is_empty(self, position):
        row, col = position
        return self.board[row][col] is None

    def move_piece(self, start_pos, end_pos):
        piece = self.get_piece(start_pos)
        if piece and end_pos in piece.valid_moves(self, start_pos):
            self.set_piece(end_pos, piece)
            self.set_piece(start_pos, None)

    def get_piece(self, position):
        row, col = position
        return self.board[row][col]

    def set_piece(self, position, piece):
        row, col = position
        self.board[row][col] = piece

    def display(self):
        for row in self.board:
            print(' '.join([str(piece) if piece else '.' for piece in row]))
        print()


class Game:
    def __init__(self):
        self.board = Board()
        self.current_turn = 'white'

    def switch_turn(self):
        self.current_turn = 'black' if self.current_turn == 'white' else 'white'

    def play(self):
        while True:
            self.board.display()
            print(f"{self.current_turn}'s turn")
            start = input("Enter start position (e.g., 1 0 for a pawn): ")
            end = input("Enter end position (e.g., 2 0 to move forward): ")
            start_pos = tuple(map(int, start.split()))
            end_pos = tuple(map(int, end.split()))

            piece = self.board.get_piece(start_pos)
            if piece and piece.color == self.current_turn:
                self.board.move_piece(start_pos, end_pos)
                self.switch_turn()
            else:
                print("Invalid move, try again.")
play = Game()
play.play()

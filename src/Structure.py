from enum import Enum

class Colors(Enum):
    WHITE = "white"
    BLACK = "black"

class Pieces(Enum):
    PAWN = "Pawn"
    ROOK = "Rook"
    KNIGHT = "Knight"
    BISHOP = "Bishop"
    QUEEN = "Queen"
    KING = "King"

class ChessPiece:
    def __init__(self, piece: Pieces, color: Colors):
        self.piece = piece
        self.color = color

class ChessCell:
    def __init__(self, color: Colors, piece=None):
        self.color: Colors = color
        self.piece: ChessPiece = piece


class ChessBoard:
    def __init__(self):
        self.board = [[ChessCell(self._get_cell_color(i, j)) for i in range(8)] for j in range(8)]

    def _get_cell_color(self, col, row):
        return Colors.WHITE if (col+row) % 2 else Colors.BLACK


    def setup_initial_position(self):
        # Pawns
        for i in range(8):
            self.board[1][i].piece = ChessPiece(Pieces.PAWN, Colors.WHITE)
            self.board[6][i].piece = ChessPiece(Pieces.PAWN, Colors.BLACK)
        
        # Rooks
        self.board[0][0].piece = ChessPiece(Pieces.ROOK, Colors.WHITE)
        self.board[0][7].piece = ChessPiece(Pieces.ROOK, Colors.WHITE)
        self.board[7][0].piece = ChessPiece(Pieces.ROOK, Colors.BLACK)
        self.board[7][7].piece = ChessPiece(Pieces.ROOK, Colors.BLACK)

        # Knights
        self.board[0][1].piece = ChessPiece(Pieces.KNIGHT, Colors.WHITE)
        self.board[0][6].piece = ChessPiece(Pieces.KNIGHT, Colors.WHITE)
        self.board[7][1].piece = ChessPiece(Pieces.KNIGHT, Colors.BLACK)
        self.board[7][6].piece = ChessPiece(Pieces.KNIGHT, Colors.BLACK)

        # Bishops
        self.board[0][2].piece = ChessPiece(Pieces.BISHOP, Colors.WHITE)
        self.board[0][5].piece = ChessPiece(Pieces.BISHOP, Colors.WHITE)
        self.board[7][2].piece = ChessPiece(Pieces.BISHOP, Colors.BLACK)
        self.board[7][5].piece = ChessPiece(Pieces.BISHOP, Colors.BLACK)

        # Kings and Queens
        self.board[0][3].piece = ChessPiece(Pieces.QUEEN, Colors.WHITE)
        self.board[0][4].piece = ChessPiece(Pieces.KING, Colors.WHITE)
        self.board[7][3].piece = ChessPiece(Pieces.QUEEN, Colors.BLACK)
        self.board[7][4].piece = ChessPiece(Pieces.KING, Colors.BLACK)

    def move_piece(self, from_position, to_position):
        # Implement logic for moving chess pieces
        print("TODO")

    def is_valid_move(self, piece, from_position, to_position):
        # Check if a move is valid
        print("TODO")

    def is_checkmate(self, color):
        # Check for checkmate condition
        print("TODO")

    # Other methods for game logic and board management

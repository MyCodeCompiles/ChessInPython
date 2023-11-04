from enum import Enum

class Colors(Enum):
    WHITE = "white"
    BLACK = "black"

class Pieces(Enum):
    PAWN = "pawn"
    ROOK = "rook"
    KNIGHT = "knight"
    BISHOP = "bishop"
    QUEEN = "queen"
    KING = "king"

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
            self.board[i][1].piece = ChessPiece(Pieces.PAWN, Colors.WHITE)
            self.board[i][6].piece = ChessPiece(Pieces.PAWN, Colors.BLACK)
        
        # Rooks
        self.board[0][0].piece = ChessPiece(Pieces.ROOK, Colors.WHITE)
        self.board[7][0].piece = ChessPiece(Pieces.ROOK, Colors.WHITE)
        self.board[0][7].piece = ChessPiece(Pieces.ROOK, Colors.BLACK)
        self.board[7][7].piece = ChessPiece(Pieces.ROOK, Colors.BLACK)

        # Knights
        self.board[1][0].piece = ChessPiece(Pieces.KNIGHT, Colors.WHITE)
        self.board[6][0].piece = ChessPiece(Pieces.KNIGHT, Colors.WHITE)
        self.board[1][7].piece = ChessPiece(Pieces.KNIGHT, Colors.BLACK)
        self.board[6][7].piece = ChessPiece(Pieces.KNIGHT, Colors.BLACK)

        # Bishops
        self.board[2][0].piece = ChessPiece(Pieces.BISHOP, Colors.WHITE)
        self.board[5][0].piece = ChessPiece(Pieces.BISHOP, Colors.WHITE)
        self.board[2][7].piece = ChessPiece(Pieces.BISHOP, Colors.BLACK)
        self.board[5][7].piece = ChessPiece(Pieces.BISHOP, Colors.BLACK)

        # Kings and Queens
        self.board[3][0].piece = ChessPiece(Pieces.QUEEN, Colors.WHITE)
        self.board[4][0].piece = ChessPiece(Pieces.KING, Colors.WHITE)
        self.board[3][7].piece = ChessPiece(Pieces.QUEEN, Colors.BLACK)
        self.board[4][7].piece = ChessPiece(Pieces.KING, Colors.BLACK)

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

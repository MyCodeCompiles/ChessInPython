from Structure import *
from Structure import Colors
import pygame
from enum import Enum

# Define Colors enum and ChessBoard class (as in your previous code)

# Initialize pygame
def start_game():
    pygame.init()
    game = ChessBoard()
    game.setup_initial_position()
    game_loop(game)

# Main game loop
def game_loop(game: ChessBoard):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw the chessboard
        draw_board(game)
        pygame.display.flip()

    pygame.quit()



# Constants
SCREEN_WIDTH = 600  # Adjust as needed
SCREEN_HEIGHT = 600  # Adjust as needed
SQUARE_SIZE = SCREEN_WIDTH // 8

# Create a window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chess")

# Color mapping
COLOR_MAP = {
    Colors.WHITE: (220, 192, 139),
    Colors.BLACK: (139, 69, 19),
}

def draw_board(game: ChessBoard):
    for row in range(7, -1, -1):
        for col in range(8):
            color = COLOR_MAP[game.board[col][row].color]
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            if game.board[col][row].piece != None:
                piece_x = col * SQUARE_SIZE
                piece_y = row * SQUARE_SIZE
                screen.blit(get_piece_image(game.board[col][row].piece), (piece_x, piece_y))

def get_piece_image(piece: ChessPiece):
    image_name = "images/" + get_image_name(piece)
    return pygame.transform.scale(pygame.image.load(image_name), (SQUARE_SIZE, SQUARE_SIZE))

def get_image_name(piece: ChessPiece):
    return piece.color.value + "_" + piece.piece.value + ".png"
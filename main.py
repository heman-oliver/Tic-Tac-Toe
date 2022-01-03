# IMPORTS
import pygame
import random
from board import Board

pygame.init()

# SCREEN
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900

# RGB
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# SCREEN
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Tic Tac Toe")

# FUNCS
def make_turn(player_1, player_2):
    turn = random.randint(0, 1)
    if turn == 0:
        return player_1
    return player_2

def change_turn(turn, player_1, player_2):
    if turn == player_1:
        return player_2
    else:
        return player_1

board = Board()
board.create_boxes()

markers = ("X", "O")
player_1 = markers[0]
player_2 = markers[1]

turn = make_turn(player_1, player_2)

if turn == player_1:
    print("Player 1 to start")
else:
    print("Player 2 to start")

# CLOCK
clock = pygame.time.Clock()

# GAME LOOP
run = True
gameOver = False
while not(gameOver):

    clock.tick(30)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = list(pygame.mouse.get_pos())
            if board.isCollided(mouse_pos, turn):
                print("Clicked")
                if turn == player_1:
                    turn = player_2
                else:
                    turn = player_1
            if board.win_check_1(board.board):
                print("Player 1 has won the game")
                gameOver = True
            elif board.win_check_2(board.board):
                print("Player 2 has won the game")
                gameOver = True
            elif board.game_over():
                print("GAME OVER")
                gameOver = True
            
    board.draw(screen, BLACK)
    board.draw_gamestate(screen)

    pygame.display.flip()

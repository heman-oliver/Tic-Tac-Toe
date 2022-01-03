import pygame

class Board(object):
    def __init__(self):
        self.screen_width = 900
        self.screen_height = 900
        self.boxes = []
        self.board = [
            ["--", "--", "--"],
            ["--", "--", "--"],
            ["--", "--", "--"]
        ]
        self.image_X = pygame.image.load("X.png")
        self.image_O = pygame.image.load("O.png")
        self.font = pygame.font.Font("freesansbold.ttf", 64)
        self.block_size = self.screen_width // 3

    def print_board(self):
        print(self.board[0])
        print(self.board[1])
        print(self.board[2])

    def draw(self, screen, color):
        block_size = self.screen_width // 3
        for x in range(0, self.screen_width, block_size):
            for y in range(0, self.screen_height, block_size):
                rect = pygame.Rect(x, y, block_size, block_size)
                pygame.draw.rect(screen, color, rect, 15)

    # CREATES BOXES
    def create_boxes(self):
        block_size = self.screen_width // 3
        for x in range(0, self.screen_width, block_size):
            for y in range(0, self.screen_height, block_size):
                rect = pygame.Rect(x, y, block_size, block_size)
                self.boxes.append(rect)

    # UPDATES THE GAME STATE
    def draw_gamestate(self, screen):
        for x, a in enumerate(self.board):
            for y, b in enumerate(a):
                if b == "X":
                    screen.blit(self.image_X, (y * self.block_size + self.block_size // 2 - 50, x * self.block_size + self.block_size // 2 - 50))
                if b == "O":
                    screen.blit(self.image_O, (y * self.block_size + self.block_size // 2 - 50, x * self.block_size + self.block_size // 2 - 50))

    # CHECKS IF ANY PLAYER HAS WON THE GAME
    @staticmethod
    def win_check_1(board):
        return (
            # HORIZONTAL
            (board[0][0] == board[0][1] == board[0][2] == "X") or
            (board[1][0] == board[1][1] == board[1][2] == "X") or
            (board[2][0] == board[2][1] == board[2][2] == "X") or

            # VERTICAL
            (board[0][0] == board[1][0] == board[2][0] == "X") or
            (board[0][1] == board[1][0] == board[2][0] == "X") or
            (board[0][2] == board[1][1] == board[2][1] == "X") or

            # DIAGNOLS
            (board[0][0] == board[1][1] == board[2][2] == "X") or
            (board[0][2] == board[1][1] == board[2][0] == "X")
        )

    @staticmethod
    def win_check_2(board):
        return (
            # HORIZONTAL
            (board[0][0] == board[0][1] == board[0][2] == "O") or
            (board[1][0] == board[1][1] == board[1][2] == "O") or
            (board[2][0] == board[2][1] == board[2][2] == "O") or

            # VERTICAL
            (board[0][0] == board[1][0] == board[2][0] == "O") or
            (board[0][1] == board[1][0] == board[2][0] == "O") or
            (board[0][2] == board[1][1] == board[2][1] == "O") or

            # DIAGNOLS
            (board[0][0] == board[1][1] == board[2][2] == "O") or
            (board[0][2] == board[1][1] == board[2][0] == "O")
        )
    
    def game_over(self):
        for x in self.board:
            for y in x:
                if y == "--":
                    return False
        else:
            return True

    # PLACES X AND Y INTO THE BOARD
    def place_marker(self, marker, index):
        if index < 3:
            self.board[index][0] = marker
        elif index < 6:
            self.board[index - 3][1] = marker
        else:
            self.board[index - 6][2] = marker
        self.print_board()

    # CHECKS IF THE PLAYER CLICKED THE BOARD
    def isCollided(self, mouse_pos, player):
        for box in self.boxes:
            if box.collidepoint(mouse_pos[0], mouse_pos[1]):
                # print("Collided")
                # print(self.boxes.index(box))
                self.place_marker(player, self.boxes.index(box))
                return True
        else:
            return False

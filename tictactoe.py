import pygame
import sys

def run_tictactoe_game():
    pygame.init()

    WIDTH, HEIGHT = 300, 300
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tic Tac Toe")

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    font = pygame.font.Font(None, 80)

    board = [[None]*3 for _ in range(3)]
    current_player = "X"

    def draw_board():
        screen.fill(WHITE)
        pygame.draw.line(screen, BLACK, (100, 0), (100, 300), 3)
        pygame.draw.line(screen, BLACK, (200, 0), (200, 300), 3)
        pygame.draw.line(screen, BLACK, (0, 100), (300, 100), 3)
        pygame.draw.line(screen, BLACK, (0, 200), (300, 200), 3)

        for y in range(3):
            for x in range(3):
                if board[y][x]:
                    label = font.render(board[y][x], True, RED)
                    screen.blit(label, (x*100 + 30, y*100 + 10))

        pygame.display.flip()

    def check_winner():
        for row in board:
            if row.count(row[0]) == 3 and row[0]:
                return True
        for col in range(3):
            if [board[row][col] for row in range(3)].count(board[0][col]) == 3 and board[0][col]:
                return True
        if [board[i][i] for i in range(3)].count(board[0][0]) == 3 and board[0][0]:
            return True
        if [board[i][2-i] for i in range(3)].count(board[0][2]) == 3 and board[0][2]:
            return True
        return False

    running = True
    while running:
        draw_board()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                x //= 100
                y //= 100
                if not board[y][x]:
                    board[y][x] = current_player
                    if check_winner():
                        running = False
                    current_player = "O" if current_player == "X" else "X"

    pygame.time.delay(1000)  # Oyun bitince bekle

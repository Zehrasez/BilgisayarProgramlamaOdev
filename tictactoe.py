import pygame
import sys

def run_tictactoe_game():
    pygame.init()

    WIDTH, HEIGHT = 500, 500
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tic Tac Toe")

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    font = pygame.font.Font(None, 80)
    small_font = pygame.font.Font(None, 36)

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
                return row[0]
        for col in range(3):
            if [board[row][col] for row in range(3)].count(board[0][col]) == 3 and board[0][col]:
                return board[0][col]
        if [board[i][i] for i in range(3)].count(board[0][0]) == 3 and board[0][0]:
            return board[0][0]
        if [board[i][2-i] for i in range(3)].count(board[0][2]) == 3 and board[0][2]:
            return board[0][2]
        return None

    def is_draw():
        for row in board:
            if None in row:
                return False
        return True

    def show_message(text):
        screen.fill(WHITE)
        msg = font.render(text, True, BLUE)
        screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2 - msg.get_height()//2))
        pygame.display.flip()
        pygame.time.delay(1500)

    def main_menu():
        screen.fill(WHITE)
        title = font.render("Tic Tac Toe", True, BLACK)
        play_text = small_font.render("Oyunu başlatmak için bir tuşa basın", True, BLACK)

        screen.blit(title, (WIDTH//2 - title.get_width()//2, 80))
        screen.blit(play_text, (WIDTH//2 - play_text.get_width()//2, 180))
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False

    while True:
        main_menu()

        board = [[None]*3 for _ in range(3)]
        current_player = "X"
        game_over = False

        while not game_over:
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
                        winner = check_winner()
                        if winner:
                            draw_board()
                            show_message(f"{winner} kazandı!")
                            game_over = True
                        elif is_draw():
                            draw_board()
                            show_message("Berabere!")
                            game_over = True
                        else:
                            current_player = "O" if current_player == "X" else "X"

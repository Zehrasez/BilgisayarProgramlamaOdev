import pygame
import sys
import subprocess

def run_tictactoe_game():
    pygame.init()

    WIDTH, HEIGHT = 300, 360  # 60 px alta buton için
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tic Tac Toe")

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GRAY = (200, 200, 200)

    font = pygame.font.Font(None, 80)
    small_font = pygame.font.Font(None, 30)

    def draw_board():
        screen.fill(WHITE)
        # Grid çizgileri
        pygame.draw.line(screen, BLACK, (100, 0), (100, 300), 3)
        pygame.draw.line(screen, BLACK, (200, 0), (200, 300), 3)
        pygame.draw.line(screen, BLACK, (0, 100), (300, 100), 3)
        pygame.draw.line(screen, BLACK, (0, 200), (300, 200), 3)

        for y in range(3):
            for x in range(3):
                if board[y][x]:
                    label = font.render(board[y][x], True, RED)
                    screen.blit(label, (x * 100 + 30, y * 100 + 10))

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
        if [board[i][2 - i] for i in range(3)].count(board[0][2]) == 3 and board[0][2]:
            return board[0][2]
        return None

    def is_draw():
        for row in board:
            if None in row:
                return False
        return True

    def show_end_screen(message):
        screen.fill(WHITE)

        msg = font.render(message, True, BLUE)
        screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, 80))

        button_rect = pygame.Rect(WIDTH // 2 - 100, 200, 200, 50)
        pygame.draw.rect(screen, GRAY, button_rect)
        button_text = small_font.render("Ana Menüye Dön", True, BLACK)
        screen.blit(button_text, (button_rect.x + 25, button_rect.y + 12))

        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        waiting = False
                        pygame.quit()  # Şu anki pygame penceresini kapat
                        subprocess.run(["python", "main.py"])  # main.py'yi çalıştır

    def main_menu():
        screen.fill(WHITE)
        title = font.render("Tic Tac Toe", True, BLACK)
        play_text = small_font.render("Başlamak için tıkla", True, BLACK)

        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 80))
        screen.blit(play_text, (WIDTH // 2 - play_text.get_width() // 2, 180))
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False

    while True:
        main_menu()

        board = [[None] * 3 for _ in range(3)]
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
                    if y >= 300:  # 300 altına tıklama engeli (buton bölgesi değil)
                        continue
                    x //= 100
                    y //= 100
                    if not board[y][x]:
                        board[y][x] = current_player
                        winner = check_winner()
                        if winner:
                            draw_board()
                            show_end_screen(f"{winner} Kazandı!")
                            game_over = True
                        elif is_draw():
                            draw_board()
                            show_end_screen("Berabere!")
                            game_over = True
                        else:
                            current_player = "O" if current_player == "X" else "X"

import pygame
import sys

def run_tictactoe_game():
    pygame.init()

    WIDTH, HEIGHT = 300, 360  # Alt kısımda düğme için fazladan alan
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tic Tac Toe")

    # Renkler
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (200, 0, 0)
    BLUE = (0, 0, 200)
    GRAY = (220, 220, 220)

    # Yazı tipleri
    font = pygame.font.SysFont(None, 80)
    small_font = pygame.font.SysFont(None, 32)

    def draw_board():
        screen.fill(WHITE)
        # Çizgiler
        pygame.draw.line(screen, BLACK, (100, 0), (100, 300), 4)
        pygame.draw.line(screen, BLACK, (200, 0), (200, 300), 4)
        pygame.draw.line(screen, BLACK, (0, 100), (300, 100), 4)
        pygame.draw.line(screen, BLACK, (0, 200), (300, 200), 4)

        # X ve O'ları çiz
        for row in range(3):
            for col in range(3):
                if board[row][col] == "X":
                    label = font.render("X", True, RED)
                    screen.blit(label, (col * 100 + 25, row * 100 + 10))
                elif board[row][col] == "O":
                    label = font.render("O", True, BLUE)
                    screen.blit(label, (col * 100 + 25, row * 100 + 10))

        pygame.display.flip()

    def check_winner():
        # Satırlar ve sütunlar
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] and board[i][0]:
                return board[i][0]
            if board[0][i] == board[1][i] == board[2][i] and board[0][i]:
                return board[0][i]
        # Çaprazlar
        if board[0][0] == board[1][1] == board[2][2] and board[0][0]:
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] and board[0][2]:
            return board[0][2]
        return None

    def is_draw():
        for row in board:
            if None in row:
                return False
        return True

    def show_end_screen(message):
        screen.fill(WHITE)
        msg = font.render(message, True, BLACK)
        screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, 80))

        # Buton
        button_rect = pygame.Rect(WIDTH // 2 - 80, 200, 160, 50)
        pygame.draw.rect(screen, GRAY, button_rect)
        text = small_font.render("Yeniden Oyna", True, BLACK)
        screen.blit(text, (button_rect.x + 20, button_rect.y + 12))

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

    # Oyun döngüsü
    while True:
        board = [[None for _ in range(3)] for _ in range(3)]
        current_player = "X"
        game_over = False

        while not game_over:
            draw_board()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if y < 300:
                        row = y // 100
                        col = x // 100
                        if board[row][col] is None:
                            board[row][col] = current_player
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

# Oyunu çalıştır
if __name__ == "__main__":
    run_tictactoe_game()

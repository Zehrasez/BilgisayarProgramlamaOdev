import pygame
import random

def run_memory_game():
    pygame.init()

    WIDTH, HEIGHT = 600, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Memory Card Game")

    BG_COLOR = (30, 30, 30)
    CARD_COLOR = (200, 200, 200)
    CARD_BACK_COLOR = (100, 100, 255)
    TEXT_COLOR = (0, 0, 0)

    ROWS, COLS = 4, 4
    CARD_SIZE = WIDTH // COLS
    cards = list(range(1, (ROWS * COLS) // 2 + 1)) * 2
    random.shuffle(cards)
    card_grid = [cards[i * COLS:(i + 1) * COLS] for i in range(ROWS)]
    revealed = [[False] * COLS for _ in range(ROWS)]

    font = pygame.font.SysFont(None, 48)
    clock = pygame.time.Clock()

    first_card = None
    second_card = None
    reveal_time = 0
    matched_pairs = 0

    running = True
    while running:
        screen.fill(BG_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN and not reveal_time:
                x, y = pygame.mouse.get_pos()
                row = y // CARD_SIZE
                col = x // CARD_SIZE
                if not revealed[row][col]:
                    revealed[row][col] = True
                    if not first_card:
                        first_card = (row, col)
                    elif not second_card:
                        second_card = (row, col)
                        if card_grid[first_card[0]][first_card[1]] != card_grid[second_card[0]][second_card[1]]:
                            reveal_time = pygame.time.get_ticks()
                        else:
                            matched_pairs += 1
                            first_card = None
                            second_card = None

        if reveal_time and pygame.time.get_ticks() - reveal_time > 1000:
            revealed[first_card[0]][first_card[1]] = False
            revealed[second_card[0]][second_card[1]] = False
            first_card = None
            second_card = None
            reveal_time = 0

        for i in range(ROWS):
            for j in range(COLS):
                rect = pygame.Rect(j * CARD_SIZE, i * CARD_SIZE, CARD_SIZE - 5, CARD_SIZE - 5)
                if revealed[i][j]:
                    pygame.draw.rect(screen, CARD_COLOR, rect)
                    num_text = font.render(str(card_grid[i][j]), True, TEXT_COLOR)
                    screen.blit(num_text, (j * CARD_SIZE + 30, i * CARD_SIZE + 30))
                else:
                    pygame.draw.rect(screen, CARD_BACK_COLOR, rect)

        if matched_pairs == (ROWS * COLS) // 2:
            win_text = font.render("Kazandınız!", True, (0, 255, 0))
            screen.blit(win_text, (WIDTH // 2 - 100, HEIGHT // 2 - 20))
            pygame.display.flip()
            pygame.time.delay(2000)
            return

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    run_memory_game()

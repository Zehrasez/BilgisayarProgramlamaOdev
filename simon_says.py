import pygame
import random
import sys
import time

def run_simon_says():
    pygame.init()
    WIDTH, HEIGHT = 600, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simon Says")

    COLORS = {
        "red": ((255, 0, 0), pygame.Rect(0, 0, 300, 300)),
        "green": ((0, 255, 0), pygame.Rect(300, 0, 300, 300)),
        "blue": ((0, 0, 255), pygame.Rect(0, 300, 300, 300)),
        "yellow": ((255, 255, 0), pygame.Rect(300, 300, 300, 300))
    }

    SEQUENCE = []
    user_sequence = []
    FPS = 60
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("arial", 40)

    def flash(color_name):
        color, rect = COLORS[color_name]
        bright_color = tuple(min(255, c + 100) for c in color)
        pygame.draw.rect(screen, bright_color, rect)
        pygame.display.flip()
        pygame.time.delay(500)
        pygame.draw.rect(screen, color, rect)
        pygame.display.flip()
        pygame.time.delay(200)

    def draw_board():
        for color, (_, rect) in COLORS.items():
            pygame.draw.rect(screen, COLORS[color][0], rect)
        pygame.display.flip()

    def wait_for_click():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    for name, (_, rect) in COLORS.items():
                        if rect.collidepoint(x, y):
                            return name
            clock.tick(FPS)

    def show_sequence():
        draw_board()
        pygame.time.delay(500)
        for color in SEQUENCE:
            flash(color)

    def show_game_over():
        screen.fill((0, 0, 0))
        text = font.render("Yanlış! Oyun Bitti!", True, (255, 0, 0))
        screen.blit(text, (WIDTH // 2 - 160, HEIGHT // 2 - 30))
        pygame.display.flip()
        pygame.time.delay(3000)

    # Başlangıç
    draw_board()
    running = True

    while running:
        SEQUENCE.append(random.choice(list(COLORS.keys())))
        user_sequence = []

        show_sequence()

        for color in SEQUENCE:
            selected = wait_for_click()
            flash(selected)
            user_sequence.append(selected)
            if user_sequence[-1] != color:
                show_game_over()
                return

        pygame.time.delay(500)

if __name__ == "__main__":
    run_simon_says()

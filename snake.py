import pygame
import random
import sys

def run_snake_game():
    pygame.init()

    WIDTH, HEIGHT = 600, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("🐍 Yılan Oyunu")

    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 28)
    big_font = pygame.font.SysFont("Arial", 50, bold=True)

    # Renkler
    BG_COLOR = (240, 248, 255)
    SNAKE_COLOR = (50, 205, 50)
    SNAKE_BORDER = (34, 139, 34)
    FOOD_COLOR = (255, 99, 71)
    TEXT_COLOR = (30, 30, 30)
    FRAME_COLOR = (0, 0, 0)

    BLOCK_SIZE = 20
    snake = [(100, 100)]
    direction = (BLOCK_SIZE, 0)
    food = (random.randrange(0, WIDTH, BLOCK_SIZE), random.randrange(0, HEIGHT, BLOCK_SIZE))

    def draw_grid():
        for x in range(0, WIDTH, BLOCK_SIZE):
            for y in range(0, HEIGHT, BLOCK_SIZE):
                pygame.draw.rect(screen, (230, 230, 230), pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE), 1)

    def draw_snake():
        for segment in snake:
            pygame.draw.rect(screen, SNAKE_COLOR, pygame.Rect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(screen, SNAKE_BORDER, pygame.Rect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE), 2)

    def draw_food():
        pygame.draw.circle(screen, FOOD_COLOR, (food[0] + BLOCK_SIZE // 2, food[1] + BLOCK_SIZE // 2), BLOCK_SIZE // 2)

    def move_snake():
        nonlocal food
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        if new_head == food:
            snake.insert(0, new_head)
            while True:
                new_food = (random.randrange(0, WIDTH, BLOCK_SIZE), random.randrange(0, HEIGHT, BLOCK_SIZE))
                if new_food not in snake:
                    food = new_food
                    break
        else:
            snake.insert(0, new_head)
            snake.pop()

    def check_collision():
        head = snake[0]
        if (head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT or head in snake[1:]):
            return True
        return False

    def show_game_over():
        screen.fill(BG_COLOR)
        game_over_text = big_font.render("💀 Oyun Bitti", True, TEXT_COLOR)
        score_text = font.render(f"Puan: {len(snake)}", True, TEXT_COLOR)
        btn_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 30, 200, 50)

        pygame.draw.rect(screen, (70, 70, 70), btn_rect)
        btn_text = font.render("Ana Menüye Dön", True, (255, 255, 255))

        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 3))
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - 10))
        screen.blit(btn_text, (btn_rect.x + 15, btn_rect.y + 10))

        pygame.display.flip()
        return btn_rect

    running = True
    while running:
        screen.fill(BG_COLOR)
        draw_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, BLOCK_SIZE):
                    direction = (0, -BLOCK_SIZE)
                elif event.key == pygame.K_DOWN and direction != (0, -BLOCK_SIZE):
                    direction = (0, BLOCK_SIZE)
                elif event.key == pygame.K_LEFT and direction != (BLOCK_SIZE, 0):
                    direction = (-BLOCK_SIZE, 0)
                elif event.key == pygame.K_RIGHT and direction != (-BLOCK_SIZE, 0):
                    direction = (BLOCK_SIZE, 0)

        move_snake()
        if check_collision():
            btn = show_game_over()
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN and btn.collidepoint(event.pos):
                        waiting = False
                        running = False
            continue

        draw_snake()
        draw_food()
        pygame.draw.rect(screen, FRAME_COLOR, pygame.Rect(0, 0, WIDTH, HEIGHT), 4)

        pygame.display.flip()
        clock.tick(12)

    pygame.quit()
    
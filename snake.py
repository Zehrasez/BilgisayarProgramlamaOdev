import pygame
import sys
import random

def run_snake_game():
    pygame.init()

    WIDTH, HEIGHT = 600, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake")

    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 35)

    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)

    snake = [(100, 100)]
    direction = (20, 0)
    food = (300, 200)

    def draw_snake():
        for segment in snake:
            pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], 20, 20))

    def move_snake():
        nonlocal food
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        if new_head == food:
            snake.insert(0, new_head)
            food = (random.randrange(0, WIDTH, 20), random.randrange(0, HEIGHT, 20))
        else:
            snake.insert(0, new_head)
            snake.pop()

    def check_collision():
        head = snake[0]
        if (head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT or head in snake[1:]):
            return True
        return False

    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, 20):
                    direction = (0, -20)
                if event.key == pygame.K_DOWN and direction != (0, -20):
                    direction = (0, 20)
                if event.key == pygame.K_LEFT and direction != (20, 0):
                    direction = (-20, 0)
                if event.key == pygame.K_RIGHT and direction != (-20, 0):
                    direction = (20, 0)

        move_snake()

        if check_collision():
            running = False

        draw_snake()
        pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], 20, 20))
        pygame.display.flip()
        clock.tick(10)

    pygame.time.delay(1000)  # Ölümden sonra bekle

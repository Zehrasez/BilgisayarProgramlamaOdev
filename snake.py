import pygame
import random
import sys

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

    def game_over():
        # Oyun bitti mesajı ve butonlar
        font = pygame.font.Font(None, 50)
        game_over_text = font.render("Oyun Bitti!", True, RED)
        screen.blit(game_over_text, (WIDTH / 2 - 100, HEIGHT / 3))

        # Ana menüye dönüş butonu
        menu_button = pygame.Rect(WIDTH / 2 - 100, HEIGHT / 2, 200, 50)
        pygame.draw.rect(screen, BLACK, menu_button)
        menu_text = font.render("Ana Menüye Dön", True, WHITE)
        screen.blit(menu_text, (WIDTH / 2 - 100 + 20, HEIGHT / 2 + 10))

        pygame.display.flip()

        return menu_button

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
            # Oyun bitti
            menu_button = game_over()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if menu_button.collidepoint(x, y):
                        return  # Ana menüye dönmek için oyunu sonlandırıyoruz

        draw_snake()
        pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], 20, 20))
        pygame.display.flip()
        clock.tick(10)

    pygame.time.delay(1000)  # Ölümden sonra bekle

if __name__ == "__main__":
    run_snake_game()

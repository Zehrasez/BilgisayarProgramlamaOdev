import pygame
import sys

def run_pong_game():
    pygame.init()

    WIDTH, HEIGHT = 600, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong")

    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 35)

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    paddle_width, paddle_height = 10, 60
    player = pygame.Rect(10, HEIGHT//2 - 30, paddle_width, paddle_height)
    opponent = pygame.Rect(WIDTH - 20, HEIGHT//2 - 30, paddle_width, paddle_height)
    ball = pygame.Rect(WIDTH//2 - 10, HEIGHT//2 - 10, 15, 15)

    ball_speed = [5, 5]
    player_speed = 0
    opponent_speed = 5

    running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player_speed = -5
                if event.key == pygame.K_DOWN:
                    player_speed = 5
            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    player_speed = 0

        player.y += player_speed
        opponent.y += (ball.centery - opponent.centery) * 0.05

        ball.x += ball_speed[0]
        ball.y += ball_speed[1]

        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed[1] *= -1
        if ball.left <= 0 or ball.right >= WIDTH:
            running = False  # Skor olursa oyun bitir

        if ball.colliderect(player) or ball.colliderect(opponent):
            ball_speed[0] *= -1

        pygame.draw.rect(screen, WHITE, player)
        pygame.draw.rect(screen, WHITE, opponent)
        pygame.draw.ellipse(screen, WHITE, ball)
        pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

        pygame.display.flip()
        clock.tick(60)

    pygame.time.delay(1000)  # Kaybettikten sonra bekle

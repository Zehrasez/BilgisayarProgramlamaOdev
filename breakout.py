import pygame
import sys
import random

def run_breakout_game():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Breakout")

    clock = pygame.time.Clock()

    # Renkler
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    # PADDLE
    paddle = pygame.Rect(250, 550, 100, 10)

    # BALL
    ball = pygame.Rect(290, 300, 20, 20)
    ball_speed = [5, -5]

    # BRICKS
    bricks = [pygame.Rect(60 + i*110, 40 + j*30, 100, 20) for j in range(5) for i in range(5)]

    running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.move_ip(-8, 0)
        if keys[pygame.K_RIGHT] and paddle.right < 600:
            paddle.move_ip(8, 0)

        ball.move_ip(*ball_speed)

        # Kenar çarpışmaları
        if ball.left <= 0 or ball.right >= 600:
            ball_speed[0] *= -1
        if ball.top <= 0:
            ball_speed[1] *= -1
        if ball.bottom >= 600:
            running = False  # top yere düştü

        # Paddle çarpışma
        if ball.colliderect(paddle):
            ball_speed[1] *= -1

        # Tuğla çarpışmaları
        hit_index = ball.collidelist(bricks)
        if hit_index != -1:
            del bricks[hit_index]
            ball_speed[1] *= -1

        # Çizimler
        pygame.draw.rect(screen, BLUE, paddle)
        pygame.draw.ellipse(screen, WHITE, ball)
        for brick in bricks:
            pygame.draw.rect(screen, RED, brick)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

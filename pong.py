import pygame
import sys
import subprocess

def run_pong_game():
    pygame.init()

    WIDTH, HEIGHT = 800, 500
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 50, 50)
    BLUE = (50, 50, 255)
    FONT = pygame.font.SysFont("Arial", 36)
    BIG_FONT = pygame.font.SysFont("Arial", 60)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong")

    clock = pygame.time.Clock()

    # Paddle ve top ayarları
    paddle_width, paddle_height = 10, 100
    ball_size = 20
    player1 = pygame.Rect(30, HEIGHT//2 - paddle_height//2, paddle_width, paddle_height)
    player2 = pygame.Rect(WIDTH - 40, HEIGHT//2 - paddle_height//2, paddle_width, paddle_height)
    ball = pygame.Rect(WIDTH//2 - ball_size//2, HEIGHT//2 - ball_size//2, ball_size, ball_size)
    ball_speed = [5, 5]
    paddle_speed = 7
    score = [0, 0]
    max_score = 5
    min_speed = 3

    def draw_middle_line():
        for y in range(0, HEIGHT, 20):
            if y % 40 == 0:
                pygame.draw.rect(screen, WHITE, (WIDTH//2 - 2, y, 4, 20))

    def draw_screen():
        screen.fill(BLACK)
        draw_middle_line()
        pygame.draw.rect(screen, WHITE, player1)
        pygame.draw.rect(screen, WHITE, player2)
        pygame.draw.ellipse(screen, WHITE, ball)

        # Skor
        score_text = FONT.render(f"{score[0]}   {score[1]}", True, WHITE)
        screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 20))
        pygame.display.flip()

    def reset_ball():
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_speed[0] = -5 if ball_speed[0] > 0 else 5
        ball_speed[1] = 5

    def slow_down_ball():
        for i in range(2):
            if abs(ball_speed[i]) > min_speed:
                ball_speed[i] *= 0.95  # %5 yavaşlat

    def show_winner(winner_text):
        screen.fill(BLACK)
        msg = BIG_FONT.render(winner_text, True, RED)
        screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2 - 60))

        button_rect = pygame.Rect(WIDTH//2 - 140, HEIGHT//2 + 20, 280, 60)
        pygame.draw.rect(screen, BLUE, button_rect, border_radius=10)
        text = FONT.render("Ana Menüye Dön", True, WHITE)
        screen.blit(text, (button_rect.x + (button_rect.width - text.get_width()) // 2,
                           button_rect.y + (button_rect.height - text.get_height()) // 2))
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        pygame.quit()
                        subprocess.run(["python", "main.py"])
                        waiting = False

    running = True
    while running:
        draw_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player1.top > 0:
            player1.y -= paddle_speed
        if keys[pygame.K_s] and player1.bottom < HEIGHT:
            player1.y += paddle_speed
        if keys[pygame.K_UP] and player2.top > 0:
            player2.y -= paddle_speed
        if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
            player2.y += paddle_speed

        # Top hareketi
        ball.x += int(ball_speed[0])
        ball.y += int(ball_speed[1])

        # Kenarlara çarpma
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed[1] *= -1
            slow_down_ball()

        # Paddle çarpma
        if ball.colliderect(player1) or ball.colliderect(player2):
            ball_speed[0] *= -1
            slow_down_ball()

        # Skor kontrolü
        if ball.left <= 0:
            score[1] += 1
            reset_ball()
        if ball.right >= WIDTH:
            score[0] += 1
            reset_ball()

        # Kazanan kontrolü
        if score[0] >= max_score:
            show_winner("Sol Oyuncu Kazandı!")
            running = False
        elif score[1] >= max_score:
            show_winner("Sağ Oyuncu Kazandı!")
            running = False

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    run_pong_game()

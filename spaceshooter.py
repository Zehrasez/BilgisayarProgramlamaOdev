import pygame
import random

def run_spaceshooter_game():
    pygame.init()

    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)

    WIDTH, HEIGHT = 480, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Uzay Gemisi (Space Shooter)")

    clock = pygame.time.Clock()
    FPS = 60

    player_img = pygame.Surface((50, 40))
    player_img.fill(BLUE)
    player_rect = player_img.get_rect()
    player_rect.centerx = WIDTH // 2
    player_rect.bottom = HEIGHT - 10
    player_speed = 5

    bullets = []
    bullet_speed = -7

    enemies = []
    enemy_speed = 3
    spawn_timer = 30

    def spawn_enemy():
        enemy = pygame.Rect(random.randint(0, WIDTH - 40), 0, 40, 30)
        enemies.append(enemy)

    score = 0
    font = pygame.font.SysFont(None, 36)

    running = True
    while running:
        clock.tick(FPS)
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_rect.left > 0:
            player_rect.x -= player_speed
        if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
            player_rect.x += player_speed
        if keys[pygame.K_SPACE]:
            if len(bullets) < 5:
                bullet = pygame.Rect(player_rect.centerx - 2, player_rect.top, 4, 10)
                bullets.append(bullet)

        for bullet in bullets[:]:
            bullet.y += bullet_speed
            if bullet.bottom < 0:
                bullets.remove(bullet)

        spawn_timer -= 1
        if spawn_timer <= 0:
            spawn_enemy()
            spawn_timer = random.randint(20, 40)

        for enemy in enemies[:]:
            enemy.y += enemy_speed
            if enemy.top > HEIGHT:
                enemies.remove(enemy)

        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if bullet.colliderect(enemy):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 1
                    break

        for enemy in enemies:
            if enemy.colliderect(player_rect):
                running = False

        screen.blit(player_img, player_rect)
        for bullet in bullets:
            pygame.draw.rect(screen, WHITE, bullet)
        for enemy in enemies:
            pygame.draw.rect(screen, RED, enemy)

        score_text = font.render(f"Skor: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

    pygame.quit()  # Oyunu düzgün kapat (ancak sys.exit() yok!)

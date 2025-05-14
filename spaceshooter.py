import pygame
import random

def run_spaceshooter_game():
    pygame.init()

    # Renkler
    DARK_BLUE = (10, 10, 30)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 100, 255)
    YELLOW = (255, 255, 0)
    GRAY = (150, 150, 150)
    PURPLE = (150, 0, 255)
    ORANGE = (255, 140, 0)

    # Ekran boyutu
    WIDTH, HEIGHT = 480, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("🚀 Space Shooter")

    clock = pygame.time.Clock()
    FPS = 60

    # Oyuncu görseli (üçgen uzay gemisi)
    player_img = pygame.Surface((50, 40), pygame.SRCALPHA)
    pygame.draw.polygon(player_img, BLUE, [(0, 40), (25, 0), (50, 40)])
    player_rect = player_img.get_rect(center=(WIDTH // 2, HEIGHT - 50))
    player_speed = 5

    # Kurşunlar
    bullets = []
    bullet_speed = -10

    # Düşmanlar
    enemies = []
    enemy_speed = 3
    spawn_timer = 30

    # Skor
    score = 0
    font = pygame.font.SysFont("consolas", 28)

    # Rastgele gezegen ve yıldız konumları
    stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(60)]
    planets = [
        {"pos": (80, 120), "radius": 40, "color": PURPLE},
        {"pos": (400, 80), "radius": 30, "color": ORANGE},
        {"pos": (300, 400), "radius": 50, "color": GRAY}
    ]

    def spawn_enemy():
        enemy = pygame.Rect(random.randint(0, WIDTH - 40), -40, 40, 30)
        enemies.append(enemy)

    def draw_background():
        screen.fill(DARK_BLUE)
        for x, y in stars:
            pygame.draw.circle(screen, WHITE, (x, y), 1)
        for planet in planets:
            pygame.draw.circle(screen, planet["color"], planet["pos"], planet["radius"])

    def draw_explosion(center):
        for _ in range(10):
            radius = random.randint(3, 6)
            offset_x = random.randint(-10, 10)
            offset_y = random.randint(-10, 10)
            pygame.draw.circle(screen, YELLOW, (center[0] + offset_x, center[1] + offset_y), radius)

    # Ana oyun döngüsü
    running = True
    while running:
        clock.tick(FPS)
        draw_background()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Tuş kontrol
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_rect.left > 0:
            player_rect.x -= player_speed
        if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
            player_rect.x += player_speed
        if keys[pygame.K_SPACE]:
            if len(bullets) < 6:
                bullet = pygame.Rect(player_rect.centerx - 2, player_rect.top, 4, 10)
                bullets.append(bullet)

        # Kurşun güncelleme
        for bullet in bullets[:]:
            bullet.y += bullet_speed
            if bullet.bottom < 0:
                bullets.remove(bullet)

        # Düşman üretimi
        spawn_timer -= 1
        if spawn_timer <= 0:
            spawn_enemy()
            spawn_timer = random.randint(20, 40)

        # Düşman güncelleme
        for enemy in enemies[:]:
            enemy.y += enemy_speed
            if enemy.top > HEIGHT:
                enemies.remove(enemy)

        # Çarpışma
        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if bullet.colliderect(enemy):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 1
                    draw_explosion(enemy.center)
                    break

        # Oyuncuya çarpma
        for enemy in enemies:
            if enemy.colliderect(player_rect):
                running = False

        # Çizimler
        screen.blit(player_img, player_rect)
        for bullet in bullets:
            pygame.draw.rect(screen, WHITE, bullet)
        for enemy in enemies:
            pygame.draw.rect(screen, RED, enemy)

        # Skor
        score_text = font.render(f"Skor: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

    pygame.quit()

# Oyun çağrısı
if __name__ == "__main__":
    run_spaceshooter_game()

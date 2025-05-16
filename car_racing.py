import pygame
import random
import sys

def run_car_racing_game():
    pygame.init()

    WIDTH, HEIGHT = 400, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Car Racing")

    clock = pygame.time.Clock()

    # Renkler
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (200, 0, 0)
    GREEN = (0, 180, 0)
    GREY = (60, 60, 60)
    YELLOW = (255, 215, 0)

    # Oyuncu arabası
    car_img = pygame.Surface((40, 70), pygame.SRCALPHA)
    pygame.draw.rect(car_img, GREEN, (0, 0, 40, 70), border_radius=8)
    car = car_img.get_rect(center=(WIDTH // 2, HEIGHT - 80))

    # Düşman arabaları
    enemy_img = pygame.Surface((40, 70), pygame.SRCALPHA)
    pygame.draw.rect(enemy_img, RED, (0, 0, 40, 70), border_radius=8)
    enemy_cars = []
    enemy_speed = 5
    spawn_enemy_event = pygame.USEREVENT + 1
    pygame.time.set_timer(spawn_enemy_event, 1500)

    # Altınlar
    coin_radius = 10
    coins = []
    spawn_coin_event = pygame.USEREVENT + 2
    pygame.time.set_timer(spawn_coin_event, 2000)

    score = 0
    font = pygame.font.SysFont(None, 32)

    def draw_road_lines():
        for y in range(0, HEIGHT, 40):
            pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 5, y, 10, 20))

    running = True
    while running:
        screen.fill(GREY)
        draw_road_lines()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == spawn_enemy_event:
                lane = random.choice([
                    WIDTH // 4 - 20,
                    WIDTH // 2 - 20,
                    3 * WIDTH // 4 - 20
                ])
                enemy_cars.append(enemy_img.get_rect(topleft=(lane, -70)))
            if event.type == spawn_coin_event:
                x = random.choice([WIDTH // 4, WIDTH // 2, 3 * WIDTH // 4])
                coins.append(pygame.Rect(x - coin_radius, -20, coin_radius*2, coin_radius*2))

        # Tuşlar
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car.left > 0:
            car.x -= 5
        if keys[pygame.K_RIGHT] and car.right < WIDTH:
            car.x += 5

        # Düşmanları hareket ettir
        for enemy in enemy_cars:
            enemy.y += enemy_speed
        enemy_cars = [e for e in enemy_cars if e.y < HEIGHT]

        # Altınları hareket ettir
        for coin in coins:
            coin.y += 4
        coins = [c for c in coins if c.y < HEIGHT]

        # Çarpışma kontrolü
        for enemy in enemy_cars:
            if car.colliderect(enemy):
                game_over_text = font.render(f"Game Over! Skor: {score}", True, RED)
                screen.blit(game_over_text, (WIDTH // 2 - 130, HEIGHT // 2))
                pygame.display.flip()
                pygame.time.delay(2000)
                return

        for coin in coins[:]:
            if car.colliderect(coin):
                coins.remove(coin)
                score += 5

        # Çizimler
        screen.blit(car_img, car.topleft)
        for enemy in enemy_cars:
            screen.blit(enemy_img, enemy.topleft)
        for coin in coins:
            pygame.draw.circle(screen, YELLOW, coin.center, coin_radius)

        score_text = font.render(f"Skor: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    run_car_racing_game()

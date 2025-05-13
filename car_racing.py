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
    GREY = (50, 50, 50)

    # Oyuncu arabası
    car_width, car_height = 40, 70
    car = pygame.Rect(WIDTH // 2 - car_width // 2, HEIGHT - 100, car_width, car_height)

    # Düşman arabalar
    enemy_width, enemy_height = 40, 70
    enemy_cars = []
    enemy_speed = 5
    spawn_event = pygame.USEREVENT + 1
    pygame.time.set_timer(spawn_event, 1500)

    score = 0
    font = pygame.font.SysFont(None, 36)

    running = True
    while running:
        screen.fill(GREY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == spawn_event:
                lane = random.choice([
                    WIDTH // 4 - car_width // 2,
                    WIDTH // 2 - car_width // 2,
                    3 * WIDTH // 4 - car_width // 2
                ])
                enemy_cars.append(pygame.Rect(lane, -enemy_height, enemy_width, enemy_height))

        # Tuş kontrolleri
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car.left > 0:
            car.move_ip(-5, 0)
        if keys[pygame.K_RIGHT] and car.right < WIDTH:
            car.move_ip(5, 0)

        # Düşmanları hareket ettir
        for enemy in enemy_cars:
            enemy.move_ip(0, enemy_speed)

        # Çarpışma kontrolü
        for enemy in enemy_cars:
            if car.colliderect(enemy):
                game_over_text = font.render("Game Over! Skor: " + str(score), True, RED)
                screen.blit(game_over_text, (WIDTH // 2 - 120, HEIGHT // 2))
                pygame.display.flip()
                pygame.time.delay(2000)
                return

        # Ekrandan çıkan düşmanları temizle
        enemy_cars = [enemy for enemy in enemy_cars if enemy.top < HEIGHT]
        score += 1

        # Çizimler
        pygame.draw.rect(screen, GREEN, car)
        for enemy in enemy_cars:
            pygame.draw.rect(screen, RED, enemy)

        score_text = font.render(f"Skor: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    run_car_racing_game()



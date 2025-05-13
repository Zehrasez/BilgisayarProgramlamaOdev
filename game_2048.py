import pygame
import sys
import random

def run_2048_game():
    pygame.init()

    WIDTH = 400
    HEIGHT = 400
    SIZE = 4
    TILE_SIZE = WIDTH // SIZE
    FONT = pygame.font.SysFont("arial", 30, bold=True)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("2048")

    COLORS = {
        0: (200, 200, 200),
        2: (240, 228, 218),
        4: (237, 224, 200),
        8: (242, 177, 121),
        16: (245, 149, 99),
        32: (246, 124, 95),
        64: (246, 94, 59),
        128: (237, 207, 114),
        256: (237, 204, 97),
        512: (237, 200, 80),
        1024: (237, 197, 63),
        2048: (237, 194, 46)
    }

    grid = [[0] * SIZE for _ in range(SIZE)]

    def draw_grid():
        screen.fill((187, 173, 160))
        for y in range(SIZE):
            for x in range(SIZE):
                val = grid[y][x]
                rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(screen, COLORS.get(val, (60, 58, 50)), rect)
                if val:
                    text = FONT.render(str(val), True, (0, 0, 0))
                    text_rect = text.get_rect(center=rect.center)
                    screen.blit(text, text_rect)
        pygame.display.flip()

    def add_random_tile():
        empty = [(y, x) for y in range(SIZE) for x in range(SIZE) if grid[y][x] == 0]
        if empty:
            y, x = random.choice(empty)
            grid[y][x] = 2 if random.random() < 0.9 else 4

    def compress_and_merge(row):
        new_row = [i for i in row if i != 0]
        for i in range(len(new_row)-1):
            if new_row[i] == new_row[i+1]:
                new_row[i] *= 2
                new_row[i+1] = 0
        return [i for i in new_row if i != 0]

    def move_left():
        moved = False
        for y in range(SIZE):
            new_row = compress_and_merge(grid[y])
            new_row += [0] * (SIZE - len(new_row))
            if new_row != grid[y]:
                grid[y] = new_row
                moved = True
        return moved

    def move_right():
        moved = False
        for y in range(SIZE):
            reversed_row = grid[y][::-1]
            new_row = compress_and_merge(reversed_row)
            new_row += [0] * (SIZE - len(new_row))
            new_row.reverse()
            if new_row != grid[y]:
                grid[y] = new_row
                moved = True
        return moved

    def move_up():
        moved = False
        for x in range(SIZE):
            col = [grid[y][x] for y in range(SIZE)]
            new_col = compress_and_merge(col)
            new_col += [0] * (SIZE - len(new_col))
            for y in range(SIZE):
                if grid[y][x] != new_col[y]:
                    grid[y][x] = new_col[y]
                    moved = True
        return moved

    def move_down():
        moved = False
        for x in range(SIZE):
            col = [grid[y][x] for y in range(SIZE)][::-1]
            new_col = compress_and_merge(col)
            new_col += [0] * (SIZE - len(new_col))
            new_col.reverse()
            for y in range(SIZE):
                if grid[y][x] != new_col[y]:
                    grid[y][x] = new_col[y]
                    moved = True
        return moved

    def can_move():
        for y in range(SIZE):
            for x in range(SIZE):
                if grid[y][x] == 0:
                    return True
                if x + 1 < SIZE and grid[y][x] == grid[y][x+1]:
                    return True
                if y + 1 < SIZE and grid[y][x] == grid[y+1][x]:
                    return True
        return False

    add_random_tile()
    add_random_tile()

    running = True
    while running:
        draw_grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                moved = False
                if event.key == pygame.K_LEFT:
                    moved = move_left()
                elif event.key == pygame.K_RIGHT:
                    moved = move_right()
                elif event.key == pygame.K_UP:
                    moved = move_up()
                elif event.key == pygame.K_DOWN:
                    moved = move_down()

                if moved:
                    add_random_tile()

        if not can_move():
            draw_grid()
            font_big = pygame.font.SysFont("arial", 50, bold=True)
            text = font_big.render("Oyun Bitti!", True, (255, 0, 0))
            screen.blit(text, (WIDTH//2 - 100, HEIGHT//2 - 25))
            pygame.display.flip()
            pygame.time.delay(3000)
            return

if __name__ == "__main__":
    run_2048_game()

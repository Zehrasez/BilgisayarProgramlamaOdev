import pygame
import sys

def run_maze_game():
    pygame.init()
    
    WIDTH, HEIGHT = 600, 600
    TILE_SIZE = 40
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Maze Game")

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)

    maze = [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
        [1,0,1,1,1,0,1,0,1,1,1,1,1,0,1],
        [1,0,1,0,1,0,0,0,0,0,0,0,1,0,1],
        [1,0,1,0,1,1,1,1,1,1,1,0,1,0,1],
        [1,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,0,1,1,1,0,1],
        [1,0,0,0,0,0,0,0,1,0,0,0,1,0,1],
        [1,0,1,1,1,1,1,0,1,1,1,0,1,0,1],
        [1,0,0,0,0,0,1,0,0,0,1,0,0,0,1],
        [1,1,1,1,1,0,1,1,1,0,1,1,1,1,1],
        [1,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
        [1,0,1,0,1,1,1,1,1,1,1,1,1,0,1],
        [1,0,1,0,0,0,0,0,0,0,0,0,1,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,0,1,1,1],
    ]

    player_pos = [1, 1]
    goal_pos = [13, 13]
    clock = pygame.time.Clock()

    def draw_maze():
        for y in range(len(maze)):
            for x in range(len(maze[y])):
                rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                color = WHITE if maze[y][x] == 0 else BLACK
                pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLUE, (player_pos[0]*TILE_SIZE, player_pos[1]*TILE_SIZE, TILE_SIZE, TILE_SIZE))
        pygame.draw.rect(screen, GREEN, (goal_pos[0]*TILE_SIZE, goal_pos[1]*TILE_SIZE, TILE_SIZE, TILE_SIZE))

    running = True
    while running:
        screen.fill(WHITE)
        draw_maze()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]: dx = -1
        elif keys[pygame.K_RIGHT]: dx = 1
        elif keys[pygame.K_UP]: dy = -1
        elif keys[pygame.K_DOWN]: dy = 1

        new_x = player_pos[0] + dx
        new_y = player_pos[1] + dy

        if 0 <= new_x < 15 and 0 <= new_y < 15 and maze[new_y][new_x] == 0:
            player_pos = [new_x, new_y]

        if player_pos == goal_pos:
            font = pygame.font.SysFont(None, 48)
            text = font.render("Tebrikler! Çıkışı buldunuz!", True, GREEN)
            screen.blit(text, (60, HEIGHT // 2))
            pygame.display.flip()
            pygame.time.delay(3000)
            return

        pygame.display.flip()
        clock.tick(10)

if __name__ == "__main__":
    run_maze_game()

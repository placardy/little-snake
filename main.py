from random import randint
import pygame
pygame.init()
WSIZE = (720, 480)

# ЧАСТЬ 3 ШРИФТ
font_score = pygame.font.SysFont("Arial", 26)
font_gameover = pygame.font.SysFont("Arial", 45)
font_space = pygame.font.SysFont("Arial", 18)


# Размер кубика
TSIDE = 30
# Размер карты, который исходит из размера экрана
MSIZE = WSIZE[0] // TSIDE, WSIZE[1] // TSIDE

# Начальная позиция - цент экрана
start_pos = MSIZE[0] // 2, MSIZE[1] // 2
# Змейка
snake = [start_pos]

apple = randint(0, MSIZE[0]-1), randint(0, MSIZE[1]-1)
# Флаг, жива ли змея
alive = True
fps = 5
direction = 0
# Направление змейки
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

pygame.init()
screen = pygame.display.set_mode(WSIZE)
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(fps)
    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.KEYDOWN:
            if alive:
                if event.key == pygame.K_RIGHT:  # and direction != 2
                    direction = 0
                if event.key == pygame.K_DOWN:   # and direction != 3
                    direction = 1
                if event.key == pygame.K_LEFT:  # and direction != 0
                    direction = 2
                if event.key == pygame.K_UP:   # and direction != 1
                    direction = 3
            else:
                if event.key == pygame.K_SPACE:
                    alive = True
                    snake = [start_pos]
                    fps = 5
                    apple = randint(0, MSIZE[0]-1), randint(0, MSIZE[1]-1)

    # Вывод змейки на экран.                 Границы объекта, который мы рисуем, проходимся по всем позициям
    [pygame.draw.rect(screen, "green", (x * TSIDE, y * TSIDE, TSIDE - 1, TSIDE - 1)) for x, y in snake]
    # Вывод яблока
    pygame.draw.rect(screen, "red", (apple[0] * TSIDE, apple[1] * TSIDE, TSIDE - 1, TSIDE - 1))

    # Движение змейки
    # Если живы - идём
    if alive: 
        new_pos = snake[0][0] + directions[direction][0], snake[0][1] + directions[direction][1]

        # ЧАСТЬ 2
        # ПРОВЕКИ, встретили яблоко, встретии бордюр, встретили сами себя
        if not (0 <= new_pos[0] < MSIZE[0] and 0 <= new_pos[1] < MSIZE[1]) or new_pos in snake:
            alive = False
        else:
        # 1 ЧАСТЬ
        # Змейке в голову передаём новую позицию
            snake.insert(0, new_pos)

            # 2 ЧАСТь
            if new_pos == apple:
                fps += 1
                apple = randint(0, MSIZE[0]-1), randint(0, MSIZE[1]-1)
            else:
                snake.pop(-1)
    else:
        text = font_gameover.render(f"GAME OVER", True, "red")
        screen.blit(text, (WSIZE[0]//2 - text.get_width()//2, WSIZE[1] // 2 - 50))
        text = font_space.render(f"Press SPACE for restart", True, "white")
        screen.blit(text, (WSIZE[0]//2 - text.get_width()//2, WSIZE[1] // 2 + 50))
    print(snake)
    screen.blit(font_score.render(f"Score: {len(snake)}", True, "yellow"), (5, 5))
    pygame.display.update()

import pygame
from cell_class import Cell
from random import randint, seed

pygame.init()
size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('')
screen.fill([255, 255, 255])
pygame.display.set_icon(screen)
clock, fps = pygame.time.Clock(), 30

cell_w = 10
cell_h = 10

def generate_grid():
    seed_ = randint(1000, 100000)
    seed(seed_)

    print('*' * 50)
    print('\nSEED', seed_, '\n')
    print('*' * 50)

    grid = []
    offset = 50
    r_offset = randint(0, 255)
    g_offset = randint(0, 255)
    b_offset = randint(0, 255)

    offset_rate_of_change = randint(1, 50)
    r_offset_rate_of_change = randint(1, 50)
    g_offset_rate_of_change = randint(1, 50)
    b_offset_rate_of_change = randint(1, 50)

    for i in range(int(size[1] / cell_h)):
        for j in range(int(size[0] / cell_w)):
            grid.append(Cell(j * cell_w, i * cell_h, cell_w, cell_h, r_offset, g_offset, b_offset, offset))

            offset += offset_rate_of_change
            r_offset += r_offset_rate_of_change
            g_offset += g_offset_rate_of_change
            b_offset += b_offset_rate_of_change

    return grid

grid = generate_grid()

slowdown = 0
frames_to_wait = 30
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    key = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    if key[pygame.K_SPACE] and slowdown <= 0:
        grid = generate_grid()
        slowdown = frames_to_wait
    else:
        slowdown -= 1

    for cell in grid:
        cell.draw(screen)

    pygame.display.update()
    clock.tick(fps)

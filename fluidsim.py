import math
import random
import time

import pygame
pygame.init()
width = 100
height = 100
scale_factor = 8
pixel_size = 1
map = []

holding_LEFT_button = False
holding_RIGHT_button = False



def setup():
    for i in range(width + 1):
        col = []
        for j in range(height + 1):
            if j == height:
                col.append(2)
            else:
                col.append(0)
        map.append(col)

def render():
    for y in range(height):
        for x in range(width):
            if map[x][y] == 1:
                rbg_colour = (0, 0, 255)
            elif map[x][y] == 2:
                rbg_colour = (255, 255, 255)
            else:
                rbg_colour = (0, 0, 0)
            #pygame.draw.circle(display_screen, rbg_colour, (x*scale_factor, y*scale_factor), pixel_size*scale_factor)
            pygame.draw.rect(display_screen, rbg_colour,(x * scale_factor, y * scale_factor, pixel_size * scale_factor, pixel_size * scale_factor))


def step():
    if holding_LEFT_button:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        map[round(mouse_x / scale_factor)][round(mouse_y / scale_factor)] = 1
    elif holding_RIGHT_button:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        map[round(mouse_x / scale_factor)][round(mouse_y / scale_factor)] = 2
    new_map = map
    for y in range(height - 1, 0, -1):
        for x in range(width - 1, -1, -1):
            if map[x][y] == 1:
                check_first = random.choice([3, 4])
                surrounding_cells = [
                    map[x][y + 1],
                    map[x - 1][y + 1],
                    map[x + 1][y + 1],
                    map[x + 1][y],
                    map[x - 1][y],
                ]
                if surrounding_cells[0] == 0:
                    new_map[x][y+1] = 1
                    new_map[x][y] = 0
                elif surrounding_cells[1] == 0:
                    new_map[x - 1][y + 1] = 1
                    new_map[x][y] = 0
                elif surrounding_cells[2] == 0:
                    new_map[x + 1][y + 1] = 1
                    new_map[x][y] = 0
                elif surrounding_cells[check_first] == 0:
                    if check_first == 3:
                        new_map[x + 1][y] = 1
                    elif check_first == 4:
                        new_map[x - 1][y] = 1
                    new_map[x][y] = 0


background_colour = 0, 0, 0
screen = pygame.display.set_mode((width, height))
display_screen = pygame.display.set_mode((width * scale_factor, height * scale_factor))
pygame.display.set_caption('fluidsim')
running = True
setup()
while running:
    step()
    render()
    time.sleep(1 / 60)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            holding_LEFT_button = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == pygame.BUTTON_LEFT:
            holding_LEFT_button = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_RIGHT:
            holding_RIGHT_button = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == pygame.BUTTON_RIGHT:
            holding_RIGHT_button = False

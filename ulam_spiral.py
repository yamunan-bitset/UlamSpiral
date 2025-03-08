import pygame
import math

w = 1000
h = 1000

def math_pos_to_screen_coord(x, y):
    return (x + w/2, h/2 - y)

def math_coord_to_screen_coord(coord):
    return (coord[0] + w/2, h/2 - coord[1])

def is_prime(n):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

radius = 2
def num_to_screen_coord(n):
    pos = [0, 0]
    s = radius * 5
    j = 0
    num = 1
    for i in range(n):
        for k in range(j):
            num += 1
            pos[0 if (i % 4) % 2 == 0 else 1] += s * (-1) ** (1 if i % 4 == 2 or i % 4 == 1 else 0)
            if num == n: return math_pos_to_screen_coord(pos[0], pos[1])
        if (i % 2 == 0): j += 1
    return math_pos_to_screen_coord(pos[0], pos[1])

pygame.init()

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Ulam Spiral")

tn = 1000
running = True
while running:
    event = pygame.event.wait()
    if event.type == pygame.QUIT: running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_PLUS: tn += 100
        if event.key == pygame.K_MINUS: tn -= 100

    screen.fill((255, 255, 255))

    pos = [0, 0]
    s = radius * 5
    j = 0
    num = 1
    for i in range(tn):
        for k in range(j):
            num += 1
            pos[0 if (i % 4) % 2 == 0 else 1] += s * (-1) ** (1 if i % 4 == 2 or i % 4 == 1 else 0)
            color = (255, 0, 0) if is_prime(num) else (0, 0, 0)
            pygame.draw.circle(screen, color, math_pos_to_screen_coord(pos[0], pos[1]), radius)
        if (i % 2 == 0): j += 1

    pygame.draw.circle(screen, (255, 0, 255), math_coord_to_screen_coord([0, 0]), radius)
    pygame.display.flip()

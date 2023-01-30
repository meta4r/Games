import pygame
import random

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake Game")

x1, y1 = 250, 250
width, height = 10, 10
vel = 10
dir_x, dir_y = 0, 0

def snake(x, y, w, h, dx, dy):
    pygame.draw.rect(win, (0, 255, 0), (x, y, h if dx == 0 else w, w if dx == 0 else h))

dot_x, dot_y = random.randint(0, 490), random.randint(0, 490)
def dot(x, y):
    pygame.draw.rect(win, (255, 0, 0), (x, y, 10, 10))

score = 0
run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: dir_x, dir_y = -vel, 0
    if keys[pygame.K_RIGHT]: dir_x, dir_y = vel, 0
    if keys[pygame.K_UP]: dir_y, dir_x = -vel, 0
    if keys[pygame.K_DOWN]: dir_y, dir_x = vel, 0
    x1 += dir_x
    y1 += dir_y
    x1 %= 500
    y1 %= 500
    win.fill((0, 0, 0))
    snake(x1, y1, width, height, dir_x, dir_y)
    dot(dot_x, dot_y)
    if x1 < dot_x + 10 and x1 + width > dot_x and y1 < dot_y + 10 and y1 + height > dot_y:
        dot_x, dot_y = random.randint(0, 490), random.randint(0, 490)
        score += 1
        width += 10
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    win.blit(text, (350, 10))
    pygame.display.update()
    
pygame.quit()

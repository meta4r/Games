import pygame
import random

pygame.init()
window = pygame.display.set_mode((600,400))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

ball_w, ball_h = 20, 20
ball_x, ball_y = window.get_width()//2 - ball_w//2, window.get_height()//2 - ball_h//2
ball_speed_x, ball_speed_y = 5, 5
ball_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

paddle_w, paddle_h = 20, 100
paddle1_x, paddle1_y = 20, window.get_height()//2 - paddle_h//2
paddle2_x, paddle2_y = window.get_width() - 20 - paddle_w, window.get_height()//2 - paddle_h//2
paddle_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
paddle_speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                paddle1_y -= paddle_speed
            if event.key == pygame.K_DOWN:
                paddle1_y += paddle_speed

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_y > paddle2_y + paddle_h//2:
        paddle2_y += paddle_speed
    elif ball_y < paddle2_y + paddle_h//2:
        paddle2_y -= paddle_speed

    if ball_y <= 0 or ball_y + ball_h >= window.get_height():
        ball_speed_y = -ball_speed_y
    if ball_x <= paddle1_x + paddle_w or ball_x + ball_w >= paddle2_x:
        ball_speed_x = -ball_speed_x

    window.fill((255,255,255))
    pygame.draw.rect(window, ball_color, (ball_x, ball_y, ball_w, ball_h))
    pygame.draw.rect(window, paddle_color, (paddle1_x, paddle1_y, paddle_w, paddle_h))
    pygame.draw.rect(window, paddle_color, (paddle2_x, paddle2_y, paddle_w, paddle_h))
    pygame.display.update()
    clock.tick(60)

pygame.quit()

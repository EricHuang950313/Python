import pygame
pygame.init()
screen = pygame.display.set_mode((640, 320))
pygame.display.set_caption("動畫")
background = pygame.Surface(screen.get_size())
background = background.convert()
COLOR = (209, 236, 252)
background.fill(COLOR)

ball = pygame.Surface((50,50))
ball.fill((209, 236, 252))
pygame.draw.circle(ball, (0, 0, 255), (25, 25), 25, 0)
rect = ball.get_rect()
rect.center = (320, 160)
x, y = rect.topleft
speed = 5
touch = 0
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0, 0))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if touch % 2 != 0:
            speed = -2
        else:
            speed = 2
        if(rect.left <= 0 or rect.right >= screen.get_width()):
            speed *= -1
            touch += 1
    else:
        if touch % 2 != 0:
            speed = -5
        else:
            speed = 5
        if(rect.left <= 0 or rect.right >= screen.get_width()):
            speed *= -1
            touch += 1
    x += speed
    rect.center = (x, y)
    screen.blit(ball, rect.topleft)
    pygame.display.update()
pygame.quit()
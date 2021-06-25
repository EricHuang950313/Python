import pygame, random, math
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("自由移動")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))
ball = pygame.Surface((30,30))  
ball.fill((255,255,255))  
pygame.draw.circle(ball, (0,0,255), (15,15), 15, 0)  
rect1 = ball.get_rect() 
rect1.center = (random.randint(100,250),random.randint(150,250))
x, y = rect1.topleft  
direction = random.randint(20, 70) 
radian = math.radians(direction) 
dx = 3
dy = -3
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0,0))
    x += dx
    y += dy
    rect1.center = (x,y)
    if(rect1.left <= 0 or rect1.right >= screen.get_width()):
        dx *= -1
    elif(rect1.top <= 5 or rect1.bottom >= screen.get_height()-5):
        dy *= -1
    screen.blit(ball, rect1.topleft)
    pygame.display.update()
pygame.quit()
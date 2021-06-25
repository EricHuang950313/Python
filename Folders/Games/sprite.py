import pygame, random, math

class Ball(pygame.sprite.Sprite):
    x = 0
    y = 0
    speedx = 0
    speedy = 0


    def __init__(self, speed, placex, placey, radius, color):
        pygame.sprite.Sprite.__init__(self)
        self.x = placex
        self.y = placey
        self.image = pygame.Surface([radius*2, radius*2])
        self.image.fill((255, 255, 255))
        pygame.draw.circle(self.image, color, (radius, radius), radius, 0)
        self.rect = self.image.get_rect()
        self.rect.center = (placex, placey)
        direction = random.randint(20, 70) 
        radian = math.radians(direction) 
        self.speedx = speed
        self.speedy = -speed


    def update(self):
        self.x += self.speedx
        self.y += self.speedy
        self.rect.x = self.x
        self.rect.y = self.y
        if(self.rect.left <= 0 or self.rect.right >= screen.get_width()):
            self.speedx *= -1
        elif(self.rect.top <= 5 or self.rect.bottom >= screen.get_height()-5):
            self.speedy *= -1

# basic set
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("撞在一起不會怎樣")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))

allsprite = pygame.sprite.Group()
Ball1 = Ball(2, 100, 100, 10, (0, 0, 255))
allsprite.add(Ball1)
Ball2 = Ball(5, 100, 100, 10, (0, 255, 0))
allsprite.add(Ball2)

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0,0))
    Ball1.update()
    Ball2.update()
    allsprite.draw(screen)
    pygame.display.update()
pygame.quit()
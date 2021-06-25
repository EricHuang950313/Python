import pygame
pygame.init()
screen = pygame.display.set_mode((640, 300))
pygame.display.set_caption("Pad_class")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))

class Pad(pygame.sprite.Sprite):
    playing = False

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ball = pygame.Surface((70,10))  
        self.ball.fill((0,0,255))  
        pygame.draw.circle(self.ball, (0,0,255), (250,320), 1, 0)
        self.rect1 = self.ball.get_rect()  
        self.rect1.center = (320,250)  
        self.x, self.y = self.rect1.topleft


    def update(self):  
        buttons = pygame.mouse.get_pressed()
        if buttons[0]:  
            Pad.playing = True
        elif buttons[2]:  
            Pad.playing = False
        if Pad.playing == True:  
            mouses = pygame.mouse.get_pos()  
            self.rect1.centerx = mouses[0]  
            self.rect1.centery = 250


clock = pygame.time.Clock()
running = True
pad = Pad()
allsprite = pygame.sprite.Group()
allsprite.add(pad)

while running:
    clock.tick(30)  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pad.update()
    screen.blit(background, (0,0))  
    screen.blit(pad.ball, pad.rect1.topleft)
    pygame.display.update()
pygame.quit()
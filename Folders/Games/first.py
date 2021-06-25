import pygame

pygame.init()    # start pygame
screen = pygame.display.set_mode((640,320))   # screen
pygame.display.set_caption("PyGame")    # Title

background = pygame.Surface(screen.get_size())    # canvas -- background
background = background.convert()

COLOR = (209, 236, 252)     # set color
background.fill(COLOR)

# square:pygame.draw.rect(canvas, colors, [x, y, width, long], outline)
pygame.draw.rect(background, (0, 0, 255), [320, 160, 50, 50], 0)

# circle:pygame.draw.circle(canvas, colors, (x, y),radius,  outline)
pygame.draw.circle(background, (255, 70, 0), (320, 160), 30, 2)

# display:screen / background
screen.blit(background, (0, 0))     # display from (0, 0)left

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
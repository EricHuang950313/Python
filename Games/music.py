import pygame

pygame.mixer.init()
def music():

    pygame.mixer.music.load("Up_Above.mp3")
    pygame.mixer.music.play(loops=-1)
music()
a = input()
print(a)
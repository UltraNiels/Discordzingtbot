import pygame
print('Starting!')

try:
    import pygame
    from pygame.locals import *
except:
    print('It seems like pygame isn\'t installed')

pygame.init()
size = width, height = 800, 800
fullscreen = False
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Lyrics Syncer')
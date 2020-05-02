import pygame, PySimpleGUI as sg, os
from pygame.locals import *


pygame.init()
size = width, height = 800, 800
fullscreen = False
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Lyrics Syncer')
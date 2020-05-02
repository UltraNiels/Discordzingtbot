import pygame, PySimpleGUI as sg, os
from pygame.locals import *

sg.theme('Darkblue3')
layout = [  
            [sg.Text('Song (mp3 or wav)')],
            [ sg.In(size=(40,0), key='FilePath'), sg.FileBrowse()],
            [sg.Text('Title of song')],
            [sg.Input(size=(50,0), key='Title')],
            [sg.Text('Artist')],
            [sg.Input(size=(50,0), key='Artist')],
            [sg.Button('Ok'), sg.Cancel()]
         ]
window = sg.Window('Lyrics Sycer Options', layout)
while True:
    event, values = window.read()
    if event in (None, 'Cancel', 'Exit'):
        window.close()
        exit()
    if event == 'Ok':
        if not os.path.isfile(values['FilePath']):
            sg.Popup('File doesn\'t exist!', title='Error')
        elif not values['FilePath'].lower().endswith(('.mp3', '.wav', '.ogg')):
            sg.Popup('File type not supported!\nPlease us an mp3, wav or ogg file.')
        elif not values['Title']:
            sg.Popup('Please provide the title of the song')
        elif not values['Artist']:
            sg.Popup('Please provide the artist of the song')
        else:
            break

window.close()

def fucking_draw_text(text, coords, font='Comic Sans MS', size=30):
    myfont = pygame.font.SysFont(font, size)
    textsurface = myfont.render(text, False, (0, 0, 0))
    screen.blit(textsurface,(coords[0], coords[1]))

pygame.init()
size = width, height = 800, 800
fullscreen = False
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Lyrics Syncer')while True:
    for event in pygame.event.get(): #system events
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
    
    screen.fill(pygame.Color(255,255,255))
    fucking_draw_text('Song: ' + song, (0, 0))
    fucking_draw_text('Artist: ' + artist, (0, 40))


    pygame.display.flip()

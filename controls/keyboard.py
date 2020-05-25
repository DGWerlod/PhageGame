import pygame
import constants

pygame.init()

presets = {'keyW': pygame.K_w, 'keyA': pygame.K_a, 'keyS': pygame.K_s, 'keyD': pygame.K_d, 'keySpace': pygame.K_SPACE,
           'keyEnter': pygame.K_RETURN, 'keyEscape': pygame.K_ESCAPE}
controls = {'keyW': False, 'keyA': False, 'keyS': False, 'keyD': False, 'keySpace': False, 'keyEnter': False,
            'keyEscape': False}


def listen(event):
    if event.type == pygame.KEYDOWN:
        for p in presets:
            if event.key == presets[p]:
                controls[p] = True
    elif event.type == pygame.KEYUP:
        for p in presets:
            if event.key == presets[p]:
                controls[p] = False

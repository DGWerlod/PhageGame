import pygame

pygame.init()

controls = {'pos': pygame.mouse.get_pos(),
            'click': False,
            'held': False}


def listen():
    controls['pos'] = pygame.mouse.get_pos()
    info = pygame.mouse.get_pressed()
    if info[0] and not controls['held']:
        controls['click'] = True
        controls['held'] = True
    elif info[0] and controls['held']:
        controls['click'] = False
    elif not info[0]:
        controls['click'] = False
        controls['held'] = False

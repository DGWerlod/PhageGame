import pygame

pygame.init()

controls = {'pos': pygame.mouse.get_pos(),
            'click': 0,
            'held': 0}


def listen():
    controls['pos'] = pygame.mouse.get_pos()
    info = pygame.mouse.get_pressed()
    if info[0] == 1 and controls['held'] == 0:
        controls['click'] = 1
        controls['held'] = 1
    elif info[0] == 1 and controls['held'] == 1:
        controls['click'] = 0
    elif info[0] == 0:
        controls['click'] = 0
        controls['held'] = 0

import pygame

pygame.init()

presets = {
    pygame.K_w: 'key_w',
    pygame.K_a: 'key_a',
    pygame.K_s: 'key_s',
    pygame.K_d: 'key_d',
    pygame.K_SPACE: 'key_space',
    pygame.K_RETURN: 'key_enter',
    pygame.K_ESCAPE: 'key_escape'
}
controls = {
    'pressed': {
        'key_w': False,
        'key_a': False,
        'key_s': False,
        'key_d': False,
        'key_space': False,
        'key_enter': False,
        'key_escape': False
    },
    'held': {
        'key_w': False,
        'key_a': False,
        'key_s': False,
        'key_d': False,
        'key_space': False,
        'key_enter': False,
        'key_escape': False
    }
}


def new_frame():
    for key in controls['pressed']:
        controls['pressed'][key] = False


def listen(event):
    if event.type == pygame.KEYDOWN:
        if event.key in presets:
            controls['pressed'][presets[event.key]] = True
            controls['held'][presets[event.key]] = True
    elif event.type == pygame.KEYUP:
        if event.key in presets:
            controls['held'][presets[event.key]] = False

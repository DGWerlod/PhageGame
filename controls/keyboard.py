import pygame

pygame.init()

presets = {'key_w': pygame.K_w,
           'key_a': pygame.K_a,
           'key_s': pygame.K_s,
           'key_d': pygame.K_d,
           'key_space': pygame.K_SPACE,
           'key_enter': pygame.K_RETURN,
           'key_escape': pygame.K_ESCAPE}
controls = {'key_w': False,
            'key_a': False,
            'key_s': False,
            'key_d': False,
            'key_space': False,
            'key_enter': False,
            'key_escape': False}


def listen(event):
    if event.type == pygame.KEYDOWN:
        for p in presets:
            if event.key == presets[p]:
                controls[p] = True
    elif event.type == pygame.KEYUP:
        for p in presets:
            if event.key == presets[p]:
                controls[p] = False

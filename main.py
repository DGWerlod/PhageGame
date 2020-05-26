import pygame
from pygame.locals import *

from controls import keyboard, mouse

flags = DOUBLEBUF

pygame.init()

window = pygame.display.set_mode((400, 400), flags)
window.set_alpha(None)
pygame.display.set_caption("PhageGame")
clock = pygame.time.Clock()


def listen():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        else:
            keyboard.listen(event)
            mouse.listen()
    return True


def main():

    running = True

    while running:

        running = listen()

        # Update Window
        pygame.display.update()
        clock.tick(30)

    pygame.quit()


main()

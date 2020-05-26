import pygame

from pygame.locals import *

flags = DOUBLEBUF

pygame.init()

window = pygame.display.set_mode((400, 400), flags)
window.set_alpha(None)
pygame.display.set_caption("PhageGame")
clock = pygame.time.Clock()


def main():
    while True:
        # Update Window
        pygame.display.update()
        clock.tick(30)

    pygame.quit()


main()

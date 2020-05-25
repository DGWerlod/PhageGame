import pygame

from pygame.locals import *

flags = DOUBLEBUF

pygame.init()

ctx = pygame.display.set_mode((400, 400), flags)
ctx.set_alpha(None)
pygame.display.set_caption("PhageGame")
clock = pygame.time.Clock()


def main():
    while True:
        # Update Window
        pygame.display.update()
        clock.tick(30)

    pygame.quit()


main()

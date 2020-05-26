import pygame
from pygame.locals import *

import constants
from logic import collisions
from controls import keyboard, mouse

from entities.base import Base
from entities.wall import Wall
from entities.buttons.summoner import Summoner
from entities.macrophages.macrophage import Macrophage
from entities.bacteriophages.bacteriophage import Bacteriophage


flags = DOUBLEBUF

pygame.init()

window = pygame.display.set_mode((500, 500), flags)
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


def get_microbe_in_front(microbes, base_is_at_left):
    in_front = None
    in_front_x = 0
    for m in microbes:
        m_x = m.get_rect().X
        rightmost = m_x > in_front_x and base_is_at_left
        leftmost = m_x < in_front_x and not base_is_at_left
        if in_front is None or leftmost or rightmost:
            in_front = m
            in_front_x = m_x
    return in_front


def main():

    macrophage_side = constants.LEFT

    macrophages = set()
    # macrophage_base = Base(500, 300, 100, constants.MACROPHAGE_SIDE)
    # macrophage_walls = [Wall(50, 300, 100, constants.MACROPHAGE_SIDE, 3),
    #                     Wall(150, 300, 100, constants.MACROPHAGE_SIDE, 2),
    #                     Wall(250, 300, 100, constants.MACROPHAGE_SIDE, 1)]
    # macrophage_summoner = Summoner(0, 0, 100, 100, constants.MACROPHAGE_SIDE)

    bacteriophages = set()
    # bacteriophage_base = Base(0, 300, 100, constants.BACTERIOPHAGE_SIDE)
    # macrophage_walls = [Wall(50, 300, 100, constants.BACTERIOPHAGE_SIDE, 3),
    #                     Wall(150, 300, 100, constants.BACTERIOPHAGE_SIDE, 2),
    #                     Wall(250, 300, 100, constants.BACTERIOPHAGE_SIDE, 1)]
    # bacteriophage_summoner = Summoner(0, 100, 100, 100, constants.BACTERIOPHAGE_SIDE)

    bacteriophages.add(Bacteriophage(0, 0, 125, 125, 5, 1, 1, "buffteriophage"))

    running = True

    while running:

        window.fill(constants.BLUE)

        # if collisions.rect_point(macrophage_summoner.get_rect(), mouse.controls['pos']):
        #     macrophages.add(Macrophage())
        # elif collisions.rect_point(bacteriophage_summoner.get_rect(), mouse.controls['pos']):
        #     bacteriophages.add(Bacteriophage())

        # macrophage_summoner.go(window)
        # bacteriophage_summoner.go(window)

        for m in macrophages:
            in_front = get_microbe_in_front(bacteriophages, constants.BACTERIOPHAGE_SIDE)
            m.go(window, in_front)
            if in_front and not in_front.is_alive():
                bacteriophages.remove(in_front)
        for b in bacteriophages:
            in_front = get_microbe_in_front(macrophages, macrophage_side)
            b.go(window, in_front)
            if in_front and not in_front.is_alive():
                macrophages.remove(in_front)
            if keyboard.controls['key_w'] and not keyboard.controls['key_s']:
                b._spd = max(1, b._spd - 1)
            if keyboard.controls['key_s'] and not keyboard.controls['key_w']:
                b._spd = min(15, b._spd + 1)

        # Update Window
        pygame.display.update()
        clock.tick(30)

        running = listen()

    pygame.quit()


main()

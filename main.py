import pygame
from pygame.locals import *

import constants
from logic import collisions
from controls import keyboard, mouse
from entities.bacteriophages.bacteriophage import Bacteriophage

# from entities.bacteriophages.bacteriophage import Bacteriophage
# from entities.macrophages.macrophage import Macrophage
# from entities.buttons.summoner import Summoner

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

    macrophage_side = constants.RIGHT

    macrophages = set()
    # macrophage_base = Base()
    # macrophage_walls = [Wall(), Wall(), Wall()]
    # macrophage_summoner = Summoner()

    bacteriophages = set()
    # bacteriophage_base = Base()
    # bacteriophage_walls = [Wall(), Wall(), Wall()]
    # bacteriophage_summoner = Summoner()

    bacteriophages.add(Bacteriophage(0,0,125,125,5,1,1,"buffteriophage"))

    running = True

    while running:

        window.fill(constants.BLUE)

        # if collisions.rect_point(macrophage_summoner.get_rect(), mouse.controls['pos']):
        #     macrophages.add(Macrophage())
        # elif collisions.rect_point(bacteriophage_summoner.get_rect(), mouse.controls['pos']):
        #     bacteriophages.add(Bacteriophage())

        for m in macrophages:
            in_front = get_microbe_in_front(bacteriophages, not macrophage_side)
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

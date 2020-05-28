import pygame
from pygame.locals import *

import constants
from entities.buildings.base import Base
from entities.buildings.wall import Wall
from logic import collisions
from controls import keyboard, mouse

from entities.buttons.summoner import Summoner
from entities.bacteriophages.b_basic import B_Basic
from entities.macrophages.m_basic import M_Basic
from dice.dice import Dice, Crit_Dice

flags = DOUBLEBUF

pygame.init()

window = pygame.display.set_mode((constants.GAME_WIDTH, constants.GAME_HEIGHT), flags)
window.set_alpha(None)
pygame.display.set_caption("PhageGame")
pygame.mouse.set_cursor(*pygame.cursors.diamond)
clock = pygame.time.Clock()


def listen():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        else:
            keyboard.listen(event)
    mouse.listen()
    return True


def first_in_front_of_second(first, second, base_is_at_left):
    if second is None:
        return True
    first_x = first.get_rect().X
    second_x = second.get_rect().X
    rightmost = first_x > second_x and base_is_at_left
    leftmost = first_x < second_x and not base_is_at_left
    if leftmost or rightmost:
        return True
    return False


def get_subject_in_front(microbes, walls, base, base_is_at_left):
    in_front = None
    for w in walls:
        if first_in_front_of_second(w, in_front, base_is_at_left):
            in_front = w
    for m in microbes:
        if first_in_front_of_second(m, in_front, base_is_at_left):
            in_front = m
    # if first_in_front_of_second(base, in_front, base_is_at_left):
    #     in_front = base

    return in_front


def main():
    macrophages = set()
    macrophage_base = None  # Base(500, 300, 100, constants.MACROPHAGE_SIDE)
    macrophage_walls = [
        # Wall(50, 300, 100, constants.MACROPHAGE_SIDE, 3),
        # Wall(150, 300, 100, constants.MACROPHAGE_SIDE, 2),
        # Wall(250, 300, 100, constants.MACROPHAGE_SIDE, 1)
    ]
    macrophage_summoner = Summoner(0, constants.GAME_HEIGHT // 4 * 3, 125, 125, constants.MACROPHAGE_SIDE)

    bacteriophages = set()
    bacteriophage_base = None  # Base(0, 300, 100, constants.BACTERIOPHAGE_SIDE)
    bacteriophage_walls = [
        # Wall(50, 300, 100, constants.BACTERIOPHAGE_SIDE, 3),
        # Wall(150, 300, 100, constants.BACTERIOPHAGE_SIDE, 2),
        # Wall(250, 300, 100, constants.BACTERIOPHAGE_SIDE, 1)
    ]
    bacteriophage_summoner = Summoner(constants.GAME_WIDTH - 125, constants.GAME_HEIGHT // 4 * 3,
                                      125, 125, constants.BACTERIOPHAGE_SIDE)

    macrophages.add(M_Basic())
    bacteriophages.add(B_Basic())

    running = True

    while running:

        window.fill(constants.BLUE)

        if mouse.controls['click']:
            if macrophage_summoner.can_summon():
                if collisions.rect_point(macrophage_summoner.get_rect(), mouse.controls['pos']):
                    macrophage_summoner.do_summon()
                    macrophages.add(M_Basic())
            if bacteriophage_summoner.can_summon():
                if collisions.rect_point(bacteriophage_summoner.get_rect(), mouse.controls['pos']):
                    bacteriophage_summoner.do_summon()
                    bacteriophages.add(B_Basic())

        macrophage_summoner.go(window)
        bacteriophage_summoner.go(window)

        for m in macrophages:
            in_front = get_subject_in_front(bacteriophages, bacteriophage_walls,
                                            bacteriophage_base, constants.BACTERIOPHAGE_SIDE)
            m.set_in_front(in_front)
            m.go(window)
            if in_front and not in_front.is_alive():
                bacteriophages.remove(in_front)
        for b in bacteriophages:
            in_front = get_subject_in_front(macrophages, macrophage_walls,
                                            macrophage_base, constants.MACROPHAGE_SIDE)
            b.set_in_front(in_front)
            b.go(window)
            if in_front and not in_front.is_alive():
                macrophages.remove(in_front)

            # here be jankiness
            # cha cha real smooth
            if keyboard.controls['key_w'] and not keyboard.controls['key_s']:
                # noinspection PyProtectedMember
                b._animation_spd = max(1, b._animation_spd - 1)
            if keyboard.controls['key_s'] and not keyboard.controls['key_w']:
                # noinspection PyProtectedMember
                b._animation_spd = min(15, b._animation_spd + 1)

        # debugging visuals
        pygame.draw.line(window, (0, 255, 0), (0, constants.GAME_HEIGHT // 4),
                         (constants.GAME_WIDTH, constants.GAME_HEIGHT // 4), 3)
        pygame.draw.line(window, (0, 255, 0), (0, constants.GAME_HEIGHT // 4 * 3),
                         (constants.GAME_WIDTH, constants.GAME_HEIGHT // 4 * 3), 3)
        pygame.draw.rect(window, (255, 0, 255), pygame.Rect(700, constants.GAME_HEIGHT // 2, 100, 125))

        # Update Window
        pygame.display.update()
        clock.tick(30)

        running = listen()

    pygame.quit()


main()

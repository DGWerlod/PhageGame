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
# from dice.dice import Dice, Crit_Dice

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
    output = False
    if base_is_at_left:
        first_w = first.get_rect().W
        second_w = second.get_rect().W
        output = first_x + first_w > second_x + second_w
    elif not base_is_at_left:
        output = first_x < second_x
    else:
        ValueError("Invalid input for parameter base_is_at_left.")
    return output


def get_subject_in_front(microbes, walls, base, base_is_at_left):
    in_front = None
    for w in walls:
        if first_in_front_of_second(w, in_front, base_is_at_left):
            in_front = w
    for m in microbes:
        if first_in_front_of_second(m, in_front, base_is_at_left):
            in_front = m
    if first_in_front_of_second(base, in_front, base_is_at_left):
        in_front = base

    return in_front


def main():
    macrophages = set()
    macrophage_base = Base(constants.GAME_WIDTH // 2 - 550 - 50, 100, constants.MACROPHAGE_SIDE)
    macrophage_walls = [
        Wall(constants.GAME_WIDTH // 2 - 400 - 15, 100, constants.MACROPHAGE_SIDE, 3),
        Wall(constants.GAME_WIDTH // 2 - 275 - 15, 100, constants.MACROPHAGE_SIDE, 2),
        Wall(constants.GAME_WIDTH // 2 - 150 - 15, 100, constants.MACROPHAGE_SIDE, 1)
    ]
    macrophage_summoner = Summoner(0, constants.GAME_HEIGHT // 4 * 3, 125, 125, constants.MACROPHAGE_SIDE)

    bacteriophages = set()
    bacteriophage_base = Base(constants.GAME_WIDTH // 2 + 550 - 50, 100, constants.BACTERIOPHAGE_SIDE)
    bacteriophage_walls = [
        Wall(constants.GAME_WIDTH // 2 + 400 - 15, 100, constants.BACTERIOPHAGE_SIDE, 3),
        Wall(constants.GAME_WIDTH // 2 + 275 - 15, 100, constants.BACTERIOPHAGE_SIDE, 2),
        Wall(constants.GAME_WIDTH // 2 + 150 - 15, 100, constants.BACTERIOPHAGE_SIDE, 1)
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

        macrophages_remaining = set()
        for m in macrophages:
            in_front = get_subject_in_front(bacteriophages, bacteriophage_walls,
                                            bacteriophage_base, constants.BACTERIOPHAGE_SIDE)
            m.set_in_front(in_front)
            m.go(window)
            if m.is_alive() and m.get_rect().X < constants.GAME_WIDTH:
                macrophages_remaining.add(m)
        macrophages = macrophages_remaining

        bacteriophages_remaining = set()
        for b in bacteriophages:
            in_front = get_subject_in_front(macrophages, macrophage_walls,
                                            macrophage_base, constants.MACROPHAGE_SIDE)
            b.set_in_front(in_front)
            b.go(window)
            b_rect = b.get_rect()
            if b.is_alive() and b_rect.X - b_rect.W > 0:
                bacteriophages_remaining.add(b)
        bacteriophages = bacteriophages_remaining

        macrophage_walls_remaining = []
        for m_w in macrophage_walls:
            if m_w.is_alive():
                macrophage_walls_remaining.append(m_w)
                m_w.go(window)
        macrophage_walls = macrophage_walls_remaining

        bacteriophage_walls_remaining = []
        for b_w in bacteriophage_walls:
            if b_w.is_alive():
                bacteriophage_walls_remaining.append(b_w)
                b_w.go(window)
        bacteriophage_walls = bacteriophage_walls_remaining

        if macrophage_base.is_alive():
            macrophage_base.go(window)
        if bacteriophage_base.is_alive():
            bacteriophage_base.go(window)

        # debugging visuals
        pygame.draw.line(window, (0, 255, 0), (0, constants.GAME_HEIGHT // 4),
                         (constants.GAME_WIDTH, constants.GAME_HEIGHT // 4), 3)
        pygame.draw.line(window, (0, 255, 0), (0, constants.GAME_HEIGHT // 4 * 3),
                         (constants.GAME_WIDTH, constants.GAME_HEIGHT // 4 * 3), 3)
        pygame.draw.line(window, constants.YELLOW, (constants.GAME_WIDTH // 2, 0),
                         (constants.GAME_WIDTH // 2, constants.GAME_HEIGHT), 3)
        # pygame.draw.rect(window, (255, 0, 255), pygame.Rect(700, constants.GAME_HEIGHT // 2, 100, 125))

        # Update Window
        pygame.display.update()
        clock.tick(30)

        running = listen()

    pygame.quit()


main()

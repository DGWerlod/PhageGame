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


def draw_debug_visuals():
    pygame.draw.line(window, constants.YELLOW, (0, constants.GAME_HEIGHT // 4),
                     (constants.GAME_WIDTH, constants.GAME_HEIGHT // 4), 3)
    pygame.draw.line(window, constants.YELLOW, (0, constants.GAME_HEIGHT // 4 * 3),
                     (constants.GAME_WIDTH, constants.GAME_HEIGHT // 4 * 3), 3)
    pygame.draw.line(window, constants.YELLOW, (constants.GAME_WIDTH // 2, 0),
                     (constants.GAME_WIDTH // 2, constants.GAME_HEIGHT), 3)
    pygame.draw.rect(window, constants.MAGENTA, pygame.Rect(constants.GAME_WIDTH // 2 - 50,
                                                            constants.GAME_HEIGHT // 2, 100, 125))


def microbe_actions(now, enemies, enemy_walls, enemy_base, enemy_side):
    now_remaining = set()
    for n in now:
        in_front = get_subject_in_front(enemies, enemy_walls, enemy_base, enemy_side)
        n.set_in_front(in_front)
        n.go(window)
        if not enemy_side:  # now are macrophages
            on_screen = n.get_rect().X < constants.GAME_WIDTH
        elif enemy_side:  # now are bacteriophages
            n_rect = n.get_rect()
            on_screen = n_rect.X + n_rect.W > 0
        else:
            raise ValueError("Unrecognized enemy_side.")
        if n.is_alive() and on_screen:
            now_remaining.add(n)
    return now_remaining


def wall_actions(walls):
    walls_remaining = []
    for w in walls:
        if w.is_alive():
            walls_remaining.append(w)
            w.go(window)
    return walls_remaining


def main():

    macrophages = set()
    macrophages.add(M_Basic())
    macrophage_base = Base(constants.MACROPHAGE_SIDE)
    macrophage_walls = [
        Wall(constants.MACROPHAGE_SIDE, 3),
        Wall(constants.MACROPHAGE_SIDE, 2),
        Wall(constants.MACROPHAGE_SIDE, 1)
    ]
    macrophage_summoner = Summoner(0, constants.GAME_HEIGHT // 4 * 3, 125, 125, constants.MACROPHAGE_SIDE)

    bacteriophages = set()
    bacteriophages.add(B_Basic())
    bacteriophage_base = Base(constants.BACTERIOPHAGE_SIDE)
    bacteriophage_walls = [
        Wall(constants.BACTERIOPHAGE_SIDE, 3),
        Wall(constants.BACTERIOPHAGE_SIDE, 2),
        Wall(constants.BACTERIOPHAGE_SIDE, 1)
    ]
    bacteriophage_summoner = Summoner(constants.GAME_WIDTH - 125, constants.GAME_HEIGHT // 4 * 3,
                                      125, 125, constants.BACTERIOPHAGE_SIDE)

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

        if macrophage_base.is_alive():
            macrophage_base.go(window)
        if bacteriophage_base.is_alive():
            bacteriophage_base.go(window)

        macrophage_walls = wall_actions(macrophage_walls)
        bacteriophage_walls = wall_actions(bacteriophage_walls)

        macrophages = microbe_actions(macrophages, bacteriophages, bacteriophage_walls,
                                      bacteriophage_base, constants.BACTERIOPHAGE_SIDE)
        bacteriophages = microbe_actions(bacteriophages, macrophages, macrophage_walls,
                                         macrophage_base, constants.MACROPHAGE_SIDE)

        draw_debug_visuals()

        # Update Window
        pygame.display.update()
        clock.tick(30)

        running = listen()

    pygame.quit()


main()

import constants


def is_on_screen(allegiant_entity):
    allegiance = allegiant_entity.get_allegiance()
    if allegiance:  # on macrophage side
        on_screen = allegiant_entity.get_rect().X < constants.GAME_WIDTH
    else:  # on bacteriophage side
        p_rect = allegiant_entity.get_rect()
        on_screen = p_rect.X + p_rect.W > 0
    return on_screen


def _first_in_front_of_second(first, second, base_is_at_left):
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


def get_mortal_in_front(mortals, microbes_index, walls_index, base_index):
    base_is_at_left = mortals[base_index].get_allegiance()  # there's always a base
    in_front = None
    for w in mortals[walls_index]:
        if _first_in_front_of_second(w, in_front, base_is_at_left):
            in_front = w
    for m in mortals[microbes_index]:
        if _first_in_front_of_second(m, in_front, base_is_at_left):
            in_front = m
    if _first_in_front_of_second(mortals[base_index], in_front, base_is_at_left):
        in_front = mortals[base_index]
    return in_front

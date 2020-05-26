from math import hypot


def rect_point(rect, point):
    if rect.X < point[0]:
        if rect.X + rect.W > point[0]:
            if rect.Y < point[1]:
                if rect.H + rect.Y > point[1]:
                    return True
    return False


def rectangles(a, b):  # exception is for player's rBall addition
    if a.X < b.X + b.W:
        if a.X + a.W > b.X:
            if a.Y < b.Y + b.H:
                if a.H + a.Y > b.Y:
                    dx = abs((a.X + a.W / 2) - (b.X + b.W / 2)) / b.W
                    dy = abs((a.Y + a.H / 2) - (b.Y + b.H / 2)) / b.H
                    if dy < dx:
                        return 1
                    else:
                        return 2
    return 0


def circles(a, b):
    # if distance between their centers is less than the sum of their radii
    dx = abs(a.X - b.X)
    dy = abs(a.Y - b.Y)
    dt = hypot(dx, dy)
    if dt < a.R + b.R:
        return True
    return False


def circle_rect(circle, rect):
    # get x and y distance from their centers
    dx = abs(circle.X - rect.X - rect.W / 2)
    dy = abs(circle.Y - rect.Y - rect.H / 2)
    dx_min = abs(rect.W / 2) + circle.R
    dy_min = abs(rect.H / 2) + circle.R

    # test collision, return false if not colliding
    if dx > dx_min:
        return False
    elif dy > dy_min:
        return False
    # elif dx <= rect.W / 2: return True
    # elif dy <= rect.H / 2: return True

    # find bounce direction, return associated number
    if dy / rect.H < dx / rect.W:  # ratios dissociate from unequal sides of rectangles
        if dx + abs(circle.spd[0]) <= dx_min:  # if this function would return true next tick
            return 3  # flip both directions
        else:
            return 1  # flip x direction
    else:  # dx / rect.W < dy / rect.H:
        if dy + abs(circle.spd[1]) <= dy_min:
            return 3  # flip both directions
        else:
            return 2  # flip y direction

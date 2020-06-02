from levels.level_one import Level_One


def build_level(level_number):
    if level_number == 1:
        return Level_One()
    else:
        raise ValueError("Invalid level number passed to factory build_level()")

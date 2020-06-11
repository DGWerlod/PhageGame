from levels.level_one import Level_One


def build_level(level_number, use_ai):
    if level_number == 1:
        return Level_One(use_ai)
    else:
        raise ValueError("Invalid level number passed to factory build_level()")

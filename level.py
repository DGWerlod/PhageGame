POSSIBLE_UPGRADES = set()


class Level(object):
    def __init__(self, microbes_available, upgrades_enabled):
        self._microbes_available = microbes_available
        self._upgrades_enabled = upgrades_enabled

import constants

# THESE ARE VALUES THAT CAN BE ADJUSTED BY UPGRADES AND FINE-TUNED BY US

microbe_speeds = {
    constants.B_BASIC: 7,
    constants.B_PULT: 7,
    constants.B_TANK: 5,
    constants.M_BASIC: 6,
    constants.M_BEACH: 5
}

microbe_hit_points = {
    constants.B_BASIC: 100,
    constants.B_PULT: 20,
    constants.B_TANK: 200,
    constants.M_BASIC: 100,
    constants.M_BEACH: 150
}

microbe_damages = {
    constants.B_BASIC: 9,
    constants.B_PULT: 0,  # projectiles
    constants.B_TANK: 10,
    constants.M_BASIC: 13,
    constants.M_BEACH: 17
}

microbe_projectile_damages = {
    # just using a die roll for our one projectile-based microbe right now
}

summoner_cooldowns = {
    constants.B_BASIC: 33,
    constants.B_PULT: 30,
    constants.B_TANK: 67,
    constants.M_BASIC: 33,
    constants.M_BEACH: 50
}

wall_hit_points = {
    constants.MACROPHAGE_SIDE: 100,
    constants.BACTERIOPHAGE_SIDE: 100
}

base_hit_points = {
    constants.MACROPHAGE_SIDE: 150,
    constants.BACTERIOPHAGE_SIDE: 150
}

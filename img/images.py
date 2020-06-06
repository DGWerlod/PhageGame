import pygame.image

import constants

IMAGES = {
    "buffteriophage": {
        "walk": [
            pygame.transform.scale(pygame.image.load("img/buffteriophage/frame1.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/buffteriophage/frame2.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/buffteriophage/frame3.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/buffteriophage/frame4.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/buffteriophage/frame5.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/buffteriophage/frame6.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/buffteriophage/frame7.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/buffteriophage/frame8.png"), (125, 125))
        ],
        "attack": [
            pygame.transform.scale(pygame.image.load("img/buffteriophage/frameS3.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/buffteriophage/frameS2.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/buffteriophage/frameS1.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/buffteriophage/frameS1.png"), (125, 125))
        ],
        "static": [
            pygame.transform.scale(pygame.image.load("img/buffteriophage/frame3.png"), (125, 125))
        ]
    },
    "tankphage": {
        "walk": [
            pygame.transform.scale(pygame.image.load("img/tankphage/1 copy.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/tankphage/2 copy.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/tankphage/3 copy.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/tankphage/4 copy.png"), (125, 125))
        ],
        "attack": [
            pygame.transform.scale(pygame.image.load("img/tankphage/frameA1.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/tankphage/frameA2.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/tankphage/frameA3.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/tankphage/frameA3.png"), (125, 125))
        ],
        "static": [
            pygame.transform.scale(pygame.image.load("img/tankphage/frame1.png"), (125, 125))
        ]
    },
    "macrophoot": {
        "walk": [
            pygame.transform.scale(pygame.image.load("img/macrophoot/frame1.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/macrophoot/frame2.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/macrophoot/frame3.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/macrophoot/frame4.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/macrophoot/frame5.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/macrophoot/frame6.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/macrophoot/frame7.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/macrophoot/frame8.png"), (125, 125))
        ],
        "attack": [
            pygame.transform.scale(pygame.image.load("img/macrophoot/frameA1.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/macrophoot/frameA2.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/macrophoot/frameA3.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/macrophoot/frameA4.png"), (125, 125))
        ],
        "static": [
            pygame.transform.scale(pygame.image.load("img/macrophoot/frame1.png"), (125, 125))
        ]
    },
    "macrobeach": {
        "walk": [
            pygame.transform.scale(pygame.image.load("img/macrobeach/frame1.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/macrobeach/frame2.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/macrobeach/frame3.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/macrobeach/frame4.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/macrobeach/frame5.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/macrobeach/frame6.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/macrobeach/frame7.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/macrobeach/frame8.png"), (125, 125))
        ],
        "attack": [
            pygame.transform.scale(pygame.image.load("img/macrobeach/frameA1.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/macrobeach/frameA2.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/macrobeach/frameA3.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/macrobeach/frameA3.png"), (125, 125))
        ],
        "static": [
            pygame.transform.scale(pygame.image.load("img/macrobeach/frame1.png"), (125, 125))
        ]
    },
    constants.M_BASIC + "_summoner": {
        "active": [
            pygame.image.load("img/buttons/summoners/footbutton.png")
        ],
        "inactive": [
            pygame.image.load("img/buttons/summoners/footbutton-inactive.png")
        ]
    },
    constants.B_BASIC + "_summoner": {
        "active": [
            pygame.image.load("img/buttons/summoners/buffbutton.png")
        ],
        "inactive": [
            pygame.image.load("img/buttons/summoners/buffbutton-inactive.png")
        ]
    },
    constants.B_TANK + "_summoner": {
        "active": [
            pygame.image.load("img/buttons/summoners/tankbutton.png")
        ],
        "inactive": [
            pygame.image.load("img/buttons/summoners/tankbutton-inactive.png")
        ]
    },
    constants.M_BEACH + "_summoner": {
        "active": [
            pygame.image.load("img/buttons/summoners/beachbutton.png")
        ],
        "inactive": [
            pygame.image.load("img/buttons/summoners/beachbutton-inactive.png")
        ]
    },
    "macrophage_wall": {
        "static": [
            pygame.transform.scale(pygame.image.load("img/walls/cellswall.png"), (90, constants.GAME_HEIGHT // 8 * 3))
        ]
    },
    "bacteriophage_wall": {
        "static": [
            pygame.transform.scale(pygame.image.load("img/walls/viralwall.png"), (90, constants.GAME_HEIGHT // 8 * 3))
        ]
    },
    "macrophage_base": {
        "static": [
            pygame.transform.scale(pygame.image.load("img/walls/foottower.png"), (100, constants.GAME_HEIGHT // 2))
        ]
    },
    "bacteriophage_base": {
        "static": [
            pygame.transform.scale(pygame.image.load("img/walls/handbase.png"), (100, constants.GAME_HEIGHT // 2))
        ]
    },
    "level": {
        "background": [
            pygame.transform.scale(pygame.image.load("img/levels/bloodbackground.png"),
                                   (constants.GAME_WIDTH, constants.GAME_HEIGHT))
        ]
    },
    "action": {
        "pause": [
            pygame.transform.scale(pygame.image.load("img/buttons/system/pause.png"), (125, 125))
        ],
        "play": [
            pygame.transform.scale(pygame.image.load("img/buttons/system/play.png"), (125, 125))
        ]
    },
    "music": {
        "audible": [
            pygame.transform.scale(pygame.image.load("img/buttons/system/audible.png"), (125, 125))
        ],
        "muted": [
            pygame.transform.scale(pygame.image.load("img/buttons/system/muted.png"), (125, 125))
        ]
    },
    "back": {
        "back": [
            pygame.transform.scale(pygame.image.load("img/buttons/system/back.png"), (125, 125))
        ]
    }
}

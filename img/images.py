import pygame.image

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
            pygame.transform.scale(pygame.image.load("img/buffteriophage/frameS2.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/buffteriophage/frameS3.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/buffteriophage/frameS1.png"), (125, 125)),
            pygame.transform.scale(pygame.image.load("img/buffteriophage/frameS3.png"), (125, 125))
        ],
        "static": [
            pygame.transform.scale(pygame.image.load("img/buffteriophage/frame3.png"), (125, 125))
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
    "macrophage_summoner": {
        "active": [
            pygame.image.load("img/buttons/footbutton.png")
        ],
        "inactive": [
            pygame.image.load("img/buttons/footbutton.png")
        ]
    },
    "bacteriophage_summoner": {
        "active": [
            pygame.image.load("img/buttons/buffbutton.png")
        ],
        "inactive": [
            pygame.image.load("img/buttons/buffbutton.png")
        ]
    },
}

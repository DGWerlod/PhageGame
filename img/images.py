import pygame.image

IMAGES = {
    "buffteriophage": {"walk":  [pygame.image.load("img/buffteriophage/frame1.png"),
                                 pygame.image.load("img/buffteriophage/frame2.png"),
                                 pygame.image.load("img/buffteriophage/frame3.png"),
                                 pygame.image.load("img/buffteriophage/frame4.png"),
                                 pygame.image.load("img/buffteriophage/frame5.png"),
                                 pygame.image.load("img/buffteriophage/frame6.png"),
                                 pygame.image.load("img/buffteriophage/frame7.png"),
                                 pygame.image.load("img/buffteriophage/frame8.png")],
                       "static": [pygame.image.load("img/buffteriophage/frame3.png")]
                       },
    "macrophoot": {"walk": [pygame.image.load("img/macrophoot/frame1.png"),
                            pygame.image.load("img/macrophoot/frame2.png"),
                            pygame.image.load("img/macrophoot/frame3.png"),
                            pygame.image.load("img/macrophoot/frame4.png"),
                            pygame.image.load("img/macrophoot/frame5.png"),
                            pygame.image.load("img/macrophoot/frame6.png"),
                            pygame.image.load("img/macrophoot/frame7.png"),
                            pygame.image.load("img/macrophoot/frame8.png")],
                   "static": [pygame.image.load("img/macrophoot/frame1.png")]
                   },
    "macrophage_summoner":    {"active": [pygame.image.load("img/buttons/footbutton.png")],
                               "inactive": [pygame.image.load("img/buttons/footbutton.png")]},
    "bacteriophage_summoner": {"active": [pygame.image.load("img/buttons/buffbutton.png")],
                               "inactive": [pygame.image.load("img/buttons/buffbutton.png")]},
}

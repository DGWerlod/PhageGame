import pygame
pygame.mixer.init()

splash_shift_time = 12.852 + 0.3  # seconds
overture_loop_time = 25.650  # seconds
END_FLAG = pygame.USEREVENT + 1  # ensures that this flag != any preset one

pygame.mixer.music.load("sound/overture.ogg")
# noinspection PyArgumentList
pygame.mixer.music.set_endevent(END_FLAG)


def start_music():
    pygame.mixer.music.play()


def stop_music():
    pygame.mixer.music.pause()


def change_music(time, song=None):
    if song is not None:
        pygame.mixer.music.load("sound/overture.ogg")
    else:
        pygame.mixer.music.pause()
        pygame.mixer.music.rewind()
    pygame.mixer.music.play()
    pygame.mixer.music.set_pos(time)

import pygame
from functools import lru_cache
pygame.init()

@lru_cache(maxsize=10000)
def make_video(screen):

    _image_num = 0

    while True:
        _image_num += 1
        str_num = "000" + str(_image_num)
        file_name = "image" + str_num[-4:] + ".jpg"
        pygame.image.save(screen, file_name)
        yield

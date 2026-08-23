import pygame
from modules.hover import *
from modules.design import UP_DOWN



music=pygame.image.load("./asset/image/music/m.png")
sound=pygame.image.load("./asset/image/music/v.png")
base=pygame.image.load("./asset/image/music/base.png")
base = pygame.transform.flip(base, False, True)

x=1450
y=950
music=pygame.transform.smoothscale(music,(200,200))
sound=pygame.transform.smoothscale(sound,(200,200))
base=pygame.transform.smoothscale(base,(x,y))


def sound_screen(screen):
    current_width, current_height = screen.get_size()

    fx=x/2
    fy=y/2
    screen.blit(base,(current_width//2 - fx  ,current_height//2 -fy + 110))
    # screen.blit(music,(current_width//2 - 500 ,current_height//2 - 130 ))
    # screen.blit(sound,(current_width//2 - 500 ,current_height //2 + 200))

    UP_DOWN(
        screen,
        music,
        current_width//2 - 350 ,current_height//2 - 58
        )
    UP_DOWN(
        screen,
        sound,
        current_width//2 - 350 ,current_height //2 + 260
        )












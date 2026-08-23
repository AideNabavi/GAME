import pygame



image=pygame.image.load("./asset/image/button/donate.png")

image=pygame.transform.smoothscale(image,(500,500))

def _donate(screen):
    screen.bilt(image,(0,0))
    
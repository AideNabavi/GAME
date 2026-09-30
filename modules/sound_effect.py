import pygame

pygame.mixer.init()

from modules import sound
click_sound = pygame.mixer.Sound(
    "./asset/sound/4.mp3"
)

ON_OFF=1
def on_off_sound_effect(x):
    global ON_OFF
    if x == 1:
        ON_OFF = 1
    else:
        ON_OFF = 0

def play_click():

    if ON_OFF == 1:

        click_sound.set_volume(sound.sound_volume)
        click_sound.play()

    else:

        return 0
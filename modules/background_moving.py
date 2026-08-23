import pygame

original_background = pygame.image.load(
    "./asset/image/background_moving/1.jpg"
)

background = None

bg_x = 0
speed = 2


def load_background(screen):

    global background

    screen_height = screen.get_height()

    ratio = screen_height / original_background.get_height()

    new_width = int(
        original_background.get_width() * ratio
    )

    background = pygame.transform.smoothscale(
        original_background,
        (
            new_width,
            screen_height
        )
    )

    print(background.get_size())
    print(screen.get_size())


def draw_background(screen):

    global bg_x

    bg_x -= speed


    if bg_x <= -(original_background.get_width() - screen.get_width()):
        bg_x = 0


    screen.blit(
        background,
        (bg_x, 0)
    )
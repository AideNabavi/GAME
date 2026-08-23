import pygame


current_background = None
background_last_size = None
background_image = None



def set_background(image_path, size):

    global current_background
    global background_last_size
    global background_image


    background_image = pygame.image.load(
        image_path
    ).convert_alpha()


    current_background = pygame.transform.smoothscale(
        background_image,
        size
    )


    background_last_size = size





def update_background(size):

    global current_background
    global background_last_size


    if background_image and size != background_last_size:

        current_background = pygame.transform.smoothscale(
            background_image,
            size
        )

        background_last_size = size





def draw_background(screen):

    if current_background:

        screen.blit(
            current_background,
            (0, 0)
        )
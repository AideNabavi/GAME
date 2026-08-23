import pygame


def hover_image_for_time_screen(
    image,
    rect,
    mouse_pos,
    current_size
):

    NORMAL_SIZE = 200
    HOVER_SIZE = 220
    SPEED = 2


    if rect.collidepoint(mouse_pos):

        if current_size < HOVER_SIZE:
            current_size += SPEED

    else:

        if current_size > NORMAL_SIZE:
            current_size -= SPEED


    new_image = pygame.transform.smoothscale(
        image,
        (
            current_size,
            current_size
        )
    )
    
    new_rect = new_image.get_rect(
        center=rect.center
    )


    return new_image, new_rect, current_size


        
        
    
    
    
    
    
    
    
    
    
def hover_image(
    image,
    rect,
    mouse_pos,
    current_size
):

    NORMAL_SIZE = 90
    HOVER_SIZE = 120
    SPEED = 2


    if rect.collidepoint(mouse_pos):

        if current_size < HOVER_SIZE:
            current_size += SPEED

    else:

        if current_size > NORMAL_SIZE:
            current_size -= SPEED


    new_image = pygame.transform.smoothscale(
        image,
        (
            current_size,
            current_size
        )
    )


    new_rect = new_image.get_rect(
        center=rect.center
    )


    return new_image, new_rect, current_size

#--------------------------------------------

def hover_image_icon(
    image,
    rect,
    mouse_pos,
    current_size
):

    NORMAL_SIZE = 150
    HOVER_SIZE = 180
    SPEED = 2


    if rect.collidepoint(mouse_pos):

        if current_size < HOVER_SIZE:
            current_size += SPEED

    else:

        if current_size > NORMAL_SIZE:
            current_size -= SPEED


    new_image = pygame.transform.smoothscale(
        image,
        (
            current_size,
            current_size
        )
    )


    new_rect = new_image.get_rect(
        center=rect.center
    )


    return new_image, new_rect, current_size







#-----------------------------------
def hover_image_profile(
    image,
    rect,
    mouse_pos,
    current_size
):

    NORMAL_SIZE = 200
    HOVER_SIZE = 230
    SPEED = 5


    if rect.collidepoint(mouse_pos):

        if current_size < HOVER_SIZE:
            current_size += SPEED

    else:

        if current_size > NORMAL_SIZE:
            current_size -= SPEED


    new_image = pygame.transform.smoothscale(
        image,
        (
            current_size,
            current_size
        )
    )


    new_rect = new_image.get_rect(
        center=rect.center
    )


    return new_image, new_rect, current_size









#----------------------------------------------

def hover_sound_button(
    image,
    rect,
    mouse_pos,
    current_size
):

    NORMAL_SIZE = 190
    HOVER_SIZE = 210
    SPEED = 2


    if rect.collidepoint(mouse_pos):

        if current_size < HOVER_SIZE:
            current_size += SPEED

    else:

        if current_size > NORMAL_SIZE:
            current_size -= SPEED


    new_image = pygame.transform.smoothscale(
        image,
        (
            current_size,
            current_size
        )
    )


    new_rect = new_image.get_rect(
        center=rect.center
    )


    return new_image, new_rect, current_size

#----------------------------------------------

def hover_image_menu(
    image,
    rect,
    mouse_pos,
    current_size
):
    NORMAL_SIZE = 80
    HOVER_SIZE = 100
    SMOOTH = 0.2

    if rect.collidepoint(mouse_pos):
        target = HOVER_SIZE
    else:
        target = NORMAL_SIZE


    current_size += (
        target - current_size
    ) * SMOOTH


    new_image = pygame.transform.smoothscale(
        image,
        (
            int(rect.width * current_size / NORMAL_SIZE),
            int(rect.height * current_size / NORMAL_SIZE)
        )
    )


    new_rect = new_image.get_rect(
        center=rect.center
    )


    return new_image, new_rect, current_size








#----------------- language
def hover_image_lan(
    image,
    rect,
    mouse_pos,
    current_size
):
    NORMAL_SIZE = 250
    HOVER_SIZE = 300
    SMOOTH = 0.3

    if rect.collidepoint(mouse_pos):
        target = HOVER_SIZE
    else:
        target = NORMAL_SIZE


    current_size += (
        target - current_size
    ) * SMOOTH


    new_image = pygame.transform.smoothscale(
        image,
        (
            int(rect.width * current_size / NORMAL_SIZE),
            int(rect.height * current_size / NORMAL_SIZE)
        )
    )


    new_rect = new_image.get_rect(
        center=rect.center
    )


    return new_image, new_rect, current_size

















#-------------------------------

def hover_image_level(
    image,
    rect,
    mouse_pos,
    current_size
):
    NORMAL_SIZE = 350
    HOVER_SIZE = 400
    SMOOTH = 0.3

    if rect.collidepoint(mouse_pos):
        target = HOVER_SIZE
    else:
        target = NORMAL_SIZE


    current_size += (
        target - current_size
    ) * SMOOTH


    new_image = pygame.transform.smoothscale(
        image,
        (
            int(rect.width * current_size / NORMAL_SIZE),
            int(rect.height * current_size / NORMAL_SIZE)
        )
    )


    new_rect = new_image.get_rect(
        center=rect.center
    )


    return new_image, new_rect, current_size































#----------------------------------------------

def hover_image_music(
    image,
    rect,
    mouse_pos,
    current_size
):
    NORMAL_SIZE = 150
    HOVER_SIZE = 190
    SMOOTH = 0.3

    if rect.collidepoint(mouse_pos):
        target = HOVER_SIZE
    else:
        target = NORMAL_SIZE


    current_size += (
        target - current_size
    ) * SMOOTH


    new_image = pygame.transform.smoothscale(
        image,
        (
            int(rect.width * current_size / NORMAL_SIZE),
            int(rect.height * current_size / NORMAL_SIZE)
        )
    )


    new_rect = new_image.get_rect(
        center=rect.center
    )


    return new_image, new_rect, current_size




















#----------------------------------------------
def hover_bug_button(
    image,
    rect,
    mouse_pos,
    current_size
):

    NORMAL_SIZE = 50
    HOVER_SIZE = 80
    SPEED = 2


    if rect.collidepoint(mouse_pos):

        if current_size < HOVER_SIZE:
            current_size += SPEED

    else:

        if current_size > NORMAL_SIZE:
            current_size -= SPEED


    new_image = pygame.transform.smoothscale(
        image,
        (
            current_size,
            current_size
        )
    )


    new_rect = new_image.get_rect(
        center=rect.center
    )


    return new_image, new_rect, current_size



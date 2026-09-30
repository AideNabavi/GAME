import pygame

from modules.setting import draw_text_stroke
from modules.EFFECT.hover import *
rec_enter=None
def hover_image_firstpage(
    image,
    rect,
    mouse_pos,
    current_size
):

    NORMAL_SIZE = 200
    HOVER_SIZE = 230
    SPEED = 2

    if rect.collidepoint(mouse_pos):

        if current_size < HOVER_SIZE:
            current_size += SPEED

    else:

        if current_size > NORMAL_SIZE:
            current_size -= SPEED

    # اندازه اصلی تصویر
    original_width = image.get_width()
    original_height = image.get_height()

    # نسبت تصویر
    ratio = original_height / original_width

    width = current_size
    height = int(current_size * ratio)

    new_image = pygame.transform.smoothscale(
        image,
        (
            width,
            height
        )
    )

    new_rect = new_image.get_rect(
        center=rect.center
    )
    global rec_enter
    rec_enter=new_rect
    return new_image, new_rect, current_size




enter_size = 200

# ============================================================
# ENTER IMAGE - LOAD ONLY ONCE
# ============================================================

_enter_image = pygame.image.load(
    "./asset/image/enter.png"
).convert_alpha()


def draw_name_screen(
    screen,
    fonts,
    player_name,
    input_box,
    enter_button
):

    # ---------------- Input Box ----------------

    pygame.draw.rect(
        screen,
        (255, 255, 255),
        input_box,
        border_radius=10
    )

    pygame.draw.rect(
        screen,
        (0, 0, 0),
        input_box,
        2,
        border_radius=10
    )


    # ---------------- Player Name ----------------

    if player_name == "":

        name_text = fonts["name"].render(
            "Your Name",
            True,
            (170, 170, 170)
        )

    else:

        name_text = fonts["name"].render(
            player_name,
            True,
            (255, 220, 0)
        )


    name_rect = name_text.get_rect(
        center=input_box.center
    )


    # ---------------- Stroke ----------------

    if player_name != "":

        stroke = fonts["name"].render(
            player_name,
            True,
            (0, 0, 0)
        )

        draw_text_stroke(
            screen,
            stroke,
            name_rect.topleft
        )


    screen.blit(
        name_text,
        name_rect
    )


    # ---------------- Enter Button ----------------

    global enter_size

    mouse_pos = pygame.mouse.get_pos()

    enter_image, enter_rect, enter_size = hover_image_firstpage(
        _enter_image,
        enter_button,
        mouse_pos,
        enter_size
    )

    screen.blit(
        enter_image,
        enter_rect
    )









    
    
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
scren = None
logo = None



def draw_new_screen(screen):
    global scren
    global logo

    if scren is None:
        # scren = pygame.image.load(
        #     "./asset/image/back22_.png"
        # ).convert_alpha()
        logo = pygame.image.load(
            "./asset/image/logo.png"
        ).convert_alpha()

        # scren = pygame.transform.smoothscale(
        #     scren,
        #     (1200, 650)
        # )
        logo = pygame.transform.smoothscale(
            logo,
            (450, 450)
        )

    current_width, current_height = screen.get_size()

    # screen.blit(
    #     scren,
    #     (
    #         current_width // 2 - scren.get_width() // 2,
    #         current_height // 2 -160
    #     )
    # )
    screen.blit(
        logo,
        (
            current_width // 2 - logo.get_width() // 2,
            current_height // 2 - 666
        )
    )




# from modules.hover import hover_image
back_size = 150
from modules.EFFECT.hover import hover_image
back_image = pygame.image.load(
        "./asset/image/back1.png"
    )
def draw_back_button(
    screen,
    back_button_rect
):

    global back_size

    mouse_pos = pygame.mouse.get_pos()


    image, image_rect, back_size = hover_image_icon(
        back_image,
        back_button_rect,
        mouse_pos,
        back_size
    )


    screen.blit(
        image,
        image_rect
    )
    
    
    
    
    













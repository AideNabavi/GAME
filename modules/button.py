from modules.hover import *
import pygame
from modules.language import get_font, display_text


size = 200


#  برای داخل بازی است 
def in_game_button(
    screen,
    exit_button_rect,
    picture
):

    global size

    mouse_pos = pygame.mouse.get_pos()


    image, image_rect, size = hover_image_icon(
        picture,
        exit_button_rect,
        mouse_pos,
        size
    )


    screen.blit(
        image,
        image_rect
    )
    
#----------------------------------------------------------------------------------

support_b = pygame.image.load(
    "./asset/image/support.png"
)


support_size = 150



def support_button(
    screen,
    support_button_rect
):

    global support_size

    mouse_pos = pygame.mouse.get_pos()


    image, image_rect, support_size = hover_image_icon(
        support_b,
        support_button_rect,
        mouse_pos,
        support_size
    )


    screen.blit(
        image,
        image_rect
    )
    
#----------------------------------------------------------------------------------

# gallery = pygame.image.load(
#     "./asset/image/gallery.png"
# )


# gallery_size = 90



# def gallery_button(
#     screen,
#     gallery_button_rect
# ):

#     global gallery_size

#     mouse_pos = pygame.mouse.get_pos()


#     image, image_rect, gallery_size = hover_image(
#         gallery,
#         gallery_button_rect,
#         mouse_pos,
#         gallery_size
#     )


#     screen.blit(
#         image,
#         image_rect
#     )
    
    
    #----------------------------------------------------------------------------------


# bug_b = pygame.image.load(
#     "./asset/image/bug.png"
# )


# bug_size = 50



# def bug_button(
#     screen,
#     bug_button_rect
# ):

#     global bug_size

#     mouse_pos = pygame.mouse.get_pos()


#     image, image_rect, bug_size = hover_image_icon(
#         bug_b,
#         bug_button_rect,
#         mouse_pos,
#         bug_size
#     )


#     screen.blit(
#         image,
#         image_rect
#     )
    
    
    
    
#----------------------------------------------------------------------------------   
    

support_Call = pygame.image.load(
    "./asset/image/support1.png"
)


call = 150



def call_support(
    screen,
    call_button_rect
):

    global call

    mouse_pos = pygame.mouse.get_pos()


    image, image_rect, call = hover_image_icon(
        support_Call,
        call_button_rect,
        mouse_pos,
        call
    )


    screen.blit(
        image,
        image_rect
    )
    
    
    
    
    




    

menu_button = pygame.image.load(
    "./asset/image/button1.png"
).convert_alpha()


button_image = pygame.transform.smoothscale(
    menu_button,
    (400,100)
)

menu_sizes = [85,85,85,85,85,85]


def draw_menu_buttons(
    screen,
    current_width,
    current_height,
    menu_button,
    fonts,
    select_buttons
):

    button_count = 6

    button_width = 400
    button_height = 100

    gap = 10


    button_titles = [
        "levels",
        "game_mode",
        "custom_game",
        "leader_board",
        "setting",
        "quit"
    ]
    total_height = (
        button_count * button_height
        + (button_count - 1) * gap
    )


    start_y = (
        current_height - total_height
    ) // 2



    for i in range(button_count):



        # ساخت Rect
        rect = button_image.get_rect()


        rect.center = (
            current_width // 2,
            start_y + i * (button_height + gap) + button_height // 2
        )


        select_buttons.append(rect)



        # ----------------
        # هاور
        # ----------------

        image, image_rect, menu_sizes[i] = hover_image_menu(
            button_image,
            rect,
            pygame.mouse.get_pos(),
            menu_sizes[i]
        )

        screen.blit(
            image,
            image_rect
        )


        # # ----------------
        # # متن
        # # ----------------

        font_size = int(
            50 * menu_sizes[i] / 90
        )

        # menu_font = pygame.font.Font(
        #     "./asset/font/name.ttf",
        #     font_size
        # )

        menu_font = get_font(font_size)

        text = menu_font.render(
            display_text(button_titles[i]),
            True,
            (0,0,0)
        )


        text_rect = text.get_rect(
            center=image_rect.center
        )


        screen.blit(
            text,
            text_rect
        )
    




















# این برای منوی تنظیمات است 

menu_button = pygame.image.load(
    "./asset/image/button1.png"
).convert_alpha()


setting_button_image = pygame.transform.smoothscale(
    menu_button,
    (400,100)
)


sizes_setting = [85,85,85,85,85,85,85]


def draw_setting_buttons(
    screen,
    current_width,
    current_height,
    fonts,
    settings_rects
):

    button_count_setting = 7

    button_width = 400
    button_height = 100

    gap = 10


    button_titles = [
        "music",
        "sound",
        "theme",
        "profile",
        "language",
        "support",
        "about"
    ]


    total_height = (
        button_count_setting * button_height
        + (button_count_setting - 1) * gap
    )


    start_y = (
        current_height - total_height
    ) // 2



    for i in range(button_count_setting):


        # استفاده از عکس آماده
        button_image = setting_button_image


        rect = button_image.get_rect()


        rect.center = (
            current_width // 2,
            start_y + i * (button_height + gap)
            + button_height // 2
        )


        settings_rects.append(rect)



        image, image_rect, sizes_setting[i] = hover_image_menu(
            button_image,
            rect,
            pygame.mouse.get_pos(),
            sizes_setting[i]
        )


        screen.blit(
            image,
            image_rect
        )


        font_size = int(
            50 * sizes_setting[i] / 90
        )


        setting_menu = get_font(font_size)


        text = setting_menu.render(
            display_text(button_titles[i]),
            True,
            (0,0,0)
        )


        text_rect = text.get_rect(
            center=image_rect.center
        )


        screen.blit(
            text,
            text_rect
        )

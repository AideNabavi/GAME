import pygame
from modules.font import *
    
# def draw_daily_title_for_today_game_and_status(
#     screen,
#     title
#     x,
#     y
# ):

#     text = fonts["date"].render(
#         title,
#         True,
#         (255, 255, 255)
#     )

#     rect = text.get_rect(
#         center=(x, y)
#     )

#     screen.blit(
#         text,
#         rect
#     )
    








def draw_today_and_status_description(
    screen,
    today_description,
    status_description,
    x,
    y
):

    text1 = fonts["date"].render(
        today_description,
        True,
        (255, 255, 255)
    )

    rect1 = text1.get_rect(
        center=(x, y)
    )

    screen.blit(
        text1,
        rect1
    )


    text2 = fonts["date"].render(
        status_description,
        True,
        (190, 190, 190)
    )

    rect2 = text2.get_rect(
        center=(x, y + 35)
    )

    screen.blit(
        text2,
        rect2
    )
    
    
    






















def draw_daily_xp(
    screen,
    font,
    xp,
    image,
    center_x,
    y,
    image_size=40,
    gap=8
):

    # ========================================================
    # TEXT
    # ========================================================

    text = font.render(
        f"+{xp} XP",
        True,
        (255, 210, 70)
    )


    # ========================================================
    # IMAGE
    # ========================================================

    image = pygame.transform.smoothscale(
        image,
        (image_size, image_size)
    )


    # ========================================================
    # TOTAL WIDTH
    # ========================================================

    total_width = (
        image.get_width()
        + gap
        + text.get_width()
    )


    # ========================================================
    # IMAGE RECT
    # ========================================================

    image_rect = image.get_rect(
        midleft=(
            center_x - total_width // 2,
            y
        )
    )


    # ========================================================
    # TEXT RECT
    # ========================================================

    text_rect = text.get_rect(
        midleft=(
            image_rect.right + gap,
            y
        )
    )


    # ========================================================
    # DRAW
    # ========================================================

    screen.blit(
        image,
        image_rect
    )

    screen.blit(
        text,
        text_rect
    )
    
    
    
    
    
    





def draw_daily_game_card(
    screen,
    rect,
    image,
    name,
    font
):

    # Card

    pygame.draw.rect(
        screen,
        (60, 60, 68),
        rect,
        border_radius=20
    )


    # Image

    image_rect = image.get_rect(
        center=(
            rect.centerx,
            rect.y + 90
        )
    )

    screen.blit(
        image,
        image_rect
    )


    # Name

    text = font.render(
        name,
        True,
        (255, 255, 255)
    )

    text_rect = text.get_rect(
        center=(
            rect.centerx,
            rect.bottom - 30
        )
    )

    screen.blit(
        text,
        text_rect
    )
    
    
    
    
    
    
    
    
    




def draw_daily_games(
    screen,
    images,
    font
):

    cards = [

        pygame.Rect(
            350,
            350,
            200,
            240
        ),

        pygame.Rect(
            600,
            350,
            200,
            240
        ),

        pygame.Rect(
            850,
            350,
            200,
            240
        )

    ]


    draw_daily_game_card(
        screen,
        cards[0],
        images[0],
        "HOW MANY",
        font
    )


    draw_daily_game_card(
        screen,
        cards[1],
        images[1],
        "MIRROR",
        font
    )


    draw_daily_game_card(
        screen,
        cards[2],
        images[2],
        "MEMORY",
        font
    )

    return cards























def draw_daily_play_button(
    screen,
    rect,
    font
):

    pygame.draw.rect(
        screen,
        (80, 150, 90),
        rect,
        border_radius=18
    )


    text = font.render(
        "PLAY",
        True,
        (255, 255, 255)
    )

    text_rect = text.get_rect(
        center=rect.center
    )

    screen.blit(
        text,
        text_rect
    )
    
    
    
    














# draw_daily_title(
#     screen,
#     title_font,
#     700,
#     130
# )

# draw_daily_description(
#     screen,
#     small_font,
#     700,
#     190
# )

# draw_daily_xp(
#     screen,
#     xp_font,
#     100,
#     700,
#     280
# )

# daily_cards = draw_daily_games(
#     screen,
#     daily_images,
#     small_font
# )

# draw_daily_play_button(
#     screen,
#     daily_play_rect,
#     button_font
# )

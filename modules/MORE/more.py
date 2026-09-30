



import pygame

from modules.EFFECT.hover import hover_image_level
from modules.font import fonts

from modules.EFFECT.slid_effect import (
    draw_random_side_effect,
    reset_side_effect
)


# ============================================================
# SUPPORT IMAGES
# ============================================================

images_support = [



    pygame.transform.smoothscale(
        pygame.image.load(
            "./asset/image/support/faq.png"
        ).convert_alpha(),
        (350, 350)
    ),

    pygame.transform.smoothscale(
        pygame.image.load(
            "./asset/image/support/info.png"
        ).convert_alpha(),
        (350, 350)
    ),

    pygame.transform.smoothscale(
        pygame.image.load(
            "./asset/image/support/policy.png"
        ).convert_alpha(),
        (350, 350)
    ),
    pygame.transform.smoothscale(
        pygame.image.load(
            "./asset/image/support/How.png"
        ).convert_alpha(),
        (350, 350)
    )

]


# ============================================================
# IMAGE SIZE
# ============================================================

image_sizes = [
    350,
    350,
    350,
    350
]


# ============================================================
# RECTANGLES
# ============================================================

support_rects = []

image_game_support = []


# ============================================================
# GAP
# ============================================================

gap_x = 435
gap_y = 230


# ============================================================
# GROUP OFFSET
# ============================================================

group_offset_x = 0
group_offset_y = 150


# ============================================================
# TEXT
# ============================================================

support_texts = [

    "How to Play",
    "FAQ",
    "INFO",
    "Privacy Policy"

]


# # ============================================================
# # SUPPORT SCREEN
# # ============================================================

# def draw_4_images_MORE(screen):

#     global image_sizes


#     mouse_pos = pygame.mouse.get_pos()


#     support_rects.clear()

#     image_game_support.clear()


#     # ========================================================
#     # CENTER
#     # ========================================================

#     center_x = (
#         screen.get_width() // 2
#         +
#         group_offset_x
#     )

#     center_y = (
#         screen.get_height() // 2
#         +
#         group_offset_y
#     )


#     # ========================================================
#     # POSITIONS
#     # ========================================================

#     positions = [

#         (-gap_x * 1.5, -100),

#         (-gap_x * 0.5, -100),

#         ( gap_x * 0.5, -100),

#         ( gap_x * 1.5, -100)

#     ]


#     # ========================================================
#     # DRAW IMAGES
#     # ========================================================

#     for i, img in enumerate(images_support):


#         # ----------------------------------------------------
#         # TARGET POSITION
#         # ----------------------------------------------------

#         offset_x, offset_y = positions[i]


#         x = center_x + offset_x

#         y = center_y + offset_y


#         # ----------------------------------------------------
#         # RECT
#         # ----------------------------------------------------

#         rect = img.get_rect(
#             center=(x, y)
#         )


#         # ----------------------------------------------------
#         # HOVER
#         # ----------------------------------------------------

#         new_img, new_rect, image_sizes[i] = (
#             hover_image_level(

#                 img,

#                 rect,

#                 mouse_pos,

#                 image_sizes[i]

#             )
#         )


#         # ----------------------------------------------------
#         # SAVE RECT
#         # ----------------------------------------------------

#         image_game_support.append(
#             new_rect
#         )


#         support_rects.append(
#             new_rect
#         )


#         # ====================================================
#         # SIDE EFFECT
#         # ====================================================

#         draw_random_side_effect(

#             screen,

#             new_img,

#             new_rect.centerx,

#             new_rect.centery,

#             i,

#             len(images_support),

#             image_size=image_sizes[i],

#             duration=600,

#             delay=120

#         )


#         # ====================================================
#         # TEXT
#         # ====================================================

#         # متن را بر اساس همان موقعیت نهایی عکس قرار می‌دهیم

#         text_surface = fonts["support"].render(

#             support_texts[i],

#             True,

#             (255, 255, 255)

#         )


#         text_rect = text_surface.get_rect(

#             center=(

#                 new_rect.centerx,

#                 new_rect.bottom + 40

#             )

#         )


#         # ----------------------------------------------------
#         # TEXT DRAW
#         # ----------------------------------------------------

#         screen.blit(

#             text_surface,

#             text_rect

#         )


#     return support_rects


# ============================================================
# MORE FACE IMAGE
# ============================================================

# IMA = pygame.transform.smoothscale(

#     pygame.image.load(
#         "./asset/image/support/SS.png"
#     ).convert_alpha(),

#     (1100, 1100)

# )


# # ============================================================
# # MORE FACE
# # ============================================================

# def draw_more_face(
#     screen,
#     current_width,
#     current_height
# ):

#     # ========================================================
#     # TARGET POSITION
#     # ========================================================

#     target_x = (
#         current_width // 2
#     )

#     target_y = (
#         current_height // 2
#         + 50
#     )


#     # ========================================================
#     # SIDE EFFECT
#     # ========================================================

#     draw_random_side_effect(

#         screen,

#         IMA,

#         target_x,

#         target_y,

#         0,

#         1,

#         image_size=1100,

#         duration=600,

#         delay=0

#     )
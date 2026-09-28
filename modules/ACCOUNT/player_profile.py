
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





#####################----------enter image in first page-----------##################
enter_size = 200

_enter_image = pygame.image.load(
    "./asset/image/enter.png"
).convert_alpha()



name_active = False

player_name = ""
name_entered = False

input_box = pygame.Rect(
    0,
    0,
    500,
    80
)


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
    
    

#####################----------email box in first page-----------##################

import pygame
from modules.sound_effect import play_click
from modules.EFFECT.hover import *


player_email = ""

email_input_box = pygame.Rect(
    500,   # X
    300,   # Y
    500,   # Width
    80     # Height
)
email_active = False

def draw_email_screen(
    screen,
    fonts,
    email
):



    pygame.draw.rect(
        screen,
        (255, 255, 255),
        email_input_box,
        border_radius=10
    )

    pygame.draw.rect(
        screen,
        (0, 0, 0),
        email_input_box,
        2,
        border_radius=10
    )

    # ========================================================
    # Email Text
    # ========================================================

    if email == "":

        email_text = fonts["name"].render(
            "Your Email",
            True,
            (170, 170, 170)
        )

    else:

        email_text = fonts["name"].render(
            email,
            True,
            (255, 220, 0)
        )

    email_rect = email_text.get_rect(
        center=email_input_box.center
    )

    # ========================================================
    # Stroke
    # ========================================================

    if email != "":

        stroke = fonts["name"].render(
            email,
            True,
            (0, 0, 0)
        )

        for dx, dy in (
            (-2, 0),
            (2, 0),
            (0, -2),
            (0, 2),
            (-1, -1),
            (1, -1),
            (-1, 1),
            (1, 1)
        ):

            screen.blit(
                stroke,
                (
                    email_rect.x + dx,
                    email_rect.y + dy
                )
            )

    # ========================================================
    # Text
    # ========================================================

    screen.blit(
        email_text,
        email_rect
    )


# ============================================================
# EMAIL INPUT
# ============================================================

def handle_email_input(
    event,
    email):

    # کاراکترهای مجاز
    allowed_characters = (
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789"
        "@._+-"
    )

    # ========================================================
    # CLICK
    # ========================================================

    if event.type == pygame.MOUSEBUTTONDOWN:

        if email_input_box.collidepoint(event.pos):

            pygame.key.start_text_input()

            return email, True

        else:

            pygame.key.stop_text_input()

            return email, False

    # ========================================================
    # TEXT INPUT
    # ========================================================

    if event.type == pygame.TEXTINPUT:

        for char in event.text:

            if char in allowed_characters:

                email += char

        return email, True

    # ========================================================
    # BACKSPACE / ENTER
    # ========================================================

    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_BACKSPACE:

            email = email[:-1]

            return email, True

        if event.key == pygame.K_RETURN:

            pygame.key.stop_text_input()

            return email, False

    return email, True




#####################----------defult preview profile-----------##################

def load_default_profile():

    image = pygame.image.load(
        "./asset/image/profile/user.png"
    ).convert_alpha()

    return image



#####################----------defult preview profile-----------##################



def load_profile_images():

    profile_images = {}

    for i in range(1, 11):

        image = pygame.image.load(
            f"./asset/image/profile/{i}.png"
        ).convert_alpha()

        profile_images[i] = image

    return profile_images


# # ============================================================
# # CACHE
# # ============================================================

_profile_circle_cache = {}


def draw_profile_circle(
    screen,
    image,
    center,
    size=250,
    border_color=None
):

    key = (
        id(image),
        size
    )

    if key not in _profile_circle_cache:

        profile_image = pygame.transform.smoothscale(
            image,
            (size, size)
        )

        _profile_circle_cache[key] = profile_image

    profile_image = _profile_circle_cache[key]

    rect = profile_image.get_rect(
        center=center
    )

    screen.blit(
        profile_image,
        rect
    )


# # ============================================================
# # PROFILE LIST
# # ============================================================




#####################----------image profile-----------##################

profile_hover_sizes = {}


def draw_profiles(
    screen,
    profile_images,
    profile_rects,
    profile_area
):

    mouse_pos = pygame.mouse.get_pos()

    profile_rects.clear()

    columns = 5

    gap_x = 150
    gap_y = 150

    total_width = (columns - 1) * gap_x

    start_x = (
        profile_area.centerx
        - total_width // 2
        + 500
    )

    start_y = profile_area.y + 150

    # فقط ۱۰ عکس
    profiles = list(profile_images.items())[:10]

    for index, (profile_id, image) in enumerate(profiles):

        row = index // columns
        col = index % columns

        x = start_x + col * gap_x
        y = start_y + row * gap_y

        # ----------------------------------------------------
        # Rect ثابت برای کلیک و Hover
        # ----------------------------------------------------

        rect = pygame.Rect(
            0,
            0,
            100,
            100
        )

        rect.center = (x, y)

        profile_rects[profile_id] = rect

        # ----------------------------------------------------
        # مقدار اولیه Hover
        # ----------------------------------------------------

        if profile_id not in profile_hover_sizes:

            profile_hover_sizes[profile_id] = 100

        # ----------------------------------------------------
        # Hover
        # ----------------------------------------------------

        new_image, new_rect, profile_hover_sizes[profile_id] = (
            hover_image_profile_(
                image,
                rect,
                mouse_pos,
                profile_hover_sizes[profile_id]
            )
        )

        # ----------------------------------------------------
        # نمایش
        # ----------------------------------------------------

        screen.blit(
            new_image,
            new_rect
        )


# # ============================================================
# # SMOOTH CIRCLE BORDER CACHE
# # ============================================================

# _circle_border_cache = {}


# def draw_smooth_circle_border(
#     screen,
#     center,
#     radius,
#     color,
#     width
# ):

#     key = (
#         radius,
#         color,
#         width
#     )

#     if key not in _circle_border_cache:

#         scale = 4

#         diameter = radius * 2

#         temp = pygame.Surface(
#             (
#                 diameter * scale + width * 2,
#                 diameter * scale + width * 2
#             ),
#             pygame.SRCALPHA
#         )

#         pygame.draw.circle(
#             temp,
#             color,
#             (
#                 temp.get_width() // 2,
#                 temp.get_height() // 2
#             ),
#             radius * scale,
#             width * scale
#         )

#         temp = pygame.transform.smoothscale(
#             temp,
#             (
#                 diameter + width * 2,
#                 diameter + width * 2
#             )
#         )

#         _circle_border_cache[key] = temp

#     temp = _circle_border_cache[key]

#     rect = temp.get_rect(
#         center=center
#     )

#     screen.blit(
#         temp,
#         rect
#     )


# # ============================================================
# # SMOOTH RECT BORDER CACHE
# # ============================================================

# _rect_border_cache = {}


# def draw_smooth_rect_border(
#     screen,
#     rect,
#     color,
#     width
# ):

#     key = (
#         rect.width,
#         rect.height,
#         color,
#         width
#     )

#     if key not in _rect_border_cache:

#         scale = 4

#         temp = pygame.Surface(
#             (
#                 rect.width * scale,
#                 rect.height * scale
#             ),
#             pygame.SRCALPHA
#         )

#         pygame.draw.rect(
#             temp,
#             color,
#             (
#                 0,
#                 0,
#                 rect.width * scale,
#                 rect.height * scale
#             ),
#             width * scale,
#             border_radius=30 * scale
#         )

#         temp = pygame.transform.smoothscale(
#             temp,
#             (
#                 rect.width,
#                 rect.height
#             )
#         )

#         _rect_border_cache[key] = temp

#     temp = _rect_border_cache[key]

#     screen.blit(
#         temp,
#         rect
#     )


# # ============================================================
# PROFILE + FRAME CACHE
# ============================================================

# _profile_frame_cache = {}


# def create_profile_with_frame(
#     frame_image,
#     profile_image,
#     frame_size,
#     profile_size
# ):

#     key = (
#         id(frame_image),
#         id(profile_image),
#         frame_size,
#         profile_size
#     )

#     if key in _profile_frame_cache:

#         return _profile_frame_cache[key]

#     # --------------------------------------------------------
#     # قاب
#     # --------------------------------------------------------

#     frame_image = pygame.transform.smoothscale(
#         frame_image,
#         (frame_size, frame_size)
#     )

#     # --------------------------------------------------------
#     # عکس پروفایل
#     # --------------------------------------------------------

#     profile_image = pygame.transform.smoothscale(
#         profile_image,
#         (profile_size, profile_size)
#     )

#     # --------------------------------------------------------
#     # دایره‌ای کردن عکس
#     # --------------------------------------------------------

#     profile_surface = pygame.Surface(
#         (profile_size, profile_size),
#         pygame.SRCALPHA
#     )

#     profile_surface.blit(
#         profile_image,
#         (0, 0)
#     )

#     mask = pygame.Surface(
#         (profile_size, profile_size),
#         pygame.SRCALPHA
#     )

#     pygame.draw.circle(
#         mask,
#         (255, 255, 255, 255),
#         (
#             profile_size // 2,
#             profile_size // 2
#         ),
#         profile_size // 2
#     )

#     profile_surface.blit(
#         mask,
#         (0, 0),
#         special_flags=pygame.BLEND_RGBA_MULT
#     )

#     # --------------------------------------------------------
#     # خروجی
#     # --------------------------------------------------------

#     result = pygame.Surface(
#         (frame_size, frame_size),
#         pygame.SRCALPHA
#     )

#     result.blit(
#         frame_image,
#         (0, 0)
#     )

#     pos = (
#         (frame_size - profile_size) // 2,
#         (frame_size - profile_size) // 2
#     )

#     result.blit(
#         profile_surface,
#         pos
#     )

#     # --------------------------------------------------------
#     # Cache
#     # --------------------------------------------------------

#     _profile_frame_cache[key] = result

#     return result
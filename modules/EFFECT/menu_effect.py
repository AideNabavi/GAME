import pygame

from modules.language import display_text
from modules.language import get_language_font


# ============================================================
# MENU BACKGROUND
# ============================================================

xxxxxxxxxx = 350
yyyyyyyyyy = 140

# menu_0 = pygame.transform.smoothscale(
#     pygame.image.load(
#         "./asset/image/menu/0.png"
#     ).convert_alpha(),
#     (500, 400)
# )

# menu_bacccccck = [
#     menu_0,

#     pygame.transform.smoothscale(
#         pygame.image.load(
#             "./asset/image/menu/1.png"
#         ).convert_alpha(),
#         (xxxxxxxxxx, yyyyyyyyyy)
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(
#             "./asset/image/menu/2.png"
#         ).convert_alpha(),
#         (xxxxxxxxxx, yyyyyyyyyy)
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(
#             "./asset/image/menu/1.png"
#         ).convert_alpha(),
#         (xxxxxxxxxx, yyyyyyyyyy)
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(
#             "./asset/image/menu/2.png"
#         ).convert_alpha(),
#         (xxxxxxxxxx, yyyyyyyyyy)
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(
#             "./asset/image/menu/1.png"
#         ).convert_alpha(),
#         (xxxxxxxxxx, yyyyyyyyyy)
#     )

    # pygame.transform.smoothscale(
    #     pygame.image.load(
    #         "./asset/image/menu/2.png"
    #     ).convert_alpha(),
    #     (xxxxxxxxxx, yyyyyyyyyy)
    # )

    # pygame.transform.smoothscale(
    #     pygame.image.load(
    #         "./asset/image/menu/1.png"
    #     ).convert_alpha(),
    #     (xxxxxxxxxx, yyyyyyyyyy)
    # )
# ]


# ============================================================
# MENU ICONS
# ============================================================

music = pygame.transform.smoothscale(
    pygame.image.load(
        "./asset/image/setting/music.png"
    ).convert_alpha(),
    (70, 70)
)

sound = pygame.transform.smoothscale(
    pygame.image.load(
        "./asset/image/setting/sound.png"
    ).convert_alpha(),
    (70, 70)
)

account = pygame.transform.smoothscale(
    pygame.image.load(
        "./asset/image/setting/user.png"
    ).convert_alpha(),
    (70, 70)
)

language = pygame.transform.smoothscale(
    pygame.image.load(
        "./asset/image/setting/lan.png"
    ).convert_alpha(),
    (70, 70)
)

more = pygame.transform.smoothscale(
    pygame.image.load(
        "./asset/image/setting/more.png"
    ).convert_alpha(),
    (70, 70)
)

back = pygame.transform.smoothscale(
    pygame.image.load(
        "./asset/image/back1.png"
    ).convert_alpha(),
    (70, 70)
)


menu_icons = [
    music,
    sound,
    account,
    language,
    more,
    back
]


# ============================================================
# MENU TITLES
# ============================================================

button_titles = [
    "music",
    "sound",
    "account",
    "language",
    "more",
    "back"
]


# ============================================================
# MENU POSITIONS
# ============================================================

ggg = 90

menu_positions = [

    (ggg, -350),
    (ggg, -210),
    (ggg, -70),
    (ggg, 70),
    (ggg, 210),
    (ggg, 350)

]


# ============================================================
# MENU CACHE
# ============================================================

menu_cache = {}


# ============================================================
# CREATE MENU SURFACE
# ============================================================

def create_menu_surface(
    index,
    size,
    fonts
):

    translated_text = display_text(
        button_titles[index]
    )

    key = (
        index,
        size,
        translated_text
    )

    if key in menu_cache:
        return menu_cache[key]

    icon = menu_icons[index]

    font = get_language_font("support")

    text_color = (245, 215, 160)
    stroke_color = (0, 0, 0)
    stroke_width = 1

    base_text = font.render(
        translated_text,
        True,
        text_color
    )

    text = pygame.Surface(
        (
            base_text.get_width()
            + stroke_width * 2,

            base_text.get_height()
            + stroke_width * 2
        ),
        pygame.SRCALPHA
    )

    stroke_surface = font.render(
        translated_text,
        True,
        stroke_color
    )

    for dx in range(
        -stroke_width,
        stroke_width + 1
    ):

        for dy in range(
            -stroke_width,
            stroke_width + 1
        ):

            if dx == 0 and dy == 0:
                continue

            text.blit(
                stroke_surface,
                (
                    stroke_width + dx,
                    stroke_width + dy
                )
            )

    text.blit(
        base_text,
        (
            stroke_width,
            stroke_width
        )
    )

    scale = size / 80.0

    icon_size = int(
        100 * scale
    )

    if icon_size < 1:
        icon_size = 1

    if size == 80:

        scaled_icon = icon

    else:

        scaled_icon = pygame.transform.smoothscale(
            icon,
            (
                icon_size,
                icon_size
            )
        )

    if size == 80:

        scaled_text = text

    else:

        text_width = max(
            1,
            int(text.get_width() * scale)
        )

        text_height = max(
            1,
            int(text.get_height() * scale)
        )

        scaled_text = pygame.transform.smoothscale(
            text,
            (
                text_width,
                text_height
            )
        )

    spacing = int(
        25 * scale
    )

    width = (
        scaled_icon.get_width()
        + spacing
        + scaled_text.get_width()
    )

    height = max(
        scaled_icon.get_height(),
        scaled_text.get_height()
    )

    surface = pygame.Surface(
        (
            width,
            height
        ),
        pygame.SRCALPHA
    )

    icon_rect = scaled_icon.get_rect()

    icon_rect.midleft = (
        0,
        height // 2
    )

    text_rect = scaled_text.get_rect()

    text_rect.midleft = (
        icon_rect.right + spacing,
        height // 2
    )

    surface.blit(
        scaled_icon,
        icon_rect
    )

    surface.blit(
        scaled_text,
        text_rect
    )

    menu_cache[key] = surface

    return surface


# ============================================================
# MENU ANIMATION
# ============================================================

_menu_current_y = None


def reset_menu():

    global _menu_current_y

    _menu_current_y = None


# ============================================================
# DRAW MENU
# ============================================================
def draw_menu___new(
    screen,
    current_width,
    current_height,
    fonts,
    select_buttons,
    show=True
):

    global _menu_current_y

    # ========================================================
    # MENU POSITIONS
    # ========================================================

    ggg = 90

    menu_positions = [
        (ggg, -350),
        (ggg, -210),
        (ggg, -70),
        (ggg, 70),
        (ggg, 210),
        (ggg, 350)
    ]

    # ========================================================
    # TARGET
    # ========================================================

    target_y = current_height // 2 - 670

    # ========================================================
    # HIDDEN
    # ========================================================

    hidden_y = -1000

    # ========================================================
    # START
    # ========================================================

    if _menu_current_y is None:
        _menu_current_y = hidden_y

    # ========================================================
    # DESTINATION
    # ========================================================

    if show:
        destination_y = target_y
    else:
        destination_y = hidden_y

    # ========================================================
    # ANIMATION
    # ========================================================

    speed = 35

    if _menu_current_y < destination_y:

        _menu_current_y += speed

        if _menu_current_y >= destination_y:
            _menu_current_y = destination_y

    elif _menu_current_y > destination_y:

        _menu_current_y -= speed

        if _menu_current_y <= destination_y:
            _menu_current_y = destination_y

    # ========================================================
    # OFFSET
    # ========================================================

    offset = _menu_current_y - target_y

    # ========================================================
    # DRAW MENU BACK
    # ========================================================

    for i, image in enumerate(menu_icons):

        x = menu_positions[i][0]

        y = (
            current_height // 2
            + menu_positions[i][1]
            + offset
        )

        # مرکز بک دقیقاً روی محل آیکون
        rect = image.get_rect(
            center=(
                x,
                int(y)
            )
        )

        screen.blit(
            image,
            rect
        )

    # ========================================================
    # BUTTONS
    # ========================================================

    select_buttons.clear()

    for i in range(len(menu_icons)):

        x = menu_positions[i][0]

        y = (
            current_height // 2
            + menu_positions[i][1]
            + offset
        )

        size = 80

        surface = create_menu_surface(
            i,
            size,
            fonts
        )

        rect = surface.get_rect(
            center=(
                x,
                int(y)
            )
        )

        screen.blit(
            surface,
            rect
        )

        select_buttons.append(
            rect.copy()
        )
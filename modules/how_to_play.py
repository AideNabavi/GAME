import pygame

from modules.font import fonts






copyright_image = pygame.image.load(
    "asset/image/copyright.png"
).convert_alpha()



game_logo = pygame.image.load(
    "asset/image/logo.png"
).convert_alpha()


_image = pygame.image.load(
    "asset/image/aiden.png"
).convert_alpha()
# ============================================================
# COLORS
# ============================================================

INFO_TITLE_COLOR = (60, 60, 60)

INFO_SECTION_COLOR = (180, 100, 35)

INFO_LABEL_COLOR = (150, 85, 30)

INFO_VALUE_COLOR = (60, 60, 60)

INFO_SPECIAL_COLOR = (120, 80, 40)

INFO_SEPARATOR_COLOR = (180, 130, 80)


# ============================================================
# SCROLL
# ============================================================

scroll_y = 0
scroll_velocity = 0

friction = 0.94


# ============================================================
# INFO DATA
# ============================================================

INFO_DATA = [

    ("Version", "1.0.0"),
    ("Created by", "AideNabavi"),
    ("Release", "2026"),

    ("Platforms", "macOS • Windows • Linux • Web"),

    ("Coming Soon", "Android • iOS"),

    (
        "Technologies",
        "Python • JavaScript • Swift • C#"
    ),

    (
        "Game Type",
        "Brain & Thinking Games"
    ),

    ("Game Collection", "40 Available"),
    ("Free Games", "10"),
    ("Premium Games", "30"),
    ("Upcoming Games", "20+"),

    ("Game Modes", "Single Player"),
    ("Multiplayer", "2 / 3 / 4 Players"),
    ("Online", "Coming Soon"),

]


# ============================================================
# DEVELOPER DATA
# ============================================================

DEVELOPER_DATA = [

    ("Developer", "AideNabavi"),
    ("Made in", "Iran"),

    ("Email", "nabavi447@gmail.com"),

    ("GitHub", "github.com/AideNabavi"),

]








COPYRIGHT_TEXT = [
    "Mental Math Challenge and its original content,",
    "including source code, game design, graphics,",
    "sounds, logos and other assets, are protected",
    "by applicable copyright and intellectual property laws.",
    "",
    "Unauthorized copying, modification, distribution,",
    "reproduction or commercial use of this game",
    "or its original assets is prohibited.",
    "",
    "Unauthorized use may result in legal action",
    "where permitted by applicable law."
]
# ============================================================
# IMAGE SCALE
# ============================================================

def scale_image_keep_ratio(image, max_width, max_height):

    if image is None:
        return None

    width, height = image.get_size()

    if width <= 0 or height <= 0:
        return image

    scale = min(
        max_width / width,
        max_height / height
    )

    new_width = max(1, int(width * scale))
    new_height = max(1, int(height * scale))

    return pygame.transform.smoothscale(
        image,
        (new_width, new_height)
    )


# ============================================================
# DRAW CENTERED TEXT
# ============================================================

def draw_center_text(
    screen,
    text,
    font,
    color,
    center_x,
    y
):

    surface = font.render(
        text,
        True,
        color
    )

    rect = surface.get_rect(
        centerx=center_x,
        top=y
    )

    screen.blit(
        surface,
        rect
    )

    return rect.height


# ============================================================
# DRAW LABEL + VALUE
# ============================================================

def draw_info_row(
    screen,
    label,
    value,
    x,
    y
):

    label_font = fonts["date"]

    value_font = fonts["date"]

    # --------------------------------------------------------
    # LABEL
    # --------------------------------------------------------

    label_surface = label_font.render(
        label,
        True,
        INFO_LABEL_COLOR
    )

    screen.blit(
        label_surface,
        (x, y)
    )

    # --------------------------------------------------------
    # VALUE
    # --------------------------------------------------------

    value_surface = value_font.render(
        value,
        True,
        INFO_VALUE_COLOR
    )

    value_x = x + label_surface.get_width() + 25

    screen.blit(
        value_surface,
        (value_x, y)
    )

    return max(
        label_surface.get_height(),
        value_surface.get_height()
    )


# ============================================================
# DRAW SEPARATOR
# ============================================================

def draw_separator(
    screen,
    x,
    y,
    width
):

    pygame.draw.line(
        screen,
        INFO_SEPARATOR_COLOR,
        (x, y),
        (x + width, y),
        2
    )


# ============================================================
# DRAW SECTION TITLE
# ============================================================

def draw_section_title(
    screen,
    text,
    center_x,
    y
):

    return draw_center_text(
        screen,
        text,
        fonts["TITLE_NEW"],
        INFO_SECTION_COLOR,
        center_x,
        y
    )

# ============================================================
# MAIN INFO DRAW
# ============================================================
def draw_INFO(
    screen,
    privacy_box,
    game_logo,
    developer_image
):

    global scroll_y
    global scroll_velocity

    # ========================================================
    # SCROLL UPDATE
    # ========================================================

    scroll_y += scroll_velocity

    scroll_velocity *= friction

    if abs(scroll_velocity) < 0.1:
        scroll_velocity = 0

    # ========================================================
    # CONTENT
    # ========================================================

    content_x = privacy_box.x
    content_width = privacy_box.width

    center_x = privacy_box.centerx

    top_y = privacy_box.y + 35

    # ========================================================
    # IMAGES
    # ========================================================

    logo = scale_image_keep_ratio(
        game_logo,
        300,
        180
    )

    dev_image = scale_image_keep_ratio(
        developer_image,
        220,
        220
    )

    # ========================================================
    # CLIP
    # ========================================================

    screen.set_clip(
        privacy_box
    )

    # ========================================================
    # START Y
    # ========================================================

    y = top_y - scroll_y

    # ========================================================
    # GAME LOGO
    # ========================================================

    if logo is not None:

        logo_rect = logo.get_rect(
            centerx=center_x,
            top=y
        )

        screen.blit(
            logo,
            logo_rect
        )

        y += logo.get_height()
        y += 25

    # ========================================================
    # GAME TITLE
    # ========================================================

    title_height = draw_center_text(
        screen,
        "MENTAL MATH CHALLENGE",
        fonts["TITLE_NEW"],
        INFO_TITLE_COLOR,
        center_x,
        y
    )

    y += title_height
    y += 45

    # ========================================================
    # SEPARATOR
    # ========================================================

    draw_separator(
        screen,
        content_x + 40,
        y,
        content_width - 80
    )

    y += 40

    # ========================================================
    # GAME INFORMATION
    # ========================================================

    section_height = draw_section_title(
        screen,
        "GAME INFORMATION",
        center_x,
        y
    )

    y += section_height
    y += 30

    # ========================================================
    # GAME INFO
    # ========================================================

    for label, value in INFO_DATA:

        row_height = draw_info_row(
            screen,
            label,
            value,
            content_x + 40,
            y
        )

        y += row_height
        y += 20

    # ========================================================
    # SEPARATOR
    # ========================================================

    draw_separator(
        screen,
        content_x + 40,
        y,
        content_width - 80
    )

    y += 60

    # ========================================================
    # DEVELOPER IMAGE
    # ========================================================

    if dev_image is not None:

        dev_rect = dev_image.get_rect(
            centerx=center_x,
            top=y
        )

        screen.blit(
            dev_image,
            dev_rect
        )

        y += dev_image.get_height()
        y += 25

    # ========================================================
    # DEVELOPER NAME
    # ========================================================

    name_height = draw_center_text(
        screen,
        "AideNabavi",
        fonts["TITLE_NEW"],
        INFO_TITLE_COLOR,
        center_x,
        y
    )

    y += name_height
    y += 15

    # ========================================================
    # DEVELOPER TITLE
    # ========================================================

    developer_title_height = draw_center_text(
        screen,
        "Game Developer",
        fonts["date"],
        INFO_SPECIAL_COLOR,
        center_x,
        y
    )

    y += developer_title_height
    y += 45

    # ========================================================
    # DEVELOPER INFORMATION
    # ========================================================

    for label, value in DEVELOPER_DATA:

        row_height = draw_info_row(
            screen,
            label,
            value,
            content_x + 40,
            y
        )

        y += row_height
        y += 20

    # ========================================================
    # SPACE AFTER DEVELOPER
    # ========================================================

    y += 100

    # ========================================================
    # COPYRIGHT SECTION SEPARATOR
    # ========================================================

    draw_separator(
        screen,
        content_x + 40,
        y,
        content_width - 80
    )

    y += 55

    # ========================================================
    # COPYRIGHT IMAGE
    # ========================================================

    copyright_icon = scale_image_keep_ratio(
        copyright_image,
        150,
        150
    )

    if copyright_icon is not None:

        copyright_rect = copyright_icon.get_rect(
            centerx=center_x,
            top=y
        )

        screen.blit(
            copyright_icon,
            copyright_rect
        )

        y += copyright_icon.get_height()
        y += 25

    # ========================================================
    # COPYRIGHT TITLE
    # ========================================================

    section_height = draw_section_title(
        screen,
        "COPYRIGHT & LEGAL",
        center_x,
        y
    )

    y += section_height
    y += 25

    # ========================================================
    # COPYRIGHT TEXT
    # ========================================================

    copyright_font = fonts["date"]

    for line in COPYRIGHT_TEXT:

        if line == "":
            y += 12
            continue

        text_surface = copyright_font.render(
            line,
            True,
            INFO_VALUE_COLOR
        )

        text_rect = text_surface.get_rect(
            centerx=center_x,
            top=y
        )

        screen.blit(
            text_surface,
            text_rect
        )

        y += text_rect.height
        y += 7

    # ========================================================
    # SPACE BEFORE FINAL COPYRIGHT
    # ========================================================

    y += 25

    # ========================================================
    # SEPARATOR
    # ========================================================

    draw_separator(
        screen,
        content_x + 40,
        y,
        content_width - 80
    )

    y += 50

    # ========================================================
    # COPYRIGHT
    # ========================================================

    copyright_height = draw_center_text(
        screen,
        "© 2026 Aiden",
        fonts["date"],
        INFO_SPECIAL_COLOR,
        center_x,
        y
    )

    y += copyright_height
    y += 20

    # ========================================================
    # ALL RIGHTS RESERVED
    # ========================================================

    reserved_height = draw_center_text(
        screen,
        "All Rights Reserved.",
        fonts["date"],
        INFO_VALUE_COLOR,
        center_x,
        y
    )

    y += reserved_height

    # ========================================================
    # REAL CONTENT BOTTOM
    # ========================================================

    content_bottom = y + 60

    # ========================================================
    # MAX SCROLL
    # ========================================================

    max_scroll = 2200

    # ========================================================
    # LIMIT SCROLL
    # ========================================================

    if scroll_y < 0:

        scroll_y = 0
        scroll_velocity = 0

    elif scroll_y > max_scroll:

        scroll_y = max_scroll
        scroll_velocity = 0

    # ========================================================
    # REMOVE CLIP
    # ========================================================

    screen.set_clip(None)
def INFO_event(event):

    global scroll_velocity

    if event.type == pygame.MOUSEWHEEL:

        scroll_velocity -= event.y * 25

# ============================================================
# RESET
# ============================================================

def reset_INFO():

    global scroll_y
    global scroll_velocity

    scroll_y = 0
    scroll_velocity = 0


# ============================================================
# INFO SIDE EFFECT
# ============================================================

def draw_INFO_side_effect(
    screen,
    rect,
):

    # --------------------------------------------------------
    # INFO BOX
    # --------------------------------------------------------

    privacy_box = pygame.Rect(

        rect.centerx - 440,
        rect.centery - 330,

        870,
        810
    )

    # --------------------------------------------------------
    # DRAW INFO
    # --------------------------------------------------------

    draw_INFO(
        screen,
        privacy_box,
        game_logo,
        developer_image
    )
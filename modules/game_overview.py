import pygame

from modules.font import fonts


# ============================================================
# GAME OVERVIEW IMAGES
# ============================================================

xp_image = pygame.image.load(
    "asset/image/logo.png"
).convert_alpha()

score_image = pygame.image.load(
    "asset/image/aiden.png"
).convert_alpha()

difficulty_image = pygame.image.load(
    "asset/image/copyright.png"
).convert_alpha()

mode_image = pygame.image.load(
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
# GAME OVERVIEW DATA
# ============================================================

GAME_OVERVIEW_DATA = [

    ("XP", "250", xp_image),

    ("SCORE", "1200", score_image),

    ("DIFFICULTY", "MEDIUM", difficulty_image),

    ("MODE", "SINGLE PLAYER", mode_image),

]


# ============================================================
# IMAGE SCALE
# ============================================================

def scale_image_keep_ratio(
    image,
    max_width,
    max_height
):

    if image is None:
        return None

    width, height = image.get_size()

    if width <= 0 or height <= 0:
        return image

    scale = min(
        max_width / width,
        max_height / height
    )

    new_width = max(
        1,
        int(width * scale)
    )

    new_height = max(
        1,
        int(height * scale)
    )

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
# DRAW GAME OVERVIEW ROW
# ============================================================

def draw_game_overview_row(
    screen,
    label,
    value,
    image,
    x,
    y,
    row_width
):

    label_font = fonts["date"]

    value_font = fonts["date"]


    # ========================================================
    # IMAGE
    # ========================================================

    # <<< CHANGE:
    # اندازه عکس کوچک جلوی هر مورد
    small_image = scale_image_keep_ratio(
        image,
        55,
        55
    )

    image_x = x

    image_y = y

    if small_image is not None:

        image_rect = small_image.get_rect(
            centerx=image_x + 27,
            centery=image_y + 25
        )

        screen.blit(
            small_image,
            image_rect
        )


    # ========================================================
    # LABEL
    # ========================================================
    center_x = 600

    label_x = center_x - 200

    label_surface = label_font.render(
        label,
        True,
        INFO_LABEL_COLOR
    )

    label_rect = label_surface.get_rect(
        left=label_x,
        centery=y + 25
    )

    screen.blit(label_surface, label_rect)


    # -------------------------
    # VALUE
    # -------------------------

    value_x = center_x + 300

    value_surface = value_font.render(
        str(value),
        True,
        INFO_VALUE_COLOR
    )

    value_rect = value_surface.get_rect(
        left=value_x,
        centery=y + 25
    )

    screen.blit(value_surface, value_rect)


    # ========================================================
    # RETURN ROW HEIGHT
    # ========================================================

    return max(
        55,
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
# MAIN GAME OVERVIEW DRAW
# ============================================================

def draw_GAME_OVERVIEW(
    screen,
    overview_box
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
    # CONTENT POSITION
    # ========================================================

    # <<< CHANGE:
    # فاصله محتوای داخلی از چپ
    content_x = overview_box.x + 40

    # <<< CHANGE:
    # عرض محتوای داخلی
    content_width = overview_box.width - 80

    # مرکز باکس
    center_x = overview_box.centerx


    # ========================================================
    # START Y
    # ========================================================

    # <<< CHANGE:
    # فاصله شروع محتوا از بالای باکس
    top_y = overview_box.y + 35


    # ========================================================
    # CLIP
    # ========================================================

    # این قسمت مشخص می‌کند فقط چیزی که
    # داخل overview_box است دیده شود.

    # <<< CHANGE:
    # محدوده قابل مشاهده را با خود overview_box تغییر بده
    screen.set_clip(
        overview_box
    )


    # ========================================================
    # START SCROLL POSITION
    # ========================================================

    y = top_y - scroll_y


    # ========================================================
    # GAME OVERVIEW TITLE
    # ========================================================

    title_height = draw_center_text(
        screen,
        "GAME OVERVIEW",
        fonts["TITLE_NEW"],
        INFO_TITLE_COLOR,
        center_x,
        y
    )

    y += title_height

    # <<< CHANGE:
    # فاصله زیر عنوان
    y += 45


    # ========================================================
    # SEPARATOR
    # ========================================================

    draw_separator(
        screen,
        content_x,
        y,
        content_width
    )

    # <<< CHANGE:
    # فاصله بعد از خط
    y += 40


    # # ========================================================
    # # SECTION TITLE
    # # ========================================================

    # section_height = draw_section_title(
    #     screen,
    #     "GAME INFORMATION",
    #     center_x,
    #     y
    # )

    # y += section_height

    # # <<< CHANGE:
    # # فاصله بین عنوان و اولین ردیف
    # y += 35



    # ========================================================
    # OPTIONAL DESCRIPTION
    # ========================================================

    description_title_height = draw_section_title(
        screen,
        "ABOUT THIS GAME",
        center_x,
        y
    )

    y += description_title_height

    y += 30



    description = [
        "Train your brain and improve your thinking skills through challenging games this is ",
        "that test your memory, speed, logic, math, and detection abilities.",
        "Complete different games, earn XP, improve your score, and challenge yourself",
        "to become faster, smarter, and better with every game you play.",
        "Each challenge is designed to keep your mind active and help you improve",
        "your thinking skills while having fun and enjoying the experience.",
        "Play different challenges and discover your strongest mental abilities.",
        "Improve your performance by practicing regularly and completing games.",
        "Challenge yourself to reach higher scores and earn more experience points.",
        "Every game gives you a new opportunity to learn and improve your skills.",
        "Train your memory, reaction speed, logic, calculation, and observation.",
        "Keep playing and try to beat your previous scores and personal records.",
        "The more you play, the more familiar you become with each challenge.",
        "Focus on the game, think carefully, and make the best decision possible.",
        "Take on new challenges and see how far you can improve your performance.",
        "Your progress is built through practice, patience, focus, and consistency.",
        "Complete games, earn XP, improve your score, and challenge yourself.",
        "Keep your mind active with different types of challenging brain games.",
        "Play, learn, improve, and enjoy the challenge every time you play.",
        "Challenge yourself every day and become better with every game.",
    ]


    description_font = fonts["date"]
    description_x = center_x - 600

    # عرض خط‌ها
    description_width = 1000


    for line in description:

        # -------------------------
        # TEXT
        # -------------------------

        text_surface = description_font.render(
            line,
            True,
            INFO_VALUE_COLOR
        )

        text_rect = text_surface.get_rect(
            left=description_x,
            top=y
        )

        screen.blit(
            text_surface,
            text_rect
        )

        y += text_rect.height + 10


        # # -------------------------
        # # LINE
        # # -------------------------

        # pygame.draw.line(
        #     screen,
        #     INFO_SEPARATOR_COLOR,
        #     (description_x, y),
        #     (
        #         description_x + description_width,
        #         y
        #     ),
        #     2
        # )

        y += 20
    # ========================================================
    # GAME INFORMATION ROWS
    # ========================================================


    y += 20

    draw_separator(
        screen,
        content_x,
        y,
        content_width
    )

    y += 50

    for label, value, image in GAME_OVERVIEW_DATA:

        row_height = draw_game_overview_row(
            screen,
            label,
            value,
            image,
            content_x,
            y,
            content_width
        )

        y += row_height

        # <<< CHANGE:
        # فاصله بین XP / SCORE / DIFFICULTY / MODE
        y += 25


    # ========================================================
    # FINAL SEPARATOR
    # ========================================================

    y += 20

    draw_separator(
        screen,
        content_x,
        y,
        content_width
    )

    y += 50



    # ========================================================
    # CONTENT BOTTOM
    # ========================================================

    content_bottom = y + 60


    # ========================================================
    # MAX SCROLL
    # ========================================================

    # <<< CHANGE:
    # حداکثر میزان اسکرول
    max_scroll = max(
        0,
        content_bottom - overview_box.bottom + 2000
    )


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


# ============================================================
# EVENT
# ============================================================

def GAME_OVERVIEW_event(event):

    global scroll_velocity


    if event.type == pygame.MOUSEWHEEL:

        scroll_velocity -= event.y * 25


# ============================================================
# RESET
# ============================================================

def reset_GAME_OVERVIEW():

    global scroll_y
    global scroll_velocity

    scroll_y = 0
    scroll_velocity = 0


# ============================================================
# GAME OVERVIEW SIDE EFFECT
# ============================================================

def draw_GAME_OVERVIEW_side_effect(
    screen,
    rect
):

    # ========================================================
    # OVERVIEW BOX
    # ========================================================

    # <<< CHANGE:
    # اینجا اندازه و محل محدوده قابل مشاهده است
    overview_box = pygame.Rect(

        rect.centerx - 750,
        rect.centery - 330,

        1500,
        810
    )


    # ========================================================
    # DRAW GAME OVERVIEW
    # ========================================================

    draw_GAME_OVERVIEW(
        screen,
        overview_box
    )
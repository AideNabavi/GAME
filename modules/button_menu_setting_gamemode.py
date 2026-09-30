import pygame

from modules.language import display_text, get_language_font
from modules.font import fonts
# # ============================================================
# # MENU SURFACE CACHE
# # ============================================================
menu_cache = {}

select_buttons_setting=[]
# ============================================================
# CREATE MENU SURFACE
# ============================================================

def create_menu_surface(
    index,
    size,
    font,
    iconss,
    text_on
):
    # ========================================================
    # ORIGINAL ICON
    # ========================================================

    icon = iconss[index]

    # ========================================================
    # SCALE
    # ========================================================

    scale = size / 80.0

    # ========================================================
    # ICON SIZE
    # ========================================================

    icon_size = max(
        1,
        int(100 * scale)
    )

    # ========================================================
    # SCALE ICON
    # ========================================================

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

    # ========================================================
    # TEXT
    # ========================================================

    scaled_text = None

    if text_on == "setting":

        translated_text = display_text(
            button_titles[index]
        )
    if text_on == "menu":

        translated_text = display_text(
            MENU_title[index]
        )
    if text_on == "gamemode":

        translated_text = display_text(
            GAME_MODE_title[index]
        )
    if text_on == "gamemode" or text_on == "menu" or text_on == "setting" :

        # ====================================================
        # CACHE KEY
        # ====================================================

        key = (
            index,
            size,
            translated_text,
            text_on
        )

        if key in menu_cache:
            return menu_cache[key]

        # ====================================================
        # FONT
        # ====================================================

        font = get_language_font("support")

        text_color = (255, 140, 0)
        stroke_color = (0, 0, 0)
        stroke_width = 1

        # ====================================================
        # BASE TEXT
        # ====================================================

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

        # ====================================================
        # TEXT STROKE
        # ====================================================

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

        # ====================================================
        # MAIN TEXT
        # ====================================================

        text.blit(
            base_text,
            (
                stroke_width,
                stroke_width
            )
        )

        # ====================================================
        # SCALE TEXT
        # ====================================================

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

        # ========================================================
        # ICON ONLY
        # ========================================================

        if not text_on:

            key = (
                index,
                size,
                None,
                text_on
            )

            if key in menu_cache:
                return menu_cache[key]

            surface = pygame.Surface(
                (
                    scaled_icon.get_width(),
                    scaled_icon.get_height()
                ),
                pygame.SRCALPHA
            )

            surface.blit(
                scaled_icon,
                (
                    0,
                    0
                )
            )

            menu_cache[key] = surface

            return surface

        # ========================================================
        # SPACING
        # ========================================================

        spacing = int(
            25 * scale
        )

        # ========================================================
        # GROUP SIZE
        # ========================================================

        width = (
            scaled_icon.get_width()
            + spacing
            + scaled_text.get_width()
        )

        height = max(
            scaled_icon.get_height(),
            scaled_text.get_height()
        )

        # ========================================================
        # GROUP SURFACE
        # ========================================================

        surface = pygame.Surface(
            (
                width,
                height
            ),
            pygame.SRCALPHA
        )

        # ========================================================
        # ICON RECT
        # ========================================================

        icon_rect = scaled_icon.get_rect()

        icon_rect.midleft = (
            0,
            height // 2
        )

        # ========================================================
        # TEXT RECT
        # ========================================================

        text_rect = scaled_text.get_rect()

        text_rect.midleft = (
            icon_rect.right + spacing,
            height // 2
        )

        # ========================================================
        # DRAW ICON
        # ========================================================

        surface.blit(
            scaled_icon,
            icon_rect
        )

        # ========================================================
        # DRAW TEXT
        # ========================================================

        surface.blit(
            scaled_text,
            text_rect
        )

        # ========================================================
        # CACHE
        # ========================================================

        menu_cache[key] = surface

        return surface









# ============================================================
# MENU ICONS
# ============================================================


ICON_SIZE = (70, 70)

games = pygame.transform.smoothscale(
    pygame.image.load(
        "./asset/image/menu/games.png"
    ).convert_alpha(),
    ICON_SIZE
)

online = pygame.transform.smoothscale(
    pygame.image.load(
        "./asset/image/menu/online.png"
    ).convert_alpha(),
    ICON_SIZE
)

setting = pygame.transform.smoothscale(
    pygame.image.load(
        "./asset/image/menu/setting.png"
    ).convert_alpha(),
    ICON_SIZE
)

leaderboard = pygame.transform.smoothscale(
    pygame.image.load(
        "./asset/image/menu/leaderboard.png"
    ).convert_alpha(),
    ICON_SIZE
)

quit_ = pygame.transform.smoothscale(
    pygame.image.load(
        "./asset/image/menu/quit.png"
    ).convert_alpha(),
    ICON_SIZE
)

support = pygame.transform.smoothscale(
    pygame.image.load(
        "./asset/image/menu/call.png"
    ).convert_alpha(),
    ICON_SIZE
)

daily = pygame.transform.smoothscale(
    pygame.image.load(
        "./asset/image/menu/daily.png"
    ).convert_alpha(),
    ICON_SIZE
)
dashboard = pygame.transform.smoothscale(
    pygame.image.load(
        "./asset/image/menu/daily.png"
    ).convert_alpha(),
    (500,130)
)
dashboard.set_alpha(0)
# ============================================================
# setting ICONS
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
        "./asset/image/setting/back.png"
    ).convert_alpha(),
    (70, 70)
)


# ============================================================
# ICON LIST
# ============================================================

setting_icons = [
    music,
    sound,
    account,
    language,
    more,
    back
]

menu_icons = [
    dashboard,
    daily,
    games,
    online,
    leaderboard,
    setting,
    support,
    quit_
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

MENU_title = [
    "",
    "start",
    "games",
    "online",
    "ranking",
    "setting",
    "support",
    "quit"
]
GAME_MODE_title = [
    "",
    "",
    "",
    "",
    ""
]


# ============================================================
# MENU POSITIONS
# ============================================================

ggg = 40


sad=50
game_mode_positions_ = [

    (sad, 250 +35),
    (sad, 400+35),
    (sad, 550+35),
    (sad, 700+35),
    (sad, 850+35),
    (sad,1000+35),

]
setting_positions = [

    (ggg, 290),
    (ggg, 460 - 5),
    (ggg, 460 + 160),
    (ggg, 460 + 320 + 5),
    (ggg, 460 + 480 + 10),
    (ggg, 1170)

]


menu_positions = [

    (40, 90 - 37),
    (ggg, 287 - 25 ),
    (ggg, 431 - 40),
    (ggg, 562 - 33),
    (ggg, 712 - 22),
    (ggg, 921 - 22),
    (ggg, 1042 - 20),
    (ggg, 1192-20)

]
hover_scales = {}

selected_button = None


def gamemode_menu_setting_panel(
    screen,
    iconss,
    menu_pos,
    text_on,
    MODE,
    x,
    y,
    size=80,
    image=None,
):
    global selected_button

    # =========================================================
    # CLEAR CLICK RECT
    # =========================================================

    select_buttons_setting.clear()

    # =========================================================
    # START TIME
    # =========================================================

    if not hasattr(
        gamemode_menu_setting_panel,
        "start_time"
    ):
        gamemode_menu_setting_panel.start_time = pygame.time.get_ticks()

    now = pygame.time.get_ticks()

    elapsed = (
        now
        - gamemode_menu_setting_panel.start_time
    )

    # =========================================================
    # PANEL ANIMATION
    # =========================================================

    duration = 700

    if elapsed >= duration:

        progress = 1.0

    else:

        progress = elapsed / duration

        progress = (
            1
            - (1 - progress) ** 3
        )

    # =========================================================
    # PANEL POSITION
    # =========================================================

    if image is not None:

        start_x = -image.get_width()

        current_x = (
            start_x
            + (x - start_x) * progress
        )

        # =====================================================
        # PANEL RECT
        # =====================================================

        panel_rect = image.get_rect(
            center=(
                int(current_x),
                y
            )
        )

        # =====================================================
        # DRAW PANEL
        # =====================================================

        screen.blit(
            image,
            panel_rect
        )

    # =========================================================
    # MOUSE POSITION
    # =========================================================

    mouse_pos = pygame.mouse.get_pos()

    # =========================================================
    # EACH BUTTON
    # =========================================================

    button_delay = 100
    button_duration = 450

    for i in range(
        len(iconss)
    ):

        # =====================================================
        # DELAY
        # =====================================================

        button_start = (
            i * button_delay
        )

        button_elapsed = (
            elapsed
            - button_start
        )

        if button_elapsed <= 0:
            continue

        # =====================================================
        # BUTTON PROGRESS
        # =====================================================

        if button_elapsed >= button_duration:

            button_progress = 1.0

        else:

            button_progress = (
                button_elapsed
                / button_duration
            )

            button_progress = (
                1
                - (1 - button_progress) ** 3
            )

        # =====================================================
        # IMAGE + TEXT
        # =====================================================

        surface = create_menu_surface(
            i,
            size,
            fonts,
            iconss,
            text_on
        )

        # =====================================================
        # ORIGINAL POSITION
        # =====================================================

        x_button = menu_pos[i][0]
        y_button = menu_pos[i][1]

        # =====================================================
        # START FROM LEFT
        # =====================================================

        start_button_x = (
            -surface.get_width()
        )

        # =====================================================
        # ANIMATED X
        # =====================================================

        current_button_x = (
            start_button_x
            + (
                x_button
                - start_button_x
            )
            * button_progress
        )

        # =====================================================
        # FULL BUTTON RECT
        # =====================================================

        rect = surface.get_rect(
            topleft=(
                int(current_button_x),
                y_button
            )
        )

        # =====================================================
        # ICON RECT
        # =====================================================

        base_scale = size / 80.0

        icon_size = max(
            1,
            int(100 * base_scale)
        )

        icon_rect = pygame.Rect(
            0,
            0,
            icon_size,
            icon_size
        )

        # =====================================================
        # ICON POSITION
        # =====================================================

        icon_rect.topleft = (
            rect.x,
            rect.y
            + (
                rect.height
                - icon_rect.height
            ) // 2
        )

        # =====================================================
        # HOVER
        # =====================================================

        is_hover = icon_rect.collidepoint(
            mouse_pos
        )

        # =====================================================
        # CREATE SCALE
        # =====================================================

        if i not in hover_scales:

            hover_scales[i] = 1.0

        # =====================================================
        # TARGET SCALE
        # =====================================================

        if (
            is_hover
            or selected_button == i
        ):

            target_scale = 1.20

        else:

            target_scale = 1.0

        # =====================================================
        # SMOOTH HOVER
        # =====================================================

        hover_scales[i] += (
            target_scale
            - hover_scales[i]
        ) * 0.15

        # =====================================================
        # SCALE BUTTON
        # =====================================================

        draw_width = int(
            surface.get_width()
            * hover_scales[i]
        )

        draw_height = int(
            surface.get_height()
            * hover_scales[i]
        )

        draw_surface = pygame.transform.smoothscale(
            surface,
            (
                draw_width,
                draw_height
            )
        )

        # =====================================================
        # KEEP CENTER
        # =====================================================

        draw_rect = draw_surface.get_rect(
            center=rect.center
        )

        # =====================================================
        # DRAW BUTTON
        # =====================================================

        screen.blit(
            draw_surface,
            draw_rect
        )

        # =====================================================
        # CLICK RECT
        # ONLY IMAGE
        # =====================================================

        if MODE in (
            "menu",
            "setting",
            "gamemode"
        ):

            select_buttons_setting.append(
                icon_rect.copy()
            )


def reset_animation_button_in_menu_gamemode_setting():

    if hasattr(
        gamemode_menu_setting_panel,
        "start_time"
    ):
        del gamemode_menu_setting_panel.start_time
import pygame
from modules.font import fonts
from modules.ACCOUNT.FLAG import *


country_window = False
selected_country = None
country_rects = {}

# مقدار اسکرول
country_scroll = 0


country_button = pygame.Rect(
    400,
    500,
    300,
    70
)


# =========================================================
# LOAD FLAGS
# =========================================================

def load_flags():

    flags = {}

    for key, data in countries.items():

        image = pygame.image.load(
            data["image"]
        ).convert_alpha()

        image = pygame.transform.smoothscale(
            image,
            (120, 80)
        )

        flags[key] = image

    return flags


# =========================================================
# COUNTRY BUTTON
# =========================================================

def draw_country_button(
        screen,
        rect,
        selected_country=None
):

    pygame.draw.rect(
        screen,
        (50, 50, 50),
        rect,
        border_radius=20
    )

    if selected_country:

        text = countries[selected_country]["name"]

    else:

        text = "SELECT COUNTRY"

    text_image = fonts["heart"].render(
        text,
        True,
        (255, 255, 255)
    )

    screen.blit(
        text_image,
        text_image.get_rect(
            center=rect.center
        )
    )


# =========================================================
# COUNTRY WINDOW
# =========================================================

def draw_country_window(
        screen,
        flags,
        country_rects
):

    global country_scroll

    # -----------------------------------------------------
    # Window
    # -----------------------------------------------------

    window = pygame.Rect(
        300,
        150,
        600,
        500
    )

    pygame.draw.rect(
        screen,
        (30, 30, 30),
        window,
        border_radius=30
    )

    pygame.draw.rect(
        screen,
        (255, 255, 255),
        window,
        width=3,
        border_radius=30
    )

    # -----------------------------------------------------
    # Title
    # -----------------------------------------------------

    title = fonts["heart"].render(
        "SELECT COUNTRY",
        True,
        (255, 255, 255)
    )

    screen.blit(
        title,
        title.get_rect(
            center=(window.centerx, 190)
        )
    )

    # -----------------------------------------------------
    # Scroll Area
    # -----------------------------------------------------

    list_rect = pygame.Rect(
        window.x + 30,
        225,
        window.width - 60,
        window.height - 55
    )

    # -----------------------------------------------------
    # Clip
    # -----------------------------------------------------

    old_clip = screen.get_clip()

    screen.set_clip(list_rect)

    # -----------------------------------------------------
    # Country positions
    # -----------------------------------------------------

    country_rects.clear()

    start_x = list_rect.centerx
    start_y = list_rect.top + 60

    gap_y = 105

    y = start_y + country_scroll

    for key, image in flags.items():

        rect = image.get_rect(
            center=(start_x, y)
        )

        # فقط کشورهایی که در محدوده هستند
        # برای کلیک قابل استفاده باشند
        if list_rect.colliderect(rect):

            screen.blit(
                image,
                rect
            )

            country_rects[key] = rect

        y += gap_y

    # -----------------------------------------------------
    # Restore Clip
    # -----------------------------------------------------

    screen.set_clip(old_clip)

    # -----------------------------------------------------
    # Border of list
    # -----------------------------------------------------

    pygame.draw.rect(
        screen,
        (80, 80, 80),
        list_rect,
        width=2,
        border_radius=15
    )

    # -----------------------------------------------------
    # Calculate max scroll
    # -----------------------------------------------------

    total_height = len(flags) * gap_y

    visible_height = list_rect.height

    max_scroll = max(
        0,
        visible_height - total_height - 20
    )

    # اینجا محدودش می‌کنیم
    country_scroll = max(
        max_scroll,
        min(0, country_scroll)
    )

    # -----------------------------------------------------
    # Scroll bar
    # -----------------------------------------------------

    if total_height > visible_height:

        scrollbar_area = pygame.Rect(
            window.right - 18,
            list_rect.top,
            8,
            list_rect.height
        )

        pygame.draw.rect(
            screen,
            (60, 60, 60),
            scrollbar_area,
            border_radius=4
        )

        # اندازه Scrollbar
        ratio = visible_height / total_height

        bar_height = max(
            40,
            int(visible_height * ratio)
        )

        scroll_range = (
            visible_height - bar_height
        )

        scroll_ratio = 0

        if max_scroll != 0:

            scroll_ratio = (
                -country_scroll / -max_scroll
            )

        bar_y = (
            list_rect.top
            + int(scroll_range * scroll_ratio)
        )

        scrollbar = pygame.Rect(
            window.right - 18,
            bar_y,
            8,
            bar_height
        )

        pygame.draw.rect(
            screen,
            (180, 180, 180),
            scrollbar,
            border_radius=4
        )


# =========================================================
# COUNTRY EVENT
# =========================================================

def country_event_(
        mouse_pos,
        country_rects
):

    for country, rect in country_rects.items():

        if rect.collidepoint(mouse_pos):

            return country

    return None


# =========================================================
# COUNTRY EVENT
# =========================================================

def country_event(
        event,
        country_button,
        country_rects,
        country_window,
        selected_country
):

    global country_scroll

    mouse_pos = pygame.mouse.get_pos()

    # -----------------------------------------------------
    # Mouse Button
    # -----------------------------------------------------

    if event.type == pygame.MOUSEBUTTONDOWN:

        # ---------------------------------------------
        # Left Click
        # ---------------------------------------------

        if event.button == 1:

            # Open window
            if country_button.collidepoint(mouse_pos):

                country_window = True

                # هر بار از اول باز شود
                country_scroll = 0

            # Select country
            elif country_window:

                result = country_event_(
                    mouse_pos,
                    country_rects
                )

                if result:

                    selected_country = result

                    country_window = False

                    # بعد از انتخاب دوباره اول لیست
                    country_scroll = 0

        # ---------------------------------------------
        # Mouse Wheel Up
        # ---------------------------------------------

        elif event.button == 4:

            if country_window:

                country_scroll += 40

        # ---------------------------------------------
        # Mouse Wheel Down
        # ---------------------------------------------

        elif event.button == 5:

            if country_window:

                country_scroll -= 40

    return (
        country_window,
        selected_country
    )


# =========================================================
# SELECTED FLAG
# =========================================================

def draw_selected_flag(
    screen,
    flags,
    selected_country
):

    if selected_country:

        image = flags[selected_country]

        rect = image.get_rect(
            center=(500, 150)
        )

        screen.blit(
            image,
            rect
        )
import pygame
import random

# =========================================================
# VERTICAL SCROLL GRID
# =========================================================


SCROLL_SPEED = 50
scroll_y = 0.0
target_scroll_y = 0.0
punch_hidden_duration = 1000
SCROLL_SPEED = 350
SCROLL_SMOOTH = 0.08
# =========================================================
# RESET SCROLL
# =========================================================

def reset_scroll():

    global scroll_y

    scroll_y = 0


# =========================================================
# EVENT
# =========================================================
def event_vertical_scroll(event, screen, images):

    global target_scroll_y

    if event.type == pygame.MOUSEWHEEL:

        target_scroll_y += (
            -event.y
            * 60
        )

        # =================================================
        # CALCULATE MAX SCROLL
        # =================================================

        cols = 3
        card_gap_y = 500

        screen_height = screen.get_height()

        rows = (
            (len(images) + cols - 1)
            // cols
        )

        content_height = (
            rows * card_gap_y
        )

        max_scroll = max(
            0,
            content_height
            - screen_height
            + 100
        )

        # =================================================
        # LIMIT TARGET
        # =================================================

        target_scroll_y = max(
            -max_scroll,
            min(
                0,
                target_scroll_y
            )
        )
            
            
def update_vertical_scroll():

    global scroll_y
    global target_scroll_y

    scroll_y += (
        target_scroll_y
        - scroll_y
    ) * SCROLL_SMOOTH   
# =========================================================
# DRAW
# =========================================================
# =========================================================
# PUNCH EFFECT
# =========================================================

punch_index = []
punch_start_time = pygame.time.get_ticks()

punch_grow_duration = 100
punch_fade_duration = 250
punch_zoom_in_duration = 300
punch_wait_duration = 300

punch_scale = 1.5


def draw_vertical_scroll_grid(
    screen,
    images,
    center_image,
    card_gap_x=500,
    card_gap_y=500
):

    global scroll_y
    global punch_index
    global punch_start_time

    screen_width = screen.get_width()
    screen_height = screen.get_height()

    cols = 3

    center_x = screen_width // 2 + 150
    center_y = screen_height // 2

    total_width = 2 * card_gap_x

    start_x = center_x - total_width // 2 
    start_y = center_y - card_gap_y // 2 + scroll_y

    now = pygame.time.get_ticks()
    elapsed = now - punch_start_time


    # =====================================================
    # TOTAL CYCLE
    # =====================================================

    total_duration = (
        punch_grow_duration
        + punch_fade_duration
        + punch_hidden_duration
        + punch_zoom_in_duration
        + punch_wait_duration
    )


    # =====================================================
    # SELECT 2 NEW RANDOM IMAGES
    # =====================================================

    if elapsed >= total_duration:

        if len(images) >= 2:

            punch_index = random.sample(
                range(len(images)),
                2
            )

        elif len(images) == 1:

            punch_index = [0]

        else:

            punch_index = []

        punch_start_time = now
        elapsed = 0


    # =====================================================
    # DRAW
    # =====================================================

    for i, image in enumerate(images):

        center_ = center_image[i]

        row = i // cols
        col = i % cols

        x = start_x + col * card_gap_x
        y = start_y + row * card_gap_y


        # =================================================
        # FRAME
        # =================================================

        rect = image.get_rect(
            center=(x, y)
        )


        # =================================================
        # CENTER IMAGE
        # =================================================

        draw_center_image = center_

        draw_center_rect = center_.get_rect(
            center=(x, y)
        )


        # =================================================
        # PUNCH
        # =================================================

        if i in punch_index:

            # ---------------------------------------------
            # 1. GROW
            # ---------------------------------------------

            if elapsed < punch_grow_duration:

                progress = (
                    elapsed /
                    punch_grow_duration
                )

                scale = 1 + (
                    (punch_scale - 1)
                    * progress
                )

                alpha = 255


            # ---------------------------------------------
            # 2. SHRINK + FADE
            # ---------------------------------------------

            elif elapsed < (
                punch_grow_duration
                + punch_fade_duration
            ):

                progress = (
                    elapsed
                    - punch_grow_duration
                ) / punch_fade_duration

                scale = punch_scale - (
                    (punch_scale - 1)
                    * progress
                )

                alpha = int(
                    255 * (1 - progress)
                )


            # ---------------------------------------------
            # 3. ZOOM IN
            # ---------------------------------------------

            elif elapsed < (
                punch_grow_duration
                + punch_fade_duration
                + punch_hidden_duration
                + punch_zoom_in_duration
            ):

                progress = (
                    elapsed
                    - punch_grow_duration
                    - punch_fade_duration
                    - punch_hidden_duration
                ) / punch_zoom_in_duration

                # از کوچک شروع شود و به اندازه اصلی برسد
                scale = progress

                alpha = int(
                    255 * progress
                )


            # ---------------------------------------------
            # 4. NORMAL
            # ---------------------------------------------

            else:

                scale = 1
                alpha = 255


            # =================================================
            # SCALE CENTER IMAGE
            # =================================================

            center_width = max(
                1,
                int(
                    center_.get_width()
                    * scale
                )
            )

            center_height = max(
                1,
                int(
                    center_.get_height()
                    * scale
                )
            )


            draw_center_image = pygame.transform.smoothscale(
                center_,
                (
                    center_width,
                    center_height
                )
            )


            draw_center_image.set_alpha(
                alpha
            )


            draw_center_rect = (
                draw_center_image.get_rect(
                    center=(x, y)
                )
            )


        # =================================================
        # VISIBILITY
        # =================================================

        if (
            rect.bottom < 0
            or rect.top > screen_height
        ):
            continue


        # =================================================
        # FRAME — NEVER SCALES
        # =================================================

        screen.blit(
            image,
            rect
        )


        # =================================================
        # CENTER IMAGE
        # =================================================

        screen.blit(
            draw_center_image,
            draw_center_rect
        )
import pygame
import random


# ============================================================
# GENERAL RANDOM SIDE EFFECT
# ============================================================

side_effect_start_times = {}

side_effect_order = []

side_effect_initialized = False

side_effect_total_images = None
# ============================================================
# RESET
# ============================================================

def reset_side_effect():

    global side_effect_start_times
    global side_effect_order
    global side_effect_initialized
    global side_effect_total_images

    side_effect_start_times.clear()

    side_effect_order = []

    side_effect_initialized = False

    side_effect_total_images = None

# ============================================================
# RANDOM SIDE EFFECT
# ============================================================
def draw_random_side_effect(
    screen,
    image,
    target_x,
    target_y,
    index,
    total_images,
    image_size=None,
    duration=600,
    delay=120
):

    global side_effect_order
    global side_effect_initialized
    global side_effect_total_images


    # ========================================================
    # CREATE RANDOM ORDER
    # ========================================================

    if (
        not side_effect_initialized
        or side_effect_total_images != total_images
    ):

        side_effect_order = list(
            range(total_images)
        )

        random.shuffle(
            side_effect_order
        )

        side_effect_initialized = True

        side_effect_total_images = total_images

        side_effect_start_times.clear()


    # ========================================================
    # CHECK INDEX
    # ========================================================

    if index not in side_effect_order:
        return


    # ========================================================
    # START TIME
    # ========================================================

    if index not in side_effect_start_times:

        order_index = side_effect_order.index(
            index
        )

        side_effect_start_times[index] = (
            pygame.time.get_ticks()
            +
            order_index * delay
        )


    start_time = side_effect_start_times[index]

    # بقیه کدت...
    # ========================================================
    # TIME
    # ========================================================

    now = pygame.time.get_ticks()

    elapsed = (
        now - start_time
    )


    # ========================================================
    # WAIT
    # ========================================================

    if elapsed < 0:

        return


    # ========================================================
    # PROGRESS
    # ========================================================

    if elapsed >= duration:

        progress = 1.0

    else:

        progress = (
            elapsed / duration
        )

        # Ease Out
        progress = (
            1
            -
            (1 - progress) ** 3
        )


    # ========================================================
    # START POSITION
    # ========================================================

    if image_size is None:

        width = image.get_width()

    else:

        width = image_size


    start_x = (
        screen.get_width()
        + width
    )


    # ========================================================
    # CURRENT POSITION
    # ========================================================

    current_x = (
        start_x
        +
        (
            target_x
            -
            start_x
        )
        *
        progress
    )


    # ========================================================
    # DRAW
    # ========================================================

    rect = image.get_rect(

        center=(

            int(current_x),

            int(target_y)

        )

    )


    screen.blit(
        image,
        rect
    )
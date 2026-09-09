from modules.support import *
import pygame
from modules.font import *

from modules import policy as PO


def open_window_with_side_effect(
    screen,
    image,
    x,
    y,
    on_draw=None
):

    if not hasattr(open_window_with_side_effect, "start_time"):
        open_window_with_side_effect.start_time = pygame.time.get_ticks()

    now = pygame.time.get_ticks()

    elapsed = (
        now - open_window_with_side_effect.start_time
    )

    duration = 600

    if elapsed >= duration:
        progress = 1.0
    else:
        progress = elapsed / duration
        progress = 1 - (1 - progress) ** 3

    start_x = (
        screen.get_width()
        + image.get_width()
    )

    current_x = (
        start_x
        + (x - start_x) * progress
    )

    rect = image.get_rect(
        center=(int(current_x), y)
    )

    # پنجره
    screen.blit(
        image,
        rect
    )

    # تابع جانبی
    if on_draw:
        on_draw(
            screen,
            rect
        )



































# ============================================================
# RESET
# ============================================================

def reset_window_side_effect():

    if hasattr(
        open_window_with_side_effect,
        "start_time"
    ):

        del open_window_with_side_effect.start_time
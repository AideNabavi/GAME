import pygame
from modules.custom_math import   *


menu_in_middle_of_play=None











menu_images = [
    pygame.image.load("./asset/image/rank.png").convert_alpha(),
    pygame.image.load("./asset/image/rank.png").convert_alpha(),
    pygame.image.load("./asset/image/rank.png").convert_alpha()
]

menu_centers = [
    (500, 300),
    (500, 450),
    (500, 600)
]

menu_sizes = [
    (300, 100),
    (300, 100),
    (300, 100)
]








def draw_punch_images_in(
    screen,
    images,
    centers,
    target_sizes,
    page_id,
    duration=450
):
    """
    چند تصویر را همزمان با افکت PUNCH رسم می‌کند.

    images:
        لیست Surface های تصاویر

    centers:
        محل مرکز هر تصویر
        [(500, 300), (700, 300), ...]

    target_sizes:
        اندازه نهایی هر تصویر
        [(200, 100), (200, 100), ...]

    page_id:
        شناسه صفحه برای کنترل انیمیشن

    duration:
        مدت انیمیشن بر حسب میلی‌ثانیه
    """

    now = pygame.time.get_ticks()

    # ========================================================
    # ANIMATION STORAGE
    # ========================================================

    if not hasattr(draw_punch_image, "_animations"):
        draw_punch_image._animations = {}

    if page_id not in draw_punch_image._animations:

        draw_punch_image._animations[page_id] = {
            "start_time": now,
            "finished": False
        }

    animation = draw_punch_image._animations[page_id]

    elapsed = now - animation["start_time"]

    # ========================================================
    # PUNCH SCALE
    # ========================================================

    if not animation["finished"]:

        if elapsed >= duration:

            animation["finished"] = True
            scale = 1.0

        else:

            progress = elapsed / duration

            if progress < 0.55:

                p = progress / 0.55

                start = 0.20
                end = 1.12

                p = 1 - (1 - p) ** 4

                scale = start + (end - start) * p

            else:

                p = (progress - 0.55) / 0.45

                start = 1.12
                end = 1.0

                p = 1 - (1 - p) ** 3

                scale = start + (end - start) * p

    else:

        scale = 1.0

    # ========================================================
    # IMAGE CACHE
    # ========================================================

    if not hasattr(draw_punch_image, "_image_cache"):
        draw_punch_image._image_cache = {}

    cache = draw_punch_image._image_cache

    # ========================================================
    # DRAW ALL IMAGES
    # ========================================================

    for image, center, target_size in zip(
        images,
        centers,
        target_sizes
    ):

        width = max(
            1,
            int(target_size[0] * scale)
        )

        height = max(
            1,
            int(target_size[1] * scale)
        )

        cache_key = (
            id(image),
            width,
            height
        )

        if cache_key not in cache:

            cache[cache_key] = pygame.transform.smoothscale(
                image,
                (width, height)
            )

        scaled_image = cache[cache_key]

        # ====================================================
        # RECT
        # ====================================================

        rect = scaled_image.get_rect(
            center=center
        )

        screen.blit(
            scaled_image,
            rect
        )
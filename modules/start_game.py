


import pygame
import time
import random
import math


# ============================================================
# COUNTDOWN ASSETS
# ============================================================

countdown_images = [
    pygame.image.load(
        "./asset/image/three.png"
    ).convert_alpha(),

    pygame.image.load(
        "./asset/image/two.png"
    ).convert_alpha(),

    pygame.image.load(
        "./asset/image/one.png"
    ).convert_alpha()
]


countdown_sounds = [
    pygame.mixer.Sound(
        "./asset/sound/countdown.mp3"
    ),
    pygame.mixer.Sound(
        "./asset/sound/countdown.mp3"
    ),
    pygame.mixer.Sound(
        "./asset/sound/countdown.mp3"
    )
]
def countdown(screen, background):

    screen_width, screen_height = screen.get_size()

    countdown_data = zip(
        countdown_images,
        countdown_sounds
    )

    # ========================================================
    # Settings
    # ========================================================

    final_size = 700

    start_scale = 0.08
    hit_scale = 1.20

    punch_time = 0.350
    hold_time = 0.30
    fade_time = 0.350

    clock = pygame.time.Clock()

    # ========================================================
    # 3 → 2 → 1
    # ========================================================

    for image, sound in countdown_data:

        sound.play()

        # ----------------------------------------------------
        # Number Size
        # ----------------------------------------------------

        original_width = image.get_width()
        original_height = image.get_height()

        ratio = min(
            final_size / original_width,
            final_size / original_height
        )

        base_width = int(
            original_width * ratio
        )

        base_height = int(
            original_height * ratio
        )

        base_image = pygame.transform.smoothscale(
            image,
            (
                base_width,
                base_height
            )
        )

        # ====================================================
        # PUNCH
        # ====================================================

        start_time = time.perf_counter()

        while True:

            elapsed = (
                time.perf_counter()
                - start_time
            )

            progress = elapsed / punch_time

            if progress >= 1:
                progress = 1
                break

            # =================================================
            # ثابت ماندن Background
            # =================================================

            screen.blit(
                background,
                background.get_rect(
                    center=(
                        screen_width // 2,
                        screen_height // 2
                    )
                )
            )

            # =================================================
            # Number Punch
            # =================================================

            ease = (
                1
                -
                (1 - progress) ** 3
            )

            scale = (
                start_scale
                +
                (
                    hit_scale
                    - start_scale
                )
                * ease
            )

            width = int(
                base_width
                * scale
            )

            height = int(
                base_height
                * scale
            )

            animated_image = pygame.transform.smoothscale(
                base_image,
                (
                    width,
                    height
                )
            )

            animated_image.set_alpha(255)

            rect = animated_image.get_rect(
                center=(
                    screen_width // 2,
                    screen_height // 2
                )
            )

            screen.blit(
                animated_image,
                rect
            )

            pygame.display.flip()

            clock.tick(120)

        # ====================================================
        # HOLD
        # ====================================================

        start_time = time.perf_counter()

        while True:

            elapsed = (
                time.perf_counter()
                - start_time
            )

            if elapsed >= hold_time:
                break

            # ------------------------------------------------
            # Background ثابت
            # ------------------------------------------------

            screen.blit(
                background,
                background.get_rect(
                    center=(
                        screen_width // 2,
                        screen_height // 2
                    )
                )
            )

            # ------------------------------------------------
            # Number
            # ------------------------------------------------

            rect = base_image.get_rect(
                center=(
                    screen_width // 2,
                    screen_height // 2
                )
            )

            screen.blit(
                base_image,
                rect
            )

            pygame.display.flip()

            clock.tick(120)

        # ====================================================
        # FADE OUT
        # ====================================================

        start_time = time.perf_counter()

        while True:

            elapsed = (
                time.perf_counter()
                - start_time
            )

            progress = elapsed / fade_time

            if progress >= 1:
                progress = 1
                break

            # ------------------------------------------------
            # Background ثابت
            # ------------------------------------------------

            screen.blit(
                background,
                background.get_rect(
                    center=(
                        screen_width // 2,
                        screen_height // 2
                    )
                )
            )

            # =================================================
            # Number Fade
            # =================================================

            alpha = int(
                255
                *
                (1 - progress)
            )

            # کمی Zoom هنگام محو شدن
            scale = (
                1.0
                +
                0.08 * progress
            )

            width = int(
                base_width
                * scale
            )

            height = int(
                base_height
                * scale
            )

            animated_image = pygame.transform.smoothscale(
                base_image,
                (
                    width,
                    height
                )
            )

            animated_image.set_alpha(
                alpha
            )

            rect = animated_image.get_rect(
                center=(
                    screen_width // 2,
                    screen_height // 2
                )
            )

            screen.blit(
                animated_image,
                rect
            )

            pygame.display.flip()

            clock.tick(120)

    # ========================================================
    # Final Background
    # ========================================================

    screen.blit(
        background,
        background.get_rect(
            center=(
                screen_width // 2,
                screen_height // 2
            )
        )
    )

    pygame.display.flip()

    return True
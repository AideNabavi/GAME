import pygame
import math


def draw_timer_circle(screen, center, radius, progress):

    progress = max(0, min(1, progress))

    TOTAL_TIME = 10

    time_left = math.ceil(progress * TOTAL_TIME)

    # =========================================================
    # رنگ
    # =========================================================

    if progress > 0.65:
        color = (0, 220, 80)

    elif progress > 0.25:
        color = (255, 200, 0)

    else:
        color = (255, 50, 50)

    # =========================================================
    # Anti-Aliasing
    # =========================================================

    SCALE = 4

    big_radius = radius * SCALE
    big_center = (big_radius, big_radius)

    size = big_radius * 2

    timer_surface = pygame.Surface(
        (size, size),
        pygame.SRCALPHA
    )

    # =========================================================
    # حلقه پس‌زمینه
    # =========================================================

    pygame.draw.circle(
        timer_surface,
        (40, 40, 40, 255),
        big_center,
        big_radius,
        12 * SCALE
    )

    # =========================================================
    # حلقه تایمر
    #
    # شروع دقیقاً از ساعت 12
    # =========================================================

    if progress > 0:

        start_angle = -math.pi / 2

        end_angle = (
            start_angle +
            (2 * math.pi * progress)
        )

        rect = pygame.Rect(
            0,
            0,
            size,
            size
        )

        pygame.draw.arc(
            timer_surface,
            (*color, 255),
            rect,
            start_angle,
            end_angle,
            12 * SCALE
        )

    # =========================================================
    # کوچک کردن برای حذف خط‌خطی
    # =========================================================

    timer_surface = pygame.transform.smoothscale(
        timer_surface,
        (radius * 2, radius * 2)
    )

    # =========================================================
    # قرار دادن حلقه روی صفحه
    # =========================================================

    screen.blit(
        timer_surface,
        (
            center[0] - radius,
            center[1] - radius
        )
    )

    # =========================================================
    # عدد وسط حلقه
    # =========================================================

    font = pygame.font.Font(
        None,
        int(radius * 0.65)
    )

    text = font.render(
        str(time_left),
        True,
        (255, 255, 255)
    )

    text_rect = text.get_rect(
        center=center
    )

    screen.blit(
        text,
        text_rect
    )
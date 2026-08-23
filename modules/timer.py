import pygame


def draw_timer_bar(screen, rect, progress):

    progress = max(0, min(1, progress))


    # پس زمینه نوار
    pygame.draw.rect(
        screen,
        (40, 40, 40),
        rect,
        border_radius=rect.height // 2
    )


    # عرض قسمت پر شده
    fill_width = int(
        rect.width * progress
    )


    fill_rect = pygame.Rect(
        rect.x,
        rect.y,
        fill_width,
        rect.height
    )


    # تغییر رنگ بر اساس زمان
    if progress > 0.65:
        color = (0, 220, 80)

    elif progress > 0.25:
        color = (255, 200, 0)

    else:
        color = (255, 50, 50)


    pygame.draw.rect(
        screen,
        color,
        fill_rect,
        border_radius=rect.height // 2
    )


    # قاب دور نوار
    pygame.draw.rect(
        screen,
        (220, 220, 220),
        rect,
        2,
        border_radius=rect.height // 2
    )
    
    
    
    
    
    
    


# def draw_timer_circle(screen, center, radius, progress):

#     progress = max(0, min(1, progress))

#     # تغییر رنگ بر اساس زمان
#     if progress > 0.65:
#         color = (0, 220, 80)

#     elif progress > 0.25:
#         color = (255, 200, 0)

#     else:
#         color = (255, 50, 50)

#     # شعاع فعلی بر اساس زمان
#     current_radius = int(radius * progress)

#     # دایره اصلی
#     if current_radius > 0:
#         pygame.draw.circle(
#             screen,
#             color,
#             center,
#             current_radius
#         )

#     # قاب دور دایره
#     pygame.draw.circle(
#         screen,
#         (220, 220, 220),
#         center,
#         radius,
#         2
#     )

import pygame
import math


def draw_timer_circle(screen, center, radius, progress):

    progress = max(0, min(1, progress))

    # رنگ
    if progress > 0.65:
        color = (0, 220, 80)

    elif progress > 0.25:
        color = (255, 200, 0)

    else:
        color = (255, 50, 50)

    # # دایره خالیِ پشت
    # pygame.draw.circle(
    #     screen,
    #     (40, 40, 40),
    #     center,
    #     radius
    # )

    # دایره باقی‌مانده
    if progress > 0:

        # شروع از ساعت 12
        start_angle = -math.pi / 2

        # زاویه باقی‌مانده
        end_angle = start_angle - (
            2 * math.pi * progress
        )

        points = [center]

        steps = 100

        for i in range(steps + 1):

            angle = (
                start_angle
                + (end_angle - start_angle)
                * i / steps
            )

            x = center[0] + math.cos(angle) * radius
            y = center[1] + math.sin(angle) * radius

            points.append((x, y))

        pygame.draw.polygon(
            screen,
            color,
            points
        )

    # قاب
    # pygame.draw.circle(
    #     screen,
    #     (220, 220, 220),
    #     center,
    #     radius,
    #     2
    # )
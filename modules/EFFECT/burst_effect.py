


# draw_bell_icon(
#     screen,
#     icon_image__,
#     current_width//2,
#     current_height // 2
# )        
        
import pygame
import math
# def draw_bell_icon(
#     screen,
#     image,
#     x,
#     y
# ):

#     if not hasattr(draw_bell_icon, "start_time"):
#         draw_bell_icon.start_time = pygame.time.get_ticks()

#     elapsed = pygame.time.get_ticks() - draw_bell_icon.start_time

#     delay = 3000
#     duration = 500

#     cycle = delay + duration

#     current = elapsed % cycle


#     # -----------------------------
#     # ثابت
#     # -----------------------------

#     if current < delay:

#         rect = image.get_rect(
#             center=(x, y)
#         )

#         screen.blit(
#             image,
#             rect
#         )

#         return


#     # -----------------------------
#     # Bell animation
#     # -----------------------------

#     t = (current - delay) / duration

#     strength = math.sin(t * math.pi)

#     angle = math.sin(
#         t * math.pi * 6
#     ) * 12 * strength


#     rotated = pygame.transform.rotate(
#         image,
#         angle
#     )


#     # مرکز همیشه ثابت می‌ماند
#     rect = rotated.get_rect(
#         center=(x, y)
#     )


#     screen.blit(
#         rotated,
#         rect
#     )











# draw_pop_icon(
#     screen,
#     icon_image__,
#     current_width // 2,
#     current_height // 2
# )


# def draw_pop_icon(
#     screen,
#     image,
#     x,
#     y
# ):

#     if not hasattr(draw_pop_icon, "start_time"):
#         draw_pop_icon.start_time = pygame.time.get_ticks()

#     elapsed = pygame.time.get_ticks() - draw_pop_icon.start_time

#     delay = 3000
#     duration = 500

#     cycle = delay + duration

#     current = elapsed % cycle


#     # -----------------------------
#     # ثابت
#     # -----------------------------

#     if current < delay:

#         rect = image.get_rect(
#             center=(x, y)
#         )

#         screen.blit(
#             image,
#             rect
#         )

#         return


#     # -----------------------------
#     # Pop animation
#     # -----------------------------

#     t = (current - delay) / duration


#     # پف کردن
#     scale = 1 + math.sin(t * math.pi) * 0.18


#     # کمی بالا و پایین
#     bounce = math.sin(t * math.pi) * 8


#     width = int(
#         image.get_width() * scale
#     )

#     height = int(
#         image.get_height() * scale
#     )


#     scaled = pygame.transform.smoothscale(
#         image,
#         (width, height)
#     )


#     rect = scaled.get_rect(
#         center=(
#             x,
#             y - bounce
#         )
#     )


#     screen.blit(
#         scaled,
#         rect
#     )













# def draw_squash_icon(
#     screen,
#     image,
#     x,
#     y
# ):

#     if not hasattr(draw_squash_icon, "start_time"):
#         draw_squash_icon.start_time = pygame.time.get_ticks()

#     elapsed = pygame.time.get_ticks() - draw_squash_icon.start_time

#     delay = 3000
#     duration = 500

#     cycle = delay + duration

#     current = elapsed % cycle


#     # ثابت
#     if current < delay:

#         rect = image.get_rect(
#             center=(x, y)
#         )

#         screen.blit(
#             image,
#             rect
#         )

#         return


#     # Animation
#     t = (current - delay) / duration


#     # موج نرم
#     wave = math.sin(t * math.pi)


#     # فشرده افقی
#     scale_x = 1 + wave * 0.18

#     # کشیده عمودی
#     scale_y = 1 - wave * 0.18


#     width = int(
#         image.get_width() * scale_x
#     )

#     height = int(
#         image.get_height() * scale_y
#     )


#     scaled = pygame.transform.smoothscale(
#         image,
#         (width, height)
#     )


#     rect = scaled.get_rect(
#         center=(x, y)
#     )


#     screen.blit(
#         scaled,
#         rect
#     )







# import pygame
# import math
# import random


# def draw_sparkle_icon(
#     screen,
#     image,
#     x,
#     y
# ):

#     if not hasattr(draw_sparkle_icon, "start_time"):

#         draw_sparkle_icon.start_time = pygame.time.get_ticks()

#         draw_sparkle_icon.particles = []


#     elapsed = (
#         pygame.time.get_ticks()
#         - draw_sparkle_icon.start_time
#     )


#     delay = 3000
#     duration = 700

#     cycle = delay + duration

#     current = elapsed % cycle


#     # -----------------------------
#     # آیکون
#     # -----------------------------

#     rect = image.get_rect(
#         center=(x, y)
#     )

#     screen.blit(
#         image,
#         rect
#     )


#     # -----------------------------
#     # زمان ساخت ذرات
#     # -----------------------------

#     if current >= delay:

#         animation_time = current - delay

#         t = animation_time / duration


#         # فقط ابتدای افکت ذرات را بساز
#         if not draw_sparkle_icon.particles:

#             for i in range(10):

#                 angle = random.uniform(
#                     0,
#                     math.pi * 2
#                 )

#                 distance = random.uniform(
#                     30,
#                     55
#                 )

#                 size = random.randint(
#                     2,
#                     5
#                 )

#                 draw_sparkle_icon.particles.append(
#                     (
#                         angle,
#                         distance,
#                         size
#                     )
#                 )


#         # -----------------------------
#         # رسم ذرات
#         # -----------------------------

#         alpha = int(
#             255 * (1 - t)
#         )

#         for angle, distance, size in draw_sparkle_icon.particles:

#             # حرکت ذرات به بیرون
#             current_distance = (
#                 distance
#                 + t * 25
#             )


#             px = x + math.cos(angle) * current_distance
#             py = y + math.sin(angle) * current_distance


#             particle = pygame.Surface(
#                 (size * 2, size * 2),
#                 pygame.SRCALPHA
#             )


#             pygame.draw.circle(
#                 particle,
#                 (255, 255, 255, alpha),
#                 (size, size),
#                 size
#             )


#             screen.blit(
#                 particle,
#                 (
#                     int(px - size),
#                     int(py - size)
#                 )
#             )


#     else:

#         # برای اجرای بعدی دوباره ذرات ساخته شوند
#         draw_sparkle_icon.particles = []











# import pygame
# import math


# def draw_impact_icon(
#     screen,
#     image,
#     x,
#     y
# ):

#     if not hasattr(draw_impact_icon, "start_time"):
#         draw_impact_icon.start_time = pygame.time.get_ticks()

#     elapsed = (
#         pygame.time.get_ticks()
#         - draw_impact_icon.start_time
#     )

#     delay = 3000
#     duration = 500

#     cycle = delay + duration

#     current = elapsed % cycle


#     # -----------------------------
#     # حالت عادی
#     # -----------------------------

#     if current < delay:

#         rect = image.get_rect(
#             center=(x, y)
#         )

#         screen.blit(
#             image,
#             rect
#         )

#         return


#     # -----------------------------
#     # Impact
#     # -----------------------------

#     t = (current - delay) / duration


#     # -----------------------------
#     # Scale
#     # -----------------------------

#     # ضربه:
#     # کوچک → بزرگ → عادی

#     scale = (
#         1
#         - 0.12 * math.sin(t * math.pi)
#         + 0.20 * math.sin(t * math.pi * 2)
#     )


#     # -----------------------------
#     # Shake
#     # -----------------------------

#     shake_strength = (
#         10 * math.sin(t * math.pi)
#     )

#     shake_x = (
#         math.sin(t * math.pi * 12)
#         * shake_strength
#     )

#     shake_y = (
#         math.cos(t * math.pi * 10)
#         * shake_strength * 0.5
#     )


#     # -----------------------------
#     # Scale image
#     # -----------------------------

#     width = int(
#         image.get_width() * scale
#     )

#     height = int(
#         image.get_height() * scale
#     )

#     scaled = pygame.transform.smoothscale(
#         image,
#         (width, height)
#     )


#     # -----------------------------
#     # Position
#     # -----------------------------

#     rect = scaled.get_rect(
#         center=(
#             x + shake_x,
#             y + shake_y
#         )
#     )


#     screen.blit(
#         scaled,
#         rect
#     )







import pygame
import math
import random


def draw_burst_icon(
    screen,
    image,
    x,
    y
):

    if not hasattr(draw_burst_icon, "start_time"):

        draw_burst_icon.start_time = pygame.time.get_ticks()
        draw_burst_icon.particles = []


    elapsed = (
        pygame.time.get_ticks()
        - draw_burst_icon.start_time
    )


    # -----------------------------
    # زمان ها
    # -----------------------------

    show_time = 3000
    burst_time = 700
    hidden_time = 1000
    fade_in_time = 400

    cycle = (
        show_time
        + burst_time
        + hidden_time
        + fade_in_time
    )

    current = elapsed % cycle


    # ==================================================
    # نمایش عادی
    # ==================================================

    if current < show_time:

        image.set_alpha(255)

        rect = image.get_rect(
            center=(x, y)
        )

        screen.blit(
            image,
            rect
        )

        return


    # ==================================================
    # ساخت ذرات
    # ==================================================

    if not draw_burst_icon.particles:

        for i in range(20):

            angle = random.uniform(
                0,
                math.pi * 2
            )

            speed = random.uniform(
                50,
                110
            )

            size = random.randint(
                2,
                5
            )

            draw_burst_icon.particles.append(
                (
                    angle,
                    speed,
                    size
                )
            )


    # ==================================================
    # انفجار
    # ==================================================

    burst_elapsed = current - show_time


    if burst_elapsed < burst_time:

        t = burst_elapsed / burst_time


        scale = (
            1
            + math.sin(t * math.pi) * 0.35
        )


        if t < 0.45:

            alpha = 255

        else:

            fade = (
                (t - 0.45)
                / 0.55
            )

            alpha = int(
                255 * (1 - fade)
            )


        width = int(
            image.get_width() * scale
        )

        height = int(
            image.get_height() * scale
        )


        scaled = pygame.transform.smoothscale(
            image,
            (width, height)
        )

        scaled.set_alpha(alpha)


        rect = scaled.get_rect(
            center=(x, y)
        )

        screen.blit(
            scaled,
            rect
        )


        # -----------------------------
        # ذرات
        # -----------------------------

        for angle, speed, size in draw_burst_icon.particles:

            distance = speed * t

            px = (
                x
                + math.cos(angle) * distance
            )

            py = (
                y
                + math.sin(angle) * distance
            )

            particle_alpha = int(
                255 * (1 - t)
            )


            particle = pygame.Surface(
                (size * 2, size * 2),
                pygame.SRCALPHA
            )


            pygame.draw.circle(
                particle,
                (255, 255, 255, particle_alpha),
                (size, size),
                size
            )


            screen.blit(
                particle,
                (
                    int(px - size),
                    int(py - size)
                )
            )


        return


    # ==================================================
    # محو کامل
    # ==================================================

    hidden_start = show_time + burst_time

    hidden_end = hidden_start + hidden_time


    if current < hidden_end:

        # هیچ چیزی نمایش داده نمی‌شود

        return


    # ==================================================
    # Fade In
    # ==================================================

    fade_elapsed = current - hidden_end

    fade_t = fade_elapsed / fade_in_time

    alpha = int(
        255 * fade_t
    )


    image.set_alpha(alpha)


    rect = image.get_rect(
        center=(x, y)
    )


    screen.blit(
        image,
        rect
    )


    # -----------------------------
    # آماده برای چرخه بعدی
    # -----------------------------

    if current >= cycle - 1:

        draw_burst_icon.particles = []
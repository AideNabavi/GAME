import pygame


# ============================================================
# IMAGE
# ============================================================
# ============================================================
# PUNCH IMAGES
# ============================================================

punch_1 = pygame.transform.smoothscale(
    pygame.image.load("./asset/image/22.png").convert_alpha(),
    (400, 400)
)

punch_2 = pygame.transform.smoothscale(
    pygame.image.load("./asset/image/222.png").convert_alpha(),
    (400, 400)
)

# ============================================================
# PUNCH RECT
# ============================================================

punch1_rect = punch_1.get_rect(
    center=(400, 350)
)

punch2_rect = punch_2.get_rect(
    center=(800, 350)
)

# ============================================================
# PUNCH IMAGE
# ============================================================

PUN_CH=None
def draw_punch_image(
    screen,
    image,
    center,
    target_size,
    page_id,
    duration=450
):

    now = pygame.time.get_ticks()


    # ========================================================
    # Animation Storage
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
    # PUNCH ANIMATION
    # ========================================================

    if not animation["finished"]:

        if elapsed >= duration:

            animation["finished"] = True

            scale = 1.0

        else:

            progress = elapsed / duration


            # =================================================
            # Phase 1
            # کوچک → اندازه واقعی
            # =================================================

            if progress < 0.55:

                p = progress / 0.55

                # شروع خیلی کوچک
                start = 0.20

                # رسیدن به اندازه بزرگ
                end = 1.12

                # easing سریع
                p = 1 - (1 - p) ** 4

                scale = start + (
                    end - start
                ) * p


            # =================================================
            # Phase 2
            # Overshoot → اندازه واقعی
            # =================================================

            else:

                p = (progress - 0.55) / 0.45

                start = 1.12
                end = 1.0

                # easing نرم
                p = 1 - (1 - p) ** 3

                scale = start + (
                    end - start
                ) * p


    else:

        # ====================================================
        # FINAL SIZE
        # ====================================================

        scale = 1.0


    # ========================================================
    # Size
    # ========================================================

    width = int(target_size[0] * scale)
    height = int(target_size[1] * scale)


    width = max(1, width)
    height = max(1, height)


    # ========================================================
    # Scale Image
    # ========================================================

    scaled_image = pygame.transform.smoothscale(
        image,
        (width, height)
    )


    # ========================================================
    # Center
    # ========================================================

    rect = scaled_image.get_rect(
        center=center
    )


    # ========================================================
    # Draw
    # ========================================================

    screen.blit(
        scaled_image,
        rect
    )
    global punch_rect
    punch_rect = rect
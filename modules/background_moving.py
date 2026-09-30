

import pygame
import os
import random


def draw_moving_map(screen, width, height, dt):

    # -------------------------
    # Initialize position
    # -------------------------

    if not hasattr(draw_moving_map, "map_x"):
        draw_moving_map.map_x = 0


    # -------------------------
    # Load image ONLY ONCE
    # -------------------------

    if not hasattr(draw_moving_map, "map_image"):

        folder = "asset/image/background_moving"

        images = [
            file for file in os.listdir(folder)
            if file.lower().endswith(
                (".jpg", ".jpeg", ".png")
            )
        ]

        random_image = random.choice(images)

        image = pygame.image.load(
            os.path.join(folder, random_image)
        ).convert()


        # -------------------------
        # Scale ONLY ONCE
        # -------------------------

        scale_width = int(
            image.get_width()
            * height
            / image.get_height()
        )

        draw_moving_map.map_image = pygame.transform.smoothscale(
            image,
            (scale_width, height)
        )


    # -------------------------
    # Get image
    # -------------------------

    image = draw_moving_map.map_image

    scale_width = image.get_width()


    # -------------------------
    # Move
    # -------------------------

    speed = 0.5

    draw_moving_map.map_x -= speed * dt


    # -------------------------
    # Stop at end
    # -------------------------

    minimum_x = width - scale_width

    if draw_moving_map.map_x <= minimum_x:
        draw_moving_map.map_x = minimum_x


    # -------------------------
    # Visible area
    # -------------------------

    source_x = int(-draw_moving_map.map_x)

    source_rect = pygame.Rect(
        source_x,
        0,
        width,
        height
    )


    # -------------------------
    # Draw ONLY visible part
    # -------------------------

    screen.blit(
        image,
        (0, 0),
        source_rect
    )
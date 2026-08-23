import pygame


def draw_ceill_screen(
    screen,
    fonts,
    ceill_button_rects,
    current_width,
    current_height,
    level_images
):

    mouse_pos = pygame.mouse.get_pos()
    
    for key in level_images:

        level_images[key] = pygame.transform.smoothscale(
            level_images[key],
            (55,55)
    )
    ceills = [
        10,
        100,
        1000,
        10000,
        100000
    ]

    colors = [
        (0, 200, 0),       # 10
        (255, 220, 0),     # 100
        (255, 165, 0),     # 1000
        (255, 0, 0),       # 10000
        (160, 32, 240)     # 100000
    ]

    # ---------------- Title ----------------

    # title = fonts["name"].render(
    #     "Select Level",
    #     True,
    #     (255, 220, 0)
    # )

    # title_rect = title.get_rect(
    #     center=(
    #         current_width // 2,
    #         current_height // 2 - 130
    #     )
    # )

    # screen.blit(
    #     title,
    #     title_rect
    # )

    # ---------------- Buttons ----------------

    button_size = 100
    hover_size = 115
    gap = 25

    total_width = (
        len(ceills) * button_size
        + (len(ceills) - 1) * gap
    )

    start_x = (
        current_width - total_width
    ) // 2

    center_y = current_height // 2

    for i, ceill in enumerate(ceills):

        x = start_x + i * (
            button_size + gap
        )

        center = (
            x + button_size // 2,
            center_y
        )

        # محدوده اصلی برای کلیک
        normal_rect = pygame.Rect(
            0,
            0,
            button_size,
            button_size
        )

        normal_rect.center = center

        ceill_button_rects[ceill] = normal_rect

        # ---------------- Hover ----------------
        current_hover_image = None
        if normal_rect.collidepoint(mouse_pos):

            size = hover_size
            current_hover_image = level_images[ceill]
        else:

            size = button_size

        rect = pygame.Rect(
            0,
            0,
            size,
            size
        )

        rect.center = center

        # ---------------- Button ----------------

        pygame.draw.rect(
            screen,
            colors[i],
            rect,
            border_radius=15
        )
        # ---------------- Level Image ----------------

        image = level_images[ceill]


        image_rect = image.get_rect(
            center=(
                rect.centerx,
                rect.centery - 20
            )
        )


        screen.blit(
            image,
            image_rect
        )
                # ---------------- Text ----------------

        text = fonts["name"].render(
            str(ceill),
            True,
            (255, 255, 255)
        )

        text_rect = text.get_rect(
            center=rect.center
        )

        screen.blit(
            text,
            text_rect
        )
        
        
        
        
        
        
        
        
        
        
        if current_hover_image:

            image = pygame.transform.smoothscale(
                current_hover_image,
                (120,120)
            )


            image_rect = image.get_rect(
                center=(
                    current_width // 2,
                    current_height // 2 - 180
                )
            )


            screen.blit(
                image,
                image_rect
            )
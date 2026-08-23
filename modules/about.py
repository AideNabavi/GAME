import pygame


def draw_about(
    screen,
    current_width,
    current_height,
    about_image,
    font_big,
    font
):

    # =====================================
    # استروک فقط برای عنوان
    # =====================================

    def draw_title(
        text,
        font,
        position,
        text_color=(255,180,0),
        stroke_color=(0,0,0),
        stroke_size=3
    ):

        text_surface = font.render(
            text,
            True,
            text_color
        )

        stroke_surface = font.render(
            text,
            True,
            stroke_color
        )


        rect = text_surface.get_rect(
            center=position
        )


        x, y = rect.topleft


        for dx, dy in [
            (-stroke_size,0),
            (stroke_size,0),
            (0,-stroke_size),
            (0,stroke_size)
        ]:

            screen.blit(
                stroke_surface,
                (
                    x + dx,
                    y + dy
                )
            )


        screen.blit(
            text_surface,
            rect
        )


    # =====================================
    # کارت اصلی
    # =====================================

    about_rect = pygame.Rect(
        current_width // 2 - 300,
        50,
        600,
        700
    )


    # سایه

    shadow = pygame.Surface(
        (
            about_rect.width + 20,
            about_rect.height + 20
        ),
        pygame.SRCALPHA
    )


    pygame.draw.rect(
        shadow,
        (0,0,0,70),
        (
            10,
            10,
            about_rect.width,
            about_rect.height
        ),
        border_radius=35
    )


    screen.blit(
        shadow,
        (
            about_rect.x - 10,
            about_rect.y - 10
        )
    )


    # کارت زرد

    pygame.draw.rect(
        screen,
        (255,245,180),
        about_rect,
        border_radius=35
    )


    pygame.draw.rect(
        screen,
        (0,0,0),
        about_rect,
        width=3,
        border_radius=35
    )


    # =====================================
    # عکس دایره ای
    # =====================================

    image_size = 150


    image = pygame.transform.smoothscale(
        about_image,
        (
            image_size,
            image_size
        )
    )


    image_rect = image.get_rect(
        center=(
            current_width//2,
            about_rect.y + 120
        )
    )


    # قاب مشکی عکس

    pygame.draw.circle(
        screen,
        (0,0,0),
        image_rect.center,
        image_size//2 + 8
    )


    # ماسک دایره

    mask = pygame.Surface(
        (
            image_size,
            image_size
        ),
        pygame.SRCALPHA
    )


    pygame.draw.circle(
        mask,
        (255,255,255,255),
        (
            image_size//2,
            image_size//2
        ),
        image_size//2
    )


    circle_image = pygame.Surface(
        (
            image_size,
            image_size
        ),
        pygame.SRCALPHA
    )


    circle_image.blit(
        image,
        (0,0)
    )


    circle_image.blit(
        mask,
        (0,0),
        special_flags=pygame.BLEND_RGBA_MIN
    )


    screen.blit(
        circle_image,
        image_rect
    )


    # =====================================
    # عنوان با استروک
    # =====================================

    draw_title(
        "About Us",
        font_big,
        (
            current_width//2,
            about_rect.y + 240
        )
    )


    # =====================================
    # توضیحات بدون استروک
    # =====================================

    texts = [
        "Mental Math Challenge",
        "A smart game for improving",
        "your calculation skills"
    ]


    y = about_rect.y + 300


    for text in texts:


        surface = font.render(
            text,
            True,
            (70,70,70)
        )


        rect = surface.get_rect(
            center=(
                current_width//2,
                y
            )
        )


        screen.blit(
            surface,
            rect
        )


        y += 40



    # =====================================
    # کارت های اطلاعات
    # =====================================

    info_boxes = [

        pygame.Rect(
            current_width//2 - 230,
            about_rect.y + 420,
            460,
            60
        ),

        pygame.Rect(
            current_width//2 - 230,
            about_rect.y + 500,
            460,
            60
        ),

        pygame.Rect(
            current_width//2 - 230,
            about_rect.y + 580,
            460,
            60
        )

    ]


    labels = [

        "Email : example@gmail.com",

        "Version : 1.0.0",

        "Developer : Aiden"

    ]



    for rect, label in zip(
        info_boxes,
        labels
    ):


        pygame.draw.rect(
            screen,
            (255,255,255),
            rect,
            border_radius=20
        )


        pygame.draw.rect(
            screen,
            (0,0,0),
            rect,
            width=2,
            border_radius=20
        )


        # متن بدون استروک

        text_surface = font.render(
            label,
            True,
            (30,30,30)
        )


        text_rect = text_surface.get_rect(
            center=rect.center
        )


        screen.blit(
            text_surface,
            text_rect
        )
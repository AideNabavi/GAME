import pygame


typing_start_time = None


def reset_typing_timer():
    global typing_start_time
    typing_start_time = pygame.time.get_ticks()
    return typing_start_time
import pygame


def draw_typing_text(
    screen,
    text,
    font,
    color,
    center,
    char_delay=60,
    zoom_duration=250,
    stroke_width=2,
    stroke_color=(0, 0, 0)
):
    start_time = typing_start_time

    if start_time is None:
        return False
    now = pygame.time.get_ticks()

    # =====================================================
    # ساخت حروف
    # =====================================================

    char_surfaces = []

    total_width = 0

    for char in text:

        # فاصله
        if char == " ":

            surface = pygame.Surface(
                (font.get_height() // 2, font.get_height()),
                pygame.SRCALPHA
            )

        else:

            surface = font.render(
                char,
                True,
                color
            )

            # استروک مشکی نازک
            surface_with_stroke = font.render(
                char,
                True,
                color
            )

            # render با outline
            surface = font.render(
                char,
                True,
                color
            )

            # ساخت نسخه با استروک
            surface = font.render(
                char,
                True,
                color
            )

            # از font.render با stroke استفاده نمی‌کنیم
            # چون pygame.font.Font.render استروک ندارد.
            # پس با render_to_surface این کار را انجام می‌دهیم.

            rect = surface.get_rect()

            stroke_surface = pygame.Surface(
                (
                    rect.width + stroke_width * 2,
                    rect.height + stroke_width * 2
                ),
                pygame.SRCALPHA
            )

            # استروک با چند offset بسیار کوچک
            for dx in range(
                -stroke_width,
                stroke_width + 1
            ):
                for dy in range(
                    -stroke_width,
                    stroke_width + 1
                ):

                    if dx == 0 and dy == 0:
                        continue

                    stroke_part = font.render(
                        char,
                        True,
                        stroke_color
                    )

                    stroke_surface.blit(
                        stroke_part,
                        (
                            stroke_width + dx,
                            stroke_width + dy
                        )
                    )

            # متن نارنجی روی استروک
            stroke_surface.blit(
                surface,
                (
                    stroke_width,
                    stroke_width
                )
            )

            surface = stroke_surface

        char_surfaces.append(surface)

        total_width += surface.get_width()

    # =====================================================
    # شروع متن از مرکز
    # =====================================================

    start_x = (
        center[0]
        - total_width / 2
    )

    # =====================================================
    # DRAW
    # =====================================================

    current_x = start_x

    finished = True

    for i, surface in enumerate(char_surfaces):

        # -------------------------------------------------
        # زمان شروع این حرف
        # -------------------------------------------------

        char_start = (
            start_time
            + i * char_delay
        )

        elapsed = (
            now
            - char_start
        )

        # هنوز نوبت این حرف نرسیده
        if elapsed < 0:

            finished = False

            current_x += surface.get_width()

            continue

        # -------------------------------------------------
        # Progress
        # -------------------------------------------------

        progress = min(
            elapsed / zoom_duration,
            1.0
        )

        if progress < 1.0:
            finished = False

        # -------------------------------------------------
        # Ease Out
        # -------------------------------------------------

        progress = 1 - (
            1 - progress
        ) ** 3

        # -------------------------------------------------
        # ZOOM
        #
        # 0.3 → 1.0
        # -------------------------------------------------

        scale = (
            0.3
            + 0.7 * progress
        )

        width = max(
            1,
            int(
                surface.get_width()
                * scale
            )
        )

        height = max(
            1,
            int(
                surface.get_height()
                * scale
            )
        )

        scaled = pygame.transform.smoothscale(
            surface,
            (
                width,
                height
            )
        )

        # -------------------------------------------------
        # مرکز حرف
        # -------------------------------------------------

        char_center_x = (
            current_x
            + surface.get_width() / 2
        )

        char_rect = scaled.get_rect(
            center=(
                int(char_center_x),
                center[1]
            )
        )

        # -------------------------------------------------
        # DRAW
        # -------------------------------------------------

        screen.blit(
            scaled,
            char_rect
        )

        # -------------------------------------------------
        # حرکت به حرف بعدی
        # -------------------------------------------------

        current_x += surface.get_width()

    # =====================================================
    # RETURN
    # =====================================================

    return finished
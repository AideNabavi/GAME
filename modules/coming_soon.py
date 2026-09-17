import pygame


# ---------------------------------------------------------
# COMING SOON NOTIFICATION
# ---------------------------------------------------------

_coming_soon_start = 0
_coming_soon_active = False

# عکس فقط یک بار در زمان اجرای این فایل Load می‌شود
_coming_soon_image = pygame.image.load(
    "asset/image/coming_soon.png"
).convert_alpha()

# عکس Scale شده
_coming_soon_scaled = None
_coming_soon_scaled_width = 0


def coming_soon_notification(screen, trigger=False):

    global _coming_soon_start
    global _coming_soon_active
    global _coming_soon_scaled
    global _coming_soon_scaled_width

    # -----------------------------------------------------
    # شروع Notification
    # -----------------------------------------------------

    if trigger:

        _coming_soon_active = True
        _coming_soon_start = pygame.time.get_ticks()

    if not _coming_soon_active:
        return

    # -----------------------------------------------------
    # Scale فقط یک بار
    # -----------------------------------------------------

    target_width = int(screen.get_width() * 0.42)

    if (
        _coming_soon_scaled is None
        or _coming_soon_scaled_width != target_width
    ):

        ratio = (
            _coming_soon_image.get_height()
            / _coming_soon_image.get_width()
        )

        target_height = int(target_width * ratio)

        _coming_soon_scaled = pygame.transform.smoothscale(
            _coming_soon_image,
            (target_width, target_height)
        )

        _coming_soon_scaled_width = target_width

    image = _coming_soon_scaled

    target_height = image.get_height()

    # -----------------------------------------------------
    # زمان
    # -----------------------------------------------------

    now = pygame.time.get_ticks()
    elapsed = now - _coming_soon_start

    ENTER_TIME = 500
    HOLD_TIME = 3000
    EXIT_TIME = 250

    TOTAL_TIME = (
        ENTER_TIME
        + HOLD_TIME
        + EXIT_TIME
    )

    # -----------------------------------------------------
    # پایان Notification
    # -----------------------------------------------------

    if elapsed >= TOTAL_TIME:

        _coming_soon_active = False
        return

    # -----------------------------------------------------
    # Position
    # -----------------------------------------------------

    screen_width = screen.get_width()
    screen_height = screen.get_height()

    x = (
        screen_width
        - target_width
    ) // 2

    # 200 پیکسل بالاتر از مرکز
    target_y = (
        screen_height
        - target_height
    ) // 2 - 400

    # خارج از بالای صفحه
    start_y = -target_height - 30

    # -----------------------------------------------------
    # ورود
    # -----------------------------------------------------

    if elapsed < ENTER_TIME:

        progress = elapsed / ENTER_TIME

        # Ease Out
        progress = 1 - (1 - progress) ** 3

        y = (
            start_y
            + (target_y - start_y)
            * progress
        )

    # -----------------------------------------------------
    # ماندن
    # -----------------------------------------------------

    elif elapsed < ENTER_TIME + HOLD_TIME:

        y = target_y

    # -----------------------------------------------------
    # خروج سریع
    # -----------------------------------------------------

    else:

        exit_elapsed = (
            elapsed
            - ENTER_TIME
            - HOLD_TIME
        )

        progress = exit_elapsed / EXIT_TIME

        # خروج سریع‌تر
        progress = progress ** 2

        y = (
            target_y
            + (start_y - target_y)
            * progress
        )

    # -----------------------------------------------------
    # Draw
    # -----------------------------------------------------

    screen.blit(
        image,
        (x, int(y))
    )
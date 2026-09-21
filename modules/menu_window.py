import pygame
from modules.font import *

xp_window_start = None
button_rects = None

def draw_dark_overlay(screen):
    overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))
    screen.blit(overlay, (0, 0))


image_____ = pygame.transform.smoothscale(
    pygame.image.load("./asset/image/window11.png").convert_alpha(),
    (1200, 1200)
)

button_images = [
    pygame.transform.smoothscale(
        pygame.image.load("./asset/image/menu_window/home.png").convert_alpha(),
        (150, 150)
    ),
    pygame.transform.smoothscale(
        pygame.image.load("./asset/image/menu_window/back.png").convert_alpha(),
        (150, 150)
    ),
    pygame.transform.smoothscale(
        pygame.image.load("./asset/image/menu_window/next.png").convert_alpha(),
        (150, 150)
    )
]


def SHOW_XP(screen,xp_, WIDTH, HEIGHT):

    global xp_window_start
    global button_rects
    

    # شروع انیمیشن
    if xp_window_start is None:
        xp_window_start = pygame.time.get_ticks()

    elapsed = pygame.time.get_ticks() - xp_window_start

    progress = min(elapsed / 400, 1.0)

    # Ease Out
    progress = 1 - (1 - progress) ** 3

    # =====================================================
    # DARK OVERLAY
    # =====================================================

    draw_dark_overlay(screen)

    # =====================================================
    # MAIN IMAGE ZOOM
    # =====================================================

    base_size = 200

    scale = 0.5 + (0.5 * progress)

    size = int(base_size * scale)

    image = pygame.transform.smoothscale(
        image_____,
        (size, size)
    )

    image_rect = image.get_rect(
        center=(WIDTH // 2, HEIGHT // 2)
    )

    screen.blit(image, image_rect)

    # =====================================================
    # XP TEXT
    # =====================================================

    T = fonts["date"].render(
        f"{xp_} XP",
        True,
        (255, 255, 255)
    )

    screen.blit(
        T,
        T.get_rect(center=image_rect.center)
    )

    # =====================================================
    # THREE BUTTONS
    # =====================================================

    button_rects = []

    button_size = 110
    gap = 40

    total_width = button_size * 3 + gap * 2

    start_x = WIDTH // 2 - total_width // 2

    y = HEIGHT // 2 + 170

    for i, button_image in enumerate(button_images):

        button_scale = 0.5 + (0.5 * progress)

        current_size = int(
            button_size * button_scale
        )

        button = pygame.transform.smoothscale(
            button_image,
            (current_size, current_size)
        )

        center_x = (
            start_x
            + i * (button_size + gap)
            + button_size // 2
        )

        rect = button.get_rect(
            center=(center_x, y)
        )

        screen.blit(button, rect)

        button_rects.append(rect)

    return button_rects




def RESET_MENU_WINDOW_EFFECT():
    global xp_window_start
    xp_window_start = None
    
    
    
    
    



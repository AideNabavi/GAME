import pygame
screen = pygame.display.set_mode((900, 700))

# پنجره اصلی
window_rect = pygame.Rect(150, 100, 600, 500)

# محتوای بزرگ‌تر از پنجره
content_height = 1200
content = pygame.Surface((window_rect.width, content_height), pygame.SRCALPHA)

scroll_y = 0
scroll_speed = 30


def draw_scroll_window(screen):
    global scroll_y


    font = pygame.font.Font(None, 40)

    texts = [
        "FAST MATHTER",
        "About The Game",
        "Features",
        "Multiple Modes",
        "Profiles",
        "Leaderboard",
        "Support",
        "Contact Us",
        "Version 1.0.0",
        "Created with Pygame"
    ]

    y = 40

    for text in texts:
        img = font.render(text, True, (255,255,255))
        content.blit(img, (50, y))
        y += 100


    # فقط قسمت پنجره را نمایش بده
    screen.blit(
        content,
        window_rect.topleft,
        pygame.Rect(
            0,
            scroll_y,
            window_rect.width,
            window_rect.height
        )
    )

    # کادر دور پنجره
    pygame.draw.rect(
        screen,
        (255,255,255),
        window_rect,
        3
    )
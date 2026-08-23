import pygame
from modules.font import *

def loading_screen1(screen, fonts):

    screen.fill((255,0,0))

    pygame.display.update()

    pygame.time.delay(2000)
    
def loading_screen(screen, fonts):

    clock = pygame.time.Clock()


    # Load image

    logo = pygame.image.load(
        "./asset/image/loading/logo.png"
    ).convert_alpha()


    # تغییر اندازه لوگو

    logo = pygame.transform.smoothscale(
        logo,
        (300,300)
    )


    progress = 0


    running = True

    while running:

        screen.fill(
            (15,15,25)
        )


        # قرار دادن عکس وسط

        logo_rect = logo.get_rect(
            center=(
                screen.get_width() // 2,
                250
            )
        )


        screen.blit(
            logo,
            logo_rect
        )


        # اسم بازی

        title = fonts["title"].render(
            "MENTAL MATH CHALLENGE",
            True,
            (255,255,255)
        )


        title_rect = title.get_rect(
            center=(
                screen.get_width() // 2,
                430
            )
        )


        screen.blit(
            title,
            title_rect
        )


        # نوار لود

        bar_width = 600
        bar_height = 35

        x = (screen.get_width()-bar_width)//2
        y = 520


        pygame.draw.rect(
            screen,
            (60,60,60),
            (x,y,bar_width,bar_height),
            border_radius=20
        )


        pygame.draw.rect(
            screen,
            (0,220,120),
            (
                x,
                y,
                bar_width * progress // 100,
                bar_height
            ),
            border_radius=20
        )


        pygame.display.update()


        if progress < 100:
            progress += 1
        else:
            running = False


        clock.tick(60)
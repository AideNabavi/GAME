import pygame


FONT_PATH4 = "./asset/font/title.ttf"
FONT_PATH = "./asset/font/math.ttf"
FONT_PATH0 = "./asset/font/about.ttf"
FONT_PATH1 = "./asset/font/name.ttf"
FONT_GAME = "./asset/font/game.ttf"
FONT_PATH3 = "./asset/font/Goof.otf"


# ============================================================
# FONT SIZES
# ============================================================

FONT_SIZES = {
    "main": 250,
    "quastion": 200,
    "answer": 100,
    "heart": 150,
    "date": 50,
    "profile_": 30,
    "TITLE_NEW": 70,
    "DAY": 100,
    "weekdays": 90,
    "month": 70,
    "month_real": 40,
    "icon2": 70,
    "more and support": 35,
    "support": 40,
    "name": 40,
    "about": 20,
    "time_screen": 40,
    "time_screen1": 50,
    "title": 50,
}


def load_fonts():

    fonts = {

        "main": pygame.font.Font(
            FONT_PATH,
            250
        ),

        "quastion": pygame.font.Font(
            FONT_PATH1,
            200
        ),

        "answer": pygame.font.Font(
            FONT_PATH1,
            100
        ),

        "heart": pygame.font.Font(
            FONT_PATH1,
            100
        ),

        "date": pygame.font.Font(
            FONT_PATH1,
            50
        ),

        "profile_": pygame.font.Font(
            FONT_PATH1,
            30
        ),

        "TITLE_NEW": pygame.font.Font(
            FONT_PATH1,
            70
        ),

        "DAY": pygame.font.Font(
            FONT_PATH1,
            100
        ),

        "weekdays": pygame.font.Font(
            FONT_PATH1,
            90
        ),

        "month": pygame.font.Font(
            FONT_PATH1,
            70
        ),

        "month_real": pygame.font.Font(
            FONT_PATH1,
            40
        ),

        "icon2": pygame.font.Font(
            FONT_PATH1,
            70
        ),

        "more and support": pygame.font.Font(
            FONT_PATH3,
            35
        ),

        "support": pygame.font.Font(
            FONT_PATH1,
            40
        ),

        "name": pygame.font.Font(
            FONT_PATH1,
            40
        ),

        "answer_math": pygame.font.Font(
            FONT_PATH,
            60
        ),

        "about": pygame.font.Font(
            FONT_PATH0,
            20
        ),

        "time_screen": pygame.font.Font(
            FONT_PATH0,
            40
        ),

        "time_screen1": pygame.font.Font(
            FONT_PATH0,
            50
        ),

        "title": pygame.font.Font(
            FONT_PATH4,
            50
        )
    }

    return fonts


fonts = load_fonts()
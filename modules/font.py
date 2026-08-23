import pygame


FONT_PATH4 = "./asset/font/title.ttf"
FONT_PATH = "./asset/font/math.ttf"
FONT_PATH0 = "./asset/font/about.ttf"
FONT_PATH1 = "./asset/font/name.ttf"
FONT_GAME = "./asset/font/game.ttf"


def load_fonts():

    fonts = {

        "main": pygame.font.Font(
            FONT_PATH,
            250
        ),
        "quastion": pygame.font.Font(
            FONT_GAME,
            200
        ),
        
        
        "answer": pygame.font.Font(
            FONT_GAME,
            100
        ),
        
        "heart": pygame.font.Font(
            FONT_PATH1,
            100
        ),


        "name": pygame.font.Font(
            FONT_PATH1,
            40
        ),

        "answer": pygame.font.Font(
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


fonts=load_fonts()

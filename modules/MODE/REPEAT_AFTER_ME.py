import pygame
import random
import time
from modules.font import fonts

# pygame.init()


# WIDTH = 600
# HEIGHT = 700

# screen = pygame.display.set_mode(
#     (WIDTH, HEIGHT)
# )

# pygame.display.set_caption(
#     "Pattern Memory"
# )


# clock = pygame.time.Clock()


# font = pygame.font.Font(None, 45)


# -----------------------
# Colors
# -----------------------

# BG = (25,25,30)

WHITE = (255,255,255)

NORMAL = (60,60,70)

SHOW_COLOR = (50,180,255)

CLICK_COLOR = (255,170,50)

RED = (255,50,50)



# -----------------------
# Grid
# -----------------------

ROWS = 4
COLS = 4


CELL = 100
GAP = 10



# -----------------------
# Game
# -----------------------

level = 1

score = 0


pattern = []

selected = []


state = "show"


timer = 0


SHOW_TIME = 2

ANSWER_TIME = 10


game_over = False




# -----------------------
# Create pattern
# -----------------------

def create_pattern():

    global pattern


    count = level + 1


    count = min(
        count,
        ROWS * COLS
    )


    cells = list(
        range(ROWS*COLS)
    )


    random.shuffle(cells)


    pattern = cells[:count]






# -----------------------
# New round
# -----------------------

def new_round():

    global state
    global timer
    global selected


    create_pattern()


    selected = []


    state = "show"


    timer = time.time()






# -----------------------
# Cell position
# -----------------------

def get_rect(index):


    row = index // COLS

    col = index % COLS


    return pygame.Rect(

        50 + col*(CELL+GAP),

        100 + row*(CELL+GAP),

        CELL,

        CELL

    )







def REPEAT_AFTER_ME_(screen):
    global state
    global game_over
    global timer
    global selected
    global ANSWER_TIME
    global SHOW_TIME
 

 
    # -----------------------
    # Timer
    # -----------------------

    if not game_over:


        elapsed = time.time()-timer



        if state == "show":


            if elapsed >= SHOW_TIME:


                state="answer"

                timer=time.time()




        elif state == "answer":


            if elapsed >= ANSWER_TIME:


                game_over=True

                state="end"






    # -----------------------
    # Draw grid
    # -----------------------

    for i in range(
        ROWS*COLS
    ):


        rect = get_rect(i)


        color = NORMAL



        if state == "show" and i in pattern:


            color = SHOW_COLOR



        if i in selected:


            color = CLICK_COLOR




        pygame.draw.rect(

            screen,

            color,

            rect,

            border_radius=15

        )






    # -----------------------
    # Text
    # -----------------------

    info = fonts["heart"].render(

        f"Level: {level}  Score: {score}",

        True,

        WHITE

    )


    screen.blit(

        info,

        (100,30)

    )





    if state == "show":


        text = fonts["heart"].render(

            "MEMORIZE",

            True,

            SHOW_COLOR

        )


        screen.blit(

            text,

            (190,560)

        )



    elif state == "answer":


        remain = int(

            ANSWER_TIME -

            (time.time()-timer)

        )


        text = fonts["heart"].render(

            f"TIME: {remain}",

            True,

            WHITE

        )


        screen.blit(

            text,

            (220,560)

        )





    if state == "end":


        text = fonts["heart"].render(

            "GAME OVER",

            True,

            RED

        )


        screen.blit(

            text,

            (170,560)

        )


        text2 = fonts["heart"].render(

            "Press R",

            True,

            WHITE

        )


        screen.blit(

            text2,

            (220,620)

        )




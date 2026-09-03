import pygame
import random
import time
from modules.font import fonts

# pygame.init()


# WIDTH = 900
# HEIGHT = 500

# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Focus Direction Test")


# clock = pygame.time.Clock()


# font = pygame.font.Font(None, 70)
# small_font = pygame.font.Font(None, 40)

buttons = {}

QUESTION_Y = 130
BUTTON_SIZE = 100
BUTTON_GAP = 20


WHITE = (255,255,255)
BG = (30,30,30)


# به جای این عکس بیاد چهار تا سمت رو نشون بده 
directions = [
    "LEFT",
    "RIGHT",
    "UP",
    "DOWN"
]


keys = {

    pygame.K_LEFT: "LEFT",
    pygame.K_RIGHT: "RIGHT",
    pygame.K_UP: "UP",
    pygame.K_DOWN: "DOWN"

}

def create_direction_buttons(WIDTH, HEIGHT):

    global buttons

    total_width = (
        BUTTON_SIZE * 4
        + BUTTON_GAP * 3
    )

    start_x = (
        WIDTH - total_width
    ) // 2

    y = HEIGHT - 150

    buttons = {

        "LEFT": pygame.Rect(
            start_x,
            y,
            BUTTON_SIZE,
            BUTTON_SIZE
        ),

        "RIGHT": pygame.Rect(
            start_x + (BUTTON_SIZE + BUTTON_GAP),
            y,
            BUTTON_SIZE,
            BUTTON_SIZE
        ),

        "UP": pygame.Rect(
            start_x + 2 * (BUTTON_SIZE + BUTTON_GAP),
            y,
            BUTTON_SIZE,
            BUTTON_SIZE
        ),

        "DOWN": pygame.Rect(
            start_x + 3 * (BUTTON_SIZE + BUTTON_GAP),
            y,
            BUTTON_SIZE,
            BUTTON_SIZE
        )
    }


score = 0
correct = 0
wrong = 0



game_time = 60

start_time = time.time()


items = []

answer = None



def new_round_DIRECTION():

    global items
    global answer


    items = []


    same = random.choice(
        [True, False]
    )


    main = random.choice(
        directions
    )


    if same:


        for i in range(5):

            items.append(main)


        answer = main



    else:


        different = random.choice(
            [
                x for x in directions
                if x != main
            ]
        )


        position = random.randint(
            0,4
        )


        for i in range(5):

            if i == position:

                items.append(
                    different
                )

            else:

                items.append(
                    main
                )


        answer = different




def reset_game_DIRECTION(WIDTH, HEIGHT):

    global score
    global correct
    global wrong
    global game_time
    global start_time
    global finished

    score = 0
    correct = 0
    wrong = 0

    game_time = 60

    start_time = time.time()

    finished = False

    create_direction_buttons(
        WIDTH,
        HEIGHT
    )

    new_round_DIRECTION()



finished = False

def DIRECTION_(screen):

    global finished
    global items
    global game_time
    global score
    global wrong
    global correct

    WIDTH, HEIGHT = screen.get_size()

    # =========================
    # TIMER
    # =========================

    elapsed = time.time() - start_time

    remaining = int(
        game_time - elapsed
    )

    if remaining <= 0:

        remaining = 0
        finished = True

    # =========================
    # BACKGROUND
    # =========================

    screen.fill(BG)

    # =========================
    # HUD
    # =========================

    info = fonts["heart"].render(
        f"Time: {remaining}    Score: {score}",
        True,
        WHITE
    )

    screen.blit(
        info,
        (20, 20)
    )

    # =========================
    # GAME
    # =========================

    if not finished:

        # =========================
        # QUESTION
        # =========================

        question_text = fonts["heart"].render(
            "WHICH DIRECTION IS DIFFERENT?",
            True,
            WHITE
        )

        screen.blit(
            question_text,
            question_text.get_rect(
                center=(
                    WIDTH // 2,
                    120
                )
            )
        )

        # =========================
        # FIVE ITEMS
        # =========================

        total_width = 5 * 120

        start_x = (
            WIDTH - total_width
        ) // 2

        for i, item in enumerate(items):

            text = fonts["heart"].render(
                item,
                True,
                WHITE
            )

            rect = text.get_rect(
                center=(
                    start_x + i * 120 + 60,
                    260
                )
            )

            screen.blit(
                text,
                rect
            )

        # =========================
        # BUTTONS
        # =========================

        mouse_pos = pygame.mouse.get_pos()

        if not buttons:

            create_direction_buttons(
                WIDTH,
                HEIGHT
            )

        for direction, rect in buttons.items():

            # ---------------------
            # HOVER
            # ---------------------

            if rect.collidepoint(mouse_pos):

                button_color = (
                    80,
                    150,
                    230
                )

            else:

                button_color = (
                    50,
                    80,
                    120
                )

            # ---------------------
            # BUTTON
            # ---------------------

            pygame.draw.rect(
                screen,
                button_color,
                rect,
                border_radius=15
            )

            pygame.draw.rect(
                screen,
                (120, 120, 140),
                rect,
                2,
                border_radius=15
            )

            # ---------------------
            # BUTTON TEXT
            # ---------------------

            text = fonts["heart"].render(
                direction,
                True,
                WHITE
            )

            screen.blit(
                text,
                text.get_rect(
                    center=rect.center
                )
            )

    # =========================
    # FINISHED
    # =========================

    else:

        title = fonts["heart"].render(
            "FINISHED",
            True,
            WHITE
        )

        screen.blit(
            title,
            title.get_rect(
                center=(
                    WIDTH // 2,
                    180
                )
            )
        )

        result = fonts["heart"].render(
            f"Score: {score}    Correct: {correct}    Wrong: {wrong}",
            True,
            WHITE
        )

        screen.blit(
            result,
            result.get_rect(
                center=(
                    WIDTH // 2,
                    280
                )
            )
        )
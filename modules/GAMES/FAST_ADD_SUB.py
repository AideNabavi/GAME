import pygame
import random

from modules.font import *


# =========================================================
# SETTINGS
# =========================================================

SHOW_TIME = 0.7

ANSWER_TIME = 5.0

ITEM_COUNT = 5

OPTION_COUNT = 4

MAX_LIVES = 3


# =========================================================
# COLORS
# =========================================================

WHITE = (255, 255, 255)

BLACK = (20, 20, 20)

GREEN = (60, 220, 100)

RED = (230, 60, 60)

BLUE = (70, 130, 255)

YELLOW = (245, 190, 70)

GRAY = (100, 100, 100)

DARK_GRAY = (40, 40, 40)

HOVER_GRAY = (60, 65, 75)


# =========================================================
# GAME STATES
# =========================================================

SHOWING = "SHOWING"

ANSWERING = "ANSWERING"

GAME_OVER = "GAME_OVER"


# =========================================================
# GAME VARIABLES
# =========================================================

game_state = SHOWING


score = 0

lives = MAX_LIVES


items = []

current_item = 0


# زمان شروع نمایش آیتم
show_timer = 0


# جواب صحیح
answer = 0


# گزینه‌ها
options = []


# زمان شروع انتخاب جواب
answer_timer = 0


# =========================================================
# CREATE QUESTION
# =========================================================

def create_question():

    global items
    global answer

    while True:

        # -------------------------------------------------
        # Numbers
        # -------------------------------------------------

        numbers = [

            random.randint(
                0,
                100
            ),

            random.randint(
                0,
                100
            ),

            random.randint(
                0,
                100
            )

        ]

        # -------------------------------------------------
        # Operators
        # -------------------------------------------------

        operators = [

            random.choice(
                [
                    "+",
                    "-"
                ]
            ),

            random.choice(
                [
                    "+",
                    "-"
                ]
            )

        ]

        # -------------------------------------------------
        # Calculate
        # -------------------------------------------------

        result = numbers[0]


        if operators[0] == "+":

            result += numbers[1]

        else:

            result -= numbers[1]


        if operators[1] == "+":

            result += numbers[2]

        else:

            result -= numbers[2]


        # -------------------------------------------------
        # Valid answer
        # -------------------------------------------------

        if 0 <= result <= 100:

            answer = result

            items = [

                str(numbers[0]),

                operators[0],

                str(numbers[1]),

                operators[1],

                str(numbers[2])

            ]

            return


# =========================================================
# CREATE OPTIONS
# =========================================================

def create_options():

    global options

    options = [

        answer

    ]


    while len(options) < OPTION_COUNT:

        fake = (
            answer
            + random.randint(
                -20,
                20
            )
        )


        if (

            0 <= fake <= 100

            and fake not in options

        ):

            options.append(
                fake
            )


    random.shuffle(
        options
    )


# =========================================================
# START ROUND
# =========================================================

def start_round():

    global game_state

    global current_item

    global show_timer

    global answer_timer


    # -------------------------------------------------
    # New question
    # -------------------------------------------------

    create_question()


    # -------------------------------------------------
    # Reset showing
    # -------------------------------------------------

    current_item = 0


    # زمان شروع نمایش
    show_timer = pygame.time.get_ticks()


    # تایمر جواب فعلاً شروع نشده
    answer_timer = 0


    game_state = SHOWING


# =========================================================
# RESET GAME
# =========================================================

def reset_game():

    global score

    global lives

    global game_state


    score = 0

    lives = MAX_LIVES


    game_state = SHOWING


    start_round()


# =========================================================
# DRAW CENTER TEXT
# =========================================================

def draw_center_text(
    screen,
    WIDTH,
    HEIGHT,
    text,
    font,
    color=WHITE,
    center_y=None
):

    surface = font.render(
        str(text),
        True,
        color
    )


    if center_y is None:

        center_y = HEIGHT // 2


    rect = surface.get_rect(

        center=(

            WIDTH // 2,

            center_y

        )

    )


    screen.blit(
        surface,
        rect
    )


# =========================================================
# DRAW HEADER
# =========================================================

def draw_header(
    screen,
    WIDTH
):

    # -----------------------------------------------------
    # Score
    # -----------------------------------------------------

    score_text = fonts["heart"].render(

        f"Score: {score}",

        True,

        WHITE

    )


    screen.blit(

        score_text,

        (
            30,
            25
        )

    )


    # -----------------------------------------------------
    # Lives
    # -----------------------------------------------------

    lives_text = fonts["heart"].render(

        f"Lives: {lives}",

        True,

        WHITE

    )


    screen.blit(

        lives_text,

        (
            WIDTH
            - lives_text.get_width()
            - 30,

            25
        )

    )


# =========================================================
# DRAW SHOWING
# =========================================================

def draw_showing(
    screen,
    WIDTH,
    HEIGHT
):

    if current_item < len(items):

        draw_center_text(

            screen,

            WIDTH,

            HEIGHT,

            items[current_item],

            fonts["heart"],

            WHITE,

            HEIGHT // 2

        )


    # -----------------------------------------------------
    # Progress
    # -----------------------------------------------------

    progress = fonts["heart"].render(

        f"{current_item + 1} / {ITEM_COUNT}",

        True,

        GRAY

    )


    progress_rect = progress.get_rect(

        center=(

            WIDTH // 2,

            HEIGHT - 70

        )

    )


    screen.blit(

        progress,

        progress_rect

    )


# =========================================================
# BUILD EXPRESSION
# =========================================================

def get_expression():

    expression = " ".join(
        items
    )


    expression = (

        expression

        .replace(
            "*",
            "×"
        )

        .replace(
            "/",
            "÷"
        )

    )


    return expression


# =========================================================
# DRAW QUESTION
# =========================================================

def draw_question(
    screen,
    WIDTH,
    HEIGHT
):

    expression = get_expression()


    draw_center_text(

        screen,

        WIDTH,

        HEIGHT,

        expression + " = ?",

        fonts["heart"],

        WHITE,

        145

    )


# =========================================================
# DRAW TIMER
# =========================================================

def draw_timer(
    screen,
    WIDTH,
    HEIGHT,
    remaining
):

    # -----------------------------------------------------
    # Color
    # -----------------------------------------------------

    if remaining <= 1:

        color = RED

    elif remaining <= 2:

        color = YELLOW

    else:

        color = BLUE


    # -----------------------------------------------------
    # Circle
    # -----------------------------------------------------

    center = (

        WIDTH // 2,

        220

    )


    radius = 35


    pygame.draw.circle(

        screen,

        DARK_GRAY,

        center,

        radius

    )


    pygame.draw.circle(

        screen,

        color,

        center,

        radius,

        4

    )


    # -----------------------------------------------------
    # Number
    # -----------------------------------------------------

    timer_text = fonts["heart"].render(

        f"{remaining:.1f}",

        True,

        WHITE

    )


    timer_rect = timer_text.get_rect(

        center=center

    )


    screen.blit(

        timer_text,

        timer_rect

    )


# =========================================================
# GET OPTION RECTS
# =========================================================

def get_option_rects(
    WIDTH,
    HEIGHT
):

    button_width = 280

    button_height = 100


    horizontal_gap = 30

    vertical_gap = 25


    # -----------------------------------------------------
    # Total width of two buttons
    # -----------------------------------------------------

    total_width = (

        button_width * 2

        + horizontal_gap

    )


    start_x = (

        WIDTH
        - total_width

    ) // 2


    # پایین صفحه
    start_y = HEIGHT - 310


    positions = [

        (

            start_x,

            start_y

        ),

        (

            start_x
            + button_width
            + horizontal_gap,

            start_y

        ),

        (

            start_x,

            start_y
            + button_height
            + vertical_gap

        ),

        (

            start_x
            + button_width
            + horizontal_gap,

            start_y
            + button_height
            + vertical_gap

        )

    ]


    rects = []


    for x, y in positions:

        rects.append(

            pygame.Rect(

                x,

                y,

                button_width,

                button_height

            )

        )


    return rects


# =========================================================
# DRAW ANSWERS
# =========================================================

def draw_answering(
    screen,
    WIDTH,
    HEIGHT,
    remaining
):

    # -----------------------------------------------------
    # Question
    # -----------------------------------------------------

    draw_question(

        screen,

        WIDTH,

        HEIGHT

    )


    # -----------------------------------------------------
    # Timer
    # -----------------------------------------------------

    draw_timer(

        screen,

        WIDTH,

        HEIGHT,

        remaining

    )


    # -----------------------------------------------------
    # Buttons
    # -----------------------------------------------------

    rects = get_option_rects(

        WIDTH,

        HEIGHT

    )


    mouse = pygame.mouse.get_pos()


    for i, rect in enumerate(rects):

        # -------------------------------------------------
        # Hover
        # -------------------------------------------------

        if rect.collidepoint(mouse):

            color = HOVER_GRAY

        else:

            color = DARK_GRAY


        # -------------------------------------------------
        # Background
        # -------------------------------------------------

        pygame.draw.rect(

            screen,

            color,

            rect,

            border_radius=18

        )


        # -------------------------------------------------
        # Border
        # -------------------------------------------------

        pygame.draw.rect(

            screen,

            BLUE,

            rect,

            width=3,

            border_radius=18

        )


        # -------------------------------------------------
        # Answer
        # -------------------------------------------------

        text = fonts["heart"].render(

            str(options[i]),

            True,

            WHITE

        )


        text_rect = text.get_rect(

            center=rect.center

        )


        screen.blit(

            text,

            text_rect

        )


        # -------------------------------------------------
        # Option number
        # -------------------------------------------------

        index_text = fonts["heart"].render(

            str(i + 1),

            True,

            GRAY

        )


        index_rect = index_text.get_rect(

            center=(

                rect.x + 25,

                rect.y + 25

            )

        )


        screen.blit(

            index_text,

            index_rect

        )


# =========================================================
# SELECT ANSWER
# =========================================================

def select_answer(
    selected
):

    global score

    global lives

    global game_state


    # -----------------------------------------------------
    # Correct
    # -----------------------------------------------------

    if selected == answer:

        score += 100

        start_round()


    # -----------------------------------------------------
    # Wrong
    # -----------------------------------------------------

    else:

        lives -= 1


        if lives <= 0:

            game_state = GAME_OVER

        else:

            start_round()


# =========================================================
# CLICK OPTION
# =========================================================

def click_option(
    position,
    WIDTH,
    HEIGHT
):

    if game_state != ANSWERING:

        return


    rects = get_option_rects(

        WIDTH,

        HEIGHT

    )


    for i, rect in enumerate(rects):

        if rect.collidepoint(position):

            select_answer(

                options[i]

            )

            return


# =========================================================
# DRAW GAME OVER
# =========================================================

def draw_game_over(
    screen,
    WIDTH,
    HEIGHT
):

    draw_center_text(

        screen,

        WIDTH,

        HEIGHT,

        "GAME OVER",

        fonts["heart"],

        RED,

        HEIGHT // 2 - 80

    )


    draw_center_text(

        screen,

        WIDTH,

        HEIGHT,

        f"Final Score: {score}",

        fonts["heart"],

        WHITE,

        HEIGHT // 2 + 20

    )


    draw_center_text(

        screen,

        WIDTH,

        HEIGHT,

        "Press R to Restart",

        fonts["heart"],

        GRAY,

        HEIGHT // 2 + 100

    )

def restart_game():

    global score
    global lives
    global game_state

    score = 0
    lives = MAX_LIVES

    game_state = SHOWING

    start_round()

# =========================================================
# MAIN GAME
# =========================================================

def QUICK_MATH(screen):

    global game_state

    global current_item

    global show_timer

    global answer_timer


    WIDTH, HEIGHT = screen.get_size()


    # =====================================================
    # CURRENT TIME
    # =====================================================

    now = pygame.time.get_ticks()


    # =====================================================
    # SHOWING
    # =====================================================

    if game_state == SHOWING:

        # -----------------------------------------------
        # How long current item has been visible
        # -----------------------------------------------

        elapsed = (

            now
            - show_timer

        )


        if elapsed >= SHOW_TIME * 1000:

            show_timer = now

            current_item += 1


            # -------------------------------------------
            # All items finished
            # -------------------------------------------

            if current_item >= ITEM_COUNT:

                create_options()


                # زمان شروع انتخاب جواب
                answer_timer = now


                game_state = ANSWERING


    # =====================================================
    # ANSWERING
    # =====================================================

    elif game_state == ANSWERING:

        elapsed = (

            now
            - answer_timer

        )


        remaining = (

            ANSWER_TIME
            - elapsed / 1000

        )


        # -----------------------------------------------
        # Time Up
        # -----------------------------------------------

        if remaining <= 0:

            lives -= 1


            if lives <= 0:

                game_state = GAME_OVER

            else:

                start_round()


    # =====================================================
    # DRAW
    # =====================================================

    screen.fill(
        BLACK
    )


    draw_header(

        screen,

        WIDTH

    )


    # =====================================================
    # SHOWING
    # =====================================================

    if game_state == SHOWING:

        draw_showing(

            screen,

            WIDTH,

            HEIGHT

        )


    # =====================================================
    # ANSWERING
    # =====================================================

    elif game_state == ANSWERING:

        elapsed = (

            now
            - answer_timer

        )


        remaining = max(

            0,

            ANSWER_TIME
            - elapsed / 1000

        )


        draw_answering(

            screen,

            WIDTH,

            HEIGHT,

            remaining

        )


    # =====================================================
    # GAME OVER
    # =====================================================

    elif game_state == GAME_OVER:

        draw_game_over(

            screen,

            WIDTH,

            HEIGHT

        )


# =========================================================
# INITIAL START
# =========================================================


import pygame
import random
import time
from modules.font import fonts


# =========================================================
# COLORS
# =========================================================

WHITE = (255, 255, 255)

NORMAL = (60, 60, 70)

SHOW_COLOR = (50, 180, 255)

CLICK_COLOR = (255, 170, 50)

RED = (255, 50, 50)


# =========================================================
# GRID
# =========================================================

ROWS = 4
COLS = 4

CELL = 100
GAP = 10


# =========================================================
# GAME
# =========================================================

level = 1

score = 0

lives = 3

pattern = []

selected = []

state = "show"

timer = 0

SHOW_TIME = 2

ANSWER_TIME = 10

game_over = False


# =========================================================
# CREATE PATTERN
# =========================================================

def create_pattern():

    global pattern

    count = level + 1

    count = min(
        count,
        ROWS * COLS
    )

    cells = list(
        range(ROWS * COLS)
    )

    random.shuffle(cells)

    pattern = cells[:count]


# =========================================================
# NEW ROUND
# =========================================================

def new_round():

    global state
    global timer
    global selected

    create_pattern()

    selected = []

    state = "show"

    timer = time.time()


# =========================================================
# CELL POSITION
# =========================================================

def get_rect(index):

    row = index // COLS
    col = index % COLS

    return pygame.Rect(

        50 + col * (CELL + GAP),

        100 + row * (CELL + GAP),

        CELL,

        CELL
    )


# =========================================================
# CLICK
# =========================================================

def click_REPEAT_AFTER_ME(pos):

    global lives
    global score
    global level
    global state
    global game_over
    global selected

    # فقط در حالت جواب دادن اجازه کلیک داریم
    if state != "answer":
        return

    # پیدا کردن خانه‌ای که کلیک شده
    for i in range(ROWS * COLS):

        rect = get_rect(i)

        if rect.collidepoint(pos):

            # -----------------------------------------
            # اگر قبلاً انتخاب شده
            # -----------------------------------------

            if i in selected:
                return

            # -----------------------------------------
            # جواب درست
            # -----------------------------------------

            if i in pattern:

                selected.append(i)

                score += 10

                # آیا کل Pattern پیدا شده؟
                if len(selected) == len(pattern):

                    level += 1

                    score += 50

                    new_round()

                return

            # -----------------------------------------
            # جواب اشتباه
            # -----------------------------------------

            else:

                lives -= 1

                # اگر جان تمام شد
                if lives <= 0:

                    lives = 0

                    game_over = True

                    state = "end"

                return


# =========================================================
# GAME
# =========================================================

def REPEAT_AFTER_ME_(screen):

    global state
    global game_over
    global timer

    # =====================================================
    # TIMER
    # =====================================================

    if not game_over:

        elapsed = time.time() - timer

        # ---------------------------------------------
        # SHOW PATTERN
        # ---------------------------------------------

        if state == "show":

            if elapsed >= SHOW_TIME:

                state = "answer"

                timer = time.time()

        # ---------------------------------------------
        # ANSWER
        # ---------------------------------------------

        elif state == "answer":

            if elapsed >= ANSWER_TIME:

                game_over = True

                state = "end"

    # =====================================================
    # DRAW GRID
    # =====================================================

    for i in range(ROWS * COLS):

        rect = get_rect(i)

        color = NORMAL

        # Pattern فقط در زمان نمایش
        if state == "show" and i in pattern:

            color = SHOW_COLOR

        # انتخاب‌های درست
        if i in selected:

            color = CLICK_COLOR

        pygame.draw.rect(

            screen,

            color,

            rect,

            border_radius=15
        )

    # =====================================================
    # INFO
    # =====================================================

    info = fonts["heart"].render(

        f"Level: {level}   Score: {score}   Lives: {lives}",

        True,

        WHITE
    )

    screen.blit(

        info,

        (100, 30)
    )

    # =====================================================
    # SHOW
    # =====================================================

    if state == "show":

        text = fonts["heart"].render(

            "MEMORIZE",

            True,

            SHOW_COLOR
        )

        screen.blit(

            text,

            (190, 560)
        )

    # =====================================================
    # ANSWER
    # =====================================================

    elif state == "answer":

        remain = max(
            0,
            int(
                ANSWER_TIME -
                (time.time() - timer)
            )
        )

        text = fonts["heart"].render(

            f"TIME: {remain}",

            True,

            WHITE
        )

        screen.blit(

            text,

            (220, 560)
        )

    # =====================================================
    # GAME OVER
    # =====================================================

    elif state == "end":

        text = fonts["heart"].render(

            "GAME OVER",

            True,

            RED
        )

        screen.blit(

            text,

            (170, 560)
        )

        text2 = fonts["heart"].render(

            "Press R",

            True,

            WHITE
        )

        screen.blit(

            text2,

            (220, 620)
        )


# =========================================================
# RESET
# =========================================================

def reset_REPEAT_AFTER_ME():

    global level
    global score
    global lives
    global pattern
    global selected
    global state
    global timer
    global game_over

    level = 1

    score = 0

    lives = 3

    pattern = []

    selected = []

    state = "show"

    game_over = False

    timer = time.time()

    create_pattern()
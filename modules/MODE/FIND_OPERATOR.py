import random
import pygame

from modules.font import fonts


# ============================================================
# STATE
# ============================================================

ceill = 100

option_rects = []

correct_count = 0
wrong_count = 0

question_number = 1

find_operator_question = None

start_time = 0


# ============================================================
# TIME
# ============================================================

def get_question_time(question_number):

    current_time = 10 - ((question_number - 1) // 10)

    return max(
        5,
        current_time
    )


# ============================================================
# GENERATE QUESTION
# ============================================================

def generate_operator_question(ceill):

    while True:

        operator = random.choice(
            [
                "+",
                "-",
                "*",
                "/"
            ]
        )

        x = random.randint(
            1,
            ceill
        )

        y = random.randint(
            1,
            ceill
        )

        # ---------------- PLUS ----------------

        if operator == "+":

            result = x + y

        # ---------------- MINUS ----------------

        elif operator == "-":

            if x < y:
                x, y = y, x

            result = x - y

        # ---------------- MULTIPLY ----------------

        elif operator == "*":

            result = x * y

        # ---------------- DIVIDE ----------------

        else:

            if x < y:
                x, y = y, x

            result = x / y

            if result.is_integer():

                result = int(result)

            else:

                result = round(
                    result,
                    2
                )

        # ---------------- CEILING ----------------

        if result <= ceill:
            break

    return {
        "question": f"{x} ? {y} = {result}",
        "answer": operator,
        "options": [
            "+",
            "-",
            "*",
            "/"
        ]
    }


# ============================================================
# START GAME
# ============================================================

def start_game_find_Op():

    global correct_count
    global wrong_count
    global question_number
    global find_operator_question
    global start_time

    correct_count = 0
    wrong_count = 0

    question_number = 1

    find_operator_question = generate_operator_question(
        ceill
    )

    find_operator_question["time"] = get_question_time(
        question_number
    )

    start_time = pygame.time.get_ticks()


# ============================================================
# DRAW QUESTION
# ============================================================

def draw_question(
    screen,
    question
):

    global option_rects

    option_rects.clear()

    WIDTH = screen.get_width()
    HEIGHT = screen.get_height()

    # ========================================================
    # QUESTION
    # ========================================================

    question_text = fonts["heart"].render(
        question["question"],
        True,
        (255, 165, 0)
    )

    question_rect = question_text.get_rect(
        center=(
            WIDTH // 2,
            HEIGHT // 2 - 220
        )
    )

    screen.blit(
        question_text,
        question_rect
    )

    # ========================================================
    # OPTIONS
    # ========================================================

    option_width = 150
    option_height = 100

    gap = 30

    total_width = (
        option_width * 4
        +
        gap * 3
    )

    start_x = (
        WIDTH - total_width
    ) // 2

    y = HEIGHT // 2 + 100

    for i, option in enumerate(
        question["options"]
    ):

        x = start_x + i * (
            option_width + gap
        )

        rect = pygame.Rect(
            x,
            y,
            option_width,
            option_height
        )

        pygame.draw.rect(
            screen,
            (255, 255, 255),
            rect,
            border_radius=20
        )

        option_text = fonts["heart"].render(
            option,
            True,
            (0, 0, 0)
        )

        option_rect = option_text.get_rect(
            center=rect.center
        )

        screen.blit(
            option_text,
            option_rect
        )

        option_rects.append(
            (
                rect,
                option
            )
        )

    return option_rects


# ============================================================
# NEXT QUESTION
# ============================================================

def next_question_find_Op():

    global question_number
    global find_operator_question
    global start_time

    question_number += 1

    find_operator_question = generate_operator_question(
        ceill
    )

    find_operator_question["time"] = get_question_time(
        question_number
    )

    start_time = pygame.time.get_ticks()


# ============================================================
# UPDATE + DRAW
# ============================================================

def FIND_OPERATOR_(screen):

    global find_operator_question
    global wrong_count
    global start_time

    # --------------------------------------------------------
    # SAFETY
    # --------------------------------------------------------

    if find_operator_question is None:

        find_operator_question = generate_operator_question(
            ceill
        )

        find_operator_question["time"] = get_question_time(
            question_number
        )

        start_time = pygame.time.get_ticks()

    # --------------------------------------------------------
    # DRAW QUESTION
    # --------------------------------------------------------

    draw_question(
        screen,
        find_operator_question
    )

    # ========================================================
    # TIMER
    # ========================================================

    elapsed = (
        pygame.time.get_ticks()
        -
        start_time
    ) / 1000

    remaining_time = max(
        0,
        find_operator_question["time"] - int(elapsed)
    )

    timer_text = fonts["heart"].render(
        f"Time: {remaining_time}",
        True,
        (255, 255, 0)
    )

    timer_rect = timer_text.get_rect(
        center=(
            screen.get_width() // 2,
            80
        )
    )

    screen.blit(
        timer_text,
        timer_rect
    )

    # ========================================================
    # TIME OUT
    # ========================================================

    if elapsed >= find_operator_question["time"]:

        # فقط یک اشتباه
        wrong_count += 1

        # سؤال بعدی
        next_question_find_Op()

    # ========================================================
    # SCORE
    # ========================================================

    correct_text = fonts["heart"].render(
        f"Correct: {correct_count}",
        True,
        (0, 255, 0)
    )

    wrong_text = fonts["heart"].render(
        f"Wrong: {wrong_count}",
        True,
        (255, 0, 0)
    )

    screen.blit(
        correct_text,
        (50, 50)
    )

    screen.blit(
        wrong_text,
        (350, 50)
    )
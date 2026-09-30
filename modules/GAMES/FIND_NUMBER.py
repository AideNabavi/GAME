import random
import pygame

from modules.font import *
from modules.setting import draw_text_stroke


# ============================================================
# GAME STATE
# ============================================================


# ============================================================
# TIME
# ============================================================

def get_question_time():
    return 10


def get_remaining_time():

    if current_question is None:
        return 0

    elapsed = (
        pygame.time.get_ticks() - start_time
    ) / 1000

    remaining = (
        current_question["time"] - elapsed
    )

    return max(0, remaining)


def is_time_over():

    return get_remaining_time() <= 0


# ============================================================
# RESET GAME
# ============================================================

def reset_game():

    global current_question
    global question_number
    global start_time
    global correct_count
    global wrong_count

    current_question = None

    question_number = 1

    start_time = 0

    correct_count = 0
    wrong_count = 0


# ============================================================
# START GAME
# ============================================================

def start_game():

    global current_question
    global question_number
    global start_time
    global correct_count
    global wrong_count

    question_number = 1

    correct_count = 0
    wrong_count = 0

    current_question = generate_missing_number_question(
        question_number
    )

    start_time = pygame.time.get_ticks()


# ============================================================
# NEXT QUESTION
# ============================================================

def next_question():

    global current_question
    global question_number
    global start_time

    question_number += 1

    current_question = generate_missing_number_question(
        question_number
    )

    start_time = pygame.time.get_ticks()


# ============================================================
# CHECK TIME
# ============================================================

def update_game():

    if current_question is None:
        return

    if is_time_over():

        # تایم تمام شد = سؤال بعدی
        next_question()
# ============================================================
# GAME STATE
# ============================================================

current_question = None

question_number = 1

start_time = 0

correct_count = 0
wrong_count = 0


# ============================================================
# TIME
# ============================================================

def get_question_time():

    return 10


def get_remaining_time():

    global current_question
    global start_time

    if current_question is None:
        return 0

    elapsed = (
        pygame.time.get_ticks() - start_time
    ) / 1000

    remaining = (
        current_question["time"] - elapsed
    )

    return max(0, remaining)


def is_time_over():

    return get_remaining_time() <= 0


# ============================================================
# START GAME
# ============================================================

def start_game():

    global current_question
    global question_number
    global start_time
    global correct_count
    global wrong_count

    question_number = 1

    correct_count = 0
    wrong_count = 0

    current_question = generate_missing_number_question(
        question_number
    )

    start_time = pygame.time.get_ticks()


# ============================================================
# NEXT QUESTION
# ============================================================

def next_question():

    global current_question
    global question_number
    global start_time

    question_number += 1

    current_question = generate_missing_number_question(
        question_number
    )

    start_time = pygame.time.get_ticks()


# ============================================================
# ANSWER CEILING
# ============================================================

def get_answer_ceill(question_number):

    return (
        100
        + ((question_number - 1) // 10) * 50
    )


# ============================================================
# GENERATE QUESTION
# ============================================================

def generate_missing_number_question(
    question_number
):

    answer_ceill = get_answer_ceill(
        question_number
    )

    operators = [
        "+",
        "-",
        "*",
        "/"
    ]

    while True:

        operator = random.choice(
            operators
        )

        # ----------------------------------------------------
        # ADDITION
        # ----------------------------------------------------

        if operator == "+":

            result = random.randint(
                2,
                answer_ceill
            )

            x = random.randint(
                1,
                result - 1
            )

            y = result - x

        # ----------------------------------------------------
        # SUBTRACTION
        # ----------------------------------------------------

        elif operator == "-":

            result = random.randint(
                1,
                answer_ceill
            )

            y = random.randint(
                1,
                answer_ceill
            )

            x = result + y

        # ----------------------------------------------------
        # MULTIPLICATION
        # ----------------------------------------------------

        elif operator == "*":

            result = random.randint(
                2,
                answer_ceill
            )

            factors = []

            for i in range(
                1,
                result + 1
            ):

                if result % i == 0:

                    factors.append(
                        i
                    )

            if len(factors) < 2:
                continue

            x = random.choice(
                factors
            )

            y = result // x

            operator = "×"

        # ----------------------------------------------------
        # DIVISION
        # ----------------------------------------------------

        elif operator == "/":

            y = random.randint(
                1,
                20
            )

            result = random.randint(
                1,
                answer_ceill
            )

            x = result * y

            operator = "÷"

        # ----------------------------------------------------
        # CHECK
        # ----------------------------------------------------

        if result <= answer_ceill:

            break

    # ========================================================
    # CORRECT ANSWER
    # ========================================================

    correct = (
        x,
        y
    )

    # ========================================================
    # OPTIONS
    # ========================================================

    options = []

    # اول جواب صحیح
    options.append(
        correct
    )

    # سه جواب اشتباه
    while len(options) < 4:

        wrong = (
            random.randint(
                1,
                answer_ceill
            ),
            random.randint(
                1,
                answer_ceill
            )
        )

        if wrong not in options:

            options.append(
                wrong
            )

    # مخلوط کردن گزینه‌ها
    random.shuffle(
        options
    )

    # ========================================================
    # RETURN
    # ========================================================

    return {

        "question":
        f"? {operator} ? = {result}",

        "answer":
        correct,

        "options":
        options,

        "time":
        get_question_time()
    }


# ============================================================
# BUTTON
# ============================================================

button_width = 430
button_height = 250

option_rects = []

button = pygame.transform.smoothscale(
    pygame.image.load(
        "./asset/image/in_game/button.png"
    ).convert_alpha(),
    (
        button_width,
        button_height
    )
)


# ============================================================
# DRAW QUESTION
# ============================================================

def draw_question_find_number(
    screen,
    fonts,
    question,
    current_width,
    current_height
):

    global option_rects

    option_rects = []

    # ========================================================
    # SAFETY
    # ========================================================

    if question is None:

        return

    # ========================================================
    # QUESTION
    # ========================================================

    question_text = question["question"]

    question_surface = fonts[
        "quastion"
    ].render(
        question_text,
        True,
        (255, 255, 255)
    )

    question_stroke = fonts[
        "quastion"
    ].render(
        question_text,
        True,
        (0, 0, 0)
    )

    question_rect = question_surface.get_rect(
        center=(
            current_width // 2,
            current_height // 2 - 170
        )
    )

    draw_text_stroke(
        screen,
        question_stroke,
        question_rect.topleft,
        6
    )

    screen.blit(
        question_surface,
        question_rect
    )

    # ========================================================
    # OPTIONS POSITION
    # ========================================================

    gap_x = 450
    gap_y = 15

    center_x = current_width // 2

    center_y = (
        current_height // 2
        + 80
    )

    positions = [

        (
            center_x
            - button_width
            - gap_x // 2,

            center_y
        ),

        (
            center_x
            + gap_x // 2,

            center_y
        ),

        (
            center_x
            - button_width
            - gap_x // 2,

            center_y
            + button_height
            + gap_y
        ),

        (
            center_x
            + gap_x // 2,

            center_y
            + button_height
            + gap_y
        )
    ]

    # ========================================================
    # DRAW OPTIONS
    # ========================================================

    for i, option in enumerate(
        question["options"]
    ):

        # ----------------------------------------------------
        # Safety
        # ----------------------------------------------------

        if not isinstance(
            option,
            tuple
        ):

            continue

        if len(option) != 2:

            continue

        # ----------------------------------------------------
        # RECT
        # ----------------------------------------------------

        rect = pygame.Rect(
            positions[i][0],
            positions[i][1],
            button_width,
            button_height
        )

        # ----------------------------------------------------
        # BUTTON
        # ----------------------------------------------------

        screen.blit(
            button,
            rect
        )

        # ----------------------------------------------------
        # OPTION TEXT
        # ----------------------------------------------------

        option_value = (
            f"{option[0]}, {option[1]}"
        )

        option_surface = fonts[
            "answer"
        ].render(
            option_value,
            True,
            (255, 255, 255)
        )

        option_stroke = fonts[
            "answer"
        ].render(
            option_value,
            True,
            (0, 0, 0)
        )

        option_text_rect = (
            option_surface.get_rect(
                center=rect.center
            )
        )

        draw_text_stroke(
            screen,
            option_stroke,
            option_text_rect.topleft,
            2
        )

        screen.blit(
            option_surface,
            option_text_rect
        )

        # ----------------------------------------------------
        # SAVE RECT + ANSWER
        # ----------------------------------------------------

        option_rects.append(
            (
                rect,
                option
            )
        )
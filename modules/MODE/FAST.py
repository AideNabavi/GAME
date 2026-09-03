import random
import pygame

from modules.font import fonts


# ============================================================
# TIME
# ============================================================

def get_question_time():

    return 3


# ============================================================
# CEILING
# ============================================================

def get_answer_ceill():

    return 100


# ============================================================
# GENERATE QUESTION
# ============================================================

def generate_true_false_question():

    ceill = 100

    operators = [
        "+",
        "-",
        "*"
    ]

    while True:

        x = random.randint(
            1,
            ceill
        )

        y = random.randint(
            1,
            ceill
        )

        operator = random.choice(
            operators
        )

        if operator == "+":

            result = x + y

        elif operator == "-":

            result = x - y

        else:

            result = x * y

        if 0 <= result <= ceill:
            break

    is_true = random.choice(
        [
            True,
            False
        ]
    )

    if is_true:

        shown_result = result

    else:

        while True:

            shown_result = random.randint(
                0,
                ceill
            )

            if shown_result != result:
                break

    return {

        "question":
        f"{x} {operator} {y} = {shown_result}",

        "answer":
        is_true,

        "options":
        [
            True,
            False
        ],

        "time":
        get_question_time()
    }


# ============================================================
# STATE
# ============================================================

option_rects = []

current_question = generate_true_false_question()

start_time = pygame.time.get_ticks()

correct_count = 0
wrong_count = 0


# ============================================================
# RESET
# ============================================================

def reset_FAST():

    global current_question
    global start_time
    global correct_count
    global wrong_count
    global option_rects

    current_question = generate_true_false_question()

    start_time = pygame.time.get_ticks()

    correct_count = 0
    wrong_count = 0

    option_rects.clear()


# ============================================================
# NEXT QUESTION
# ============================================================

def next_question_FAST():

    global current_question
    global start_time

    current_question = generate_true_false_question()

    start_time = pygame.time.get_ticks()


# ============================================================
# DRAW QUESTION
# ============================================================

def draw_question(
    screen,
    font,
    question,
    WIDTH
):

    global option_rects

    # خیلی مهم
    # لیست گزینه‌ها را هر فریم پاک کن
    option_rects.clear()

    HEIGHT = screen.get_height()

    # ========================================================
    # QUESTION
    # ========================================================

    text = fonts["heart"].render(
        question["question"],
        True,
        (255, 165, 0)
    )

    text_rect = text.get_rect(
        center=(
            WIDTH // 2,
            HEIGHT // 2 - 220
        )
    )

    screen.blit(
        text,
        text_rect
    )

    # ========================================================
    # OPTIONS
    # ========================================================

    option_width = 200
    option_height = 100

    gap = 40

    total_width = (
        option_width * 2
        +
        gap
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

        # متن True / False
        if option is True:
            option_name = "TRUE"
        else:
            option_name = "FALSE"

        option_text = fonts["heart"].render(
            option_name,
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
# UPDATE + DRAW
# ============================================================

def FAST_(screen, WIDTH):

    global wrong_count
    global correct_count
    global start_time
    global current_question

    # ========================================================
    # SAFETY
    # ========================================================

    if current_question is None:

        current_question = generate_true_false_question()

        start_time = pygame.time.get_ticks()

    # ========================================================
    # DRAW
    # ========================================================

    draw_question(
        screen,
        fonts["heart"],
        current_question,
        WIDTH
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
        current_question["time"] - int(elapsed)
    )

    timer_text = fonts["heart"].render(
        f"Time: {remaining_time}",
        True,
        (255, 255, 0)
    )

    timer_rect = timer_text.get_rect(
        center=(
            WIDTH // 2,
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

    if elapsed >= current_question["time"]:

        # فقط یکی اضافه می‌شود
        wrong_count += 1

        # سؤال جدید
        next_question_FAST()

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

    # مرتب و وسط بالا

    score_gap = 80

    total_score_width = (
        correct_text.get_width()
        +
        wrong_text.get_width()
        +
        score_gap
    )

    score_start_x = (
        WIDTH - total_score_width
    ) // 2

    screen.blit(
        correct_text,
        (
            score_start_x,
            50
        )
    )

    screen.blit(
        wrong_text,
        (
            score_start_x
            +
            correct_text.get_width()
            +
            score_gap,
            50
        )
    )
    
    
    
    
    
    
    
    
def event_FAST_MODE(event):

    global current_question
    global correct_count
    global wrong_count
    global start_time

    if event.type != pygame.MOUSEBUTTONDOWN:
        return

    if event.button != 1:
        return

    mouse_pos = event.pos

    for rect, option in option_rects:

        if rect.collidepoint(mouse_pos):

            # ---------------- CORRECT ----------------

            if option == current_question["answer"]:

                correct_count += 1

            # ---------------- WRONG ----------------

            else:

                wrong_count += 1

            # سؤال بعدی
            next_question_FAST()

            break
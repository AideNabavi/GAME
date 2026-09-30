import pygame
import random
import sys

from modules.font import *


# ============================================================
# COLORS
# ============================================================

BACKGROUND = (20, 23, 32)
CARD = (43, 47, 60)
HOVER = (62, 68, 84)

WHITE = (245, 245, 245)
GRAY = (155, 160, 170)

BLUE = (70, 145, 240)
GREEN = (70, 210, 120)
RED = (230, 70, 80)
YELLOW = (245, 190, 70)


# ============================================================
# SETTINGS
# ============================================================

QUESTION_TIME = 10
TOTAL_OPTIONS = 4


# ============================================================
# GAME VARIABLES
# ============================================================

question_number = 1

score = 0

correct_answers = 0
wrong_answers = 0

time_left = QUESTION_TIME

question_start_time = 0

current_expression = ""
current_answer = 0

options = []

state = "PLAY"

result_text = ""
result_color = WHITE
result_start_time = 0


# ============================================================
# MAX NUMBER
# ============================================================

def get_max_number():

    return (
        100
        + ((question_number - 1) // 10) * 50
    )


# ============================================================
# CALCULATE EXPRESSION
# ============================================================

def calculate_expression(numbers, operators):

    nums = numbers[:]
    ops = operators[:]

    # --------------------------------------------------------
    # Multiplication / Division first
    # --------------------------------------------------------

    i = 0

    while i < len(ops):

        if ops[i] in ("*", "/"):

            a = nums[i]
            b = nums[i + 1]

            if ops[i] == "/":

                if b == 0:
                    return None

                if a % b != 0:
                    return None

                result = a // b

            else:

                result = a * b

            nums[i] = result

            del nums[i + 1]
            del ops[i]

        else:

            i += 1

    # --------------------------------------------------------
    # Addition / subtraction
    # --------------------------------------------------------

    result = nums[0]

    for i, op in enumerate(ops):

        if op == "+":

            result += nums[i + 1]

        elif op == "-":

            result -= nums[i + 1]

    return result


# ============================================================
# CREATE RANDOM EXPRESSION
# ============================================================

def create_random_expression():

    max_number = get_max_number()

    # --------------------------------------------------------
    # Number of operations
    # --------------------------------------------------------

    if question_number <= 10:

        operation_count = random.randint(2, 4)

    elif question_number <= 30:

        operation_count = random.randint(3, 5)

    else:

        operation_count = random.randint(3, 6)

    # --------------------------------------------------------
    # Try to create valid expression
    # --------------------------------------------------------

    for attempt in range(100):

        numbers = []
        operators = []

        # ----------------------------------------------------
        # Generate numbers
        # ----------------------------------------------------

        for i in range(operation_count + 1):

            number = random.randint(
                1,
                min(max_number, 30)
            )

            numbers.append(number)

        # ----------------------------------------------------
        # Generate operators
        # ----------------------------------------------------

        for i in range(operation_count):

            operator = random.choice(
                [
                    "+",
                    "-",
                    "*",
                    "/"
                ]
            )

            operators.append(operator)

        # ----------------------------------------------------
        # Force valid divisions
        # ----------------------------------------------------

        for i, op in enumerate(operators):

            if op == "/":

                divisor = numbers[i]

                multiplier = random.randint(
                    1,
                    min(20, max_number // max(1, divisor))
                )

                numbers[i + 1] = (
                    divisor * multiplier
                )

        # ----------------------------------------------------
        # Calculate normal expression
        # ----------------------------------------------------

        answer = calculate_expression(
            numbers,
            operators
        )

        if answer is None:
            continue

        # ----------------------------------------------------
        # Parentheses
        # ----------------------------------------------------

        expression = str(numbers[0])

        for i, operator in enumerate(operators):

            expression += (
                " "
                + operator
                + " "
                + str(numbers[i + 1])
            )

        if (
            operation_count >= 3
            and random.random() < 0.55
        ):

            start = random.randint(
                0,
                operation_count - 2
            )

            end = start + 1

            expression = ""

            for i in range(operation_count + 1):

                if i == start:
                    expression += "("

                expression += str(numbers[i])

                if i == end:
                    expression += ")"

                if i < operation_count:

                    expression += (
                        " "
                        + operators[i]
                        + " "
                    )

            # ------------------------------------------------
            # Evaluate expression
            # ------------------------------------------------

            try:

                answer = int(
                    eval(
                        expression,
                        {
                            "__builtins__": {}
                        }
                    )
                )

            except Exception:

                continue

        # ----------------------------------------------------
        # Validate answer
        # ----------------------------------------------------

        if answer < 0:
            continue

        if answer > max_number:
            continue

        # ----------------------------------------------------
        # Convert symbols for display
        # ----------------------------------------------------

        display_expression = (
            expression
            .replace("*", "×")
            .replace("/", "÷")
        )

        return (
            display_expression,
            answer
        )

    # --------------------------------------------------------
    # Fallback
    # --------------------------------------------------------

    return (
        "1 + 2 + 3",
        6
    )


# ============================================================
# CREATE QUESTION
# ============================================================

def create_question():

    global current_expression
    global current_answer
    global options
    global time_left
    global question_start_time
    global state

    (
        current_expression,
        current_answer
    ) = create_random_expression()

    # --------------------------------------------------------
    # Create answer options
    # --------------------------------------------------------

    options = [
        current_answer
    ]

    while len(options) < TOTAL_OPTIONS:

        difference = random.randint(
            1,
            max(
                5,
                current_answer // 4 + 5
            )
        )

        wrong_answer = random.choice(
            [
                current_answer + difference,
                current_answer - difference
            ]
        )

        if wrong_answer < 0:
            continue

        if wrong_answer in options:
            continue

        options.append(
            wrong_answer
        )

    random.shuffle(options)

    # --------------------------------------------------------
    # Timer
    # --------------------------------------------------------

    time_left = QUESTION_TIME

    question_start_time = pygame.time.get_ticks()

    state = "PLAY"


# ============================================================
# DRAW TEXT
# ============================================================

def draw_text(
    screen,
    value,
    font,
    color,
    center
):

    surface = font.render(
        str(value),
        True,
        color
    )

    rect = surface.get_rect(
        center=center
    )

    screen.blit(
        surface,
        rect
    )


# ============================================================
# HEADER
# ============================================================

def draw_header(screen, WIDTH):

    draw_text(
        screen,
        "MENTAL MATH",
        fonts["heart"],
        WHITE,
        (
            WIDTH // 2,
            45
        )
    )

    draw_text(
        screen,
        "Question " + str(question_number),
        fonts["heart"],
        WHITE,
        (
            110,
            45
        )
    )

    draw_text(
        screen,
        "Score: " + str(score),
        fonts["heart"],
        WHITE,
        (
            WIDTH - 100,
            45
        )
    )

def reset_game():

    global question_number
    global score
    global correct_answers
    global wrong_answers
    global time_left
    global question_start_time
    global current_expression
    global current_answer
    global options
    global state
    global result_text
    global result_color
    global result_start_time

    # --------------------------------------------------------
    # RESET GAME
    # --------------------------------------------------------

    question_number = 1

    score = 0

    correct_answers = 0
    wrong_answers = 0

    time_left = QUESTION_TIME

    question_start_time = 0

    current_expression = ""
    current_answer = 0

    options = []

    state = "PLAY"

    result_text = ""
    result_color = WHITE
    result_start_time = 0

    # --------------------------------------------------------
    # CREATE FIRST QUESTION
    # --------------------------------------------------------

    create_question()

# ============================================================
# TIMER
# ============================================================

def draw_timer(screen, WIDTH):

    center = (
        WIDTH // 2,
        145
    )

    radius = 42

    if time_left <= 3:

        color = RED

    elif time_left <= 5:

        color = YELLOW

    else:

        color = BLUE

    pygame.draw.circle(
        screen,
        CARD,
        center,
        radius
    )

    pygame.draw.circle(
        screen,
        color,
        center,
        radius,
        5
    )

    draw_text(
        screen,
        time_left,
        fonts["heart"],
        WHITE,
        center
    )


# ============================================================
# DRAW QUESTION
# ============================================================

def draw_question(screen, WIDTH, HEIGHT):

    screen.fill(
        BACKGROUND
    )

    draw_header(
        screen,
        WIDTH
    )

    draw_text(
        screen,
        "Range: 1 - " + str(get_max_number()),
        fonts["heart"],
        GRAY,
        (
            WIDTH // 2,
            95
        )
    )

    draw_timer(
        screen,
        WIDTH
    )

    # --------------------------------------------------------
    # Expression
    # --------------------------------------------------------

    draw_text(
        screen,
        current_expression + " = ?",
        fonts["heart"],
        WHITE,
        (
            WIDTH // 2,
            235
        )
    )

    # --------------------------------------------------------
    # Options
    # --------------------------------------------------------

    option_width = 300
    option_height = 100
    gap = 25

    positions = [

        (
            WIDTH // 2
            - option_width
            - gap // 2,
            350
        ),

        (
            WIDTH // 2
            + gap // 2,
            350
        ),

        (
            WIDTH // 2
            - option_width
            - gap // 2,
            475
        ),

        (
            WIDTH // 2
            + gap // 2,
            475
        )

    ]

    mouse = pygame.mouse.get_pos()

    for i, option in enumerate(options):

        x, y = positions[i]

        rect = pygame.Rect(
            x,
            y,
            option_width,
            option_height
        )

        if rect.collidepoint(mouse):

            color = HOVER

        else:

            color = CARD

        pygame.draw.rect(
            screen,
            color,
            rect,
            border_radius=20
        )

        pygame.draw.rect(
            screen,
            BLUE,
            rect,
            2,
            border_radius=20
        )

        draw_text(
            screen,
            option,
            fonts["heart"],
            WHITE,
            rect.center
        )

        draw_text(
            screen,
            i + 1,
            fonts["heart"],
            GRAY,
            (
                rect.x + 25,
                rect.y + 25
            )
        )

    # --------------------------------------------------------
    # Statistics
    # --------------------------------------------------------

    draw_text(
        screen,
        "Correct: " + str(correct_answers),
        fonts["heart"],
        GREEN,
        (
            WIDTH // 2 - 100,
            HEIGHT - 40
        )
    )

    draw_text(
        screen,
        "Wrong: " + str(wrong_answers),
        fonts["heart"],
        RED,
        (
            WIDTH // 2 + 100,
            HEIGHT - 40
        )
    )


# ============================================================
# DRAW RESULT
# ============================================================

def draw_result(screen, WIDTH, HEIGHT):

    screen.fill(
        BACKGROUND
    )

    draw_header(
        screen,
        WIDTH
    )

    draw_text(
        screen,
        result_text,
        fonts["heart"],
        result_color,
        (
            WIDTH // 2,
            HEIGHT // 2
        )
    )


# ============================================================
# ANSWER
# ============================================================

def answer_question(selected_answer):

    global question_number
    global score
    global correct_answers
    global wrong_answers
    global state
    global result_text
    global result_color
    global result_start_time

    if selected_answer == current_answer:

        correct_answers += 1

        score += 100

        result_text = "CORRECT!"

        result_color = GREEN

    else:

        wrong_answers += 1

        result_text = "WRONG!"

        result_color = RED

    result_start_time = pygame.time.get_ticks()

    state = "RESULT"


# ============================================================
# TIMER CHECK
# ============================================================

def check_timer():

    global time_left
    global state
    global wrong_answers
    global result_text
    global result_color
    global result_start_time

    now = pygame.time.get_ticks()

    elapsed = (
        now - question_start_time
    )

    time_left = max(
        0,
        QUESTION_TIME
        - elapsed // 1000
    )

    if time_left <= 0:

        wrong_answers += 1

        result_text = "TIME UP!"

        result_color = RED

        result_start_time = now

        state = "RESULT"


# ============================================================
# CLICK OPTION
# ============================================================

def click_option(position, WIDTH):

    option_width = 300
    option_height = 100
    gap = 25

    positions = [

        (
            WIDTH // 2
            - option_width
            - gap // 2,
            350
        ),

        (
            WIDTH // 2
            + gap // 2,
            350
        ),

        (
            WIDTH // 2
            - option_width
            - gap // 2,
            475
        ),

        (
            WIDTH // 2
            + gap // 2,
            475
        )

    ]

    for i, option in enumerate(options):

        rect = pygame.Rect(
            positions[i][0],
            positions[i][1],
            option_width,
            option_height
        )

        if rect.collidepoint(position):

            answer_question(
                option
            )

            return


# ============================================================
# START
# ============================================================




# ============================================================
# MAIN GAME FUNCTION
# ============================================================

def MATH_GO_(screen):

    WIDTH, HEIGHT = screen.get_size()

    # --------------------------------------------------------
    # EVENTS
    # --------------------------------------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                if state == "PLAY":

                    click_option(
                        event.pos,
                        WIDTH
                    )

    # --------------------------------------------------------
    # PLAY
    # --------------------------------------------------------

    if state == "PLAY":

        check_timer()

        draw_question(
            screen,
            WIDTH,
            HEIGHT
        )

    # --------------------------------------------------------
    # RESULT
    # --------------------------------------------------------

    elif state == "RESULT":

        draw_result(
            screen,
            WIDTH,
            HEIGHT
        )

        now = pygame.time.get_ticks()

        if (
            now - result_start_time
            >= 700
        ):

            globals()["question_number"] += 1

            create_question()
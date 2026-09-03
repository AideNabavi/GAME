import pygame
import random
import sys


pygame.init()


# ============================================================
# SCREEN
# ============================================================

WIDTH = 1200
HEIGHT = 800

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "Mental Math Challenge"
)

clock = pygame.time.Clock()


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
# FONTS
# ============================================================

font_title = pygame.font.Font(None, 48)
font_question = pygame.font.Font(None, 52)
font_option = pygame.font.Font(None, 36)
font_normal = pygame.font.Font(None, 28)
font_small = pygame.font.Font(None, 22)
font_result = pygame.font.Font(None, 70)


# ============================================================
# SETTINGS
# ============================================================

QUESTION_TIME = 10

TOTAL_OPTIONS = 4


# ============================================================
# GAME
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

def calculate_expression(
    numbers,
    operators
):

    # --------------------------------------------------------
    # Work on copies
    # --------------------------------------------------------

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


            # Division must be integer

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
    #
    # Early game:
    # 2-4 operations
    #
    # Later:
    # 3-6 operations
    # --------------------------------------------------------

    if question_number <= 10:

        operation_count = random.randint(
            2,
            4
        )

    elif question_number <= 30:

        operation_count = random.randint(
            3,
            5
        )

    else:

        operation_count = random.randint(
            3,
            6
        )


    # --------------------------------------------------------
    # Generate many times until valid
    # --------------------------------------------------------

    for attempt in range(100):

        numbers = []

        operators = []


        # ----------------------------------------------------
        # Generate numbers
        # ----------------------------------------------------

        for i in range(
            operation_count + 1
        ):

            # Multiplication and division
            # use smaller numbers so that
            # answers don't explode.

            number = random.randint(
                1,
                min(
                    max_number,
                    30
                )
            )

            numbers.append(
                number
            )


        # ----------------------------------------------------
        # Generate operators
        # ----------------------------------------------------

        for i in range(
            operation_count
        ):

            operator = random.choice(
                [
                    "+",
                    "-",
                    "*",
                    "/"
                ]
            )

            operators.append(
                operator
            )


        # ----------------------------------------------------
        # Force valid divisions
        # ----------------------------------------------------

        for i, op in enumerate(
            operators
        ):

            if op == "/":

                divisor = numbers[i]

                # Change next number so division
                # becomes clean.

                multiplier = random.randint(
                    1,
                    min(
                        20,
                        max_number
                    )
                )

                numbers[i + 1] = (
                    divisor * multiplier
                )


        # ----------------------------------------------------
        # Calculate
        # ----------------------------------------------------

        answer = calculate_expression(
            numbers,
            operators
        )


        if answer is None:

            continue


        # Avoid very large or negative answers.

        if answer < 0:

            continue


        if answer > max_number:

            continue


        # ----------------------------------------------------
        # Build expression
        # ----------------------------------------------------

        expression = str(
            numbers[0]
        )


        for i, operator in enumerate(
            operators
        ):

            expression += (
                " "
                + operator
                + " "
                + str(numbers[i + 1])
            )


        # ----------------------------------------------------
        # Random parentheses
        # ----------------------------------------------------

        if (
            operation_count >= 3
            and random.random() < 0.55
        ):

            start = random.randint(
                0,
                operation_count - 2
            )

            end = start + 1


            left = ""

            for i in range(
                start,
                end + 2
            ):

                if i == start:

                    left += "("

                left += str(
                    numbers[i]
                )

                if i < end + 1:

                    left += (
                        " "
                        + operators[i]
                        + " "
                    )


            left += ")"


            # Build again with parentheses.

            expression = ""


            for i in range(
                operation_count + 1
            ):

                if i == start:

                    expression += "("


                expression += str(
                    numbers[i]
                )


                if i == end + 1:

                    expression += ")"


                if i < operation_count:

                    expression += (
                        " "
                        + operators[i]
                        + " "
                    )


            # Evaluate parentheses correctly
            try:

                answer = int(
                    eval(
                        expression
                    )
                )

            except:

                continue


            if answer < 0:

                continue


            if answer > max_number:

                continue


        # ----------------------------------------------------
        # Convert symbols
        # ----------------------------------------------------

        display_expression = (
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
    # Options
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


    random.shuffle(
        options
    )


    # --------------------------------------------------------
    # Timer
    # --------------------------------------------------------

    time_left = QUESTION_TIME

    question_start_time = (
        pygame.time.get_ticks()
    )

    state = "PLAY"


# ============================================================
# DRAW TEXT
# ============================================================

def draw_text(
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

def draw_header():

    draw_text(
        "MENTAL MATH",
        font_title,
        WHITE,
        (
            WIDTH // 2,
            45
        )
    )


    draw_text(
        "Question "
        + str(question_number),
        font_normal,
        WHITE,
        (
            110,
            45
        )
    )


    draw_text(
        "Score: "
        + str(score),
        font_normal,
        WHITE,
        (
            WIDTH - 100,
            45
        )
    )


# ============================================================
# TIMER
# ============================================================

def draw_timer():

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
        time_left,
        font_normal,
        WHITE,
        center
    )


# ============================================================
# DRAW QUESTION
# ============================================================

def draw_question():

    screen.fill(
        BACKGROUND
    )


    draw_header()


    draw_text(
        "Range: 1 - "
        + str(get_max_number()),
        font_small,
        GRAY,
        (
            WIDTH // 2,
            95
        )
    )


    draw_timer()


    # --------------------------------------------------------
    # Expression
    # --------------------------------------------------------

    draw_text(
        current_expression
        + " = ?",
        font_question,
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


    for i, option in enumerate(
        options
    ):

        x, y = positions[i]


        rect = pygame.Rect(
            x,
            y,
            option_width,
            option_height
        )


        if rect.collidepoint(
            mouse
        ):

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
            option,
            font_option,
            WHITE,
            rect.center
        )


        draw_text(
            i + 1,
            font_small,
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
        "Correct: "
        + str(correct_answers),
        font_small,
        GREEN,
        (
            WIDTH // 2 - 100,
            HEIGHT - 40
        )
    )


    draw_text(
        "Wrong: "
        + str(wrong_answers),
        font_small,
        RED,
        (
            WIDTH // 2 + 100,
            HEIGHT - 40
        )
    )


# ============================================================
# RESULT
# ============================================================

def draw_result():

    screen.fill(
        BACKGROUND
    )


    draw_header()


    draw_text(
        result_text,
        font_result,
        result_color,
        (
            WIDTH // 2,
            HEIGHT // 2
        )
    )


# ============================================================
# ANSWER
# ============================================================

def answer_question(
    selected_answer
):

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


    result_start_time = (
        pygame.time.get_ticks()
    )

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

def click_option(
    position
):

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


    for i, option in enumerate(
        options
    ):

        rect = pygame.Rect(
            positions[i][0],
            positions[i][1],
            option_width,
            option_height
        )


        if rect.collidepoint(
            position
        ):

            answer_question(
                option
            )

            return


# ============================================================
# START
# ============================================================

create_question()


# ============================================================
# MAIN LOOP
# ============================================================

running = True


while running:

    # ========================================================
    # EVENTS
    # ========================================================

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:

                running = False


            if state == "PLAY":

                if event.key == pygame.K_1:

                    answer_question(
                        options[0]
                    )

                elif event.key == pygame.K_2:

                    answer_question(
                        options[1]
                    )

                elif event.key == pygame.K_3:

                    answer_question(
                        options[2]
                    )

                elif event.key == pygame.K_4:

                    answer_question(
                        options[3]
                    )


        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                if state == "PLAY":

                    click_option(
                        event.pos
                    )


    # ========================================================
    # PLAY
    # ========================================================

    if state == "PLAY":

        check_timer()

        draw_question()


    # ========================================================
    # RESULT
    # ========================================================

    elif state == "RESULT":

        draw_result()


        now = pygame.time.get_ticks()


        if (
            now - result_start_time
            >= 700
        ):

            question_number += 1

            create_question()


    # ========================================================
    # DISPLAY
    # ========================================================

    pygame.display.flip()

    clock.tick(60)


# ============================================================
# QUIT
# ============================================================

pygame.quit()

sys.exit()
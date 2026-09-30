import random
import pygame


from modules.font import fonts
# ---------------- Time ----------------

def get_question_time():

    return 10



# ---------------- Result Ceiling ----------------

def get_result_ceill(question_number):

    return 100 + ((question_number - 1) // 10) * 50



# ---------------- Make Expression ----------------

def make_expression(
    ceill
):

    operators = [

        "+",
        "-",
        "*",
        "/"

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



        elif operator == "*":

            result = x * y



        elif operator == "/":


            if y == 0:

                continue


            # فقط تقسیم صحیح

            if x % y != 0:

                continue


            result = x // y



        # کنترل سقف نتیجه

        if abs(result) <= ceill:

            break



    return (

        f"{x}{operator}{y}",

        result

    )





# ---------------- Generate Compare Question ----------------

def generate_compare_question(
    question_number
):


    ceill = get_result_ceill(
        question_number
    )



    left_text, left_result = make_expression(
        ceill
    )


    right_text, right_result = make_expression(
        ceill
    )



    if left_result > right_result:

        answer = ">"



    elif left_result < right_result:

        answer = "<"



    else:

        answer = "="



    return {


        "question":

        f"{left_text}  ?  {right_text}",



        "answer":

        answer,



        "options":

        [

            ">",
            "=",
            "<"

        ],



        "time":

        get_question_time()

    }




option_rects = []



# ---------------- Draw Question ----------------
def draw_question(screen, font, question):

    global option_rects

    option_rects.clear()

    # ---------------- Question ----------------

    text = fonts["heart"].render(
        question["question"],
        True,
        (255, 165, 0)
    )

    text_rect = text.get_rect(
        center=(screen.get_width() // 2, 220)
    )

    screen.blit(
        text,
        text_rect
    )

    # ---------------- Options ----------------

    option_width = 200
    option_height = 100

    gap = 40

    total_width = (
        option_width * 3
        +
        gap * 2
    )

    start_x = (
        screen.get_width() - total_width
    ) // 2

    y = 500

    for i, option in enumerate(question["options"]):

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



# ---------------- Game ----------------

question_number = 1

current_question = generate_compare_question(
    question_number
)

start_time = pygame.time.get_ticks()

correct_count = 0
wrong_count = 0


# ---------------- Reset Game ----------------

def reset_MORE_LESS_EQUAL():

    global question_number
    global current_question
    global start_time
    global correct_count
    global wrong_count

    question_number = 1

    correct_count = 0
    wrong_count = 0

    current_question = generate_compare_question(
        question_number
    )

    start_time = pygame.time.get_ticks()


# ---------------- Draw Game ----------------

def MORE_LESS_EQUAL_(screen):

    global current_question
    global correct_count
    global wrong_count
    global start_time
    global question_number

    option_rects = draw_question(
        screen,
        fonts["heart"],
        current_question
    )

    # -------- Timer --------

    elapsed = (
        pygame.time.get_ticks()
        -
        start_time
    ) / 1000

    remaining = max(
        0,
        current_question["time"]
        -
        int(elapsed)
    )

    timer = fonts["heart"].render(
        f"Time: {remaining}",
        True,
        (255,255,0)
    )

    screen.blit(
        timer,
        (900,50)
    )

    # -------- Time Out --------

    if elapsed >= current_question["time"]:

        # یک اشتباه
        wrong_count += 1

        question_number += 1

        current_question = generate_compare_question(
            question_number
        )

        start_time = pygame.time.get_ticks()

    # -------- Score --------

    correct = fonts["heart"].render(
        f"Correct: {correct_count}",
        True,
        (0,255,0)
    )

    wrong = fonts["heart"].render(
        f"Wrong: {wrong_count}",
        True,
        (255,0,0)
    )

    screen.blit(
        correct,
        (50,50)
    )

    screen.blit(
        wrong,
        (300,50)
    )

    return option_rects


# ---------------- Event ----------------

def event_MORE_LESS_EQUAL(event, option_rects):

    global current_question
    global correct_count
    global wrong_count
    global question_number
    global start_time

    if event.type != pygame.MOUSEBUTTONDOWN:
        return

    if event.button != 1:
        return

    mouse_pos = event.pos

    for rect, option in option_rects:

        if rect.collidepoint(mouse_pos):

            # -------- Correct --------

            if option == current_question["answer"]:

                correct_count += 1

            # -------- Wrong --------

            else:

                wrong_count += 1

            # سوال بعدی

            question_number += 1

            current_question = generate_compare_question(
                question_number
            )

            start_time = pygame.time.get_ticks()

            break
import random
import pygame
from modules.font import *
from modules.setting import draw_text_stroke



# ---------------- Time ----------------

def get_question_time():

    return 10





# ---------------- Answer Ceiling ----------------

def get_answer_ceill(question_number):

    return 100 + ((question_number - 1) // 10) * 50










# ---------------- Generate Question ----------------

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



        elif operator == "*":

            result = random.randint(
                2,
                answer_ceill
            )


            factors = []


            for i in range(1, result + 1):

                if result % i == 0:

                    factors.append(i)



            if len(factors) < 2:

                continue



            x = random.choice(
                factors
            )


            y = result // x



            operator = "×"
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


            operator ="÷"
        if result <= answer_ceill:

            break

        


    correct = (
        x,
        y
    )



    options = [
        correct
    ]



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



    random.shuffle(
        options
    )



    return {

        "question":
        f"? {operator} ? = {result}",


        "answer":
        correct,


        "options":
        options,


        "time":
        10

    }




button_width = 430
button_height = 250
option_rects = []
# button=pygame.image.load("./asset/image/in_game/button.png")
button=pygame.transform.smoothscale(pygame.image.load("./asset/image/in_game/button.png").convert_alpha(),(button_width,button_height))

# ---------------- Draw Question ----------------

def draw_question_find_number(
    screen,
    fonts,
    question,
    current_width,
    current_height
):


    global option_rects

    option_rects = []


    # ---------------- Question ----------------

    question_text = question["question"]


    # متن نارنجی
    question_surface = fonts["quastion"].render(
        question_text,
        True,
        (255,255,255)
        # (255,165,0)
    )


    # استروک مشکی
    question_stroke = fonts["quastion"].render(
        question_text,
        True,
        (0,0,0)
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



    # ---------------- Options ----------------



    gap_x = 450
    gap_y = 15


    center_x = current_width // 2
    center_y = current_height // 2 + 80


    positions = [

        (
            center_x - button_width - gap_x//2,
            center_y
        ),

        (
            center_x + gap_x//2,
            center_y
        ),

        (
            center_x - button_width - gap_x//2,
            center_y + button_height + gap_y
        ),

        (
            center_x + gap_x//2,
            center_y + button_height + gap_y
        )

    ]
    for i, option__ in enumerate(
        question["options"]
    ):


        rect = pygame.Rect(
            positions[i][0],
            positions[i][1],
            button_width,
            button_height
        )

        # # پس زمینه گزینه
        # pygame.draw.rect(
        #     screen,
        #     (60,60,60),
        #     rect,
        #     border_radius=20
        # )

        screen.blit(button,rect)

        option_value = f"{option__[0]}, {option__[1]}"


        # متن سفید
        option_surface = fonts["answer"].render(
            option_value,
            True,
            (255,255,255)
            # (255,165,0)
        )


        # استروک مشکی
        option_stroke = fonts["answer"].render(
            option_value,
            True,
            (0,0,0)
        )


        option_text_rect = option_surface.get_rect(
            center=rect.center
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


        option_rects.append(
            (
                rect,
                option__
            )
        )



    return option_rects























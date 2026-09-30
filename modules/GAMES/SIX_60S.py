import random
import pygame
from modules.font import fonts






def start_game():

    global game_start_time
    global game_over
    global score
    global wrong
    global question

    game_start_time = pygame.time.get_ticks()

    game_over = False
    score = 0
    wrong = 0
    question = generate_question()


# ---------------- Generate Question ----------------

def generate_question():


    ceill = 150


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

            answer = x + y



        elif operator == "-":

            answer = x - y



        elif operator == "*":

            answer = x * y




        if 0 <= answer <= ceill:

            break




    options = [

        answer

    ]



    while len(options) < 4:


        wrong = random.randint(

            0,

            ceill

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

        f"{x} {operator} {y} = ?",



        "answer":

        answer,



        "options":

        options

    }























# ---------------- Draw Question ----------------

def draw_question(
    question,
    screen,
    WIDTH
):


    rects = []



    text = fonts["heart"].render(

        question["question"],

        True,

        (255,165,0)

    )


    text_rect = text.get_rect(

        center=(WIDTH//2,150)

    )


    screen.blit(

        text,

        text_rect

    )




    positions = [

        (200,350),

        (700,350),

        (200,500),

        (700,500)

    ]



    for i, option in enumerate(

        question["options"]

    ):



        rect = pygame.Rect(

            positions[i][0],

            positions[i][1],

            300,

            100

        )



        pygame.draw.rect(

            screen,

            (255,255,255),

            rect,

            border_radius=20

        )



        option_text = fonts["heart"].render(

            str(option),

            True,

            (0,0,0)

        )



        option_rect = option_text.get_rect(

            center=rect.center

        )



        screen.blit(

            option_text,

            option_rect

        )



        rects.append(

            (

                rect,

                option

            )

        )



    return rects







# ---------------- Game ----------------


question = generate_question()



score = 0


wrong = 0



game_start_time =  None





game_over = False




















option_rects=[]




def SIX_60S(screen,WIDTH):
    global game_over
    global wrong
    global score
    global  option_rects
    global game_start_time

    if not game_over:


        option_rects = draw_question(

            question,
            screen,
            WIDTH

        )



        # Timer


        elapsed = (

            pygame.time.get_ticks()

            -

            game_start_time

        ) / 1000



        remaining = max(

            0,

            60 - int(elapsed)

        )



        timer_text = fonts["heart"].render(

            f"Time: {remaining}",

            True,

            (255,255,0)

        )


        screen.blit(

            timer_text,

            (950,50)

        )



        score_text = fonts["heart"].render(

            f"Score: {score}",

            True,

            (0,255,0)

        )


        screen.blit(

            score_text,

            (50,50)

        )



        if elapsed >= 60:


            game_over = True





    else:



        over_text = fonts["heart"].render(

            "GAME OVER",

            True,

            (255,0,0)

        )


        over_rect = over_text.get_rect(

            center=(WIDTH//2,250)

        )


        screen.blit(

            over_text,

            over_rect

        )



        score_text = fonts["heart"].render(

            f"Score: {score}",

            True,

            (255,255,255)

        )


        score_rect = score_text.get_rect(

            center=(WIDTH//2,350)

        )


        screen.blit(

            score_text,

            score_rect

        )





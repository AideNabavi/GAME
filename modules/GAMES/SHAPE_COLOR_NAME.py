import pygame
import random
import time
from modules.font import fonts



# ------------------------
# Colors
# ------------------------

BG = (30,30,30)

WHITE = (255,255,255)

GRAY = (70,70,70)


COLORS = {

    "RED": (255,50,50),
    "BLUE": (50,120,255),
    "GREEN": (50,220,100),
    "YELLOW": (255,220,0),
    "PURPLE": (180,70,255),
    "ORANGE": (255,150,30),
    "BLACK": (0,0,0),
    "WHAIT": (255,255,255)

}


color_names = list(
    COLORS.keys()
)



# ------------------------
# Game Variables
# ------------------------

score = 0

level = 1


QUESTION_TIME = 10

start_time = 0



word_text = None

word_color = None

background_color = None


question = None

options = []





# ------------------------
# Create Question
# ------------------------
def new_question_SHAPE_COLOR_NAME():

    global word_text
    global word_color
    global background_color
    global question
    global options
    global start_time


    # انتخاب سه رنگ کاملا متفاوت

    selected_colors = random.sample(
        color_names,
        3
    )


    word_text = selected_colors[0]

    word_color = selected_colors[1]

    background_color = selected_colors[2]



    questions = [

        "Text Color?",

        "Background Color?",

        "Word Mean?"

    ]


    question = random.choice(
        questions
    )



    if question == "Text Color?":

        correct = word_color


    elif question == "Background Color?":

        correct = background_color


    else:

        correct = word_text



    wrong = [
        x for x in color_names
        if x != correct
    ]


    options = random.sample(
        wrong,
        3
    )


    options.append(
        correct
    )


    random.shuffle(
        options
    )


    start_time = time.time()



buttons = []

# ------------------------
# Buttons
# ------------------------
def one____(screen, width, height):
    global buttons

    buttons.clear()

    button_width = 250
    button_height = 60

    gap_x = 100
    gap_y = 20

    start_x = width // 2 - button_width - gap_x // 2
    start_y = height // 2 + 80   # کمی پایین‌تر از مرکز

    for i in range(4):

        col = i % 2
        row = i // 2

        rect = pygame.Rect(
            start_x + col * (button_width + gap_x),
            start_y + row * (button_height + gap_y),
            button_width,
            button_height
        )

        buttons.append(rect)






def SHAPE_COLOR_NAME(screen,WIDTH):
    global word_text
    global word_color
    global background_color
    global question
    global options
    global start_time
    global score

    # ------------------------
    # Timer
    # ------------------------

    remaining = int(

        QUESTION_TIME -

        (time.time() - start_time)

    )



    if remaining <= 0:


        score -= 1

        new_question_SHAPE_COLOR_NAME()






    # ------------------------
    # Draw Circle
    # ------------------------

    pygame.draw.circle(

        screen,

        COLORS[background_color],

        (WIDTH//2,230),

        120

    )



    word = fonts["heart"].render(

        word_text,

        True,

        COLORS[word_color]

    )


    word_rect = word.get_rect(

        center=(WIDTH//2,230)

    )


    screen.blit(

        word,

        word_rect

    )





    # Question

    q = fonts["heart"].render(

        question,

        True,

        WHITE

    )


    screen.blit(

        q,

        (250,50)

    )





    # Timer

    timer_text = fonts["heart"].render(

        f"Time: {max(0,remaining)}",

        True,

        WHITE

    )


    screen.blit(

        timer_text,

        (50,50)

    )





    # Score

    score_text = fonts["heart"].render(

        f"Score: {score}   Level: {level}",

        True,

        WHITE

    )


    screen.blit(

        score_text,

        (50,90)

    )







    # Answer Buttons

    for i,rect in enumerate(buttons):


        pygame.draw.rect(

            screen,

            GRAY,

            rect,

            border_radius=15

        )


        if i < len(options):

            answer_text = fonts["heart"].render(
                options[i],
                True,
                WHITE
            )


        answer_rect = answer_text.get_rect(

            center=rect.center

        )


        screen.blit(

            answer_text,

            answer_rect

        )

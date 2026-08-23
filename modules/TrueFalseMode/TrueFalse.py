import random
import pygame
from modules.button import exit_button 
from modules.font import fonts

from modules.timer import draw_timer_bar


MAX_NUMBER = 150

question_text_TrueFalse = ""
correct_operator = ""

answers = []

question_start_time = 0
# ---------------- Generate Operator Question ----------------

def generate_operator_question():

    operators = [
        "+",
        "-",
        "*",
        "/"
    ]


    while True:
        
        x = random.randint(1, MAX_NUMBER)
        y = random.randint(1, MAX_NUMBER)


        operator = random.choice(operators)



        # جمع

        if operator == "+":

            result = x + y


        # تفریق

        elif operator == "-":

            if x < y:
                x, y = y, x

            result = x - y



        # ضرب

        elif operator == "*":

            result = x * y



        # تقسیم

        elif operator == "/":


            # تقسیم صحیح

            if x % y != 0:

                continue


            result = x // y



        # محدودیت سقف 150

        if result <= MAX_NUMBER:


            question_text_TrueFalse = (
                f"{x} ? {y} = {result}"
            )


            return (
                question_text_TrueFalse,
                operator
            )





# ---------------- Generate Operator Answers ----------------


def generate_operator_answers(correct_operator):


    operators = [
        "+",
        "-",
        "*",
        "/"
    ]


    answers = operators.copy()


    random.shuffle(
        answers
    )


    return answers







# ---------------- Time System ----------------


def get_time_limit(question_count):


    time_limit = (
        10 -
        (question_count // 20)
    )


    if time_limit < 5:

        time_limit = 5



    return time_limit





# ---------------- Check Answer ----------------


def check_operator_answer(

    selected_operator,
    correct_operator,
    score

):


    if selected_operator == correct_operator:

        score += 1


    else:

        score -= 1



    return score





# ---------------- Example ----------------


score = 0

question_count = 0



question, correct = generate_operator_question()


answers = generate_operator_answers(
    correct
)



time_limit = get_time_limit(
    question_count
)



print(question)

print(answers)

print(
    "Time:",
    time_limit
)










def draw_game_screen(screen, fonts):

    # سوال

    text = fonts.render(
        question_text_TrueFalse,
        True,
        (255,255,255)
    )


    rect = text.get_rect(
        center=(
            screen.get_width() // 2,
            200
        )
    )


    screen.blit(
        text,
        rect
    )



    # جواب ها

    button_y = 350

    for i, answer in enumerate(answers):


        answer_text = fonts.render(
            answer,
            True,
            (255,220,0)
        )


        answer_rect = answer_text.get_rect(
            center=(
                250 + i * 180,
                button_y
            )
        )


        screen.blit(
            answer_text,
            answer_rect
        )






# current_width, current_height = screen.get_size()


# #------------------------------------------------------------- Time image
# timer_icon = pygame.image.load(
#     "./asset/image/time_image.png"
# ).convert_alpha()

# timer_icon = pygame.transform.smoothscale(
#     timer_icon,
#     (45,45)
# )


# #------------------------------------

# exit_button_rect = pygame.Rect(
#     current_width - 110,  # فاصله از راست
#     20,                   # فاصله از بالا
#     90,
#     90
# )


# #------------------------------------------------------------- Score


# score = 0
# score_icon = pygame.image.load(
#     "./asset/image/imagee.png"
# ).convert_alpha()

# score_icon = pygame.transform.smoothscale(
#     score_icon,
#     (80,80)
# )
# # ---------------- time image----------------
# time_icon = pygame.image.load(
#     "./asset/image/ttime.png"
# ).convert_alpha()

# time_icon = pygame.transform.smoothscale(
#     time_icon,
#     (150,150)
# )






# # ---------------- Score Display ----------------

# score_text = fonts["name"].render(
#     str(score),
#     True,
#     (255,220,0)
# )


# score_rect = score_text.get_rect(
#     midleft=(
#         current_width // 2 + 35,
#         45
#     )
# )


# icon_rect = score_icon.get_rect(
#     center=(
#         current_width // 2,
#         45
#     )
# )


# screen.blit(
#     score_icon,
#     icon_rect
# )


# screen.blit(
#     score_text,
#     score_rect
# )




# exit_button(screen,exit_button_rect)


# # ---------------- Show Time Limit ----------------
# question_start_time = 0

# elapsed = pygame.time.get_ticks() - question_start_time


# progress = 1 - (
#     elapsed / (time_limit * 1000)
# )


# progress = max(0, min(1, progress))


# timer_rect = pygame.Rect(
#     current_width - 320,
#     25,
#     280,
#     35
# )



            


# timer_rect = pygame.Rect(
#     current_width // 2 -120,
#     current_height // 2 - 329,
#     280,
#     35
# )


# draw_timer_bar(
#     screen,
#     timer_rect,
#     progress
# )

# if timer_icon:

#     icon_rect = timer_icon.get_rect(
#         center=(
#             timer_rect.left - 35,
#             timer_rect.centery
#         )
#     )

#     screen.blit(
#         timer_icon,
#         icon_rect
#     )
    
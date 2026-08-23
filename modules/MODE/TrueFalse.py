import random
import pygame



# ---------------- Time ----------------

def get_question_time():

    return 10



# ---------------- Ceiling ----------------

def get_answer_ceill(question_number):

    return 100 + ((question_number - 1) // 20) * 50

# ---------------- Generate Question ----------------

def generate_true_false_question(
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


        x = random.randint(
            1,
            answer_ceill
        )


        y = random.randint(
            1,
            answer_ceill
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


            result = x / y


            result = round(
                result,
                2
            )



        # فقط جواب کنترل می‌شود

        if abs(result) <= answer_ceill:

            break



    # درست یا غلط کردن سوال

    is_true = random.choice(
        [
            True,
            False
        ]
    )


    if is_true:

        shown_result = result


    else:

        shown_result = result + random.randint(
            1,
            20
        )



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
        10

    }

# ---------------- Draw Question ----------------

def draw_question(
    screen,
    font,
    question
):

    option_rects = []



    # سوال

    question_text = font.render(
        question["question"],
        True,
        (255,165,0)
    )


    question_rect = question_text.get_rect(
        center=(600,200)
    )


    screen.blit(
        question_text,
        question_rect
    )



    positions = [

        (400,400),

        (700,400)

    ]



    for i, option in enumerate(
        question["options"]
    ):


        rect = pygame.Rect(

            positions[i][0],

            positions[i][1],

            200,

            100

        )



        pygame.draw.rect(

            screen,

            (255,255,255),

            rect,

            border_radius=20

        )



        option_text = font.render(

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



        option_rects.append(

            (
                rect,
                option
            )

        )



    return option_rects







# ---------------- Game ----------------


pygame.init()



screen = pygame.display.set_mode(

    (1200,700)

)



font = pygame.font.SysFont(

    None,

    50

)



question_number = 1



current_question = generate_true_false_question(

    question_number

)



start_time = pygame.time.get_ticks()



correct_count = 0

wrong_count = 0



running = True



while running:


    screen.fill(

        (50,50,50)

    )



    option_rects = draw_question(

        screen,

        font,

        current_question

    )



    for event in pygame.event.get():



        if event.type == pygame.QUIT:

            running = False



        if event.type == pygame.MOUSEBUTTONDOWN:


            mouse_pos = pygame.mouse.get_pos()



            for rect, option in option_rects:



                if rect.collidepoint(mouse_pos):



                    if option == current_question["answer"]:

                        correct_count += 1


                    else:

                        wrong_count += 1



                    question_number += 1



                    current_question = generate_true_false_question(

                        question_number

                    )



                    start_time = pygame.time.get_ticks()





    # ---------------- Timer ----------------


    elapsed = (

        pygame.time.get_ticks()

        -

        start_time

    ) / 1000



    remaining_time = max(

        0,

        current_question["time"] - int(elapsed)

    )



    timer_text = font.render(

        f"Time: {remaining_time}",

        True,

        (255,255,0)

    )



    screen.blit(

        timer_text,

        (900,50)

    )



    # پایان بازی اگر زمان تمام شود

    if elapsed >= current_question["time"]:


        wrong_count += 1

        running = False





    # ---------------- Score ----------------


    correct_text = font.render(

        f"Correct: {correct_count}",

        True,

        (0,255,0)

    )


    wrong_text = font.render(

        f"Wrong: {wrong_count}",

        True,

        (255,0,0)

    )



    screen.blit(

        correct_text,

        (50,50)

    )



    screen.blit(

        wrong_text,

        (300,50)

    )



    pygame.display.update()



pygame.quit()
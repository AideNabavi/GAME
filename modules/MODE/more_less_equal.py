import random
import pygame



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







# ---------------- Draw Question ----------------

def draw_question(
    screen,
    font,
    question
):


    option_rects = []



    text = font.render(
        question["question"],
        True,
        (255,165,0)
    )



    text_rect = text.get_rect(
        center=(600,200)
    )



    screen.blit(
        text,
        text_rect
    )




    positions = [

        (200,450),
        (500,450),
        (800,450)

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

            option,

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



pygame.display.set_caption(

    "Compare Math"

)



font = pygame.font.SysFont(

    None,

    60

)



question_number = 1



current_question = generate_compare_question(

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



                if rect.collidepoint(
                    mouse_pos
                ):



                    if option == current_question["answer"]:

                        correct_count += 1


                    else:

                        wrong_count += 1



                    question_number += 1



                    current_question = generate_compare_question(

                        question_number

                    )



                    start_time = pygame.time.get_ticks()






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



    timer = font.render(

        f"Time: {remaining}",

        True,

        (255,255,0)

    )



    screen.blit(

        timer,

        (900,50)

    )




    if elapsed >= current_question["time"]:

        wrong_count += 1

        question_number += 1


        current_question = generate_compare_question(

            question_number

        )


        start_time = pygame.time.get_ticks()





    correct = font.render(

        f"Correct: {correct_count}",

        True,

        (0,255,0)

    )


    wrong = font.render(

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



    pygame.display.update()



pygame.quit()
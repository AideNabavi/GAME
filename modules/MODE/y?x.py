import random
import pygame



# ---------------- Time ----------------

def get_question_time(question_number):

    current_time = 10 - ((question_number - 1) // 10)

    return max(
        5,
        current_time
    )



# ---------------- Generate Question ----------------

def generate_operator_question(
    ceill
):

    while True:

        operators = [
            "+",
            "-",
            "*",
            "/"
        ]


        operator = random.choice(
            operators
        )


        x = random.randint(
            1,
            ceill
        )

        y = random.randint(
            1,
            ceill
        )



        if operator == "+":

            result = x + y



        elif operator == "-":

            if x < y:

                x, y = y, x


            result = x - y



        elif operator == "*":

            result = x * y



        elif operator == "/":

            if y == 0:

                continue


            if x < y:

                x, y = y, x


            result = x / y


            if result.is_integer():

                result = int(result)

            else:

                result = round(
                    result,
                    2
                )



        if result <= ceill:

            break



    return {

        "question": f"{x} ? {y} = {result}",

        "answer": operator,

        "options": [
            "+",
            "-",
            "*",
            "/"
        ]

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

        (200,400),
        (450,400),
        (700,400),
        (950,400)

    ]



    for i, option in enumerate(question["options"]):


        rect = pygame.Rect(
            positions[i][0],
            positions[i][1],
            150,
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


font = pygame.font.SysFont(
    None,
    50
)



ceill = 100



question_number = 1



current_question = generate_operator_question(
    ceill
)



current_question["time"] = get_question_time(
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



                    # سوال بعدی

                    question_number += 1



                    current_question = generate_operator_question(
                        ceill
                    )



                    current_question["time"] = get_question_time(
                        question_number
                    )



                    start_time = pygame.time.get_ticks()





    # -------- Timer --------


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

    if elapsed >= current_question["time"]:

    # وقتی بازی تموم شد 
        wrong_count += 1

        running = False



    # -------- Score --------


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
        (350,50)
    )



    pygame.display.update()



pygame.quit()
import random
import pygame



pygame.init()



# ---------------- Settings ----------------

WIDTH = 1200
HEIGHT = 700


screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)


pygame.display.set_caption(
    "True False Math"
)



font = pygame.font.SysFont(
    None,
    55
)





# ---------------- Time ----------------

def get_question_time():

    return 3




# ---------------- Ceiling ----------------

def get_answer_ceill():

    return 100



def generate_true_false_question():


    ceill = 100


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

            result = x + y



        elif operator == "-":

            result = x - y



        elif operator == "*":

            result = x * y




        # نتیجه حتما بین 0 تا 100 باشد

        if 0 <= result <= ceill:

            break




    is_true = random.choice(

        [

            True,

            False

        ]

    )



    if is_true:


        shown_result = result



    else:


        while True:


            shown_result = random.randint(

                0,

                ceill

            )


            if shown_result != result:

                break





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

        3

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

        center=(WIDTH//2,150)

    )


    screen.blit(

        text,

        text_rect

    )





    positions = [

        (300,400),

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


current_question = generate_true_false_question()



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




                    current_question = generate_true_false_question()



                    start_time = pygame.time.get_ticks()








    # ---------------- Timer ----------------


    elapsed = (

        pygame.time.get_ticks()

        -

        start_time

    ) / 1000





    remaining_time = max(

        0,

        current_question["time"]

        -

        int(elapsed)

    )





    timer_text = font.render(

        f"Time: {remaining_time}",

        True,

        (255,255,0)

    )



    screen.blit(

        timer_text,

        (950,50)

    )





    # زمان تمام شد

    if elapsed >= current_question["time"]:



        wrong_count += 1



        current_question = generate_true_false_question()



        start_time = pygame.time.get_ticks()





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
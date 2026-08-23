import random
import pygame


def generate_answers(answer):

    options = [answer]

    while len(options) < 4:

        wrong = answer + random.randint(-10, 10)

        if wrong not in options:

            options.append(wrong)


    random.shuffle(options)

    return options



def generate_10_questions(
    ceill,
    operator,
    time_limit
):

    questions = []


    while len(questions) < 10:

        x = random.randint(1, ceill)
        y = random.randint(1, ceill)


        if operator == "+":

            answer = x + y


        elif operator == "-":

            if x < y:
                x, y = y, x

            answer = x - y


        elif operator == "*":

            answer = x * y


        elif operator == "/":

            if x < y:
                x, y = y, x

            answer = round(x / y, 2)


        if answer > ceill:
            continue



        questions.append({

            "question": f"{x} {operator} {y} = ?",

            "answer": answer,

            "options": generate_answers(answer),

            "time": time_limit

        })


    return questions






def draw_question(
    screen,
    font,
    question
):

    answer_rects = []


    # سوال
    text = font.render(
        question["question"],
        True,
        (255,165,0)
    )

    rect = text.get_rect(
        center=(500,200)
    )

    screen.blit(text, rect)



    positions = [

        (250,400),
        (500,400),
        (750,400),
        (1000,400)

    ]


    for i, option in enumerate(question["options"]):

        box = pygame.Rect(
            positions[i][0],
            positions[i][1],
            150,
            100
        )


        pygame.draw.rect(
            screen,
            (255,255,255),
            box,
            border_radius=20
        )


        answer_text = font.render(
            str(option),
            True,
            (0,0,0)
        )


        answer_rect = answer_text.get_rect(
            center=box.center
        )


        screen.blit(
            answer_text,
            answer_rect
        )


        answer_rects.append(
            (box, option)
        )


    return answer_rects
















        
correct_count = 0
wrong_count = 0



if __name__ == "__main__":

    pygame.init()

    screen = pygame.display.set_mode((1200,700))

    font = pygame.font.SysFont(None,50)


    questions = generate_10_questions(
        100,
        "+",
        5
    )


    index = 0

    current_question = questions[index]


    start_time = pygame.time.get_ticks()


    correct_count = 0
    wrong_count = 0


    running = True


    while running:

        screen.fill((50,50,50))


        answer_rects = draw_question(
            screen,
            font,
            current_question
        )


        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                running = False


            if event.type == pygame.MOUSEBUTTONDOWN:

                mouse_pos = pygame.mouse.get_pos()


                for rect, option in answer_rects:

                    if rect.collidepoint(mouse_pos):

                        if option == current_question["answer"]:

                            correct_count += 1

                        else:

                            wrong_count += 1


                        index += 1

                        current_question = questions[index]

                        start_time = pygame.time.get_ticks()



        elapsed = (
            pygame.time.get_ticks()
            -
            start_time
        ) / 1000


        if elapsed >= current_question["time"]:

            wrong_count += 1

            index += 1

            current_question = questions[index]

            start_time = pygame.time.get_ticks()



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







# # تولید سوال برای فصل ۵

# def generate_random_questions(
#     ceill,
#     question_count,
#     time_limit
# ):

#     operators = [
#         "+",
#         "-",
#         "*",
#         "/"
#     ]


#     questions = []


#     while len(questions) < question_count:


#         operator = random.choice(
#             operators
#         )


#         x = random.randint(
#             1,
#             ceill
#         )

#         y = random.randint(
#             1,
#             ceill
#         )


#         if operator == "+":

#             result = x + y



#         elif operator == "-":

#             if x < y:
#                 x, y = y, x

#             result = x - y



#         elif operator == "*":

#             result = x * y



#         elif operator == "/":

#             if y == 0:
#                 continue

#             if x < y:
#                 x, y = y, x

#             result = x / y

#             if result.is_integer():
#                 result = int(result)
#             else:
#                 result = round(result, 2)



#         if result > ceill:

#             continue



#         questions.append(
#             {
#                 "question": f"{x} {operator} {y} = ?",
#                 "answer": result,
#                 "time": time_limit
#             }
#         )


#     return questions
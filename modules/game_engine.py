import random
import pygame

from modules.setting import draw_text_stroke
from modules.ACCOUNT.player_profile import draw_profile_circle


# ---------------- Generate Answers ----------------

def generate_answers(result):

    answers = []

    answers.append(result)

    while len(answers) < 4:

        wrong = result + random.randint(-10, 10)

        if wrong != result and wrong not in answers:

            answers.append(wrong)

    random.shuffle(answers)

    return answers



# ---------------- Generate Question ----------------
def generate_question(ceill, operator):

    if not operator:
        operator = "+"

    ceill = int(ceill)

    x = random.randint(1, ceill)
    y = random.randint(1, ceill)

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
            y = 1

        if x < y:
            x, y = y, x

        result = x / y

        if result.is_integer():
            result = int(result)
        else:
            result = round(result, 2)

    else:
        raise ValueError(f"Invalid operator: {operator!r}")

    question_text = f"{x} {operator} {y} = ?"

    return question_text, result
# ---------------- Game Engine ----------------

def run_game(

    screen,
    fonts,

    current_width,
    current_height,


    player_name,
    selected_profile,
    profile_images,


    ceill,
    operator,
    time_limit,


    question_started,
    question_text,
    question_start_time,
    remaining_time,


    result,
    score,


    answers,
    answer_rects,
    answer_selected

):


    # ---------------- New Question ----------------
    if not question_started:


        question_text, result = generate_question(
            ceill,
            operator
        )


        answers.clear()

        answers.extend(
            generate_answers(result)
        )


        answer_rects.clear()


        question_start_time = pygame.time.get_ticks()


        question_started = True


        remaining_time = time_limit





    # ---------------- Draw Question ----------------


    question_surface = fonts["main"].render(
        question_text,
        True,
        (255,165,0)
    )


    question_stroke = fonts["main"].render(
        question_text,
        True,
        (0,0,0)
    )


    question_rect = question_surface.get_rect(

        center=(

            current_width//2,

            current_height//2 - 60

        )

    )


    draw_text_stroke(
        screen,
        question_stroke,
        question_rect.topleft
    )


    screen.blit(
        question_surface,
        question_rect
    )






    # ---------------- Draw Answers ----------------
    mouse_pos = pygame.mouse.get_pos()

    positions = [

        (current_width//2 - 500, 470),

        (current_width//2 - 250, 470),

        (current_width//2 - 0, 470),

        (current_width//2 + 250, 470)

    ]



    for i, answer in enumerate(answers):

        base_rect = pygame.Rect(
            positions[i][0],
            positions[i][1],
            170,
            120
        )


        rect = base_rect.copy()


        if rect.collidepoint(mouse_pos):

            rect.inflate_ip(
                20,
                20
            )

            rect.center = base_rect.center


        # Stroke
        pygame.draw.rect(
            screen,
            (0,0,0),
            rect.inflate(8,8),
            border_radius=35
        )


        # Main box
        pygame.draw.rect(
            screen,
            (255,255,255),
            rect,
            border_radius=30
        )


        text = fonts["answer"].render(

            str(answer),

            True,

            (255,165,0)

        )


        text_rect = text.get_rect(

            center=rect.center

        )


        screen.blit(

            text,

            text_rect

        )


        answer_rects[i] = (

            rect,

            answer

        )







    # ---------------- Check Answer ----------------


    if answer_selected is not None:


        if answer_selected == result:


            score += 1


            question_started = False


        else:


            score -= 1



        answer_selected = None







    # ---------------- Timer ----------------


    elapsed = (

        pygame.time.get_ticks()

        -

        question_start_time

    ) / 1000



    remaining_time = max(

        0,

        time_limit - int(elapsed)

    )




    # ---------------- Time Over ----------------


    if elapsed >= time_limit:


        score -= 1


        question_started = False






    # ---------------- Player Name ----------------


    player_text = fonts["name"].render(

        player_name,

        True,

        (255,220,0)

    )


    player_rect = player_text.get_rect(

        topleft=(20,20)

    )


    player_stroke = fonts["name"].render(

        player_name,

        True,

        (0,0,0)

    )


    draw_text_stroke(

        screen,

        player_stroke,

        player_rect.topleft

    )


    screen.blit(

        player_text,

        player_rect

    )





    # ---------------- Profile ----------------


    if selected_profile is not None:


        selected_image = profile_images[selected_profile]


        draw_profile_circle(

            screen,

            selected_image,

            (

                player_rect.right + 45,

                player_rect.centery

            ),

            50

        )





    return (

        question_started,

        question_text,

        question_start_time,

        remaining_time,

        result,

        score,

        answers,

        answer_rects,

        answer_selected

    )
    
    
    
    
    
    
    
    

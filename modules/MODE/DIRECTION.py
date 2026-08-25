import pygame
import random
import time
from modules.font import fonts

# pygame.init()


# WIDTH = 900
# HEIGHT = 500

# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Focus Direction Test")


# clock = pygame.time.Clock()


# font = pygame.font.Font(None, 70)
# small_font = pygame.font.Font(None, 40)



WHITE = (255,255,255)
BG = (30,30,30)


# به جای این عکس بیاد چهار تا سمت رو نشون بده 
directions = [
    "LEFT",
    "RIGHT",
    "UP",
    "DOWN"
]


keys = {

    pygame.K_LEFT: "LEFT",
    pygame.K_RIGHT: "RIGHT",
    pygame.K_UP: "UP",
    pygame.K_DOWN: "DOWN"

}



score = 0
correct = 0
wrong = 0



game_time = 60

start_time = time.time()


items = []

answer = None



def new_round_DIRECTION():

    global items
    global answer


    items = []


    same = random.choice(
        [True, False]
    )


    main = random.choice(
        directions
    )


    if same:


        for i in range(5):

            items.append(main)


        answer = main



    else:


        different = random.choice(
            [
                x for x in directions
                if x != main
            ]
        )


        position = random.randint(
            0,4
        )


        for i in range(5):

            if i == position:

                items.append(
                    different
                )

            else:

                items.append(
                    main
                )


        answer = different








finished = False



def DIRECTION_(screen):



    global finished
    global items
    global game_time
    global score
    global wrong
    global correct
    
    elapsed = time.time() - start_time


    remaining = int(game_time - elapsed)



    if remaining <= 0:

        finished = True





    if not finished:


        for i,item in enumerate(items):


            text = fonts["heart"].render(

                item,

                True,

                WHITE

            )


            screen.blit(

                text,

                (100+i*160,220)

            )


    else:


        text = fonts["heart"].render(
            "FINISHED",
            True,
            WHITE
        )

        screen.blit(
            text,
            (330,100)
        )


        result = fonts["heart"].render(

            f"Score {score}  Correct {correct}  Wrong {wrong}",

            True,

            WHITE

        )


        screen.blit(
            result,
            (180,220)
        )




    info = fonts["heart"].render(

        f"Time: {max(0,remaining)}   Score: {score}",

        True,

        WHITE

    )


    screen.blit(
        info,
        (20,20)
    )



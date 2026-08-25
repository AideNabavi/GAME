import pygame
import random
import time
from modules.font import fonts

# pygame.init()


# WIDTH = 900
# HEIGHT = 600


# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Reaction Focus Test")


# clock = pygame.time.Clock()


# font = pygame.font.Font(None, 45)



# رنگ ها


YELLOW = (255,220,0)

RED = (255,50,50)

WHITE = (255,255,255)



# --------------------------
# ساخت شکل ها
# --------------------------

shapes = []


shape_types = [
    "circle",
    "square",
    "diamond",
    "rect"
]

















def create_shapes():


    global shapes


    shapes.clear()



    count = random.randint(1,3)


    used = []



    for i in range(count):


        shape = random.choice(shape_types)



        x = random.randint(80,820)

        y = random.randint(120,500)



        obj = {

            "type": shape,

            "x": x,

            "y": y,

            "color": YELLOW,

            "size": random.randint(35,55),

            "rect": None

        }



        shapes.append(obj)



































# --------------------------
# رسم شکل
# --------------------------

def draw_shape(obj,screen):


    x = obj["x"]
    y = obj["y"]
    size = obj["size"]


    color = obj["color"]



    if obj["type"] == "circle":


        pygame.draw.circle(
            screen,
            color,
            (x,y),
            size
        )


        obj["rect"] = pygame.Rect(
            x-size,
            y-size,
            size*2,
            size*2
        )




    elif obj["type"] == "square":


        rect = pygame.Rect(
            x-size,
            y-size,
            size*2,
            size*2
        )


        pygame.draw.rect(
            screen,
            color,
            rect
        )


        obj["rect"] = rect




    elif obj["type"] == "diamond":


        points = [

            (x,y-size),
            (x+size,y),
            (x,y+size),
            (x-size,y)

        ]


        pygame.draw.polygon(
            screen,
            color,
            points
        )


        obj["rect"] = pygame.Rect(
            x-size,
            y-size,
            size*2,
            size*2
        )




    elif obj["type"] == "rect":


        rect = pygame.Rect(

            x-size*2,
            y-size,

            size*4,
            size*2

        )


        pygame.draw.rect(
            screen,
            color,
            rect
        )


        obj["rect"] = rect







































# --------------------------
# شروع بازی
# --------------------------

def reset_game_ACTION():


    global state
    global change_time
    global click_start
    global result



    create_shapes()



    state = "waiting"


    change_time = (
        time.time()
        +
        random.uniform(2,5)
    )


    click_start = 0


    result = ""


















def ACTION_(screen):


    global click_start
    global state





    # تغییر رنگ

    if state == "waiting":


        if time.time() >= change_time:


            for s in shapes:

                s["color"] = RED



            click_start = time.time()


            state = "ready"







    # رسم شکل ها

    for s in shapes:

        draw_shape(s,screen)




    # متن

    if state == "waiting":


        txt = fonts["heart"].render(
            "Wait...",
            True,
            WHITE
        )


        screen.blit(
            txt,
            (380,40)
        )




    if result:


        txt = fonts["heart"].render(
            result,
            True,
            WHITE
        )


        screen.blit(
            txt,
            (380,40)
        )



    info = fonts["heart"].render(
        "Press R Restart",
        True,
        WHITE
    )


    screen.blit(
        info,
        (20,20)
    )




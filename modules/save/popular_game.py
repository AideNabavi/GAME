import pygame
import json
import os




POPULAR_GAMES_FILE = "./modules/save/popular_game.json"


popular_games = {
    "ACTION": 0,
    "DETECT": 0,
    "DETECT_PRO": 0,
    "DIRECTION": 0,
    "FAST": 0,
    "FAST_ADD_SUB": 0,
    "FIND_NUMBER": 0,
    "FIND_OPERATOR": 0,
    "FOLLOW_THAT": 0,
    "HARD": 0,
    "HOW_MANY": 0,
    "IMAGE_SELECT": 0,
    "MATH_GO": 0,
    "MEMORY_GO": 0,
    "MEMORY": 0,
    "MIRROR": 0,
    "MOVE_ARROW": 0,
    "MORE_LESS_EQUAL": 0,
    "SIX_60S": 0,
    "TRUE_FALSE": 0,
    "REPEAT_AFTER_ME": 0,
    "SHAPE_COLOR_NAME": 0,
}


# ============================================================
# LOAD POPULAR GAMES
# ============================================================

# load_popular_games

def load_popular_games():

    global popular_games

    if os.path.exists(POPULAR_GAMES_FILE):

        with open(POPULAR_GAMES_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        # فقط ID هایی که در سیستم بازی تعریف شده‌اند
        for game_id in popular_games:

            if game_id in data:
                popular_games[game_id] = data[game_id]


# ============================================================
# ADD POPULAR GAME
# ============================================================
# هر دفعه برای هر بازی در ایونت هندلر یکی اضافه میکنه 
def add_popular_game(game_id):

    if not os.path.exists(POPULAR_GAMES_FILE):

        data = popular_games.copy()

    else:

        with open(
            POPULAR_GAMES_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

    if game_id in data:
        data[game_id] += 1
    else:
        data[game_id] = 1

    with open(
        POPULAR_GAMES_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4
        )

    # دوباره اطلاعات جدید را وارد RAM کن
    load_popular_games()
    
    
    
# ============================================================
# GET TOP 3 POPULAR GAMES
# ============================================================
# این رو باید در منو بگیرم همون داشبورد رد ایونت هندلر 
def get_top_3_popular_games():

    top_3 = sorted(
        popular_games.items(),
        key=lambda x: x[1],
        reverse=True
    )[:3]

    return top_3






























POPULAR_IMAGES = {}

def load_popular_images(image_folder):

    global POPULAR_IMAGES

    POPULAR_IMAGES.clear()

    top_3 = sorted(
        popular_games.items(),
        key=lambda item: item[1],
        reverse=True
    )[:3]

    print("TOP 3 =", top_3)

    for game_id, count in top_3:

        image_path = os.path.join(
            image_folder,
            game_id + ".png"
        )

        print("LOADING:", game_id)
        print("PATH:", image_path)

        if os.path.isfile(image_path):

            image = pygame.image.load(
                image_path
            ).convert_alpha()

            image = pygame.transform.smoothscale(
                image,
                (300, 300)
            )

            POPULAR_IMAGES[game_id] = image
            
            
            
            
            
            
            
            
            


def get_popular_game_images(top_3):

    selected_images = []

    for game_id, count in top_3[:3]:

        image = POPULAR_IMAGES.get(game_id)

        if image is not None:
            selected_images.append(image)

    return selected_images



























import random
import pygame


image_paths = [
    "./asset/image/MODE/1.png",
    "./asset/image/MODE/2.png",
    "./asset/image/MODE/3.png",
    "./asset/image/MODE/4.png",
    "./asset/image/MODE/5.png",
    "./asset/image/MODE/6.png",
    "./asset/image/MODE/7.png",
    "./asset/image/MODE/8.png",
    "./asset/image/MODE/9.png",
    "./asset/image/MODE/10.png",
    "./asset/image/MODE/11.png",
    "./asset/image/MODE/12.png",
    "./asset/image/MODE/13.png",
    "./asset/image/MODE/14.png",
    "./asset/image/MODE/15.png",
    "./asset/image/MODE/16.png",
]


# ============================================================
# LOAD + CONVERT ALPHA + SCALE
# فقط یک بار انجام می‌شود
# ============================================================

images = [
    pygame.transform.smoothscale(
        pygame.image.load(path).convert_alpha(),
        (300, 300)
    )
    for path in image_paths
]


# ============================================================
# انتخاب 3 عکس رندوم
# فقط هنگام شروع بازی اجرا کن
# ============================================================

def choose_three_random_images():

    return random.sample(images, 3)


# ============================================================
# رسم 3 عکس
# این تابع بسیار سبک است
# ============================================================

def draw_three_images(
    screen,
    selected_images,
    gap=160
):

    image_width = 200
    image_height = 200

    total_width = (
        image_width * 3
        + gap * 2
    )

    start_x = (
        screen.get_width()
        - total_width
    ) // 2 - 50

    y = (
        screen.get_height()
        - image_height
    ) // 2 + 415

    rects = []

    for i, image in enumerate(selected_images):

        x = start_x + i * (
            image_width + gap
        )

        rect = image.get_rect(
            topleft=(x, y)
        )

        screen.blit(
            image,
            rect
        )

        rects.append(rect)

    return rects
import json
import os


import random
import pygame


image_paths = [
    "./asset/image/MODE/2.png",
    "./asset/image/MODE/2.png",
    "./asset/image/MODE/2.png",

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
def draw_three_images_recent_game(
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
    ) // 2

    y = screen.get_height() // 2

    rects = []

    for i, image in enumerate(selected_images):

        x = (
            start_x
            + image_width // 2
            + i * (image_width + gap)
        )

        rect = image.get_rect(
            center=(x, y)
        )

        screen.blit(
            image,
            rect
        )

        rects.append(rect)

    return rects











import json
import os
import pygame


# ============================================================
# SETTINGS
# ============================================================

RECENT_GAMES_FILE = "./modules/save/recent_game.json"

recent_games = []

RECENT_IMAGES = {}


# ============================================================
# LOAD RECENT GAMES
# قبل از حلقه while اجرا شود
# ============================================================

def load_recent_games():

    global recent_games

    if os.path.exists(RECENT_GAMES_FILE):

        with open(
            RECENT_GAMES_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        recent_games = data.get(
            "recent_game",
            []
        )[:3]

    else:

        recent_games = []


# ============================================================
# ADD RECENT GAME
# در Event Handler هر بازی اجرا شود
# ============================================================

def add_recent_game(game_id):

    global recent_games

    # اگر قبلاً در لیست هست، حذفش کن
    if game_id in recent_games:
        recent_games.remove(game_id)

    # بازی جدید را اول لیست قرار بده
    recent_games.insert(
        0,
        game_id
    )

    # فقط 3 بازی آخر
    recent_games = recent_games[:3]

    # ذخیره پوشه در صورت نیاز
    folder = os.path.dirname(
        RECENT_GAMES_FILE
    )

    if folder:
        os.makedirs(
            folder,
            exist_ok=True
        )

    # ذخیره در JSON
    with open(
        RECENT_GAMES_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            {
                "recent_game": recent_games
            },
            file,
            ensure_ascii=False,
            indent=4
        )


# ============================================================
# GET RECENT GAMES
# ============================================================

def get_recent_games():

    return recent_games


# ============================================================
# LOAD RECENT IMAGES
# فقط یک بار هنگام شروع / Loading
# ============================================================

def load_recent_images(image_folder):

    global RECENT_IMAGES

    RECENT_IMAGES.clear()

    # print("RECENT GAMES =", recent_games)

    for game_id in recent_games:

        image_path = os.path.join(
            image_folder,
            game_id + ".png"
        )

        # print("LOADING:", game_id)
        # print("PATH:", image_path)

        if not os.path.isfile(image_path):

            print(
                "NOT FOUND:",
                image_path
            )

            continue

        image = pygame.image.load(
            image_path
        ).convert_alpha()

        image = pygame.transform.smoothscale(
            image,
            (170, 170)
        )

        RECENT_IMAGES[game_id] = image


# ============================================================
# GET RECENT GAME IMAGES
# ترتیب دقیقاً مثل recent_games است
# ============================================================

def get_recent_game_images():

    selected_images = []

    for game_id in recent_games:

        image = RECENT_IMAGES.get(
            game_id
        )

        if image is not None:

            selected_images.append(
                image
            )

    return selected_images


# ============================================================
# DRAW 3 RECENT GAMES
# ============================================================
def draw_three_images_recent_game(
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
    ) // 2 + 100

    rects = []

    for i, image in enumerate(
        selected_images
    ):

        x = start_x + i * (
            image_width + gap
        )

        rect = image.get_rect(
            center=(
                x + image_width // 2,
                y + image_height // 2
            )
        )

        screen.blit(
            image,
            rect
        )

        rects.append(rect)

    return rects
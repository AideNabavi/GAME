import pygame
import random
import os
import time

from modules.font import fonts


# ============================================================
# COLORS
# ============================================================

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)


# ============================================================
# GAME SETTINGS
# ============================================================

GAME_TIME = 3.0

IMAGE_SIZE = 450

ZOOM_DURATION = 0.5

IMAGE_GAP = 500


# ============================================================
# GAME STATE
# ============================================================

first_round = True

score = 0

lives = 3

game_over = False


# ============================================================
# IMAGE FOLDER
# ============================================================

IMAGE_FOLDER = "/Users/mac/Desktop/app/asset/image/MODE/memory_detect"


# ============================================================
# GET IMAGE FILES
# ============================================================

image_files = []

for file in os.listdir(IMAGE_FOLDER):

    if file.lower().endswith(
        (".png", ".jpg", ".jpeg")
    ):

        image_files.append(file)


if len(image_files) < 2:

    raise Exception(
        "Need at least 2 images"
    )


# ============================================================
# LOAD IMAGE
# ============================================================

def load_image(filename):

    img = pygame.image.load(
        os.path.join(
            IMAGE_FOLDER,
            filename
        )
    ).convert_alpha()


    img = pygame.transform.smoothscale(
        img,
        (IMAGE_SIZE, IMAGE_SIZE)
    )


    return img


# ============================================================
# CACHE ALL IMAGES
# ============================================================

images = {}

for file in image_files:

    images[file] = load_image(file)


# ============================================================
# GAME IMAGES
# ============================================================

old_image = random.choice(
    image_files
)


new_image = random.choice(
    [
        x for x in image_files
        if x != old_image
    ]
)


left_image = old_image

right_image = new_image


# ============================================================
# TIMER
# ============================================================

start_time = time.time()

animation_start = time.time()


# ============================================================
# IMAGE RECTANGLES
# ============================================================

left_rect = pygame.Rect(
    0,
    0,
    IMAGE_SIZE,
    IMAGE_SIZE
)


right_rect = pygame.Rect(
    0,
    0,
    IMAGE_SIZE,
    IMAGE_SIZE
)


# ============================================================
# GET NEW IMAGE
# ============================================================

def get_new_image(old):

    available = [
        x for x in image_files
        if x != old
    ]

    return random.choice(
        available
    )


# ============================================================
# UPDATE IMAGE RECTS
# ============================================================

def update_image_rects(WIDTH, HEIGHT):

    global left_rect
    global right_rect

    left_center_x = WIDTH // 2 - IMAGE_GAP // 2

    right_center_x = WIDTH // 2 + IMAGE_GAP // 2

    center_y = HEIGHT // 2 + 50


    left_rect = pygame.Rect(
        0,
        0,
        IMAGE_SIZE,
        IMAGE_SIZE
    )

    left_rect.center = (
        left_center_x,
        center_y
    )


    right_rect = pygame.Rect(
        0,
        0,
        IMAGE_SIZE,
        IMAGE_SIZE
    )

    right_rect.center = (
        right_center_x,
        center_y
    )


# ============================================================
# DRAW ZOOM IMAGE
# ============================================================
def draw_image(image, x, y, screen):

    rect = image.get_rect(
        center=(x, y)
    )

    screen.blit(
        image,
        rect
    )

# ============================================================
# RESTART GAME
# ============================================================

def restart_game():

    global first_round

    global left_image
    global right_image

    global old_image
    global new_image

    global score

    global lives

    global game_over

    global start_time

    global animation_start


    # ========================================================
    # RESET STATE
    # ========================================================

    first_round = True

    score = 0

    lives = 3

    game_over = False


    # ========================================================
    # CREATE FIRST ROUND
    # ========================================================

    old_image = random.choice(
        image_files
    )


    new_image = get_new_image(
        old_image
    )


    left_image = old_image

    right_image = new_image


    # ========================================================
    # RESET TIMER
    # ========================================================

    start_time = time.time()

    animation_start = time.time()


# ============================================================
# START GAME
# ============================================================



# ============================================================
# MAIN DRAW FUNCTION
# ============================================================

def DETECT_(screen, WIDTH, HEIGHT):

    global first_round

    global left_image
    global right_image

    global start_time
    global lives

    global animation_start

    global game_over

    global new_image

    global score


    # ========================================================
    # UPDATE IMAGE RECTANGLES
    # ========================================================

    update_image_rects(
        WIDTH,
        HEIGHT
    )


    # ========================================================
    # SCORE
    # ========================================================

    score_text = fonts["heart"].render(
        "Score: " + str(score),
        True,
        BLACK
    )


    screen.blit(
        score_text,
        (20, 20)
    )


    # ========================================================
    # LIVES
    # ========================================================

    life_text = fonts["heart"].render(
        "Lives: " + str(lives),
        True,
        BLACK
    )


    screen.blit(
        life_text,
        (20, 60)
    )


    # ========================================================
    # GAME OVER
    # ========================================================

    if game_over:

        game_over_text = fonts["heart"].render(
            "GAME OVER",
            True,
            BLACK
        )


        game_over_rect = game_over_text.get_rect(
            center=(
                WIDTH // 2,
                HEIGHT // 2 - 50
            )
        )


        screen.blit(
            game_over_text,
            game_over_rect
        )


        score_text = fonts["heart"].render(
            "Score: " + str(score),
            True,
            BLACK
        )


        score_rect = score_text.get_rect(
            center=(
                WIDTH // 2,
                HEIGHT // 2 + 20
            )
        )


        screen.blit(
            score_text,
            score_rect
        )


        restart_text = fonts["heart"].render(
            "Press R to Restart",
            True,
            BLACK
        )


        restart_rect = restart_text.get_rect(
            center=(
                WIDTH // 2,
                HEIGHT // 2 + 90
            )
        )


        screen.blit(
            restart_text,
            restart_rect
        )


        return


    # ========================================================
    # TIMER
    # ========================================================

    elapsed = time.time() - start_time

    remaining = GAME_TIME - elapsed


    # ========================================================
    # TIME OUT
    # ========================================================

    if remaining <= 0:

        lives -= 1


        # ====================================================
        # GAME OVER
        # ====================================================

        if lives <= 0:

            lives = 0

            game_over = True

            return


        # ====================================================
        # CONTINUE
        # ====================================================

        start_time = time.time()

        animation_start = time.time()

        remaining = GAME_TIME


    # ========================================================
    # TIMER TEXT
    # ========================================================

    timer_text = fonts["heart"].render(
        "Time: " + str(
            round(
                max(0, remaining),
                1
            )
        ),
        True,
        BLACK
    )


    timer_rect = timer_text.get_rect(
        center=(
            WIDTH // 2,
            50
        )
    )


    screen.blit(
        timer_text,
        timer_rect
    )


    # ========================================================
    # FIRST ROUND INSTRUCTION
    # ========================================================

    if first_round:

        text = fonts["heart"].render(
            "Choose: " + new_image,
            True,
            BLACK
        )


        text_rect = text.get_rect(
            center=(
                WIDTH // 2,
                100
            )
        )


        screen.blit(
            text,
            text_rect
        )


    # ========================================================
    # LEFT IMAGE
    # ========================================================
    draw_image(
        images[left_image],
        WIDTH // 2 - 250,
        HEIGHT // 2 + 50,
        screen
    )

    draw_image(
        images[right_image],
        WIDTH // 2 + 250,
        HEIGHT // 2 + 50,
        screen
    )

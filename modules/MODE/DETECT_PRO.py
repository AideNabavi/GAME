import pygame
import random
import os
import sys
from modules.font import *
# pygame.init()

# =========================
# SETTINGS
# =========================

# WIDTH, HEIGHT = 1000, 800
# screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
# pygame.display.set_caption("REACTION GAME")

# clock = pygame.time.Clock()

ANIMAL_FOLDER = "./asset/image/MODE/AN_OB_NA/animal/"
OBJECT_FOLDER = "./asset/image/MODE/AN_OB_NA/object/"
NATURE_FOLDER = "./asset/image/MODE/AN_OB_NA/fruit/"

TIME_LIMIT = 2
MAX_LIVES = 3

# font_big = pygame.font.Font(None, 100)
# font_medium = pygame.font.Font(None, 50)
# font_small = pygame.font.Font(None, 35)

# =========================
# LOAD IMAGES
# =========================

images = {
    "Animal": [],
    "Object": [],
    "Fruit": []
}

folders = {
    "Animal": ANIMAL_FOLDER,
    "Object": OBJECT_FOLDER,
    "Fruit": NATURE_FOLDER
}

for category, folder in folders.items():

    if not os.path.exists(folder):
        print("Folder not found:", folder)
        continue

    for file in os.listdir(folder):

        if file.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):

            try:
                image = pygame.image.load(
                    folder + file
                ).convert_alpha()

                images[category].append(image)

            except pygame.error:
                print("Could not load:", folder + file)

if any(len(images[x]) == 0 for x in images):

    print("ERROR: Every folder needs at least one image.")

    pygame.quit()
    sys.exit()

# =========================
# VARIABLES
# =========================

score = 0
lives = MAX_LIVES

current_category = None
current_image = None

buttons = []
timer = TIME_LIMIT
round_start_time = 0
game_over = False

# =========================
# RESIZE IMAGE
# =========================

def resize_image(image, size):

    width, height = image.get_size()

    scale = min(
        size / width,
        size / height
    )

    new_size = (
        max(1, int(width * scale)),
        max(1, int(height * scale))
    )

    return pygame.transform.smoothscale(
        image,
        new_size
    )

# =========================
# NEW ROUND
# =========================

def new_round(WIDTH,HEIGHT):

    global current_category
    global current_image
    global buttons
    global timer
    global round_start_time
    current_category = random.choice(
        list(images.keys())
    )

    current_image = random.choice(
        images[current_category]
    )

    categories = list(images.keys())
    random.shuffle(categories)

    buttons = []

    button_width = 220
    button_height = 80
    gap = 30

    total_width = (
        button_width * 3 +
        gap * 2
    )

    start_x = (
        WIDTH - total_width
    ) // 2

    y = HEIGHT - 150

    for i, category in enumerate(categories):

        rect = pygame.Rect(
            start_x + i * (button_width + gap),
            y,
            button_width,
            button_height
        )

        buttons.append(
            (category, rect)
        )

    timer = TIME_LIMIT
    round_start_time = pygame.time.get_ticks()
# =========================
# RESET
# =========================

def reset_game(WIDTH,HEIGHT):

    global score
    global lives
    global game_over

    score = 0
    lives = MAX_LIVES
    game_over = False

    new_round(WIDTH,HEIGHT)

    # =====================
def DETECT_PRO_(screen,WIDTH,HEIGHT):
    global timer
    global lives
    global game_over
    global round_start_time
        # =====================
    # TIMER
    # =====================

    if not game_over:

        elapsed = (
            pygame.time.get_ticks() - round_start_time
        ) / 1000

        timer = TIME_LIMIT - elapsed

        if timer <= 0:

            lives -= 1

            if lives <= 0:
                game_over = True

            else:
                new_round(WIDTH, HEIGHT)
    # =====================
    # DRAW
    # =====================

    screen.fill((20, 20, 28))

    # =====================
    # GAME
    # =====================

    if not game_over:

        # Score
        screen.blit(
            fonts["date"].render(
                f"Score: {score}",
                True,
                "white"
            ),
            (30, 25)
        )

        # Lives
        screen.blit(
            fonts["date"].render(
                f"Lives: {lives}",
                True,
                "white"
            ),
            (30, 65)
        )

        # Timer
        timer_text = fonts["heart"].render(
            f"{max(0, timer):.1f}",
            True,
            "white"
        )

        screen.blit(
            timer_text,
            timer_text.get_rect(
                center=(WIDTH // 2, 70)
            )
        )

        # =================
        # IMAGE
        # =================

        image = resize_image(
            current_image,
            450
        )

        screen.blit(
            image,
            image.get_rect(
                center=(WIDTH // 2, 350)
            )
        )

        # =================
        # BUTTONS
        # =================

        mouse_pos = pygame.mouse.get_pos()

        for category, rect in buttons:

            if rect.collidepoint(mouse_pos):
                color = (80, 150, 230)
            else:
                color = (50, 90, 150)

            pygame.draw.rect(
                screen,
                color,
                rect,
                border_radius=15
            )

            text = fonts["heart"].render(
                category,
                True,
                "white"
            )

            screen.blit(
                text,
                text.get_rect(
                    center=rect.center
                )
            )

    # =====================
    # GAME OVER
    # =====================

    else:

        title = fonts["DAY"].render(
            "GAME OVER",
            True,
            (230, 70, 70)
        )

        screen.blit(
            title,
            title.get_rect(
                center=(WIDTH // 2, 280)
            )
        )

        score_text = fonts["heart"].render(
            f"Score: {score}",
            True,
            "white"
        )

        screen.blit(
            score_text,
            score_text.get_rect(
                center=(WIDTH // 2, 390)
            )
        )

        restart = fonts["heart"].render(
            "Press R to Restart",
            True,
            "white"
        )

        screen.blit(
            restart,
            restart.get_rect(
                center=(WIDTH // 2, 480)
            )
        )


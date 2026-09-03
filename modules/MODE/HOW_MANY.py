import pygame
import random
from modules.font import fonts
import os
import sys


# WIDTH, HEIGHT = 1000, 800
# screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
# pygame.display.set_caption("COUNT THE IMAGE")
# clock = pygame.time.Clock()

IMAGE_FOLDER = "./asset/image/droping/"

GRID_SIZE = 5
TOTAL_CELLS = 25
CELL_SIZE = 105
GAP = 8
GRID_X, GRID_Y = 220, 100

TARGET_TIME = 1.0
ANSWER_TIME = 5.0
MAX_LIVES = 3

# font_big = pygame.font.Font(None, 70)
# font_medium = pygame.font.Font(None, 42)
# font_small = pygame.font.Font(None, 32)

# =========================
# LOAD IMAGES
# =========================

images = []

for file in os.listdir(IMAGE_FOLDER):
    if file.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
        try:
            img = pygame.image.load(
                os.path.join(IMAGE_FOLDER, file)
            ).convert_alpha()
            images.append(img)
        except pygame.error:
            pass

if len(images) < 2:
    print("ERROR: At least 2 valid images are required.")
    pygame.quit()
    sys.exit()

# =========================
# VARIABLES
# =========================

score = 0
lives = MAX_LIVES
state = "target"
timer = TARGET_TIME
round_start_time = 0
target = None
grid = []
answer = 0
options = []

# =========================
# RESIZE
# =========================

def resize_image(img, size):
    w, h = img.get_size()
    scale = min(size / w, size / h)

    new_size = (
        max(1, int(w * scale)),
        max(1, int(h * scale))
    )

    return pygame.transform.smoothscale(img, new_size)

# =========================
# NEW ROUND
# =========================

def new_round():
    global target, grid, answer, options, state, timer, round_start_time
    target = random.choice(images)
    answer = random.randint(1, 10)

    grid = [target] * answer

    while len(grid) < TOTAL_CELLS:
        img = random.choice(images)

        if img is not target:
            grid.append(img)

    random.shuffle(grid)

    options = [answer]

    while len(options) < 4:
        n = random.randint(1, TOTAL_CELLS)

        if n not in options:
            options.append(n)

    random.shuffle(options)

    state = "target"
    timer = TARGET_TIME
    round_start_time = pygame.time.get_ticks()
# =========================
# RESET
# =========================

def reset_game():
    global score, lives

    score = 0
    lives = MAX_LIVES
    new_round()

# =========================
# OPTION RECT
# =========================

def get_option_rect(index,WIDTH):
    width = 130
    height = 60
    gap = 15

    total_width = width * 4 + gap * 3
    start_x = (WIDTH - total_width) // 2

    x = start_x + index * (width + gap)
    y = 665

    return pygame.Rect(x, y, width, height)

# =========================
# START
# =========================




# dt = clock.tick(60) / 1000

    # =====================
    # UPDATE
    # =====================
def HOW_MANY_(screen,WIDTH,HEIGHT):
    # global timer
    # global state
    # global lives
    global timer, state, lives,round_start_time
    elapsed = (pygame.time.get_ticks() - round_start_time) / 1000

    if state == "target":

        timer = TARGET_TIME - elapsed

        if timer <= 0:
            state = "game"
            timer = ANSWER_TIME
            round_start_time = pygame.time.get_ticks()

    elif state == "game":

        timer = ANSWER_TIME - elapsed

        if timer <= 0:

            lives -= 1

            if lives <= 0:
                state = "gameover"
            else:
                new_round()
    # =====================
    # DRAW
    # =====================

    screen.fill((25, 25, 32))

    # =====================
    # TARGET
    # =====================

    if state == "target":

        title = fonts["heart"].render(
            "MEMORIZE THIS IMAGE",
            True,
            "white"
        )

        screen.blit(
            title,
            title.get_rect(
                center=(WIDTH // 2, 70)
            )
        )

        img = resize_image(target, 300)

        screen.blit(
            img,
            img.get_rect(
                center=(WIDTH // 2, HEIGHT // 2)
            )
        )

        countdown = fonts["DAY"].render(
            f"{max(0, timer):.1f}",
            True,
            "white"
        )

        screen.blit(
            countdown,
            countdown.get_rect(
                center=(WIDTH // 2, 650)
            )
        )

    # =====================
    # GAME
    # =====================

    elif state == "game":

        question = fonts["heart"].render(
            "How many of this image are there?",
            True,
            "white"
        )

        screen.blit(
            question,
            question.get_rect(
                center=(WIDTH // 2, 45)
            )
        )

        # GRID
        for i, img in enumerate(grid):

            row = i // GRID_SIZE
            col = i % GRID_SIZE

            x = GRID_X + col * (CELL_SIZE + GAP)
            y = GRID_Y + row * (CELL_SIZE + GAP)

            cell = pygame.Rect(
                x,
                y,
                CELL_SIZE,
                CELL_SIZE
            )

            pygame.draw.rect(
                screen,
                (45, 45, 55),
                cell,
                border_radius=8
            )

            img2 = resize_image(
                img,
                CELL_SIZE - 12
            )

            screen.blit(
                img2,
                img2.get_rect(
                    center=cell.center
                )
            )

        # =================
        # FOUR OPTIONS
        # =================

        for i, option in enumerate(options):

            rect = get_option_rect(i,WIDTH)

            pygame.draw.rect(
                screen,
                (55, 110, 210),
                rect,
                border_radius=12
            )

            text = fonts["heart"].render(
                str(option),
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

    elif state == "gameover":

        gameover = fonts["DAY"].render(
            "GAME OVER",
            True,
            (220, 60, 60)
        )

        screen.blit(
            gameover,
            gameover.get_rect(
                center=(WIDTH // 2, 300)
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

        restart = fonts["DAY"].render(
            "Press R to Restart",
            True,
            "white"
        )

        screen.blit(
            restart,
            restart.get_rect(
                center=(WIDTH // 2, 470)
            )
        )

    # =====================
    # HUD
    # =====================

    if state != "gameover":

        screen.blit(
            fonts["date"].render(
                f"Score: {score}",
                True,
                "white"
            ),
            (20, 20)
        )

        screen.blit(
            fonts["date"].render(
                f"Lives: {lives}",
                True,
                "white"
            ),
            (20, 55)
        )

        screen.blit(
            fonts["date"].render(
                f"Time: {max(0, timer):.1f}",
                True,
                "white"
            ),
            (850, 20)
        )


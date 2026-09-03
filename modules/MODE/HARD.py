






import pygame
import random
import os
import sys
from modules.font import *
# pygame.init()

# WIDTH, HEIGHT = 1000, 800
# screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
# pygame.display.set_caption("MEMORY MATH")
# clock = pygame.time.Clock()

IMAGE_FOLDER = "./asset/image/MODE/memory_detect/"

TIME_SHOW = 1.0
ANSWER_TIME = 7.0
MAX_LIVES = 3

# font_big = pygame.font.Font(None, 100)
# font_medium = pygame.font.Font(None, 50)
# font_small = pygame.font.Font(None, 35)
# =========================
# LOAD IMAGES
# =========================

images = []

for file in os.listdir(IMAGE_FOLDER):
    if file.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
        try:
            images.append(
                pygame.image.load(
                    IMAGE_FOLDER + file
                ).convert_alpha()
            )
        except pygame.error:
            pass

if len(images) < 4:
    print("At least 4 images are required.")
    pygame.quit()
    sys.exit()

# =========================
# VARIABLES
# =========================

score = 0
lives = MAX_LIVES

phase = 0
timer = TIME_SHOW
round_start_time = 0
game_over = False

image1 = None
image2 = None

number1 = 0
number2 = 0
operator = "+"

answer = 0
options = []

# =========================
# RESIZE
# =========================

def resize_image(image, size):

    w, h = image.get_size()

    scale = min(
        size / w,
        size / h
    )

    return pygame.transform.smoothscale(
        image,
        (
            max(1, int(w * scale)),
            max(1, int(h * scale))
        )
    )

# =========================
# NEW ROUND
# =========================

def new_round():

    global image1, image2
    global number1, number2
    global operator, answer
    global options, phase, timer , round_start_time

    image1, image2 = random.sample(images, 2)

    number1 = random.randint(1, 20)
    number2 = random.randint(1, 100)

    operator = random.choice(["+", "-"])

    if operator == "+":
        answer = number1 + number2
    else:
        answer = number1 - number2

    # =====================
    # CORRECT OPTION
    # =====================

    options = [{
        "image1": image1,
        "image2": image2,
        "number1": number1,
        "number2": number2,
        "operator": operator
    }]

    # =====================
    # WRONG OPTIONS
    # =====================

    while len(options) < 4:

        wrong = {
            "image1": random.choice(images),
            "image2": random.choice(images),
            "number1": number1,
            "number2": number2,
            "operator": operator
        }

        # تغییر یکی از قسمت‌ها
        change = random.randint(0, 2)

        if change == 0:

            wrong["image1"] = random.choice(images)

        elif change == 1:

            wrong["image2"] = random.choice(images)

        else:

            wrong["number1"] = random.randint(1, 20)

        # جلوگیری از گزینه کاملاً درست
        if (
            wrong["image1"] is image1
            and wrong["image2"] is image2
            and wrong["number1"] == number1
            and wrong["number2"] == number2
            and wrong["operator"] == operator
        ):
            continue

        # جلوگیری از تکراری شدن گزینه
        duplicate = False

        for x in options:

            if (
                x["image1"] is wrong["image1"]
                and x["image2"] is wrong["image2"]
                and x["number1"] == wrong["number1"]
                and x["number2"] == wrong["number2"]
                and x["operator"] == wrong["operator"]
            ):
                duplicate = True
                break

        if not duplicate:
            options.append(wrong)

    random.shuffle(options)

    # شروع نمایش مرحله‌ای
    phase = 0
    timer = TIME_SHOW
    round_start_time = pygame.time.get_ticks()
# =========================
# RESET
# =========================

def reset_game():

    global score, lives, game_over

    score = 0
    lives = MAX_LIVES
    game_over = False

    new_round()

# =========================
# OPTION RECT
# =========================

def get_option_rect(index):

    width = 400
    height = 110

    gap_x = 30
    gap_y = 20

    x = 70 + (index % 2) * (width + gap_x)
    y = 520 + (index // 2) * (height + gap_y)

    return pygame.Rect(
        x,
        y,
        width,
        height
    )

# =========================
# START
# =========================

new_round()

# running = True

# =========================
# LOOP
# =========================

# while running:

#     dt = clock.tick(60) / 1000


def HARD_(screen,WIDTH,HEIGHT):

    global timer, phase, lives, game_over, round_start_time
    # =====================
    # EVENTS
    # =====================

    # =====================
    # TIMER
    # =====================

    if not game_over:

        elapsed = (pygame.time.get_ticks() - round_start_time) / 1000

        if phase < 5:

            timer = TIME_SHOW - elapsed

            if timer <= 0:

                if phase < 4:
                    phase += 1
                    round_start_time = pygame.time.get_ticks()

                else:
                    phase = 5
                    timer = ANSWER_TIME
                    round_start_time = pygame.time.get_ticks()

        else:

            timer = ANSWER_TIME - elapsed

            if timer <= 0:

                lives -= 1

                if lives <= 0:
                    game_over = True
                else:
                    new_round()

    # =====================
    # DRAW
    # =====================

    screen.fill((20, 20, 28))

    # =====================
    # GAME
    # =====================

    if not game_over:

        # HUD

        screen.blit(
            fonts["date"].render(
                f"Score: {score}",
                True,
                "white"
            ),
            (25, 20)
        )

        screen.blit(
            fonts["date"].render(
                f"Lives: {lives}",
                True,
                "white"
            ),
            (25, 60)
        )

        if phase < 5:
            time_text = f"{max(0, timer):.1f}"
        else:
            time_text = f"{max(0, timer):.1f}"

        screen.blit(
            fonts["DAY"].render(
                time_text,
                True,
                "white"
            ),
            fonts["DAY"].render(
                time_text,
                True,
                "white"
            ).get_rect(
                center=(WIDTH // 2, 50)
            )
        )

        # =================
        # MEMORY PHASES
        # =================

        if phase < 5:

            label = fonts["date"].render(
                "MEMORIZE",
                True,
                "white"
            )

            screen.blit(
                label,
                label.get_rect(
                    center=(WIDTH // 2, 120)
                )
            )

            # Phase 0
            if phase == 0:

                img = resize_image(image1, 350)

                screen.blit(
                    img,
                    img.get_rect(
                        center=(WIDTH // 2, 400)
                    )
                )

            # Phase 1
            elif phase == 1:

                text = fonts["heart"].render(
                    str(number1),
                    True,
                    "white"
                )

                screen.blit(
                    text,
                    text.get_rect(
                        center=(WIDTH // 2, 400)
                    )
                )

            # Phase 2
            elif phase == 2:

                text = fonts["heart"].render(
                    operator,
                    True,
                    (80, 180, 255)
                )

                screen.blit(
                    text,
                    text.get_rect(
                        center=(WIDTH // 2, 400)
                    )
                )

            # Phase 3
            elif phase == 3:

                text = fonts["heart"].render(
                    str(number2),
                    True,
                    "white"
                )

                screen.blit(
                    text,
                    text.get_rect(
                        center=(WIDTH // 2, 400)
                    )
                )

            # Phase 4
            elif phase == 4:

                img = resize_image(image2, 350)

                screen.blit(
                    img,
                    img.get_rect(
                        center=(WIDTH // 2, 400)
                    )
                )

        # =====================
        # ANSWERS
        # =====================

        else:

            question = fonts["DAY"].render(
                "SELECT THE CORRECT ANSWER",
                True,
                "white"
            )

            screen.blit(
                question,
                question.get_rect(
                    center=(WIDTH // 2, 110)
                )
            )

            for i, option in enumerate(options):

                rect = get_option_rect(i)

                mouse = pygame.mouse.get_pos()

                if rect.collidepoint(mouse):
                    color = (80, 150, 230)
                else:
                    color = (45, 80, 130)

                pygame.draw.rect(
                    screen,
                    color,
                    rect,
                    border_radius=15
                )

                # Image 1
                img1 = resize_image(
                    option["image1"],
                    65
                )

                screen.blit(
                    img1,
                    img1.get_rect(
                        center=(rect.x + 55, rect.centery)
                    )
                )
                # RESULT
                if option["operator"] == "+":
                    result = option["number1"] + option["number2"]
                else:
                    result = option["number1"] - option["number2"]

                result_text = fonts["DAY"].render(
                    str(result),
                    True,
                    "white"
                )

                screen.blit(
                    result_text,
                    result_text.get_rect(
                        center=(rect.centerx, rect.centery)
                    )
                )
                # Image 2
                img2 = resize_image(
                    option["image2"],
                    65
                )

                screen.blit(
                    img2,
                    img2.get_rect(
                        center=(rect.x + 345, rect.centery)
                    )
                )

    # =====================
    # GAME OVER
    # =====================

    else:

        title = fonts["heart"].render(
            "GAME OVER",
            True,
            (230, 60, 60)
        )

        screen.blit(
            title,
            title.get_rect(
                center=(WIDTH // 2, 280)
            )
        )

        score_text = fonts["DAY"].render(
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
                center=(WIDTH // 2, 480)
            )
        )


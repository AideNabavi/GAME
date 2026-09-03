import pygame
import random
import sys
from modules.font import *


SHOW_TIME = 1.0
MAX_LIVES = 3

score = 0
lives = MAX_LIVES
level = 1
round_start_time = 0
circles = []
numbers = []
correct_order = []
next_index = 0

show_numbers = True
timer = SHOW_TIME
game_over = False


# =========================
# NEW LEVEL
# =========================

def new_level(WIDTH, HEIGHT):

    global circles
    global numbers
    global correct_order
    global next_index
    global show_numbers
    global timer
    global round_start_time

    # هر 5 مرحله یک دایره بیشتر
    circle_count = min(3 + (level - 1) // 5, 7)

    # اعداد رندوم و بدون تکرار
    numbers = random.sample(
        range(1, 100),
        circle_count
    )

    # ترتیب درست
    correct_order = sorted(numbers)

    next_index = 0

    # جای دایره‌ها
    circles = []

    center_x = WIDTH // 2
    center_y = HEIGHT // 2

    radius_area = 250

    for i in range(circle_count):

        while True:

            x = random.randint(
                center_x - radius_area,
                center_x + radius_area
            )

            y = random.randint(
                center_y - radius_area,
                center_y + radius_area
            )

            pos = pygame.Vector2(x, y)

            good = True

            for old_pos, old_radius in circles:

                if pos.distance_to(old_pos) < 150:
                    good = False
                    break

            if good:
                break

        circles.append(
            (pos, 70)
        )

    show_numbers = True
    timer = SHOW_TIME

    # شروع تایمر این مرحله
    round_start_time = pygame.time.get_ticks()
# =========================
# RESET
# =========================

def reset_game(WIDTH,HEIGHT):

    global score
    global lives
    global level
    global game_over

    score = 0
    lives = MAX_LIVES
    level = 1
    game_over = False

    new_level(WIDTH,HEIGHT)



def MEMORY_GO_(screen,WIDTH,HEIGHT):
    global circles
    global numbers
    global correct_order
    global next_index
    global show_numbers
    global timer
    global round_start_time
    # =====================
    # SHOW TIMER
    # =====================

    if not game_over and show_numbers:

        elapsed = (
            pygame.time.get_ticks() - round_start_time
        ) / 1000

        timer = SHOW_TIME - elapsed

        if timer <= 0:

            timer = 0
            show_numbers = False

    # =====================
    # DRAW
    # =====================

    screen.fill(
        (20, 20, 28)
    )

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
            (30, 60)
        )

        # Level
        screen.blit(
            fonts["date"].render(
                f"Level: {level}",
                True,
                "white"
            ),
            (30, 95)
        )

        # Circle count
        circle_count = len(circles)

        text = fonts["date"].render(
            f"Circles: {circle_count}",
            True,
            "white"
        )

        screen.blit(
            text,
            (WIDTH - 180, 25)
        )

        # =================
        # INSTRUCTION
        # =================

        if show_numbers:

            instruction = fonts["heart"].render(
                "MEMORIZE THE NUMBERS",
                True,
                "white"
            )

        else:

            instruction = fonts["heart"].render(
                "CLICK FROM LOWEST TO HIGHEST",
                True,
                "white"
            )

        screen.blit(
            instruction,
            instruction.get_rect(
                center=(WIDTH // 2, 80)
            )
        )

        # =================
        # CIRCLES
        # =================

        for i, (pos, radius) in enumerate(circles):

            pygame.draw.circle(
                screen,
                (60, 110, 200),
                pos,
                radius
            )

            pygame.draw.circle(
                screen,
                (100, 160, 240),
                pos,
                radius,
                4
            )

            # فقط در یک ثانیه اول عدد دیده شود
            if show_numbers:

                text = fonts["DAY"].render(
                    str(numbers[i]),
                    True,
                    "white"
                )

                screen.blit(
                    text,
                    text.get_rect(
                        center=pos
                    )
                )

            else:

                # دایره خالی
                text = fonts["DAY"].render(
                    "?",
                    True,
                    "white"
                )

                screen.blit(
                    text,
                    text.get_rect(
                        center=pos
                    )
                )

    # =====================
    # GAME OVER
    # =====================

    else:

        title = fonts["DAY"].render(
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

        score_text = fonts["heart"].render(
            f"Score: {score}",
            True,
            "white"
        )

        screen.blit(
            score_text,
            score_text.get_rect(
                center=(WIDTH // 2, 380)
            )
        )

        level_text = fonts["heart"].render(
            f"Level: {level}",
            True,
            "white"
        )

        screen.blit(
            level_text,
            level_text.get_rect(
                center=(WIDTH // 2, 430)
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
                center=(WIDTH // 2, 510)
            )
        )


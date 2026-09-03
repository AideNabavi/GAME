import pygame
import random

pygame.init()

# =========================================================
# SETTINGS
# =========================================================

WIDTH = 1000
HEIGHT = 700

FPS = 60

# مدت نمایش هر عدد / عملگر
SHOW_TIME = 0.7

# زمان انتخاب جواب
ANSWER_TIME = 5.0

# تعداد آیتم‌های عبارت
ITEM_COUNT = 5

# تعداد گزینه‌ها
OPTION_COUNT = 4

# تعداد جان
MAX_LIVES = 3

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quick Math Game")

clock = pygame.time.Clock()

# =========================================================
# FONTS
# =========================================================

font_big = pygame.font.Font(None, 130)
font_medium = pygame.font.Font(None, 70)
font_small = pygame.font.Font(None, 45)

# =========================================================
# COLORS
# =========================================================

WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
GREEN = (60, 220, 100)
RED = (230, 60, 60)
BLUE = (70, 130, 255)
GRAY = (100, 100, 100)
DARK_GRAY = (40, 40, 40)

# =========================================================
# GAME STATES
# =========================================================

SHOWING = "SHOWING"
ANSWERING = "ANSWERING"
GAME_OVER = "GAME_OVER"

game_state = SHOWING

# =========================================================
# GAME VARIABLES
# =========================================================

score = 0
lives = MAX_LIVES

items = []
current_item = 0

show_timer = 0

answer = 0
options = []

answer_timer = ANSWER_TIME

# =========================================================
# CREATE QUESTION
# =========================================================

def create_question():

    global items
    global answer

    while True:

        # سه عدد بین 0 تا 100
        numbers = [
            random.randint(0, 100),
            random.randint(0, 100),
            random.randint(0, 100)
        ]

        # فقط + و -
        operators = [
            random.choice(["+", "-"]),
            random.choice(["+", "-"])
        ]

        # ---------------------------------------------
        # محاسبه جواب
        # ---------------------------------------------

        result = numbers[0]

        result = (
            result + numbers[1]
            if operators[0] == "+"
            else result - numbers[1]
        )

        result = (
            result + numbers[2]
            if operators[1] == "+"
            else result - numbers[2]
        )

        # جواب باید بین 0 تا 100 باشد
        if 0 <= result <= 100:

            answer = result

            items = [
                str(numbers[0]),
                operators[0],
                str(numbers[1]),
                operators[1],
                str(numbers[2])
            ]

            return


# =========================================================
# CREATE OPTIONS
# =========================================================

def create_options():

    global options

    options = [answer]

    while len(options) < OPTION_COUNT:

        # گزینه‌های نزدیک به جواب
        fake = answer + random.randint(-20, 20)

        # جواب باید بین 0 تا 100 باشد
        if 0 <= fake <= 100 and fake not in options:
            options.append(fake)

    random.shuffle(options)


# =========================================================
# START NEW ROUND
# =========================================================

def start_round():

    global game_state
    global current_item
    global show_timer
    global answer_timer

    create_question()

    current_item = 0
    show_timer = 0

    answer_timer = ANSWER_TIME

    game_state = SHOWING


# =========================================================
# RESTART GAME
# =========================================================

def restart_game():

    global score
    global lives

    score = 0
    lives = MAX_LIVES

    start_round()


# =========================================================
# DRAW CENTER TEXT
# =========================================================

def draw_center_text(text, font, color=WHITE, y=HEIGHT // 2):

    surface = font.render(str(text), True, color)

    rect = surface.get_rect(
        center=(WIDTH // 2, y)
    )

    screen.blit(surface, rect)


# =========================================================
# DRAW HEADER
# =========================================================

def draw_header():

    score_text = font_small.render(
        f"Score: {score}",
        True,
        WHITE
    )

    lives_text = font_small.render(
        f"Lives: {lives}",
        True,
        WHITE
    )

    screen.blit(score_text, (30, 25))
    screen.blit(
        lives_text,
        (WIDTH - lives_text.get_width() - 30, 25)
    )


# =========================================================
# DRAW SHOWING PHASE
# =========================================================

def draw_showing():

    # فقط آیتم فعلی نمایش داده می‌شود
    if current_item < len(items):

        draw_center_text(
            items[current_item],
            font_big,
            WHITE
        )

    # شماره آیتم
    progress = font_small.render(
        f"{current_item + 1} / {ITEM_COUNT}",
        True,
        GRAY
    )

    rect = progress.get_rect(
        center=(WIDTH // 2, HEIGHT - 80)
    )

    screen.blit(progress, rect)


# =========================================================
# DRAW ANSWER PHASE
# =========================================================

def draw_answering():

    # نکته مهم:
    # عبارت کامل اینجا نمایش داده نمی‌شود.

    title = font_medium.render(
        "Choose the Answer",
        True,
        WHITE
    )

    title_rect = title.get_rect(
        center=(WIDTH // 2, 130)
    )

    screen.blit(title, title_rect)

    # ---------------------------------------------
    # TIMER
    # ---------------------------------------------

    timer_text = font_small.render(
        f"Time: {max(0, answer_timer):.1f}",
        True,
        WHITE
    )

    timer_rect = timer_text.get_rect(
        center=(WIDTH // 2, 200)
    )

    screen.blit(timer_text, timer_rect)

    # ---------------------------------------------
    # OPTIONS
    # ---------------------------------------------

    button_width = 250
    button_height = 100

    positions = [
        (WIDTH // 2 - button_width - 30, 300),
        (WIDTH // 2 + 30, 300),
        (WIDTH // 2 - button_width - 30, 430),
        (WIDTH // 2 + 30, 430)
    ]

    for i, value in enumerate(options):

        rect = pygame.Rect(
            positions[i][0],
            positions[i][1],
            button_width,
            button_height
        )

        pygame.draw.rect(
            screen,
            DARK_GRAY,
            rect,
            border_radius=15
        )

        pygame.draw.rect(
            screen,
            BLUE,
            rect,
            width=3,
            border_radius=15
        )

        text = font_medium.render(
            str(value),
            True,
            WHITE
        )

        text_rect = text.get_rect(
            center=rect.center
        )

        screen.blit(text, text_rect)


# =========================================================
# GET OPTION RECT
# =========================================================

def get_option_rects():

    button_width = 250
    button_height = 100

    positions = [
        (WIDTH // 2 - button_width - 30, 300),
        (WIDTH // 2 + 30, 300),
        (WIDTH // 2 - button_width - 30, 430),
        (WIDTH // 2 + 30, 430)
    ]

    rects = []

    for x, y in positions:

        rects.append(
            pygame.Rect(
                x,
                y,
                button_width,
                button_height
            )
        )

    return rects


# =========================================================
# DRAW GAME OVER
# =========================================================

def draw_game_over():

    draw_center_text(
        "GAME OVER",
        font_big,
        RED,
        HEIGHT // 2 - 80
    )

    score_text = font_medium.render(
        f"Final Score: {score}",
        True,
        WHITE
    )

    score_rect = score_text.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 30)
    )

    screen.blit(score_text, score_rect)

    restart_text = font_small.render(
        "Press R to Restart",
        True,
        GRAY
    )

    restart_rect = restart_text.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 110)
    )

    screen.blit(restart_text, restart_rect)


# =========================================================
# MAIN LOOP
# =========================================================

create_question()

running = True

while running:

    # dt بر حسب ثانیه
    dt = clock.tick(FPS) / 1000.0

    # =====================================================
    # EVENTS
    # =====================================================

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # ---------------------------------------------
        # KEYBOARD
        # ---------------------------------------------

        if event.type == pygame.KEYDOWN:

            # فقط در Game Over
            if game_state == GAME_OVER:

                if event.key == pygame.K_r:

                    restart_game()

        # ---------------------------------------------
        # MOUSE
        # ---------------------------------------------

        if event.type == pygame.MOUSEBUTTONDOWN:

            if game_state == ANSWERING:

                mouse_pos = event.pos

                rects = get_option_rects()

                for i, rect in enumerate(rects):

                    if rect.collidepoint(mouse_pos):

                        selected = options[i]

                        # ---------------------------------
                        # CORRECT
                        # ---------------------------------

                        if selected == answer:

                            score += 1

                        # ---------------------------------
                        # WRONG
                        # ---------------------------------

                        else:

                            lives -= 1

                        # ---------------------------------
                        # GAME OVER
                        # ---------------------------------

                        if lives <= 0:

                            game_state = GAME_OVER

                        else:

                            start_round()

                        break

    # =====================================================
    # GAME LOGIC
    # =====================================================

    if game_state == SHOWING:

        show_timer += dt

        # زمان نمایش آیتم تمام شد
        if show_timer >= SHOW_TIME:

            show_timer = 0

            current_item += 1

            # ---------------------------------------------
            # 5 آیتم تمام شد
            # ---------------------------------------------

            if current_item >= ITEM_COUNT:

                create_options()

                answer_timer = ANSWER_TIME

                game_state = ANSWERING

    # =====================================================
    # ANSWERING TIMER
    # =====================================================

    elif game_state == ANSWERING:

        answer_timer -= dt

        # زمان تمام شد
        if answer_timer <= 0:

            lives -= 1

            if lives <= 0:

                game_state = GAME_OVER

            else:

                start_round()

    # =====================================================
    # DRAW
    # =====================================================

    screen.fill(BLACK)

    draw_header()

    if game_state == SHOWING:

        draw_showing()

    elif game_state == ANSWERING:

        draw_answering()

    elif game_state == GAME_OVER:

        draw_game_over()

    pygame.display.flip()


pygame.quit()
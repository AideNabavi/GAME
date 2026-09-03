import pygame
import random

from modules.font import *

buttons = {}

# ============================================================
# DIRECTIONS
# ============================================================

DIRECTIONS = [
    "UP",
    "DOWN",
    "LEFT",
    "RIGHT"
]


# ============================================================
# MOVEMENT
# ============================================================

MOVEMENT = {

    "UP": (0, -1),

    "DOWN": (0, 1),

    "LEFT": (-1, 0),

    "RIGHT": (1, 0)

}


# ============================================================
# GAME SETTINGS
# ============================================================

QUESTION_TIME = 5.0

ARROW_SPEED = 120

MAX_ARROWS = 28

SPAWN_DISTANCE = 55

SPAWN_MARGIN = 80


# ============================================================
# GAME VARIABLES
# ============================================================

score = 0

current_direction = None

movement_direction = None

question_start_time = 0

arrows = []

spawn_distance = 0

last_move_time = 0


# ============================================================
# LOAD ARROW IMAGES
# ============================================================

ARROW_IMAGES = {

    "UP": pygame.image.load(
        "asset/image/MODE/MOVE/U.png"
    ).convert_alpha(),

    "DOWN": pygame.image.load(
        "asset/image/MODE/MOVE/D.png"
    ).convert_alpha(),

    "LEFT": pygame.image.load(
        "asset/image/MODE/MOVE/L.png"
    ).convert_alpha(),

    "RIGHT": pygame.image.load(
        "asset/image/MODE/MOVE/R.png"
    ).convert_alpha()

}


# ============================================================
# RESIZE ARROW IMAGES
# ============================================================

ARROW_SIZE = (90, 90)

for direction in ARROW_IMAGES:

    ARROW_IMAGES[direction] = pygame.transform.smoothscale(
        ARROW_IMAGES[direction],
        ARROW_SIZE
    )


# ============================================================
# TIMER FONT
# ============================================================

timer_font = pygame.font.Font(
    None,
    42
)


# ============================================================
# BUTTONS
# ============================================================

BUTTON_SIZE = 110


def create_buttons(WIDTH, HEIGHT):

    BUTTON_Y = HEIGHT - 200

    buttons = {

        "LEFT": pygame.Rect(
            WIDTH // 2 - 170,
            BUTTON_Y,
            BUTTON_SIZE,
            BUTTON_SIZE
        ),

        "UP": pygame.Rect(
            WIDTH // 2 - 80,
            BUTTON_Y,
            BUTTON_SIZE,
            BUTTON_SIZE
        ),

        "DOWN": pygame.Rect(
            WIDTH // 2 + 10,
            BUTTON_Y,
            BUTTON_SIZE,
            BUTTON_SIZE
        ),

        "RIGHT": pygame.Rect(
            WIDTH // 2 + 100,
            BUTTON_Y,
            BUTTON_SIZE,
            BUTTON_SIZE
        )

    }

    return buttons


# ============================================================
# CREATE ARROW
# ============================================================

def create_arrow(WIDTH, HEIGHT, first_spawn=False):

    if movement_direction == "RIGHT":

        x = -SPAWN_MARGIN

        if first_spawn:

            x = random.randint(
                0,
                WIDTH
            )

        y = random.randint(
            100,
            HEIGHT - 150
        )


    elif movement_direction == "LEFT":

        x = WIDTH + SPAWN_MARGIN

        if first_spawn:

            x = random.randint(
                0,
                WIDTH
            )

        y = random.randint(
            100,
            HEIGHT - 150
        )


    elif movement_direction == "DOWN":

        x = random.randint(
            30,
            WIDTH - 30
        )

        y = -SPAWN_MARGIN

        if first_spawn:

            y = random.randint(
                100,
                HEIGHT
            )


    else:

        x = random.randint(
            30,
            WIDTH - 30
        )

        y = HEIGHT + SPAWN_MARGIN

        if first_spawn:

            y = random.randint(
                100,
                HEIGHT
            )


    arrows.append({

        "x": float(x),

        "y": float(y)

    })


# ============================================================
# NEW QUESTION
# ============================================================

def new_question(WIDTH, HEIGHT):

    global current_direction
    global movement_direction
    global question_start_time
    global spawn_distance
    global last_move_time

    # --------------------------------------------------------
    # جهت فلش
    # --------------------------------------------------------

    current_direction = random.choice(
        DIRECTIONS
    )


    # --------------------------------------------------------
    # جهت حرکت
    # --------------------------------------------------------

    movement_direction = random.choice(
        DIRECTIONS
    )


    # --------------------------------------------------------
    # پاک کردن فلش‌های قبلی
    # --------------------------------------------------------

    arrows.clear()


    # --------------------------------------------------------
    # ساخت فلش‌های اولیه
    # --------------------------------------------------------

    for _ in range(MAX_ARROWS):

        create_arrow(
            WIDTH,
            HEIGHT,
            first_spawn=True
        )


    # --------------------------------------------------------
    # RESET SPAWN
    # --------------------------------------------------------

    spawn_distance = 0


    # --------------------------------------------------------
    # START QUESTION TIMER
    # --------------------------------------------------------

    question_start_time = pygame.time.get_ticks()


    # --------------------------------------------------------
    # START MOVEMENT TIMER
    # --------------------------------------------------------

    last_move_time = pygame.time.get_ticks()


# ============================================================
# SPAWN SYSTEM
# ============================================================

def update_spawn(WIDTH, HEIGHT):

    global spawn_distance

    current_time = pygame.time.get_ticks()

    spawn_distance = (
        current_time - question_start_time
    )


    # هر SPAWN_DISTANCE میلی‌ثانیه
    # یک فلش جدید ایجاد می‌شود

    if len(arrows) < MAX_ARROWS:

        if spawn_distance >= SPAWN_DISTANCE:

            create_arrow(
                WIDTH,
                HEIGHT
            )

            spawn_distance = 0


# ============================================================
# UPDATE ARROWS
# ============================================================

def update_arrows(WIDTH, HEIGHT):

    global last_move_time

    current_time = pygame.time.get_ticks()

    elapsed = (
        current_time - last_move_time
    ) / 1000

    last_move_time = current_time


    dx, dy = MOVEMENT[
        movement_direction
    ]


    for arrow in arrows:

        arrow["x"] += (
            dx
            * ARROW_SPEED
            * elapsed
        )

        arrow["y"] += (
            dy
            * ARROW_SPEED
            * elapsed
        )


    # --------------------------------------------------------
    # حذف فلش‌های خارج از صفحه
    # --------------------------------------------------------

    visible_arrows = []


    for arrow in arrows:

        if (

            -100
            < arrow["x"]
            < WIDTH + 100

            and

            -100
            < arrow["y"]
            < HEIGHT + 100

        ):

            visible_arrows.append(
                arrow
            )


    arrows[:] = visible_arrows


# ============================================================
# DRAW ARROWS
# ============================================================

def draw_arrows(screen):

    image = ARROW_IMAGES[
        current_direction
    ]


    for arrow in arrows:

        rect = image.get_rect(

            center=(

                int(arrow["x"]),

                int(arrow["y"])

            )

        )


        screen.blit(
            image,
            rect
        )


# ============================================================
# DRAW BUTTONS
# ============================================================

def draw_buttons(screen, mouse_pos, buttons):

    for direction, rect in buttons.items():

        # ----------------------------------------------------
        # HOVER
        # ----------------------------------------------------

        if rect.collidepoint(
            mouse_pos
        ):

            background = (
                75,
                75,
                95
            )

        else:

            background = (
                40,
                40,
                55
            )


        # ----------------------------------------------------
        # BACKGROUND
        # ----------------------------------------------------

        pygame.draw.rect(

            screen,

            background,

            rect,

            border_radius=15

        )


        # ----------------------------------------------------
        # BORDER
        # ----------------------------------------------------

        pygame.draw.rect(

            screen,

            (110, 110, 130),

            rect,

            2,

            border_radius=15

        )


        # ----------------------------------------------------
        # ARROW IMAGE
        # ----------------------------------------------------

        image = ARROW_IMAGES[
            direction
        ]


        image_rect = image.get_rect(

            center=rect.center

        )


        screen.blit(

            image,

            image_rect

        )


# ============================================================
# ANSWER
# ============================================================

def answer(direction, WIDTH, HEIGHT):

    global score

    # --------------------------------------------------------
    # CORRECT
    # --------------------------------------------------------

    if direction == movement_direction:

        score += 1


    # --------------------------------------------------------
    # WRONG
    # --------------------------------------------------------

    else:

        score -= 1


    # --------------------------------------------------------
    # NEW QUESTION
    # --------------------------------------------------------

    new_question(
        WIDTH,
        HEIGHT
    )


# ============================================================
# DRAW SCORE
# ============================================================

def draw_score(screen):

    text = fonts["heart"].render(

        f"Score: {score}",

        True,

        (255, 255, 255)

    )


    screen.blit(

        text,

        (25, 20)

    )


# ============================================================
# DRAW TIMER
# ============================================================

def draw_timer(screen, WIDTH):

    elapsed = (

        pygame.time.get_ticks()

        - question_start_time

    ) / 1000


    remaining = max(

        0,

        QUESTION_TIME - elapsed

    )


    text = timer_font.render(

        f"{remaining:.1f}",

        True,

        (255, 255, 255)

    )


    rect = text.get_rect(

        center=(

            WIDTH // 2,

            35

        )

    )


    screen.blit(

        text,

        rect

    )


# ============================================================
# RESET GAME
# ============================================================

def reset_game(WIDTH, HEIGHT):

    global score

    score = 0

    new_question(
        WIDTH,
        HEIGHT
    )


# ============================================================
# START / MAIN FUNCTION
# ============================================================

def MOVE_ARROW_(screen, WIDTH, HEIGHT):

    global buttons
    global score

    # ========================================================
    # MOUSE
    # ========================================================

    mouse_pos = pygame.mouse.get_pos()


    # ========================================================
    # TIMER
    # ========================================================

    elapsed = (

        pygame.time.get_ticks()

        - question_start_time

    ) / 1000


    if elapsed >= QUESTION_TIME:

        score -= 1

        new_question(
            WIDTH,
            HEIGHT
        )


    # ========================================================
    # UPDATE
    # ========================================================

    update_spawn(
        WIDTH,
        HEIGHT
    )


    update_arrows(
        WIDTH,
        HEIGHT
    )


    # ========================================================
    # DRAW
    # ========================================================

    screen.fill(
        (18, 18, 25)
    )


    draw_arrows(
        screen
    )


    draw_score(
        screen
    )


    draw_timer(
        screen,
        WIDTH
    )


    buttons = create_buttons(
        WIDTH,
        HEIGHT
    )


    draw_buttons(
        screen,
        mouse_pos,
        buttons
    )
import pygame
import random
import math
import sys
from modules.font import *

WIDTH = 1000
HEIGHT = 700

screen = None


def WIDTH_HEIGHT_gettter(screen_, WIDTH_, HEIGHT_):

    global WIDTH
    global HEIGHT
    global screen

    WIDTH = WIDTH_
    HEIGHT = HEIGHT_
    screen = screen_
    
# =========================================================
# FPS
# =========================================================

# clock = pygame.time.Clock()

# FPS = 60


# =========================================================
# COLORS
# =========================================================

BACKGROUND = (18, 22, 27)
GRID_COLOR = (28, 33, 39)

SNAKE_HEAD_COLOR = (80, 215, 100)
SNAKE_BODY_COLOR = (45, 165, 70)

FOOD_COLOR = (235, 65, 65)
FOOD_LIGHT = (255, 150, 150)

WHITE = (245, 245, 245)
GRAY = (160, 160, 160)

GAME_OVER_COLOR = (235, 70, 70)

TARGET_COLOR = (255, 215, 80)

LIFE_COLOR = (235, 70, 70)


# # =========================================================
# # FONTS
# # =========================================================

# FONT_BIG = pygame.font.SysFont(
#     "arial",
#     58,
#     bold=True
# )

# FONT_MEDIUM = pygame.font.SysFont(
#     "arial",
#     30,
#     bold=True
# )

# FONT_SMALL = pygame.font.SysFont(
#     "arial",
#     23
# )

# FONT_NUMBER = pygame.font.SysFont(
#     "arial",
#     25,
#     bold=True
# )


# =========================================================
# GAME SETTINGS
# =========================================================

SEGMENT_SIZE = 24

SEGMENT_DISTANCE = 19

SNAKE_SPEED = 220

FOOD_DISTANCE = 28

COLLISION_DISTANCE = 17


# =========================================================
# NUMBER SETTINGS
# =========================================================

# تعداد اولیه اعداد پرت
BASE_DISTRACTOR_COUNT = 8

# حداکثر عدد هدف
MAX_TARGET = 30

# حداقل فاصله مرکز دو دایره
NUMBER_MIN_DISTANCE = 75

# شعاع دایره عدد
NUMBER_RADIUS = 27


# =========================================================
# LIFE SETTINGS
# =========================================================

MAX_LIVES = 3

lives = MAX_LIVES


# =========================================================
# GAME VARIABLES
# =========================================================

snake = []

foods = []

score = 0

target_number = 1

game_over = False

game_won = False

paused = False


# =========================================================
# MOVEMENT
# =========================================================

direction = pygame.Vector2(
    1,
    0
)

next_direction = pygame.Vector2(
    1,
    0
)


# =========================================================
# TIMER
# =========================================================

start_time = 0

game_time = 0


# =========================================================
# GET DISTRACTOR COUNT
# =========================================================

def get_distractor_count():

    # -----------------------------------------------------
    # 1 تا 10  -> 8 distractors
    # 11 تا 20 -> 9 distractors
    # 21 تا 30 -> 10 distractors
    # -----------------------------------------------------

    extra = (
        (target_number - 1) // 10
    )

    return (
        BASE_DISTRACTOR_COUNT
        + extra
    )


# =========================================================
# RESET
# =========================================================

def reset_SNAKE():

    global snake
    global foods
    global score
    global target_number
    global game_over
    global game_won
    global paused
    global direction
    global next_direction
    global start_time
    global game_time
    global lives


    # =====================================================
    # RESET STATE
    # =====================================================

    score = 0

    target_number = 1

    lives = MAX_LIVES

    game_over = False

    game_won = False

    paused = False


    # =====================================================
    # RESET DIRECTION
    # =====================================================

    direction = pygame.Vector2(
        1,
        0
    )

    next_direction = pygame.Vector2(
        1,
        0
    )


    # =====================================================
    # CREATE SNAKE
    # =====================================================

    center_x = WIDTH / 2

    center_y = HEIGHT / 2


    snake = []


    for i in range(8):

        position = pygame.Vector2(

            center_x
            - i * SEGMENT_DISTANCE,

            center_y

        )

        snake.append(
            position
        )


    # =====================================================
    # CREATE NUMBERS
    # =====================================================

    foods = create_foods()


    # =====================================================
    # TIMER
    # =====================================================

    start_time = pygame.time.get_ticks()

    game_time = 0


# =========================================================
# CREATE FOOD POSITION
# =========================================================

def create_food_position(existing_positions):

    max_attempts = 2000


    for _ in range(max_attempts):

        x = random.randint(
            NUMBER_RADIUS + 10,
            WIDTH - NUMBER_RADIUS - 10
        )

        y = random.randint(
            105 + NUMBER_RADIUS,
            HEIGHT - NUMBER_RADIUS - 10
        )


        position = pygame.Vector2(
            x,
            y
        )


        valid = True


        # =================================================
        # DON'T SPAWN ON SNAKE
        # =================================================

        for segment in snake:

            if (
                position.distance_to(segment)
                < NUMBER_RADIUS + SEGMENT_SIZE + 10
            ):

                valid = False

                break


        if not valid:

            continue


        # =================================================
        # DON'T OVERLAP OTHER NUMBERS
        # =================================================

        for other_position in existing_positions:

            if (
                position.distance_to(other_position)
                < NUMBER_MIN_DISTANCE
            ):

                valid = False

                break


        if valid:

            return position


    # =====================================================
    # FALLBACK
    # =====================================================

    # این حالت فقط زمانی استفاده می‌شود که صفحه
    # بیش از حد شلوغ شده باشد.
    return pygame.Vector2(
        WIDTH // 2,
        HEIGHT // 2
    )


# =========================================================
# CREATE DISTRACTOR NUMBER
# =========================================================

def create_distractor_number(existing_numbers):

    max_attempts = 1000


    for _ in range(max_attempts):

        number = random.randint(
            1,
            MAX_TARGET
        )


        # -------------------------------------------------
        # نباید هدف فعلی باشد
        # -------------------------------------------------

        if number == target_number:

            continue


        # -------------------------------------------------
        # نباید تکراری باشد
        # -------------------------------------------------

        if number in existing_numbers:

            continue


        return number


    # -----------------------------------------------------
    # Fallback
    # -----------------------------------------------------

    for number in range(
        1,
        MAX_TARGET + 1
    ):

        if number != target_number:

            if number not in existing_numbers:

                return number


    return 1


# =========================================================
# CREATE NUMBERS
# =========================================================

def create_foods():

    foods = []

    positions = []

    used_numbers = []


    # =====================================================
    # TARGET
    # =====================================================

    target_position = create_food_position(
        positions
    )

    positions.append(
        target_position
    )

    used_numbers.append(
        target_number
    )


    foods.append({

        "number": target_number,

        "position": target_position,

        "target": True

    })


    # =====================================================
    # DISTRACTORS
    # =====================================================

    distractor_count = get_distractor_count()


    for _ in range(
        distractor_count
    ):

        number = create_distractor_number(
            used_numbers
        )


        used_numbers.append(
            number
        )


        position = create_food_position(
            positions
        )


        positions.append(
            position
        )


        foods.append({

            "number": number,

            "position": position,

            "target": False

        })


    return foods


# =========================================================
# ADD NEW DISTRACTOR
# =========================================================

def add_new_distractor():

    global foods


    # -----------------------------------------------------
    # Existing numbers
    # -----------------------------------------------------

    existing_numbers = []


    for food in foods:

        existing_numbers.append(
            food["number"]
        )


    # -----------------------------------------------------
    # Existing positions
    # -----------------------------------------------------

    existing_positions = []


    for food in foods:

        existing_positions.append(
            food["position"]
        )


    # -----------------------------------------------------
    # Create number
    # -----------------------------------------------------

    number = create_distractor_number(
        existing_numbers
    )


    # -----------------------------------------------------
    # Create position
    # -----------------------------------------------------

    position = create_food_position(
        existing_positions
    )


    # -----------------------------------------------------
    # Add
    # -----------------------------------------------------

    foods.append({

        "number": number,

        "position": position,

        "target": False

    })


# =========================================================
# EVENTS
# =========================================================

def event_SNAKE(event):

    global next_direction
    global paused


    if event.type != pygame.KEYDOWN:

        return


    # =====================================================
    # RESTART
    # =====================================================

    if event.key == pygame.K_r:

        reset_SNAKE()

        return


    # =====================================================
    # ESC
    # =====================================================

    if event.key == pygame.K_ESCAPE:

        pygame.quit()

        sys.exit()


    # =====================================================
    # PAUSE
    # =====================================================

    if event.key == pygame.K_p:

        if not game_over:

            paused = not paused

        return


    # =====================================================
    # UP
    # =====================================================

    if event.key in (
        pygame.K_UP,
        pygame.K_w
    ):

        new_direction = pygame.Vector2(
            0,
            -1
        )


    # =====================================================
    # DOWN
    # =====================================================

    elif event.key in (
        pygame.K_DOWN,
        pygame.K_s
    ):

        new_direction = pygame.Vector2(
            0,
            1
        )


    # =====================================================
    # LEFT
    # =====================================================

    elif event.key in (
        pygame.K_LEFT,
        pygame.K_a
    ):

        new_direction = pygame.Vector2(
            -1,
            0
        )


    # =====================================================
    # RIGHT
    # =====================================================

    elif event.key in (
        pygame.K_RIGHT,
        pygame.K_d
    ):

        new_direction = pygame.Vector2(
            1,
            0
        )


    else:

        return


    # =====================================================
    # PREVENT 180 DEGREE TURN
    # =====================================================

    if new_direction == -direction:

        return


    next_direction = new_direction


# =========================================================
# UPDATE TIMER
# =========================================================

def update_timer():

    global game_time


    if game_over:

        return


    if paused:

        return


    current_time = pygame.time.get_ticks()


    game_time = (
        current_time - start_time
    ) // 1000


# =========================================================
# UPDATE DIRECTION
# =========================================================

def update_direction():

    global direction


    if next_direction == direction:

        return


    direction = next_direction.copy()


# =========================================================
# MOVE HEAD
# =========================================================

def move_head(dt):

    if not snake:

        return


    # -----------------------------------------------------
    # Direction
    # -----------------------------------------------------

    update_direction()


    # -----------------------------------------------------
    # Movement
    # -----------------------------------------------------

    movement = (
        direction
        * SNAKE_SPEED
        * dt
    )


    snake[0] += movement


# =========================================================
# WRAP SCREEN
# =========================================================

def wrap_head():

    if not snake:

        return


    head = snake[0]


    # =====================================================
    # RIGHT
    # =====================================================

    if head.x > WIDTH:

        head.x = 0


    # =====================================================
    # LEFT
    # =====================================================

    elif head.x < 0:

        head.x = WIDTH


    # =====================================================
    # BOTTOM
    # =====================================================

    if head.y > HEIGHT:

        head.y = 70


    # =====================================================
    # TOP
    # =====================================================

    elif head.y < 70:

        head.y = HEIGHT


# =========================================================
# FOLLOW HEAD
# =========================================================

def update_body():

    if len(snake) < 2:

        return


    for i in range(
        1,
        len(snake)
    ):

        previous = snake[i - 1]

        current = snake[i]


        difference = (
            previous - current
        )


        distance = difference.length()


        if distance == 0:

            continue


        target_distance = SEGMENT_DISTANCE


        if distance > target_distance:

            direction_to_previous = (
                difference.normalize()
            )


            snake[i] = (
                previous
                - direction_to_previous
                * target_distance
            )


# =========================================================
# CHECK NUMBER
# =========================================================

def check_food():

    global foods
    global score
    global target_number
    global game_over
    global game_won
    global lives


    if not foods:

        return


    head = snake[0]


    eaten_food = None


    # =====================================================
    # CHECK ALL NUMBERS
    # =====================================================

    for food in foods:

        position = food["position"]


        distance = (
            head.distance_to(position)
        )


        if distance <= FOOD_DISTANCE:

            eaten_food = food

            break


    # =====================================================
    # NOTHING TOUCHED
    # =====================================================

    if eaten_food is None:

        return


    # =====================================================
    # CORRECT NUMBER
    # =====================================================

    if eaten_food["number"] == target_number:

        # -------------------------------------------------
        # SCORE
        # -------------------------------------------------

        score += 1


        # -------------------------------------------------
        # REMOVE TARGET
        # -------------------------------------------------

        foods.remove(
            eaten_food
        )


        # -------------------------------------------------
        # FINISHED
        # -------------------------------------------------

        if target_number >= MAX_TARGET:

            game_over = True

            game_won = True

            return


        # -------------------------------------------------
        # NEXT TARGET
        # -------------------------------------------------

        target_number += 1


        # -------------------------------------------------
        # NEW LAYOUT
        # -------------------------------------------------

        foods = create_foods()


    # =====================================================
    # WRONG NUMBER
    # =====================================================

    else:

        # -------------------------------------------------
        # Lose one life
        # -------------------------------------------------

        lives -= 1


        # -------------------------------------------------
        # Remove wrong number
        # -------------------------------------------------

        foods.remove(
            eaten_food
        )


        # -------------------------------------------------
        # Game Over
        # -------------------------------------------------

        if lives <= 0:

            lives = 0

            game_over = True

            game_won = False

            return


        # -------------------------------------------------
        # Replace the wrong distractor
        # -------------------------------------------------

        add_new_distractor()


# =========================================================
# SELF COLLISION
# =========================================================

def check_self_collision():

    global game_over


    if len(snake) < 6:

        return


    head = snake[0]


    for segment in snake[5:]:

        distance = (
            head.distance_to(segment)
        )


        if distance < COLLISION_DISTANCE:

            game_over = True

            return


# =========================================================
# UPDATE
# =========================================================

def update_SNAKE(dt):

    if game_over:

        return


    if paused:

        return


    # =====================================================
    # TIMER
    # =====================================================

    update_timer()


    # =====================================================
    # MOVE HEAD
    # =====================================================

    move_head(dt)


    # =====================================================
    # WRAP
    # =====================================================

    wrap_head()


    # =====================================================
    # BODY FOLLOW
    # =====================================================

    update_body()


    # =====================================================
    # NUMBERS
    # =====================================================

    check_food()


    # =====================================================
    # SELF COLLISION
    # =====================================================

    check_self_collision()


# =========================================================
# DRAW GRID
# =========================================================

def draw_grid():

    grid_size = 35


    # -----------------------------------------------------
    # Vertical
    # -----------------------------------------------------

    for x in range(
        0,
        WIDTH,
        grid_size
    ):

        pygame.draw.line(

            screen,

            GRID_COLOR,

            (
                x,
                70
            ),

            (
                x,
                HEIGHT
            ),

            1
        )


    # -----------------------------------------------------
    # Horizontal
    # -----------------------------------------------------

    for y in range(
        70,
        HEIGHT,
        grid_size
    ):

        pygame.draw.line(

            screen,

            GRID_COLOR,

            (
                0,
                y
            ),

            (
                WIDTH,
                y
            ),

            1
        )


# =========================================================
# DRAW FOOD NUMBERS
# =========================================================

def draw_food():

    for food in foods:

        position = food["position"]

        number = food["number"]

        x = int(position.x)

        y = int(position.y)


        # =================================================
        # SHADOW
        # =================================================

        pygame.draw.circle(

            screen,

            (100, 25, 25),

            (
                x + 2,
                y + 3
            ),

            NUMBER_RADIUS
        )


        # =================================================
        # MAIN CIRCLE
        # =================================================

        pygame.draw.circle(

            screen,

            FOOD_COLOR,

            (
                x,
                y
            ),

            NUMBER_RADIUS
        )


        # =================================================
        # LIGHT
        # =================================================

        pygame.draw.circle(

            screen,

            FOOD_LIGHT,

            (
                x - 7,
                y - 7
            ),

            7
        )


        # =================================================
        # NUMBER
        # =================================================

        number_surface = fonts["heart"].render(

            str(number),

            True,

            WHITE
        )


        number_rect = number_surface.get_rect(

            center=(
                x,
                y
            )

        )


        screen.blit(

            number_surface,

            number_rect
        )


# =========================================================
# DRAW SNAKE
# =========================================================

def draw_snake():

    # -----------------------------------------------------
    # Draw body first
    # -----------------------------------------------------

    for i in range(
        len(snake) - 1,
        -1,
        -1
    ):

        segment = snake[i]


        x = int(segment.x)

        y = int(segment.y)


        if i == 0:

            color = SNAKE_HEAD_COLOR

            radius = SEGMENT_SIZE // 2 + 2

        else:

            color = SNAKE_BODY_COLOR

            radius = SEGMENT_SIZE // 2


        pygame.draw.circle(

            screen,

            color,

            (
                x,
                y
            ),

            radius
        )


    # -----------------------------------------------------
    # Head eyes
    # -----------------------------------------------------

    draw_eyes()


# =========================================================
# DRAW EYES
# =========================================================

def draw_eyes():

    if not snake:

        return


    head = snake[0]


    forward = direction


    if forward.length() == 0:

        forward = pygame.Vector2(
            1,
            0
        )


    side = pygame.Vector2(
        -forward.y,
        forward.x
    )


    eye_center = head + (
        forward * 6
    )


    eye_1 = (
        eye_center
        + side * 5
    )


    eye_2 = (
        eye_center
        - side * 5
    )


    # -----------------------------------------------------
    # Eye 1
    # -----------------------------------------------------

    pygame.draw.circle(

        screen,

        (20, 25, 20),

        (
            int(eye_1.x),
            int(eye_1.y)
        ),

        3
    )


    # -----------------------------------------------------
    # Eye 2
    # -----------------------------------------------------

    pygame.draw.circle(

        screen,

        (20, 25, 20),

        (
            int(eye_2.x),
            int(eye_2.y)
        ),

        3
    )


# =========================================================
# TEXT
# =========================================================

def draw_text(
    text,
    font,
    center,
    color=WHITE
):

    surface = font.render(

        str(text),

        True,

        color
    )


    rect = surface.get_rect(
        center=center
    )


    screen.blit(
        surface,
        rect
    )


# =========================================================
# UI
# =========================================================

def draw_UI():

    # =====================================================
    # SCORE
    # =====================================================

    draw_text(

        f"SCORE  {score}",

        fonts["heart"],

        (
            110,
            32
        )
    )


    # =====================================================
    # TARGET
    # =====================================================

    draw_text(

        f"TARGET  {target_number}",

        fonts["heart"],

        (
            WIDTH // 2,
            32
        ),

        TARGET_COLOR
    )


    # =====================================================
    # LIVES
    # =====================================================

    draw_text(

        f"LIVES  {lives}",

        fonts["heart"],

        (
            WIDTH - 220,
            32
        ),

        LIFE_COLOR
    )


    # =====================================================
    # TIME
    # =====================================================

    draw_text(

        f"{game_time}s",

        fonts["heart"],

        (
            WIDTH - 65,
            32
        ),

        GRAY
    )


# =========================================================
# PAUSE
# =========================================================

def draw_pause():

    if not paused:

        return


    overlay = pygame.Surface(
        (WIDTH, HEIGHT),
        pygame.SRCALPHA
    )


    overlay.fill(
        (0, 0, 0, 130)
    )


    screen.blit(
        overlay,
        (0, 0)
    )


    draw_text(

        "PAUSED",

        fonts["heart"],

        (
            WIDTH // 2,
            HEIGHT // 2
        )
    )


    draw_text(

        "Press P to Continue",

        fonts["heart"],

        (
            WIDTH // 2,
            HEIGHT // 2 + 60
        ),

        GRAY
    )


# =========================================================
# GAME OVER
# =========================================================

def draw_game_over():

    if not game_over:

        return


    # =====================================================
    # OVERLAY
    # =====================================================

    overlay = pygame.Surface(

        (WIDTH, HEIGHT),

        pygame.SRCALPHA
    )


    overlay.fill(
        (0, 0, 0, 170)
    )


    screen.blit(
        overlay,
        (0, 0)
    )


    # =====================================================
    # WIN
    # =====================================================

    if game_won:

        draw_text(

            "COMPLETE!",

            fonts["heart"],

            (
                WIDTH // 2,
                HEIGHT // 2 - 90
            ),

            TARGET_COLOR
        )


        draw_text(

            f"You reached {MAX_TARGET}",

            fonts["heart"],

            (
                WIDTH // 2,
                HEIGHT // 2 - 25
            )
        )


    # =====================================================
    # LOSE
    # =====================================================

    else:

        draw_text(

            "GAME OVER",

            fonts["heart"],

            (
                WIDTH // 2,
                HEIGHT // 2 - 90
            ),

            GAME_OVER_COLOR
        )


        draw_text(

            "No Lives Left",

            fonts["heart"],

            (
                WIDTH // 2,
                HEIGHT // 2 - 25
            ),

            LIFE_COLOR
        )


    # =====================================================
    # SCORE
    # =====================================================

    draw_text(

        f"Score: {score}",

        fonts["heart"],

        (
            WIDTH // 2,
            HEIGHT // 2 + 25
        )
    )


    # =====================================================
    # TIME
    # =====================================================

    draw_text(

        f"Time: {game_time}s",

        fonts["heart"],

        (
            WIDTH // 2,
            HEIGHT // 2 + 65
        ),

        GRAY
    )


    # =====================================================
    # RESTART
    # =====================================================

    draw_text(

        "Press R to Restart",

        fonts["heart"],

        (
            WIDTH // 2,
            HEIGHT // 2 + 120
        )
    )


# =========================================================
# DRAW
# =========================================================

def draw_SNAKE():

    # -----------------------------------------------------
    # Background
    # -----------------------------------------------------

    screen.fill(
        BACKGROUND
    )


    # -----------------------------------------------------
    # Grid
    # -----------------------------------------------------

    draw_grid()


    # -----------------------------------------------------
    # Numbers
    # -----------------------------------------------------

    draw_food()


    # -----------------------------------------------------
    # Snake
    # -----------------------------------------------------

    draw_snake()


    # -----------------------------------------------------
    # UI
    # -----------------------------------------------------

    draw_UI()


    # -----------------------------------------------------
    # Pause
    # -----------------------------------------------------

    draw_pause()


    # -----------------------------------------------------
    # Game Over
    # -----------------------------------------------------

    draw_game_over()


    # -----------------------------------------------------
    # Display
    # -----------------------------------------------------

    # pygame.display.flip()


# =========================================================
# MAIN
# =========================================================


def main_SNAKE():

    # -------------------------------------------------
    # GAME TIME
    # -------------------------------------------------

    current_time = pygame.time.get_ticks()

    if not hasattr(main_SNAKE, "last_time"):
        main_SNAKE.last_time = current_time

    dt = (current_time - main_SNAKE.last_time) / 1000.0
    main_SNAKE.last_time = current_time


    # -------------------------------------------------
    # Limit huge dt
    # -------------------------------------------------

    dt = min(
        dt,
        0.05
    )
        # -------------------------------------------------
        # EVENTS
        # -------------------------------------------------




    # -------------------------------------------------
    # UPDATE
    # -------------------------------------------------

    update_SNAKE(dt)


    # -------------------------------------------------
    # DRAW
    # -------------------------------------------------

    draw_SNAKE()


    # pygame.quit()

    # sys.exit()


# =========================================================
# RUN
# =========================================================

# if __name__ == "__main__":

#     main_SNAKE()
    
    
    
    

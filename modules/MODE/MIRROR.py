import pygame
import random
import time
from modules.font import fonts


pygame.init()


# --------------------------------------------------
# Screen
# --------------------------------------------------

WIDTH = 1000
HEIGHT = 700

# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Mirror Pattern")


# clock = pygame.time.Clock()


# font = pygame.font.Font(None, 45)
# small_font = pygame.font.Font(None, 32)


# --------------------------------------------------
# Colors
# --------------------------------------------------

BG = (25, 25, 30)

WHITE = (255, 255, 255)

GRID_COLOR = (80, 80, 90)

EMPTY_COLOR = (45, 45, 50)

ACTIVE_COLOR = (80, 170, 255)

LINE_COLOR = (200, 200, 200)

MIRROR_COLOR = (100, 100, 110)


# --------------------------------------------------
# Game settings
# --------------------------------------------------

START_GRID = 3

MAX_GRID = 8

TIME_LIMIT = 15


level = 1

score = 0

grid_size = START_GRID

player_pattern = []

target_pattern = []

start_time = 0

game_over = False

message = ""


# --------------------------------------------------
# Grid settings
# --------------------------------------------------

CELL_SIZE = 55

LEFT_X = 150
RIGHT_X = 600

GRID_Y = 180


# --------------------------------------------------
# Create random pattern
# --------------------------------------------------

def create_pattern():

    pattern = []

    for row in range(grid_size):

        current_row = []

        for col in range(grid_size):

            value = random.choice([0, 0, 0, 1])

            current_row.append(value)

        pattern.append(current_row)

    # مطمئن شو حداقل یک خانه فعال باشد

    if not any(
        any(row)
        for row in pattern
    ):

        row = random.randint(0, grid_size - 1)

        col = random.randint(0, grid_size - 1)

        pattern[row][col] = 1

    return pattern


# --------------------------------------------------
# Create mirror
# --------------------------------------------------

def create_mirror(pattern):

    mirror = []

    for row in pattern:

        mirror.append(row[::-1])

    return mirror


# --------------------------------------------------
# Start new round
# --------------------------------------------------

def new_round_MIRROR():

    global target_pattern
    global player_pattern
    global start_time
    global message

    target_pattern = create_pattern()

    player_pattern = []

    for row in range(grid_size):

        player_pattern.append(
            [0] * grid_size
        )

    start_time = time.time()

    message = ""


# --------------------------------------------------
# Check answer
# --------------------------------------------------

def check_answer():

    global score
    global level
    global grid_size
    global game_over
    global message

    correct_pattern = create_mirror(
        target_pattern
    )

    if player_pattern == correct_pattern:

        score += grid_size * 10

        level += 1

        if grid_size < MAX_GRID:

            grid_size += 1

        message = "CORRECT!"

        new_round_MIRROR()

    else:

        score -= 5

        message = "WRONG!"

        new_round_MIRROR()


# --------------------------------------------------
# Get cell from mouse
# --------------------------------------------------

def get_clicked_cell(mouse_pos):

    mouse_x, mouse_y = mouse_pos

    grid_width = grid_size * CELL_SIZE

    grid_height = grid_size * CELL_SIZE


    # سمت راست

    right_rect = pygame.Rect(
        RIGHT_X,
        GRID_Y,
        grid_width,
        grid_height
    )


    if right_rect.collidepoint(mouse_pos):

        col = (
            mouse_x - RIGHT_X
        ) // CELL_SIZE

        row = (
            mouse_y - GRID_Y
        ) // CELL_SIZE

        if (
            0 <= row < grid_size
            and
            0 <= col < grid_size
        ):

            return row, col


    return None


# --------------------------------------------------
# Draw grid
# --------------------------------------------------

def draw_grid(
    pattern,
    x,
    y,
    screen,
    editable=False
):

    for row in range(grid_size):

        for col in range(grid_size):

            rect = pygame.Rect(

                x + col * CELL_SIZE,

                y + row * CELL_SIZE,

                CELL_SIZE,

                CELL_SIZE
            )


            # خانه

            if pattern[row][col] == 1:

                pygame.draw.rect(
                    screen,
                    ACTIVE_COLOR,
                    rect.inflate(-6, -6),
                    border_radius=8
                )

            else:

                pygame.draw.rect(
                    screen,
                    EMPTY_COLOR,
                    rect.inflate(-6, -6),
                    border_radius=8
                )


            # خط دور

            pygame.draw.rect(
                screen,
                GRID_COLOR,
                rect,
                2,
                border_radius=8
            )


# --------------------------------------------------
# Start
# --------------------------------------------------




    # --------------------------------------------------
    # Timer
    # --------------------------------------------------
def MIRROR_(screen):
    global game_over
    global message
    global target_pattern
    global player_pattern
    global score
    global level
    global grid_size



    if not game_over:

        elapsed = time.time() - start_time

        remaining = TIME_LIMIT - elapsed


        if remaining <= 0:

            game_over = True

            message = "TIME OUT!"


    else:

        remaining = 0


    # --------------------------------------------------
    # Title
    # --------------------------------------------------

    title = fonts["heart"].render(
        "MIRROR PATTERN",
        True,
        WHITE
    )

    screen.blit(
        title,
        (350, 40)
    )


    # --------------------------------------------------
    # Left label
    # --------------------------------------------------

    left_text = fonts["heart"].render(
        "PATTERN",
        True,
        WHITE
    )

    screen.blit(
        left_text,
        (LEFT_X + 20, 135)
    )


    # --------------------------------------------------
    # Right label
    # --------------------------------------------------

    right_text = fonts["heart"].render(
        "MIRROR",
        True,
        WHITE
    )

    screen.blit(
        right_text,
        (RIGHT_X + 20, 135)
    )


    # --------------------------------------------------
    # Mirror line
    # --------------------------------------------------

    line_x = (
        LEFT_X
        +
        grid_size * CELL_SIZE
        +
        110
    )

    pygame.draw.line(
        screen,
        MIRROR_COLOR,
        (line_x, GRID_Y - 20),
        (
            line_x,
            GRID_Y + grid_size * CELL_SIZE + 20
        ),
        4
    )


    # --------------------------------------------------
    # Draw grids
    # --------------------------------------------------

    draw_grid(
        target_pattern,
        LEFT_X,
        GRID_Y,
        screen
    )


    draw_grid(
        player_pattern,
        RIGHT_X,
        GRID_Y,
        screen,
        True
    )


    # --------------------------------------------------
    # UI
    # --------------------------------------------------

    score_text = fonts["heart"].render(
        f"Score: {score}",
        True,
        WHITE
    )

    screen.blit(
        score_text,
        (30, 30)
    )


    level_text = fonts["heart"].render(
        f"Level: {level}",
        True,
        WHITE
    )

    screen.blit(
        level_text,
        (30, 65)
    )


    time_text = fonts["heart"].render(
        f"Time: {max(0, int(remaining))}",
        True,
        WHITE
    )

    screen.blit(
        time_text,
        (800, 30)
    )


    # --------------------------------------------------
    # Message
    # --------------------------------------------------

    if message:

        message_text = fonts["heart"].render(
            message,
            True,
            WHITE
        )

        screen.blit(
            message_text,
            (450, 620)
        )


    # --------------------------------------------------
    # Game over
    # --------------------------------------------------

    if game_over:

        overlay = pygame.Surface(
            (WIDTH, HEIGHT),
            pygame.SRCALPHA
        )

        overlay.fill(
            (0, 0, 0, 150)
        )

        screen.blit(
            overlay,
            (0, 0)
        )


        game_over_text = fonts["heart"].render(
            "GAME OVER",
            True,
            WHITE
        )

        screen.blit(
            game_over_text,
            (380, 250)
        )


        result_text = fonts["heart"].render(
            f"Score: {score}    Press R to Restart",
            True,
            WHITE
        )

        screen.blit(
            result_text,
            (300, 310)
        )



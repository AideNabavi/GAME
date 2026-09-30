import pygame
import random

from modules.font import *


WIDTH = 1080
HEIGHT = 720
screen = None


def WIDTH_HEIGHT_gettter(screen_, WIDTH_, HEIGHT_):

    global WIDTH
    global HEIGHT
    global screen

    WIDTH = WIDTH_
    HEIGHT = HEIGHT_
    screen = screen_

# ============================================================
# COLORS
# ============================================================

BACKGROUND = (20, 23, 32)

POINT_COLOR = (80, 170, 255)
POINT_ACTIVE = (90, 220, 140)

LINE_COLOR = (80, 170, 255)
PLAYER_LINE_COLOR = (255, 190, 70)

WHITE = (245, 245, 245)
GRAY = (150, 155, 165)

RED = (230, 70, 80)
GREEN = (70, 210, 120)


# ============================================================
# GAME SETTINGS
# ============================================================

POINT_RADIUS = 14
CLICK_RADIUS = 32

LINE_WIDTH = 6
PLAYER_LINE_WIDTH = 7

SHOW_TIME = 1200
RESULT_TIME = 900


# ============================================================
# GAME STATE
# ============================================================

level = 1
score = 0

state = "SHOW"


# ============================================================
# PATH
# ============================================================

path = []
player_path = []

current_player_point = 0


# ============================================================
# TIMERS
# ============================================================

show_start_time = 0
result_start_time = 0


# ============================================================
# RESULT
# ============================================================

result_text = ""
result_color = WHITE


# ============================================================
# DRAW TEXT
# ============================================================

def draw_text(
    screen,
    value,
    font,
    color,
    center
):

    surface = font.render(
        str(value),
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


# ============================================================
# DISTANCE
# ============================================================

def distance(p1, p2):

    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]

    return (dx * dx + dy * dy) ** 0.5


# ============================================================
# CREATE PATH
# ============================================================

def create_path():

    global path
    global player_path
    global current_player_point
    global state
    global show_start_time

    number_of_points = level + 1

    path = []

    attempts = 0

    # --------------------------------------------------------
    # Create random points
    # --------------------------------------------------------

    while len(path) < number_of_points:

        attempts += 1

        if attempts > 10000:
            break

        x = random.randint(
            100,
            WIDTH - 100
        )

        y = random.randint(
            160,
            HEIGHT - 100
        )

        new_point = (x, y)

        # ----------------------------------------------------
        # Keep points separated
        # ----------------------------------------------------

        valid = True

        for old_point in path:

            if distance(
                new_point,
                old_point
            ) < 80:

                valid = False
                break

        if valid:

            path.append(new_point)

    # --------------------------------------------------------
    # Reset player
    # --------------------------------------------------------

    player_path = []

    current_player_point = 0

    # --------------------------------------------------------
    # Start SHOW
    # --------------------------------------------------------

    state = "SHOW"

    show_start_time = pygame.time.get_ticks()


# ============================================================
# RESET GAME
# ============================================================

def reset_game():

    global level
    global score
    global state
    global result_text
    global result_color

    level = 1
    score = 0

    state = "SHOW"

    result_text = ""
    result_color = WHITE

    create_path()


# ============================================================
# DRAW HEADER
# ============================================================

def draw_header(
    screen,
    WIDTH
):

    draw_text(
        screen,
        "PATH MEMORY",
        fonts["heart"],
        WHITE,
        (
            WIDTH // 2,
            45
        )
    )

    draw_text(
        screen,
        "Level " + str(level),
        fonts["heart"],
        WHITE,
        (
            80,
            45
        )
    )

    draw_text(
        screen,
        "Score: " + str(score),
        fonts["heart"],
        WHITE,
        (
            WIDTH - 100,
            45
        )
    )


# ============================================================
# DRAW POINT
# ============================================================

def draw_point(
    screen,
    point,
    color
):

    pygame.draw.circle(
        screen,
        color,
        point,
        POINT_RADIUS
    )

    pygame.draw.circle(
        screen,
        WHITE,
        point,
        POINT_RADIUS,
        2
    )


# ============================================================
# DRAW ORIGINAL PATH
# ============================================================

def draw_original_path(screen):

    if len(path) < 2:
        return

    for i in range(len(path) - 1):

        pygame.draw.line(
            screen,
            LINE_COLOR,
            path[i],
            path[i + 1],
            LINE_WIDTH
        )


# ============================================================
# DRAW PLAYER PATH
# ============================================================

def draw_player_path(screen):

    if len(player_path) < 2:
        return

    for i in range(len(player_path) - 1):

        pygame.draw.line(
            screen,
            PLAYER_LINE_COLOR,
            player_path[i],
            player_path[i + 1],
            PLAYER_LINE_WIDTH
        )


# ============================================================
# DRAW SHOW
# ============================================================

def draw_show(
    screen,
    WIDTH,
    HEIGHT
):

    screen.fill(BACKGROUND)

    draw_header(
        screen,
        WIDTH
    )

    draw_text(
        screen,
        "MEMORIZE THE PATH",
        fonts["heart"],
        LINE_COLOR,
        (
            WIDTH // 2,
            105
        )
    )

    # --------------------------------------------------------
    # Original path
    # --------------------------------------------------------

    draw_original_path(screen)

    # --------------------------------------------------------
    # Points
    # --------------------------------------------------------

    for i, point in enumerate(path):

        draw_point(
            screen,
            point,
            POINT_COLOR
        )

        draw_text(
            screen,
            i + 1,
            fonts["heart"],
            WHITE,
            (
                point[0],
                point[1] - 30
            )
        )


# ============================================================
# DRAW PLAY
# ============================================================

def draw_play(
    screen,
    WIDTH,
    HEIGHT
):

    screen.fill(BACKGROUND)

    draw_header(
        screen,
        WIDTH
    )

    draw_text(
        screen,
        "REPEAT THE PATH",
        fonts["heart"],
        PLAYER_LINE_COLOR,
        (
            WIDTH // 2,
            105
        )
    )

    # --------------------------------------------------------
    # Player path
    # --------------------------------------------------------

    draw_player_path(screen)

    # --------------------------------------------------------
    # Points
    # --------------------------------------------------------

    for i, point in enumerate(path):

        if i < len(player_path):

            color = POINT_ACTIVE

        elif i == current_player_point:

            color = POINT_COLOR

        else:

            color = GRAY

        draw_point(
            screen,
            point,
            color
        )

    # --------------------------------------------------------
    # Progress
    # --------------------------------------------------------

    draw_text(
        screen,
        f"{len(player_path)} / {len(path)}",
        fonts["heart"],
        WHITE,
        (
            WIDTH // 2,
            HEIGHT - 45
        )
    )


# ============================================================
# DRAW RESULT
# ============================================================

def draw_result(
    screen,
    WIDTH,
    HEIGHT
):

    screen.fill(BACKGROUND)

    draw_header(
        screen,
        WIDTH
    )

    draw_text(
        screen,
        result_text,
        fonts["heart"],
        result_color,
        (
            WIDTH // 2,
            HEIGHT // 2
        )
    )


# ============================================================
# FIND POINT
# ============================================================

def find_point(mouse_position):

    for index, point in enumerate(path):

        if distance(
            mouse_position,
            point
        ) <= CLICK_RADIUS:

            return index

    return None


# ============================================================
# SELECT POINT
# ============================================================

def select_point(index):

    global current_player_point
    global state
    global score
    global result_text
    global result_color
    global result_start_time

    # --------------------------------------------------------
    # Already selected
    # --------------------------------------------------------

    if index in player_path:
        return

    # --------------------------------------------------------
    # Correct
    # --------------------------------------------------------

    if index == current_player_point:

        player_path.append(
            path[index]
        )

        current_player_point += 1

        # ----------------------------------------------------
        # Complete
        # ----------------------------------------------------

        if current_player_point >= len(path):

            score += level * 100

            result_text = "CORRECT!"
            result_color = GREEN

            result_start_time = pygame.time.get_ticks()

            state = "RESULT"

    # --------------------------------------------------------
    # Wrong
    # --------------------------------------------------------

    else:

        result_text = "WRONG!"
        result_color = RED

        result_start_time = pygame.time.get_ticks()

        state = "RESULT"


# ============================================================
# MAIN GAME FUNCTION
# ============================================================

def FOLLOW_THAT_(screen):

    global state
    global level

    WIDTH, HEIGHT = screen.get_size()

    # --------------------------------------------------------
    # SHOW
    # --------------------------------------------------------

    if state == "SHOW":

        now = pygame.time.get_ticks()

        if now - show_start_time >= SHOW_TIME:

            state = "PLAY"

        draw_show(
            screen,
            WIDTH,
            HEIGHT
        )

    # --------------------------------------------------------
    # PLAY
    # --------------------------------------------------------

    elif state == "PLAY":

        draw_play(
            screen,
            WIDTH,
            HEIGHT
        )

    # --------------------------------------------------------
    # RESULT
    # --------------------------------------------------------

    elif state == "RESULT":

        draw_result(
            screen,
            WIDTH,
            HEIGHT
        )

        now = pygame.time.get_ticks()

        if now - result_start_time >= RESULT_TIME:

            if result_text == "CORRECT!":

                level += 1

            create_path()
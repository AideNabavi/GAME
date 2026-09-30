import pygame
import random
import os
import math

from modules.font import  *


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

# =========================================================
# SETTINGS
# =========================================================

# WIDTH = 1200
# HEIGHT = 800

# FPS = 60

ROWS = 8
COLS = 8

CELL_SIZE = 150

BOARD_WIDTH = COLS * CELL_SIZE
BOARD_HEIGHT = ROWS * CELL_SIZE

BOARD_X = (WIDTH  ) // 2
BOARD_Y = (HEIGHT ) // 2

IMAGE_FOLDER = "/Users/mac/Desktop/app/asset/image/MODE/memory_detect"


# =========================================================
# GAME SETTINGS
# =========================================================

START_TIME = 60

TIME_PER_THREE = 2

MAX_TIME = 120

SWAP_DURATION = 180

REMOVE_DURATION = 220

FALL_DURATION = 260

SPAWN_DURATION = 280


# =========================================================
# COLORS
# =========================================================

WHITE = (255, 255, 255)
BLACK = (25, 25, 25)

GRAY = (150, 150, 150)
LIGHT_GRAY = (225, 225, 225)

GREEN = (70, 200, 110)
RED = (220, 70, 70)

YELLOW = (240, 195, 60)
BLUE = (70, 140, 220)

BOARD_COLOR = (245, 245, 245)
CELL_COLOR = (0, 0, 0)


# =========================================================
# PYGAME
# =========================================================

# pygame.init()

# screen = pygame.display.set_mode(
#     (WIDTH, HEIGHT)
# )

# pygame.display.set_caption(
#     "MATCH 3"
# )

# clock = pygame.time.Clock()


# font_big = pygame.font.SysFont(
#     "Arial",
#     42,
#     bold=True
# )

# font = pygame.font.SysFont(
#     "Arial",
#     28,
#     bold=True
# )

# font_small = pygame.font.SysFont(
#     "Arial",
#     20,
#     bold=True
# )


# =========================================================
# IMAGES
# =========================================================

images = []


def load_images():

    global images

    images.clear()

    if not os.path.exists(
        IMAGE_FOLDER
    ):

        print(
            "IMAGE FOLDER NOT FOUND:"
        )

        print(
            IMAGE_FOLDER
        )

        return

    valid_extensions = (
        ".png",
        ".jpg",
        ".jpeg",
        ".webp"
    )

    files = []

    for file in os.listdir(
        IMAGE_FOLDER
    ):

        if file.lower().endswith(
            valid_extensions
        ):

            files.append(file)

    files.sort()

    for file in files:

        path = os.path.join(
            IMAGE_FOLDER,
            file
        )

        try:

            image = pygame.image.load(
                path
            ).convert_alpha()

            image = pygame.transform.smoothscale(
                image,
                (
                    CELL_SIZE - 10,
                    CELL_SIZE - 10
                )
            )

            images.append(
                image
            )

        except Exception as e:

            print(
                "IMAGE ERROR:",
                file,
                e
            )

    print(
        "Loaded images:",
        len(images)
    )


# =========================================================
# BOARD
#
# board[row][col] = image index
# None = empty
# =========================================================

board = []


# =========================================================
# GAME STATE
# =========================================================

score = 0

remaining_time = START_TIME

selected_cell = None

game_over = False

game_busy = False


# =========================================================
# ANIMATION STATE
# =========================================================

animation = None

animation_start = 0

animation_data = {}


# =========================================================
# COMBO
# =========================================================

combo = 0


# =========================================================
# TIMER
# =========================================================

last_timer_tick = 0


# =========================================================
# EASING
# =========================================================

def ease_out_cubic(t):

    t = max(
        0.0,
        min(
            1.0,
            t
        )
    )

    return 1 - (1 - t) ** 3


def ease_in_out(t):

    t = max(
        0.0,
        min(
            1.0,
            t
        )
    )

    return (
        3 * t * t
        - 2 * t * t * t
    )


# =========================================================
# BOARD CREATION
# =========================================================

def create_board():

    global board

    board = [
        [
            None
            for _ in range(COLS)
        ]
        for _ in range(ROWS)
    ]

    for row in range(ROWS):

        for col in range(COLS):

            choices = list(
                range(len(images))
            )

            # ---------------------------------------------
            # Prevent immediate horizontal match
            # ---------------------------------------------

            if col >= 2:

                a = board[row][col - 1]

                b = board[row][col - 2]

                if (
                    a == b
                    and a in choices
                ):

                    choices.remove(a)

            # ---------------------------------------------
            # Prevent immediate vertical match
            # ---------------------------------------------

            if row >= 2:

                a = board[row - 1][col]

                b = board[row - 2][col]

                if (
                    a == b
                    and a in choices
                ):

                    if a in choices:

                        choices.remove(a)

            board[row][col] = random.choice(
                choices
            )


# =========================================================
# FIND MATCHES
# =========================================================

def find_matches():

    matches = set()

    # =====================================================
    # HORIZONTAL
    # =====================================================

    for row in range(ROWS):

        col = 0

        while col < COLS:

            value = board[row][col]

            if value is None:

                col += 1

                continue

            start = col

            col += 1

            while (
                col < COLS
                and board[row][col] == value
            ):

                col += 1

            length = col - start

            if length >= 3:

                for c in range(
                    start,
                    col
                ):

                    matches.add(
                        (row, c)
                    )

    # =====================================================
    # VERTICAL
    # =====================================================

    for col in range(COLS):

        row = 0

        while row < ROWS:

            value = board[row][col]

            if value is None:

                row += 1

                continue

            start = row

            row += 1

            while (
                row < ROWS
                and board[row][col] == value
            ):

                row += 1

            length = row - start

            if length >= 3:

                for r in range(
                    start,
                    row
                ):

                    matches.add(
                        (r, col)
                    )

    return matches


# =========================================================
# CELL CENTER
# =========================================================

def cell_center(
    row,
    col
):

    return (
        BOARD_X
        + col * CELL_SIZE
        + CELL_SIZE // 2,

        BOARD_Y
        + row * CELL_SIZE
        + CELL_SIZE // 2
    )


# =========================================================
# DRAW ONE IMAGE
# =========================================================

def draw_image_at(
    image_index,
    center,
    scale=1.0,
    alpha=255
):

    if image_index is None:
        return

    image = images[
        image_index
    ]

    if scale != 1.0:

        width = max(
            1,
            int(image.get_width() * scale)
        )

        height = max(
            1,
            int(image.get_height() * scale)
        )

        image = pygame.transform.smoothscale(
            image,
            (
                width,
                height
            )
        )

    if alpha != 255:

        image = image.copy()

        image.set_alpha(
            int(alpha)
        )

    rect = image.get_rect(
        center=(
            int(center[0]),
            int(center[1])
        )
    )

    screen.blit(
        image,
        rect
    )


# =========================================================
# DRAW BOARD BACKGROUND
# =========================================================

def draw_board_background():

    board_rect = pygame.Rect(
        BOARD_X,
        BOARD_Y,
        BOARD_WIDTH,
        BOARD_HEIGHT
    )

    pygame.draw.rect(
        screen,
        BOARD_COLOR,
        board_rect,
        border_radius=14
    )

    for row in range(ROWS):

        for col in range(COLS):

            x = (
                BOARD_X
                + col * CELL_SIZE
            )

            y = (
                BOARD_Y
                + row * CELL_SIZE
            )

            rect = pygame.Rect(
                x,
                y,
                CELL_SIZE,
                CELL_SIZE
            )

            pygame.draw.rect(
                screen,
                CELL_COLOR,
                rect,
                border_radius=8
            )

            pygame.draw.rect(
                screen,
                WHITE,
                rect,
                2,
                border_radius=8
            )

    pygame.draw.rect(
        screen,
        GRAY,
        board_rect,
        3,
        border_radius=14
    )


# =========================================================
# DRAW NORMAL BOARD
# =========================================================

def draw_normal_board():

    for row in range(ROWS):

        for col in range(COLS):

            value = board[row][col]

            if value is None:
                continue

            center = cell_center(
                row,
                col
            )

            draw_image_at(
                value,
                center
            )


# =========================================================
# GET CELL FROM MOUSE
# =========================================================

def get_cell_from_mouse(
    pos
):

    mouse_x, mouse_y = pos

    if not (
        BOARD_X
        <= mouse_x
        < BOARD_X + BOARD_WIDTH
    ):

        return None

    if not (
        BOARD_Y
        <= mouse_y
        < BOARD_Y + BOARD_HEIGHT
    ):

        return None

    col = (
        mouse_x - BOARD_X
    ) // CELL_SIZE

    row = (
        mouse_y - BOARD_Y
    ) // CELL_SIZE

    return (
        row,
        col
    )


# =========================================================
# ADJACENT
# =========================================================

def is_adjacent(
    first,
    second
):

    r1, c1 = first

    r2, c2 = second

    return (
        abs(r1 - r2)
        + abs(c1 - c2)
        == 1
    )


# =========================================================
# SWAP
# =========================================================

def swap_cells(
    first,
    second
):

    r1, c1 = first

    r2, c2 = second

    board[r1][c1], board[r2][c2] = (
        board[r2][c2],
        board[r1][c1]
    )


# =========================================================
# START SWAP ANIMATION
# =========================================================

def start_swap_animation(
    first,
    second
):

    global animation
    global animation_start
    global animation_data
    global game_busy

    r1, c1 = first

    r2, c2 = second

    value1 = board[r1][c1]

    value2 = board[r2][c2]

    # -----------------------------------------------------
    # Temporarily swap board
    # -----------------------------------------------------

    swap_cells(
        first,
        second
    )

    animation = "SWAP"

    animation_start = pygame.time.get_ticks()

    animation_data = {

        "first": first,

        "second": second,

        "value1": value1,

        "value2": value2,

    }

    game_busy = True


# =========================================================
# START REMOVE ANIMATION
# =========================================================

def start_remove_animation(
    matches
):

    global animation
    global animation_start
    global animation_data
    global game_busy

    animation = "REMOVE"

    animation_start = pygame.time.get_ticks()

    animation_data = {

        "matches": list(matches)

    }

    game_busy = True


# =========================================================
# REMOVE MATCHES FROM BOARD
# =========================================================

def actually_remove_matches(
    matches
):

    global score
    global remaining_time
    global combo

    count = len(matches)

    if count <= 0:
        return

    # -----------------------------------------------------
    # SCORE
    # -----------------------------------------------------

    score += count * 10

    # -----------------------------------------------------
    # TIME
    #
    # Every 3 removed pieces = +2 seconds
    # -----------------------------------------------------

    bonus = (
        count // 3
    ) * TIME_PER_THREE

    remaining_time += bonus

    if remaining_time > MAX_TIME:

        remaining_time = MAX_TIME

    # -----------------------------------------------------
    # REMOVE
    # -----------------------------------------------------

    for row, col in matches:

        board[row][col] = None


# =========================================================
# COLLAPSE BOARD
# =========================================================

def prepare_collapse():

    movements = []

    for col in range(COLS):

        write_row = ROWS - 1

        for row in range(
            ROWS - 1,
            -1,
            -1
        ):

            value = board[row][col]

            if value is not None:

                if row != write_row:

                    movements.append({

                        "value": value,

                        "from": cell_center(
                            row,
                            col
                        ),

                        "to": cell_center(
                            write_row,
                            col
                        ),

                        "row": write_row,

                        "col": col

                    })

                else:

                    movements.append({

                        "value": value,

                        "from": cell_center(
                            row,
                            col
                        ),

                        "to": cell_center(
                            write_row,
                            col
                        ),

                        "row": write_row,

                        "col": col

                    })

                write_row -= 1

    # -----------------------------------------------------
    # Create empty board
    # -----------------------------------------------------

    new_board = [
        [
            None
            for _ in range(COLS)
        ]
        for _ in range(ROWS)
    ]

    # -----------------------------------------------------
    # Place existing pieces
    # -----------------------------------------------------

    for movement in movements:

        new_board[
            movement["row"]
        ][
            movement["col"]
        ] = movement["value"]

    # -----------------------------------------------------
    # Count empty spaces
    # -----------------------------------------------------

    spawn_data = []

    for col in range(COLS):

        empty_count = 0

        for row in range(ROWS):

            if new_board[row][col] is None:

                empty_count += 1

        for i in range(empty_count):

            target_row = i

            value = random.randrange(
                len(images)
            )

            new_board[
                target_row
            ][
                col
            ] = value

            spawn_data.append({

                "value": value,

                "target": cell_center(
                    target_row,
                    col
                ),

                "start": (
                    BOARD_X
                    + col * CELL_SIZE
                    + CELL_SIZE // 2,

                    BOARD_Y
                    - (
                        empty_count - i
                    ) * CELL_SIZE
                    - CELL_SIZE // 2
                )

            })

    return (
        new_board,
        movements,
        spawn_data
    )


# =========================================================
# START FALL ANIMATION
# =========================================================

def start_fall_animation():

    global animation
    global animation_start
    global animation_data
    global board
    global game_busy

    new_board, movements, spawn_data = (
        prepare_collapse()
    )

    board = new_board

    animation = "FALL"

    animation_start = pygame.time.get_ticks()

    animation_data = {

        "movements": movements,

        "spawn": spawn_data

    }

    game_busy = True


# =========================================================
# DRAW SWAP ANIMATION
# =========================================================

def draw_swap_animation():

    elapsed = (
        pygame.time.get_ticks()
        - animation_start
    )

    t = min(
        1.0,
        elapsed / SWAP_DURATION
    )

    t = ease_in_out(
        t
    )

    first = animation_data[
        "first"
    ]

    second = animation_data[
        "second"
    ]

    value1 = animation_data[
        "value1"
    ]

    value2 = animation_data[
        "value2"
    ]

    p1 = cell_center(
        first[0],
        first[1]
    )

    p2 = cell_center(
        second[0],
        second[1]
    )

    x1 = (
        p1[0]
        + (p2[0] - p1[0]) * t
    )

    y1 = (
        p1[1]
        + (p2[1] - p1[1]) * t
    )

    x2 = (
        p2[0]
        + (p1[0] - p2[0]) * t
    )

    y2 = (
        p2[1]
        + (p1[1] - p2[1]) * t
    )

    draw_image_at(
        value1,
        (x2, y2)
    )

    draw_image_at(
        value2,
        (x1, y1)
    )

    return t >= 1.0


# =========================================================
# DRAW REMOVE ANIMATION
# =========================================================

def draw_remove_animation():

    elapsed = (
        pygame.time.get_ticks()
        - animation_start
    )

    t = min(
        1.0,
        elapsed / REMOVE_DURATION
    )

    for row, col in animation_data[
        "matches"
    ]:

        value = board[row][col]

        # At this point board is still
        # holding the matched value.

        if value is None:
            continue

        scale = 1.0 - ease_in_out(
            t
        )

        alpha = int(
            255
            * (
                1.0 - t
            )
        )

        center = cell_center(
            row,
            col
        )

        draw_image_at(
            value,
            center,
            scale,
            alpha
        )

    return t >= 1.0


# =========================================================
# DRAW FALL ANIMATION
# =========================================================

def draw_fall_animation():

    elapsed = (
        pygame.time.get_ticks()
        - animation_start
    )

    t = min(
        1.0,
        elapsed / FALL_DURATION
    )

    t = ease_out_cubic(
        t
    )

    # -----------------------------------------------------
    # Existing pieces
    # -----------------------------------------------------

    for movement in animation_data[
        "movements"
    ]:

        value = movement[
            "value"
        ]

        start = movement[
            "from"
        ]

        target = movement[
            "to"
        ]

        x = (
            start[0]
            + (
                target[0]
                - start[0]
            ) * t
        )

        y = (
            start[1]
            + (
                target[1]
                - start[1]
            ) * t
        )

        draw_image_at(
            value,
            (x, y)
        )

    # -----------------------------------------------------
    # New pieces
    # -----------------------------------------------------

    for spawn in animation_data[
        "spawn"
    ]:

        start = spawn[
            "start"
        ]

        target = spawn[
            "target"
        ]

        x = (
            start[0]
            + (
                target[0]
                - start[0]
            ) * t
        )

        y = (
            start[1]
            + (
                target[1]
                - start[1]
            ) * t
        )

        draw_image_at(
            spawn["value"],
            (x, y)
        )

    return t >= 1.0


# =========================================================
# FINISH REMOVE
# =========================================================

def finish_remove():

    matches = animation_data[
        "matches"
    ]

    actually_remove_matches(
        matches
    )

    start_fall_animation()


# =========================================================
# FINISH FALL
# =========================================================

def finish_fall():

    global animation
    global game_busy

    animation = None

    game_busy = False

    # -----------------------------------------------------
    # Check chain reaction
    # -----------------------------------------------------

    matches = find_matches()

    if matches:

        start_remove_animation(
            matches
        )


# =========================================================
# UPDATE ANIMATION
# =========================================================

def update_animation():

    global animation
    global animation_start
    global animation_data
    if animation is None:
        return

    # =====================================================
    # SWAP
    # =====================================================

    if animation == "SWAP":

        finished = (
            pygame.time.get_ticks()
            - animation_start
            >= SWAP_DURATION
        )

        if finished:

            matches = find_matches()

            if matches:

                animation = None

                start_remove_animation(
                    matches
                )

            else:

                # -----------------------------------------
                # Invalid move
                # -----------------------------------------

                first = animation_data[
                    "first"
                ]

                second = animation_data[
                    "second"
                ]

                swap_cells(
                    first,
                    second
                )

                animation = None

                # -----------------------------------------
                # Animate return
                # -----------------------------------------

                animation_data = {
                    "first": second,
                    "second": first,

                    "value1":
                        animation_data["value2"],

                    "value2":
                        animation_data["value1"]
                }

                # Start return animation

                animation = "SWAP"

                animation_start = pygame.time.get_ticks()

                # Special flag

                animation_data[
                    "returning"
                ] = True

        return

    # =====================================================
    # REMOVE
    # =====================================================

    if animation == "REMOVE":

        finished = (
            pygame.time.get_ticks()
            - animation_start
            >= REMOVE_DURATION
        )

        if finished:

            finish_remove()

        return

    # =====================================================
    # FALL
    # =====================================================

    if animation == "FALL":

        finished = (
            pygame.time.get_ticks()
            - animation_start
            >= FALL_DURATION
        )

        if finished:

            finish_fall()

        return


# =========================================================
# DRAW ANIMATION
# =========================================================

def draw_animation():

    if animation == "SWAP":

        draw_swap_animation()

    elif animation == "REMOVE":

        draw_remove_animation()

    elif animation == "FALL":

        draw_fall_animation()


# =========================================================
# TRY MOVE
# =========================================================

def try_move(
    first,
    second
):

    global selected_cell

    if game_busy:
        return

    if game_over:
        return

    if not is_adjacent(
        first,
        second
    ):

        selected_cell = second

        return

    start_swap_animation(
        first,
        second
    )

    selected_cell = None


# =========================================================
# TIMER UPDATE
# =========================================================

def update_timer():

    global remaining_time
    global last_timer_tick
    global game_over

    if game_over:
        return

    now = pygame.time.get_ticks()

    if last_timer_tick == 0:

        last_timer_tick = now

        return

    delta_ms = (
        now
        - last_timer_tick
    )

    last_timer_tick = now

    remaining_time -= (
        delta_ms / 1000.0
    )

    if remaining_time <= 0:

        remaining_time = 0

        game_over = True


# =========================================================
# HUD
# =========================================================

def draw_hud():

    # =====================================================
    # SCORE
    # =====================================================

    score_surface = fonts["heart"].render(
        f"SCORE  {score}",
        True,
        BLACK
    )

    screen.blit(
        score_surface,
        (
            35,
            32
        )
    )

    # =====================================================
    # TIME
    # =====================================================

    seconds = max(
        0,
        math.ceil(
            remaining_time
        )
    )

    if seconds <= 10:

        time_color = RED

    elif seconds <= 20:

        time_color = YELLOW

    else:

        time_color = GREEN

    time_surface = fonts["heart"].render(
        f"{seconds}s",
        True,
        time_color
    )

    time_rect = time_surface.get_rect(
        center=(
            WIDTH // 2,
            52
        )
    )

    screen.blit(
        time_surface,
        time_rect
    )

    # =====================================================
    # HELP
    # =====================================================

    help_surface = fonts["heart"].render(
        "CLICK TWO ADJACENT PIECES",
        True,
        GRAY
    )

    help_rect = help_surface.get_rect(
        center=(
            WIDTH // 2,
            HEIGHT - 30
        )
    )

    screen.blit(
        help_surface,
        help_rect
    )


# =========================================================
# SELECTED CELL
# =========================================================

def draw_selected():

    if selected_cell is None:
        return

    row, col = selected_cell

    rect = pygame.Rect(
        BOARD_X
        + col * CELL_SIZE
        + 3,

        BOARD_Y
        + row * CELL_SIZE
        + 3,

        CELL_SIZE - 6,
        CELL_SIZE - 6
    )

    pygame.draw.rect(
        screen,
        YELLOW,
        rect,
        4,
        border_radius=8
    )


# =========================================================
# GAME OVER
# =========================================================

def draw_game_over():

    # overlay = pygame.Surface(
    #     (
    #         WIDTH,
    #         HEIGHT
    #     ),
    #     pygame.SRCALPHA
    # )

    # overlay.fill(
    #     (
    #         0,
    #         0,
    #         0,
    #         170
    #     )
    # )

    # screen.blit(
    #     overlay,
    #     (0, 0)
    # )

    title = fonts["heart"].render(
        "TIME'S UP",
        True,
        WHITE
    )

    title_rect = title.get_rect(
        center=(
            WIDTH // 2,
            HEIGHT // 2 - 70
        )
    )

    screen.blit(
        title,
        title_rect
    )

    score_surface = fonts["heart"].render(
        f"FINAL SCORE  {score}",
        True,
        WHITE
    )

    score_rect = score_surface.get_rect(
        center=(
            WIDTH // 2,
            HEIGHT // 2
        )
    )

    screen.blit(
        score_surface,
        score_rect
    )

    restart_surface = fonts["heart"].render(
        "PRESS R TO PLAY AGAIN",
        True,
        YELLOW
    )

    restart_rect = restart_surface.get_rect(
        center=(
            WIDTH // 2,
            HEIGHT // 2 + 55
        )
    )

    screen.blit(
        restart_surface,
        restart_rect
    )


# =========================================================
# RESET GAME
# =========================================================

def reset_game():

    global score
    global remaining_time
    global selected_cell
    global game_over
    global game_busy
    global animation
    global animation_start
    global animation_data
    global last_timer_tick
    global combo

    score = 0

    remaining_time = START_TIME

    selected_cell = None

    game_over = False

    game_busy = False

    animation = None

    animation_start = 0

    animation_data = {}

    combo = 0

    last_timer_tick = pygame.time.get_ticks()

    create_board()


# =========================================================
# LOAD IMAGES
# =========================================================

load_images()


if len(images) < 3:

    print()
    print(
        "ERROR:"
    )

    print(
        "MATCH-3 NEEDS AT LEAST 3 IMAGES."
    )

    print(
        "IMAGE FOLDER:"
    )

    print(
        IMAGE_FOLDER
    )

    pygame.quit()

    raise SystemExit




def event_MATCH(event):
        global running
        global game_over
        global game_busy
        global selected_cell
        if (
            event.type
            == pygame.MOUSEBUTTONDOWN
            and event.button == 1
        ):

            if (
                not game_over
                and not game_busy
            ):

                cell = get_cell_from_mouse(
                    event.pos
                )

                if cell is not None:

                    # -------------------------------------
                    # First click
                    # -------------------------------------

                    if selected_cell is None:

                        selected_cell = cell

                    # -------------------------------------
                    # Second click
                    # -------------------------------------

                    else:

                        if (
                            cell
                            == selected_cell
                        ):

                            selected_cell = None

                        else:

                            try_move(
                                selected_cell,
                                cell
                            )

        # -------------------------------------------------
        # KEYBOARD
        # -------------------------------------------------

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:

                running = False

            elif event.key == pygame.K_r:

                reset_game()
                
                
def MATCH3_():
    global game_over
    global animation
    global animation_data
    # =====================================================
    # TIMER
    # =====================================================

    update_timer()

    # =====================================================
    # ANIMATION
    # =====================================================

    if not game_over:

        update_animation()

    # =====================================================
    # DRAW
    # =====================================================

    # screen.fill(
    #     WHITE
    # )

    draw_hud()

    draw_board_background()

    # -----------------------------------------------------
    # Normal board
    # -----------------------------------------------------

    if animation is None:

        draw_normal_board()

    else:

        # Draw pieces not involved in animation

        if animation == "SWAP":

            first = animation_data[
                "first"
            ]

            second = animation_data[
                "second"
            ]

            for row in range(ROWS):

                for col in range(COLS):

                    if (
                        (row, col)
                        == first
                        or
                        (row, col)
                        == second
                    ):

                        continue

                    value = board[row][col]

                    if value is not None:

                        draw_image_at(
                            value,
                            cell_center(
                                row,
                                col
                            )
                        )

        elif animation == "REMOVE":

            matches = set(
                animation_data[
                    "matches"
                ]
            )

            for row in range(ROWS):

                for col in range(COLS):

                    if (
                        row,
                        col
                    ) in matches:

                        continue

                    value = board[row][col]

                    if value is not None:

                        draw_image_at(
                            value,
                            cell_center(
                                row,
                                col
                            )
                        )

        elif animation == "FALL":

            # Fall animation draws
            # its own pieces.

            pass

        # -------------------------------------------------
        # Animation itself
        # -------------------------------------------------

        draw_animation()

    # =====================================================
    # SELECTED
    # =====================================================

    if (
        selected_cell is not None
        and not game_busy
    ):

        draw_selected()

    # =====================================================
    # GAME OVER
    # =====================================================

    if game_over:

        # Draw board normally if no animation

        if animation is None:

            pass

        draw_game_over()


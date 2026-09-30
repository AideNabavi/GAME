import pygame
import random
import sys
import math
from modules.font import *
# =========================================================
# SETTINGS
# =========================================================

# 
WIDTH = 1080
HEIGHT = 720

screen = None


# =========================================================
# INITIALIZE SCREEN
# =========================================================

def WIDTH_HEIGHT_gettter(screen_, WIDTH_, HEIGHT_):

    global WIDTH
    global HEIGHT
    global screen

    WIDTH = WIDTH_
    HEIGHT = HEIGHT_

    screen = screen_

# =========================================================
# COLORS
# =========================================================

BG = (18, 20, 27)
GRID_BG = (27, 30, 40)
GRID_LINE = (65, 70, 82)
WHITE = (245, 245, 245)
GRAY = (150, 155, 165)
DARK = (12, 14, 20)

GREEN = (70, 220, 120)
YELLOW = (240, 200, 70)
RED = (235, 80, 80)

# 10 colors
FLOW_COLORS = [
    (235, 75, 75),     # Red
    (65, 170, 255),    # Blue
    (80, 220, 125),    # Green
    (245, 195, 65),    # Yellow
    (190, 100, 240),   # Purple
    (255, 135, 65),    # Orange
    (60, 210, 205),    # Cyan
    (240, 100, 170),   # Pink
    (160, 220, 70),    # Lime
    (245, 245, 245),   # White
]

# =========================================================
# FONTS
# =========================================================

FONT_BIG = fonts["heart"]
FONT_TITLE = fonts["heart"]
FONT_MED = fonts["heart"]
FONT_SMALL = fonts["heart"]
FONT_TIMER = fonts["heart"]

# =========================================================
# LEVELS
# =========================================================

LEVELS = {
    "EASY": {
        "size": 5,
        "pairs": 5,
    },

    "MEDIUM": {
        "size": 7,
        "pairs": 7,
    },

    "HARD": {
        "size": 10,
        "pairs": 10,
    },
}

LEVEL_NAMES = ["EASY", "MEDIUM", "HARD"]

# =========================================================
# GAME STATE
# =========================================================

LEVEL_SELECT = 0
PLAYING = 1
WIN = 2

game_state = LEVEL_SELECT

selected_level = "EASY"

GRID_SIZE = 5

GRID_X = 0
GRID_Y = 0
CELL_SIZE = 100

# =========================================================
# DATA
# =========================================================

# endpoints:
# [
#   {
#       "color": (...),
#       "start": (row, col),
#       "end": (row, col)
#   }
# ]
endpoints = []

# paths:
# color_id -> [(row,col), ...]
paths = {}

# cell owner:
# (row,col) -> color_id
cell_owner = {}

current_color = None
dragging = False

moves = 0

start_time = 0
finish_time = 0

# animation
path_animation = {}

# =========================================================
# TIME
# =========================================================

def reset_time():
    global start_time
    start_time = pygame.time.get_ticks()


def get_elapsed_time():

    if game_state == WIN:
        current = finish_time
    else:
        current = pygame.time.get_ticks()

    return max(0, (current - start_time) // 1000)


# =========================================================
# GRID POSITION
# =========================================================

def calculate_grid():

    global GRID_X
    global GRID_Y
    global CELL_SIZE

    max_grid_width = 680
    max_grid_height = 620

    CELL_SIZE = min(
        max_grid_width // GRID_SIZE,
        max_grid_height // GRID_SIZE
    )

    grid_width = CELL_SIZE * GRID_SIZE
    grid_height = CELL_SIZE * GRID_SIZE

    GRID_X = (WIDTH - grid_width) // 2
    GRID_Y = 120 + (HEIGHT - 120 - grid_height) // 2


# =========================================================
# HAMILTONIAN SNAKE
# =========================================================

def create_snake_path(size):

    cells = []

    for row in range(size):

        if row % 2 == 0:

            for col in range(size):
                cells.append((row, col))

        else:

            for col in range(size - 1, -1, -1):
                cells.append((row, col))

    return cells


# =========================================================
# CREATE GUARANTEED PUZZLE
# =========================================================

def generate_puzzle():

    global endpoints
    global paths
    global cell_owner
    global current_color
    global dragging
    global moves
    global path_animation

    config = LEVELS[selected_level]

    GRID_SIZE = config["size"]
    pair_count = config["pairs"]

    # Update global
    globals()["GRID_SIZE"] = GRID_SIZE

    calculate_grid()

    endpoints = []
    paths = {}
    cell_owner = {}
    path_animation = {}

    current_color = None
    dragging = False
    moves = 0

    # -----------------------------------------------------
    # Create guaranteed full-grid solution
    # -----------------------------------------------------

    snake = create_snake_path(GRID_SIZE)

    # Random segment lengths
    total_cells = len(snake)

    min_length = max(2, total_cells // (pair_count * 2))

    cuts = []

    remaining = total_cells

    for i in range(pair_count):

        left_pairs = pair_count - i - 1

        if left_pairs == 0:
            length = remaining
        else:

            min_remaining = left_pairs * min_length

            max_length = remaining - min_remaining

            length = random.randint(
                min_length,
                max(min_length, max_length)
            )

        cuts.append(length)
        remaining -= length

    # Fix total if needed
    difference = total_cells - sum(cuts)

    cuts[-1] += difference

    # -----------------------------------------------------
    # Randomly rotate/flip snake
    # -----------------------------------------------------

    transform = random.randint(0, 3)

    transformed = []

    for r, c in snake:

        if transform == 0:
            nr, nc = r, c

        elif transform == 1:
            nr, nc = c, GRID_SIZE - 1 - r

        elif transform == 2:
            nr, nc = GRID_SIZE - 1 - r, GRID_SIZE - 1 - c

        else:
            nr, nc = GRID_SIZE - 1 - c, r

        transformed.append((nr, nc))

    snake = transformed

    # -----------------------------------------------------
    # Shuffle colors
    # -----------------------------------------------------

    color_ids = list(range(pair_count))
    random.shuffle(color_ids)

    index = 0

    for pair_index in range(pair_count):

        length = cuts[pair_index]

        segment = snake[index:index + length]

        index += length

        start_cell = segment[0]
        end_cell = segment[-1]

        color_id = color_ids[pair_index]

        endpoints.append({
            "color": FLOW_COLORS[color_id],
            "color_id": color_id,
            "start": start_cell,
            "end": end_cell,
        })

    reset_time()


# =========================================================
# RESET GAME
# =========================================================

def reset_game():

    global game_state

    game_state = PLAYING

    generate_puzzle()


# =========================================================
# CELL RECT
# =========================================================

def get_cell_rect(row, col):

    return pygame.Rect(
        GRID_X + col * CELL_SIZE,
        GRID_Y + row * CELL_SIZE,
        CELL_SIZE,
        CELL_SIZE
    )


# =========================================================
# CELL CENTER
# =========================================================

def get_cell_center(row, col):

    rect = get_cell_rect(row, col)

    return rect.center


# =========================================================
# MOUSE -> CELL
# =========================================================

def mouse_to_cell(pos):

    x, y = pos

    if (
        x < GRID_X
        or y < GRID_Y
        or x >= GRID_X + GRID_SIZE * CELL_SIZE
        or y >= GRID_Y + GRID_SIZE * CELL_SIZE
    ):
        return None

    col = int((x - GRID_X) / CELL_SIZE)
    row = int((y - GRID_Y) / CELL_SIZE)

    return row, col


# =========================================================
# FIND ENDPOINT
# =========================================================

def get_endpoint_color(cell):

    for endpoint in endpoints:

        if (
            endpoint["start"] == cell
            or endpoint["end"] == cell
        ):
            return endpoint["color_id"]

    return None


# =========================================================
# IS ADJACENT
# =========================================================

def is_adjacent(a, b):

    return (
        abs(a[0] - b[0]) +
        abs(a[1] - b[1])
    ) == 1


# =========================================================
# FIND PATH INDEX
# =========================================================

def find_path_index(color_id, cell):

    path = paths.get(color_id, [])

    try:
        return path.index(cell)

    except ValueError:
        return -1


# =========================================================
# START PATH
# =========================================================

def start_path(color_id, cell):

    global current_color
    global dragging
    global moves

    # If path already exists, remove it
    if color_id in paths:

        old_path = paths[color_id]

        for p in old_path:

            if cell_owner.get(p) == color_id:
                del cell_owner[p]

        paths[color_id] = []

    paths[color_id] = [cell]
    cell_owner[cell] = color_id

    current_color = color_id
    dragging = True

    moves += 1


# =========================================================
# CLEAR PATH
# =========================================================

def clear_path(color_id):

    path = paths.get(color_id, [])

    for cell in path:

        if cell_owner.get(cell) == color_id:
            del cell_owner[cell]

    paths[color_id] = []


# =========================================================
# ADD CELL TO PATH
# =========================================================

def add_to_path(color_id, cell):

    path = paths.get(color_id, [])

    if not path:
        return

    last = path[-1]

    if not is_adjacent(last, cell):
        return

    # -----------------------------------------------------
    # Going backwards on own path
    # -----------------------------------------------------

    if cell in path:

        index = path.index(cell)

        removed = path[index + 1:]

        for p in removed:

            if cell_owner.get(p) == color_id:
                del cell_owner[p]

        paths[color_id] = path[:index + 1]

        return

    # -----------------------------------------------------
    # Occupied by another color
    # -----------------------------------------------------

    owner = cell_owner.get(cell)

    if owner is not None:

        if owner != color_id:
            return

    # -----------------------------------------------------
    # Endpoint
    # -----------------------------------------------------

    endpoint_color = get_endpoint_color(cell)

    if endpoint_color is not None:

        if endpoint_color != color_id:
            return

        # correct endpoint
        path.append(cell)
        cell_owner[cell] = color_id

        paths[color_id] = path

        return

    # -----------------------------------------------------
    # Normal cell
    # -----------------------------------------------------

    path.append(cell)
    cell_owner[cell] = color_id

    paths[color_id] = path


# =========================================================
# CHECK COMPLETED CONNECTION
# =========================================================

def is_connection_complete(color_id):

    path = paths.get(color_id, [])

    if len(path) < 2:
        return False

    for endpoint in endpoints:

        if endpoint["color_id"] == color_id:

            a = endpoint["start"]
            b = endpoint["end"]

            return (
                path[0] == a and
                path[-1] == b
            ) or (
                path[0] == b and
                path[-1] == a
            )

    return False


# =========================================================
# CHECK WIN
# =========================================================

def check_win():

    # Every pair must be connected
    for endpoint in endpoints:

        color_id = endpoint["color_id"]

        if not is_connection_complete(color_id):
            return False

    # Every cell must be filled
    total_cells = GRID_SIZE * GRID_SIZE

    if len(cell_owner) != total_cells:
        return False

    return True


# =========================================================
# FINISH
# =========================================================

def finish_game():

    global game_state
    global finish_time

    finish_time = pygame.time.get_ticks()

    game_state = WIN


# =========================================================
# UPDATE
# =========================================================

def update_game():

    if game_state != PLAYING:
        return

    if check_win():
        finish_game()


# =========================================================
# DRAW TEXT
# =========================================================

def draw_center_text(
    text,
    font,
    color,
    center
):

    surface = font.render(
        text,
        True,
        color
    )

    rect = surface.get_rect(
        center=center
    )

    screen.blit(surface, rect)


# =========================================================
# DRAW HEADER
# =========================================================

def draw_header():

    draw_center_text(
        "FLOW FREE",
        FONT_TITLE,
        WHITE,
        (WIDTH // 2, 42)
    )

    # Level
    level_surface = FONT_SMALL.render(
        selected_level,
        True,
        GRAY
    )

    screen.blit(
        level_surface,
        (40, 28)
    )

    # Timer
    seconds = get_elapsed_time()

    minutes = seconds // 60
    sec = seconds % 60

    timer_text = f"{minutes:02d}:{sec:02d}"

    timer_surface = FONT_TIMER.render(
        timer_text,
        True,
        WHITE
    )

    timer_rect = timer_surface.get_rect(
        top=28,
        right=WIDTH - 40
    )

    screen.blit(
        timer_surface,
        timer_rect
    )


# =========================================================
# DRAW GRID
# =========================================================

def draw_grid():

    grid_rect = pygame.Rect(
        GRID_X,
        GRID_Y,
        GRID_SIZE * CELL_SIZE,
        GRID_SIZE * CELL_SIZE
    )

    pygame.draw.rect(
        screen,
        GRID_BG,
        grid_rect,
        border_radius=14
    )

    # Cells
    for row in range(GRID_SIZE):

        for col in range(GRID_SIZE):

            rect = get_cell_rect(row, col)

            pygame.draw.rect(
                screen,
                GRID_LINE,
                rect,
                1
            )


# =========================================================
# DRAW PATH
# =========================================================

def draw_path(color_id, path):

    if not path:
        return

    color = FLOW_COLORS[color_id]

    # -----------------------------------------------------
    # Smooth line
    # -----------------------------------------------------

    points = [
        get_cell_center(r, c)
        for r, c in path
    ]

    if len(points) >= 2:

        pygame.draw.lines(
            screen,
            color,
            False,
            points,
            max(18, CELL_SIZE // 4)
        )

    # -----------------------------------------------------
    # Rounded ends / nodes
    # -----------------------------------------------------

    radius = max(
        10,
        CELL_SIZE // 8
    )

    for point in points:

        pygame.draw.circle(
            screen,
            color,
            point,
            radius
        )


# =========================================================
# DRAW ENDPOINT
# =========================================================

def draw_endpoint(
    center,
    color,
    pulse
):

    # glow
    glow_radius = int(
        CELL_SIZE * 0.25 + pulse
    )

    glow_surface = pygame.Surface(
        (glow_radius * 2 + 10, glow_radius * 2 + 10),
        pygame.SRCALPHA
    )

    alpha = 45

    pygame.draw.circle(
        glow_surface,
        (*color, alpha),
        (
            glow_surface.get_width() // 2,
            glow_surface.get_height() // 2
        ),
        glow_radius
    )

    screen.blit(
        glow_surface,
        (
            center[0] - glow_surface.get_width() // 2,
            center[1] - glow_surface.get_height() // 2
        )
    )

    # Main circle
    radius = max(
        13,
        CELL_SIZE // 7
    )

    pygame.draw.circle(
        screen,
        color,
        center,
        radius
    )

    pygame.draw.circle(
        screen,
        WHITE,
        center,
        radius,
        3
    )


# =========================================================
# DRAW GAME
# =========================================================

def draw_game():

    screen.fill(BG)

    draw_header()

    draw_grid()

    # -----------------------------------------------------
    # Draw all paths
    # -----------------------------------------------------

    for color_id, path in paths.items():

        draw_path(
            color_id,
            path
        )

    # -----------------------------------------------------
    # Draw endpoints
    # -----------------------------------------------------

    pulse = math.sin(
        pygame.time.get_ticks() * 0.005
    ) * 3

    for endpoint in endpoints:

        color = endpoint["color"]

        draw_endpoint(
            get_cell_center(
                *endpoint["start"]
            ),
            color,
            pulse
        )

        draw_endpoint(
            get_cell_center(
                *endpoint["end"]
            ),
            color,
            pulse
        )

    # -----------------------------------------------------
    # Bottom info
    # -----------------------------------------------------

    info = (
        "Drag between matching dots   •   "
        "R = Restart   •   ESC = Level Select"
    )

    draw_center_text(
        info,
        FONT_SMALL,
        GRAY,
        (WIDTH // 2, HEIGHT - 28)
    )


# =========================================================
# LEVEL SELECT
# =========================================================

def draw_level_select():

    screen.fill(BG)

    draw_center_text(
        "FLOW FREE",
        FONT_BIG,
        WHITE,
        (WIDTH // 2, 120)
    )

    draw_center_text(
        "CONNECT ALL PAIRS",
        FONT_SMALL,
        GRAY,
        (WIDTH // 2, 175)
    )

    button_width = 270
    button_height = 100

    gap = 35

    total_width = (
        button_width * 3
        + gap * 2
    )

    start_x = (
        WIDTH - total_width
    ) // 2

    y = 310

    for i, level in enumerate(LEVEL_NAMES):

        x = start_x + i * (
            button_width + gap
        )

        rect = pygame.Rect(
            x,
            y,
            button_width,
            button_height
        )

        mouse_pos = pygame.mouse.get_pos()

        hover = rect.collidepoint(
            mouse_pos
        )

        color = (
            GREEN if i == 0 else
            YELLOW if i == 1 else
            RED
        )

        if hover:

            pygame.draw.rect(
                screen,
                color,
                rect,
                border_radius=18
            )

            text_color = DARK

        else:

            pygame.draw.rect(
                screen,
                (30, 34, 44),
                rect,
                border_radius=18
            )

            pygame.draw.rect(
                screen,
                color,
                rect,
                3,
                border_radius=18
            )

            text_color = WHITE

        draw_center_text(
            level,
            FONT_MED,
            text_color,
            rect.center
        )

        pair_text = (
            f"{LEVELS[level]['pairs']} PAIRS  •  "
            f"{LEVELS[level]['size']}×"
            f"{LEVELS[level]['size']}"
        )

        draw_center_text(
            pair_text,
            FONT_SMALL,
            text_color,
            (
                rect.centerx,
                rect.centery + 28
            )
        )

    draw_center_text(
        "Connect matching colors and fill every cell.",
        FONT_SMALL,
        GRAY,
        (WIDTH // 2, 550)
    )

    draw_center_text(
        "ESC = Quit",
        FONT_SMALL,
        GRAY,
        (WIDTH // 2, 620)
    )


# =========================================================
# WIN SCREEN
# =========================================================

def draw_win():

    screen.fill(BG)

    draw_center_text(
        "PUZZLE COMPLETE!",
        FONT_BIG,
        GREEN,
        (WIDTH // 2, 210)
    )

    seconds = get_elapsed_time()

    minutes = seconds // 60
    sec = seconds % 60

    time_text = (
        f"TIME   {minutes:02d}:{sec:02d}"
    )

    draw_center_text(
        time_text,
        FONT_TITLE,
        WHITE,
        (WIDTH // 2, 310)
    )

    draw_center_text(
        f"MOVES   {moves}",
        FONT_MED,
        GRAY,
        (WIDTH // 2, 365)
    )

    # Restart
    restart_rect = pygame.Rect(
        WIDTH // 2 - 180,
        460,
        360,
        75
    )

    mouse_pos = pygame.mouse.get_pos()

    hover = restart_rect.collidepoint(
        mouse_pos
    )

    if hover:

        pygame.draw.rect(
            screen,
            GREEN,
            restart_rect,
            border_radius=15
        )

        text_color = DARK

    else:

        pygame.draw.rect(
            screen,
            (30, 34, 44),
            restart_rect,
            border_radius=15
        )

        pygame.draw.rect(
            screen,
            GREEN,
            restart_rect,
            2,
            border_radius=15
        )

        text_color = WHITE

    draw_center_text(
        "PLAY AGAIN",
        FONT_MED,
        text_color,
        restart_rect.center
    )

    draw_center_text(
        "ESC = Level Select",
        FONT_SMALL,
        GRAY,
        (WIDTH // 2, 590)
    )


# =========================================================
# EVENT LEVEL SELECT
# =========================================================

def event_level_select(event):

    global selected_level
    global game_state

    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_ESCAPE:

            pygame.quit()
            sys.exit()

        if event.key == pygame.K_1:

            selected_level = "EASY"
            reset_game()

        elif event.key == pygame.K_2:

            selected_level = "MEDIUM"
            reset_game()

        elif event.key == pygame.K_3:

            selected_level = "HARD"
            reset_game()

    if event.type == pygame.MOUSEBUTTONDOWN:

        if event.button != 1:
            return

        button_width = 270
        button_height = 100
        gap = 35

        total_width = (
            button_width * 3
            + gap * 2
        )

        start_x = (
            WIDTH - total_width
        ) // 2

        y = 310

        for i, level in enumerate(LEVEL_NAMES):

            rect = pygame.Rect(
                start_x + i * (
                    button_width + gap
                ),
                y,
                button_width,
                button_height
            )

            if rect.collidepoint(event.pos):

                selected_level = level

                reset_game()

                return


# =========================================================
# EVENT PLAYING
# =========================================================

def event_playing(event):

    global dragging
    global current_color
    global game_state

    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_r:

            reset_game()

            return

        if event.key == pygame.K_ESCAPE:

            dragging = False
            current_color = None
            game_state = LEVEL_SELECT

            return

    # -----------------------------------------------------
    # Mouse down
    # -----------------------------------------------------

    if event.type == pygame.MOUSEBUTTONDOWN:

        if event.button != 1:
            return

        cell = mouse_to_cell(
            event.pos
        )

        if cell is None:
            return

        color_id = get_endpoint_color(
            cell
        )

        # Start from endpoint
        if color_id is not None:

            start_path(
                color_id,
                cell
            )

            return

        # Start from own existing path
        owner = cell_owner.get(cell)

        if owner is not None:

            path = paths.get(
                owner,
                []
            )

            index = find_path_index(
                owner,
                cell
            )

            if index >= 0:

                removed = path[index + 1:]

                for p in removed:

                    if cell_owner.get(p) == owner:
                        del cell_owner[p]

                paths[owner] = path[:index + 1]

                current_color = owner
                dragging = True

    # -----------------------------------------------------
    # Mouse motion
    # -----------------------------------------------------

    elif event.type == pygame.MOUSEMOTION:

        if not dragging:
            return

        if current_color is None:
            return

        cell = mouse_to_cell(
            event.pos
        )

        if cell is None:
            return

        add_to_path(
            current_color,
            cell
        )

    # -----------------------------------------------------
    # Mouse up
    # -----------------------------------------------------

    elif event.type == pygame.MOUSEBUTTONUP:

        if event.button != 1:
            return

        dragging = False
        current_color = None


# =========================================================
# EVENT WIN
# =========================================================

def event_win(event):

    global game_state

    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_r:

            reset_game()

        elif event.key == pygame.K_ESCAPE:

            game_state = LEVEL_SELECT

    if event.type == pygame.MOUSEBUTTONDOWN:

        if event.button != 1:
            return

        restart_rect = pygame.Rect(
            WIDTH // 2 - 180,
            460,
            360,
            75
        )

        if restart_rect.collidepoint(
            event.pos
        ):

            reset_game()


# =========================================================
# MAIN
# =========================================================

def FOLLOW_FREE_():

    global game_state



    # -------------------------------------------------
    # Update
    # -------------------------------------------------

    update_game()

    # -------------------------------------------------
    # Draw
    # -------------------------------------------------

    if game_state == LEVEL_SELECT:

        draw_level_select()

    elif game_state == PLAYING:

        draw_game()

    elif game_state == WIN:

        draw_win()



def event_FOLLOW_FREE(event):
    global game_state
    if game_state == LEVEL_SELECT:

        event_level_select(event)

    elif game_state == PLAYING:

        event_playing(event)

    elif game_state == WIN:

        event_win(event)


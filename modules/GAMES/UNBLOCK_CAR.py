import pygame
import sys
import time
import random

from modules.font import *

# =========================================================
# INIT
# =========================================================

# pygame.init()

WIDTH = 1200
HEIGHT = 850
screen=None


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

BG = (20, 23, 30)
BOARD_BG = (35, 39, 48)

GRID_COLOR = (70, 75, 88)

WHITE = (245, 245, 245)
GRAY = (150, 155, 165)

RED = (220, 55, 55)
RED_LIGHT = (245, 85, 85)

BLUE = (55, 125, 220)
GREEN = (65, 185, 105)
YELLOW = (230, 180, 55)
PURPLE = (145, 85, 205)
ORANGE = (225, 120, 45)
CYAN = (50, 180, 190)

EXIT_COLOR = (80, 220, 120)


# =========================================================
# FONTS
# =========================================================

# FONT_BIG = pygame.font.SysFont(
#     "Arial",
#     48,
#     bold=True
# )

# FONT_TITLE = pygame.font.SysFont(
#     "Arial",
#     42,
#     bold=True
# )

# FONT_MEDIUM = pygame.font.SysFont(
#     "Arial",
#     28,
#     bold=True
# )

# FONT_SMALL = pygame.font.SysFont(
#     "Arial",
#     22
# )


# =========================================================
# CONSTANTS
# =========================================================

GRID_SIZE = 6

TARGET_ROW = 2

ANIMATION_SPEED = 14.0


# =========================================================
# DIFFICULTY
# =========================================================

DIFFICULTY_EASY = "EASY"
DIFFICULTY_MEDIUM = "MEDIUM"
DIFFICULTY_HARD = "HARD"


# =========================================================
# GAME STATES
# =========================================================

MENU = "MENU"
PLAYING = "PLAYING"
WIN = "WIN"

game_state = MENU

selected_difficulty = DIFFICULTY_EASY


# =========================================================
# RANDOM LEVEL SETTINGS
# =========================================================

DIFFICULTY_SETTINGS = {

    DIFFICULTY_EASY: {
        "min_cars": 5,
        "max_cars": 6,

        # Easy mostly uses one direction for each car.
        "allow_mixed_direction": False,

        # More empty cells.
        "min_empty_cells": 10,
    },

    DIFFICULTY_MEDIUM: {
        "min_cars": 7,
        "max_cars": 8,

        "allow_mixed_direction": True,

        "min_empty_cells": 7,
    },

    DIFFICULTY_HARD: {
        "min_cars": 9,
        "max_cars": 11,

        "allow_mixed_direction": True,

        "min_empty_cells": 3,
    }
}


# =========================================================
# CAR COLORS
# =========================================================

CAR_COLORS = [
    BLUE,
    GREEN,
    YELLOW,
    PURPLE,
    ORANGE,
    CYAN,
]


# =========================================================
# RANDOM LAYOUT HISTORY
#
# Keeps recently generated layouts so pressing R does not
# immediately give the same puzzle again.
# =========================================================

generated_layout_history = []

MAX_LAYOUT_HISTORY = 100


# =========================================================
# BOARD GEOMETRY
# =========================================================

def get_board_rect():

    w, h = screen.get_size()

    board_size = min(
        h - 170,
        w - 380
    )

    board_size = max(
        board_size,
        400
    )

    x = (w - board_size) // 2 - 100

    y = 110

    return pygame.Rect(
        x,
        y,
        board_size,
        board_size
    )


def get_cell_size():

    board = get_board_rect()

    return board.width / GRID_SIZE


# =========================================================
# CAR CLASS
# =========================================================

class Car:

    def __init__(
        self,
        name,
        grid_x,
        grid_y,
        length,
        horizontal,
        target=False
    ):

        self.name = name

        self.grid_x = grid_x
        self.grid_y = grid_y

        self.target = target

        self.length = length

        self.horizontal = horizontal

        # Actual animated position
        self.x = float(grid_x)
        self.y = float(grid_y)

        # Animation target
        self.target_x = float(grid_x)
        self.target_y = float(grid_y)

        self.dragging = False

        self.start_drag_position = 0

        self.moved_this_drag = False

    # -----------------------------------------------------
    # UPDATE ANIMATION
    # -----------------------------------------------------

    def update(self, dt):

        dx = self.target_x - self.x
        dy = self.target_y - self.y

        distance = (dx * dx + dy * dy) ** 0.5

        if distance < 0.001:

            self.x = self.target_x
            self.y = self.target_y

            return

        step = ANIMATION_SPEED * dt

        if distance <= step:

            self.x = self.target_x
            self.y = self.target_y

        else:

            self.x += dx / distance * step
            self.y += dy / distance * step

    # -----------------------------------------------------
    # IS ANIMATING
    # -----------------------------------------------------

    def is_animating(self):

        return (
            abs(self.x - self.target_x) > 0.001
            or
            abs(self.y - self.target_y) > 0.001
        )

    # -----------------------------------------------------
    # CELLS
    #
    # Important:
    # This uses target_x / target_y so collision checking
    # works correctly while dragging.
    # -----------------------------------------------------

    def cells(self):

        result = []

        gx = round(self.target_x)
        gy = round(self.target_y)

        if self.horizontal:

            for i in range(self.length):

                result.append(
                    (
                        gx + i,
                        gy
                    )
                )

        else:

            for i in range(self.length):

                result.append(
                    (
                        gx,
                        gy + i
                    )
                )

        return result

    # -----------------------------------------------------
    # DRAW
    # -----------------------------------------------------

    def draw(self, surface):

        board = get_board_rect()

        cell = board.width / GRID_SIZE

        px = board.x + self.x * cell
        py = board.y + self.y * cell

        if self.horizontal:

            width = cell * self.length

            height = cell * 0.82

            rect = pygame.Rect(
                int(px + cell * 0.09),
                int(py + cell * 0.09),
                int(width - cell * 0.18),
                int(height)
            )

        else:

            width = cell * 0.82

            height = cell * self.length

            rect = pygame.Rect(
                int(px + cell * 0.09),
                int(py + cell * 0.09),
                int(width),
                int(height - cell * 0.18)
            )

        if self.target:

            color = RED

        else:

            color = CAR_COLORS[
                ord(self.name[0]) % len(CAR_COLORS)
            ]

        # -------------------------------------------------
        # SHADOW
        # -------------------------------------------------

        shadow = rect.move(
            int(cell * 0.05),
            int(cell * 0.06)
        )

        pygame.draw.rect(
            surface,
            (10, 12, 16),
            shadow,
            border_radius=14
        )

        # -------------------------------------------------
        # BODY
        # -------------------------------------------------

        pygame.draw.rect(
            surface,
            color,
            rect,
            border_radius=14
        )

        # -------------------------------------------------
        # INNER HIGHLIGHT
        # -------------------------------------------------

        inner = rect.inflate(
            -int(cell * 0.12),
            -int(cell * 0.12)
        )

        highlight = tuple(
            min(255, c + 25)
            for c in color
        )

        pygame.draw.rect(
            surface,
            highlight,
            inner,
            3,
            border_radius=10
        )

        # -------------------------------------------------
        # WINDOWS
        # -------------------------------------------------

        if self.horizontal:

            window_width = rect.width * 0.25

            window = pygame.Rect(
                rect.centerx - window_width // 2,
                rect.y + rect.height * 0.18,
                window_width,
                rect.height * 0.35
            )

        else:

            window_height = rect.height * 0.25

            window = pygame.Rect(
                rect.x + rect.width * 0.18,
                rect.centery - window_height // 2,
                rect.width * 0.35,
                window_height
            )

        pygame.draw.rect(
            surface,
            (35, 45, 58),
            window,
            border_radius=5
        )

        # -------------------------------------------------
        # TARGET SYMBOL
        # -------------------------------------------------

        if self.target:

            pygame.draw.circle(
                surface,
                WHITE,
                rect.center,
                max(
                    5,
                    int(cell * 0.08)
                )
            )


# =========================================================
# RANDOM LEVEL GENERATOR
# =========================================================
#
# This is the important part.
#
# We do NOT use LEVELS anymore.
#
# Every call creates a new random layout.
# =========================================================

def get_random_length():

    return random.choice(
        [2, 2, 2, 3]
    )


def get_allowed_orientation():

    settings = DIFFICULTY_SETTINGS[
        selected_difficulty
    ]

    if not settings["allow_mixed_direction"]:

        # Easy:
        # random horizontal / vertical,
        # but later we ensure useful distribution.
        return random.choice(
            [True, False]
        )

    return random.choice(
        [True, False]
    )


# =========================================================
# CHECK CAR POSITION
# =========================================================

def get_cells_for_position(
    x,
    y,
    length,
    horizontal
):

    result = []

    if horizontal:

        for i in range(length):

            result.append(
                (
                    x + i,
                    y
                )
            )

    else:

        for i in range(length):

            result.append(
                (
                    x,
                    y + i
                )
            )

    return result


# =========================================================
# POSITION INSIDE BOARD
# =========================================================

def position_inside_board(
    x,
    y,
    length,
    horizontal
):

    if horizontal:

        if x < 0:
            return False

        if x + length > GRID_SIZE:
            return False

        if y < 0 or y >= GRID_SIZE:
            return False

    else:

        if y < 0:
            return False

        if y + length > GRID_SIZE:
            return False

        if x < 0 or x >= GRID_SIZE:
            return False

    return True


# =========================================================
# COLLISION CHECK
# =========================================================

def position_is_free(
    occupied,
    x,
    y,
    length,
    horizontal
):

    if not position_inside_board(
        x,
        y,
        length,
        horizontal
    ):

        return False

    cells = get_cells_for_position(
        x,
        y,
        length,
        horizontal
    )

    for cell in cells:

        if cell in occupied:

            return False

    return True


# =========================================================
# LAYOUT SIGNATURE
# =========================================================
#
# Used to prevent duplicate layouts.
# =========================================================

def create_layout_signature(
    layout
):

    normalized = []

    for item in layout:

        name, x, y, length, horizontal = item

        normalized.append(
            (
                name,
                x,
                y,
                length,
                horizontal
            )
        )

    return tuple(
        normalized
    )


# =========================================================
# FULL INITIAL COLLISION CHECK
# =========================================================

def validate_generated_layout(
    layout
):

    occupied = set()

    for item in layout:

        name, x, y, length, horizontal = item

        cells = get_cells_for_position(
            x,
            y,
            length,
            horizontal
        )

        # Check board
        for cx, cy in cells:

            if cx < 0 or cx >= GRID_SIZE:
                return False

            if cy < 0 or cy >= GRID_SIZE:
                return False

        # Check collision
        for cell in cells:

            if cell in occupied:

                return False

        for cell in cells:

            occupied.add(cell)

    return True


# =========================================================
# GENERATE RANDOM LAYOUT
# =========================================================

def generate_random_layout():

    settings = DIFFICULTY_SETTINGS[
        selected_difficulty
    ]

    min_cars = settings["min_cars"]
    max_cars = settings["max_cars"]

    # Random number of cars
    car_count = random.randint(
        min_cars,
        max_cars
    )

    # -----------------------------------------------------
    # TARGET
    # -----------------------------------------------------
    #
    # Red car ALWAYS:
    # horizontal
    # row = TARGET_ROW
    # length = 2
    #
    # x is randomized.
    # -----------------------------------------------------

    target_x = random.randint(
        0,
        GRID_SIZE - 2
    )

    layout = [
        (
            "TARGET",
            target_x,
            TARGET_ROW,
            2,
            True
        )
    ]

    occupied = set(
        get_cells_for_position(
            target_x,
            TARGET_ROW,
            2,
            True
        )
    )

    # -----------------------------------------------------
    # OTHER CARS
    # -----------------------------------------------------

    names = list(
        "ABCDEFGHIJKLM"
    )

    random.shuffle(
        names
    )

    horizontal_count = 0
    vertical_count = 0

    attempts = 0

    max_attempts = 3000

    while (
        len(layout) < car_count + 1
        and
        attempts < max_attempts
    ):

        attempts += 1

        name = names[
            len(layout) - 1
        ]

        length = get_random_length()

        horizontal = get_allowed_orientation()

        # -------------------------------------------------
        # Make sure easy does not become all same type.
        # -------------------------------------------------

        if selected_difficulty == DIFFICULTY_EASY:

            if horizontal_count >= 3:

                horizontal = False

            elif vertical_count >= 3:

                horizontal = True

        # -------------------------------------------------
        # Random position
        # -------------------------------------------------

        if horizontal:

            x = random.randint(
                0,
                GRID_SIZE - length
            )

            y = random.randint(
                0,
                GRID_SIZE - 1
            )

        else:

            x = random.randint(
                0,
                GRID_SIZE - 1
            )

            y = random.randint(
                0,
                GRID_SIZE - length
            )

        # -------------------------------------------------
        # Do not place a blocker directly over target.
        # -------------------------------------------------

        if not position_is_free(
            occupied,
            x,
            y,
            length,
            horizontal
        ):

            continue

        # -------------------------------------------------
        # Add car
        # -------------------------------------------------

        layout.append(
            (
                name,
                x,
                y,
                length,
                horizontal
            )
        )

        cells = get_cells_for_position(
            x,
            y,
            length,
            horizontal
        )

        for cell in cells:

            occupied.add(
                cell
            )

        if horizontal:

            horizontal_count += 1

        else:

            vertical_count += 1

    # -----------------------------------------------------
    # Could not generate enough cars
    # -----------------------------------------------------

    if len(layout) != car_count + 1:

        return None

    # -----------------------------------------------------
    # FINAL COLLISION CHECK
    # -----------------------------------------------------

    if not validate_generated_layout(
        layout
    ):

        return None

    # -----------------------------------------------------
    # Make sure it is not exactly the same as a recent
    # generated layout.
    # -----------------------------------------------------

    signature = create_layout_signature(
        layout
    )

    if signature in generated_layout_history:

        return None

    # -----------------------------------------------------
    # Save history
    # -----------------------------------------------------

    generated_layout_history.append(
        signature
    )

    if len(
        generated_layout_history
    ) > MAX_LAYOUT_HISTORY:

        generated_layout_history.pop(
            0
        )

    return layout


# =========================================================
# GENERATE GUARANTEED RANDOM LAYOUT
# =========================================================

def create_new_random_level():

    # Try many times.
    #
    # Usually succeeds very quickly.
    #

    for _ in range(100):

        layout = generate_random_layout()

        if layout is not None:

            return layout

    # -----------------------------------------------------
    # Emergency fallback
    #
    # This is still generated dynamically and collision
    # checked.
    # -----------------------------------------------------

    fallback = [
        (
            "TARGET",
            0,
            TARGET_ROW,
            2,
            True
        ),

        (
            "A",
            2,
            0,
            3,
            False
        ),

        (
            "B",
            3,
            1,
            2,
            False
        ),

        (
            "C",
            4,
            3,
            2,
            False
        ),

        (
            "D",
            0,
            4,
            3,
            True
        ),

        (
            "E",
            3,
            5,
            2,
            True
        ),
    ]

    if validate_generated_layout(
        fallback
    ):

        signature = create_layout_signature(
            fallback
        )

        if signature not in generated_layout_history:

            generated_layout_history.append(
                signature
            )

        return fallback

    return None


# =========================================================
# GAME VARIABLES
# =========================================================

cars = []

current_layout = None

moves = 0

level_start_time = 0

elapsed_time = 0

selected_car = None

win_time = 0


# =========================================================
# RESET GAME
# =========================================================
#
# Every reset:
#
# 1. Clears cars.
# 2. Generates a NEW random level.
# 3. Collision checks it.
# 4. Creates Car objects.
# 5. Resets timer.
#
# =========================================================

def reset_game():

    global cars
    global current_layout
    global moves
    global level_start_time
    global elapsed_time
    global selected_car
    global game_state

    # -----------------------------------------------------
    # Create NEW puzzle
    # -----------------------------------------------------

    current_layout = create_new_random_level()

    # Safety
    if current_layout is None:

        return

    # -----------------------------------------------------
    # Create cars
    # -----------------------------------------------------

    cars = []

    for data in current_layout:

        name, x, y, length, horizontal = data

        target = (
            name == "TARGET"
        )

        cars.append(
            Car(
                name,
                x,
                y,
                length,
                horizontal,
                target
            )
        )

    # -----------------------------------------------------
    # Reset game data
    # -----------------------------------------------------

    moves = 0

    elapsed_time = 0

    level_start_time = time.perf_counter()

    selected_car = None

    game_state = PLAYING


# =========================================================
# RESET TIMER
# =========================================================

def reset_timer():

    global level_start_time
    global elapsed_time

    elapsed_time = 0

    level_start_time = time.perf_counter()


# =========================================================
# GET CAR RECT
# =========================================================

def get_car_rect(car):

    board = get_board_rect()

    cell = board.width / GRID_SIZE

    px = board.x + car.x * cell
    py = board.y + car.y * cell

    if car.horizontal:

        return pygame.Rect(
            int(px),
            int(py),
            int(cell * car.length),
            int(cell)
        )

    return pygame.Rect(
        int(px),
        int(py),
        int(cell),
        int(cell * car.length)
    )


# =========================================================
# BOARD OCCUPANCY
# =========================================================

def occupied_cells(
    ignore_car=None
):

    occupied = set()

    for car in cars:

        if car is ignore_car:

            continue

        for cell in car.cells():

            occupied.add(
                cell
            )

    return occupied


# =========================================================
# VALID MOVE
# =========================================================

def can_move_to(
    car,
    new_x,
    new_y
):

    gx = round(new_x)
    gy = round(new_y)

    # -----------------------------------------------------
    # Boundaries
    # -----------------------------------------------------

    if car.horizontal:

        if gx < 0:

            return False

        if gx + car.length > GRID_SIZE:

            return False

        if gy < 0 or gy >= GRID_SIZE:

            return False

    else:

        if gy < 0:

            return False

        if gy + car.length > GRID_SIZE:

            return False

        if gx < 0 or gx >= GRID_SIZE:

            return False

    # -----------------------------------------------------
    # Collision
    # -----------------------------------------------------

    occupied = occupied_cells(
        ignore_car=car
    )

    if car.horizontal:

        for i in range(
            car.length
        ):

            if (
                gx + i,
                gy
            ) in occupied:

                return False

    else:

        for i in range(
            car.length
        ):

            if (
                gx,
                gy + i
            ) in occupied:

                return False

    return True


# =========================================================
# MOUSE -> GRID
# =========================================================

def mouse_to_grid():

    board = get_board_rect()

    cell = board.width / GRID_SIZE

    mx, my = pygame.mouse.get_pos()

    gx = (
        mx - board.x
    ) / cell

    gy = (
        my - board.y
    ) / cell

    return gx, gy


# =========================================================
# START DRAG
# =========================================================

def start_drag(pos):

    global selected_car

    # Do not start another movement while cars animate.
    if any(
        car.is_animating()
        for car in cars
    ):

        return

    for car in reversed(cars):

        rect = get_car_rect(
            car
        )

        if rect.collidepoint(
            pos
        ):

            selected_car = car

            car.dragging = True

            if car.horizontal:

                car.start_drag_position = car.x

            else:

                car.start_drag_position = car.y

            return


# =========================================================
# DRAG CAR
# =========================================================

def drag_car(pos):

    global selected_car

    if selected_car is None:

        return

    car = selected_car

    board = get_board_rect()

    cell = board.width / GRID_SIZE

    mx, my = pos

    gx = (
        mx - board.x
    ) / cell

    gy = (
        my - board.y
    ) / cell

    # -----------------------------------------------------
    # HORIZONTAL CAR
    # -----------------------------------------------------

    if car.horizontal:

        desired_x = (
            gx
            -
            car.length / 2
            +
            0.5
        )

        min_x = 0

        max_x = (
            GRID_SIZE
            -
            car.length
        )

        desired_x = max(
            min_x,
            min(
                max_x,
                desired_x
            )
        )

        if can_move_to(
            car,
            desired_x,
            car.grid_y
        ):

            car.target_x = desired_x

            car.x = desired_x

            if (
                abs(
                    car.x
                    -
                    car.start_drag_position
                ) > 0.15
            ):

                car.moved_this_drag = True

    # -----------------------------------------------------
    # VERTICAL CAR
    # -----------------------------------------------------

    else:

        desired_y = (
            gy
            -
            car.length / 2
            +
            0.5
        )

        min_y = 0

        max_y = (
            GRID_SIZE
            -
            car.length
        )

        desired_y = max(
            min_y,
            min(
                max_y,
                desired_y
            )
        )

        if can_move_to(
            car,
            car.grid_x,
            desired_y
        ):

            car.target_y = desired_y

            car.y = desired_y

            if (
                abs(
                    car.y
                    -
                    car.start_drag_position
                ) > 0.15
            ):

                car.moved_this_drag = True


# =========================================================
# END DRAG
# =========================================================

def end_drag():

    global selected_car
    global moves

    if selected_car is None:

        return

    car = selected_car

    car.dragging = False

    # -----------------------------------------------------
    # Horizontal
    # -----------------------------------------------------

    if car.horizontal:

        final_x = round(
            car.target_x
        )

        if can_move_to(
            car,
            final_x,
            car.grid_y
        ):

            if final_x != car.grid_x:

                moves += 1

            car.grid_x = final_x

            car.target_x = float(
                final_x
            )

            car.x = float(
                final_x
            )

        else:

            car.target_x = float(
                car.grid_x
            )

            car.x = float(
                car.grid_x
            )

    # -----------------------------------------------------
    # Vertical
    # -----------------------------------------------------

    else:

        final_y = round(
            car.target_y
        )

        if can_move_to(
            car,
            car.grid_x,
            final_y
        ):

            if final_y != car.grid_y:

                moves += 1

            car.grid_y = final_y

            car.target_y = float(
                final_y
            )

            car.y = float(
                final_y
            )

        else:

            car.target_y = float(
                car.grid_y
            )

            car.y = float(
                car.grid_y
            )

    car.moved_this_drag = False

    selected_car = None

    check_win()


# =========================================================
# CHECK WIN
# =========================================================

def check_win():

    global game_state
    global win_time

    target = None

    for car in cars:

        if car.target:

            target = car

            break

    if target is None:

        return

    # -----------------------------------------------------
    # Target must stay in exit row
    # -----------------------------------------------------

    if target.grid_y != TARGET_ROW:

        return

    # -----------------------------------------------------
    # Check path to right edge
    # -----------------------------------------------------

    occupied = occupied_cells(
        ignore_car=target
    )

    start = (
        target.grid_x
        +
        target.length
    )

    clear = True

    for x in range(
        start,
        GRID_SIZE
    ):

        if (
            x,
            TARGET_ROW
        ) in occupied:

            clear = False

            break

    if clear:

        # Move target outside board
        target.target_x = 6.0

        game_state = WIN

        win_time = time.perf_counter()


# =========================================================
# DRAW BOARD
# =========================================================

def draw_board():

    board = get_board_rect()

    pygame.draw.rect(
        screen,
        BOARD_BG,
        board,
        border_radius=18
    )

    cell = (
        board.width
        /
        GRID_SIZE
    )

    # -----------------------------------------------------
    # EXIT
    # -----------------------------------------------------

    exit_rect = pygame.Rect(
        board.right - 8,
        int(
            board.y
            +
            TARGET_ROW * cell
        ),
        20,
        int(cell)
    )

    pygame.draw.rect(
        screen,
        EXIT_COLOR,
        exit_rect,
        border_radius=8
    )

    # -----------------------------------------------------
    # GRID
    # -----------------------------------------------------

    for i in range(
        GRID_SIZE + 1
    ):

        x = int(
            board.x
            +
            i * cell
        )

        pygame.draw.line(
            screen,
            GRID_COLOR,
            (x, board.y),
            (x, board.bottom),
            2
        )

        y = int(
            board.y
            +
            i * cell
        )

        pygame.draw.line(
            screen,
            GRID_COLOR,
            (board.x, y),
            (board.right, y),
            2
        )


# =========================================================
# DRAW HEADER
# =========================================================

def draw_header():

    title = fonts["heart"].render(
        "UNBLOCK CAR",
        True,
        WHITE
    )

    screen.blit(
        title,
        (
            45,
            35
        )
    )

    diff = fonts["heart"].render(
        selected_difficulty,
        True,
        YELLOW
    )

    screen.blit(
        diff,
        (
            45,
            82
        )
    )


# =========================================================
# DRAW UI
# =========================================================

def draw_ui():

    w, h = screen.get_size()

    panel_x = w - 330

    # -----------------------------------------------------
    # MOVES
    # -----------------------------------------------------

    move_text = fonts["heart"].render(
        f"MOVES  {moves}",
        True,
        WHITE
    )

    screen.blit(
        move_text,
        (
            panel_x,
            170
        )
    )

    # -----------------------------------------------------
    # TIMER
    # -----------------------------------------------------

    if game_state == PLAYING:

        current_time = (
            time.perf_counter()
            -
            level_start_time
        )

    else:

        current_time = elapsed_time

    minutes = int(
        current_time // 60
    )

    seconds = int(
        current_time % 60
    )

    timer_text = fonts["heart"].render(
        f"TIME  {minutes:02d}:{seconds:02d}",
        True,
        WHITE
    )

    screen.blit(
        timer_text,
        (
            panel_x,
            215
        )
    )

    # -----------------------------------------------------
    # RANDOM PUZZLE
    # -----------------------------------------------------

    puzzle_text = fonts["heart"].render(
        "R = New Puzzle",
        True,
        YELLOW
    )

    screen.blit(
        puzzle_text,
        (
            panel_x,
            265
        )
    )

    # -----------------------------------------------------
    # CONTROLS
    # -----------------------------------------------------

    controls = [
        "Drag cars",
        "R  New Puzzle",
        "ESC  Menu"
    ]

    y = 350

    for text in controls:

        surf = fonts["heart"].render(
            text,
            True,
            GRAY
        )

        screen.blit(
            surf,
            (
                panel_x,
                y
            )
        )

        y += 35


# =========================================================
# MENU
# =========================================================

def draw_menu():

    w, h = screen.get_size()

    title = fonts["heart"].render(
        "UNBLOCK CAR",
        True,
        WHITE
    )

    screen.blit(
        title,
        (
            w // 2
            -
            title.get_width() // 2,
            110
        )
    )

    subtitle = fonts["heart"].render(
        "Clear the road and free the red car",
        True,
        GRAY
    )

    screen.blit(
        subtitle,
        (
            w // 2
            -
            subtitle.get_width() // 2,
            175
        )
    )

    difficulties = [
        DIFFICULTY_EASY,
        DIFFICULTY_MEDIUM,
        DIFFICULTY_HARD
    ]

    colors = [
        GREEN,
        YELLOW,
        RED
    ]

    start_y = 280

    for i, diff in enumerate(
        difficulties
    ):

        rect = pygame.Rect(
            w // 2 - 170,
            start_y + i * 100,
            340,
            70
        )

        mouse = pygame.mouse.get_pos()

        hover = rect.collidepoint(
            mouse
        )

        color = colors[i]

        if hover:

            color = tuple(
                min(
                    255,
                    c + 30
                )
                for c in color
            )

        pygame.draw.rect(
            screen,
            color,
            rect,
            border_radius=15
        )

        text = fonts["heart"].render(
            diff,
            True,
            WHITE
        )

        screen.blit(
            text,
            (
                rect.centerx
                -
                text.get_width() // 2,
                rect.centery
                -
                text.get_height() // 2
            )
        )

    info = fonts["heart"].render(
        "Choose your difficulty",
        True,
        GRAY
    )

    screen.blit(
        info,
        (
            w // 2
            -
            info.get_width() // 2,
            610
        )
    )


# =========================================================
# WIN SCREEN
# =========================================================

def draw_win():

    draw_board()

    for car in cars:

        car.draw(screen)

    w, h = screen.get_size()

    overlay = pygame.Surface(
        (w, h),
        pygame.SRCALPHA
    )

    overlay.fill(
        (0, 0, 0, 165)
    )

    screen.blit(
        overlay,
        (0, 0)
    )

    title = fonts["heart"].render(
        "LEVEL COMPLETE!",
        True,
        GREEN
    )

    screen.blit(
        title,
        (
            w // 2
            -
            title.get_width() // 2,
            230
        )
    )

    result = fonts["heart"].render(
        f"Moves: {moves}",
        True,
        WHITE
    )

    screen.blit(
        result,
        (
            w // 2
            -
            result.get_width() // 2,
            310
        )
    )

    seconds = int(
        elapsed_time
    )

    result_time = fonts["heart"].render(
        f"Time: {seconds // 60:02d}:{seconds % 60:02d}",
        True,
        WHITE
    )

    screen.blit(
        result_time,
        (
            w // 2
            -
            result_time.get_width() // 2,
            355
        )
    )

    restart = fonts["heart"].render(
        "ENTER  New Puzzle     R  Replay     ESC  Menu",
        True,
        GRAY
    )

    screen.blit(
        restart,
        (
            w // 2
            -
            restart.get_width() // 2,
            450
        )
    )


# =========================================================
# UPDATE
# =========================================================

def update_game(dt):

    global elapsed_time

    if game_state != PLAYING:

        return

    elapsed_time = (
        time.perf_counter()
        -
        level_start_time
    )

    for car in cars:

        car.update(dt)


# =========================================================
# NEXT LEVEL
#
# There are no predefined levels anymore.
#
# "Next Level" simply means:
# generate another random puzzle.
# =========================================================

def next_level():

    reset_game()


# =========================================================
# EVENT HANDLING
# =========================================================

def handle_event(event):

    global game_state
    global selected_difficulty

    # =====================================================
    # QUIT
    # =====================================================

    if event.type == pygame.QUIT:

        pygame.quit()

        sys.exit()

    # =====================================================
    # MENU
    # =====================================================

    if game_state == MENU:

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                w, h = screen.get_size()

                difficulties = [
                    DIFFICULTY_EASY,
                    DIFFICULTY_MEDIUM,
                    DIFFICULTY_HARD
                ]

                for i, diff in enumerate(
                    difficulties
                ):

                    rect = pygame.Rect(
                        w // 2 - 170,
                        280 + i * 100,
                        340,
                        70
                    )

                    if rect.collidepoint(
                        event.pos
                    ):

                        selected_difficulty = diff

                        # Clear old history when
                        # changing difficulty so the
                        # new difficulty starts fresh.
                        generated_layout_history.clear()

                        reset_game()

                        return

        return

    # =====================================================
    # PLAYING
    # =====================================================

    if game_state == PLAYING:

        if event.type == pygame.KEYDOWN:

            # -------------------------------------------------
            # R = COMPLETELY NEW RANDOM PUZZLE
            # -------------------------------------------------

            if event.key == pygame.K_r:

                reset_game()

                return

            # -------------------------------------------------
            # ESC
            # -------------------------------------------------

            if event.key == pygame.K_ESCAPE:

                game_state = MENU

                return

        # -----------------------------------------------------
        # MOUSE DOWN
        # -----------------------------------------------------

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                start_drag(
                    event.pos
                )

        # -----------------------------------------------------
        # MOUSE MOVE
        # -----------------------------------------------------

        elif event.type == pygame.MOUSEMOTION:

            if selected_car is not None:

                drag_car(
                    event.pos
                )

        # -----------------------------------------------------
        # MOUSE UP
        # -----------------------------------------------------

        elif event.type == pygame.MOUSEBUTTONUP:

            if event.button == 1:

                end_drag()

        return

    # =====================================================
    # WIN
    # =====================================================

    if game_state == WIN:

        if event.type == pygame.KEYDOWN:

            # -------------------------------------------------
            # R = RANDOM REPLAY
            # -------------------------------------------------

            if event.key == pygame.K_r:

                reset_game()

                return

            # -------------------------------------------------
            # ENTER = NEXT RANDOM PUZZLE
            # -------------------------------------------------

            if event.key == pygame.K_RETURN:

                next_level()

                return

            # -------------------------------------------------
            # ESC = MENU
            # -------------------------------------------------

            if event.key == pygame.K_ESCAPE:

                game_state = MENU

                return


# =========================================================
# DRAW
# =========================================================

def draw():

    screen.fill(
        BG
    )

    # -----------------------------------------------------
    # MENU
    # -----------------------------------------------------

    if game_state == MENU:

        draw_menu()

        return

    # -----------------------------------------------------
    # PLAYING
    # -----------------------------------------------------

    if game_state == PLAYING:

        draw_header()

        draw_board()

        for car in cars:

            car.draw(screen)

        draw_ui()

        return

    # -----------------------------------------------------
    # WIN
    # -----------------------------------------------------

    if game_state == WIN:

        draw_header()

        draw_win()


# =========================================================
# MAIN LOOP
# =========================================================

# previous_time = time.perf_counter()

# while True:

#     current_time = time.perf_counter()

#     dt = (
#         current_time
#         -
#         previous_time
#     )

#     previous_time = current_time

#     # Prevent huge dt after window freeze
#     dt = min(
#         dt,
#         0.05
#     )

#     # -----------------------------------------------------
#     # EVENTS
#     # -----------------------------------------------------

#     for event in pygame.event.get():

#         handle_event(
#             event
#         )

#     # -----------------------------------------------------
#     # UPDATE
#     # -----------------------------------------------------

#     update_game(
#         dt
#     )

#     # -----------------------------------------------------
#     # DRAW
#     # -----------------------------------------------------

#     draw()

#     # pygame.display.flip()

#     # # -----------------------------------------------------
#     # # FPS
#     # # -----------------------------------------------------

#     # clock.tick(
#     #     FPS
#     # )





import time
import pygame


# =========================================================
# TIME
# =========================================================

previous_time = time.perf_counter()


# =========================================================
# MAIN
# =========================================================

def main():

    global previous_time

    # -----------------------------------------------------
    # DT
    # -----------------------------------------------------

    current_time = time.perf_counter()

    dt = (
        current_time
        -
        previous_time
    )

    previous_time = current_time

    # جلوگیری از dt خیلی بزرگ بعد از فریز شدن پنجره
    dt = min(
        dt,
        0.05
    )

    # -----------------------------------------------------
    # EVENTS
    # -----------------------------------------------------

    for event in pygame.event.get():

        handle_event(
            event
        )

    # -----------------------------------------------------
    # UPDATE
    # -----------------------------------------------------

    update_game(
        dt
    )

    # -----------------------------------------------------
    # DRAW
    # -----------------------------------------------------

    draw()
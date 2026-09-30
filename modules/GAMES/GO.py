import pygame
import random
import math
import sys
from modules.font import *
# =========================================================
# SETTINGS
# =========================================================

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

# pygame.init()

# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("GO")

# clock = pygame.time.Clock()

# =========================================================
# COLORS
# =========================================================

# BG = (20, 22, 28)
PANEL = (29, 32, 40)

BOARD_COLOR = (205, 170, 105)
BOARD_DARK = (125, 92, 48)

BLACK = (20, 20, 22)
WHITE = (245, 245, 245)

TEXT = (240, 240, 240)
GRAY = (155, 160, 170)

GREEN = (80, 220, 120)
YELLOW = (235, 195, 70)
RED = (235, 80, 80)

LAST_MOVE_COLOR = (80, 220, 120)

# =========================================================
# FONTS
# =========================================================

FONT_BIG = fonts["heart"]
FONT_TITLE =fonts["heart"]

FONT_MED =fonts["heart"]

FONT_SMALL =fonts["heart"]

FONT_TIMER =fonts["heart"]

# =========================================================
# GAME STATES
# =========================================================

LEVEL_SELECT = 0
PLAYING = 1
GAME_OVER = 2

game_state = LEVEL_SELECT

# =========================================================
# LEVELS
# =========================================================

LEVELS = {

    "EASY": {
        "size": 9,
        "bot_depth": 1,
        "simulations": 30,
    },

    "MEDIUM": {
        "size": 9,
        "bot_depth": 2,
        "simulations": 80,
    },

    "HARD": {
        "size": 13,
        "bot_depth": 2,
        "simulations": 150,
    },
}

LEVEL_NAMES = [
    "EASY",
    "MEDIUM",
    "HARD",
]

selected_level = "EASY"

# =========================================================
# GO CONSTANTS
# =========================================================

EMPTY = 0
PLAYER = 1
BOT = 2

# =========================================================
# BOARD
# =========================================================

BOARD_SIZE = 9

board = []

current_player = PLAYER

captures_player = 0
captures_bot = 0

passes = 0

move_number = 0

last_move = None

previous_board = None

# =========================================================
# TIMER
# =========================================================

start_time = 0
finish_time = 0

# =========================================================
# BOARD POSITION
# =========================================================

BOARD_LEFT = 100
BOARD_TOP = 110

BOARD_PIXEL_SIZE = 600
CELL_SIZE = 70

# =========================================================
# ANIMATION
# =========================================================

stone_animation = None

# {
#     row,
#     col,
#     color,
#     start,
#     duration
# }

# =========================================================
# BOT
# =========================================================

bot_thinking = False

bot_think_start = 0

BOT_THINK_DELAY = 350

# =========================================================
# BUTTONS
# =========================================================

pass_rect = pygame.Rect(
    850,
    610,
    230,
    65
)

restart_rect = pygame.Rect(
    850,
    690,
    230,
    65
)

# =========================================================
# TIME
# =========================================================

def reset_time():

    global start_time

    start_time = pygame.time.get_ticks()


def elapsed_seconds():

    now = pygame.time.get_ticks()

    if game_state == GAME_OVER:
        now = finish_time

    return max(
        0,
        (now - start_time) // 1000
    )


# =========================================================
# BOARD CREATION
# =========================================================

def create_board():

    return [
        [EMPTY for _ in range(BOARD_SIZE)]
        for _ in range(BOARD_SIZE)
    ]


# =========================================================
# COPY BOARD
# =========================================================

def copy_board(source):

    return [
        row[:] for row in source
    ]


# =========================================================
# BOARD GEOMETRY
# =========================================================

def calculate_board_geometry():

    global BOARD_PIXEL_SIZE
    global CELL_SIZE
    global BOARD_LEFT
    global BOARD_TOP

    if BOARD_SIZE == 9:

        BOARD_PIXEL_SIZE = 590

        CELL_SIZE = (
            BOARD_PIXEL_SIZE /
            (BOARD_SIZE - 1)
        )

        BOARD_LEFT = 80
        BOARD_TOP = 115

    else:

        BOARD_PIXEL_SIZE = 610

        CELL_SIZE = (
            BOARD_PIXEL_SIZE /
            (BOARD_SIZE - 1)
        )

        BOARD_LEFT = 55
        BOARD_TOP = 105


# =========================================================
# CELL -> SCREEN
# =========================================================

def cell_to_screen(row, col):

    x = BOARD_LEFT + col * CELL_SIZE
    y = BOARD_TOP + row * CELL_SIZE

    return int(x), int(y)


# =========================================================
# SCREEN -> CELL
# =========================================================

def screen_to_cell(pos):

    x, y = pos

    col = round(
        (x - BOARD_LEFT) / CELL_SIZE
    )

    row = round(
        (y - BOARD_TOP) / CELL_SIZE
    )

    if (
        row < 0
        or row >= BOARD_SIZE
        or col < 0
        or col >= BOARD_SIZE
    ):
        return None

    sx, sy = cell_to_screen(
        row,
        col
    )

    distance = math.hypot(
        x - sx,
        y - sy
    )

    if distance > CELL_SIZE * 0.48:
        return None

    return row, col


# =========================================================
# NEIGHBORS
# =========================================================

def neighbors(row, col):

    result = []

    if row > 0:
        result.append(
            (row - 1, col)
        )

    if row < BOARD_SIZE - 1:
        result.append(
            (row + 1, col)
        )

    if col > 0:
        result.append(
            (row, col - 1)
        )

    if col < BOARD_SIZE - 1:
        result.append(
            (row, col + 1)
        )

    return result


# =========================================================
# GROUP
# =========================================================

def get_group(state, start):

    sr, sc = start

    color = state[sr][sc]

    if color == EMPTY:
        return set()

    group = set()

    stack = [start]

    while stack:

        cell = stack.pop()

        if cell in group:
            continue

        r, c = cell

        if state[r][c] != color:
            continue

        group.add(cell)

        for nr, nc in neighbors(r, c):

            if (
                state[nr][nc] == color
                and (nr, nc) not in group
            ):
                stack.append(
                    (nr, nc)
                )

    return group


# =========================================================
# LIBERTIES
# =========================================================

def get_liberties(state, group):

    liberties = set()

    for r, c in group:

        for nr, nc in neighbors(r, c):

            if state[nr][nc] == EMPTY:

                liberties.add(
                    (nr, nc)
                )

    return liberties


# =========================================================
# REMOVE GROUP
# =========================================================

def remove_group(state, group):

    for r, c in group:

        state[r][c] = EMPTY


# =========================================================
# PLAY MOVE ON COPY
# =========================================================

def simulate_move(
    state,
    row,
    col,
    color,
    ko_board=None
):

    if state[row][col] != EMPTY:
        return None, 0

    new_board = copy_board(state)

    new_board[row][col] = color

    opponent = (
        BOT
        if color == PLAYER
        else PLAYER
    )

    captured = 0

    # Capture opponent groups
    for nr, nc in neighbors(
        row,
        col
    ):

        if new_board[nr][nc] != opponent:
            continue

        group = get_group(
            new_board,
            (nr, nc)
        )

        liberties = get_liberties(
            new_board,
            group
        )

        if len(liberties) == 0:

            captured += len(group)

            remove_group(
                new_board,
                group
            )

    # Check suicide
    own_group = get_group(
        new_board,
        (row, col)
    )

    own_liberties = get_liberties(
        new_board,
        own_group
    )

    if len(own_liberties) == 0:

        # Suicide not allowed
        return None, 0

    # Ko:
    # New board cannot equal previous board
    if ko_board is not None:

        if new_board == ko_board:
            return None, 0

    return new_board, captured


# =========================================================
# LEGAL MOVES
# =========================================================

def get_legal_moves(
    state,
    color,
    ko_board=None
):

    moves = []

    for row in range(BOARD_SIZE):

        for col in range(BOARD_SIZE):

            if state[row][col] != EMPTY:
                continue

            new_board, captured = simulate_move(
                state,
                row,
                col,
                color,
                ko_board
            )

            if new_board is not None:

                moves.append(
                    (
                        row,
                        col,
                        captured
                    )
                )

    return moves


# =========================================================
# TERRITORY / SCORE
# =========================================================

def calculate_score(state):

    black_stones = 0
    white_stones = 0

    for row in state:

        for cell in row:

            if cell == PLAYER:
                black_stones += 1

            elif cell == BOT:
                white_stones += 1

    visited = set()

    black_territory = 0
    white_territory = 0

    for row in range(BOARD_SIZE):

        for col in range(BOARD_SIZE):

            if state[row][col] != EMPTY:
                continue

            if (row, col) in visited:
                continue

            region = set()

            stack = [
                (row, col)
            ]

            bordering_colors = set()

            while stack:

                cell = stack.pop()

                if cell in region:
                    continue

                r, c = cell

                if state[r][c] != EMPTY:

                    bordering_colors.add(
                        state[r][c]
                    )

                    continue

                region.add(cell)

                for nr, nc in neighbors(
                    r,
                    c
                ):

                    if (
                        state[nr][nc] == EMPTY
                        and (nr, nc) not in region
                    ):

                        stack.append(
                            (nr, nc)
                        )

                    elif state[nr][nc] != EMPTY:

                        bordering_colors.add(
                            state[nr][nc]
                        )

            visited.update(region)

            if bordering_colors == {PLAYER}:

                black_territory += len(region)

            elif bordering_colors == {BOT}:

                white_territory += len(region)

    black_score = (
        black_stones
        + black_territory
        + captures_player
    )

    white_score = (
        white_stones
        + white_territory
        + captures_bot
        + 6.5
    )

    return (
        black_score,
        white_score
    )


# =========================================================
# START GAME
# =========================================================

def reset_game():

    global BOARD_SIZE
    global board
    global current_player
    global captures_player
    global captures_bot
    global passes
    global move_number
    global last_move
    global previous_board
    global stone_animation
    global bot_thinking
    global bot_think_start
    global game_state
    global finish_time

    config = LEVELS[
        selected_level
    ]

    BOARD_SIZE = config["size"]

    calculate_board_geometry()

    board = create_board()

    current_player = PLAYER

    captures_player = 0
    captures_bot = 0

    passes = 0

    move_number = 0

    last_move = None

    previous_board = None

    stone_animation = None

    bot_thinking = False

    bot_think_start = 0

    finish_time = 0

    game_state = PLAYING

    reset_time()


# =========================================================
# PLAYER MOVE
# =========================================================

def player_move(row, col):

    global board
    global current_player
    global captures_player
    global previous_board
    global last_move
    global passes
    global move_number
    global stone_animation

    if current_player != PLAYER:
        return

    new_board, captured = simulate_move(
        board,
        row,
        col,
        PLAYER,
        previous_board
    )

    if new_board is None:
        return

    old_board = board

    previous_board = copy_board(
        board
    )

    board = new_board

    captures_player += captured

    last_move = (
        row,
        col
    )

    move_number += 1

    passes = 0

    stone_animation = {
        "row": row,
        "col": col,
        "color": PLAYER,
        "start": pygame.time.get_ticks(),
        "duration": 180,
    }

    current_player = BOT


# =========================================================
# PASS
# =========================================================

def pass_turn():

    global current_player
    global passes
    global game_state
    global finish_time
    global previous_board
    global move_number

    passes += 1

    move_number += 1

    previous_board = copy_board(
        board
    )

    if passes >= 2:

        finish_time = pygame.time.get_ticks()

        game_state = GAME_OVER

        return

    if current_player == PLAYER:

        current_player = BOT

    else:

        current_player = PLAYER


# =========================================================
# BOT HEURISTIC
# =========================================================

def evaluate_move(
    state,
    row,
    col,
    color,
    captured
):

    score = 0

    # -----------------------------------------------------
    # Captures are valuable
    # -----------------------------------------------------

    score += captured * 35

    # -----------------------------------------------------
    # Center preference
    # -----------------------------------------------------

    center = (
        BOARD_SIZE - 1
    ) / 2

    distance = abs(
        row - center
    ) + abs(
        col - center
    )

    score += max(
        0,
        15 - distance
    )

    # -----------------------------------------------------
    # Adjacent friendly groups
    # -----------------------------------------------------

    friendly = 0
    enemy = 0

    for nr, nc in neighbors(
        row,
        col
    ):

        if state[nr][nc] == color:
            friendly += 1

        elif state[nr][nc] != EMPTY:
            enemy += 1

    score += friendly * 7
    score += enemy * 4

    # -----------------------------------------------------
    # Liberty after move
    # -----------------------------------------------------

    group = get_group(
        state,
        (row, col)
    )

    liberties = get_liberties(
        state,
        group
    )

    score += min(
        len(liberties) * 3,
        24
    )

    # -----------------------------------------------------
    # Randomness
    # -----------------------------------------------------

    score += random.uniform(
        0,
        8
    )

    return score


# =========================================================
# BOT MOVE
# =========================================================

def choose_bot_move():

    config = LEVELS[
        selected_level
    ]

    legal = get_legal_moves(
        board,
        BOT,
        previous_board
    )

    if not legal:

        return None

    scored = []

    for row, col, captured in legal:

        new_board, real_captured = simulate_move(
            board,
            row,
            col,
            BOT,
            previous_board
        )

        if new_board is None:
            continue

        score = evaluate_move(
            new_board,
            row,
            col,
            BOT,
            real_captured
        )

        # -------------------------------------------------
        # Difficulty
        # -------------------------------------------------

        if selected_level == "EASY":

            score += random.uniform(
                -25,
                25
            )

        elif selected_level == "MEDIUM":

            score += random.uniform(
                -10,
                10
            )

        else:

            score += random.uniform(
                -3,
                3
            )

        scored.append(
            (
                score,
                row,
                col,
                real_captured
            )
        )

    if not scored:
        return None

    scored.sort(
        key=lambda x: x[0],
        reverse=True
    )

    # Easy is more random
    if selected_level == "EASY":

        top = scored[
            :min(6, len(scored))
        ]

        return random.choice(top)

    # Medium
    if selected_level == "MEDIUM":

        top = scored[
            :min(3, len(scored))
        ]

        return random.choice(top)

    # Hard
    return scored[0]


# =========================================================
# APPLY BOT MOVE
# =========================================================

def apply_bot_move():

    global board
    global current_player
    global captures_bot
    global previous_board
    global last_move
    global move_number
    global passes
    global stone_animation
    global bot_thinking

    result = choose_bot_move()

    if result is None:

        # Bot passes
        passes += 1

        move_number += 1

        if passes >= 2:

            global game_state
            global finish_time

            finish_time = pygame.time.get_ticks()

            game_state = GAME_OVER

            bot_thinking = False

            return

        current_player = PLAYER

        bot_thinking = False

        return

    score, row, col, captured = result

    new_board, real_captured = simulate_move(
        board,
        row,
        col,
        BOT,
        previous_board
    )

    if new_board is None:

        current_player = PLAYER

        bot_thinking = False

        return

    previous_board = copy_board(
        board
    )

    board = new_board

    captures_bot += real_captured

    last_move = (
        row,
        col
    )

    move_number += 1

    passes = 0

    stone_animation = {
        "row": row,
        "col": col,
        "color": BOT,
        "start": pygame.time.get_ticks(),
        "duration": 180,
    }

    current_player = PLAYER

    bot_thinking = False


# =========================================================
# UPDATE BOT
# =========================================================

def update_bot():

    global bot_thinking
    global bot_think_start

    if game_state != PLAYING:
        return

    if current_player != BOT:
        return

    if not bot_thinking:

        bot_thinking = True

        bot_think_start = pygame.time.get_ticks()

        return

    now = pygame.time.get_ticks()

    if (
        now - bot_think_start
        >= BOT_THINK_DELAY
    ):

        apply_bot_move()


# =========================================================
# DRAW BOARD
# =========================================================

def draw_board():

    board_width = (
        (BOARD_SIZE - 1)
        * CELL_SIZE
    )

    board_height = board_width

    outer = pygame.Rect(
        int(BOARD_LEFT - 35),
        int(BOARD_TOP - 35),
        int(board_width + 70),
        int(board_height + 70)
    )

    pygame.draw.rect(
        screen,
        BOARD_COLOR,
        outer,
        border_radius=15
    )

    # -----------------------------------------------------
    # Grid lines
    # -----------------------------------------------------

    for i in range(BOARD_SIZE):

        x = int(
            BOARD_LEFT
            + i * CELL_SIZE
        )

        y = int(
            BOARD_TOP
            + i * CELL_SIZE
        )

        pygame.draw.line(
            screen,
            BOARD_DARK,
            (
                int(BOARD_LEFT),
                y
            ),
            (
                int(BOARD_LEFT + board_width),
                y
            ),
            2
        )

        pygame.draw.line(
            screen,
            BOARD_DARK,
            (
                x,
                int(BOARD_TOP)
            ),
            (
                x,
                int(BOARD_TOP + board_height)
            ),
            2
        )

    # -----------------------------------------------------
    # Star points
    # -----------------------------------------------------

    if BOARD_SIZE == 9:

        stars = [
            (2, 2),
            (2, 6),
            (4, 4),
            (6, 2),
            (6, 6),
        ]

    else:

        stars = [
            (3, 3),
            (3, 9),
            (6, 6),
            (9, 3),
            (9, 9),
        ]

    for row, col in stars:

        x, y = cell_to_screen(
            row,
            col
        )

        pygame.draw.circle(
            screen,
            BOARD_DARK,
            (x, y),
            5
        )


# =========================================================
# DRAW STONE
# =========================================================

def draw_stone(
    row,
    col,
    color,
    scale=1.0
):

    x, y = cell_to_screen(
        row,
        col
    )

    radius = int(
        CELL_SIZE * 0.43 * scale
    )

    if radius <= 0:
        return

    # Shadow
    pygame.draw.circle(
        screen,
        (70, 55, 35),
        (
            x + 3,
            y + 4
        ),
        radius
    )

    pygame.draw.circle(
        screen,
        color,
        (x, y),
        radius
    )

    # Small highlight
    if color == BLACK:

        pygame.draw.circle(
            screen,
            (75, 75, 78),
            (
                x - radius // 3,
                y - radius // 3
            ),
            max(
                2,
                radius // 8
            )
        )

    else:

        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (
                x - radius // 3,
                y - radius // 3
            ),
            max(
                2,
                radius // 8
            )
        )


# =========================================================
# DRAW STONES
# =========================================================

def draw_stones():

    for row in range(BOARD_SIZE):

        for col in range(BOARD_SIZE):

            value = board[row][col]

            if value == EMPTY:
                continue

            # Skip animated stone
            if stone_animation:

                if (
                    stone_animation["row"] == row
                    and stone_animation["col"] == col
                ):
                    continue

            if value == PLAYER:

                draw_stone(
                    row,
                    col,
                    BLACK
                )

            elif value == BOT:

                draw_stone(
                    row,
                    col,
                    WHITE
                )


# =========================================================
# DRAW ANIMATION
# =========================================================

def draw_stone_animation():

    if stone_animation is None:
        return

    now = pygame.time.get_ticks()

    elapsed = (
        now
        - stone_animation["start"]
    )

    duration = stone_animation["duration"]

    progress = min(
        1.0,
        elapsed / duration
    )

    # Ease out
    progress = 1 - (
        1 - progress
    ) ** 3

    scale = 0.2 + (
        0.8 * progress
    )

    color = (
        BLACK
        if stone_animation["color"] == PLAYER
        else WHITE
    )

    draw_stone(
        stone_animation["row"],
        stone_animation["col"],
        color,
        scale
    )


# =========================================================
# DRAW LAST MOVE
# =========================================================

def draw_last_move():

    if last_move is None:
        return

    row, col = last_move

    x, y = cell_to_screen(
        row,
        col
    )

    radius = int(
        CELL_SIZE * 0.10
    )

    pygame.draw.circle(
        screen,
        LAST_MOVE_COLOR,
        (x, y),
        radius
    )


# =========================================================
# DRAW HEADER
# =========================================================

def draw_header():

    title = FONT_TITLE.render(
        "GO",
        True,
        TEXT
    )

    screen.blit(
        title,
        (45, 35)
    )

    level = FONT_SMALL.render(
        selected_level,
        True,
        GRAY
    )

    screen.blit(
        level,
        (130, 48)
    )

    # Timer
    seconds = elapsed_seconds()

    minutes = seconds // 60
    sec = seconds % 60

    timer = FONT_TIMER.render(
        f"{minutes:02d}:{sec:02d}",
        True,
        TEXT
    )

    timer_rect = timer.get_rect(
        top=38,
        right=WIDTH - 50
    )

    screen.blit(
        timer,
        timer_rect
    )


# =========================================================
# DRAW SIDE PANEL
# =========================================================

def draw_panel():

    panel = pygame.Rect(
        760,
        100,
        380,
        620
    )

    pygame.draw.rect(
        screen,
        PANEL,
        panel,
        border_radius=20
    )

    # Turn
    if current_player == PLAYER:

        turn_color = BLACK
        turn_text = "YOUR TURN"

    else:

        turn_color = WHITE
        turn_text = "BOT THINKING"

    draw_center_text(
        turn_text,
        FONT_MED,
        TEXT,
        (
            panel.centerx,
            145
        )
    )

    # Stone
    pygame.draw.circle(
        screen,
        turn_color,
        (
            panel.centerx,
            205
        ),
        35
    )

    pygame.draw.circle(
        screen,
        GRAY,
        (
            panel.centerx,
            205
        ),
        35,
        2
    )

    # Captures
    draw_center_text(
        f"YOUR CAPTURES: {captures_player}",
        FONT_SMALL,
        TEXT,
        (
            panel.centerx,
            285
        )
    )

    draw_center_text(
        f"BOT CAPTURES: {captures_bot}",
        FONT_SMALL,
        TEXT,
        (
            panel.centerx,
            320
        )
    )

    # Moves
    draw_center_text(
        f"MOVES: {move_number}",
        FONT_SMALL,
        GRAY,
        (
            panel.centerx,
            370
        )
    )

    # Passes
    draw_center_text(
        f"CONSECUTIVE PASSES: {passes}/2",
        FONT_SMALL,
        GRAY,
        (
            panel.centerx,
            405
        )
    )

    # Pass button
    mouse_pos = pygame.mouse.get_pos()

    hover = pass_rect.collidepoint(
        mouse_pos
    )

    if hover:

        pygame.draw.rect(
            screen,
            GREEN,
            pass_rect,
            border_radius=14
        )

        color = BG

    else:

        pygame.draw.rect(
            screen,
            (40, 44, 54),
            pass_rect,
            border_radius=14
        )

        pygame.draw.rect(
            screen,
            GREEN,
            pass_rect,
            2,
            border_radius=14
        )

        color = TEXT

    draw_center_text(
        "PASS",
        FONT_MED,
        color,
        pass_rect.center
    )

    # Restart
    hover_restart = restart_rect.collidepoint(
        mouse_pos
    )

    if hover_restart:

        pygame.draw.rect(
            screen,
            RED,
            restart_rect,
            border_radius=14
        )

        color = BG

    else:

        pygame.draw.rect(
            screen,
            (40, 44, 54),
            restart_rect,
            border_radius=14
        )

        pygame.draw.rect(
            screen,
            RED,
            restart_rect,
            2,
            border_radius=14
        )

        color = TEXT

    draw_center_text(
        "RESTART",
        FONT_MED,
        color,
        restart_rect.center
    )


# =========================================================
# CENTER TEXT
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

    screen.blit(
        surface,
        rect
    )


# =========================================================
# DRAW PLAYING
# =========================================================

def draw_playing():

    # screen.fill(BG)

    draw_header()

    draw_board()

    draw_stones()

    draw_stone_animation()

    draw_last_move()

    draw_panel()

    # Bottom
    draw_center_text(
        "Click an intersection to place a stone",
        FONT_SMALL,
        GRAY,
        (
            450,
            HEIGHT - 30
        )
    )


# =========================================================
# DRAW LEVEL SELECT
# =========================================================

def draw_level_select():

    # screen.fill(BG)

    draw_center_text(
        "GO",
        FONT_BIG,
        TEXT,
        (
            WIDTH // 2,
            120
        )
    )

    draw_center_text(
        "PLAYER VS BOT",
        FONT_SMALL,
        GRAY,
        (
            WIDTH // 2,
            175
        )
    )

    button_width = 270
    button_height = 115

    gap = 35

    total_width = (
        button_width * 3
        + gap * 2
    )

    start_x = (
        WIDTH - total_width
    ) // 2

    y = 300

    for i, level in enumerate(
        LEVEL_NAMES
    ):

        x = (
            start_x
            + i * (
                button_width
                + gap
            )
        )

        rect = pygame.Rect(
            x,
            y,
            button_width,
            button_height
        )

        mouse = pygame.mouse.get_pos()

        hover = rect.collidepoint(
            mouse
        )

        if i == 0:
            accent = GREEN
            size_text = "9 × 9"

        elif i == 1:
            accent = YELLOW
            size_text = "9 × 9"

        else:
            accent = RED
            size_text = "13 × 13"

        if hover:

            pygame.draw.rect(
                screen,
                accent,
                rect,
                border_radius=18
            )

            text_color = BG

        else:

            pygame.draw.rect(
                screen,
                PANEL,
                rect,
                border_radius=18
            )

            pygame.draw.rect(
                screen,
                accent,
                rect,
                3,
                border_radius=18
            )

            text_color = TEXT

        draw_center_text(
            level,
            FONT_MED,
            text_color,
            (
                rect.centerx,
                rect.centery - 15
            )
        )

        draw_center_text(
            size_text,
            FONT_SMALL,
            text_color,
            (
                rect.centerx,
                rect.centery + 25
            )
        )

    draw_center_text(
        "Black = You     White = Bot",
        FONT_SMALL,
        GRAY,
        (
            WIDTH // 2,
            535
        )
    )

    draw_center_text(
        "1 = Easy     2 = Medium     3 = Hard",
        FONT_SMALL,
        GRAY,
        (
            WIDTH // 2,
            580
        )
    )

    draw_center_text(
        "ESC = Quit",
        FONT_SMALL,
        GRAY,
        (
            WIDTH // 2,
            630
        )
    )


# =========================================================
# DRAW GAME OVER
# =========================================================

def draw_game_over():

    # screen.fill(BG)

    black_score, white_score = calculate_score()

    if black_score > white_score:

        winner = "YOU WIN!"

        winner_color = GREEN

    elif white_score > black_score:

        winner = "BOT WINS!"

        winner_color = RED

    else:

        winner = "DRAW!"

        winner_color = YELLOW

    draw_center_text(
        winner,
        FONT_BIG,
        winner_color,
        (
            WIDTH // 2,
            170
        )
    )

    draw_center_text(
        f"BLACK   {black_score:.1f}",
        FONT_TITLE,
        TEXT,
        (
            WIDTH // 2,
            290
        )
    )

    draw_center_text(
        f"WHITE   {white_score:.1f}",
        FONT_TITLE,
        TEXT,
        (
            WIDTH // 2,
            350
        )
    )

    seconds = elapsed_seconds()

    minutes = seconds // 60
    sec = seconds % 60

    draw_center_text(
        f"TIME   {minutes:02d}:{sec:02d}",
        FONT_MED,
        GRAY,
        (
            WIDTH // 2,
            425
        )
    )

    # Play again
    mouse = pygame.mouse.get_pos()

    hover = restart_rect.collidepoint(
        mouse
    )

    if hover:

        pygame.draw.rect(
            screen,
            GREEN,
            restart_rect,
            border_radius=15
        )

        color = BG

    else:

        pygame.draw.rect(
            screen,
            PANEL,
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

        color = TEXT

    draw_center_text(
        "PLAY AGAIN",
        FONT_MED,
        color,
        restart_rect.center
    )

    draw_center_text(
        "R = Restart     ESC = Level Select",
        FONT_SMALL,
        GRAY,
        (
            WIDTH // 2,
            600
        )
    )


# =========================================================
# LEVEL SELECT EVENTS
# =========================================================

def event_level_select(event):

    global selected_level

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

    elif event.type == pygame.MOUSEBUTTONDOWN:

        if event.button != 1:
            return

        button_width = 270
        button_height = 115

        gap = 35

        total_width = (
            button_width * 3
            + gap * 2
        )

        start_x = (
            WIDTH - total_width
        ) // 2

        y = 300

        for i, level in enumerate(
            LEVEL_NAMES
        ):

            rect = pygame.Rect(
                start_x
                + i * (
                    button_width
                    + gap
                ),
                y,
                button_width,
                button_height
            )

            if rect.collidepoint(
                event.pos
            ):

                selected_level = level

                reset_game()

                return


# =========================================================
# PLAYING EVENTS
# =========================================================

def event_playing(event):

    global game_state

    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_r:

            reset_game()

            return

        if event.key == pygame.K_ESCAPE:

            game_state = LEVEL_SELECT

            return

        if event.key == pygame.K_SPACE:

            if current_player == PLAYER:

                pass_turn()

                return

    if event.type == pygame.MOUSEBUTTONDOWN:

        if event.button != 1:
            return

        # Pass
        if pass_rect.collidepoint(
            event.pos
        ):

            if current_player == PLAYER:

                pass_turn()

            return

        # Restart
        if restart_rect.collidepoint(
            event.pos
        ):

            reset_game()

            return

        # Board
        if current_player != PLAYER:
            return

        cell = screen_to_cell(
            event.pos
        )

        if cell is None:
            return

        row, col = cell

        player_move(
            row,
            col
        )


# =========================================================
# GAME OVER EVENTS
# =========================================================

def event_game_over(event):

    global game_state

    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_r:

            reset_game()

        elif event.key == pygame.K_ESCAPE:

            game_state = LEVEL_SELECT

    elif event.type == pygame.MOUSEBUTTONDOWN:

        if event.button != 1:
            return

        if restart_rect.collidepoint(
            event.pos
        ):

            reset_game()


# =========================================================
# UPDATE
# =========================================================

def update_game():

    global stone_animation

    if game_state != PLAYING:
        return

    update_bot()

    # Animation cleanup
    if stone_animation:

        now = pygame.time.get_ticks()

        if (
            now
            - stone_animation["start"]
            >= stone_animation["duration"]
        ):

            stone_animation = None


# =========================================================
# MAIN
# =========================================================

def GO_():

    global game_state



    # Update
    update_game()

    # Draw
    if game_state == LEVEL_SELECT:

        draw_level_select()

    elif game_state == PLAYING:

        draw_playing()

    elif game_state == GAME_OVER:

        draw_game_over()


def event_GO(event):
    global game_state

    if game_state == LEVEL_SELECT:

        event_level_select(
            event
        )

    elif game_state == PLAYING:

        event_playing(
            event
        )

    elif game_state == GAME_OVER:

        event_game_over(
            event
        )


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

ROWS = 6
COLS = 7

EMPTY = 0
PLAYER = 1
BOT = 2

# =========================================================
# COLORS
# =========================================================

BG = (24, 27, 35)

BOARD_COLOR = (35, 75, 150)
BOARD_BORDER = (75, 120, 210)

EMPTY_COLOR = (20, 25, 35)

PLAYER_COLOR = (235, 65, 75)
PLAYER_LIGHT = (255, 115, 120)

BOT_COLOR = (245, 190, 45)
BOT_LIGHT = (255, 225, 100)

WHITE = (245, 245, 245)
TEXT_GRAY = (175, 180, 195)

WIN_COLOR = (80, 235, 130)

# =========================================================
# LEVELS
# =========================================================

LEVEL_EASY = "EASY"
LEVEL_MEDIUM = "MEDIUM"
LEVEL_HARD = "HARD"

selected_level = None

BOT_DEPTH = {
    LEVEL_EASY: 1,
    LEVEL_MEDIUM: 3,
    LEVEL_HARD: 5,
}

# =========================================================
# GAME STATES
# =========================================================

LEVEL_SELECT = 0
PLAYING = 1
GAME_OVER = 2

game_state = LEVEL_SELECT

# =========================================================
# BOARD
# =========================================================

board = []

current_turn = PLAYER

winner = None

winning_positions = []

# =========================================================
# TIMER
# =========================================================

game_start_time = 0


def reset_time():
    """
    Reset game timer.
    """

    global game_start_time

    game_start_time = pygame.time.get_ticks()


# =========================================================
# RESET GAME
# =========================================================

def reset_game():

    global board
    global current_turn
    global winner
    global winning_positions

    board = [
        [EMPTY for _ in range(COLS)]
        for _ in range(ROWS)
    ]

    current_turn = PLAYER

    winner = None

    winning_positions = []

    reset_time()


# =========================================================
# BOARD GEOMETRY
# =========================================================

BOARD_WIDTH = 700
BOARD_HEIGHT = 600

CELL_SIZE = 90

BOARD_X = 0
BOARD_Y = 0


def update_geometry():

    global BOARD_WIDTH
    global BOARD_HEIGHT
    global CELL_SIZE
    global BOARD_X
    global BOARD_Y

    max_width = WIDTH - 260
    max_height = HEIGHT - 150

    CELL_SIZE = min(
        max_width // COLS,
        max_height // ROWS
    )

    BOARD_WIDTH = CELL_SIZE * COLS
    BOARD_HEIGHT = CELL_SIZE * ROWS

    BOARD_X = (
        WIDTH - BOARD_WIDTH
    ) // 2

    BOARD_Y = (
        HEIGHT - BOARD_HEIGHT
    ) // 2 + 25


# =========================================================
# CELL CENTER
# =========================================================

def cell_center(row, col):

    x = (
        BOARD_X
        + col * CELL_SIZE
        + CELL_SIZE // 2
    )

    y = (
        BOARD_Y
        + row * CELL_SIZE
        + CELL_SIZE // 2
    )

    return x, y


# =========================================================
# COLUMN FROM MOUSE
# =========================================================

def get_column_from_mouse(pos):

    x, y = pos

    if not (
        BOARD_X <= x <= BOARD_X + BOARD_WIDTH
    ):
        return None

    if not (
        BOARD_Y <= y <= BOARD_Y + BOARD_HEIGHT
    ):
        return None

    col = int(
        (x - BOARD_X) / CELL_SIZE
    )

    if 0 <= col < COLS:

        return col

    return None


# =========================================================
# AVAILABLE ROW
# =========================================================

def get_available_row(board_state, col):

    for row in range(
        ROWS - 1,
        -1,
        -1
    ):

        if board_state[row][col] == EMPTY:

            return row

    return None


# =========================================================
# VALID COLUMNS
# =========================================================

def get_valid_columns(board_state):

    return [
        col
        for col in range(COLS)
        if board_state[0][col] == EMPTY
    ]


# =========================================================
# MAKE MOVE
# =========================================================

def make_move(
    board_state,
    row,
    col,
    player
):

    board_state[row][col] = player


# =========================================================
# CHECK WIN
# =========================================================

def check_win(
    board_state,
    player
):

    # -----------------------------------------------------
    # HORIZONTAL
    # -----------------------------------------------------

    for row in range(ROWS):

        for col in range(COLS - 3):

            positions = [
                (row, col),
                (row, col + 1),
                (row, col + 2),
                (row, col + 3)
            ]

            if all(
                board_state[r][c] == player
                for r, c in positions
            ):

                return True, positions

    # -----------------------------------------------------
    # VERTICAL
    # -----------------------------------------------------

    for row in range(ROWS - 3):

        for col in range(COLS):

            positions = [
                (row, col),
                (row + 1, col),
                (row + 2, col),
                (row + 3, col)
            ]

            if all(
                board_state[r][c] == player
                for r, c in positions
            ):

                return True, positions

    # -----------------------------------------------------
    # DIAGONAL DOWN RIGHT
    # -----------------------------------------------------

    for row in range(ROWS - 3):

        for col in range(COLS - 3):

            positions = [
                (row, col),
                (row + 1, col + 1),
                (row + 2, col + 2),
                (row + 3, col + 3)
            ]

            if all(
                board_state[r][c] == player
                for r, c in positions
            ):

                return True, positions

    # -----------------------------------------------------
    # DIAGONAL UP RIGHT
    # -----------------------------------------------------

    for row in range(3, ROWS):

        for col in range(COLS - 3):

            positions = [
                (row, col),
                (row - 1, col + 1),
                (row - 2, col + 2),
                (row - 3, col + 3)
            ]

            if all(
                board_state[r][c] == player
                for r, c in positions
            ):

                return True, positions

    return False, []


# =========================================================
# DRAW PIECE
# =========================================================

def draw_piece(
    surface,
    center,
    player,
    radius,
    alpha=255,
    winning=False
):

    temp = pygame.Surface(
        (
            radius * 2 + 20,
            radius * 2 + 20
        ),
        pygame.SRCALPHA
    )

    cx = temp.get_width() // 2
    cy = temp.get_height() // 2

    if player == PLAYER:

        main_color = PLAYER_COLOR
        light_color = PLAYER_LIGHT

    else:

        main_color = BOT_COLOR
        light_color = BOT_LIGHT

    # shadow
    pygame.draw.circle(
        temp,
        (0, 0, 0, int(alpha * 0.35)),
        (
            cx + 4,
            cy + 5
        ),
        radius
    )

    # main ball
    pygame.draw.circle(
        temp,
        (
            main_color[0],
            main_color[1],
            main_color[2],
            alpha
        ),
        (
            cx,
            cy
        ),
        radius
    )

    # highlight
    highlight_radius = max(
        3,
        int(radius * 0.22)
    )

    pygame.draw.circle(
        temp,
        (
            light_color[0],
            light_color[1],
            light_color[2],
            min(alpha, 190)
        ),
        (
            cx - int(radius * 0.28),
            cy - int(radius * 0.30)
        ),
        highlight_radius
    )

    # winning ring
    if winning:

        pygame.draw.circle(
            temp,
            (
                WIN_COLOR[0],
                WIN_COLOR[1],
                WIN_COLOR[2],
                alpha
            ),
            (
                cx,
                cy
            ),
            radius + 6,
            5
        )

    surface.blit(
        temp,
        (
            center[0] - temp.get_width() // 2,
            center[1] - temp.get_height() // 2
        )
    )


# =========================================================
# DRAW BOARD
# =========================================================

def draw_board(surface):

    # shadow
    shadow_rect = pygame.Rect(
        BOARD_X + 10,
        BOARD_Y + 12,
        BOARD_WIDTH,
        BOARD_HEIGHT
    )

    pygame.draw.rect(
        surface,
        (10, 12, 18),
        shadow_rect,
        border_radius=22
    )

    # board
    board_rect = pygame.Rect(
        BOARD_X,
        BOARD_Y,
        BOARD_WIDTH,
        BOARD_HEIGHT
    )

    pygame.draw.rect(
        surface,
        BOARD_COLOR,
        board_rect,
        border_radius=20
    )

    pygame.draw.rect(
        surface,
        BOARD_BORDER,
        board_rect,
        5,
        border_radius=20
    )

    # holes
    radius = int(
        CELL_SIZE * 0.34
    )

    for row in range(ROWS):

        for col in range(COLS):

            center = cell_center(
                row,
                col
            )

            pygame.draw.circle(
                surface,
                EMPTY_COLOR,
                center,
                radius
            )

    # pieces
    for row in range(ROWS):

        for col in range(COLS):

            value = board[row][col]

            if value == EMPTY:
                continue

            winning = (
                (row, col)
                in winning_positions
            )

            draw_piece(
                surface,
                cell_center(
                    row,
                    col
                ),
                value,
                radius,
                255,
                winning
            )


# =========================================================
# SCORE WINDOW
# =========================================================

def draw_top_ui(surface):

    # font_big = pygame.font.Font(
    #     None,
    #     48
    # )

    # font = pygame.font.Font(
    #     None,
    #     26
    # )

    title = fonts["heart"].render(
        "CONNECT FOUR",
        True,
        WHITE
    )

    surface.blit(
        title,
        title.get_rect(
            center=(
                WIDTH // 2,
                45
            )
        )
    )

    if current_turn == PLAYER:

        text = "YOUR TURN"

        color = PLAYER_COLOR

    else:

        text = "BOT TURN"

        color = BOT_COLOR

    turn = fonts["heart"].render(
        text,
        True,
        color
    )

    surface.blit(
        turn,
        (
            35,
            35
        )
    )

    level = fonts["heart"].render(
        f"LEVEL: {selected_level}",
        True,
        TEXT_GRAY
    )

    surface.blit(
        level,
        (
            WIDTH - level.get_width() - 35,
            35
        )
    )


# =========================================================
# TIMER UI
# =========================================================

def draw_timer(surface):

    # font = pygame.font.Font(
    #     None,
    #     24
    # )

    elapsed = (
        pygame.time.get_ticks()
        - game_start_time
    )

    total_seconds = elapsed // 1000

    minutes = total_seconds // 60
    seconds = total_seconds % 60

    text = fonts["heart"].render(
        f"TIME  {minutes:02d}:{seconds:02d}",
        True,
        TEXT_GRAY
    )

    surface.blit(
        text,
        text.get_rect(
            center=(
                WIDTH // 2,
                HEIGHT - 25
            )
        )
    )


# =========================================================
# EVALUATE WINDOW
# =========================================================

def evaluate_window(
    window,
    player
):

    score = 0

    opponent = (
        BOT
        if player == PLAYER
        else PLAYER
    )

    player_count = window.count(
        player
    )

    opponent_count = window.count(
        opponent
    )

    empty_count = window.count(
        EMPTY
    )

    if player_count == 4:

        score += 100

    elif (
        player_count == 3
        and empty_count == 1
    ):

        score += 5

    elif (
        player_count == 2
        and empty_count == 2
    ):

        score += 2

    if (
        opponent_count == 3
        and empty_count == 1
    ):

        score -= 4

    return score


# =========================================================
# SCORE POSITION
# =========================================================

def score_position(
    board_state,
    player
):

    score = 0

    # -----------------------------------------------------
    # CENTER
    # -----------------------------------------------------

    center_col = [
        board_state[row][COLS // 2]
        for row in range(ROWS)
    ]

    center_count = center_col.count(
        player
    )

    score += center_count * 3

    # -----------------------------------------------------
    # HORIZONTAL
    # -----------------------------------------------------

    for row in range(ROWS):

        row_array = board_state[row]

        for col in range(COLS - 3):

            window = row_array[
                col:col + 4
            ]

            score += evaluate_window(
                window,
                player
            )

    # -----------------------------------------------------
    # VERTICAL
    # -----------------------------------------------------

    for col in range(COLS):

        col_array = [
            board_state[row][col]
            for row in range(ROWS)
        ]

        for row in range(ROWS - 3):

            window = col_array[
                row:row + 4
            ]

            score += evaluate_window(
                window,
                player
            )

    # -----------------------------------------------------
    # DIAGONAL
    # -----------------------------------------------------

    for row in range(ROWS - 3):

        for col in range(COLS - 3):

            window = [
                board_state[row + i][col + i]
                for i in range(4)
            ]

            score += evaluate_window(
                window,
                player
            )

    # -----------------------------------------------------
    # OTHER DIAGONAL
    # -----------------------------------------------------

    for row in range(ROWS - 3):

        for col in range(COLS - 3):

            window = [
                board_state[
                    row + 3 - i
                ][
                    col + i
                ]
                for i in range(4)
            ]

            score += evaluate_window(
                window,
                player
            )

    return score


# =========================================================
# TERMINAL STATE
# =========================================================

def is_terminal(
    board_state
):

    player_win, _ = check_win(
        board_state,
        PLAYER
    )

    bot_win, _ = check_win(
        board_state,
        BOT
    )

    no_moves = (
        len(
            get_valid_columns(
                board_state
            )
        ) == 0
    )

    return (
        player_win
        or bot_win
        or no_moves
    )


# =========================================================
# MINIMAX
# =========================================================

def minimax(
    board_state,
    depth,
    alpha,
    beta,
    maximizing
):

    valid_columns = get_valid_columns(
        board_state
    )

    terminal = is_terminal(
        board_state
    )

    if depth == 0 or terminal:

        bot_win, _ = check_win(
            board_state,
            BOT
        )

        player_win, _ = check_win(
            board_state,
            PLAYER
        )

        if bot_win:

            return (
                1000000 + depth,
                None
            )

        if player_win:

            return (
                -1000000 - depth,
                None
            )

        if not valid_columns:

            return 0, None

        return (
            score_position(
                board_state,
                BOT
            ),
            None
        )

    if maximizing:

        value = -math.inf

        best_column = random.choice(
            valid_columns
        )

        # center first
        ordered_columns = sorted(
            valid_columns,
            key=lambda c: abs(
                c - COLS // 2
            )
        )

        for col in ordered_columns:

            row = get_available_row(
                board_state,
                col
            )

            temp_board = [
                r.copy()
                for r in board_state
            ]

            temp_board[row][col] = BOT

            new_score, _ = minimax(
                temp_board,
                depth - 1,
                alpha,
                beta,
                False
            )

            if new_score > value:

                value = new_score

                best_column = col

            alpha = max(
                alpha,
                value
            )

            if alpha >= beta:

                break

        return value, best_column

    else:

        value = math.inf

        best_column = random.choice(
            valid_columns
        )

        ordered_columns = sorted(
            valid_columns,
            key=lambda c: abs(
                c - COLS // 2
            )
        )

        for col in ordered_columns:

            row = get_available_row(
                board_state,
                col
            )

            temp_board = [
                r.copy()
                for r in board_state
            ]

            temp_board[row][col] = PLAYER

            new_score, _ = minimax(
                temp_board,
                depth - 1,
                alpha,
                beta,
                True
            )

            if new_score < value:

                value = new_score

                best_column = col

            beta = min(
                beta,
                value
            )

            if alpha >= beta:

                break

        return value, best_column


# =========================================================
# BOT MOVE
# =========================================================

def get_bot_move():

    if selected_level == LEVEL_EASY:

        valid = get_valid_columns(
            board
        )

        if not valid:
            return None

        # Easy:
        # mostly random
        if random.random() < 0.75:

            return random.choice(
                valid
            )

        # occasionally make smart move
        _, column = minimax(
            board,
            1,
            -math.inf,
            math.inf,
            True
        )

        return column

    depth = BOT_DEPTH[
        selected_level
    ]

    _, column = minimax(
        board,
        depth,
        -math.inf,
        math.inf,
        True
    )

    return column


# =========================================================
# ANIMATION SYSTEM
# =========================================================

animation_active = False

animation_player = None

animation_column = None
animation_target_row = None

animation_start_time = 0

ANIMATION_TIME = 450

animation_alpha = 0


def start_drop_animation(
    player,
    column
):

    global animation_active
    global animation_player
    global animation_column
    global animation_target_row
    global animation_start_time
    global animation_alpha

    row = get_available_row(
        board,
        column
    )

    if row is None:
        return False

    animation_active = True

    animation_player = player

    animation_column = column

    animation_target_row = row

    animation_start_time = (
        pygame.time.get_ticks()
    )

    animation_alpha = 0

    return True


# =========================================================
# UPDATE ANIMATION
# =========================================================

def update_animation():

    global animation_active
    global animation_alpha
    global current_turn
    global winner
    global winning_positions
    global game_state

    if not animation_active:
        return

    now = pygame.time.get_ticks()

    elapsed = (
        now - animation_start_time
    )

    progress = min(
        1.0,
        elapsed / ANIMATION_TIME
    )

    # ease out
    eased = 1 - (
        1 - progress
    ) ** 3

    animation_alpha = int(
        min(
            255,
            progress * 255
        )
    )

    if progress >= 1:

        board[
            animation_target_row
        ][
            animation_column
        ] = animation_player

        animation_active = False

        # check winner
        won, positions = check_win(
            board,
            animation_player
        )

        if won:

            winner = animation_player

            winning_positions = positions

            game_state = GAME_OVER

            return

        # draw?
        if not get_valid_columns(board):

            winner = 0

            game_state = GAME_OVER

            return

        # next player
        if animation_player == PLAYER:

            current_turn = BOT

        else:

            current_turn = PLAYER


# =========================================================
# DRAW ANIMATION
# =========================================================

def draw_animation(surface):

    if not animation_active:
        return

    now = pygame.time.get_ticks()

    elapsed = (
        now - animation_start_time
    )

    progress = min(
        1.0,
        elapsed / ANIMATION_TIME
    )

    eased = 1 - (
        1 - progress
    ) ** 3

    start_y = (
        BOARD_Y
        - CELL_SIZE * 1.1
    )

    target_x, target_y = cell_center(
        animation_target_row,
        animation_column
    )

    y = (
        start_y
        + (
            target_y - start_y
        ) * eased
    )

    radius = int(
        CELL_SIZE * 0.34
    )

    # Fade in
    alpha = int(
        min(
            255,
            progress * 255
        )
    )

    draw_piece(
        surface,
        (
            target_x,
            int(y)
        ),
        animation_player,
        radius,
        alpha
    )


# =========================================================
# LEVEL SELECT UI
# =========================================================

def draw_level_select(surface):

    surface.fill(BG)

    # title_font = pygame.font.Font(
    #     None,
    #     70
    # )

    # text_font = pygame.font.Font(
    #     None,
    #     30
    # )

    title = fonts["heart"].render(
        "CONNECT FOUR",
        True,
        WHITE
    )

    surface.blit(
        title,
        title.get_rect(
            center=(
                WIDTH // 2,
                120
            )
        )
    )

    subtitle = fonts["heart"].render(
        "CONNECT 4 TO WIN",
        True,
        TEXT_GRAY
    )

    surface.blit(
        subtitle,
        subtitle.get_rect(
            center=(
                WIDTH // 2,
                175
            )
        )
    )

    buttons = [
        (
            LEVEL_EASY,
            (65, 175, 100)
        ),
        (
            LEVEL_MEDIUM,
            (210, 160, 45)
        ),
        (
            LEVEL_HARD,
            (190, 55, 65)
        )
    ]

    button_width = 380
    button_height = 85

    gap = 25

    start_y = 245

    mouse = pygame.mouse.get_pos()

    for i, (level, color) in enumerate(buttons):

        rect = pygame.Rect(
            WIDTH // 2 - button_width // 2,
            start_y + i * (
                button_height + gap
            ),
            button_width,
            button_height
        )

        hover = rect.collidepoint(
            mouse
        )

        draw_color = tuple(
            min(
                255,
                c + 25
            )
            for c in color
        ) if hover else color

        pygame.draw.rect(
            surface,
            draw_color,
            rect,
            border_radius=18
        )

        pygame.draw.rect(
            surface,
            WHITE,
            rect,
            2,
            border_radius=18
        )

        text = fonts["heart"].render(
            level,
            True,
            WHITE
        )

        surface.blit(
            text,
            text.get_rect(
                center=rect.center
            )
        )

    info = pygame.font.Font(
        None,
        22
    ).render(
        "1 = EASY    2 = MEDIUM    3 = HARD",
        True,
        TEXT_GRAY
    )

    surface.blit(
        info,
        info.get_rect(
            center=(
                WIDTH // 2,
                HEIGHT - 45
            )
        )
    )


# =========================================================
# GAME OVER UI
# =========================================================

def draw_game_over(surface):

    overlay = pygame.Surface(
        (
            WIDTH,
            HEIGHT
        ),
        pygame.SRCALPHA
    )

    overlay.fill(
        (0, 0, 0, 175)
    )

    surface.blit(
        overlay,
        (0, 0)
    )

    # big_font = pygame.font.Font(
    #     None,
    #     75
    # )

    # small_font = pygame.font.Font(
    #     None,
    #     30
    # )

    if winner == PLAYER:

        text = "YOU WIN!"

        color = PLAYER_COLOR

    elif winner == BOT:

        text = "BOT WINS!"

        color = BOT_COLOR

    else:

        text = "DRAW!"

        color = WHITE

    title = fonts["heart"].render(
        text,
        True,
        color
    )

    surface.blit(
        title,
        title.get_rect(
            center=(
                WIDTH // 2,
                HEIGHT // 2 - 50
            )
        )
    )

    info = fonts["heart"].render(
        "R = RESTART     ESC = LEVEL SELECT",
        True,
        WHITE
    )

    surface.blit(
        info,
        info.get_rect(
            center=(
                WIDTH // 2,
                HEIGHT // 2 + 45
            )
        )
    )


# =========================================================
# MAIN DRAW
# =========================================================

def draw():

    screen.fill(BG)

    if game_state == LEVEL_SELECT:

        draw_level_select(
            screen
        )

        return

    draw_top_ui(
        screen
    )

    draw_board(
        screen
    )

    draw_animation(
        screen
    )

    draw_timer(
        screen
    )

    if game_state == GAME_OVER:

        draw_game_over(
            screen
        )


# =========================================================
# EVENT
# =========================================================

def handle_event(event):

    global selected_level
    global game_state

    # =====================================================
    # LEVEL SELECT
    # =====================================================

    if game_state == LEVEL_SELECT:

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_1:

                selected_level = LEVEL_EASY

                reset_game()

                game_state = PLAYING

            elif event.key == pygame.K_2:

                selected_level = LEVEL_MEDIUM

                reset_game()

                game_state = PLAYING

            elif event.key == pygame.K_3:

                selected_level = LEVEL_HARD

                reset_game()

                game_state = PLAYING

            elif event.key == pygame.K_ESCAPE:

                pygame.quit()

                sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if event.button != 1:
                return

            button_width = 380
            button_height = 85
            gap = 25
            start_y = 245

            levels = [
                LEVEL_EASY,
                LEVEL_MEDIUM,
                LEVEL_HARD
            ]

            for i, level in enumerate(
                levels
            ):

                rect = pygame.Rect(
                    WIDTH // 2
                    - button_width // 2,
                    start_y
                    + i * (
                        button_height
                        + gap
                    ),
                    button_width,
                    button_height
                )

                if rect.collidepoint(
                    event.pos
                ):

                    selected_level = level

                    reset_game()

                    game_state = PLAYING

                    return

        return

    # =====================================================
    # GAME OVER
    # =====================================================

    if game_state == GAME_OVER:

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_r:

                reset_game()

                game_state = PLAYING

            elif event.key == pygame.K_ESCAPE:

                game_state = LEVEL_SELECT

        return

    # =====================================================
    # PLAYING
    # =====================================================

    if game_state == PLAYING:

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_r:

                reset_game()

            elif event.key == pygame.K_ESCAPE:

                game_state = LEVEL_SELECT

            return

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button != 1:
                return

            # player only
            if current_turn != PLAYER:
                return

            # animation active
            if animation_active:
                return

            column = get_column_from_mouse(
                event.pos
            )

            if column is None:
                return

            if get_available_row(
                board,
                column
            ) is None:

                return

            start_drop_animation(
                PLAYER,
                column
            )


# =========================================================
# UPDATE
# =========================================================

bot_think_start = 0

BOT_THINK_DELAY = 350


def update():

    global bot_think_start

    if game_state != PLAYING:
        return

    # animation
    if animation_active:

        update_animation()

        return

    # =====================================================
    # BOT
    # =====================================================

    if current_turn == BOT:

        now = pygame.time.get_ticks()

        if bot_think_start == 0:

            bot_think_start = now

        if (
            now - bot_think_start
            >= BOT_THINK_DELAY
        ):

            column = get_bot_move()

            if column is not None:

                start_drop_animation(
                    BOT,
                    column
                )

            bot_think_start = 0

    else:

        bot_think_start = 0

















def CONNECT_FOUR_():
    update()

    draw()


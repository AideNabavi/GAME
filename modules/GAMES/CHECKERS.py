import pygame
import random
import math

from modules.font import *
# =========================================================
# GAME STATES
# =========================================================

LEVEL_SELECT = "CHECKERS_LEVEL_SELECT"
PLAYING = "CHECKERS_PLAYING"
GAME_OVER = "CHECKERS_GAME_OVER"


game_state = LEVEL_SELECT

# =========================================================
# BOARD
# =========================================================

BOARD_SIZE = 8

board = []

selected_piece = None
possible_moves = []

current_turn = "PLAYER"

winner = None

# =========================================================
# LEVEL
# =========================================================

selected_level = None

LEVEL_EASY = "EASY"
LEVEL_MEDIUM = "MEDIUM"
LEVEL_HARD = "HARD"

BOT_DEPTH = {
    LEVEL_EASY: 1,
    LEVEL_MEDIUM: 3,
    LEVEL_HARD: 5,
}

# =========================================================
# COLORS
# =========================================================

BOARD_LIGHT = (238, 218, 181)
BOARD_DARK = (130, 82, 48)

PLAYER_COLOR = (55, 110, 220)
PLAYER_KING_COLOR = (35, 75, 170)

BOT_COLOR = (210, 65, 65)
BOT_KING_COLOR = (155, 35, 35)

SELECT_COLOR = (255, 215, 50)
MOVE_COLOR = (70, 220, 120)

TEXT_COLOR = (245, 245, 245)

# =========================================================
# TIMING
# =========================================================

game_start_time = 0
bot_start_time = 0

BOT_DELAY = 500

# movement animation
moving_piece = None
move_start_pos = None
move_end_pos = None

move_animation_start = 0
MOVE_ANIMATION_TIME = 180

# =========================================================
# MULTI JUMP
# =========================================================

forced_piece = None


# =========================================================
# SCREEN SETUP
# =========================================================

def WIDTH_HEIGHT_gettter(screen_, WIDTH_, HEIGHT_):

    global screen
    global WIDTH
    global HEIGHT

    screen = screen_
    WIDTH = WIDTH_
    HEIGHT = HEIGHT_


# =========================================================
# RESET TIME
# =========================================================

def reset_time():

    global game_start_time
    global bot_start_time
    global move_animation_start

    now = pygame.time.get_ticks()

    game_start_time = now
    bot_start_time = now
    move_animation_start = 0


# =========================================================
# RESET GAME
# =========================================================

def reset_checkers():

    global board
    global selected_piece
    global possible_moves
    global current_turn
    global winner
    global game_state
    global moving_piece
    global move_start_pos
    global move_end_pos
    global forced_piece

    board = create_board()

    selected_piece = None
    possible_moves = []

    current_turn = "PLAYER"

    winner = None

    moving_piece = None
    move_start_pos = None
    move_end_pos = None

    forced_piece = None

    reset_time()

    game_state = PLAYING


# =========================================================
# CREATE BOARD
# =========================================================

def create_board():

    new_board = [
        [None for _ in range(BOARD_SIZE)]
        for _ in range(BOARD_SIZE)
    ]

    # BOT
    for row in range(3):

        for col in range(BOARD_SIZE):

            if (row + col) % 2 == 1:

                new_board[row][col] = {
                    "color": "BOT",
                    "king": False
                }

    # PLAYER
    for row in range(5, 8):

        for col in range(BOARD_SIZE):

            if (row + col) % 2 == 1:

                new_board[row][col] = {
                    "color": "PLAYER",
                    "king": False
                }

    return new_board


# =========================================================
# BOARD RECT
# =========================================================

def get_board_rect():

    size = min(
        WIDTH * 0.72,
        HEIGHT * 0.82
    )

    size = int(size)

    x = (WIDTH - size) // 2
    y = (HEIGHT - size) // 2

    return pygame.Rect(
        x,
        y,
        size,
        size
    )


# =========================================================
# CELL RECT
# =========================================================

def get_cell_rect(row, col):

    board_rect = get_board_rect()

    cell_size = board_rect.width // 8

    return pygame.Rect(
        board_rect.x + col * cell_size,
        board_rect.y + row * cell_size,
        cell_size,
        cell_size
    )


# =========================================================
# POSITION FROM MOUSE
# =========================================================

def mouse_to_cell(pos):

    board_rect = get_board_rect()

    if not board_rect.collidepoint(pos):
        return None

    cell_size = board_rect.width // 8

    col = int(
        (pos[0] - board_rect.x) /
        cell_size
    )

    row = int(
        (pos[1] - board_rect.y) /
        cell_size
    )

    if 0 <= row < 8 and 0 <= col < 8:

        return row, col

    return None


# =========================================================
# DRAW BOARD
# =========================================================

def draw_board():

    board_rect = get_board_rect()

    cell_size = board_rect.width // 8

    for row in range(8):

        for col in range(8):

            color = (
                BOARD_LIGHT
                if (row + col) % 2 == 0
                else BOARD_DARK
            )

            rect = pygame.Rect(
                board_rect.x + col * cell_size,
                board_rect.y + row * cell_size,
                cell_size,
                cell_size
            )

            pygame.draw.rect(
                screen,
                color,
                rect
            )


# =========================================================
# DRAW PIECE
# =========================================================

def draw_piece(row, col, piece):

    rect = get_cell_rect(row, col)

    center = rect.center

    radius = int(
        rect.width * 0.34
    )

    if piece["color"] == "PLAYER":

        color = (
            PLAYER_KING_COLOR
            if piece["king"]
            else PLAYER_COLOR
        )

    else:

        color = (
            BOT_KING_COLOR
            if piece["king"]
            else BOT_COLOR
        )

    # shadow
    pygame.draw.circle(
        screen,
        (40, 40, 40),
        (
            center[0] + 3,
            center[1] + 4
        ),
        radius
    )

    pygame.draw.circle(
        screen,
        color,
        center,
        radius
    )

    pygame.draw.circle(
        screen,
        (245, 245, 245),
        center,
        radius,
        3
    )

    # KING
    if piece["king"]:

        pygame.draw.circle(
            screen,
            (255, 215, 60),
            center,
            int(radius * 0.52),
            5
        )

        pygame.draw.circle(
            screen,
            (255, 215, 60),
            center,
            int(radius * 0.20)
        )


# =========================================================
# DRAW ALL PIECES
# =========================================================

def draw_pieces():

    for row in range(8):

        for col in range(8):

            piece = board[row][col]

            if piece is None:
                continue

            # animated piece
            if (
                moving_piece is not None
                and moving_piece["row"] == row
                and moving_piece["col"] == col
            ):
                continue

            draw_piece(
                row,
                col,
                piece
            )

    # animated piece
    update_move_animation()


# =========================================================
# DRAW SELECTION
# =========================================================

def draw_selection():

    if selected_piece is None:
        return

    row, col = selected_piece

    rect = get_cell_rect(
        row,
        col
    )

    pygame.draw.rect(
        screen,
        SELECT_COLOR,
        rect,
        5
    )

    for move in possible_moves:

        mr, mc = move

        rect = get_cell_rect(
            mr,
            mc
        )

        pygame.draw.circle(
            screen,
            MOVE_COLOR,
            rect.center,
            int(rect.width * 0.13)
        )


# =========================================================
# DIRECTIONS
# =========================================================

def get_directions(piece):

    if piece["king"]:

        return [
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1)
        ]

    if piece["color"] == "PLAYER":

        return [
            (-1, -1),
            (-1, 1)
        ]

    return [
        (1, -1),
        (1, 1)
    ]


# =========================================================
# VALID NORMAL MOVES
# =========================================================

def get_normal_moves(board_state, row, col):

    piece = board_state[row][col]

    if piece is None:
        return []

    moves = []

    for dr, dc in get_directions(piece):

        nr = row + dr
        nc = col + dc

        if not (
            0 <= nr < 8
            and 0 <= nc < 8
        ):
            continue

        if board_state[nr][nc] is None:

            moves.append(
                (nr, nc)
            )

    return moves


# =========================================================
# VALID CAPTURE MOVES
# =========================================================

def get_capture_moves(board_state, row, col):

    piece = board_state[row][col]

    if piece is None:
        return []

    moves = []

    for dr, dc in get_directions(piece):

        enemy_r = row + dr
        enemy_c = col + dc

        land_r = row + dr * 2
        land_c = col + dc * 2

        if not (
            0 <= land_r < 8
            and 0 <= land_c < 8
        ):
            continue

        if not (
            0 <= enemy_r < 8
            and 0 <= enemy_c < 8
        ):
            continue

        enemy = board_state[
            enemy_r
        ][
            enemy_c
        ]

        landing = board_state[
            land_r
        ][
            land_c
        ]

        if (
            enemy is not None
            and enemy["color"] != piece["color"]
            and landing is None
        ):

            moves.append(
                (land_r, land_c)
            )

    return moves


# =========================================================
# ALL CAPTURES
# =========================================================

def get_all_captures(board_state, color):

    captures = []

    for row in range(8):

        for col in range(8):

            piece = board_state[row][col]

            if (
                piece is not None
                and piece["color"] == color
            ):

                moves = get_capture_moves(
                    board_state,
                    row,
                    col
                )

                for move in moves:

                    captures.append(
                        (
                            (row, col),
                            move
                        )
                    )

    return captures


# =========================================================
# ALL LEGAL MOVES
# =========================================================

def get_all_moves(board_state, color):

    captures = get_all_captures(
        board_state,
        color
    )

    # CAPTURE IS MANDATORY
    if captures:
        return captures

    moves = []

    for row in range(8):

        for col in range(8):

            piece = board_state[row][col]

            if (
                piece is not None
                and piece["color"] == color
            ):

                for move in get_normal_moves(
                    board_state,
                    row,
                    col
                ):

                    moves.append(
                        (
                            (row, col),
                            move
                        )
                    )

    return moves


# =========================================================
# APPLY MOVE
# =========================================================

def apply_move(
    board_state,
    start,
    end
):

    new_board = [
        [
            None if p is None
            else p.copy()
            for p in row
        ]
        for row in board_state
    ]

    sr, sc = start
    er, ec = end

    piece = new_board[sr][sc]

    new_board[sr][sc] = None

    # capture
    if abs(er - sr) == 2:

        middle_r = (
            sr + er
        ) // 2

        middle_c = (
            sc + ec
        ) // 2

        new_board[
            middle_r
        ][
            middle_c
        ] = None

    new_board[er][ec] = piece

    # KING
    if (
        piece["color"] == "PLAYER"
        and er == 0
    ):

        piece["king"] = True

    elif (
        piece["color"] == "BOT"
        and er == 7
    ):

        piece["king"] = True

    return new_board


# =========================================================
# BOT EVALUATION
# =========================================================

def evaluate(board_state):

    score = 0

    for row in range(8):

        for col in range(8):

            piece = board_state[row][col]

            if piece is None:
                continue

            value = 3

            if piece["king"]:
                value = 6

            else:

                if piece["color"] == "BOT":

                    value += row * 0.15

                else:

                    value += (
                        7 - row
                    ) * 0.15

            if piece["color"] == "BOT":
                score += value
            else:
                score -= value

    return score


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

    bot_moves = get_all_moves(
        board_state,
        "BOT"
    )

    player_moves = get_all_moves(
        board_state,
        "PLAYER"
    )

    if depth == 0:

        return evaluate(
            board_state
        ), None

    if not bot_moves:

        return -10000, None

    if not player_moves:

        return 10000, None

    if maximizing:

        best_score = -math.inf
        best_move = None

        moves = bot_moves

        for move in moves:

            start, end = move

            new_board = apply_move(
                board_state,
                start,
                end
            )

            score, _ = minimax(
                new_board,
                depth - 1,
                alpha,
                beta,
                False
            )

            if score > best_score:

                best_score = score
                best_move = move

            alpha = max(
                alpha,
                best_score
            )

            if beta <= alpha:
                break

        return best_score, best_move

    else:

        best_score = math.inf
        best_move = None

        moves = player_moves

        for move in moves:

            start, end = move

            new_board = apply_move(
                board_state,
                start,
                end
            )

            score, _ = minimax(
                new_board,
                depth - 1,
                alpha,
                beta,
                True
            )

            if score < best_score:

                best_score = score
                best_move = move

            beta = min(
                beta,
                best_score
            )

            if beta <= alpha:
                break

        return best_score, best_move


# =========================================================
# BOT MOVE
# =========================================================

def bot_make_move():

    global board
    global current_turn
    global bot_start_time

    depth = BOT_DEPTH.get(
        selected_level,
        1
    )

    _, move = minimax(
        board,
        depth,
        -math.inf,
        math.inf,
        True
    )

    if move is None:

        end_game(
            "PLAYER"
        )

        return

    start, end = move

    board = apply_move(
        board,
        start,
        end
    )

    # check additional capture
    er, ec = end

    piece = board[er][ec]

    if piece is not None:

        extra_captures = get_capture_moves(
            board,
            er,
            ec
        )

        if (
            abs(end[0] - start[0]) == 2
            and extra_captures
        ):

            # Bot continues jumping
            bot_multi_jump(
                er,
                ec
            )

            return

    current_turn = "PLAYER"

    bot_start_time = pygame.time.get_ticks()

    check_game_over()


# =========================================================
# BOT MULTI JUMP
# =========================================================

def bot_multi_jump(row, col):

    global board
    global current_turn

    while True:

        captures = get_capture_moves(
            board,
            row,
            col
        )

        if not captures:
            break

        # choose best capture
        end = random.choice(
            captures
        )

        board = apply_move(
            board,
            (row, col),
            end
        )

        row, col = end

    current_turn = "PLAYER"

    check_game_over()


# =========================================================
# PLAYER MOVE
# =========================================================

def player_move(
    start,
    end
):

    global board
    global selected_piece
    global possible_moves
    global current_turn
    global forced_piece

    board = apply_move(
        board,
        start,
        end
    )

    sr, sc = start
    er, ec = end

    was_capture = (
        abs(er - sr) == 2
    )

    selected_piece = None
    possible_moves = []

    # MULTI JUMP
    if was_capture:

        next_captures = get_capture_moves(
            board,
            er,
            ec
        )

        if next_captures:

            forced_piece = (
                er,
                ec
            )

            selected_piece = (
                er,
                ec
            )

            possible_moves = (
                next_captures
            )

            return

    forced_piece = None

    current_turn = "BOT"

    check_game_over()


# =========================================================
# CHECK GAME OVER
# =========================================================

def check_game_over():

    global winner
    global game_state

    player_moves = get_all_moves(
        board,
        "PLAYER"
    )

    bot_moves = get_all_moves(
        board,
        "BOT"
    )

    player_exists = any(
        board[r][c] is not None
        and board[r][c]["color"] == "PLAYER"
        for r in range(8)
        for c in range(8)
    )

    bot_exists = any(
        board[r][c] is not None
        and board[r][c]["color"] == "BOT"
        for r in range(8)
        for c in range(8)
    )

    if not player_exists or not player_moves:

        end_game("BOT")

    elif not bot_exists or not bot_moves:

        end_game("PLAYER")


# =========================================================
# END GAME
# =========================================================

def end_game(player):

    global winner
    global game_state

    winner = player

    game_state = GAME_OVER


# =========================================================
# DRAW LEVEL SELECT
# =========================================================

def draw_level_select():

    screen.fill(
        (25, 25, 30)
    )

    # font_big = pygame.font.Font(
    #     None,
    #     max(40, int(HEIGHT * 0.07))
    # )

    # font = pygame.font.Font(
    #     None,
    #     max(28, int(HEIGHT * 0.04))
    # )

    title = fonts["heart"].render(
        "CHECKERS",
        True,
        (255, 255, 255)
    )

    screen.blit(
        title,
        title.get_rect(
            center=(
                WIDTH // 2,
                int(HEIGHT * 0.16)
            )
        )
    )

    levels = [
        ("EASY", LEVEL_EASY),
        ("MEDIUM", LEVEL_MEDIUM),
        ("HARD", LEVEL_HARD),
    ]

    button_w = min(
        400,
        int(WIDTH * 0.4)
    )

    button_h = 80

    gap = 25

    total_h = (
        len(levels) * button_h
        + (len(levels) - 1) * gap
    )

    start_y = (
        HEIGHT - total_h
    ) // 2

    for i, (text, level) in enumerate(levels):

        rect = pygame.Rect(
            WIDTH // 2 - button_w // 2,
            start_y + i * (button_h + gap),
            button_w,
            button_h
        )

        color = (
            (60, 170, 90)
            if level == LEVEL_EASY
            else
            (210, 160, 45)
            if level == LEVEL_MEDIUM
            else
            (190, 55, 55)
        )

        pygame.draw.rect(
            screen,
            color,
            rect,
            border_radius=18
        )

        text_surface = fonts["heart"].render(
            text,
            True,
            (255, 255, 255)
        )

        screen.blit(
            text_surface,
            text_surface.get_rect(
                center=rect.center
            )
        )


# =========================================================
# DRAW GAME UI
# =========================================================

def draw_game_ui():

    # font = pygame.font.Font(
    #     None,
    #     max(24, int(HEIGHT * 0.032))
    # )

    # turn
    turn_text = (
        "YOUR TURN"
        if current_turn == "PLAYER"
        else "BOT TURN"
    )

    turn_color = (
        PLAYER_COLOR
        if current_turn == "PLAYER"
        else BOT_COLOR
    )

    text = fonts["heart"].render(
        turn_text,
        True,
        turn_color
    )

    screen.blit(
        text,
        (
            25,
            25
        )
    )

    # level
    level_text = fonts["heart"].render(
        f"LEVEL: {selected_level}",
        True,
        TEXT_COLOR
    )

    screen.blit(
        level_text,
        (
            25,
            65
        )
    )

    # time
    elapsed = (
        pygame.time.get_ticks()
        - game_start_time
    )

    seconds = elapsed // 1000

    minutes = seconds // 60
    seconds %= 60

    time_text = fonts["heart"].render(
        f"TIME  {minutes:02d}:{seconds:02d}",
        True,
        TEXT_COLOR
    )

    screen.blit(
        time_text,
        (
            WIDTH - time_text.get_width() - 25,
            25
        )
    )


# =========================================================
# DRAW GAME OVER
# =========================================================

def draw_game_over():

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

    # font_big = pygame.font.Font(
    #     None,
    #     max(50, int(HEIGHT * 0.08))
    # )

    # font = pygame.font.Font(
    #     None,
    #     max(25, int(HEIGHT * 0.04))
    # )

    if winner == "PLAYER":

        text = "YOU WIN!"

    else:

        text = "BOT WINS!"

    title = fonts["heart"].render(
        text,
        True,
        (255, 220, 70)
    )

    screen.blit(
        title,
        title.get_rect(
            center=(
                WIDTH // 2,
                HEIGHT // 2 - 60
            )
        )
    )

    info = fonts["heart"].render(
        "Press R to restart",
        True,
        (255, 255, 255)
    )

    screen.blit(
        info,
        info.get_rect(
            center=(
                WIDTH // 2,
                HEIGHT // 2 + 40
            )
        )
    )


# =========================================================
# MOVE ANIMATION
# =========================================================

def start_move_animation(
    piece,
    start,
    end
):

    global moving_piece
    global move_start_pos
    global move_end_pos
    global move_animation_start

    moving_piece = piece.copy()

    move_start_pos = start
    move_end_pos = end

    move_animation_start = (
        pygame.time.get_ticks()
    )


def update_move_animation():

    global moving_piece

    if moving_piece is None:
        return

    now = pygame.time.get_ticks()

    elapsed = (
        now - move_animation_start
    )

    progress = min(
        1.0,
        elapsed / MOVE_ANIMATION_TIME
    )

    sr, sc = move_start_pos
    er, ec = move_end_pos

    start_rect = get_cell_rect(
        sr,
        sc
    )

    end_rect = get_cell_rect(
        er,
        ec
    )

    x = (
        start_rect.centerx
        + (
            end_rect.centerx
            - start_rect.centerx
        ) * progress
    )

    y = (
        start_rect.centery
        + (
            end_rect.centery
            - start_rect.centery
        ) * progress
    )

    radius = int(
        start_rect.width * 0.34
    )

    if moving_piece["color"] == "PLAYER":

        color = (
            PLAYER_KING_COLOR
            if moving_piece["king"]
            else PLAYER_COLOR
        )

    else:

        color = (
            BOT_KING_COLOR
            if moving_piece["king"]
            else BOT_COLOR
        )

    pygame.draw.circle(
        screen,
        (40, 40, 40),
        (
            int(x + 3),
            int(y + 4)
        ),
        radius
    )

    pygame.draw.circle(
        screen,
        color,
        (
            int(x),
            int(y)
        ),
        radius
    )

    pygame.draw.circle(
        screen,
        (245, 245, 245),
        (
            int(x),
            int(y)
        ),
        radius,
        3
    )

    if moving_piece["king"]:

        pygame.draw.circle(
            screen,
            (255, 215, 60),
            (
                int(x),
                int(y)
            ),
            int(radius * 0.5),
            5
        )

    if progress >= 1:

        moving_piece = None


# =========================================================
# DRAW CHECKERS
# =========================================================

def CHECKERS_():

    if game_state == LEVEL_SELECT:

        draw_level_select()

        return

    if game_state in (
        PLAYING,
        GAME_OVER
    ):

        draw_board()

        draw_selection()

        draw_pieces()

        draw_game_ui()

    if game_state == GAME_OVER:

        draw_game_over()


# =========================================================
# EVENT CHECKERS
# =========================================================

def event_checkers(event):

    global selected_level
    global game_state
    global selected_piece
    global possible_moves

    # =====================================================
    # LEVEL SELECT
    # =====================================================

    if game_state == LEVEL_SELECT:

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:

                return

            if event.key == pygame.K_1:

                selected_level = LEVEL_EASY
                reset_checkers()

            elif event.key == pygame.K_2:

                selected_level = LEVEL_MEDIUM
                reset_checkers()

            elif event.key == pygame.K_3:

                selected_level = LEVEL_HARD
                reset_checkers()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button != 1:
                return

            mouse = event.pos

            button_w = min(
                400,
                int(WIDTH * 0.4)
            )

            button_h = 80

            gap = 25

            total_h = (
                3 * button_h
                + 2 * gap
            )

            start_y = (
                HEIGHT - total_h
            ) // 2

            levels = [
                LEVEL_EASY,
                LEVEL_MEDIUM,
                LEVEL_HARD
            ]

            for i, level in enumerate(levels):

                rect = pygame.Rect(
                    WIDTH // 2 - button_w // 2,
                    start_y + i * (
                        button_h + gap
                    ),
                    button_w,
                    button_h
                )

                if rect.collidepoint(mouse):

                    selected_level = level

                    reset_checkers()

                    return

        return

    # =====================================================
    # GAME OVER
    # =====================================================

    if game_state == GAME_OVER:

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_r:

                reset_checkers()

            elif event.key == pygame.K_ESCAPE:

                game_state = LEVEL_SELECT

        return

    # =====================================================
    # PLAYING
    # =====================================================

    if game_state != PLAYING:
        return

    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_ESCAPE:

            game_state = LEVEL_SELECT

            return

        if event.key == pygame.K_r:

            reset_checkers()

            return

    # =====================================================
    # PLAYER INPUT
    # =====================================================

    if event.type == pygame.MOUSEBUTTONDOWN:

        if event.button != 1:
            return

        if current_turn != "PLAYER":
            return

        if moving_piece is not None:
            return

        cell = mouse_to_cell(
            event.pos
        )

        if cell is None:
            return

        row, col = cell

        piece = board[row][col]

        # ================================================
        # FORCED MULTI JUMP
        # ================================================

        if forced_piece is not None:

            if cell in possible_moves:

                player_move(
                    forced_piece,
                    cell
                )

            return

        # ================================================
        # SELECT MOVE
        # ================================================

        if selected_piece is not None:

            if cell in possible_moves:

                start = selected_piece

                player_move(
                    start,
                    cell
                )

                return

        # ================================================
        # SELECT PLAYER PIECE
        # ================================================

        if (
            piece is not None
            and piece["color"] == "PLAYER"
        ):

            all_captures = get_all_captures(
                board,
                "PLAYER"
            )

            piece_captures = (
                get_capture_moves(
                    board,
                    row,
                    col
                )
            )

            # mandatory capture
            if all_captures:

                if not piece_captures:

                    return

                selected_piece = (
                    row,
                    col
                )

                possible_moves = (
                    piece_captures
                )

            else:

                selected_piece = (
                    row,
                    col
                )

                possible_moves = (
                    get_normal_moves(
                        board,
                        row,
                        col
                    )
                )


# =========================================================
# UPDATE CHECKERS
# =========================================================
# این برای حلقه قبل از تابع درو چکر باید رسم بشه 
def update_checkers():

    global bot_start_time

    if game_state != PLAYING:
        return

    if moving_piece is not None:
        return

    if current_turn == "BOT":

        now = pygame.time.get_ticks()

        if (
            now - bot_start_time
            >= BOT_DELAY
        ):

            bot_make_move()
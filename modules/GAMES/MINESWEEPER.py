# import pygame
# import random

# from modules.font import *
# # =========================
# # SETTINGS
# # =========================

# HEIGHT = None
# WIDTH = None
# screen = None


# def WIDTH_HEIGHT_gettter(screen_, WIDTH_, HEIGHT_):

#     global WIDTH
#     global HEIGHT
#     global screen

#     WIDTH = WIDTH_
#     HEIGHT = HEIGHT_
#     screen = screen_


# # Colors
# BG = (30, 45, 30)
# BUTTON = (80, 110, 70)
# BUTTON_HOVER = (110, 145, 90)
# HIDDEN = (100, 125, 85)
# OPEN = (220, 205, 165)
# GRID = (40, 40, 40)
# WHITE = (255, 255, 255)
# BLACK = (20, 20, 20)
# RED = (190, 50, 50)


# # =========================
# # GAME DATA
# # =========================

# sizes = {
#     "8x8": (8, 8),
#     "15x15": (15, 15)
# }

# bombs = {
#     "Easy": {
#         "8x8": 8,
#         "15x15": 20
#     },
#     "Medium": {
#         "8x8": 12,
#         "15x15": 35
#     },
#     "Hard": {
#         "8x8": 16,
#         "15x15": 50
#     }
# }


# # =========================
# # BUTTON
# # =========================

# def button(text, rect):
#     mouse = pygame.mouse.get_pos()

#     color = BUTTON_HOVER if rect.collidepoint(mouse) else BUTTON

#     pygame.draw.rect(screen, color, rect, border_radius=12)

#     t = fonts["heart"].render(text, True, WHITE)
#     screen.blit(t, t.get_rect(center=rect.center))


# # =========================
# # CREATE BOARD
# # =========================

# def create_board(rows, cols, bomb_count):

#     board = [[0 for _ in range(cols)] for _ in range(rows)]

#     positions = random.sample(
#         [(r, c) for r in range(rows) for c in range(cols)],
#         bomb_count
#     )

#     for r, c in positions:
#         board[r][c] = -1

#     # Numbers
#     for r in range(rows):
#         for c in range(cols):

#             if board[r][c] == -1:
#                 continue

#             count = 0

#             for dr in (-1, 0, 1):
#                 for dc in (-1, 0, 1):

#                     nr = r + dr
#                     nc = c + dc

#                     if 0 <= nr < rows and 0 <= nc < cols:
#                         if board[nr][nc] == -1:
#                             count += 1

#             board[r][c] = count

#     return board


# # =========================
# # OPEN CELL
# # =========================

# def open_cell(row, col):

#     global game_over, win

#     if opened[row][col] or game_over or win:
#         return

#     opened[row][col] = True

#     # Bomb
#     if board[row][col] == -1:

#         game_over = True

#         # Show all bombs
#         for r in range(rows):
#             for c in range(cols):

#                 if board[r][c] == -1:
#                     opened[r][c] = True

#         return

#     # Check win
#     safe = rows * cols - bomb_count

#     found = sum(
#         opened[r][c] and board[r][c] != -1
#         for r in range(rows)
#         for c in range(cols)
#     )

#     if found == safe:
#         win = True


# # =========================
# # DRAW BOARD
# # =========================

# def draw_board():

#     screen.fill(BG)

#     # Timer
#     seconds = (pygame.time.get_ticks() - start_time) // 1000

#     timer = fonts["heart"].render(
#         f"Time: {seconds}",
#         True,
#         WHITE
#     )

#     screen.blit(timer, (20, 20))

#     # Board size
#     cell = min(
#         700 // cols,
#         650 // rows
#     )

#     board_width = cols * cell
#     board_height = rows * cell

#     start_x = (WIDTH - board_width) // 2
#     start_y = 80

#     for r in range(rows):
#         for c in range(cols):

#             x = start_x + c * cell
#             y = start_y + r * cell

#             rect = pygame.Rect(
#                 x,
#                 y,
#                 cell,
#                 cell
#             )

#             if opened[r][c]:

#                 if board[r][c] == -1:

#                     pygame.draw.rect(
#                         screen,
#                         RED,
#                         rect
#                     )

#                     text = "B"

#                 else:

#                     pygame.draw.rect(
#                         screen,
#                         OPEN,
#                         rect
#                     )

#                     text = str(board[r][c])

#                 t = pygame.font.SysFont(
#                     None,
#                     max(20, cell // 2)
#                 ).render(
#                     text,
#                     True,
#                     BLACK
#                 )

#                 screen.blit(
#                     t,
#                     t.get_rect(center=rect.center)
#                 )

#             else:

#                 pygame.draw.rect(
#                     screen,
#                     HIDDEN,
#                     rect
#                 )

#             pygame.draw.rect(
#                 screen,
#                 GRID,
#                 rect,
#                 2
#             )

#     # Result
#     if game_over or win:

#         message = "YOU WIN!" if win else "BOOM!"

#         t = fonts["heart"].render(
#             message,
#             True,
#             WHITE
#         )

#         screen.blit(
#             t,
#             t.get_rect(
#                 center=(WIDTH // 2, 45)
#             )
#         )


# # =========================
# # MENU
# # =========================

# def menu():

#     global rows, cols
#     global bomb_count
#     global board, opened
#     global game_over, win
#     global start_time

#     # Size menu
#     while True:

#         screen.fill(BG)

#         title = fonts["heart"].render(
#             "HIDDEN BOMBS",
#             True,
#             WHITE
#         )

#         screen.blit(
#             title,
#             title.get_rect(
#                 center=(WIDTH // 2, 120)
#             )
#         )

#         b1 = pygame.Rect(300, 250, 300, 70)
#         b2 = pygame.Rect(300, 350, 300, 70)

#         button("8 x 8", b1)
#         button("15 x 15", b2)

#         pygame.display.flip()

#         for event in pygame.event.get():

#             if event.type == pygame.QUIT:
#                 return False

#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     return False

#             if event.type == pygame.MOUSEBUTTONDOWN:

#                 if event.button == 1:

#                     if b1.collidepoint(event.pos):
#                         rows, cols = sizes["8x8"]
#                         selected_size = "8x8"
#                         break

#                     if b2.collidepoint(event.pos):
#                         rows, cols = sizes["15x15"]
#                         selected_size = "15x15"
#                         break

#         else:
#             clock.tick(60)
#             continue

#         break

#     # Difficulty menu
#     while True:

#         screen.fill(BG)

#         title = fonts["heart"].render(
#             "DIFFICULTY",
#             True,
#             WHITE
#         )

#         screen.blit(
#             title,
#             title.get_rect(
#                 center=(WIDTH // 2, 120)
#             )
#         )

#         easy = pygame.Rect(300, 230, 300, 70)
#         medium = pygame.Rect(300, 330, 300, 70)
#         hard = pygame.Rect(300, 430, 300, 70)

#         button("EASY", easy)
#         button("MEDIUM", medium)
#         button("HARD", hard)

#         pygame.display.flip()

#         for event in pygame.event.get():

#             if event.type == pygame.QUIT:
#                 return False

#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     return False

#             if event.type == pygame.MOUSEBUTTONDOWN:

#                 if event.button == 1:

#                     if easy.collidepoint(event.pos):
#                         difficulty = "Easy"
#                         break

#                     if medium.collidepoint(event.pos):
#                         difficulty = "Medium"
#                         break

#                     if hard.collidepoint(event.pos):
#                         difficulty = "Hard"
#                         break

#         else:
#             clock.tick(60)
#             continue

#         break

#     # Start game
#     bomb_count = bombs[difficulty][selected_size]

#     board = create_board(
#         rows,
#         cols,
#         bomb_count
#     )

#     opened = [
#         [False] * cols
#         for _ in range(rows)
#     ]

#     game_over = False
#     win = False

#     start_time = pygame.time.get_ticks()

#     return True


# # =========================
# # MAIN
# # =========================

# # running = True

# # while running:

# def 
#     if not menu():
#         break

#     while True:

#         for event in pygame.event.get():

#             if event.type == pygame.QUIT:
#                 running = False
#                 break

#             if event.type == pygame.KEYDOWN:

#                 if event.key == pygame.K_ESCAPE:
#                     running = False
#                     break

#                 # Restart
#                 if event.key == pygame.K_r:

#                     board = create_board(
#                         rows,
#                         cols,
#                         bomb_count
#                     )

#                     opened = [
#                         [False] * cols
#                         for _ in range(rows)
#                     ]

#                     game_over = False
#                     win = False

#                     start_time = pygame.time.get_ticks()

#             if event.type == pygame.MOUSEBUTTONDOWN:

#                 if event.button == 1:

#                     # Board dimensions
#                     cell = min(
#                         700 // cols,
#                         650 // rows
#                     )

#                     board_width = cols * cell
#                     board_height = rows * cell

#                     start_x = (WIDTH - board_width) // 2
#                     start_y = 80

#                     mx, my = event.pos

#                     col = (mx - start_x) // cell
#                     row = (my - start_y) // cell

#                     if (
#                         0 <= row < rows
#                         and 0 <= col < cols
#                     ):
#                         open_cell(row, col)

#         if not running:
#             break

#         draw_board()

#         pygame.display.flip()
#         clock.tick(60)

#         # After win/loss:
#         if game_over or win:

#             # Wait until R / ESC / mouse
#             pass

#     if not running:
#         break




# def MINESWEPEER():
# def event_MINESWEPEER():













import pygame
import random

from modules.font import *


# =========================================================
# SETTINGS
# =========================================================

HEIGHT = None
WIDTH = None
screen = None


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

BG = (30, 45, 30)

BUTTON = (80, 110, 70)
BUTTON_HOVER = (110, 145, 90)

HIDDEN = (100, 125, 85)
OPEN = (220, 205, 165)

GRID = (40, 40, 40)

WHITE = (255, 255, 255)
BLACK = (20, 20, 20)

RED = (190, 50, 50)


# =========================================================
# GAME SETTINGS
# =========================================================

sizes = {
    "8x8": (8, 8),
    "15x15": (15, 15)
}


bombs = {

    "Easy": {
        "8x8": 8,
        "15x15": 20
    },

    "Medium": {
        "8x8": 12,
        "15x15": 35
    },

    "Hard": {
        "8x8": 16,
        "15x15": 50
    }
}


# =========================================================
# GAME STATES
# =========================================================

LEVEL_SELECT = "LEVEL_SELECT"
DIFFICULTY_SELECT = "DIFFICULTY_SELECT"
PLAYING = "PLAYING"
GAME_OVER = "GAME_OVER"
WIN = "WIN"


game_state = LEVEL_SELECT


# =========================================================
# GAME DATA
# =========================================================

rows = 0
cols = 0

selected_size = None
difficulty = None

bomb_count = 0

board = []
opened = []

start_time = 0


# =========================================================
# BUTTON
# =========================================================

def button(text, rect):

    mouse = pygame.mouse.get_pos()

    color = (
        BUTTON_HOVER
        if rect.collidepoint(mouse)
        else BUTTON
    )

    pygame.draw.rect(
        screen,
        color,
        rect,
        border_radius=12
    )

    t = fonts["heart"].render(
        text,
        True,
        WHITE
    )

    screen.blit(
        t,
        t.get_rect(
            center=rect.center
        )
    )


# =========================================================
# CREATE BOARD
# =========================================================

def create_board(
    rows_,
    cols_,
    bomb_count_
):

    board_ = [
        [0 for _ in range(cols_)]
        for _ in range(rows_)
    ]

    positions = random.sample(
        [
            (r, c)
            for r in range(rows_)
            for c in range(cols_)
        ],
        bomb_count_
    )

    for r, c in positions:

        board_[r][c] = -1

    # =====================================================
    # NUMBERS
    # =====================================================

    for r in range(rows_):

        for c in range(cols_):

            if board_[r][c] == -1:
                continue

            count = 0

            for dr in (-1, 0, 1):

                for dc in (-1, 0, 1):

                    nr = r + dr
                    nc = c + dc

                    if (
                        0 <= nr < rows_
                        and
                        0 <= nc < cols_
                    ):

                        if board_[nr][nc] == -1:

                            count += 1

            board_[r][c] = count

    return board_


# =========================================================
# START GAME
# =========================================================

def start_minesweeper():

    global board
    global opened
    global bomb_count
    global start_time
    global game_state

    bomb_count = bombs[
        difficulty
    ][
        selected_size
    ]

    board = create_board(
        rows,
        cols,
        bomb_count
    )

    opened = [
        [False] * cols
        for _ in range(rows)
    ]

    start_time = pygame.time.get_ticks()

    game_state = PLAYING


# =========================================================
# RESET GAME
# =========================================================

def reset_MINESWEEPER():

    global rows
    global cols
    global selected_size
    global difficulty
    global bomb_count
    global board
    global opened
    global start_time
    global game_state

    rows = 0
    cols = 0

    selected_size = None
    difficulty = None

    bomb_count = 0

    board = []
    opened = []

    start_time = 0

    game_state = LEVEL_SELECT


# =========================================================
# RESTART SAME GAME
# =========================================================

def restart_minesweeper():

    if (
        selected_size is None
        or
        difficulty is None
    ):
        return

    start_minesweeper()


# =========================================================
# OPEN CELL
# =========================================================

def open_cell(row, col):

    global game_state

    if game_state != PLAYING:
        return

    if opened[row][col]:
        return

    opened[row][col] = True

    # =====================================================
    # BOMB
    # =====================================================

    if board[row][col] == -1:

        game_state = GAME_OVER

        # Show all bombs

        for r in range(rows):

            for c in range(cols):

                if board[r][c] == -1:

                    opened[r][c] = True

        return

    # =====================================================
    # CHECK WIN
    # =====================================================

    safe = (
        rows * cols
        - bomb_count
    )

    found = sum(
        opened[r][c]
        and board[r][c] != -1

        for r in range(rows)

        for c in range(cols)
    )

    if found == safe:

        game_state = WIN


# =========================================================
# BOARD RECT DATA
# =========================================================

def get_board_data():

    cell = min(
        700 // cols,
        650 // rows
    )

    board_width = cols * cell
    board_height = rows * cell

    start_x = (
        WIDTH - board_width
    ) // 2

    start_y = 80

    return (
        cell,
        board_width,
        board_height,
        start_x,
        start_y
    )


# =========================================================
# DRAW BOARD
# =========================================================

def draw_board():

    screen.fill(BG)

    # =====================================================
    # TIMER
    # =====================================================

    seconds = (
        pygame.time.get_ticks()
        - start_time
    ) // 1000

    timer = fonts["heart"].render(
        f"Time: {seconds}",
        True,
        WHITE
    )

    screen.blit(
        timer,
        (20, 20)
    )

    # =====================================================
    # BOARD
    # =====================================================

    (
        cell,
        board_width,
        board_height,
        start_x,
        start_y
    ) = get_board_data()

    for r in range(rows):

        for c in range(cols):

            x = start_x + c * cell
            y = start_y + r * cell

            rect = pygame.Rect(
                x,
                y,
                cell,
                cell
            )

            # =================================================
            # OPEN
            # =================================================

            if opened[r][c]:

                if board[r][c] == -1:

                    pygame.draw.rect(
                        screen,
                        RED,
                        rect
                    )

                    text = "B"

                else:

                    pygame.draw.rect(
                        screen,
                        OPEN,
                        rect
                    )

                    text = str(
                        board[r][c]
                    )

                number_font = pygame.font.SysFont(
                    None,
                    max(
                        20,
                        cell // 2
                    )
                )

                t = number_font.render(
                    text,
                    True,
                    BLACK
                )

                screen.blit(
                    t,
                    t.get_rect(
                        center=rect.center
                    )
                )

            # =================================================
            # HIDDEN
            # =================================================

            else:

                pygame.draw.rect(
                    screen,
                    HIDDEN,
                    rect
                )

            # =================================================
            # GRID
            # =================================================

            pygame.draw.rect(
                screen,
                GRID,
                rect,
                2
            )

    # =====================================================
    # RESULT
    # =====================================================

    if game_state == WIN:

        message = "YOU WIN!"

        t = fonts["heart"].render(
            message,
            True,
            WHITE
        )

        screen.blit(
            t,
            t.get_rect(
                center=(
                    WIDTH // 2,
                    45
                )
            )
        )

    elif game_state == GAME_OVER:

        message = "BOOM!"

        t = fonts["heart"].render(
            message,
            True,
            WHITE
        )

        screen.blit(
            t,
            t.get_rect(
                center=(
                    WIDTH // 2,
                    45
                )
            )
        )


# =========================================================
# DRAW LEVEL SELECT
# =========================================================

def draw_level_select():

    screen.fill(BG)

    title = fonts["heart"].render(
        "HIDDEN BOMBS",
        True,
        WHITE
    )

    screen.blit(
        title,
        title.get_rect(
            center=(
                WIDTH // 2,
                120
            )
        )
    )

    b1 = pygame.Rect(
        WIDTH // 2 - 150,
        250,
        300,
        70
    )

    b2 = pygame.Rect(
        WIDTH // 2 - 150,
        350,
        300,
        70
    )

    button(
        "8 x 8",
        b1
    )

    button(
        "15 x 15",
        b2
    )


# =========================================================
# DRAW DIFFICULTY
# =========================================================

def draw_difficulty_select():

    screen.fill(BG)

    title = fonts["heart"].render(
        "DIFFICULTY",
        True,
        WHITE
    )

    screen.blit(
        title,
        title.get_rect(
            center=(
                WIDTH // 2,
                120
            )
        )
    )

    easy = pygame.Rect(
        WIDTH // 2 - 150,
        230,
        300,
        70
    )

    medium = pygame.Rect(
        WIDTH // 2 - 150,
        330,
        300,
        70
    )

    hard = pygame.Rect(
        WIDTH // 2 - 150,
        430,
        300,
        70
    )

    button(
        "EASY",
        easy
    )

    button(
        "MEDIUM",
        medium
    )

    button(
        "HARD",
        hard
    )


# =========================================================
# EVENT HANDLER
# =========================================================

def event_MINESWEEPER(event):

    global rows
    global cols
    global selected_size
    global difficulty
    global game_state

    # =====================================================
    # LEVEL SELECT
    # =====================================================

    if game_state == LEVEL_SELECT:

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:

                reset_MINESWEEPER()

                return

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                b1 = pygame.Rect(
                    WIDTH // 2 - 150,
                    250,
                    300,
                    70
                )

                b2 = pygame.Rect(
                    WIDTH // 2 - 150,
                    350,
                    300,
                    70
                )

                if b1.collidepoint(
                    event.pos
                ):

                    rows, cols = sizes["8x8"]

                    selected_size = "8x8"

                    game_state = (
                        DIFFICULTY_SELECT
                    )

                    return

                if b2.collidepoint(
                    event.pos
                ):

                    rows, cols = sizes["15x15"]

                    selected_size = "15x15"

                    game_state = (
                        DIFFICULTY_SELECT
                    )

                    return

    # =====================================================
    # DIFFICULTY SELECT
    # =====================================================

    elif game_state == DIFFICULTY_SELECT:

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:

                reset_MINESWEEPER()

                return

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                easy = pygame.Rect(
                    WIDTH // 2 - 150,
                    230,
                    300,
                    70
                )

                medium = pygame.Rect(
                    WIDTH // 2 - 150,
                    330,
                    300,
                    70
                )

                hard = pygame.Rect(
                    WIDTH // 2 - 150,
                    430,
                    300,
                    70
                )

                if easy.collidepoint(
                    event.pos
                ):

                    difficulty = "Easy"

                    start_minesweeper()

                    return

                if medium.collidepoint(
                    event.pos
                ):

                    difficulty = "Medium"

                    start_minesweeper()

                    return

                if hard.collidepoint(
                    event.pos
                ):

                    difficulty = "Hard"

                    start_minesweeper()

                    return

    # =====================================================
    # PLAYING
    # =====================================================

    elif game_state == PLAYING:

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:

                reset_MINESWEEPER()

                return

            if event.key == pygame.K_r:

                restart_minesweeper()

                return

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                (
                    cell,
                    board_width,
                    board_height,
                    start_x,
                    start_y
                ) = get_board_data()

                mx, my = event.pos

                col = (
                    mx - start_x
                ) // cell

                row = (
                    my - start_y
                ) // cell

                if (
                    0 <= row < rows
                    and
                    0 <= col < cols
                ):

                    open_cell(
                        row,
                        col
                    )

                    return

    # =====================================================
    # GAME OVER / WIN
    # =====================================================

    elif (
        game_state == GAME_OVER
        or
        game_state == WIN
    ):

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_r:

                restart_minesweeper()

                return

            if event.key == pygame.K_ESCAPE:

                reset_MINESWEEPER()

                return


# =========================================================
# MAIN DRAW FUNCTION
# =========================================================

def MINESWEEPER_():

    if game_state == LEVEL_SELECT:

        draw_level_select()

    elif game_state == DIFFICULTY_SELECT:

        draw_difficulty_select()

    elif (
        game_state == PLAYING
        or
        game_state == GAME_OVER
        or
        game_state == WIN
    ):

        draw_board()
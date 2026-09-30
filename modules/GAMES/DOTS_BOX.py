# import pygame
# import random
# import math
# from modules.font import *
# # =========================================================
# # SETTINGS
# # =========================================================
# WIDTH = 1080
# HEIGHT = 720
# screen = None


# def WIDTH_HEIGHT_gettter(screen_, WIDTH_, HEIGHT_):

#     global WIDTH
#     global HEIGHT
#     global screen

#     WIDTH = WIDTH_
#     WIDTH1 = WIDTH_
#     HEIGHT = HEIGHT_
#     HEIGHT1 = HEIGHT_
#     screen = screen_
# # FPS = 60

# DOTS = 10                 # 10 x 10 dots
# BOXES = DOTS - 1          # 9 x 9 boxes

# DOT_RADIUS = 7

# PLAYER = "PLAYER"
# BOT = "BOT"

# PLAYER_COLOR = (45, 120, 255)
# BOT_COLOR = (235, 65, 65)

# DOT_COLOR = (35, 35, 35)
# BG_COLOR = (245, 245, 245)
# BOX_BORDER_COLOR = (210, 210, 210)

# LINE_WIDTH = 8

# LINE_ANIMATION_TIME = 180
# BOT_DELAY = 450

# # =========================================================
# # PYGAME
# # =========================================================

# # pygame.init()

# # screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# # WIDTH, HEIGHT = screen.get_size()

# # pygame.display.set_caption("Dots & Boxes")

# # clock = pygame.time.Clock()

# # font = pygame.font.SysFont("Arial", 32, bold=True)
# # small_font = pygame.font.SysFont("Arial", 22, bold=True)
# # big_font = pygame.font.SysFont("Arial", 60, bold=True)

# # =========================================================
# # BOARD POSITION
# # =========================================================

# BOARD_SIZE = min(WIDTH, HEIGHT) - 220

# START_X = (WIDTH - BOARD_SIZE) // 2
# START_Y = 130

# CELL = BOARD_SIZE / (DOTS - 1)

# # =========================================================
# # GAME DATA
# # =========================================================

# horizontal = [
#     [False for _ in range(DOTS - 1)]
#     for _ in range(DOTS)
# ]

# vertical = [
#     [False for _ in range(DOTS)]
#     for _ in range(DOTS - 1)
# ]

# horizontal_owner = [
#     [None for _ in range(DOTS - 1)]
#     for _ in range(DOTS)
# ]

# vertical_owner = [
#     [None for _ in range(DOTS)]
#     for _ in range(DOTS - 1)
# ]

# boxes = [
#     [None for _ in range(BOXES)]
#     for _ in range(BOXES)
# ]

# player_score = 0
# bot_score = 0

# current_turn = PLAYER

# game_over = False

# # =========================================================
# # ANIMATION
# # =========================================================

# animation = None

# # {
# #     "type": "H" / "V",
# #     "r": row,
# #     "c": col,
# #     "owner": PLAYER/BOT,
# #     "start": milliseconds
# # }

# bot_wait_start = None

# # =========================================================
# # HELPERS
# # =========================================================


# def point_position(row, col):

#     x = START_X + col * CELL
#     y = START_Y + row * CELL

#     return int(x), int(y)


# def get_color(owner):

#     if owner == PLAYER:
#         return PLAYER_COLOR

#     return BOT_COLOR


# def line_is_available(line_type, row, col):

#     if line_type == "H":
#         return not horizontal[row][col]

#     return not vertical[row][col]


# # =========================================================
# # BOX CHECK
# # =========================================================

# def check_completed_boxes(line_type, row, col):

#     completed = []

#     if line_type == "H":

#         # Box ABOVE
#         if row > 0:

#             box_r = row - 1
#             box_c = col

#             if (
#                 horizontal[box_r][box_c]
#                 and horizontal[box_r + 1][box_c]
#                 and vertical[box_r][box_c]
#                 and vertical[box_r][box_c + 1]
#             ):
#                 if boxes[box_r][box_c] is None:
#                     completed.append((box_r, box_c))

#         # Box BELOW
#         if row < BOXES:

#             box_r = row
#             box_c = col

#             if (
#                 horizontal[box_r][box_c]
#                 and horizontal[box_r + 1][box_c]
#                 and vertical[box_r][box_c]
#                 and vertical[box_r][box_c + 1]
#             ):
#                 if boxes[box_r][box_c] is None:
#                     completed.append((box_r, box_c))

#     else:

#         # Box LEFT
#         if col > 0:

#             box_r = row
#             box_c = col - 1

#             if (
#                 vertical[box_r][box_c]
#                 and vertical[box_r][box_c + 1]
#                 and horizontal[box_r][box_c]
#                 and horizontal[box_r + 1][box_c]
#             ):
#                 if boxes[box_r][box_c] is None:
#                     completed.append((box_r, box_c))

#         # Box RIGHT
#         if col < BOXES:

#             box_r = row
#             box_c = col

#             if (
#                 vertical[box_r][box_c]
#                 and vertical[box_r][box_c + 1]
#                 and horizontal[box_r][box_c]
#                 and horizontal[box_r + 1][box_c]
#             ):
#                 if boxes[box_r][box_c] is None:
#                     completed.append((box_r, box_c))

#     return completed


# # =========================================================
# # APPLY MOVE
# # =========================================================

# def apply_move(line_type, row, col, owner):

#     global player_score
#     global bot_score
#     global current_turn
#     global game_over

#     if line_type == "H":

#         horizontal[row][col] = True
#         horizontal_owner[row][col] = owner

#     else:

#         vertical[row][col] = True
#         vertical_owner[row][col] = owner

#     completed = check_completed_boxes(
#         line_type,
#         row,
#         col
#     )

#     for box_r, box_c in completed:

#         boxes[box_r][box_c] = owner

#         if owner == PLAYER:
#             player_score += 1
#         else:
#             bot_score += 1

#     # -----------------------------------------------------
#     # If a box was completed:
#     # same player plays again
#     # -----------------------------------------------------

#     if len(completed) == 0:

#         if owner == PLAYER:
#             current_turn = BOT
#         else:
#             current_turn = PLAYER

#     else:

#         current_turn = owner

#     # -----------------------------------------------------
#     # Check game over
#     # -----------------------------------------------------

#     total_lines = (
#         (DOTS * (DOTS - 1))
#         +
#         ((DOTS - 1) * DOTS)
#     )

#     used_lines = 0

#     for row_data in horizontal:
#         used_lines += sum(row_data)

#     for row_data in vertical:
#         used_lines += sum(row_data)

#     if used_lines >= total_lines:
#         game_over = True


# # =========================================================
# # START LINE ANIMATION
# # =========================================================

# def start_line_animation(line_type, row, col, owner):

#     global animation

#     animation = {
#         "type": line_type,
#         "r": row,
#         "c": col,
#         "owner": owner,
#         "start": pygame.time.get_ticks()
#     }


# # =========================================================
# # FINISH ANIMATION
# # =========================================================

# def finish_animation():

#     global animation

#     if animation is None:
#         return

#     line_type = animation["type"]
#     row = animation["r"]
#     col = animation["c"]
#     owner = animation["owner"]

#     apply_move(
#         line_type,
#         row,
#         col,
#         owner
#     )

#     animation = None


# # =========================================================
# # DRAW BOXES
# # =========================================================

# def draw_boxes():

#     for r in range(BOXES):

#         for c in range(BOXES):

#             owner = boxes[r][c]

#             if owner is None:
#                 continue

#             x1, y1 = point_position(r, c)
#             x2, y2 = point_position(r + 1, c + 1)

#             color = get_color(owner)

#             surface = pygame.Surface(
#                 (
#                     int(CELL),
#                     int(CELL)
#                 ),
#                 pygame.SRCALPHA
#             )

#             surface.fill(
#                 (
#                     color[0],
#                     color[1],
#                     color[2],
#                     55
#                 )
#             )

#             screen.blit(
#                 surface,
#                 (
#                     x1,
#                     y1
#                 )
#             )


# # =========================================================
# # DRAW STATIC LINES
# # =========================================================

# def draw_static_lines():

#     # Horizontal

#     for r in range(DOTS):

#         for c in range(DOTS - 1):

#             if not horizontal[r][c]:
#                 continue

#             owner = horizontal_owner[r][c]

#             color = get_color(owner)

#             x1, y1 = point_position(r, c)
#             x2, y2 = point_position(r, c + 1)

#             pygame.draw.line(
#                 screen,
#                 color,
#                 (x1, y1),
#                 (x2, y2),
#                 LINE_WIDTH
#             )

#     # Vertical

#     for r in range(DOTS - 1):

#         for c in range(DOTS):

#             if not vertical[r][c]:
#                 continue

#             owner = vertical_owner[r][c]

#             color = get_color(owner)

#             x1, y1 = point_position(r, c)
#             x2, y2 = point_position(r + 1, c)

#             pygame.draw.line(
#                 screen,
#                 color,
#                 (x1, y1),
#                 (x2, y2),
#                 LINE_WIDTH
#             )


# # =========================================================
# # DRAW ANIMATED LINE
# # =========================================================

# def draw_animation():

#     if animation is None:
#         return

#     now = pygame.time.get_ticks()

#     elapsed = now - animation["start"]

#     progress = elapsed / LINE_ANIMATION_TIME

#     progress = max(
#         0,
#         min(1, progress)
#     )

#     line_type = animation["type"]
#     row = animation["r"]
#     col = animation["c"]
#     owner = animation["owner"]

#     color = get_color(owner)

#     if line_type == "H":

#         x1, y1 = point_position(row, col)
#         x2, y2 = point_position(row, col + 1)

#     else:

#         x1, y1 = point_position(row, col)
#         x2, y2 = point_position(row + 1, col)

#     current_x = x1 + (x2 - x1) * progress
#     current_y = y1 + (y2 - y1) * progress

#     pygame.draw.line(
#         screen,
#         color,
#         (x1, y1),
#         (current_x, current_y),
#         LINE_WIDTH
#     )

#     # End glow

#     pygame.draw.circle(
#         screen,
#         color,
#         (
#             int(current_x),
#             int(current_y)
#         ),
#         LINE_WIDTH // 2 + 2
#     )


# # =========================================================
# # DRAW DOTS
# # =========================================================

# def draw_dots():

#     for r in range(DOTS):

#         for c in range(DOTS):

#             x, y = point_position(r, c)

#             pygame.draw.circle(
#                 screen,
#                 DOT_COLOR,
#                 (x, y),
#                 DOT_RADIUS
#             )


# # =========================================================
# # FIND NEAREST LINE
# # =========================================================

# def get_nearest_line(mouse_pos):

#     mx, my = mouse_pos

#     best = None
#     best_distance = 999999

#     # -----------------------------------------------------
#     # Horizontal
#     # -----------------------------------------------------

#     for r in range(DOTS):

#         for c in range(DOTS - 1):

#             if horizontal[r][c]:
#                 continue

#             x1, y1 = point_position(r, c)
#             x2, y2 = point_position(r, c + 1)

#             px = min(max(mx, x1), x2)
#             py = y1

#             distance = math.hypot(
#                 mx - px,
#                 my - py
#             )

#             if distance < best_distance:

#                 best_distance = distance

#                 best = (
#                     "H",
#                     r,
#                     c
#                 )

#     # -----------------------------------------------------
#     # Vertical
#     # -----------------------------------------------------

#     for r in range(DOTS - 1):

#         for c in range(DOTS):

#             if vertical[r][c]:
#                 continue

#             x1, y1 = point_position(r, c)
#             x2 = x1
#             y2 = START_Y + (r + 1) * CELL

#             px = x1
#             py = min(max(my, y1), y2)

#             distance = math.hypot(
#                 mx - px,
#                 my - py
#             )

#             if distance < best_distance:

#                 best_distance = distance

#                 best = (
#                     "V",
#                     r,
#                     c
#                 )

#     # -----------------------------------------------------
#     # Only accept close clicks
#     # -----------------------------------------------------

#     if best_distance <= CELL * 0.30:
#         return best

#     return None


# # =========================================================
# # SIMULATE MOVE
# # =========================================================

# def simulate_move(line_type, row, col):

#     if line_type == "H":
#         horizontal[row][col] = True
#     else:
#         vertical[row][col] = True

#     completed = check_completed_boxes(
#         line_type,
#         row,
#         col
#     )

#     # undo

#     if line_type == "H":
#         horizontal[row][col] = False
#     else:
#         vertical[row][col] = False

#     return len(completed)


# # =========================================================
# # BOT MOVE
# # =========================================================

# def bot_choose_move():

#     available = []

#     # -----------------------------------------------------
#     # Horizontal
#     # -----------------------------------------------------

#     for r in range(DOTS):

#         for c in range(DOTS - 1):

#             if not horizontal[r][c]:

#                 available.append(
#                     ("H", r, c)
#                 )

#     # -----------------------------------------------------
#     # Vertical
#     # -----------------------------------------------------

#     for r in range(DOTS - 1):

#         for c in range(DOTS):

#             if not vertical[r][c]:

#                 available.append(
#                     ("V", r, c)
#                 )

#     if not available:
#         return None

#     # -----------------------------------------------------
#     # First priority:
#     # take a box if possible
#     # -----------------------------------------------------

#     winning_moves = []

#     for move in available:

#         score = simulate_move(*move)

#         if score > 0:
#             winning_moves.append(move)

#     if winning_moves:

#         return random.choice(
#             winning_moves
#         )

#     # -----------------------------------------------------
#     # Second priority:
#     # avoid giving player a box
#     # -----------------------------------------------------

#     safe_moves = []

#     for move in available:

#         score = simulate_move(*move)

#         if score == 0:
#             safe_moves.append(move)

#     if safe_moves:

#         return random.choice(
#             safe_moves
#         )

#     # -----------------------------------------------------
#     # No safe move
#     # -----------------------------------------------------

#     return random.choice(
#         available
#     )


# # =========================================================
# # RESET
# # =========================================================

# def reset_game():

#     global horizontal
#     global vertical
#     global horizontal_owner
#     global vertical_owner
#     global boxes

#     global player_score
#     global bot_score

#     global current_turn
#     global animation
#     global game_over
#     global bot_wait_start

#     horizontal = [
#         [False for _ in range(DOTS - 1)]
#         for _ in range(DOTS)
#     ]

#     vertical = [
#         [False for _ in range(DOTS)]
#         for _ in range(DOTS - 1)
#     ]

#     horizontal_owner = [
#         [None for _ in range(DOTS - 1)]
#         for _ in range(DOTS)
#     ]

#     vertical_owner = [
#         [None for _ in range(DOTS)]
#         for _ in range(DOTS - 1)
#     ]

#     boxes = [
#         [None for _ in range(BOXES)]
#         for _ in range(BOXES)
#     ]

#     player_score = 0
#     bot_score = 0

#     current_turn = PLAYER

#     animation = None
#     game_over = False

#     bot_wait_start = None


# # =========================================================
# # DRAW HEADER
# # =========================================================

# def draw_header():

#     # Player

#     player_text = fonts["heart"].render(
#         f"YOU  {player_score}",
#         True,
#         PLAYER_COLOR
#     )

#     screen.blit(
#         player_text,
#         (60, 40)
#     )

#     # Bot

#     bot_text = fonts["heart"].render(
#         f"BOT  {bot_score}",
#         True,
#         BOT_COLOR
#     )

#     bot_rect = bot_text.get_rect(
#         top=40,
#         right=WIDTH - 60
#     )

#     screen.blit(
#         bot_text,
#         bot_rect
#     )

#     # Turn

#     if not game_over:

#         if current_turn == PLAYER:

#             text = "YOUR TURN"

#             color = PLAYER_COLOR

#         else:

#             text = "BOT TURN"

#             color = BOT_COLOR

#         turn_text = fonts["heart"].render(
#             text,
#             True,
#             color
#         )

#         turn_rect = turn_text.get_rect(
#             center=(WIDTH // 2, 65)
#         )

#         screen.blit(
#             turn_text,
#             turn_rect
#         )


# # =========================================================
# # GAME OVER
# # =========================================================

# def draw_game_over():

#     if not game_over:
#         return

#     overlay = pygame.Surface(
#         (WIDTH, HEIGHT),
#         pygame.SRCALPHA
#     )

#     overlay.fill(
#         (0, 0, 0, 150)
#     )

#     screen.blit(
#         overlay,
#         (0, 0)
#     )

#     if player_score > bot_score:

#         title = "YOU WIN!"

#         color = PLAYER_COLOR

#     elif bot_score > player_score:

#         title = "BOT WINS!"

#         color = BOT_COLOR

#     else:

#         title = "DRAW!"

#         color = (255, 255, 255)

#     title_surface = fonts["heart"].render(
#         title,
#         True,
#         color
#     )

#     title_rect = title_surface.get_rect(
#         center=(WIDTH // 2, HEIGHT // 2 - 50)
#     )

#     screen.blit(
#         title_surface,
#         title_rect
#     )

#     score_text = fonts["heart"].render(
#         f"{player_score}  -  {bot_score}",
#         True,
#         (255, 255, 255)
#     )

#     score_rect = score_text.get_rect(
#         center=(WIDTH // 2, HEIGHT // 2 + 30)
#     )

#     screen.blit(
#         score_text,
#         score_rect
#     )

#     restart_text = fonts["heart"].render(
#         "R  -  RESTART       ESC  -  EXIT",
#         True,
#         (255, 255, 255)
#     )

#     restart_rect = restart_text.get_rect(
#         center=(WIDTH // 2, HEIGHT // 2 + 100)
#     )

#     screen.blit(
#         restart_text,
#         restart_rect
#     )


# # =========================================================
# # MAIN LOOP
# # =========================================================
# def CHECKERS_():
#     now = pygame.time.get_ticks()

#     # =====================================================
#     # FINISH LINE ANIMATION
#     # =====================================================

#     if animation is not None:

#         elapsed = (
#             now -
#             animation["start"]
#         )

#         if elapsed >= LINE_ANIMATION_TIME:

#             finish_animation()

#             # If bot turn started,
#             # start waiting timer

#             if (
#                 current_turn == BOT
#                 and not game_over
#             ):

#                 bot_wait_start = now

#     # =====================================================
#     # BOT
#     # =====================================================

#     if (
#         current_turn == BOT
#         and animation is None
#         and not game_over
#     ):

#         if bot_wait_start is None:

#             bot_wait_start = now

#         elif now - bot_wait_start >= BOT_DELAY:

#             move = bot_choose_move()

#             if move is not None:

#                 line_type, row, col = move

#                 start_line_animation(
#                     line_type,
#                     row,
#                     col,
#                     BOT
#                 )

#             bot_wait_start = None

#     # =====================================================
#     # DRAW
#     # =====================================================

#     screen.fill(BG_COLOR)

#     draw_header()

#     draw_boxes()

#     draw_static_lines()

#     draw_animation()

#     draw_dots()

#     draw_game_over()



import pygame
import random
import math
import time

from modules.font import *


# =========================================================
# SETTINGS
# =========================================================

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

    update_board_size()


# =========================================================
# GAME SETTINGS
# =========================================================

DOTS = 10
BOXES = DOTS - 1

DOT_RADIUS = 7

LINE_WIDTH = 8

LINE_ANIMATION_TIME = 0.18
BOT_DELAY = 0.45


# =========================================================
# PLAYERS
# =========================================================

PLAYER = "PLAYER"
BOT = "BOT"


PLAYER_COLOR = (
    45,
    120,
    255
)

BOT_COLOR = (
    235,
    65,
    65
)

DOT_COLOR = (
    35,
    35,
    35
)

BG_COLOR = (
    245,
    245,
    245
)


# =========================================================
# BOARD
# =========================================================

BOARD_SIZE = 0
START_X = 0
START_Y = 130
CELL = 0


def update_board_size():

    global BOARD_SIZE
    global START_X
    global CELL

    BOARD_SIZE = min(
        WIDTH,
        HEIGHT
    ) - 220

    START_X = (
        WIDTH - BOARD_SIZE
    ) // 2

    CELL = BOARD_SIZE / (DOTS - 1)


# =========================================================
# GAME DATA
# =========================================================

horizontal = []

vertical = []

horizontal_owner = []

vertical_owner = []

boxes = []


player_score = 0
bot_score = 0

current_turn = PLAYER

game_over = False


# =========================================================
# INTERNAL GAME TIMER
# =========================================================

game_previous_time = None


def game_time():

    return time.perf_counter()


def get_game_dt():

    global game_previous_time

    now = game_time()

    if game_previous_time is None:

        game_previous_time = now

        return 0.0

    dt = now - game_previous_time

    game_previous_time = now

    # Prevent huge dt after freeze
    dt = min(
        dt,
        0.05
    )

    return dt


# =========================================================
# ANIMATION DATA
# =========================================================

animation = None

bot_wait_start = None


# =========================================================
# RESET GAME
# =========================================================

def reset_game():

    global horizontal
    global vertical

    global horizontal_owner
    global vertical_owner

    global boxes

    global player_score
    global bot_score

    global current_turn
    global animation
    global game_over

    global bot_wait_start

    global game_previous_time


    # -----------------------------------------------------
    # BOARD
    # -----------------------------------------------------

    horizontal = [
        [False for _ in range(DOTS - 1)]
        for _ in range(DOTS)
    ]

    vertical = [
        [False for _ in range(DOTS)]
        for _ in range(DOTS - 1)
    ]


    # -----------------------------------------------------
    # OWNERS
    # -----------------------------------------------------

    horizontal_owner = [
        [None for _ in range(DOTS - 1)]
        for _ in range(DOTS)
    ]

    vertical_owner = [
        [None for _ in range(DOTS)]
        for _ in range(DOTS - 1)
    ]


    # -----------------------------------------------------
    # BOXES
    # -----------------------------------------------------

    boxes = [
        [None for _ in range(BOXES)]
        for _ in range(BOXES)
    ]


    # -----------------------------------------------------
    # SCORE
    # -----------------------------------------------------

    player_score = 0
    bot_score = 0


    # -----------------------------------------------------
    # TURN
    # -----------------------------------------------------

    current_turn = PLAYER


    # -----------------------------------------------------
    # STATE
    # -----------------------------------------------------

    animation = None

    game_over = False

    bot_wait_start = None


    # -----------------------------------------------------
    # RESET INTERNAL TIMER
    # -----------------------------------------------------

    game_previous_time = time.perf_counter()


# =========================================================
# POINT POSITION
# =========================================================

def point_position(row, col):

    x = START_X + col * CELL
    y = START_Y + row * CELL

    return (
        int(x),
        int(y)
    )


# =========================================================
# COLOR
# =========================================================

def get_color(owner):

    if owner == PLAYER:

        return PLAYER_COLOR

    return BOT_COLOR


# =========================================================
# LINE AVAILABLE
# =========================================================

def line_is_available(
    line_type,
    row,
    col
):

    if line_type == "H":

        return not horizontal[row][col]

    return not vertical[row][col]


# =========================================================
# CHECK COMPLETED BOXES
# =========================================================

def check_completed_boxes(
    line_type,
    row,
    col
):

    completed = []


    # =====================================================
    # HORIZONTAL
    # =====================================================

    if line_type == "H":

        # -------------------------------------------------
        # BOX ABOVE
        # -------------------------------------------------

        if row > 0:

            box_r = row - 1
            box_c = col

            if (
                horizontal[box_r][box_c]
                and horizontal[box_r + 1][box_c]
                and vertical[box_r][box_c]
                and vertical[box_r][box_c + 1]
            ):

                if boxes[box_r][box_c] is None:

                    completed.append(
                        (
                            box_r,
                            box_c
                        )
                    )


        # -------------------------------------------------
        # BOX BELOW
        # -------------------------------------------------

        if row < BOXES:

            box_r = row
            box_c = col

            if (
                horizontal[box_r][box_c]
                and horizontal[box_r + 1][box_c]
                and vertical[box_r][box_c]
                and vertical[box_r][box_c + 1]
            ):

                if boxes[box_r][box_c] is None:

                    completed.append(
                        (
                            box_r,
                            box_c
                        )
                    )


    # =====================================================
    # VERTICAL
    # =====================================================

    else:

        # -------------------------------------------------
        # BOX LEFT
        # -------------------------------------------------

        if col > 0:

            box_r = row
            box_c = col - 1

            if (
                vertical[box_r][box_c]
                and vertical[box_r][box_c + 1]
                and horizontal[box_r][box_c]
                and horizontal[box_r + 1][box_c]
            ):

                if boxes[box_r][box_c] is None:

                    completed.append(
                        (
                            box_r,
                            box_c
                        )
                    )


        # -------------------------------------------------
        # BOX RIGHT
        # -------------------------------------------------

        if col < BOXES:

            box_r = row
            box_c = col

            if (
                vertical[box_r][box_c]
                and vertical[box_r][box_c + 1]
                and horizontal[box_r][box_c]
                and horizontal[box_r + 1][box_c]
            ):

                if boxes[box_r][box_c] is None:

                    completed.append(
                        (
                            box_r,
                            box_c
                        )
                    )


    return completed


# =========================================================
# APPLY MOVE
# =========================================================

def apply_move(
    line_type,
    row,
    col,
    owner
):

    global player_score
    global bot_score

    global current_turn
    global game_over


    # -----------------------------------------------------
    # SAVE LINE
    # -----------------------------------------------------

    if line_type == "H":

        horizontal[row][col] = True

        horizontal_owner[row][col] = owner

    else:

        vertical[row][col] = True

        vertical_owner[row][col] = owner


    # -----------------------------------------------------
    # CHECK BOX
    # -----------------------------------------------------

    completed = check_completed_boxes(
        line_type,
        row,
        col
    )


    # -----------------------------------------------------
    # GIVE BOX
    # -----------------------------------------------------

    for box_r, box_c in completed:

        boxes[box_r][box_c] = owner

        if owner == PLAYER:

            player_score += 1

        else:

            bot_score += 1


    # -----------------------------------------------------
    # TURN
    # -----------------------------------------------------

    if len(completed) == 0:

        if owner == PLAYER:

            current_turn = BOT

        else:

            current_turn = PLAYER

    else:

        # Completed box = play again

        current_turn = owner


    # -----------------------------------------------------
    # GAME OVER
    # -----------------------------------------------------

    total_lines = (
        DOTS * (DOTS - 1)
        +
        (DOTS - 1) * DOTS
    )


    used_lines = 0


    for row_data in horizontal:

        used_lines += sum(row_data)


    for row_data in vertical:

        used_lines += sum(row_data)


    if used_lines >= total_lines:

        game_over = True


# =========================================================
# START LINE ANIMATION
# =========================================================

def start_line_animation(
    line_type,
    row,
    col,
    owner
):

    global animation

    animation = {

        "type": line_type,

        "r": row,

        "c": col,

        "owner": owner,

        # INTERNAL GAME TIME
        "start": time.perf_counter()
    }


# =========================================================
# FINISH ANIMATION
# =========================================================

def finish_animation():

    global animation

    if animation is None:

        return


    line_type = animation["type"]

    row = animation["r"]

    col = animation["c"]

    owner = animation["owner"]


    apply_move(
        line_type,
        row,
        col,
        owner
    )


    animation = None


# =========================================================
# DRAW BOXES
# =========================================================

def draw_boxes():

    for r in range(BOXES):

        for c in range(BOXES):

            owner = boxes[r][c]

            if owner is None:

                continue


            x1, y1 = point_position(
                r,
                c
            )


            surface = pygame.Surface(
                (
                    int(CELL),
                    int(CELL)
                ),
                pygame.SRCALPHA
            )


            color = get_color(owner)


            surface.fill(
                (
                    color[0],
                    color[1],
                    color[2],
                    55
                )
            )


            screen.blit(
                surface,
                (
                    x1,
                    y1
                )
            )


# =========================================================
# DRAW STATIC LINES
# =========================================================

def draw_static_lines():

    # =====================================================
    # HORIZONTAL
    # =====================================================

    for r in range(DOTS):

        for c in range(DOTS - 1):

            if not horizontal[r][c]:

                continue


            owner = horizontal_owner[r][c]

            color = get_color(owner)


            x1, y1 = point_position(
                r,
                c
            )

            x2, y2 = point_position(
                r,
                c + 1
            )


            pygame.draw.line(
                screen,
                color,
                (x1, y1),
                (x2, y2),
                LINE_WIDTH
            )


    # =====================================================
    # VERTICAL
    # =====================================================

    for r in range(DOTS - 1):

        for c in range(DOTS):

            if not vertical[r][c]:

                continue


            owner = vertical_owner[r][c]

            color = get_color(owner)


            x1, y1 = point_position(
                r,
                c
            )

            x2, y2 = point_position(
                r + 1,
                c
            )


            pygame.draw.line(
                screen,
                color,
                (x1, y1),
                (x2, y2),
                LINE_WIDTH
            )


# =========================================================
# DRAW ANIMATION
# =========================================================

def draw_animation():

    if animation is None:

        return


    # -----------------------------------------------------
    # INTERNAL TIMER
    # -----------------------------------------------------

    now = time.perf_counter()


    elapsed = (
        now -
        animation["start"]
    )


    progress = (
        elapsed /
        LINE_ANIMATION_TIME
    )


    progress = max(
        0,
        min(
            1,
            progress
        )
    )


    line_type = animation["type"]

    row = animation["r"]

    col = animation["c"]

    owner = animation["owner"]


    color = get_color(owner)


    # -----------------------------------------------------
    # LINE POSITION
    # -----------------------------------------------------

    if line_type == "H":

        x1, y1 = point_position(
            row,
            col
        )

        x2, y2 = point_position(
            row,
            col + 1
        )

    else:

        x1, y1 = point_position(
            row,
            col
        )

        x2, y2 = point_position(
            row + 1,
            col
        )


    # -----------------------------------------------------
    # CURRENT END
    # -----------------------------------------------------

    current_x = (
        x1
        +
        (x2 - x1) * progress
    )

    current_y = (
        y1
        +
        (y2 - y1) * progress
    )


    # -----------------------------------------------------
    # DRAW
    # -----------------------------------------------------

    pygame.draw.line(
        screen,
        color,
        (x1, y1),
        (
            int(current_x),
            int(current_y)
        ),
        LINE_WIDTH
    )


    # -----------------------------------------------------
    # END GLOW
    # -----------------------------------------------------

    pygame.draw.circle(
        screen,
        color,
        (
            int(current_x),
            int(current_y)
        ),
        LINE_WIDTH // 2 + 2
    )


# =========================================================
# DRAW DOTS
# =========================================================

def draw_dots():

    for r in range(DOTS):

        for c in range(DOTS):

            x, y = point_position(
                r,
                c
            )


            pygame.draw.circle(
                screen,
                DOT_COLOR,
                (
                    x,
                    y
                ),
                DOT_RADIUS
            )


# =========================================================
# FIND NEAREST LINE
# =========================================================

def get_nearest_line(mouse_pos):

    mx, my = mouse_pos

    best = None

    best_distance = 999999


    # =====================================================
    # HORIZONTAL
    # =====================================================

    for r in range(DOTS):

        for c in range(DOTS - 1):

            if horizontal[r][c]:

                continue


            x1, y1 = point_position(
                r,
                c
            )

            x2, y2 = point_position(
                r,
                c + 1
            )


            px = min(
                max(
                    mx,
                    x1
                ),
                x2
            )


            py = y1


            distance = math.hypot(
                mx - px,
                my - py
            )


            if distance < best_distance:

                best_distance = distance

                best = (
                    "H",
                    r,
                    c
                )


    # =====================================================
    # VERTICAL
    # =====================================================

    for r in range(DOTS - 1):

        for c in range(DOTS):

            if vertical[r][c]:

                continue


            x1, y1 = point_position(
                r,
                c
            )

            x2 = x1

            y2 = START_Y + (
                r + 1
            ) * CELL


            px = x1


            py = min(
                max(
                    my,
                    y1
                ),
                y2
            )


            distance = math.hypot(
                mx - px,
                my - py
            )


            if distance < best_distance:

                best_distance = distance

                best = (
                    "V",
                    r,
                    c
                )


    # =====================================================
    # CLICK DISTANCE
    # =====================================================

    if best_distance <= CELL * 0.30:

        return best


    return None


# =========================================================
# SIMULATE MOVE
# =========================================================

def simulate_move(
    line_type,
    row,
    col
):

    if line_type == "H":

        horizontal[row][col] = True

    else:

        vertical[row][col] = True


    completed = check_completed_boxes(
        line_type,
        row,
        col
    )


    # -----------------------------------------------------
    # UNDO
    # -----------------------------------------------------

    if line_type == "H":

        horizontal[row][col] = False

    else:

        vertical[row][col] = False


    return len(completed)


# =========================================================
# BOT CHOOSE MOVE
# =========================================================

def bot_choose_move():

    available = []


    # =====================================================
    # HORIZONTAL
    # =====================================================

    for r in range(DOTS):

        for c in range(DOTS - 1):

            if not horizontal[r][c]:

                available.append(
                    (
                        "H",
                        r,
                        c
                    )
                )


    # =====================================================
    # VERTICAL
    # =====================================================

    for r in range(DOTS - 1):

        for c in range(DOTS):

            if not vertical[r][c]:

                available.append(
                    (
                        "V",
                        r,
                        c
                    )
                )


    if not available:

        return None


    # =====================================================
    # PRIORITY 1
    # TAKE BOX
    # =====================================================

    winning_moves = []


    for move in available:

        score = simulate_move(
            *move
        )


        if score > 0:

            winning_moves.append(
                move
            )


    if winning_moves:

        return random.choice(
            winning_moves
        )


    # =====================================================
    # PRIORITY 2
    # SAFE MOVE
    # =====================================================

    safe_moves = []


    for move in available:

        score = simulate_move(
            *move
        )


        if score == 0:

            safe_moves.append(
                move
            )


    if safe_moves:

        return random.choice(
            safe_moves
        )


    # =====================================================
    # NO SAFE MOVE
    # =====================================================

    return random.choice(
        available
    )


# =========================================================
# DRAW HEADER
# =========================================================

def draw_header():

    # -----------------------------------------------------
    # PLAYER
    # -----------------------------------------------------

    player_text = fonts["heart"].render(
        f"YOU  {player_score}",
        True,
        PLAYER_COLOR
    )


    screen.blit(
        player_text,
        (
            60,
            40
        )
    )


    # -----------------------------------------------------
    # BOT
    # -----------------------------------------------------

    bot_text = fonts["heart"].render(
        f"BOT  {bot_score}",
        True,
        BOT_COLOR
    )


    bot_rect = bot_text.get_rect(
        top=40,
        right=WIDTH - 60
    )


    screen.blit(
        bot_text,
        bot_rect
    )


    # -----------------------------------------------------
    # TURN
    # -----------------------------------------------------

    if not game_over:

        if current_turn == PLAYER:

            text = "YOUR TURN"

            color = PLAYER_COLOR

        else:

            text = "BOT TURN"

            color = BOT_COLOR


        turn_text = fonts["heart"].render(
            text,
            True,
            color
        )


        turn_rect = turn_text.get_rect(
            center=(
                WIDTH // 2,
                65
            )
        )


        screen.blit(
            turn_text,
            turn_rect
        )


# =========================================================
# DRAW GAME OVER
# =========================================================

def draw_game_over():

    if not game_over:

        return


    overlay = pygame.Surface(
        (
            WIDTH,
            HEIGHT
        ),
        pygame.SRCALPHA
    )


    overlay.fill(
        (
            0,
            0,
            0,
            150
        )
    )


    screen.blit(
        overlay,
        (
            0,
            0
        )
    )


    # -----------------------------------------------------
    # WINNER
    # -----------------------------------------------------

    if player_score > bot_score:

        title = "YOU WIN!"

        color = PLAYER_COLOR

    elif bot_score > player_score:

        title = "BOT WINS!"

        color = BOT_COLOR

    else:

        title = "DRAW!"

        color = (
            255,
            255,
            255
        )


    title_surface = fonts["heart"].render(
        title,
        True,
        color
    )


    title_rect = title_surface.get_rect(
        center=(
            WIDTH // 2,
            HEIGHT // 2 - 50
        )
    )


    screen.blit(
        title_surface,
        title_rect
    )


    # -----------------------------------------------------
    # SCORE
    # -----------------------------------------------------

    score_text = fonts["heart"].render(
        f"{player_score}  -  {bot_score}",
        True,
        (
            255,
            255,
            255
        )
    )


    score_rect = score_text.get_rect(
        center=(
            WIDTH // 2,
            HEIGHT // 2 + 30
        )
    )


    screen.blit(
        score_text,
        score_rect
    )


    # -----------------------------------------------------
    # RESTART
    # -----------------------------------------------------

    restart_text = fonts["heart"].render(
        "R  -  RESTART       ESC  -  EXIT",
        True,
        (
            255,
            255,
            255
        )
    )


    restart_rect = restart_text.get_rect(
        center=(
            WIDTH // 2,
            HEIGHT // 2 + 100
        )
    )


    screen.blit(
        restart_text,
        restart_rect
    )


# =========================================================
# GAME UPDATE
# =========================================================

def update_game():

    global bot_wait_start


    # -----------------------------------------------------
    # INTERNAL TIME
    # -----------------------------------------------------

    now = time.perf_counter()


    # =====================================================
    # LINE ANIMATION
    # =====================================================

    if animation is not None:

        elapsed = (
            now -
            animation["start"]
        )


        if elapsed >= LINE_ANIMATION_TIME:

            finish_animation()


            # -------------------------------------------------
            # BOT TURN STARTED
            # -------------------------------------------------

            if (
                current_turn == BOT
                and not game_over
            ):

                bot_wait_start = now


    # =====================================================
    # BOT
    # =====================================================

    if (
        current_turn == BOT
        and animation is None
        and not game_over
    ):

        if bot_wait_start is None:

            bot_wait_start = now


        elif (
            now -
            bot_wait_start
            >= BOT_DELAY
        ):

            move = bot_choose_move()


            if move is not None:

                line_type, row, col = move


                start_line_animation(
                    line_type,
                    row,
                    col,
                    BOT
                )


            bot_wait_start = None


# =========================================================
# DRAW
# =========================================================

def draw_game():

    screen.fill(
        BG_COLOR
    )

    draw_header()

    draw_boxes()

    draw_static_lines()

    draw_animation()

    draw_dots()

    draw_game_over()


# =========================================================
# MAIN GAME FUNCTION
# =========================================================

def DOTS_BOX_():

    # -----------------------------------------------------
    # UPDATE
    # -----------------------------------------------------

    update_game()


    # -----------------------------------------------------
    # DRAW
    # -----------------------------------------------------

    draw_game()


# =========================================================
# EVENT
# =========================================================

def event_DOT_BOX(event):

    global game_over

    # =====================================================
    # KEYBOARD
    # =====================================================

    if event.type == pygame.KEYDOWN:

        # -------------------------------------------------
        # EXIT
        # -------------------------------------------------

        if event.key == pygame.K_ESCAPE:

            return "EXIT"


        # -------------------------------------------------
        # RESTART
        # -------------------------------------------------

        if event.key == pygame.K_r:

            reset_game()

            return None


    # =====================================================
    # PLAYER CLICK
    # =====================================================

    if (
        event.type == pygame.MOUSEBUTTONDOWN
        and event.button == 1
        and current_turn == PLAYER
        and animation is None
        and not game_over
    ):

        move = get_nearest_line(
            event.pos
        )


        if move is not None:

            line_type, row, col = move


            start_line_animation(
                line_type,
                row,
                col,
                PLAYER
            )


    return None


# =========================================================
# INITIAL STATE
# =========================================================

update_board_size()

reset_game()
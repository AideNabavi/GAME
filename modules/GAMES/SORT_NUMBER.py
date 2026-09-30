# import pygame
# import random
# import sys
# from modules.font import *

# # =========================================================
# # SETTINGS
# # =========================================================

# # WIDTH = 1000
# # HEIGHT = 800

# # screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # pygame.display.set_caption("Number Puzzle")

# # clock = pygame.time.Clock()



# # =========================================================
# # COLORS
# # =========================================================

# BACKGROUND = (30, 35, 40)
# BUTTON = (70, 80, 90)
# BUTTON_HOVER = (100, 115, 125)
# WHITE = (245, 245, 245)
# BLACK = (15, 15, 15)
# GREEN = (70, 190, 100)

# # =========================================================
# # GAME STATES
# # =========================================================

# MENU = "MENU"
# GAME = "GAME"
# WIN = "WIN"

# game_state = MENU

# # =========================================================
# # GAME VARIABLES
# # =========================================================

# grid_size = None
# board = []

# empty_index = None

# start_time = 0
# final_time = 0

# moves = 0


# # =========================================================
# # CREATE BOARD
# # =========================================================

# def create_board(size):

#     global board
#     global empty_index
#     global start_time
#     global moves

#     numbers = list(range(1, size * size))

#     # خانه خالی
#     numbers.append(0)

#     board = numbers.copy()

#     # به هم ریختن با حرکات معتبر
#     empty_index = len(board) - 1

#     shuffle_moves = size * size * 30

#     for _ in range(shuffle_moves):

#         possible_moves = get_possible_moves(empty_index, size)

#         if possible_moves:

#             new_index = random.choice(possible_moves)

#             board[empty_index], board[new_index] = \
#                 board[new_index], board[empty_index]

#             empty_index = new_index

#     start_time = pygame.time.get_ticks()

#     moves = 0


# # =========================================================
# # POSSIBLE MOVES
# # =========================================================

# def get_possible_moves(empty_pos, size):

#     row = empty_pos // size
#     col = empty_pos % size

#     moves_list = []

#     # بالا
#     if row > 0:
#         moves_list.append(empty_pos - size)

#     # پایین
#     if row < size - 1:
#         moves_list.append(empty_pos + size)

#     # چپ
#     if col > 0:
#         moves_list.append(empty_pos - 1)

#     # راست
#     if col < size - 1:
#         moves_list.append(empty_pos + 1)

#     return moves_list


# # =========================================================
# # MOVE TILE
# # =========================================================

# def move_tile(index):

#     global empty_index
#     global moves

#     possible_moves = get_possible_moves(empty_index, grid_size)

#     if index in possible_moves:

#         board[empty_index], board[index] = \
#             board[index], board[empty_index]

#         empty_index = index

#         moves += 1


# # =========================================================
# # CHECK WIN
# # =========================================================

# def check_win():

#     correct_board = list(range(1, grid_size * grid_size))
#     correct_board.append(0)

#     return board == correct_board


# # =========================================================
# # DRAW BUTTON
# # =========================================================

# def draw_button(rect, text):

#     mouse_pos = pygame.mouse.get_pos()

#     if rect.collidepoint(mouse_pos):
#         color = BUTTON_HOVER
#     else:
#         color = BUTTON

#     pygame.draw.rect(
#         screen,
#         color,
#         rect,
#         border_radius=15
#     )

#     text_surface = fonts["heart"].render(
#         text,
#         True,
#         WHITE
#     )

#     text_rect = text_surface.get_rect(
#         center=rect.center
#     )

#     screen.blit(text_surface, text_rect)


# # =========================================================
# # MENU
# # =========================================================

# def draw_menu():

#     screen.fill(BACKGROUND)

#     title = fonts["heart"].render(
#         "NUMBER PUZZLE",
#         True,
#         WHITE
#     )

#     title_rect = title.get_rect(
#         center=(WIDTH // 2, 120)
#     )

#     screen.blit(title, title_rect)

#     subtitle = fonts["heart"].render(
#         "Choose puzzle size",
#         True,
#         WHITE
#     )

#     subtitle_rect = subtitle.get_rect(
#         center=(WIDTH // 2, 180)
#     )

#     screen.blit(subtitle, subtitle_rect)

#     button_width = 300
#     button_height = 80

#     x = WIDTH // 2 - button_width // 2

#     button_3 = pygame.Rect(
#         x,
#         250,
#         button_width,
#         button_height
#     )

#     button_5 = pygame.Rect(
#         x,
#         360,
#         button_width,
#         button_height
#     )

#     button_10 = pygame.Rect(
#         x,
#         470,
#         button_width,
#         button_height
#     )

#     draw_button(button_3, "3 x 3")
#     draw_button(button_5, "5 x 5")
#     draw_button(button_10, "10 x 10")

#     return button_3, button_5, button_10


# # =========================================================
# # DRAW GAME
# # =========================================================

# def draw_game():

#     screen.fill(BACKGROUND)

#     # -----------------------------------------------------
#     # TIMER
#     # -----------------------------------------------------

#     elapsed_seconds = (
#         pygame.time.get_ticks() - start_time
#     ) // 1000

#     timer_text = fonts["heart"].render(
#         f"TIME: {elapsed_seconds}",
#         True,
#         WHITE
#     )

#     screen.blit(
#         timer_text,
#         (40, 30)
#     )

#     # -----------------------------------------------------
#     # MOVES
#     # -----------------------------------------------------

#     moves_text = fonts["heart"].render(
#         f"MOVES: {moves}",
#         True,
#         WHITE
#     )

#     moves_rect = moves_text.get_rect(
#         top=30,
#         right=WIDTH - 40
#     )

#     screen.blit(
#         moves_text,
#         moves_rect
#     )

#     # -----------------------------------------------------
#     # GRID
#     # -----------------------------------------------------

#     margin = 40

#     available_width = WIDTH - margin * 2
#     available_height = HEIGHT - 150

#     cell_size = min(
#         available_width // grid_size,
#         available_height // grid_size
#     )

#     grid_width = cell_size * grid_size
#     grid_height = cell_size * grid_size

#     start_x = (WIDTH - grid_width) // 2
#     start_y = 120

#     for index, number in enumerate(board):

#         row = index // grid_size
#         col = index % grid_size

#         x = start_x + col * cell_size
#         y = start_y + row * cell_size

#         rect = pygame.Rect(
#             x + 3,
#             y + 3,
#             cell_size - 6,
#             cell_size - 6
#         )

#         if number == 0:

#             pygame.draw.rect(
#                 screen,
#                 BLACK,
#                 rect,
#                 border_radius=8
#             )

#         else:

#             pygame.draw.rect(
#                 screen,
#                 BUTTON,
#                 rect,
#                 border_radius=8
#             )

#             # برای 10x10 فونت کوچک‌تر
#             if grid_size >= 10:
#                 font = pygame.font.Font(
#                     None,
#                     32
#                 )
#             elif grid_size >= 5:
#                 font = pygame.font.Font(
#                     None,
#                     42
#                 )
#             else:
#                 font = fonts["heart"]

#             text = font.render(
#                 str(number),
#                 True,
#                 WHITE
#             )

#             text_rect = text.get_rect(
#                 center=rect.center
#             )

#             screen.blit(
#                 text,
#                 text_rect
#             )


# # =========================================================
# # DRAW WIN
# # =========================================================

# def draw_win():

#     screen.fill(BACKGROUND)

#     title = fonts["heart"].render(
#         "PUZZLE COMPLETE!",
#         True,
#         GREEN
#     )

#     title_rect = title.get_rect(
#         center=(WIDTH // 2, 220)
#     )

#     screen.blit(title, title_rect)

#     time_text = fonts["heart"].render(
#         f"TIME: {final_time} SECONDS",
#         True,
#         WHITE
#     )

#     time_rect = time_text.get_rect(
#         center=(WIDTH // 2, 320)
#     )

#     screen.blit(time_text, time_rect)

#     moves_text = fonts["heart"].render(
#         f"MOVES: {moves}",
#         True,
#         WHITE
#     )

#     moves_rect = moves_text.get_rect(
#         center=(WIDTH // 2, 380)
#     )

#     screen.blit(moves_text, moves_rect)

#     restart_button = pygame.Rect(
#         WIDTH // 2 - 150,
#         470,
#         300,
#         80
#     )

#     menu_button = pygame.Rect(
#         WIDTH // 2 - 150,
#         570,
#         300,
#         80
#     )

#     draw_button(
#         restart_button,
#         "PLAY AGAIN"
#     )

#     draw_button(
#         menu_button,
#         "MENU"
#     )

#     return restart_button, menu_button


# # =========================================================
# # MAIN LOOP
# # =========================================================

# def SORT_NUMBER_():
#     def event_SORT_NUM(event)
#         # -------------------------------------------------
#         # MENU
#         # -------------------------------------------------

#         if game_state == MENU:

#             if event.type == pygame.MOUSEBUTTONDOWN:

#                 mouse_pos = event.pos

#                 button_width = 300
#                 button_height = 80

#                 x = WIDTH // 2 - button_width // 2

#                 button_3 = pygame.Rect(
#                     x,
#                     250,
#                     button_width,
#                     button_height
#                 )

#                 button_5 = pygame.Rect(
#                     x,
#                     360,
#                     button_width,
#                     button_height
#                 )

#                 button_10 = pygame.Rect(
#                     x,
#                     470,
#                     button_width,
#                     button_height
#                 )

#                 if button_3.collidepoint(mouse_pos):

#                     grid_size = 3

#                     create_board(grid_size)

#                     game_state = GAME

#                 elif button_5.collidepoint(mouse_pos):

#                     grid_size = 5

#                     create_board(grid_size)

#                     game_state = GAME

#                 elif button_10.collidepoint(mouse_pos):

#                     grid_size = 10

#                     create_board(grid_size)

#                     game_state = GAME

#         # -------------------------------------------------
#         # GAME
#         # -------------------------------------------------

#         elif game_state == GAME:

#             if event.type == pygame.MOUSEBUTTONDOWN:

#                 mouse_x, mouse_y = event.pos

#                 margin = 40

#                 available_width = WIDTH - margin * 2
#                 available_height = HEIGHT - 150

#                 cell_size = min(
#                     available_width // grid_size,
#                     available_height // grid_size
#                 )

#                 grid_width = cell_size * grid_size

#                 start_x = (
#                     WIDTH - grid_width
#                 ) // 2

#                 start_y = 120

#                 if (
#                     mouse_x >= start_x
#                     and mouse_x < start_x + grid_width
#                     and mouse_y >= start_y
#                     and mouse_y < start_y + grid_width
#                 ):

#                     col = (
#                         mouse_x - start_x
#                     ) // cell_size

#                     row = (
#                         mouse_y - start_y
#                     ) // cell_size

#                     index = (
#                         row * grid_size
#                         + col
#                     )

#                     move_tile(index)

#                     if check_win():

#                         final_time = (
#                             pygame.time.get_ticks()
#                             - start_time
#                         ) // 1000

#                         game_state = WIN

#             # خروج با ESC
#             if event.type == pygame.KEYDOWN:

#                 if event.key == pygame.K_ESCAPE:

#                     game_state = MENU

#         # -------------------------------------------------
#         # WIN
#         # -------------------------------------------------

#         elif game_state == WIN:

#             if event.type == pygame.MOUSEBUTTONDOWN:

#                 mouse_pos = event.pos

#                 restart_button = pygame.Rect(
#                     WIDTH // 2 - 150,
#                     470,
#                     300,
#                     80
#                 )

#                 menu_button = pygame.Rect(
#                     WIDTH // 2 - 150,
#                     570,
#                     300,
#                     80
#                 )

#                 if restart_button.collidepoint(
#                     mouse_pos
#                 ):

#                     create_board(grid_size)

#                     game_state = GAME

#                 elif menu_button.collidepoint(
#                     mouse_pos
#                 ):

#                     game_state = MENU

#     # =====================================================
#     # DRAW
#     # =====================================================

#     if game_state == MENU:

#         draw_menu()

#     elif game_state == GAME:

#         draw_game()

#     elif game_state == WIN:

#         draw_win()











import pygame
import random

from modules.font import *


# =========================================================
# GAME STATES
# =========================================================

MENU = "MENU"
GAME = "GAME"
WIN = "WIN"


# =========================================================
# GLOBALS
# =========================================================

def WIDTH_HEIGHT_gettter(screen_,WIDTH_,HEIGHT_):
    global WIDTH
    global screen
    global HEIGHT
    WIDTH = WIDTH_
    HEIGHT = HEIGHT_
    screen = screen_

WIDTH = None
HEIGHT = None
screen = None

game_state = MENU

grid_size = None
board = []
empty_index = None

start_time = 0
final_time = 0
moves = 0


# =========================================================
# INITIALIZE
# =========================================================

def WIDTH_HEIGHT_gettter(screen_, WIDTH_, HEIGHT_):

    global screen
    global WIDTH
    global HEIGHT

    screen = screen_
    WIDTH = WIDTH_
    HEIGHT = HEIGHT_


# =========================================================
# RESET
# =========================================================

def reset_sort_number():

    global game_state
    global grid_size
    global board
    global empty_index
    global start_time
    global final_time
    global moves

    game_state = MENU

    grid_size = None
    board = []
    empty_index = None

    start_time = 0
    final_time = 0
    moves = 0


# =========================================================
# CREATE BOARD
# =========================================================

def create_board(size):

    global board
    global empty_index
    global start_time
    global moves

    numbers = list(range(1, size * size))

    # Empty tile
    numbers.append(0)

    board = numbers.copy()

    # Start with empty tile at the end
    empty_index = len(board) - 1

    # Shuffle using valid moves
    shuffle_moves = size * size * 30

    for _ in range(shuffle_moves):

        possible_moves = get_possible_moves(
            empty_index,
            size
        )

        if possible_moves:

            new_index = random.choice(
                possible_moves
            )

            board[empty_index], board[new_index] = (
                board[new_index],
                board[empty_index]
            )

            empty_index = new_index

    start_time = pygame.time.get_ticks()

    moves = 0


# =========================================================
# POSSIBLE MOVES
# =========================================================

def get_possible_moves(empty_pos, size):

    row = empty_pos // size
    col = empty_pos % size

    moves_list = []

    # Up
    if row > 0:
        moves_list.append(
            empty_pos - size
        )

    # Down
    if row < size - 1:
        moves_list.append(
            empty_pos + size
        )

    # Left
    if col > 0:
        moves_list.append(
            empty_pos - 1
        )

    # Right
    if col < size - 1:
        moves_list.append(
            empty_pos + 1
        )

    return moves_list


# =========================================================
# MOVE TILE
# =========================================================

def move_tile(index):

    global empty_index
    global moves

    if grid_size is None:
        return

    possible_moves = get_possible_moves(
        empty_index,
        grid_size
    )

    if index in possible_moves:

        board[empty_index], board[index] = (
            board[index],
            board[empty_index]
        )

        empty_index = index

        moves += 1


# =========================================================
# CHECK WIN
# =========================================================

def check_win():

    if grid_size is None:
        return False

    correct_board = list(
        range(
            1,
            grid_size * grid_size
        )
    )

    correct_board.append(0)

    return board == correct_board


# =========================================================
# DRAW BUTTON
# =========================================================

def draw_button(rect, text):

    mouse_pos = pygame.mouse.get_pos()

    if rect.collidepoint(mouse_pos):
        color = (100, 115, 125)
    else:
        color = (70, 80, 90)

    pygame.draw.rect(
        screen,
        color,
        rect,
        border_radius=15
    )

    text_surface = fonts["heart"].render(
        text,
        True,
        (245, 245, 245)
    )

    text_rect = text_surface.get_rect(
        center=rect.center
    )

    screen.blit(
        text_surface,
        text_rect
    )


# =========================================================
# MENU
# =========================================================

def draw_menu():

    # screen.fill(
    #     (30, 35, 40)
    # )

    title = fonts["heart"].render(
        "NUMBER PUZZLE",
        True,
        (245, 245, 245)
    )

    title_rect = title.get_rect(
        center=(
            WIDTH // 2,
            120
        )
    )

    screen.blit(
        title,
        title_rect
    )

    subtitle = fonts["heart"].render(
        "Choose puzzle size",
        True,
        (245, 245, 245)
    )

    subtitle_rect = subtitle.get_rect(
        center=(
            WIDTH // 2,
            180
        )
    )

    screen.blit(
        subtitle,
        subtitle_rect
    )

    button_width = 300
    button_height = 80

    x = (
        WIDTH // 2
        - button_width // 2
    )

    button_3 = pygame.Rect(
        x,
        250,
        button_width,
        button_height
    )

    button_5 = pygame.Rect(
        x,
        360,
        button_width,
        button_height
    )

    button_10 = pygame.Rect(
        x,
        470,
        button_width,
        button_height
    )

    draw_button(
        button_3,
        "3 x 3"
    )

    draw_button(
        button_5,
        "5 x 5"
    )

    draw_button(
        button_10,
        "10 x 10"
    )


# =========================================================
# DRAW GAME
# =========================================================

def draw_game():

    screen.fill(
        (30, 35, 40)
    )

    # -----------------------------------------------------
    # TIMER
    # -----------------------------------------------------

    elapsed_seconds = (
        pygame.time.get_ticks()
        - start_time
    ) // 1000

    timer_text = fonts["heart"].render(
        f"TIME: {elapsed_seconds}",
        True,
        (245, 245, 245)
    )

    screen.blit(
        timer_text,
        (40, 30)
    )

    # -----------------------------------------------------
    # MOVES
    # -----------------------------------------------------

    moves_text = fonts["heart"].render(
        f"MOVES: {moves}",
        True,
        (245, 245, 245)
    )

    moves_rect = moves_text.get_rect(
        top=30,
        right=WIDTH - 40
    )

    screen.blit(
        moves_text,
        moves_rect
    )

    # -----------------------------------------------------
    # GRID
    # -----------------------------------------------------

    margin = 40

    available_width = WIDTH - margin * 2
    available_height = HEIGHT - 150

    cell_size = min(
        available_width // grid_size,
        available_height // grid_size
    )

    grid_width = (
        cell_size * grid_size
    )

    grid_height = (
        cell_size * grid_size
    )

    start_x = (
        WIDTH - grid_width
    ) // 2

    start_y = 120

    for index, number in enumerate(board):

        row = index // grid_size
        col = index % grid_size

        x = start_x + col * cell_size
        y = start_y + row * cell_size

        rect = pygame.Rect(
            x + 3,
            y + 3,
            cell_size - 6,
            cell_size - 6
        )

        # Empty tile
        if number == 0:

            pygame.draw.rect(
                screen,
                (15, 15, 15),
                rect,
                border_radius=8
            )

        else:

            pygame.draw.rect(
                screen,
                (70, 80, 90),
                rect,
                border_radius=8
            )

            # Font size
            if grid_size >= 10:

                font = pygame.font.Font(
                    None,
                    32
                )

            elif grid_size >= 5:

                font = pygame.font.Font(
                    None,
                    42
                )

            else:

                font = fonts["heart"]

            text = font.render(
                str(number),
                True,
                (245, 245, 245)
            )

            text_rect = text.get_rect(
                center=rect.center
            )

            screen.blit(
                text,
                text_rect
            )


# =========================================================
# DRAW WIN
# =========================================================

def draw_win():

    screen.fill(
        (30, 35, 40)
    )

    title = fonts["heart"].render(
        "PUZZLE COMPLETE!",
        True,
        (70, 190, 100)
    )

    title_rect = title.get_rect(
        center=(
            WIDTH // 2,
            220
        )
    )

    screen.blit(
        title,
        title_rect
    )

    time_text = fonts["heart"].render(
        f"TIME: {final_time} SECONDS",
        True,
        (245, 245, 245)
    )

    time_rect = time_text.get_rect(
        center=(
            WIDTH // 2,
            320
        )
    )

    screen.blit(
        time_text,
        time_rect
    )

    moves_text = fonts["heart"].render(
        f"MOVES: {moves}",
        True,
        (245, 245, 245)
    )

    moves_rect = moves_text.get_rect(
        center=(
            WIDTH // 2,
            380
        )
    )

    screen.blit(
        moves_text,
        moves_rect
    )

    # -----------------------------------------------------
    # PLAY AGAIN
    # -----------------------------------------------------

    restart_button = pygame.Rect(
        WIDTH // 2 - 150,
        470,
        300,
        80
    )

    # -----------------------------------------------------
    # MENU
    # -----------------------------------------------------

    menu_button = pygame.Rect(
        WIDTH // 2 - 150,
        570,
        300,
        80
    )

    draw_button(
        restart_button,
        "PLAY AGAIN"
    )

    draw_button(
        menu_button,
        "MENU"
    )


# =========================================================
# EVENT HANDLER
# =========================================================

def event_SORT_NUM(event):

    global game_state
    global grid_size
    global final_time

    # =====================================================
    # MENU
    # =====================================================

    if game_state == MENU:

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos = event.pos

            button_width = 300
            button_height = 80

            x = (
                WIDTH // 2
                - button_width // 2
            )

            button_3 = pygame.Rect(
                x,
                250,
                button_width,
                button_height
            )

            button_5 = pygame.Rect(
                x,
                360,
                button_width,
                button_height
            )

            button_10 = pygame.Rect(
                x,
                470,
                button_width,
                button_height
            )

            # 3 x 3
            if button_3.collidepoint(mouse_pos):

                grid_size = 3

                create_board(
                    grid_size
                )

                game_state = GAME

                return

            # 5 x 5
            elif button_5.collidepoint(mouse_pos):

                grid_size = 5

                create_board(
                    grid_size
                )

                game_state = GAME

                return

            # 10 x 10
            elif button_10.collidepoint(mouse_pos):

                grid_size = 10

                create_board(
                    grid_size
                )

                game_state = GAME

                return

    # =====================================================
    # GAME
    # =====================================================

    elif game_state == GAME:

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_x, mouse_y = event.pos

            margin = 40

            available_width = (
                WIDTH - margin * 2
            )

            available_height = (
                HEIGHT - 150
            )

            cell_size = min(
                available_width // grid_size,
                available_height // grid_size
            )

            grid_width = (
                cell_size * grid_size
            )

            start_x = (
                WIDTH - grid_width
            ) // 2

            start_y = 120

            # Click inside board
            if (
                start_x <= mouse_x
                < start_x + grid_width
                and
                start_y <= mouse_y
                < start_y + grid_width
            ):

                col = (
                    mouse_x - start_x
                ) // cell_size

                row = (
                    mouse_y - start_y
                ) // cell_size

                index = (
                    row * grid_size
                    + col
                )

                move_tile(index)

                if check_win():

                    final_time = (
                        pygame.time.get_ticks()
                        - start_time
                    ) // 1000

                    game_state = WIN

                    return

        # ESC -> MENU
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:

                game_state = MENU

                return

    # =====================================================
    # WIN
    # =====================================================

    elif game_state == WIN:

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos = event.pos

            restart_button = pygame.Rect(
                WIDTH // 2 - 150,
                470,
                300,
                80
            )

            menu_button = pygame.Rect(
                WIDTH // 2 - 150,
                570,
                300,
                80
            )

            # ---------------------------------------------
            # PLAY AGAIN
            # ---------------------------------------------

            if restart_button.collidepoint(
                mouse_pos
            ):

                create_board(
                    grid_size
                )

                game_state = GAME

                return

            # ---------------------------------------------
            # MENU
            # ---------------------------------------------

            elif menu_button.collidepoint(
                mouse_pos
            ):

                game_state = MENU

                return

    # =====================================================
    # ESC
    # =====================================================

    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_ESCAPE:

            reset_sort_number()


# =========================================================
# MAIN DRAW FUNCTION
# =========================================================

def SORT_NUMBER_():

    if game_state == MENU:

        draw_menu()

    elif game_state == GAME:

        draw_game()

    elif game_state == WIN:

        draw_win()
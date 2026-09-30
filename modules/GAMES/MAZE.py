

import pygame
import random

from modules.font import *





from modules import XP


# =========================================================
# SETTINGS
# =========================================================

HEIGHT = None
WIDTH = None
screen = None
added_xp = True

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

BG = (25, 45, 30)

WALL = (255, 165, 0)
PATH = (205, 185, 140)

PLAYER = (50, 180, 80)
FINISH = (190, 60, 60)

WHITE = (255, 255, 255)


# =========================================================
# LEVELS
# =========================================================

levels = {
    "EASY": 11,
    "MEDIUM": 51,
    "HARD": 81
}


# =========================================================
# GAME STATES
# =========================================================

LEVEL_SELECT = "LEVEL_SELECT"
PLAYING = "PLAYING"
WIN = "WIN"


game_state = LEVEL_SELECT


# =========================================================
# GAME DATA
# =========================================================

maze = []

player = [1, 1]

finish = [0, 0]

selected_level = None
selected_size = None

start_time = 0
final_time = 0









#------------------------------------ این برای بازی ست 

from modules import menu_window
    

    
# =========================================================
# BUTTON
# =========================================================

def button(text, rect):

    color = (100, 130, 80)

    if rect.collidepoint(
        pygame.mouse.get_pos()
    ):
        color = (130, 160, 100)

    # pygame.draw.rect(
    #     screen,
    #     color,
    #     rect,
    #     border_radius=12
    # )

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
# LEVEL BUTTONS
# =========================================================

def get_level_buttons():

    easy = pygame.Rect(
        WIDTH // 2 - 150,
        HEIGHT // 2  - 100,
        300,
        70
    )

    medium = pygame.Rect(
        WIDTH // 2 - 150,
        HEIGHT // 2 ,
        300,
        70
    )

    hard = pygame.Rect(
        WIDTH // 2 - 150,
        HEIGHT // 2 + 100,
        300,
        70
    )

    return easy, medium, hard


# =========================================================
# CREATE MAZE
# =========================================================

def create_maze(size):

    maze_ = [
        [1] * size
        for _ in range(size)
    ]

    def carve(r, c):

        maze_[r][c] = 0

        directions = [
            (-2, 0),
            (2, 0),
            (0, -2),
            (0, 2)
        ]

        random.shuffle(directions)

        for dr, dc in directions:

            nr = r + dr
            nc = c + dc

            if (
                1 <= nr < size - 1
                and
                1 <= nc < size - 1
                and
                maze_[nr][nc] == 1
            ):

                maze_[
                    r + dr // 2
                ][
                    c + dc // 2
                ] = 0

                carve(nr, nc)

    carve(1, 1)

    for _ in range(size * 2):

        r = random.randrange(1, size - 1)
        c = random.randrange(1, size - 1)

        if maze_[r][c] == 1:

            neighbours = 0

            for dr, dc in [
                (-1, 0),
                (1, 0),
                (0, -1),
                (0, 1)
            ]:

                nr = r + dr
                nc = c + dc

                if maze_[nr][nc] == 0:
                    neighbours += 1

            if neighbours >= 2:
                maze_[r][c] = 0

    return maze_


# =========================================================
# COUNT AVAILABLE PATHS
# =========================================================

def count_paths(r, c):

    count = 0

    for dr, dc in [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]:

        nr = r + dr
        nc = c + dc

        if (
            0 <= nr < len(maze)
            and
            0 <= nc < len(maze)
            and
            maze[nr][nc] == 0
        ):

            count += 1

    return count


# =========================================================
# MOVE UNTIL WALL / TURN
# =========================================================

def move_until_stop(dr, dc):

    global game_state
    global final_time

    if game_state != PLAYING:
        return

    while True:

        r, c = player

        nr = r + dr
        nc = c + dc

        # =================================================
        # WALL
        # =================================================

        if (
            nr < 0
            or nr >= len(maze)
            or nc < 0
            or nc >= len(maze)
            or maze[nr][nc] == 1
        ):

            break

        # =================================================
        # MOVE
        # =================================================

        player[0] = nr
        player[1] = nc

        # =================================================
        # FINISH
        # =================================================

        if player == finish:

            final_time = (
                pygame.time.get_ticks()
                - start_time
            ) // 1000

            game_state = WIN
            break

        # =================================================
        # TURN / INTERSECTION
        # =================================================

        if count_paths(
            nr,
            nc
        ) > 2:

            break


# =========================================================
# START GAME
# =========================================================

def start_game(size):

    global maze
    global player
    global finish
    global selected_size
    global start_time
    global final_time
    global game_state
    global added_xp

    selected_size = size
    added_xp = False
    maze = create_maze(size)

    player = [1, 1]

    finish = [
        size - 2,
        size - 2
    ]

    # =====================================================
    # MAKE FINISH OPEN
    # =====================================================

    maze[
        finish[0]
    ][
        finish[1]
    ] = 0

    maze[
        finish[0]
    ][
        finish[1] - 1
    ] = 0

    maze[
        finish[0] - 1
    ][
        finish[1]
    ] = 0

    # =====================================================
    # TIMER
    # =====================================================

    start_time = pygame.time.get_ticks()

    final_time = 0

    game_state = PLAYING


# =========================================================
# RESET GAME
# =========================================================

def reset_maze():

    global maze
    global player
    global finish
    global selected_level
    global selected_size
    global start_time
    global final_time
    global game_state

    maze = []

    player = [1, 1]

    finish = [0, 0]

    selected_level = None
    selected_size = None

    start_time = 0
    final_time = 0

    # برگشت کامل به انتخاب Level
    game_state = LEVEL_SELECT


# =========================================================
# RESTART SAME LEVEL
# =========================================================

def restart_maze():

    if selected_size is None:
        return

    start_game(
        selected_size
    )


# =========================================================
# GET CURRENT TIME
# =========================================================

def get_game_time():

    if game_state == WIN:

        return final_time

    if game_state != PLAYING:

        return 0

    return (
        pygame.time.get_ticks()
        - start_time
    ) // 1000


# =========================================================
# DRAW TIMER
# =========================================================

def draw_timer():

    seconds = get_game_time()

    timer = fonts["heart"].render(
        f"Time: {seconds}",
        True,
        WHITE
    )

    screen.blit(
        timer,
        (20, 20)
    )


# =========================================================
# DRAW LEVEL SELECT
# =========================================================

def draw_level_select():

    # screen.fill(BG)

    title = fonts["quastion"].render(
        "MAZE",
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

    easy, medium, hard = (
        get_level_buttons()
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
# DRAW GAME
# =========================================================
# =====================================================
# MAZE IMAGES
# =====================================================

WALL_IMAGE = pygame.image.load(
    "asset/image/GAME/MAZE/wall.png"
).convert_alpha()

# FLOOR_IMAGE = pygame.image.load(
#     "asset/image/GAME/MAZE/floor.png"
# ).convert_alpha()

PLAYER_IMAGE = pygame.image.load(
    "asset/image/GAME/MAZE/player.png"
).convert_alpha()

FINISH_IMAGE = pygame.image.load(
    "asset/image/GAME/MAZE/finish.png"
).convert_alpha()


# =====================================================
# IMAGE CACHE
# =====================================================

wall_cache = {}
floor_cache = {}
player_cache = {}
finish_cache = {}


def draw_game():

    global added_xp

    size = len(maze)

    # =====================================================
    # TIMER
    # =====================================================

    draw_timer()

    # =====================================================
    # CELL SIZE
    # =====================================================

    cell = min(
        1300 // size,
        1300 // size
    )

    board_w = size * cell
    board_h = size * cell

    start_x = (
        WIDTH - board_w
    ) // 2

    start_y = 0

    # =====================================================
    # DRAW MAZE
    # =====================================================

    for r in range(size):

        for c in range(size):

            x = start_x + c * cell
            y = start_y + r * cell

            # =================================================
            # WALL
            # =================================================

            if maze[r][c] == 1:

                if cell not in wall_cache:

                    wall_cache[cell] = pygame.transform.smoothscale(
                        WALL_IMAGE,
                        (cell, cell)
                    )

                screen.blit(
                    wall_cache[cell],
                    (x, y)
                )

            # =================================================
            # FLOOR
            # =================================================

            # else:

            #     if cell not in floor_cache:

            #         floor_cache[cell] = pygame.transform.smoothscale(
            #             FLOOR_IMAGE,
            #             (cell, cell)
            #         )

            #     screen.blit(
            #         floor_cache[cell],
            #         (x, y)
            #     )

    # =====================================================
    # FINISH
    # =====================================================

    fr, fc = finish

    finish_rect = pygame.Rect(
        start_x + fc * cell,
        start_y + fr * cell,
        cell,
        cell
    )

    if cell not in finish_cache:

        finish_cache[cell] = pygame.transform.smoothscale(
            FINISH_IMAGE,
            (cell, cell)
        )

    screen.blit(
        finish_cache[cell],
        finish_rect
    )

    # =====================================================
    # PLAYER
    # =====================================================

    pr, pc = player

    player_rect = pygame.Rect(
        start_x + pc * cell,
        start_y + pr * cell,
        cell,
        cell
    )

    if cell not in player_cache:

        player_cache[cell] = pygame.transform.smoothscale(
            PLAYER_IMAGE,
            (cell, cell)
        )

    screen.blit(
        player_cache[cell],
        player_rect
    )

    # =====================================================
    # WIN
    # =====================================================

    if game_state == WIN:

        text = fonts["heart"].render(
            f"YOU WIN!  {final_time}s",
            True,
            WHITE
        )

        screen.blit(
            text,
            text.get_rect(
                center=(
                    WIDTH // 2,
                    35
                )
            )
        )

        if not added_xp:

            XP.X_P(
                2,
                "add"
            )

            added_xp = True

        menu_window.SHOW_XP(
            screen,
            2,
            HEIGHT,
            WIDTH
        )
        



# =========================================================
# EVENT HANDLER
# =========================================================

def event_MAZE(event):

    global selected_level
    global selected_size
    global game_state

    # =====================================================
    # LEVEL SELECT
    # =====================================================

    if game_state == LEVEL_SELECT:

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:

                reset_maze()

                return

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                easy, medium, hard = (
                    get_level_buttons()
                )

                # =========================================
                # EASY
                # =========================================

                if easy.collidepoint(
                    event.pos
                ):

                    selected_level = "EASY"

                    start_game(
                        levels["EASY"]
                    )

                    return

                # =========================================
                # MEDIUM
                # =========================================

                if medium.collidepoint(
                    event.pos
                ):

                    selected_level = "MEDIUM"

                    start_game(
                        levels["MEDIUM"]
                    )

                    return

                # =========================================
                # HARD
                # =========================================

                if hard.collidepoint(
                    event.pos
                ):

                    selected_level = "HARD"

                    start_game(
                        levels["HARD"]
                    )

                    return

    # =====================================================
    # PLAYING
    # =====================================================

    elif game_state == PLAYING:

        if event.type == pygame.KEYDOWN:

            # =============================================
            # BACK
            # =============================================

            if event.key == pygame.K_ESCAPE:

                reset_maze()

                return

            # =============================================
            # RESTART
            # =============================================

            if event.key == pygame.K_r:

                restart_maze()

                return

            # =============================================
            # UP
            # =============================================

            if event.key in (
                pygame.K_UP,
                pygame.K_w
            ):

                move_until_stop(
                    -1,
                    0
                )

                return

            # =============================================
            # DOWN
            # =============================================

            if event.key in (
                pygame.K_DOWN,
                pygame.K_s
            ):

                move_until_stop(
                    1,
                    0
                )

                return

            # =============================================
            # LEFT
            # =============================================

            if event.key in (
                pygame.K_LEFT,
                pygame.K_a
            ):

                move_until_stop(
                    0,
                    -1
                )

                return

            # =============================================
            # RIGHT
            # =============================================

            if event.key in (
                pygame.K_RIGHT,
                pygame.K_d
            ):

                move_until_stop(
                    0,
                    1
                )

                return

    # =====================================================
    # WIN
    # =====================================================

    elif game_state == WIN:

        if event.type == pygame.KEYDOWN:

            # =============================================
            # RESTART SAME LEVEL
            # =============================================

            if event.key == pygame.K_r:

                restart_maze()

                return

            # =============================================
            # BACK TO LEVEL SELECT
            # =============================================

            if event.key == pygame.K_ESCAPE:

                reset_maze()

                return


# =========================================================
# MAIN DRAW FUNCTION
# =========================================================

def MAZE_():

    if game_state == LEVEL_SELECT:

        draw_level_select()

    elif (
        game_state == PLAYING
        or
        game_state == WIN
    ):

        draw_game()


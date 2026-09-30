import pygame
import random
import time

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
# SUDOKU BOARD
# =========================================================

BOARD_SIZE = 1300

BOARD_X = 0
BOARD_Y = 0


# =========================================================
# 9 SEPARATE 3x3 BOXES
# =========================================================
#
# BOARD.png همچنان یک عکس کامل است.
#
# این مختصات فقط برای:
#   - GRID
#   - NUMBERS
#   - SELECTED CELL
#   - CLICK
#
# استفاده می‌شوند.
#
# هر باکس شامل 3x3 سلول است.
# =========================================================


BOX_SIZES = [
    360, 360, 360,
    360, 360, 360,
    360, 360, 360
]


BOX_POSITIONS = [

    # ROW 1
    ( 470, 110),
    (845, 110),
    (1220, 110),

    # ROW 2
    (465, 475),
    (835, 475),
    (1207, 475),

    # ROW 3
    (465, 857),
    (835, 857),
    (1207, 857)

]


# =========================================================
# COLORS
# =========================================================

BACKGROUND = (255, 255, 255)

WHITE = (245, 245, 245)
BLACK = (30, 30, 30)

BUTTON = (55, 65, 75)
BUTTON_HOVER = (75, 90, 105)

LINE_COLOR = (35, 35, 35)

SELECT_COLOR = (210, 225, 245)

FIXED_COLOR = (30, 30, 30)
PLAYER_COLOR = (45, 105, 190)

GREEN = (70, 190, 100)


# =========================================================
# BOARD IMAGE
# =========================================================

board_image = pygame.image.load(
    "asset/image/GAME/SUDOKU/BOARD.png"
).convert_alpha()

board_image = pygame.transform.scale(
    board_image,
    (
        BOARD_SIZE,
        BOARD_SIZE
    )
)


# =========================================================
# DIFFICULTY
# =========================================================

DIFFICULTIES = {

    "EASY": 35,

    "MEDIUM": 48,

    "HARD": 58

}


# =========================================================
# GAME STATE
# =========================================================

game_state = "LEVEL_SELECT"

difficulty = None

solution = None
board = None

selected_cell = None

message = ""


# =========================================================
# TIMER
# =========================================================

game_start_time = None
final_time = 0


# =========================================================
# GET BOX RECT
# =========================================================

def get_box_rect(box_index):

    x, y = BOX_POSITIONS[box_index]

    size = BOX_SIZES[box_index]

    return pygame.Rect(
        x,
        y,
        size,
        size
    )


# =========================================================
# GET CELL RECT
# =========================================================

def get_cell_rect(row, col):

    # -----------------------------------------------------
    # مشخص کردن شماره باکس
    # -----------------------------------------------------

    box_row = row // 3
    box_col = col // 3

    box_index = (
        box_row * 3
        +
        box_col
    )

    # -----------------------------------------------------
    # موقعیت باکس
    # -----------------------------------------------------

    box_x, box_y = BOX_POSITIONS[
        box_index
    ]

    box_size = BOX_SIZES[
        box_index
    ]

    # -----------------------------------------------------
    # اندازه سلول
    # -----------------------------------------------------

    cell_size = box_size // 3

    # -----------------------------------------------------
    # موقعیت سلول داخل باکس
    # -----------------------------------------------------

    local_row = row % 3
    local_col = col % 3

    x = (
        box_x
        +
        local_col * cell_size
    )

    y = (
        box_y
        +
        local_row * cell_size
    )

    return pygame.Rect(
        x,
        y,
        cell_size,
        cell_size
    )


# =========================================================
# GET BOARD CELL RECT
# =========================================================

def get_screen_cell_rect(row, col):

    rect = get_cell_rect(
        row,
        col
    )

    return pygame.Rect(
        BOARD_X + rect.x,
        BOARD_Y + rect.y,
        rect.width,
        rect.height
    )


# =========================================================
# RESET
# =========================================================

def reset_sudoku():

    global game_state
    global difficulty
    global solution
    global board
    global selected_cell
    global message
    global game_start_time
    global final_time

    game_state = "LEVEL_SELECT"

    difficulty = None

    solution = None
    board = None

    selected_cell = None

    message = ""

    game_start_time = None

    final_time = 0


# =========================================================
# SUDOKU VALIDATION
# =========================================================

def is_valid(board, row, col, num):

    # -----------------------------------------------------
    # ROW
    # -----------------------------------------------------

    for c in range(9):

        if board[row][c] == num:

            return False

    # -----------------------------------------------------
    # COLUMN
    # -----------------------------------------------------

    for r in range(9):

        if board[r][col] == num:

            return False

    # -----------------------------------------------------
    # 3x3 BOX
    # -----------------------------------------------------

    box_row = (
        row // 3
    ) * 3

    box_col = (
        col // 3
    ) * 3

    for r in range(
        box_row,
        box_row + 3
    ):

        for c in range(
            box_col,
            box_col + 3
        ):

            if board[r][c] == num:

                return False

    return True


# =========================================================
# SOLVE BOARD
# =========================================================

def solve_board(board):

    for row in range(9):

        for col in range(9):

            if board[row][col] == 0:

                numbers = list(
                    range(1, 10)
                )

                random.shuffle(
                    numbers
                )

                for num in numbers:

                    if is_valid(
                        board,
                        row,
                        col,
                        num
                    ):

                        board[row][col] = num

                        if solve_board(board):

                            return True

                        board[row][col] = 0

                return False

    return True


# =========================================================
# GENERATE SOLUTION
# =========================================================

def generate_solution():

    board = [

        [0 for _ in range(9)]

        for _ in range(9)

    ]

    solve_board(board)

    return board


# =========================================================
# CREATE PUZZLE
# =========================================================

def create_puzzle(
    solution,
    difficulty
):

    puzzle = [

        row[:]

        for row in solution

    ]

    empty_cells = DIFFICULTIES[
        difficulty
    ]

    cells = [

        (r, c)

        for r in range(9)

        for c in range(9)

    ]

    random.shuffle(cells)

    for i in range(empty_cells):

        r, c = cells[i]

        puzzle[r][c] = 0

    return puzzle


# =========================================================
# START GAME
# =========================================================

def start_game(selected_difficulty):

    global difficulty
    global solution
    global board
    global selected_cell
    global message
    global game_state
    global game_start_time
    global final_time

    difficulty = selected_difficulty

    solution = generate_solution()

    board = create_puzzle(
        solution,
        difficulty
    )

    selected_cell = None

    message = ""

    final_time = 0

    game_start_time = time.time()

    game_state = "GAME"


# =========================================================
# NEW GAME
# =========================================================

def new_game():

    global solution
    global board
    global selected_cell
    global message
    global game_start_time
    global final_time

    if difficulty is None:

        return

    solution = generate_solution()

    board = create_puzzle(
        solution,
        difficulty
    )

    selected_cell = None

    message = ""

    final_time = 0

    game_start_time = time.time()


# =========================================================
# TIMER
# =========================================================

def get_elapsed_time():

    if game_start_time is None:

        return 0

    if message == "YOU WIN!":

        return final_time

    return int(
        time.time()
        -
        game_start_time
    )


def format_time(seconds):

    minutes = seconds // 60

    seconds = seconds % 60

    return f"{minutes:02d}:{seconds:02d}"


# =========================================================
# LEVEL BUTTONS
# =========================================================

def get_level_buttons():

    button_width = 300
    button_height = 75

    x = (
        WIDTH // 2
        -
        button_width // 2
    )

    buttons = {

        "EASY": pygame.Rect(
            x,
            250,
            button_width,
            button_height
        ),

        "MEDIUM": pygame.Rect(
            x,
            360,
            button_width,
            button_height
        ),

        "HARD": pygame.Rect(
            x,
            470,
            button_width,
            button_height
        )

    }

    return buttons


# =========================================================
# NUMBER BUTTONS
# =========================================================

def get_number_buttons():

    button_size = 55

    gap = 8

    total_width = (
        button_size * 9
        +
        gap * 8
    )

    start_x = (
        WIDTH // 2
        -
        total_width // 2
    )

    y = 735

    buttons = []

    for i in range(9):

        x = (
            start_x
            +
            i * (
                button_size + gap
            )
        )

        rect = pygame.Rect(
            x,
            y,
            button_size,
            button_size
        )

        buttons.append(rect)

    return buttons


# =========================================================
# ERASE BUTTON
# =========================================================

def get_erase_button():

    return pygame.Rect(

        WIDTH // 2 - 90,

        810,

        180,

        50

    )


# =========================================================
# DRAW LEVEL SELECT
# =========================================================

def draw_level_select():

    screen.fill(
        BACKGROUND
    )

    title = fonts["date"].render(
        "SUDOKU",
        True,
        WHITE
    )

    screen.blit(
        title,
        (
            WIDTH // 2
            -
            title.get_width() // 2,
            90
        )
    )

    subtitle = fonts["heart"].render(
        "SELECT LEVEL",
        True,
        WHITE
    )

    screen.blit(
        subtitle,
        (
            WIDTH // 2
            -
            subtitle.get_width() // 2,
            170
        )
    )

    buttons = get_level_buttons()

    mouse_pos = pygame.mouse.get_pos()

    for level, rect in buttons.items():

        if rect.collidepoint(
            mouse_pos
        ):

            color = BUTTON_HOVER

        else:

            color = BUTTON

        pygame.draw.rect(
            screen,
            color,
            rect,
            border_radius=15
        )

        text = fonts["date"].render(
            level,
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


# =========================================================
# DRAW NUMBER BUTTONS
# =========================================================

def draw_number_buttons():

    buttons = get_number_buttons()

    mouse_pos = pygame.mouse.get_pos()

    for i, rect in enumerate(buttons):

        if rect.collidepoint(
            mouse_pos
        ):

            color = BUTTON_HOVER

        else:

            color = BUTTON

        pygame.draw.rect(
            screen,
            color,
            rect,
            border_radius=10
        )

        text = fonts["date"].render(
            str(i + 1),
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


# =========================================================
# DRAW ERASE BUTTON
# =========================================================

def draw_erase_button():

    rect = get_erase_button()

    mouse_pos = pygame.mouse.get_pos()

    if rect.collidepoint(
        mouse_pos
    ):

        color = BUTTON_HOVER

    else:

        color = BUTTON

    pygame.draw.rect(
        screen,
        color,
        rect,
        border_radius=10
    )

    text = fonts["date"].render(
        "ERASE",
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


# =========================================================
# DRAW 9 BOX GRIDS
# =========================================================

def draw_box_grids():

    for box_index in range(9):

        box_x, box_y = BOX_POSITIONS[
            box_index
        ]

        box_size = BOX_SIZES[
            box_index
        ]

        # -------------------------------------------------
        # هر باکس 3x3
        # -------------------------------------------------

        cell_size = box_size // 3

        # -------------------------------------------------
        # خطوط عمودی
        # -------------------------------------------------

        for i in range(4):

            x = (
                BOARD_X
                +
                box_x
                +
                i * cell_size
            )

            pygame.draw.line(
                screen,
                LINE_COLOR,
                (
                    x,
                    BOARD_Y + box_y
                ),
                (
                    x,
                    BOARD_Y
                    +
                    box_y
                    +
                    box_size
                ),
                1
            )

        # -------------------------------------------------
        # خطوط افقی
        # -------------------------------------------------

        for i in range(4):

            y = (
                BOARD_Y
                +
                box_y
                +
                i * cell_size
            )

            pygame.draw.line(
                screen,
                LINE_COLOR,
                (
                    BOARD_X + box_x,
                    y
                ),
                (
                    BOARD_X
                    +
                    box_x
                    +
                    box_size,
                    y
                ),
                1
            )


# =========================================================
# DRAW GAME
# =========================================================

def draw_game():

    screen.fill(
        BACKGROUND
    )

    # =====================================================
    # TITLE
    # =====================================================

    title = fonts["date"].render(
        "SUDOKU",
        True,
        WHITE
    )

    screen.blit(
        title,
        (
            WIDTH // 2
            -
            title.get_width() // 2,
            15
        )
    )

    # =====================================================
    # DIFFICULTY
    # =====================================================

    difficulty_text = fonts["heart"].render(
        difficulty,
        True,
        WHITE
    )

    screen.blit(
        difficulty_text,
        (
            WIDTH // 2
            -
            difficulty_text.get_width() // 2,
            80
        )
    )

    # =====================================================
    # TIMER
    # =====================================================

    elapsed = get_elapsed_time()

    timer_text = fonts["date"].render(
        f"TIME  {format_time(elapsed)}",
        True,
        WHITE
    )

    screen.blit(
        timer_text,
        (
            WIDTH // 2
            -
            timer_text.get_width() // 2,
            110
        )
    )

    # =====================================================
    # BOARD POSITION
    # =====================================================

    BOARD_X = (
        WIDTH
        -
        BOARD_SIZE
    ) // 2

    BOARD_Y = (
        HEIGHT
        -
        BOARD_SIZE
    ) // 2

    # =====================================================
    # ONE BACKGROUND IMAGE
    # =====================================================
    #
    # این عکس اصلاً تقسیم نمی‌شود.
    # =====================================================

    screen.blit(
        board_image,
        (
            BOARD_X,
            BOARD_Y
        )
    )

    # =====================================================
    # SELECTED CELL
    # =====================================================

    if selected_cell is not None:

        row, col = selected_cell

        rect = get_screen_cell_rect(
            row,
            col
        )

        pygame.draw.rect(
            screen,
            SELECT_COLOR,
            rect
        )

    # =====================================================
    # NUMBERS
    # =====================================================

    for row in range(9):

        for col in range(9):

            value = board[row][col]

            if value == 0:

                continue

            # -------------------------------------------------
            # COLOR
            # -------------------------------------------------

            if value == solution[row][col]:

                color = FIXED_COLOR

            else:

                color = PLAYER_COLOR

            # -------------------------------------------------
            # TEXT
            # -------------------------------------------------

            text = fonts["date"].render(
                str(value),
                True,
                color
            )

            # -------------------------------------------------
            # CELL
            # -------------------------------------------------

            rect = get_screen_cell_rect(
                row,
                col
            )

            # -------------------------------------------------
            # CENTER
            # -------------------------------------------------

            x = (
                rect.centerx
                -
                text.get_width() // 2
            )

            y = (
                rect.centery
                -
                text.get_height() // 2
            )

            screen.blit(
                text,
                (
                    x,
                    y
                )
            )

    # =====================================================
    # GRID
    # =====================================================

    draw_box_grids()

    # =====================================================
    # NUMBER BUTTONS
    # =====================================================

    draw_number_buttons()

    # =====================================================
    # ERASE
    # =====================================================

    draw_erase_button()

    # =====================================================
    # WIN MESSAGE
    # =====================================================

    if message:

        win_text = fonts["date"].render(
            message,
            True,
            GREEN
        )

        screen.blit(
            win_text,
            (
                WIDTH // 2
                -
                win_text.get_width() // 2,
                680
            )
        )


# =========================================================
# CHECK WIN
# =========================================================

def check_win():

    for row in range(9):

        for col in range(9):

            if (
                board[row][col]
                !=
                solution[row][col]
            ):

                return False

    return True


# =========================================================
# PUT NUMBER
# =========================================================

def put_number(number):

    global message
    global final_time

    if selected_cell is None:

        return

    if message == "YOU WIN!":

        return

    row, col = selected_cell

    # -----------------------------------------------------
    # ORIGINAL CELL
    # -----------------------------------------------------

    if board[row][col] == solution[row][col]:

        return

    # -----------------------------------------------------
    # PUT NUMBER
    # -----------------------------------------------------

    board[row][col] = number

    # -----------------------------------------------------
    # CHECK WIN
    # -----------------------------------------------------

    if check_win():

        final_time = int(
            time.time()
            -
            game_start_time
        )

        message = "YOU WIN!"


# =========================================================
# ERASE NUMBER
# =========================================================

def erase_number():

    if selected_cell is None:

        return

    row, col = selected_cell

    if board[row][col] == solution[row][col]:

        return

    board[row][col] = 0


# =========================================================
# FIND CELL FROM MOUSE
# =========================================================

def get_cell_from_mouse(
    mouse_x,
    mouse_y
):

    # -----------------------------------------------------
    # بررسی هر 9 باکس
    # -----------------------------------------------------

    for box_index in range(9):

        box_x, box_y = BOX_POSITIONS[
            box_index
        ]

        box_size = BOX_SIZES[
            box_index
        ]

        rect = pygame.Rect(
            BOARD_X + box_x,
            BOARD_Y + box_y,
            box_size,
            box_size
        )

        # -------------------------------------------------
        # آیا داخل این باکس کلیک شده؟
        # -------------------------------------------------

        if rect.collidepoint(
            mouse_x,
            mouse_y
        ):

            # ---------------------------------------------
            # Cell size
            # ---------------------------------------------

            cell_size = box_size // 3

            local_x = (
                mouse_x
                -
                (
                    BOARD_X
                    +
                    box_x
                )
            )

            local_y = (
                mouse_y
                -
                (
                    BOARD_Y
                    +
                    box_y
                )
            )

            local_col = (
                local_x
                //
                cell_size
            )

            local_row = (
                local_y
                //
                cell_size
            )

            # ---------------------------------------------
            # Safety
            # ---------------------------------------------

            if not (
                0 <= local_row < 3
                and
                0 <= local_col < 3
            ):

                return None

            # ---------------------------------------------
            # Sudoku row
            # ---------------------------------------------

            row = (
                (box_index // 3) * 3
                +
                local_row
            )

            # ---------------------------------------------
            # Sudoku column
            # ---------------------------------------------

            col = (
                (box_index % 3) * 3
                +
                local_col
            )

            return (
                row,
                col
            )

    return None


# =========================================================
# EVENT SUDOKU
# =========================================================

def event_sudoku(event):

    global game_state
    global selected_cell

    # =====================================================
    # LEVEL SELECT
    # =====================================================

    if game_state == "LEVEL_SELECT":

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                buttons = get_level_buttons()

                for level, rect in buttons.items():

                    if rect.collidepoint(
                        event.pos
                    ):

                        start_game(level)

                        return

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:

                reset_sudoku()

                return

    # =====================================================
    # GAME
    # =====================================================

    elif game_state == "GAME":

        # -------------------------------------------------
        # KEYBOARD
        # -------------------------------------------------

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:

                game_state = "LEVEL_SELECT"

                selected_cell = None

                return

            elif event.key == pygame.K_r:

                new_game()

                return

        # -------------------------------------------------
        # MOUSE
        # -------------------------------------------------

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                mouse_x, mouse_y = event.pos

                # =========================================
                # NUMBER BUTTONS
                # =========================================

                buttons = get_number_buttons()

                for i, rect in enumerate(buttons):

                    if rect.collidepoint(
                        event.pos
                    ):

                        put_number(
                            i + 1
                        )

                        return

                # =========================================
                # ERASE
                # =========================================

                erase_button = get_erase_button()

                if erase_button.collidepoint(
                    event.pos
                ):

                    erase_number()

                    return

                # =========================================
                # SUDOKU BOXES
                # =========================================

                cell = get_cell_from_mouse(
                    mouse_x,
                    mouse_y
                )

                if cell is not None:

                    selected_cell = cell

                    return

    # =====================================================
    # GLOBAL RESET
    # =====================================================

    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_ESCAPE:

            reset_sudoku()


# =========================================================
# MAIN DRAW
# =========================================================

def SUDOKU_():

    if game_state == "LEVEL_SELECT":

        draw_level_select()

    elif game_state == "GAME":

        draw_game()
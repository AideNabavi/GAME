
import pygame
import random

from modules.font import fonts


MENU_BACKGROUND = pygame.image.load(
    "asset/image/GAME/first_page.png"
).convert()


# ============================================================
# GLOBAL
# ============================================================

WIDTH = 1920
HEIGHT = 1080
screen = None

def WIDTH_HEIGHT_gettter(screen_, WIDTH_, HEIGHT_):

    global WIDTH
    global HEIGHT
    global screen
    global MENU_BACKGROUND

    WIDTH = WIDTH_
    HEIGHT = HEIGHT_
    screen = screen_


    MENU_BACKGROUND = pygame.transform.smoothscale(
        MENU_BACKGROUND,
        (WIDTH_, HEIGHT_)
    )
# ============================================================
# COLORS
# ============================================================

BACKGROUND = (28, 32, 38)

BUTTON = (65, 75, 85)
BUTTON_HOVER = (90, 105, 115)

WHITE = (245, 245, 245)
BLACK = (15, 15, 15)

X_COLOR = (220, 80, 80)
O_COLOR = (80, 150, 230)

WIN_COLOR = (80, 210, 120)


# ============================================================
# STATES
# ============================================================

MENU = "MENU"
GAME = "GAME"
WIN_ANIMATION = "WIN_ANIMATION"
WIN = "WIN"


# ============================================================
# GAME STATE
# ============================================================

TOZE_state = MENU


# ============================================================
# GAME VARIABLES
# ============================================================

difficulty = None

board = [""] * 9

player = "X"
computer = "O"

current_turn = player

winner = None


# ============================================================
# SCORE
# ============================================================

player_score = 0
computer_score = 0

X_CACHE = {}
O_CACHE = {}
# ============================================================
# BOARD
# ============================================================

BOARD_SIZE = 855
CELL_SIZE = BOARD_SIZE // 3

PIECE_SIZE = int(CELL_SIZE * 0.70)


# ============================================================
# LOAD IMAGES
# ============================================================

X_IMAGE = pygame.transform.smoothscale(
    pygame.image.load(
        "asset/image/GAME/THOOZ/X.png"
    ).convert_alpha(),
    (100, 100)
)


O_IMAGE = pygame.transform.smoothscale(
    pygame.image.load(
        "asset/image/GAME/THOOZ/O.png"
    ).convert_alpha(),
    (100, 100)
)


# ============================================================
# WINNING LINE
# ============================================================

winning_line = None
winning_line_start = 0


# ============================================================
# COMPUTER DELAY
# ============================================================

computer_move_pending = False
computer_move_start = 0


# ============================================================
# PIECE ANIMATION
# ============================================================

piece_animation_start = {}


# ============================================================
# RESET CURRENT ROUND
# ============================================================

def reset_game():

    global board
    global current_turn
    global winner

    global winning_line
    global winning_line_start

    global computer_move_pending
    global computer_move_start

    global piece_animation_start

    board = [""] * 9

    current_turn = player

    winner = None

    winning_line = None
    winning_line_start = 0

    computer_move_pending = False
    computer_move_start = 0

    piece_animation_start = {}


# ============================================================
# RESET EVERYTHING
# ============================================================

def reset_all():

    global player_score
    global computer_score
    global difficulty
    global TOZE_state

    player_score = 0
    computer_score = 0

    difficulty = None

    reset_game()

    TOZE_state = MENU


# ============================================================
# SET DIFFICULTY
# ============================================================

def set_difficulty(level):

    global difficulty
    global TOZE_state

    difficulty = level

    # فقط راند جدید
    # امتیازها ریست نمی‌شوند
    reset_game()

    TOZE_state = GAME


# ============================================================
# RETURN TO MENU
# ============================================================

def go_to_menu():

    global TOZE_state

    TOZE_state = MENU


# ============================================================
# CHECK WINNER
# ============================================================

def check_winner(game_board):

    winning_lines = [

        # Horizontal
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),

        # Vertical
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),

        # Diagonal
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_lines:

        if (
            game_board[a] != ""
            and game_board[a] == game_board[b]
            and game_board[a] == game_board[c]
        ):

            return game_board[a]

    # Draw
    if "" not in game_board:

        return "DRAW"

    return None


# ============================================================
# GET WINNING LINE
# ============================================================

def get_winning_line(game_board):

    winning_lines = [

        # Horizontal
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),

        # Vertical
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),

        # Diagonal
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_lines:

        if (
            game_board[a] != ""
            and game_board[a] == game_board[b]
            and game_board[a] == game_board[c]
        ):

            return (a, b, c)

    return None


# ============================================================
# EMPTY CELLS
# ============================================================

def get_empty_cells(game_board):

    return [
        index
        for index in range(9)
        if game_board[index] == ""
    ]


# ============================================================
# FIND WINNING MOVE
# ============================================================

def find_winning_move(game_board, symbol):

    for index in get_empty_cells(game_board):

        game_board[index] = symbol

        result = check_winner(game_board)

        game_board[index] = ""

        if result == symbol:

            return index

    return None


# ============================================================
# EASY AI
# ============================================================

def easy_move():

    empty = get_empty_cells(board)

    if not empty:

        return None

    return random.choice(empty)


# ============================================================
# MEDIUM AI
# ============================================================

def medium_move():

    # --------------------------------------------------------
    # 1. Try to win
    # --------------------------------------------------------

    move = find_winning_move(
        board,
        computer
    )

    if move is not None:

        return move

    # --------------------------------------------------------
    # 2. Block player
    # --------------------------------------------------------

    move = find_winning_move(
        board,
        player
    )

    if move is not None:

        return move

    # --------------------------------------------------------
    # 3. Center
    # --------------------------------------------------------

    if board[4] == "":

        return 4

    # --------------------------------------------------------
    # 4. Corners
    # --------------------------------------------------------

    corners = [
        0,
        2,
        6,
        8
    ]

    available_corners = [
        index
        for index in corners
        if board[index] == ""
    ]

    if available_corners:

        return random.choice(
            available_corners
        )

    # --------------------------------------------------------
    # 5. Random
    # --------------------------------------------------------

    return easy_move()


# ============================================================
# MINIMAX
# ============================================================

def minimax(game_board, maximizing):

    result = check_winner(game_board)

    # Computer wins
    if result == computer:

        return 1

    # Player wins
    if result == player:

        return -1

    # Draw
    if result == "DRAW":

        return 0

    # --------------------------------------------------------
    # Computer
    # --------------------------------------------------------

    if maximizing:

        best_score = -999

        for index in get_empty_cells(game_board):

            game_board[index] = computer

            score = minimax(
                game_board,
                False
            )

            game_board[index] = ""

            best_score = max(
                best_score,
                score
            )

        return best_score

    # --------------------------------------------------------
    # Player
    # --------------------------------------------------------

    else:

        best_score = 999

        for index in get_empty_cells(game_board):

            game_board[index] = player

            score = minimax(
                game_board,
                True
            )

            game_board[index] = ""

            best_score = min(
                best_score,
                score
            )

        return best_score


# ============================================================
# HARD AI
# ============================================================

def hard_move():

    best_score = -999

    best_move = None

    for index in get_empty_cells(board):

        board[index] = computer

        score = minimax(
            board,
            False
        )

        board[index] = ""

        if score > best_score:

            best_score = score

            best_move = index

    return best_move


# ============================================================
# COMPUTER MOVE SELECTOR
# ============================================================

def computer_move():

    if difficulty == "EASY":

        return easy_move()

    elif difficulty == "MEDIUM":

        return medium_move()

    elif difficulty == "HARD":

        return hard_move()

    return None


# ============================================================
# START WIN
# ============================================================

def start_win(winner_result):

    global winner
    global winning_line
    global winning_line_start
    global TOZE_state

    global player_score
    global computer_score

    winner = winner_result

    # --------------------------------------------------------
    # Player wins
    # --------------------------------------------------------

    if winner == player:

        player_score += 1

    # --------------------------------------------------------
    # Computer wins
    # --------------------------------------------------------

    elif winner == computer:

        computer_score += 1

    # --------------------------------------------------------
    # Get winning line
    # --------------------------------------------------------

    winning_line = get_winning_line(board)

    winning_line_start = pygame.time.get_ticks()

    # --------------------------------------------------------
    # Start animation
    # --------------------------------------------------------

    TOZE_state = WIN_ANIMATION


# ============================================================
# UPDATE COMPUTER MOVE
# ============================================================

def update_computer_move():

    global current_turn
    global computer_move_pending

    if not computer_move_pending:

        return

    now = pygame.time.get_ticks()

    # 500ms delay
    if now - computer_move_start < 500:

        return

    computer_move_pending = False

    move = computer_move()

    if move is None:

        return

    # --------------------------------------------------------
    # Put O
    # --------------------------------------------------------

    board[move] = computer

    piece_animation_start[move] = pygame.time.get_ticks()

    # --------------------------------------------------------
    # Check result
    # --------------------------------------------------------

    result = check_winner(board)

    if result:

        start_win(result)

        return

    # --------------------------------------------------------
    # Player turn
    # --------------------------------------------------------

    current_turn = player


# ============================================================
# UPDATE WIN ANIMATION
# ============================================================

def update_win_animation():

    global TOZE_state

    now = pygame.time.get_ticks()

    elapsed = now - winning_line_start

    # 500ms winning line animation
    if elapsed >= 500:

        TOZE_state = WIN


# ============================================================
# PLAYER MOVE
# ============================================================

def player_move(index):

    global current_turn
    global computer_move_pending
    global computer_move_start

    # فقط وقتی نوبت Player است
    if current_turn != player:

        return

    # خانه پر است
    if board[index] != "":

        return

    # --------------------------------------------------------
    # Player X
    # --------------------------------------------------------

    board[index] = player

    piece_animation_start[index] = pygame.time.get_ticks()

    # --------------------------------------------------------
    # Check player result
    # --------------------------------------------------------

    result = check_winner(board)

    if result:

        start_win(result)

        return

    # --------------------------------------------------------
    # Computer turn
    # --------------------------------------------------------

    current_turn = computer

    computer_move_pending = True

    computer_move_start = pygame.time.get_ticks()


# ============================================================
# BOARD POSITION
# ============================================================

def get_board_position(WIDTH):

    start_x = (
        WIDTH - BOARD_SIZE
    ) // 2  

    start_y = (
        HEIGHT - BOARD_SIZE
    ) // 2  - 40

    return start_x, start_y


# ============================================================
# BOARD RECT
# ============================================================

def get_board_rect(WIDTH):

    start_x, start_y = get_board_position(WIDTH)

    return pygame.Rect(
        start_x,
        start_y,
        BOARD_SIZE,
        BOARD_SIZE
    )


# ============================================================
# GET CELL FROM MOUSE
# ============================================================

def get_cell_from_mouse(mouse_pos, WIDTH):

    mouse_x, mouse_y = mouse_pos

    start_x, start_y = get_board_position(WIDTH)

    # خارج Board
    if not (
        start_x <= mouse_x < start_x + BOARD_SIZE
        and
        start_y <= mouse_y < start_y + BOARD_SIZE
    ):

        return None

    col = (
        mouse_x - start_x
    ) // CELL_SIZE

    row = (
        mouse_y - start_y
    ) // CELL_SIZE

    if row < 0 or row > 2:

        return None

    if col < 0 or col > 2:

        return None

    index = row * 3 + col

    return index


# ============================================================
# DRAW BUTTON
# ============================================================

def draw_button(
    screen,
    rect,
    text
):

    mouse = pygame.mouse.get_pos()

    if rect.collidepoint(mouse):

        color = BUTTON_HOVER

    else:

        color = BUTTON

    pygame.draw.rect(
        screen,
        color,
        rect,
        border_radius=15
    )

    text_surface = fonts["heart"].render(
        text,
        True,
        WHITE
    )

    text_rect = text_surface.get_rect(
        center=rect.center
    )

    screen.blit(
        text_surface,
        text_rect
    )


# ============================================================
# MENU BUTTONS
# ============================================================

def get_menu_buttons(WIDTH):

    button_width = 320
    button_height = 80

    x = (
        WIDTH // 2
        - button_width // 2
    )

    easy_button = pygame.Rect(
        x,
        250,
        button_width,
        button_height
    )

    medium_button = pygame.Rect(
        x,
        360,
        button_width,
        button_height
    )

    hard_button = pygame.Rect(
        x,
        470,
        button_width,
        button_height
    )

    return (
        easy_button,
        medium_button,
        hard_button
    )


# ============================================================
# WIN BUTTONS
# ============================================================

def get_win_buttons(WIDTH):

    again_button = pygame.Rect(
        WIDTH // 2 - 160,
        380,
        320,
        80
    )

    menu_button = pygame.Rect(
        WIDTH // 2 - 160,
        490,
        320,
        80
    )

    return (
        again_button,
        menu_button
    )


# ============================================================
# DRAW MENU
# ============================================================

def draw_menu(
    screen,
    WIDTH
):



    screen.blit(
        MENU_BACKGROUND,
        (0, 0)
    )
    # --------------------------------------------------------
    # Title
    # --------------------------------------------------------

    title = fonts["heart"].render(
        "TIC TAC TOE",
        True,
        WHITE
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

    # --------------------------------------------------------
    # Score
    # --------------------------------------------------------

    score_text = fonts["heart"].render(
        f"YOU  {player_score}   -   {computer_score}  BOT",
        True,
        WHITE
    )

    score_rect = score_text.get_rect(
        center=(
            WIDTH // 2,
            180
        )
    )

    screen.blit(
        score_text,
        score_rect
    )

    # --------------------------------------------------------
    # Subtitle
    # --------------------------------------------------------

    subtitle = fonts["heart"].render(
        "Choose difficulty",
        True,
        WHITE
    )

    subtitle_rect = subtitle.get_rect(
        center=(
            WIDTH // 2,
            220
        )
    )

    screen.blit(
        subtitle,
        subtitle_rect
    )

    # --------------------------------------------------------
    # Buttons
    # --------------------------------------------------------

    (
        easy_button,
        medium_button,
        hard_button
    ) = get_menu_buttons(WIDTH)

    draw_button(
        screen,
        easy_button,
        "EASY"
    )

    draw_button(
        screen,
        medium_button,
        "MEDIUM"
    )

    draw_button(
        screen,
        hard_button,
        "HARD"
    )


# ============================================================
# DRAW SCORE
# ============================================================

def draw_score(screen, WIDTH):

    score_text = fonts["heart"].render(
        f"YOU: {player_score}     BOT: {computer_score}",
        True,
        WHITE
    )

    score_rect = score_text.get_rect(
        center=(
            WIDTH // 2,
            35
        )
    )

    screen.blit(
        score_text,
        score_rect
    )


# ============================================================
# DRAW GAME
# ============================================================

def draw_game(
    screen,
    WIDTH
):

    # --------------------------------------------------------
    # Level
    # --------------------------------------------------------

    title = fonts["heart"].render(
        f"LEVEL: {difficulty}",
        True,
        WHITE
    )

    screen.blit(
        title,
        (40, 30)
    )

    # --------------------------------------------------------
    # Score
    # --------------------------------------------------------

    draw_score(
        screen,
        WIDTH
    )

    # --------------------------------------------------------
    # Turn
    # --------------------------------------------------------

    turn_text = fonts["heart"].render(
        f"TURN: {current_turn}",
        True,
        WHITE
    )

    turn_rect = turn_text.get_rect(
        top=30,
        right=WIDTH - 40
    )

    screen.blit(
        turn_text,
        turn_rect
    )

    # --------------------------------------------------------
    # Board Position
    # --------------------------------------------------------

    start_x, start_y = get_board_position(WIDTH)


    # --------------------------------------------------------
    # Grid
    # --------------------------------------------------------

    # for i in range(1, 3):

    #     # Vertical
    #     pygame.draw.line(
    #         screen,
    #         WHITE,
    #         (
    #             start_x + i * CELL_SIZE,
    #             start_y
    #         ),
    #         (
    #             start_x + i * CELL_SIZE,
    #             start_y + BOARD_SIZE
    #         ),
    #         5
    #     )

    #     # Horizontal
    #     pygame.draw.line(
    #         screen,
    #         WHITE,
    #         (
    #             start_x,
    #             start_y + i * CELL_SIZE
    #         ),
    #         (
    #             start_x + BOARD_SIZE,
    #             start_y + i * CELL_SIZE
    #         ),
    #         5
    #     )

    # --------------------------------------------------------
    # X / O
    # --------------------------------------------------------

    now = pygame.time.get_ticks()

    for index, value in enumerate(board):

        if value == "":

            continue

        row = index // 3
        col = index % 3

        center_x = (
            start_x
            + col * CELL_SIZE
            + CELL_SIZE // 2
        )

        center_y = (
            start_y
            + row * CELL_SIZE
            + CELL_SIZE // 2
        )

        if value == "X":

            piece = X_IMAGE

        else:

            piece = O_IMAGE

        base_size = PIECE_SIZE

        start_time = piece_animation_start.get(index)

        if start_time is not None:

            elapsed = now - start_time

            duration = 250

            if elapsed < duration:

                progress = elapsed / duration

                # Zoom from 20% -> 100%
                scale = (
                    0.2
                    + 0.8 * progress
                )

            else:

                scale = 1.0

            size = int(
                base_size * scale
            )

        else:

            size = base_size

        # piece_scaled = pygame.transform.smoothscale(
        #     piece,
        #     (
        #         size,
        #         size
        #     )
        # )
        cache = X_CACHE if value == "X" else O_CACHE

        if size not in cache:

            cache[size] = pygame.transform.smoothscale(
                piece,
                (size, size)
            )

        piece_scaled = cache[size]
        
        piece_rect = piece_scaled.get_rect(
            center=(
                center_x,
                center_y
            )
        )

        screen.blit(
            piece_scaled,
            piece_rect
        )

    # --------------------------------------------------------
    # Winning Line
    # --------------------------------------------------------

    if winning_line is not None:

        now = pygame.time.get_ticks()

        elapsed = (
            now
            - winning_line_start
        )

        duration = 500

        progress = min(
            elapsed / duration,
            1.0
        )

        start_index = winning_line[0]
        end_index = winning_line[2]

        start_row = start_index // 3
        start_col = start_index % 3

        end_row = end_index // 3
        end_col = end_index % 3

        start_pos = (
            start_x
            + start_col * CELL_SIZE
            + CELL_SIZE // 2,

            start_y
            + start_row * CELL_SIZE
            + CELL_SIZE // 2
        )

        end_pos = (
            start_x
            + end_col * CELL_SIZE
            + CELL_SIZE // 2,

            start_y
            + end_row * CELL_SIZE
            + CELL_SIZE // 2
        )

        current_pos = (
            start_pos[0]
            + (
                end_pos[0]
                - start_pos[0]
            ) * progress,

            start_pos[1]
            + (
                end_pos[1]
                - start_pos[1]
            ) * progress
        )

        pygame.draw.line(
            screen,
            WIN_COLOR,
            start_pos,
            current_pos,
            12
        )


# ============================================================
# DRAW WIN
# ============================================================

def draw_win(
    screen,
    WIDTH
):

    screen.fill(
        BACKGROUND
    )

    # --------------------------------------------------------
    # Result
    # --------------------------------------------------------

    if winner == player:

        title_text = "YOU WIN!"

        title_color = WIN_COLOR

    elif winner == computer:

        title_text = "YOU LOSE!"

        title_color = X_COLOR

    else:

        title_text = "DRAW!"

        title_color = WHITE

    title = fonts["heart"].render(
        title_text,
        True,
        title_color
    )

    title_rect = title.get_rect(
        center=(
            WIDTH // 2,
            180
        )
    )

    screen.blit(
        title,
        title_rect
    )

    # --------------------------------------------------------
    # Score
    # --------------------------------------------------------

    score_text = fonts["heart"].render(
        f"YOU: {player_score}     BOT: {computer_score}",
        True,
        WHITE
    )

    score_rect = score_text.get_rect(
        center=(
            WIDTH // 2,
            260
        )
    )

    screen.blit(
        score_text,
        score_rect
    )

    # --------------------------------------------------------
    # Buttons
    # --------------------------------------------------------

    (
        again_button,
        menu_button
    ) = get_win_buttons(WIDTH)

    draw_button(
        screen,
        again_button,
        "PLAY AGAIN"
    )

    draw_button(
        screen,
        menu_button,
        "MENU"
    )


# ============================================================
# MAIN DRAW / UPDATE FUNCTION
# ============================================================

def THOOZ_(
    screen,
    WIDTH
):

    global TOZE_state

    # --------------------------------------------------------
    # MENU
    # --------------------------------------------------------

    if TOZE_state == MENU:

        draw_menu(
            screen,
            WIDTH
        )

    # --------------------------------------------------------
    # GAME
    # --------------------------------------------------------

    elif TOZE_state == GAME:

        # Update computer delay
        update_computer_move()

        draw_game(
            screen,
            WIDTH
        )

    # --------------------------------------------------------
    # WIN ANIMATION
    # --------------------------------------------------------

    elif TOZE_state == WIN_ANIMATION:

        update_win_animation()

        draw_game(
            screen,
            WIDTH
        )

    # --------------------------------------------------------
    # WIN SCREEN
    # --------------------------------------------------------

    elif TOZE_state == WIN:

        draw_win(
            screen,
            WIDTH
        )


# ============================================================
# TIC TAC TOE EVENT
# ============================================================

def event_THOZ(
    event,
    WIDTH
):

    global TOZE_state

    # ========================================================
    # MENU
    # ========================================================

    if TOZE_state == MENU:

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse = event.pos

            (
                easy_button,
                medium_button,
                hard_button
            ) = get_menu_buttons(WIDTH)

            # ------------------------------------------------
            # EASY
            # ------------------------------------------------

            if easy_button.collidepoint(mouse):

                set_difficulty(
                    "EASY"
                )

            # ------------------------------------------------
            # MEDIUM
            # ------------------------------------------------

            elif medium_button.collidepoint(mouse):

                set_difficulty(
                    "MEDIUM"
                )

            # ------------------------------------------------
            # HARD
            # ------------------------------------------------

            elif hard_button.collidepoint(mouse):

                set_difficulty(
                    "HARD"
                )

    # ========================================================
    # GAME
    # ========================================================

    elif TOZE_state == GAME:

        # ----------------------------------------------------
        # Mouse
        # ----------------------------------------------------

        if event.type == pygame.MOUSEBUTTONDOWN:

            # فقط Player می‌تواند حرکت کند
            if current_turn == player:

                index = get_cell_from_mouse(
                    event.pos,
                    WIDTH
                )

                if index is not None:

                    player_move(
                        index
                    )

        # ----------------------------------------------------
        # ESC
        # ----------------------------------------------------

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:

                go_to_menu()

    # ========================================================
    # WIN ANIMATION
    # ========================================================

    elif TOZE_state == WIN_ANIMATION:

        # در زمان انیمیشن برد
        # کلیک روی صفحه کاری نمی‌کند

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:

                go_to_menu()

    # ========================================================
    # WIN
    # ========================================================

    elif TOZE_state == WIN:

        # ----------------------------------------------------
        # Mouse
        # ----------------------------------------------------

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse = event.pos

            (
                again_button,
                menu_button
            ) = get_win_buttons(WIDTH)

            # ------------------------------------------------
            # PLAY AGAIN
            # ------------------------------------------------

            if again_button.collidepoint(mouse):

                # فقط بازی ریست می‌شود
                # امتیازها باقی می‌مانند
                reset_game()

                TOZE_state = GAME

            # ------------------------------------------------
            # MENU
            # ------------------------------------------------

            elif menu_button.collidepoint(mouse):

                go_to_menu()

        # ----------------------------------------------------
        # ESC
        # ----------------------------------------------------

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:

                go_to_menu()


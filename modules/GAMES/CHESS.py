


import pygame
import random
from copy import deepcopy

from modules.font import *


# ============================================================
# SETTINGS
# ============================================================

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
ROWS = 8
COLS = 8

LIGHT = (240, 217, 181)
DARK = (181, 136, 99)

SELECTED_COLOR = (255, 215, 0)
MOVE_COLOR = (80, 180, 80)
CHECK_COLOR = (220, 70, 70)

BACKGROUND = (35, 35, 35)
BUTTON_COLOR = (100, 100, 100)
WHITE_COLOR = (255, 255, 255)

SQUARE_SIZE = 100


# ============================================================
# GAME STATE
# ============================================================

game_state = "difficulty"

difficulty = None

# Player = White
# Bot    = Black
turn = "white"

selected_square = None

game_over = False
game_result = None

# Promotion state
promotion_pending = False
promotion_square = None
promotion_color = None

# En passant target square
# Example: (5, 3)
en_passant_target = None

# Castling rights
castling_rights = {
    "K": True,   # White king side
    "Q": True,   # White queen side
    "k": True,   # Black king side
    "q": True    # Black queen side
}

# Piece movement history
white_king_moved = False
black_king_moved = False

white_rook_a_moved = False
white_rook_h_moved = False

black_rook_a_moved = False
black_rook_h_moved = False


# ============================================================
# BOARD
# ============================================================

INITIAL_BOARD = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"]
]

board = deepcopy(INITIAL_BOARD)


# ============================================================
# PIECE VALUES
# ============================================================

PIECE_VALUES = {
    "p": 100,
    "n": 320,
    "b": 330,
    "r": 500,
    "q": 900,
    "k": 20000
}


# ============================================================
# AI SETTINGS
# ============================================================

AI_DEPTH = {
    "easy": 1,
    "medium": 2,
    "hard": 3
}


# ============================================================
# DIFFICULTY BUTTONS
# ============================================================

difficulty_buttons = {
    "easy": pygame.Rect(250, 250, 300, 80),
    "medium": pygame.Rect(250, 350, 300, 80),
    "hard": pygame.Rect(250, 450, 300, 80)
}


difficulty_font = pygame.font.SysFont(
    "dejavusans",
    45
)


# ============================================================
# CHESS IMAGES
# ============================================================

PIECE_SIZE = (80, 80)

piece_images = {}


def load_piece_images():
    """
    تصاویر مهره‌ها را فقط یک بار لود می‌کند.
    """

    global piece_images

    if piece_images:
        return

    base_path = "/Users/mac/Desktop/app/asset/image/GAME/CHESS"

    names = {
        "K": "king_2.png",
        "Q": "queen_2.png",
        "R": "rook_2.png",
        "B": "bishop_2.png",
        "N": "knight_2.png",
        "P": "pawn_2.png"
    }

    for piece, filename in names.items():

        image = pygame.image.load(
            f"{base_path}/{filename}"
        ).convert_alpha()

        image = pygame.transform.smoothscale(
            image,
            PIECE_SIZE
        )

        piece_images[piece] = image
        piece_images[piece.lower()] = image


# ============================================================
# SCREEN SETUP
# ============================================================

def WIDTH_HEIGHT_gettter(
    screen_,
    WIDTH_,
    HEIGHT_
):
    """
    این تابع را از فایل اصلی پروژه صدا بزن.

    مثال:

        CHESS.WIDTH_HEIGHT_gettter(
            screen,
            WIDTH,
            HEIGHT
        )
    """

    global screen
    global WIDTH
    global HEIGHT
    global SQUARE_SIZE

    screen = screen_

    WIDTH = WIDTH_
    HEIGHT = HEIGHT_

    SQUARE_SIZE = min(
        WIDTH // COLS,
        HEIGHT // ROWS
    )

    load_piece_images()


# ============================================================
# RESET
# ============================================================
def reset_chess():
    """
    بازی را کاملاً ریست می‌کند
    و دوباره به صفحه انتخاب درجه سختی برمی‌گردد.
    """

    global board
    global turn
    global selected_square

    global game_over
    global game_result

    global difficulty

    global promotion_pending
    global promotion_square
    global promotion_color

    global en_passant_target
    global castling_rights

    global game_state

    # --------------------------------------------------------
    # BOARD
    # --------------------------------------------------------

    board = deepcopy(INITIAL_BOARD)

    # --------------------------------------------------------
    # TURN
    # --------------------------------------------------------

    turn = "white"

    # --------------------------------------------------------
    # SELECTION
    # --------------------------------------------------------

    selected_square = None

    # --------------------------------------------------------
    # GAME OVER
    # --------------------------------------------------------

    game_over = False
    game_result = None

    # --------------------------------------------------------
    # DIFFICULTY
    # --------------------------------------------------------

    difficulty = None

    # --------------------------------------------------------
    # PROMOTION
    # --------------------------------------------------------

    promotion_pending = False
    promotion_square = None
    promotion_color = None

    # --------------------------------------------------------
    # EN PASSANT
    # --------------------------------------------------------

    en_passant_target = None

    # --------------------------------------------------------
    # CASTLING
    # --------------------------------------------------------

    castling_rights = {
        "K": True,
        "Q": True,
        "k": True,
        "q": True
    }

    # --------------------------------------------------------
    # BACK TO DIFFICULTY SCREEN
    # --------------------------------------------------------

    game_state = "difficulty"


# ============================================================
# COLORS
# ============================================================

def is_white(piece):
    return (
        piece != ""
        and piece.isupper()
    )


def is_black(piece):
    return (
        piece != ""
        and piece.islower()
    )


def color_of(piece):
    if piece == "":
        return None

    if piece.isupper():
        return "white"

    return "black"


# ============================================================
# BOARD HELPERS
# ============================================================

def inside_board(row, col):

    return (
        0 <= row < 8
        and
        0 <= col < 8
    )


def find_king(board_state, color):

    king = "K" if color == "white" else "k"

    for row in range(8):

        for col in range(8):

            if board_state[row][col] == king:

                return row, col

    return None


# ============================================================
# ATTACK DETECTION
# ============================================================

def is_square_attacked(
    board_state,
    square,
    by_color
):
    """
    بررسی می‌کند خانه موردنظر توسط رنگ مشخص
    مورد حمله قرار گرفته یا نه.

    این تابع یکی از مهم‌ترین قسمت‌های قوانین شطرنج است.
    """

    target_row, target_col = square

    # --------------------------------------------------------
    # PAWN
    # --------------------------------------------------------

    pawn = "P" if by_color == "white" else "p"

    pawn_direction = -1 if by_color == "white" else 1

    source_row = target_row - pawn_direction

    for dc in (-1, 1):

        source_col = target_col - dc

        if inside_board(
            source_row,
            source_col
        ):

            if board_state[source_row][source_col] == pawn:

                return True

    # --------------------------------------------------------
    # KNIGHT
    # --------------------------------------------------------

    knight = "N" if by_color == "white" else "n"

    knight_moves = [
        (-2, -1),
        (-2, 1),
        (-1, -2),
        (-1, 2),
        (1, -2),
        (1, 2),
        (2, -1),
        (2, 1)
    ]

    for dr, dc in knight_moves:

        row = target_row + dr
        col = target_col + dc

        if inside_board(row, col):

            if board_state[row][col] == knight:

                return True

    # --------------------------------------------------------
    # KING
    # --------------------------------------------------------

    king = "K" if by_color == "white" else "k"

    for dr in (-1, 0, 1):

        for dc in (-1, 0, 1):

            if dr == 0 and dc == 0:
                continue

            row = target_row + dr
            col = target_col + dc

            if inside_board(row, col):

                if board_state[row][col] == king:

                    return True

    # --------------------------------------------------------
    # ROOK / QUEEN
    # --------------------------------------------------------

    rook = "R" if by_color == "white" else "r"
    queen = "Q" if by_color == "white" else "q"

    straight_directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in straight_directions:

        row = target_row + dr
        col = target_col + dc

        while inside_board(row, col):

            piece = board_state[row][col]

            if piece != "":

                if piece == rook or piece == queen:
                    return True

                break

            row += dr
            col += dc

    # --------------------------------------------------------
    # BISHOP / QUEEN
    # --------------------------------------------------------

    bishop = "B" if by_color == "white" else "b"

    diagonal_directions = [
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    ]

    for dr, dc in diagonal_directions:

        row = target_row + dr
        col = target_col + dc

        while inside_board(row, col):

            piece = board_state[row][col]

            if piece != "":

                if piece == bishop or piece == queen:
                    return True

                break

            row += dr
            col += dc

    return False


# ============================================================
# CHECK
# ============================================================

def is_in_check(
    board_state,
    color
):

    king_position = find_king(
        board_state,
        color
    )

    if king_position is None:
        return True

    opponent = (
        "black"
        if color == "white"
        else "white"
    )

    return is_square_attacked(
        board_state,
        king_position,
        opponent
    )


# ============================================================
# RAW MOVES
# ============================================================

def get_pseudo_moves(
    board_state,
    row,
    col,
    include_castling=True
):
    """
    حرکت‌های ممکن مهره را بدون اینکه هنوز بررسی کنیم
    شاه خودی در کیش می‌ماند یا نه.
    """

    piece = board_state[row][col]

    if piece == "":
        return []

    color = color_of(piece)

    piece_type = piece.lower()

    moves = []

    # ========================================================
    # PAWN
    # ========================================================

    if piece_type == "p":

        direction = -1 if color == "white" else 1

        start_row = (
            6
            if color == "white"
            else 1
        )

        # یک خانه جلو
        new_row = row + direction

        if inside_board(new_row, col):

            if board_state[new_row][col] == "":

                moves.append(
                    (new_row, col)
                )

                # دو خانه جلو
                new_row_2 = row + direction * 2

                if (
                    row == start_row
                    and
                    board_state[new_row_2][col] == ""
                ):

                    moves.append(
                        (new_row_2, col)
                    )

        # گرفتن مورب
        for dc in (-1, 1):

            new_col = col + dc

            if inside_board(
                new_row,
                new_col
            ):

                target = board_state[
                    new_row
                ][
                    new_col
                ]

                if target != "":

                    if color_of(target) != color:

                        moves.append(
                            (new_row, new_col)
                        )

        # ----------------------------------------------------
        # EN PASSANT
        # ----------------------------------------------------

        if en_passant_target is not None:

            ep_row, ep_col = en_passant_target

            if (
                new_row == ep_row
                and
                abs(ep_col - col) == 1
            ):

                moves.append(
                    (ep_row, ep_col)
                )

    # ========================================================
    # KNIGHT
    # ========================================================

    elif piece_type == "n":

        directions = [
            (-2, -1),
            (-2, 1),
            (-1, -2),
            (-1, 2),
            (1, -2),
            (1, 2),
            (2, -1),
            (2, 1)
        ]

        for dr, dc in directions:

            new_row = row + dr
            new_col = col + dc

            if not inside_board(
                new_row,
                new_col
            ):
                continue

            target = board_state[
                new_row
            ][
                new_col
            ]

            if (
                target == ""
                or
                color_of(target) != color
            ):

                moves.append(
                    (new_row, new_col)
                )

    # ========================================================
    # BISHOP
    # ========================================================

    elif piece_type == "b":

        directions = [
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1)
        ]

        moves.extend(
            get_sliding_moves(
                board_state,
                row,
                col,
                color,
                directions
            )
        )

    # ========================================================
    # ROOK
    # ========================================================

    elif piece_type == "r":

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        moves.extend(
            get_sliding_moves(
                board_state,
                row,
                col,
                color,
                directions
            )
        )

    # ========================================================
    # QUEEN
    # ========================================================

    elif piece_type == "q":

        directions = [
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1),
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        moves.extend(
            get_sliding_moves(
                board_state,
                row,
                col,
                color,
                directions
            )
        )

    # ========================================================
    # KING
    # ========================================================

    elif piece_type == "k":

        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1)
        ]

        for dr, dc in directions:

            new_row = row + dr
            new_col = col + dc

            if not inside_board(
                new_row,
                new_col
            ):
                continue

            target = board_state[
                new_row
            ][
                new_col
            ]

            if (
                target == ""
                or
                color_of(target) != color
            ):

                moves.append(
                    (new_row, new_col)
                )

        # ----------------------------------------------------
        # CASTLING
        # ----------------------------------------------------

        if include_castling:

            moves.extend(
                get_castling_moves(
                    board_state,
                    color
                )
            )

    return moves


# ============================================================
# SLIDING MOVES
# ============================================================

def get_sliding_moves(
    board_state,
    row,
    col,
    color,
    directions
):

    moves = []

    for dr, dc in directions:

        new_row = row + dr
        new_col = col + dc

        while inside_board(
            new_row,
            new_col
        ):

            target = board_state[
                new_row
            ][
                new_col
            ]

            if target == "":

                moves.append(
                    (new_row, new_col)
                )

            else:

                if color_of(target) != color:

                    moves.append(
                        (new_row, new_col)
                    )

                break

            new_row += dr
            new_col += dc

    return moves


# ============================================================
# CASTLING
# ============================================================

def get_castling_moves(
    board_state,
    color
):

    moves = []

    if is_in_check(
        board_state,
        color
    ):
        return moves

    if color == "white":

        king = board_state[7][4]

        if king != "K":
            return moves

        # ----------------------------------------------------
        # KING SIDE
        # ----------------------------------------------------

        if (
            castling_rights["K"]
            and
            board_state[7][5] == ""
            and
            board_state[7][6] == ""
            and
            board_state[7][7] == "R"
        ):

            if (
                not is_square_attacked(
                    board_state,
                    (7, 5),
                    "black"
                )
                and
                not is_square_attacked(
                    board_state,
                    (7, 6),
                    "black"
                )
            ):

                moves.append(
                    (7, 6)
                )

        # ----------------------------------------------------
        # QUEEN SIDE
        # ----------------------------------------------------

        if (
            castling_rights["Q"]
            and
            board_state[7][1] == ""
            and
            board_state[7][2] == ""
            and
            board_state[7][3] == ""
            and
            board_state[7][0] == "R"
        ):

            if (
                not is_square_attacked(
                    board_state,
                    (7, 3),
                    "black"
                )
                and
                not is_square_attacked(
                    board_state,
                    (7, 2),
                    "black"
                )
            ):

                moves.append(
                    (7, 2)
                )

    else:

        king = board_state[0][4]

        if king != "k":
            return moves

        # ----------------------------------------------------
        # KING SIDE
        # ----------------------------------------------------

        if (
            castling_rights["k"]
            and
            board_state[0][5] == ""
            and
            board_state[0][6] == ""
            and
            board_state[0][7] == "r"
        ):

            if (
                not is_square_attacked(
                    board_state,
                    (0, 5),
                    "white"
                )
                and
                not is_square_attacked(
                    board_state,
                    (0, 6),
                    "white"
                )
            ):

                moves.append(
                    (0, 6)
                )

        # ----------------------------------------------------
        # QUEEN SIDE
        # ----------------------------------------------------

        if (
            castling_rights["q"]
            and
            board_state[0][1] == ""
            and
            board_state[0][2] == ""
            and
            board_state[0][3] == ""
            and
            board_state[0][0] == "r"
        ):

            if (
                not is_square_attacked(
                    board_state,
                    (0, 3),
                    "white"
                )
                and
                not is_square_attacked(
                    board_state,
                    (0, 2),
                    "white"
                )
            ):

                moves.append(
                    (0, 2)
                )

    return moves


# ============================================================
# MAKE MOVE ON COPY
# ============================================================

def make_move_on_board(
    board_state,
    start,
    end,
    promotion=None
):

    new_board = deepcopy(board_state)

    start_row, start_col = start
    end_row, end_col = end

    piece = new_board[
        start_row
    ][
        start_col
    ]

    captured_piece = new_board[
        end_row
    ][
        end_col
    ]

    # ========================================================
    # EN PASSANT CAPTURE
    # ========================================================

    if (
        piece.lower() == "p"
        and
        start_col != end_col
        and
        captured_piece == ""
    ):

        new_board[
            start_row
        ][
            end_col
        ] = ""

    # ========================================================
    # NORMAL MOVE
    # ========================================================

    new_board[
        end_row
    ][
        end_col
    ] = piece

    new_board[
        start_row
    ][
        start_col
    ] = ""

    # ========================================================
    # CASTLING
    # ========================================================

    if piece.lower() == "k":

        # White king side
        if (
            piece == "K"
            and start == (7, 4)
            and end == (7, 6)
        ):

            new_board[7][5] = new_board[7][7]
            new_board[7][7] = ""

        # White queen side
        elif (
            piece == "K"
            and start == (7, 4)
            and end == (7, 2)
        ):

            new_board[7][3] = new_board[7][0]
            new_board[7][0] = ""

        # Black king side
        elif (
            piece == "k"
            and start == (0, 4)
            and end == (0, 6)
        ):

            new_board[0][5] = new_board[0][7]
            new_board[0][7] = ""

        # Black queen side
        elif (
            piece == "k"
            and start == (0, 4)
            and end == (0, 2)
        ):

            new_board[0][3] = new_board[0][0]
            new_board[0][0] = ""

    # ========================================================
    # PROMOTION
    # ========================================================

    if piece == "P" and end_row == 0:

        new_board[end_row][end_col] = (
            promotion if promotion else "Q"
        )

    elif piece == "p" and end_row == 7:

        new_board[end_row][end_col] = (
            promotion.lower()
            if promotion
            else "q"
        )

    return new_board


# ============================================================
# LEGAL MOVES
# ============================================================

def get_legal_moves(
    board_state,
    row,
    col
):

    piece = board_state[row][col]

    if piece == "":
        return []

    color = color_of(piece)

    pseudo_moves = get_pseudo_moves(
        board_state,
        row,
        col
    )

    legal_moves = []

    for move in pseudo_moves:

        test_board = make_move_on_board(
            board_state,
            (row, col),
            move
        )

        # شاه نباید بعد از حرکت در کیش باشد
        if not is_in_check(
            test_board,
            color
        ):

            legal_moves.append(move)

    return legal_moves


# ============================================================
# ALL LEGAL MOVES
# ============================================================

def get_all_legal_moves(
    board_state,
    color
):

    moves = []

    for row in range(8):

        for col in range(8):

            piece = board_state[row][col]

            if piece == "":
                continue

            if color_of(piece) != color:
                continue

            legal = get_legal_moves(
                board_state,
                row,
                col
            )

            for end in legal:

                moves.append(
                    (
                        (row, col),
                        end
                    )
                )

    return moves


# ============================================================
# CHECKMATE / STALEMATE
# ============================================================

def is_checkmate(
    board_state,
    color
):

    if not is_in_check(
        board_state,
        color
    ):
        return False

    return len(
        get_all_legal_moves(
            board_state,
            color
        )
    ) == 0


def is_stalemate(
    board_state,
    color
):

    if is_in_check(
        board_state,
        color
    ):
        return False

    return len(
        get_all_legal_moves(
            board_state,
            color
        )
    ) == 0


# ============================================================
# UPDATE CASTLING RIGHTS
# ============================================================

def update_castling_rights(
    piece,
    start,
    end,
    captured_piece
):

    global castling_rights

    # White king
    if piece == "K":

        castling_rights["K"] = False
        castling_rights["Q"] = False

    # Black king
    elif piece == "k":

        castling_rights["k"] = False
        castling_rights["q"] = False

    # White rooks
    if piece == "R":

        if start == (7, 0):
            castling_rights["Q"] = False

        elif start == (7, 7):
            castling_rights["K"] = False

    # Black rooks
    if piece == "r":

        if start == (0, 0):
            castling_rights["q"] = False

        elif start == (0, 7):
            castling_rights["k"] = False

    # Rook captured
    if captured_piece == "R":

        if end == (7, 0):
            castling_rights["Q"] = False

        elif end == (7, 7):
            castling_rights["K"] = False

    elif captured_piece == "r":

        if end == (0, 0):
            castling_rights["q"] = False

        elif end == (0, 7):
            castling_rights["k"] = False


# ============================================================
# REAL MOVE
# ============================================================

def move_piece(
    start,
    end,
    promotion=None
):

    global board
    global en_passant_target

    start_row, start_col = start
    end_row, end_col = end

    piece = board[
        start_row
    ][
        start_col
    ]

    captured_piece = board[
        end_row
    ][
        end_col
    ]

    # Update castling rights
    update_castling_rights(
        piece,
        start,
        end,
        captured_piece
    )

    # --------------------------------------------------------
    # EN PASSANT TARGET
    # --------------------------------------------------------

    en_passant_target = None

    if (
        piece.lower() == "p"
        and
        abs(end_row - start_row) == 2
    ):

        en_passant_target = (
            (
                start_row + end_row
            ) // 2,
            start_col
        )

    # --------------------------------------------------------
    # MOVE
    # --------------------------------------------------------

    board = make_move_on_board(
        board,
        start,
        end,
        promotion
    )


# ============================================================
# DRAW BOARD
# ============================================================

def draw_board():

    for row in range(ROWS):

        for col in range(COLS):

            if (
                row + col
            ) % 2 == 0:

                color = LIGHT

            else:

                color = DARK

            pygame.draw.rect(
                screen,
                color,
                (
                    col * SQUARE_SIZE,
                    row * SQUARE_SIZE,
                    SQUARE_SIZE,
                    SQUARE_SIZE
                )
            )


# ============================================================
# DRAW CHECK
# ============================================================

def draw_check():

    for color in ("white", "black"):

        if is_in_check(
            board,
            color
        ):

            king_position = find_king(
                board,
                color
            )

            if king_position:

                row, col = king_position

                pygame.draw.rect(
                    screen,
                    CHECK_COLOR,
                    (
                        col * SQUARE_SIZE,
                        row * SQUARE_SIZE,
                        SQUARE_SIZE,
                        SQUARE_SIZE
                    ),
                    6
                )


# ============================================================
# DRAW PIECES
# ============================================================

def draw_pieces():

    for row in range(ROWS):

        for col in range(COLS):

            piece = board[row][col]

            if piece == "":
                continue

            image = piece_images.get(piece)

            if image is None:
                continue

            rect = image.get_rect(
                center=(
                    col * SQUARE_SIZE
                    + SQUARE_SIZE // 2,

                    row * SQUARE_SIZE
                    + SQUARE_SIZE // 2
                )
            )

            screen.blit(
                image,
                rect
            )


# ============================================================
# DRAW SELECTION
# ============================================================

def draw_selection():

    if selected_square is None:
        return

    row, col = selected_square

    pygame.draw.rect(
        screen,
        SELECTED_COLOR,
        (
            col * SQUARE_SIZE,
            row * SQUARE_SIZE,
            SQUARE_SIZE,
            SQUARE_SIZE
        ),
        5
    )


# ============================================================
# DRAW POSSIBLE MOVES
# ============================================================

def draw_possible_moves():

    if selected_square is None:
        return

    row, col = selected_square

    moves = get_legal_moves(
        board,
        row,
        col
    )

    for move_row, move_col in moves:

        center_x = (
            move_col * SQUARE_SIZE
            + SQUARE_SIZE // 2
        )

        center_y = (
            move_row * SQUARE_SIZE
            + SQUARE_SIZE // 2
        )

        # اگر خانه مهره دارد، حلقه رسم کن
        if board[move_row][move_col] != "":

            pygame.draw.circle(
                screen,
                MOVE_COLOR,
                (center_x, center_y),
                25,
                5
            )

        else:

            pygame.draw.circle(
                screen,
                MOVE_COLOR,
                (center_x, center_y),
                10
            )


# ============================================================
# DIFFICULTY SCREEN
# ============================================================

def draw_difficulty_screen():

    screen.fill(
        BACKGROUND
    )

    title_font = pygame.font.SysFont(
        "dejavusans",
        65
    )

    title = title_font.render(
        "CHESS",
        True,
        WHITE_COLOR
    )

    title_rect = title.get_rect(
        center=(
            WIDTH // 2,
            130
        )
    )

    screen.blit(
        title,
        title_rect
    )

    for name, rect in difficulty_buttons.items():

        pygame.draw.rect(
            screen,
            BUTTON_COLOR,
            rect,
            border_radius=15
        )

        text = difficulty_font.render(
            name.upper(),
            True,
            WHITE_COLOR
        )

        text_rect = text.get_rect(
            center=rect.center
        )

        screen.blit(
            text,
            text_rect
        )


# ============================================================
# GAME OVER DRAW
# ============================================================

def draw_game_over():

    if not game_over:
        return

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

    font = pygame.font.SysFont(
        "dejavusans",
        55
    )

    restart_font = pygame.font.SysFont(
        "dejavusans",
        32
    )

    text = font.render(
        game_result,
        True,
        WHITE_COLOR
    )

    rect = text.get_rect(
        center=(
            WIDTH // 2,
            HEIGHT // 2 - 40
        )
    )

    screen.blit(
        text,
        rect
    )

    restart_text = restart_font.render(
        "CLICK TO RESTART",
        True,
        WHITE_COLOR
    )

    restart_rect = restart_text.get_rect(
        center=(
            WIDTH // 2,
            HEIGHT // 2 + 40
        )
    )

    screen.blit(
        restart_text,
        restart_rect
    )


# ============================================================
# PROMOTION UI
# ============================================================

def draw_promotion():

    if not promotion_pending:
        return

    overlay = pygame.Surface(
        (WIDTH, HEIGHT),
        pygame.SRCALPHA
    )

    overlay.fill(
        (0, 0, 0, 160)
    )

    screen.blit(
        overlay,
        (0, 0)
    )

    title_font = pygame.font.SysFont(
        "dejavusans",
        40
    )

    title = title_font.render(
        "PROMOTE PAWN",
        True,
        WHITE_COLOR
    )

    title_rect = title.get_rect(
        center=(
            WIDTH // 2,
            HEIGHT // 2 - 130
        )
    )

    screen.blit(
        title,
        title_rect
    )

    pieces = [
        ("Q", "QUEEN"),
        ("R", "ROOK"),
        ("B", "BISHOP"),
        ("N", "KNIGHT")
    ]

    button_width = 150
    button_height = 100

    gap = 20

    total_width = (
        4 * button_width
        + 3 * gap
    )

    start_x = (
        WIDTH - total_width
    ) // 2

    y = HEIGHT // 2 - 60

    for index, (piece, name) in enumerate(pieces):

        x = start_x + index * (
            button_width + gap
        )

        rect = pygame.Rect(
            x,
            y,
            button_width,
            button_height
        )

        pygame.draw.rect(
            screen,
            BUTTON_COLOR,
            rect,
            border_radius=12
        )

        image = piece_images.get(
            piece
            if promotion_color == "white"
            else piece.lower()
        )

        if image:

            image_rect = image.get_rect(
                center=(
                    rect.centerx,
                    rect.centery - 10
                )
            )

            screen.blit(
                image,
                image_rect
            )

        text_font = pygame.font.SysFont(
            "dejavusans",
            20
        )

        text = text_font.render(
            name,
            True,
            WHITE_COLOR
        )

        text_rect = text.get_rect(
            center=(
                rect.centerx,
                rect.bottom - 15
            )
        )

        screen.blit(
            text,
            text_rect
        )


# ============================================================
# PROMOTION BUTTON
# ============================================================

def get_promotion_buttons():

    pieces = [
        "Q",
        "R",
        "B",
        "N"
    ]

    button_width = 150
    button_height = 100
    gap = 20

    total_width = (
        4 * button_width
        + 3 * gap
    )

    start_x = (
        WIDTH - total_width
    ) // 2

    y = HEIGHT // 2 - 60

    buttons = []

    for index, piece in enumerate(pieces):

        x = start_x + index * (
            button_width + gap
        )

        buttons.append(
            (
                piece,
                pygame.Rect(
                    x,
                    y,
                    button_width,
                    button_height
                )
            )
        )

    return buttons


# ============================================================
# AI EVALUATION
# ============================================================

def evaluate_board(board_state):

    score = 0

    for row in range(8):

        for col in range(8):

            piece = board_state[row][col]

            if piece == "":
                continue

            value = PIECE_VALUES[
                piece.lower()
            ]

            if piece.islower():

                score += value

            else:

                score -= value

    return score


# ============================================================
# MOVE ORDERING
# ============================================================

def move_score(
    board_state,
    move
):

    start, end = move

    target = board_state[
        end[0]
    ][
        end[1]
    ]

    if target == "":
        return 0

    return PIECE_VALUES.get(
        target.lower(),
        0
    )


# ============================================================
# MINIMAX
# ============================================================

def minimax(
    board_state,
    depth,
    alpha,
    beta,
    maximizing
):

    black_moves = get_all_legal_moves(
        board_state,
        "black"
    )

    white_moves = get_all_legal_moves(
        board_state,
        "white"
    )

    # Black checkmate
    if is_checkmate(
        board_state,
        "white"
    ):

        return 1000000 + depth, None

    # White checkmate
    if is_checkmate(
        board_state,
        "black"
    ):

        return -1000000 - depth, None

    # Stalemate
    if (
        not black_moves
        and
        not white_moves
    ):

        return 0, None

    if depth == 0:

        return (
            evaluate_board(board_state),
            None
        )

    if maximizing:

        best_score = -float("inf")
        best_move = None

        moves = black_moves

        moves.sort(
            key=lambda m: move_score(
                board_state,
                m
            ),
            reverse=True
        )

        for start, end in moves:

            new_board = make_move_on_board(
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
                best_move = (
                    start,
                    end
                )

            alpha = max(
                alpha,
                best_score
            )

            if beta <= alpha:
                break

        return (
            best_score,
            best_move
        )

    else:

        best_score = float("inf")
        best_move = None

        moves = white_moves

        moves.sort(
            key=lambda m: move_score(
                board_state,
                m
            ),
            reverse=True
        )

        for start, end in moves:

            new_board = make_move_on_board(
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
                best_move = (
                    start,
                    end
                )

            beta = min(
                beta,
                best_score
            )

            if beta <= alpha:
                break

        return (
            best_score,
            best_move
        )


# ============================================================
# BOT MOVE
# ============================================================

def make_bot_move():

    global turn
    global game_over
    global game_result

    if game_over:
        return

    if turn != "black":
        return

    depth = AI_DEPTH.get(
        difficulty,
        1
    )

    _, best_move = minimax(
        board,
        depth,
        -float("inf"),
        float("inf"),
        True
    )

    if best_move is None:

        if is_in_check(
            board,
            "black"
        ):

            game_over = True
            game_result = "YOU WIN - CHECKMATE"

        else:

            game_over = True
            game_result = "DRAW - STALEMATE"

        return

    start, end = best_move

    piece = board[
        start[0]
    ][
        start[1]
    ]

    # Bot promotion
    promotion = None

    if (
        piece == "p"
        and
        end[0] == 7
    ):

        promotion = "q"

    move_piece(
        start,
        end,
        promotion
    )

    turn = "white"

    check_game_status()


# ============================================================
# GAME STATUS
# ============================================================

def check_game_status():

    global game_over
    global game_result

    current_color = turn

    legal_moves = get_all_legal_moves(
        board,
        current_color
    )

    if len(legal_moves) == 0:

        game_over = True

        if is_in_check(
            board,
            current_color
        ):

            if current_color == "white":

                game_result = (
                    "YOU LOST - CHECKMATE"
                )

            else:

                game_result = (
                    "YOU WIN - CHECKMATE"
                )

        else:

            game_result = (
                "DRAW - STALEMATE"
            )


# ============================================================
# PLAYER MOVE
# ============================================================

def player_move(
    start,
    end
):

    global turn
    global promotion_pending
    global promotion_square
    global promotion_color

    piece = board[
        start[0]
    ][
        start[1]
    ]

    # Promotion
    if (
        piece == "P"
        and
        end[0] == 0
    ):

        promotion_pending = True
        promotion_square = (
            start,
            end
        )
        promotion_color = "white"

        return

    move_piece(
        start,
        end
    )

    turn = "black"

    check_game_status()

    if not game_over:

        make_bot_move()


# ============================================================
# PROMOTION SELECT
# ============================================================

def select_promotion(
    piece
):

    global promotion_pending
    global promotion_square
    global promotion_color
    global turn

    if not promotion_pending:
        return

    start, end = promotion_square

    move_piece(
        start,
        end,
        piece
    )

    promotion_pending = False
    promotion_square = None
    promotion_color = None

    turn = "black"

    check_game_status()

    if not game_over:

        make_bot_move()


# ============================================================
# CHESS DRAW
# ============================================================

def draw_chess():

    draw_board()

    draw_possible_moves()

    draw_selection()

    draw_check()

    draw_pieces()

    draw_promotion()

    draw_game_over()
























# ============================================================
# MAIN DRAW FUNCTION
# ============================================================

def CHESS_():

    if screen is None:
        return

    if game_state == "difficulty":

        draw_difficulty_screen()

    elif game_state == "chess":

        draw_chess()





























# ============================================================
# EVENT HANDLER
# ============================================================

def event_CHESS(event):

    global game_state
    global difficulty
    global selected_square

    global promotion_pending

    global game_over

    if event.type != pygame.MOUSEBUTTONDOWN:
        return

    mouse_x, mouse_y = event.pos

    # ========================================================
    # DIFFICULTY
    # ========================================================

    if game_state == "difficulty":

        for name, rect in difficulty_buttons.items():

            if rect.collidepoint(
                mouse_x,
                mouse_y
            ):

                difficulty = name

                reset_chess()

                game_state = "chess"

                return

    # ========================================================
    # GAME OVER
    # ========================================================

    if game_state == "chess":

        if game_over:

            reset_chess()

            return

    # ========================================================
    # PROMOTION
    # ========================================================

    if promotion_pending:

        for piece, rect in get_promotion_buttons():

            if rect.collidepoint(
                mouse_x,
                mouse_y
            ):

                select_promotion(
                    piece
                )

                return

        return

    # ========================================================
    # ONLY PLAYER WHITE
    # ========================================================

    if turn != "white":
        return

    # ========================================================
    # BOARD POSITION
    # ========================================================

    col = mouse_x // SQUARE_SIZE
    row = mouse_y // SQUARE_SIZE

    if not inside_board(
        row,
        col
    ):
        return

    clicked_piece = board[row][col]

    # ========================================================
    # NOTHING SELECTED
    # ========================================================

    if selected_square is None:

        if (
            clicked_piece != ""
            and
            is_white(clicked_piece)
        ):

            selected_square = (
                row,
                col
            )

        return

    # ========================================================
    # SELECTED
    # ========================================================

    start = selected_square

    possible_moves = get_legal_moves(
        board,
        start[0],
        start[1]
    )

    # ========================================================
    # LEGAL MOVE
    # ========================================================

    if (
        row,
        col
    ) in possible_moves:

        selected_square = None

        player_move(
            start,
            (row, col)
        )

        return

    # ========================================================
    # SELECT ANOTHER WHITE PIECE
    # ========================================================

    if (
        clicked_piece != ""
        and
        is_white(clicked_piece)
    ):

        selected_square = (
            row,
            col
        )

        return

    # ========================================================
    # EMPTY / INVALID
    # ========================================================

    selected_square = None
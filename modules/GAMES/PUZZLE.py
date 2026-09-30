import pygame
import random
import os
import sys

from modules.font import *

WIDTH = 1080
HEIGHT = 720
screen = None


def WIDTH_HEIGHT_gettter(screen_, WIDTH_, HEIGHT_):

    global WIDTH
    global HEIGHT
    global screen

    WIDTH = WIDTH_
    WIDTH1 = WIDTH_
    HEIGHT = HEIGHT_
    HEIGHT1 = HEIGHT_
    screen = screen_

# =========================================================
# IMAGE
# =========================================================

IMAGE_FOLDER = (
    "/Users/mac/Desktop/app/asset/image/PUZZLE"
)


# =========================================================
# LEVELS
# =========================================================

LEVELS = {

    "EASY": {
        "pieces": 10,
    },

    "MEDIUM": {
        "pieces": 50,
    },

    "HARD": {
        "pieces": 100,
    }

}


# =========================================================
# COLORS
# =========================================================

BACKGROUND = (
    24,
    27,
    33
)

WHITE = (
    240,
    240,
    240
)

GRAY = (
    150,
    155,
    165
)

DARK_GRAY = (
    70,
    75,
    85
)

GREEN = (
    70,
    220,
    120
)

RED = (
    220,
    80,
    80
)

YELLOW = (
    235,
    190,
    70
)

BLUE = (
    80,
    150,
    230
)

BORDER = (
    55,
    60,
    70
)

TRAY_COLOR = (
    30,
    34,
    42
)

TRAY_BORDER = (
    65,
    70,
    80
)

SHADOW = (
    10,
    12,
    16
)


# =========================================================
# FONTS
# =========================================================

# font_title = pygame.font.Font(
#     None,
#     48
# )

# font_big = pygame.font.Font(
#     None,
#     38
# )

# font_medium = pygame.font.Font(
#     None,
#     28
# )

# font_small = pygame.font.Font(
#     None,
#     22
# )

# font_tiny = pygame.font.Font(
#     None,
#     18
# )


# =========================================================
# LAYOUT
# =========================================================

TOP_MARGIN = 65

TRAY_HEIGHT = 145

BOTTOM_MARGIN = 10

SIDE_MARGIN = 20


# =========================================================
# PUZZLE SIZE
#
# پازل به اندازه صفحه بستگی دارد.
# =========================================================

PUZZLE_SIZE = min(
    WIDTH - SIDE_MARGIN * 2,
    HEIGHT
    - TOP_MARGIN
    - TRAY_HEIGHT
    - BOTTOM_MARGIN
)

PUZZLE_X = (
    WIDTH - PUZZLE_SIZE
) // 2

PUZZLE_Y = TOP_MARGIN


# =========================================================
# TRAY
# =========================================================

TRAY_Y = (
    HEIGHT
    - TRAY_HEIGHT
)

TRAY_PADDING = 18

TRAY_TOP = TRAY_Y + 25

TRAY_BOTTOM = (
    HEIGHT - 12
)


# =========================================================
# PIECE SETTINGS
# =========================================================

SNAP_DISTANCE = 24

PREVIEW_MAX_SIZE = 75

PREVIEW_GAP = 18


# =========================================================
# SCROLL
# =========================================================

tray_scroll_x = 0

tray_content_width = 0

scroll_speed = 80

scroll_dragging = False

scroll_drag_start_x = 0

scroll_drag_start_value = 0


# =========================================================
# GAME STATE
# =========================================================

GAME_LEVEL_SELECT = "LEVEL_SELECT"

GAME_PLAYING = "PLAYING"

GAME_FINISHED = "FINISHED"

game_state = GAME_LEVEL_SELECT

selected_level = None


# =========================================================
# GAME VARIABLES
# =========================================================

puzzle_image = None

pieces = []

dragging_piece = None

drag_offset_x = 0

drag_offset_y = 0

finished = False

start_time = 0

finish_time = 0


# =========================================================
# IMAGE FILES
# =========================================================

def get_image_files(folder):

    if not os.path.isdir(folder):

        print(
            "Image folder does not exist:"
        )

        print(folder)

        return []

    valid_extensions = (
        ".png",
        ".jpg",
        ".jpeg",
        ".webp",
        ".bmp"
    )

    files = []

    for filename in os.listdir(folder):

        if filename.lower().endswith(
            valid_extensions
        ):

            path = os.path.join(
                folder,
                filename
            )

            if os.path.isfile(path):

                files.append(
                    path
                )

    return files


# =========================================================
# LOAD IMAGE
# =========================================================

def load_random_image():

    files = get_image_files(
        IMAGE_FOLDER
    )

    if not files:

        return None

    path = random.choice(
        files
    )

    print(
        "Puzzle image:",
        path
    )

    try:

        image = pygame.image.load(
            path
        ).convert()

    except pygame.error as error:

        print(
            "Image error:",
            error
        )

        return None

    image = pygame.transform.smoothscale(
        image,
        (
            PUZZLE_SIZE,
            PUZZLE_SIZE
        )
    )

    return image


# =========================================================
# RECTANGLE ASPECT RATIO
#
# حداکثر نسبت طول به عرض:
#
# 2 : 1
#
# یعنی یک مستطیل نهایتاً تقریباً اندازه
# دو مربع کنار هم است.
# =========================================================

def valid_rect(rect):

    if rect.width <= 0:
        return False

    if rect.height <= 0:
        return False

    ratio = max(
        rect.width / rect.height,
        rect.height / rect.width
    )

    return ratio <= 2.05


# =========================================================
# CAN SPLIT
# =========================================================

def can_split(rect):

    # حداقل اندازه‌ای که یک قطعه می‌تواند داشته باشد
    min_size = max(
        28,
        int(PUZZLE_SIZE / 14)
    )

    if rect.width >= min_size * 2:

        return True

    if rect.height >= min_size * 2:

        return True

    return False


# =========================================================
# SPLIT RECTANGLE
# =========================================================

def split_rectangle(rect):

    min_size = max(
        28,
        int(PUZZLE_SIZE / 14)
    )

    candidates = []

    # -----------------------------------------------------
    # Vertical
    # -----------------------------------------------------

    if rect.width >= min_size * 2:

        candidates.append(
            "vertical"
        )

    # -----------------------------------------------------
    # Horizontal
    # -----------------------------------------------------

    if rect.height >= min_size * 2:

        candidates.append(
            "horizontal"
        )

    if not candidates:

        return None

    # -----------------------------------------------------
    # جهت مناسب بر اساس طولانی‌تر بودن مستطیل
    # -----------------------------------------------------

    if rect.width > rect.height * 1.15:

        direction = "vertical"

    elif rect.height > rect.width * 1.15:

        direction = "horizontal"

    else:

        direction = random.choice(
            candidates
        )

    # -----------------------------------------------------
    # VERTICAL
    # -----------------------------------------------------

    if direction == "vertical":

        low = min_size

        high = (
            rect.width
            - min_size
        )

        if high <= low:

            return None

        # بیشتر اوقات نزدیک وسط
        ratio = random.uniform(
            0.42,
            0.58
        )

        split = int(
            rect.width * ratio
        )

        split = max(
            low,
            min(
                split,
                high
            )
        )

        rect1 = pygame.Rect(
            rect.x,
            rect.y,
            split,
            rect.height
        )

        rect2 = pygame.Rect(
            rect.x + split,
            rect.y,
            rect.width - split,
            rect.height
        )

    # -----------------------------------------------------
    # HORIZONTAL
    # -----------------------------------------------------

    else:

        low = min_size

        high = (
            rect.height
            - min_size
        )

        if high <= low:

            return None

        ratio = random.uniform(
            0.42,
            0.58
        )

        split = int(
            rect.height * ratio
        )

        split = max(
            low,
            min(
                split,
                high
            )
        )

        rect1 = pygame.Rect(
            rect.x,
            rect.y,
            rect.width,
            split
        )

        rect2 = pygame.Rect(
            rect.x,
            rect.y + split,
            rect.width,
            rect.height - split
        )

    # -----------------------------------------------------
    # بررسی نسبت
    # -----------------------------------------------------

    if not valid_rect(rect1):

        return None

    if not valid_rect(rect2):

        return None

    return (
        rect1,
        rect2
    )


# =========================================================
# GENERATE PARTITION
#
# این مهم‌ترین قسمت پازل است.
#
# هیچ GAP یا OVERLAP ایجاد نمی‌شود.
#
# کل تصویر به صورت دقیق تقسیم می‌شود.
# =========================================================

def generate_partition(
    target_count
):

    pieces_rects = [

        pygame.Rect(
            0,
            0,
            PUZZLE_SIZE,
            PUZZLE_SIZE
        )

    ]

    attempts = 0

    max_attempts = (
        target_count * 100
    )

    while (
        len(pieces_rects)
        < target_count
        and attempts < max_attempts
    ):

        attempts += 1

        # -------------------------------------------------
        # قابل تقسیم‌ها
        # -------------------------------------------------

        candidates = []

        for index, rect in enumerate(
            pieces_rects
        ):

            if can_split(rect):

                candidates.append(
                    index
                )

        if not candidates:

            break

        # -------------------------------------------------
        # بهتر است مستطیل‌های بزرگ‌تر
        # زودتر تقسیم شوند.
        # -------------------------------------------------

        candidates.sort(
            key=lambda index:
                pieces_rects[index].width
                * pieces_rects[index].height,
            reverse=True
        )

        # کمی randomness
        top_count = min(
            5,
            len(candidates)
        )

        index = random.choice(
            candidates[:top_count]
        )

        rect = pieces_rects[
            index
        ]

        result = split_rectangle(
            rect
        )

        if result is None:

            continue

        rect1, rect2 = result

        pieces_rects.pop(
            index
        )

        pieces_rects.append(
            rect1
        )

        pieces_rects.append(
            rect2
        )

    # -----------------------------------------------------
    # اگر به تعداد دقیق نرسیدیم
    # دوباره تلاش می‌کنیم.
    # -----------------------------------------------------

    if len(pieces_rects) != target_count:

        return generate_partition(
            target_count
        )

    return pieces_rects


# =========================================================
# CREATE PIECE IMAGE
# =========================================================

def create_piece_image(
    image,
    source_rect
):

    piece = pygame.Surface(
        (
            source_rect.width,
            source_rect.height
        ),
        pygame.SRCALPHA
    )

    piece.blit(
        image,
        (
            0,
            0
        ),
        source_rect
    )

    return piece


# =========================================================
# CREATE PREVIEW
# =========================================================

def create_preview(
    image
):

    width = image.get_width()

    height = image.get_height()

    scale = min(
        PREVIEW_MAX_SIZE / width,
        PREVIEW_MAX_SIZE / height
    )

    preview_width = max(
        16,
        int(
            width * scale
        )
    )

    preview_height = max(
        16,
        int(
            height * scale
        )
    )

    return pygame.transform.smoothscale(
        image,
        (
            preview_width,
            preview_height
        )
    )


# =========================================================
# CREATE PIECES
# =========================================================

def create_pieces(
    image,
    count
):

    layout = generate_partition(
        count
    )

    result = []

    for index, target in enumerate(
        layout
    ):

        piece_image = create_piece_image(
            image,
            target
        )

        preview = create_preview(
            piece_image
        )

        piece = {

            # ---------------------------------------------
            # IMAGE
            # ---------------------------------------------

            "image": piece_image,

            "preview": preview,

            # ---------------------------------------------
            # TARGET
            # ---------------------------------------------

            "target_x":
                PUZZLE_X + target.x,

            "target_y":
                PUZZLE_Y + target.y,

            "target_width":
                target.width,

            "target_height":
                target.height,

            # ---------------------------------------------
            # CURRENT
            # ---------------------------------------------

            "x": 0,

            "y": 0,

            # ---------------------------------------------
            # STATE
            # ---------------------------------------------

            "placed": False,

            "dragging": False,

            # ---------------------------------------------
            # ID
            # ---------------------------------------------

            "id": index,

            # ---------------------------------------------
            # TRAY
            # ---------------------------------------------

            "tray_x": 0,

            "tray_y": 0,

            "tray_rect": None
        }

        result.append(
            piece
        )

    return result


# =========================================================
# PLACE PIECES IN HORIZONTAL TRAY
#
# همه قطعات فقط یک ردیف دارند.
#
# برای 100 قطعه:
#
# [1][2][3][4][5]...[100]
#
# و با Scroll حرکت می‌کنند.
# =========================================================

def place_pieces_in_tray():

    global tray_content_width
    global tray_scroll_x

    shuffled = pieces.copy()

    random.shuffle(
        shuffled
    )

    x = TRAY_PADDING

    center_y = (
        TRAY_Y
        + TRAY_HEIGHT // 2
        + 8
    )

    for piece in shuffled:

        preview = piece[
            "preview"
        ]

        width = preview.get_width()

        height = preview.get_height()

        y = int(
            center_y
            - height / 2
        )

        piece[
            "tray_x"
        ] = x

        piece[
            "tray_y"
        ] = y

        piece[
            "tray_rect"
        ] = pygame.Rect(
            x,
            y,
            width,
            height
        )

        # current
        piece["x"] = x

        piece["y"] = y

        x += (
            width
            + PREVIEW_GAP
        )

    tray_content_width = (
        x
        + TRAY_PADDING
    )

    tray_scroll_x = 0


# =========================================================
# MAX SCROLL
# =========================================================

def get_max_scroll():

    visible_width = (
        WIDTH
        - TRAY_PADDING * 2
    )

    return max(
        0,
        tray_content_width
        - visible_width
    )


# =========================================================
# SET SCROLL
# =========================================================

def set_tray_scroll(
    value
):

    global tray_scroll_x

    maximum = get_max_scroll()

    tray_scroll_x = max(
        0,
        min(
            int(value),
            maximum
        )
    )


# =========================================================
# DRAW TRAY
# =========================================================

def draw_tray():

    # -----------------------------------------------------
    # Tray background
    # -----------------------------------------------------

    tray_rect = pygame.Rect(
        0,
        TRAY_Y,
        WIDTH,
        TRAY_HEIGHT
    )

    pygame.draw.rect(
        screen,
        TRAY_COLOR,
        tray_rect
    )

    pygame.draw.line(
        screen,
        TRAY_BORDER,
        (
            0,
            TRAY_Y
        ),
        (
            WIDTH,
            TRAY_Y
        ),
        2
    )

    # -----------------------------------------------------
    # Title
    # -----------------------------------------------------

    title = fonts["heart"].render(
        f"{selected_level}  •  PIECES",
        True,
        GRAY
    )

    screen.blit(
        title,
        (
            15,
            TRAY_Y + 7
        )
    )

    # -----------------------------------------------------
    # Clip
    #
    # قطعات نمی‌توانند بیرون نوار رسم شوند.
    # -----------------------------------------------------

    old_clip = screen.get_clip()

    piece_area = pygame.Rect(
        0,
        TRAY_Y + 30,
        WIDTH,
        TRAY_HEIGHT - 30
    )

    screen.set_clip(
        piece_area
    )

    # -----------------------------------------------------
    # Pieces
    # -----------------------------------------------------

    for piece in pieces:

        if piece["placed"]:

            continue

        if piece["dragging"]:

            continue

        preview = piece[
            "preview"
        ]

        x = (
            piece["tray_x"]
            - tray_scroll_x
        )

        y = piece[
            "tray_y"
        ]

        rect = pygame.Rect(
            x,
            y,
            preview.get_width(),
            preview.get_height()
        )

        # Shadow

        shadow_rect = rect.move(
            3,
            3
        )

        pygame.draw.rect(
            screen,
            SHADOW,
            shadow_rect,
            border_radius=4
        )

        screen.blit(
            preview,
            rect
        )

        pygame.draw.rect(
            screen,
            BORDER,
            rect,
            2,
            border_radius=4
        )

    screen.set_clip(
        old_clip
    )

    # -----------------------------------------------------
    # Scroll arrows
    # -----------------------------------------------------

    max_scroll = get_max_scroll()

    if max_scroll > 0:

        # LEFT

        left_rect = pygame.Rect(
            8,
            TRAY_Y + 55,
            38,
            50
        )

        pygame.draw.rect(
            screen,
            (45, 49, 58),
            left_rect,
            border_radius=8
        )

        pygame.draw.polygon(
            screen,
            WHITE,
            [
                (
                    left_rect.x + 25,
                    left_rect.centery - 10
                ),
                (
                    left_rect.x + 14,
                    left_rect.centery
                ),
                (
                    left_rect.x + 25,
                    left_rect.centery + 10
                )
            ]
        )

        # RIGHT

        right_rect = pygame.Rect(
            WIDTH - 46,
            TRAY_Y + 55,
            38,
            50
        )

        pygame.draw.rect(
            screen,
            (45, 49, 58),
            right_rect,
            border_radius=8
        )

        pygame.draw.polygon(
            screen,
            WHITE,
            [
                (
                    right_rect.x + 13,
                    right_rect.centery - 10
                ),
                (
                    right_rect.x + 24,
                    right_rect.centery
                ),
                (
                    right_rect.x + 13,
                    right_rect.centery + 10
                )
            ]
        )

    # -----------------------------------------------------
    # Scroll bar
    # -----------------------------------------------------

    if max_scroll > 0:

        bar_width = WIDTH - 120

        bar_x = 60

        bar_y = HEIGHT - 9

        pygame.draw.rect(
            screen,
            (50, 54, 63),
            (
                bar_x,
                bar_y,
                bar_width,
                5
            ),
            border_radius=3
        )

        visible_width = WIDTH

        ratio = (
            visible_width
            / tray_content_width
        )

        thumb_width = max(
            40,
            int(
                bar_width * ratio
            )
        )

        scroll_ratio = (
            tray_scroll_x
            / max_scroll
        )

        thumb_x = (
            bar_x
            + int(
                (
                    bar_width
                    - thumb_width
                )
                * scroll_ratio
            )
        )

        pygame.draw.rect(
            screen,
            GRAY,
            (
                thumb_x,
                bar_y,
                thumb_width,
                5
            ),
            border_radius=3
        )


def draw_piece_borders(pieces):

    for piece in pieces:

        # target_x و target_y همین الان مختصات واقعی صفحه هستند
        x = piece["target_x"]
        y = piece["target_y"]

        width = piece["target_width"]
        height = piece["target_height"]

        rect = pygame.Rect(
            x,
            y,
            width,
            height
        )

        pygame.draw.rect(
            screen,
            (220, 220, 220),
            rect,
            1
        )
        
# =========================================================
# DRAW BOARD
# =========================================================

def draw_board():

    board_rect = pygame.Rect(
        PUZZLE_X,
        PUZZLE_Y,
        PUZZLE_SIZE,
        PUZZLE_SIZE
    )

    # =====================================================
    # SHADOW
    # =====================================================

    pygame.draw.rect(
        screen,
        SHADOW,
        board_rect.move(
            6,
            6
        ),
        border_radius=8
    )

    # =====================================================
    # WHITE PUZZLE BOARD
    #
    # اینجا دیگر عکس اصلی نمایش داده نمی‌شود.
    # =====================================================

    pygame.draw.rect(
        screen,
        WHITE,
        board_rect,
        border_radius=8
    )







    draw_piece_borders(pieces)
    # =====================================================
    # BORDER
    # =====================================================

    pygame.draw.rect(
        screen,
        BORDER,
        board_rect,
        3,
        border_radius=8
    )














def draw_image_preview():

    if puzzle_image is None:
        return

    # =====================================================
    # PREVIEW SIZE
    # =====================================================

    preview_size = 150

    preview = pygame.transform.smoothscale(
        puzzle_image,
        (
            preview_size,
            preview_size
        )
    )

    # =====================================================
    # POSITION
    #
    # سمت راست صفحه
    # =====================================================

    x = (
        PUZZLE_X
        + PUZZLE_SIZE
        + 25
    )

    y = PUZZLE_Y

    # اگر سمت راست جا نداشت،
    # سمت چپ قرار بگیرد.

    if x + preview_size > WIDTH - 15:

        x = (
            PUZZLE_X
            - preview_size
            - 25
        )

    # =====================================================
    # BACKGROUND
    # =====================================================

    background_rect = pygame.Rect(
        x - 8,
        y - 8,
        preview_size + 16,
        preview_size + 16
    )

    pygame.draw.rect(
        screen,
        TRAY_COLOR,
        background_rect,
        border_radius=10
    )

    pygame.draw.rect(
        screen,
        TRAY_BORDER,
        background_rect,
        2,
        border_radius=10
    )

    # =====================================================
    # IMAGE
    # =====================================================

    screen.blit(
        preview,
        (
            x,
            y
        )
    )

    # =====================================================
    # LABEL
    # =====================================================

    text = fonts["heart"].render(
        "PREVIEW",
        True,
        GRAY
    )

    text_rect = text.get_rect(
        center=(
            x + preview_size // 2,
            y + preview_size + 18
        )
    )

    screen.blit(
        text,
        text_rect
    )
    
    
    
    
    
    
    
    
# =========================================================
# DRAW PIECES
# =========================================================

def draw_pieces():

    # -----------------------------------------------------
    # اول placed pieces
    # -----------------------------------------------------

    for piece in pieces:

        if not piece["placed"]:

            continue

        screen.blit(
            piece["image"],
            (
                int(piece["x"]),
                int(piece["y"])
            )
        )

        pygame.draw.rect(
            screen,
            (
                70,
                90,
                75
            ),
            (
                int(piece["x"]),
                int(piece["y"]),
                piece["target_width"],
                piece["target_height"]
            ),
            1
        )

    # -----------------------------------------------------
    # Dragging piece
    #
    # باید روی همه چیز باشد.
    # -----------------------------------------------------

    if dragging_piece is not None:

        piece = dragging_piece

        image = piece[
            "image"
        ]

        x = int(
            piece["x"]
        )

        y = int(
            piece["y"]
        )

        # Shadow

        shadow = pygame.Surface(
            image.get_size(),
            pygame.SRCALPHA
        )

        shadow.fill(
            (
                0,
                0,
                0,
                80
            )
        )

        screen.blit(
            shadow,
            (
                x + 7,
                y + 7
            )
        )

        screen.blit(
            image,
            (
                x,
                y
            )
        )

        pygame.draw.rect(
            screen,
            WHITE,
            (
                x,
                y,
                piece["target_width"],
                piece["target_height"]
            ),
            2
        )


# =========================================================
# GET PIECE TRAY RECT
# =========================================================

def get_piece_tray_rect(
    piece
):

    preview = piece[
        "preview"
    ]

    return pygame.Rect(
        piece["tray_x"]
        - tray_scroll_x,

        piece["tray_y"],

        preview.get_width(),

        preview.get_height()
    )


# =========================================================
# CHECK PIECE
# =========================================================

def check_piece(
    piece
):

    target_x = piece[
        "target_x"
    ]

    target_y = piece[
        "target_y"
    ]

    dx = (
        piece["x"]
        - target_x
    )

    dy = (
        piece["y"]
        - target_y
    )

    distance = (
        dx * dx
        + dy * dy
    ) ** 0.5

    if distance <= SNAP_DISTANCE:

        piece["x"] = target_x

        piece["y"] = target_y

        piece["placed"] = True

        piece["dragging"] = False

        return True

    # -----------------------------------------------------
    # اشتباه بود
    #
    # برگرد به Tray
    # -----------------------------------------------------

    piece["dragging"] = False

    piece["x"] = (
        piece["tray_x"]
        - tray_scroll_x
    )

    piece["y"] = (
        piece["tray_y"]
    )

    return False


# =========================================================
# CHECK FINISHED
# =========================================================

def check_finished():

    for piece in pieces:

        if not piece["placed"]:

            return False

    return True


# =========================================================
# RESET GAME
# =========================================================

def reset_game():

    global puzzle_image
    global pieces
    global dragging_piece
    global finished
    global start_time
    global finish_time

    count = LEVELS[
        selected_level
    ][
        "pieces"
    ]

    puzzle_image = load_random_image()

    if puzzle_image is None:

        pieces = []

        return

    pieces = create_pieces(
        puzzle_image,
        count
    )

    place_pieces_in_tray()

    dragging_piece = None

    finished = False

    start_time = (
        pygame.time.get_ticks()
    )

    finish_time = 0


# =========================================================
# LEVEL BUTTONS
# =========================================================

def get_level_buttons():

    button_width = 250

    button_height = 180

    gap = 35

    total_width = (
        button_width * 3
        + gap * 2
    )

    start_x = (
        WIDTH - total_width
    ) // 2

    y = (
        HEIGHT - button_height
    ) // 2

    buttons = {}

    levels = [
        (
            "EASY",
            GREEN,
            "10 PIECES"
        ),
        (
            "MEDIUM",
            YELLOW,
            "50 PIECES"
        ),
        (
            "HARD",
            RED,
            "100 PIECES"
        )
    ]

    for i, data in enumerate(
        levels
    ):

        name, color, subtitle = data

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

        buttons[name] = (
            rect,
            color,
            subtitle
        )

    return buttons


# =========================================================
# DRAW LEVEL SELECT
# =========================================================

def draw_level_select():

    screen.fill(
        BACKGROUND
    )

    # -----------------------------------------------------
    # Title
    # -----------------------------------------------------

    title = fonts["heart"].render(
        "PUZZLE",
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

    subtitle = fonts["heart"].render(
        "SELECT DIFFICULTY",
        True,
        GRAY
    )

    subtitle_rect = subtitle.get_rect(
        center=(
            WIDTH // 2,
            165
        )
    )

    screen.blit(
        subtitle,
        subtitle_rect
    )

    # -----------------------------------------------------
    # Buttons
    # -----------------------------------------------------

    buttons = get_level_buttons()

    mouse_pos = pygame.mouse.get_pos()

    for name, data in buttons.items():

        rect, color, text = data

        hovered = rect.collidepoint(
            mouse_pos
        )

        draw_rect = rect.copy()

        if hovered:

            draw_rect.inflate_ip(
                8,
                8
            )

        # Shadow

        pygame.draw.rect(
            screen,
            SHADOW,
            draw_rect.move(
                5,
                6
            ),
            border_radius=16
        )

        # Button

        button_color = color

        if hovered:

            button_color = tuple(
                min(
                    255,
                    c + 20
                )
                for c in color
            )

        pygame.draw.rect(
            screen,
            button_color,
            draw_rect,
            border_radius=16
        )

        # -------------------------------------------------
        # Name
        # -------------------------------------------------

        name_text = fonts["heart"].render(
            name,
            True,
            BACKGROUND
        )

        name_rect = name_text.get_rect(
            center=(
                draw_rect.centerx,
                draw_rect.centery - 20
            )
        )

        screen.blit(
            name_text,
            name_rect
        )

        # -------------------------------------------------
        # Pieces
        # -------------------------------------------------

        piece_text = fonts["heart"].render(
            text,
            True,
            BACKGROUND
        )

        piece_rect = piece_text.get_rect(
            center=(
                draw_rect.centerx,
                draw_rect.centery + 30
            )
        )

        screen.blit(
            piece_text,
            piece_rect
        )

    # -----------------------------------------------------
    # Help
    # -----------------------------------------------------

    help_text = fonts["heart"].render(
        "Choose a difficulty",
        True,
        GRAY
    )

    help_rect = help_text.get_rect(
        center=(
            WIDTH // 2,
            HEIGHT - 45
        )
    )

    screen.blit(
        help_text,
        help_rect
    )


# =========================================================
# DRAW GAME UI
# =========================================================

def draw_game_ui():

    # -----------------------------------------------------
    # Title
    # -----------------------------------------------------

    title = fonts["heart"].render(
        f"{selected_level}  •  PUZZLE",
        True,
        WHITE
    )

    title_rect = title.get_rect(
        center=(
            WIDTH // 2,
            30
        )
    )

    screen.blit(
        title,
        title_rect
    )

    # -----------------------------------------------------
    # Timer
    # -----------------------------------------------------

    if finished:

        elapsed = (
            finish_time // 1000
        )

    else:

        elapsed = (
            pygame.time.get_ticks()
            - start_time
        ) // 1000

    timer = fonts["heart"].render(
        f"{elapsed}s",
        True,
        WHITE
    )

    screen.blit(
        timer,
        (
            20,
            22
        )
    )

    # -----------------------------------------------------
    # Piece count
    # -----------------------------------------------------

    placed_count = sum(
        1
        for piece in pieces
        if piece["placed"]
    )

    total_count = len(
        pieces
    )

    counter = fonts["heart"].render(
        f"{placed_count}/{total_count}",
        True,
        WHITE
    )

    counter_rect = counter.get_rect(
        top=
        22,
        right=
        WIDTH - 20
    )

    screen.blit(
        counter,
        counter_rect
    )


# =========================================================
# DRAW WIN
# =========================================================

def draw_win():

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
            180
        )
    )

    screen.blit(
        overlay,
        (
            0,
            0
        )
    )

    title = fonts["heart"].render(
        "PUZZLE COMPLETE!",
        True,
        GREEN
    )

    title_rect = title.get_rect(
        center=(
            WIDTH // 2,
            HEIGHT // 2 - 40
        )
    )

    screen.blit(
        title,
        title_rect
    )

    seconds = (
        finish_time // 1000
    )

    time_text = fonts["heart"].render(
        f"TIME  {seconds}s",
        True,
        WHITE
    )

    time_rect = time_text.get_rect(
        center=(
            WIDTH // 2,
            HEIGHT // 2 + 20
        )
    )

    screen.blit(
        time_text,
        time_rect
    )

    help_text = fonts["heart"].render(
        "R = New Puzzle     ESC = Back",
        True,
        GRAY
    )

    help_rect = help_text.get_rect(
        center=(
            WIDTH // 2,
            HEIGHT // 2 + 70
        )
    )

    screen.blit(
        help_text,
        help_rect
    )


# =========================================================
# START LEVEL
# =========================================================

def start_level(
    level
):

    global selected_level
    global game_state

    selected_level = level

    game_state = GAME_PLAYING

    reset_game()


# =========================================================
# LEVEL SELECT EVENT
# =========================================================

def handle_level_select_event(
    event
):

    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_ESCAPE:

            pygame.quit()

            sys.exit()

    if event.type == pygame.MOUSEBUTTONDOWN:

        if event.button == 1:

            buttons = get_level_buttons()

            for name, data in buttons.items():

                rect, color, subtitle = data

                if rect.collidepoint(
                    event.pos
                ):

                    start_level(
                        name
                    )

                    return


# =========================================================
# START DRAG
# =========================================================

def start_drag(
    event
):

    global dragging_piece
    global drag_offset_x
    global drag_offset_y

    mouse_x, mouse_y = event.pos

    # -----------------------------------------------------
    # از آخر به اول
    # -----------------------------------------------------

    for piece in reversed(
        pieces
    ):

        if piece["placed"]:

            continue

        rect = get_piece_tray_rect(
            piece
        )

        if rect.collidepoint(
            mouse_x,
            mouse_y
        ):

            dragging_piece = piece

            piece["dragging"] = True

            # -------------------------------------------------
            # مرکز قطعه واقعی زیر موس
            # -------------------------------------------------

            piece["x"] = (
                mouse_x
                - piece["target_width"] // 2
            )

            piece["y"] = (
                mouse_y
                - piece["target_height"] // 2
            )

            drag_offset_x = (
                piece["target_width"] // 2
            )

            drag_offset_y = (
                piece["target_height"] // 2
            )

            # -------------------------------------------------
            # بالاتر از بقیه
            # -------------------------------------------------

            pieces.remove(
                piece
            )

            pieces.append(
                piece
            )

            break


# =========================================================
# MOVE DRAG
# =========================================================

def move_drag(
    event
):

    if dragging_piece is None:

        return

    mouse_x, mouse_y = event.pos

    dragging_piece["x"] = (
        mouse_x
        - drag_offset_x
    )

    dragging_piece["y"] = (
        mouse_y
        - drag_offset_y
    )


# =========================================================
# RELEASE DRAG
# =========================================================

def release_drag():

    global dragging_piece
    global finished
    global finish_time

    if dragging_piece is None:

        return

    piece = dragging_piece

    check_piece(
        piece
    )

    dragging_piece = None

    # -----------------------------------------------------
    # Finish
    # -----------------------------------------------------

    if check_finished():

        finished = True

        game_state = GAME_FINISHED

        finish_time = (
            pygame.time.get_ticks()
            - start_time
        )


# =========================================================
# TRAY SCROLL
# =========================================================

def scroll_tray(
    amount
):

    set_tray_scroll(
        tray_scroll_x
        + amount
    )


# =========================================================
# HANDLE PLAY EVENT
# =========================================================

def handle_play_event(
    event
):

    global scroll_dragging
    global scroll_drag_start_x
    global scroll_drag_start_value

    # -----------------------------------------------------
    # KEYBOARD
    # -----------------------------------------------------

    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_ESCAPE:

            if dragging_piece is not None:

                return

            game_state = GAME_LEVEL_SELECT

            return

        if event.key == pygame.K_r:

            reset_game()

            return

        if event.key == pygame.K_LEFT:

            scroll_tray(
                -scroll_speed
            )

            return

        if event.key == pygame.K_RIGHT:

            scroll_tray(
                scroll_speed
            )

            return

    # -----------------------------------------------------
    # MOUSE DOWN
    # -----------------------------------------------------

    if event.type == pygame.MOUSEBUTTONDOWN:

        mouse_x, mouse_y = event.pos

        # ---------------------------------------------
        # LEFT BUTTON
        # ---------------------------------------------

        if event.button == 1:

            # -----------------------------------------
            # left arrow
            # -----------------------------------------

            if (
                8
                <= mouse_x
                <= 46
                and
                TRAY_Y + 55
                <= mouse_y
                <= TRAY_Y + 105
            ):

                scroll_tray(
                    -scroll_speed * 2
                )

                return

            # -----------------------------------------
            # right arrow
            # -----------------------------------------

            if (
                WIDTH - 46
                <= mouse_x
                <= WIDTH - 8
                and
                TRAY_Y + 55
                <= mouse_y
                <= TRAY_Y + 105
            ):

                scroll_tray(
                    scroll_speed * 2
                )

                return

            # -----------------------------------------
            # Tray piece
            # -----------------------------------------

            if (
                mouse_y
                >= TRAY_Y + 30
            ):

                start_drag(
                    event
                )

                return

        # ---------------------------------------------
        # Mouse wheel
        # ---------------------------------------------

        if event.button == 4:

            scroll_tray(
                -scroll_speed
            )

            return

        if event.button == 5:

            scroll_tray(
                scroll_speed
            )

            return

    # -----------------------------------------------------
    # MOUSE MOTION
    # -----------------------------------------------------

    if event.type == pygame.MOUSEMOTION:

        if dragging_piece is not None:

            move_drag(
                event
            )

    # -----------------------------------------------------
    # MOUSE UP
    # -----------------------------------------------------

    if event.type == pygame.MOUSEBUTTONUP:

        if event.button == 1:

            if dragging_piece is not None:

                release_drag()


# =========================================================
# GLOBAL EVENT
# =========================================================

def handle_event(
    event
):

    global game_state

    if event.type == pygame.QUIT:

        pygame.quit()

        sys.exit()

    if game_state == GAME_LEVEL_SELECT:

        handle_level_select_event(
            event
        )

        return

    if (
        game_state == GAME_PLAYING
        or
        game_state == GAME_FINISHED
    ):

        handle_play_event(
            event
        )

        # -------------------------------------------------
        # Finished screen
        # -------------------------------------------------

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_r:

                reset_game()

                return

            if event.key == pygame.K_ESCAPE:

                game_state = GAME_LEVEL_SELECT

                return


def PUZZLE_():
    global finished
    global game_state
    global puzzle_image
    # -----------------------------------------------------
    # DRAW
    # -----------------------------------------------------

    screen.fill(
        BACKGROUND
    )

    # =====================================================
    # LEVEL SELECT
    # =====================================================

    if game_state == GAME_LEVEL_SELECT:

        draw_level_select()

    # =====================================================
    # GAME
    # =====================================================

    else:

        if puzzle_image is not None:

            draw_board()
            draw_image_preview()
            draw_pieces()

        draw_game_ui()

        draw_tray()

        if finished:

            draw_win()


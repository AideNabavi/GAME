import pygame
import random
import os

from modules.font import *


# ============================================================
# IMAGE FOLDER
# ============================================================

IMAGE_FOLDER = "asset/image/MODE/memory_detect"


# ============================================================
# COLORS
# ============================================================

BG = (25, 28, 38)

CARD = (45, 49, 63)
HOVER = (65, 72, 90)

WHITE = (245, 245, 245)
GRAY = (160, 165, 175)

BLUE = (70, 145, 240)
GREEN = (70, 210, 120)
RED = (230, 75, 80)


# ============================================================
# GRID
# ============================================================

GRID_SIZE = 5

CELL_SIZE = 105
CELL_GAP = 12

GRID_WIDTH = (
    GRID_SIZE * CELL_SIZE
    + (GRID_SIZE - 1) * CELL_GAP
)


# ============================================================
# GAME SETTINGS
# ============================================================

SHOW_TIME = 900
RESULT_TIME = 1000


# ============================================================
# GAME
# ============================================================

level = 1
score = 0

sequence = []
selected = []
grid = []

sequence_index = 0

state = "SHOW"

last_time = 0
result_time = 0

result_text = ""
result_color = WHITE


# ============================================================
# LOAD IMAGES
# ============================================================

images = {}


if os.path.exists(IMAGE_FOLDER):

    files = os.listdir(IMAGE_FOLDER)

    for file in files:

        if not file.lower().endswith(
            (
                ".png",
                ".jpg",
                ".jpeg",
                ".bmp",
                ".webp"
            )
        ):
            continue

        path = os.path.join(
            IMAGE_FOLDER,
            file
        )

        try:

            image = pygame.image.load(
                path
            ).convert_alpha()

        except pygame.error:

            print(
                "Could not load:",
                file
            )

            continue

        name = os.path.splitext(
            file
        )[0]

        name = name.replace(
            "_",
            " "
        )

        name = name.replace(
            "-",
            " "
        )

        name = name.title()

        images[name] = image

else:

    print(
        "Image folder not found:",
        IMAGE_FOLDER
    )


# ============================================================
# IMAGE NAMES
# ============================================================

image_names = list(
    images.keys()
)


# ============================================================
# IMAGE COUNT
# ============================================================

def get_image_count():

    return (
        3
        + (level - 1) // 5
    )


# ============================================================
# FIT IMAGE
# ============================================================

def fit_image(
    image,
    width,
    height
):

    image_width, image_height = (
        image.get_size()
    )

    scale = min(
        width / image_width,
        height / image_height
    )

    new_width = max(
        1,
        int(image_width * scale)
    )

    new_height = max(
        1,
        int(image_height * scale)
    )

    return pygame.transform.smoothscale(
        image,
        (
            new_width,
            new_height
        )
    )


# ============================================================
# DRAW IMAGE
# ============================================================

def draw_image(
    screen,
    image,
    rect
):

    image = fit_image(
        image,
        rect.width - 12,
        rect.height - 12
    )

    image_rect = image.get_rect(
        center=rect.center
    )

    screen.blit(
        image,
        image_rect
    )


# ============================================================
# DRAW TEXT
# ============================================================

def draw_text(
    screen,
    value,
    font,
    color,
    center
):

    surface = font.render(
        str(value),
        True,
        color
    )

    rect = surface.get_rect(
        center=center
    )

    screen.blit(
        surface,
        rect
    )


# ============================================================
# CREATE LEVEL
# ============================================================

def create_level():

    global sequence
    global selected
    global grid
    global sequence_index
    global state
    global last_time

    count = get_image_count()

    # --------------------------------------------------------
    # Safety
    # --------------------------------------------------------

    if len(image_names) < 25:

        print(
            "You need at least 25 images."
        )

        return

    # --------------------------------------------------------
    # Sequence
    # --------------------------------------------------------

    sequence = random.sample(
        image_names,
        count
    )

    # --------------------------------------------------------
    # Grid
    # --------------------------------------------------------

    grid = random.sample(
        image_names,
        25
    )

    # --------------------------------------------------------
    # Make sure sequence images
    # are inside the grid
    # --------------------------------------------------------

    for name in sequence:

        if name not in grid:

            index = random.randrange(
                25
            )

            grid[index] = name

    # --------------------------------------------------------
    # Reset
    # --------------------------------------------------------

    selected = []

    sequence_index = 0

    state = "SHOW"

    last_time = pygame.time.get_ticks()


# ============================================================
# RESET GAME
# ============================================================

def reset_game():

    global level
    global score
    global state
    global sequence
    global selected
    global grid
    global sequence_index
    global last_time
    global result_time
    global result_text
    global result_color

    level = 1
    score = 0

    sequence = []
    selected = []
    grid = []

    sequence_index = 0

    state = "SHOW"

    last_time = 0
    result_time = 0

    result_text = ""
    result_color = WHITE

    create_level()


# ============================================================
# GRID POSITION
# ============================================================

def get_grid_rects(
    WIDTH,
    HEIGHT
):

    grid_width = (
        GRID_SIZE * CELL_SIZE
        + (GRID_SIZE - 1) * CELL_GAP
    )

    grid_height = grid_width

    grid_x = (
        WIDTH - grid_width
    ) // 2

    # کل Grid وسط صفحه
    grid_y = (
        HEIGHT - grid_height
    ) // 2 + 120
    rects = []

    for i in range(25):

        row = i // GRID_SIZE
        col = i % GRID_SIZE

        x = (
            grid_x
            + col * (
                CELL_SIZE
                + CELL_GAP
            )
        )

        y = (
            grid_y
            + row * (
                CELL_SIZE
                + CELL_GAP
            )
        )

        rects.append(
            pygame.Rect(
                x,
                y,
                CELL_SIZE,
                CELL_SIZE
            )
        )

    return rects


# ============================================================
# DRAW HEADER
# ============================================================
def draw_header(
    screen,
    WIDTH
):

    draw_text(
        screen,
        "MEMORY SEQUENCE",
        fonts["heart"],
        WHITE,
        (
            WIDTH // 2,
            40
        )
    )

    draw_text(
        screen,
        f"Level {level}",
        fonts["heart"],
        WHITE,
        (
            100,
            40
        )
    )

    draw_text(
        screen,
        f"Score: {score}",
        fonts["heart"],
        WHITE,
        (
            WIDTH - 110,
            40
        )
    )

# ============================================================
# DRAW SHOW
# ============================================================

def draw_show(
    screen,
    WIDTH,
    HEIGHT
):

    screen.fill(BG)

    draw_header(
        screen,
        WIDTH
    )

    draw_text(
        screen,
        "MEMORIZE THE ORDER",
        fonts["heart"],
        BLUE,
        (
            WIDTH // 2,
            105
        )
    )

    if sequence_index >= len(sequence):
        return

    name = sequence[
        sequence_index
    ]

    image = images[name]

    # --------------------------------------------------------
    # Big card - CENTER
    # --------------------------------------------------------

    card_width = 320
    card_height = 330

    rect = pygame.Rect(
        (
            WIDTH - card_width
        ) // 2,

        (
            HEIGHT - card_height
        ) // 2,

        card_width,
        card_height
    )

    pygame.draw.rect(
        screen,
        CARD,
        rect,
        border_radius=25
    )

    pygame.draw.rect(
        screen,
        BLUE,
        rect,
        3,
        border_radius=25
    )

    # --------------------------------------------------------
    # Image
    # --------------------------------------------------------

    image_rect = pygame.Rect(
        rect.x + 15,
        rect.y + 15,
        rect.width - 30,
        250
    )

    draw_image(
        screen,
        image,
        image_rect
    )

    # --------------------------------------------------------
    # Name
    # --------------------------------------------------------

    draw_text(
        screen,
        name,
        fonts["heart"],
        WHITE,
        (
            rect.centerx,
            rect.bottom - 45
        )
    )

    # --------------------------------------------------------
    # Number
    # --------------------------------------------------------

    draw_text(
        screen,
        f"{sequence_index + 1} / {len(sequence)}",
        fonts["heart"],
        GRAY,
        (
            WIDTH // 2,
            rect.bottom + 35
        )
    )


# ============================================================
# DRAW SELECTED
# ============================================================
def draw_selected(
    screen,
    WIDTH
):

    if not selected:
        return

    draw_text(
        screen,
        "YOUR ORDER",
        fonts["heart"],
        GRAY,
        (
            WIDTH // 2,
            145
        )
    )

    card_width = 100
    card_height = 85
    gap = 10

    total_width = (
        len(selected) * card_width
        + (len(selected) - 1) * gap
    )

    start_x = (
        WIDTH - total_width
    ) // 2

    for i, name in enumerate(selected):

        x = (
            start_x
            + i * (
                card_width + gap
            )
        )

        rect = pygame.Rect(
            x,
            170,
            card_width,
            card_height
        )

        pygame.draw.rect(
            screen,
            CARD,
            rect,
            border_radius=14
        )

        pygame.draw.rect(
            screen,
            BLUE,
            rect,
            2,
            border_radius=14
        )

        image_rect = pygame.Rect(
            rect.x + 5,
            rect.y + 5,
            rect.width - 10,
            55
        )

        draw_image(
            screen,
            images[name],
            image_rect
        )

        draw_text(
            screen,
            i + 1,
            fonts["heart"],
            WHITE,
            (
                rect.centerx,
                rect.bottom - 12
            )
        )

# ============================================================
# DRAW GRID
# ============================================================

def draw_grid(
    screen,
    WIDTH,
    HEIGHT
):

    screen.fill(BG)

    draw_header(
        screen,
        WIDTH
    )

    draw_text(
        screen,
        "SELECT IN THE SAME ORDER",
        fonts["heart"],
        BLUE,
        (
            WIDTH // 2,
            100
        )
    )

    draw_selected(
        screen,
        WIDTH
    )

    mouse = pygame.mouse.get_pos()

    rects = get_grid_rects(
        WIDTH,
        HEIGHT
    )

    for i, name in enumerate(grid):

        rect = rects[i]

        # ----------------------------------------------------
        # Hover
        # ----------------------------------------------------

        if rect.collidepoint(mouse):

            color = HOVER

        else:

            color = CARD

        pygame.draw.rect(
            screen,
            color,
            rect,
            border_radius=14
        )

        # ----------------------------------------------------
        # Selected border
        # ----------------------------------------------------

        if name in selected:

            pygame.draw.rect(
                screen,
                BLUE,
                rect,
                3,
                border_radius=14
            )

        # ----------------------------------------------------
        # Image
        # ----------------------------------------------------

        image_rect = pygame.Rect(
            rect.x + 5,
            rect.y + 5,
            rect.width - 10,
            70
        )

        draw_image(
            screen,
            images[name],
            image_rect
        )

        # ----------------------------------------------------
        # Name
        # # ----------------------------------------------------

        # display_name = name

        # if len(display_name) > 13:

        #     display_name = (
        #         display_name[:12]
        #         + "..."
        #     )

        # draw_text(
        #     screen,
        #     display_name,
        #     fonts["heart"],
        #     WHITE,
        #     (
        #         rect.centerx,
        #         rect.bottom - 16
        #     )
        # )


# ============================================================
# DRAW RESULT
# ============================================================

def draw_result(
    screen,
    WIDTH,
    HEIGHT
):

    screen.fill(BG)

    draw_header(
        screen,
        WIDTH
    )

    draw_text(
        screen,
        result_text,
        fonts["heart"],
        result_color,
        (
            WIDTH // 2,
            HEIGHT // 2 - 30
        )
    )

    draw_text(
        screen,
        "Next...",
        fonts["heart"],
        GRAY,
        (
            WIDTH // 2,
            HEIGHT // 2 + 40
        )
    )


# ============================================================
# CLICK GRID
# ============================================================

def click_grid(
    position,
    WIDTH,
    HEIGHT
):

    global score
    global state
    global result_text
    global result_color
    global result_time

    if state != "PLAYING":
        return

    rects = get_grid_rects(
        WIDTH,
        HEIGHT
    )

    for i, name in enumerate(grid):

        rect = rects[i]

        if not rect.collidepoint(position):
            continue

        # ----------------------------------------------------
        # Already selected
        # ----------------------------------------------------

        if name in selected:
            return

        # ----------------------------------------------------
        # Expected image
        # ----------------------------------------------------

        expected = sequence[
            len(selected)
        ]

        # ====================================================
        # CORRECT
        # ====================================================

        if name == expected:

            selected.append(name)

            if len(selected) == len(sequence):

                score += (
                    get_image_count()
                    * 100
                )

                result_text = "CORRECT!"
                result_color = GREEN

                result_time = (
                    pygame.time.get_ticks()
                )

                state = "RESULT"

        # ====================================================
        # WRONG
        # ====================================================

        else:

            result_text = "WRONG!"
            result_color = RED

            result_time = (
                pygame.time.get_ticks()
            )

            state = "RESULT"

        return


# ============================================================
# MAIN GAME
# ============================================================

def IMAGE_SELECT_(screen):

    global state
    global sequence_index
    global last_time
    global level

    WIDTH, HEIGHT = screen.get_size()

    # ========================================================
    # SHOW
    # ========================================================

    if state == "SHOW":

        now = pygame.time.get_ticks()

        if (
            now - last_time
            >= SHOW_TIME
        ):

            sequence_index += 1

            last_time = now

            if (
                sequence_index
                >= len(sequence)
            ):

                state = "PLAYING"

        draw_show(
            screen,
            WIDTH,
            HEIGHT
        )

    # ========================================================
    # PLAYING
    # ========================================================

    elif state == "PLAYING":

        draw_grid(
            screen,
            WIDTH,
            HEIGHT
        )

    # ========================================================
    # RESULT
    # ========================================================

    elif state == "RESULT":

        draw_result(
            screen,
            WIDTH,
            HEIGHT
        )

        now = pygame.time.get_ticks()

        if (
            now - result_time
            >= RESULT_TIME
        ):

            if result_text == "CORRECT!":

                level += 1

            create_level()
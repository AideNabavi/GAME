import pygame
import random
import os
import sys


pygame.init()


# ============================================================
# SETTINGS
# ============================================================

WIDTH = 1200
HEIGHT = 800

screen = pygame.display.set_mode(
    (1920, 1080),
    pygame.FULLSCREEN
)


pygame.display.set_caption(
    "Memory Sequence"
)

clock = pygame.time.Clock()


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
# FONTS
# ============================================================

font_title = pygame.font.Font(
    None,
    48
)

font_normal = pygame.font.Font(
    None,
    30
)

font_small = pygame.font.Font(
    None,
    22
)

font_big = pygame.font.Font(
    None,
    60
)


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

GRID_X = (
    WIDTH - GRID_WIDTH
) // 2

GRID_Y = 285


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

SHOW_TIME = 900

result_time = 0

result_text = ""

result_color = WHITE


# ============================================================
# LOAD IMAGES
# ============================================================

images = {}


if not os.path.exists(IMAGE_FOLDER):

    print(
        "Image folder not found:"
    )

    print(
        IMAGE_FOLDER
    )

    pygame.quit()
    sys.exit()


files = os.listdir(
    IMAGE_FOLDER
)


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


# ============================================================
# IMAGE NAMES
# ============================================================

image_names = list(
    images.keys()
)


if len(image_names) < 25:

    print(
        "You need at least 25 images."
    )

    print(
        "Current images:",
        len(image_names)
    )

    pygame.quit()
    sys.exit()


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


    new_width = int(
        image_width * scale
    )

    new_height = int(
        image_height * scale
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

def text(
    value,
    font,
    color,
    x,
    y
):

    surface = font.render(
        str(value),
        True,
        color
    )


    rect = surface.get_rect(
        center=(
            x,
            y
        )
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
    # Put sequence images inside grid
    # --------------------------------------------------------

    for name in sequence:

        if name not in grid:

            index = random.randrange(
                25
            )

            grid[index] = name


    # --------------------------------------------------------
    # Reset selected
    # --------------------------------------------------------

    selected = []


    # --------------------------------------------------------
    # Reset sequence
    # --------------------------------------------------------

    sequence_index = 0


    # --------------------------------------------------------
    # State
    # --------------------------------------------------------

    state = "SHOW"


    last_time = pygame.time.get_ticks()


# ============================================================
# DRAW HEADER
# ============================================================

def draw_header():

    text(
        "MEMORY SEQUENCE",
        font_title,
        WHITE,
        WIDTH // 2,
        40
    )


    text(
        "Level " + str(level),
        font_normal,
        WHITE,
        80,
        40
    )


    text(
        "Score: " + str(score),
        font_normal,
        WHITE,
        WIDTH - 100,
        40
    )


# ============================================================
# DRAW SHOW SCREEN
# ============================================================

def draw_show():

    screen.fill(
        BG
    )


    draw_header()


    text(
        "MEMORIZE THE ORDER",
        font_normal,
        BLUE,
        WIDTH // 2,
        100
    )


    if sequence_index >= len(sequence):

        return


    name = sequence[
        sequence_index
    ]


    image = images[
        name
    ]


    # --------------------------------------------------------
    # BIG CARD
    # --------------------------------------------------------

    rect = pygame.Rect(
        WIDTH // 2 - 160,
        160,
        320,
        330
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
    # IMAGE
    # --------------------------------------------------------

    image_rect = pygame.Rect(
        rect.x + 15,
        rect.y + 15,
        rect.width - 30,
        250
    )


    draw_image(
        image,
        image_rect
    )


    # --------------------------------------------------------
    # NAME
    # --------------------------------------------------------

    text(
        name,
        font_normal,
        WHITE,
        rect.centerx,
        rect.bottom - 45
    )


    # --------------------------------------------------------
    # NUMBER
    # --------------------------------------------------------

    text(
        str(sequence_index + 1)
        + " / "
        + str(len(sequence)),
        font_small,
        GRAY,
        WIDTH // 2,
        540
    )


# ============================================================
# DRAW SELECTED
# ============================================================

def draw_selected():

    if not selected:

        return


    text(
        "YOUR ORDER",
        font_small,
        GRAY,
        WIDTH // 2,
        135
    )


    card_width = 120

    card_height = 100

    gap = 12


    total = (
        len(selected) * card_width
        + (len(selected) - 1) * gap
    )


    start_x = (
        WIDTH - total
    ) // 2


    for i, name in enumerate(
        selected
    ):

        x = (
            start_x
            + i * (
                card_width
                + gap
            )
        )


        rect = pygame.Rect(
            x,
            160,
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
            65
        )


        draw_image(
            images[name],
            image_rect
        )


        text(
            str(i + 1),
            font_small,
            WHITE,
            rect.centerx,
            rect.bottom - 13
        )


# ============================================================
# DRAW GRID
# ============================================================

def draw_grid():

    screen.fill(
        BG
    )


    draw_header()


    text(
        "SELECT IN THE SAME ORDER",
        font_normal,
        BLUE,
        WIDTH // 2,
        100
    )


    draw_selected()


    mouse = pygame.mouse.get_pos()


    for i, name in enumerate(
        grid
    ):

        row = i // GRID_SIZE

        col = i % GRID_SIZE


        x = (
            GRID_X
            + col * (
                CELL_SIZE
                + CELL_GAP
            )
        )


        y = (
            GRID_Y
            + row * (
                CELL_SIZE
                + CELL_GAP
            )
        )


        rect = pygame.Rect(
            x,
            y,
            CELL_SIZE,
            CELL_SIZE
        )


        # ----------------------------------------------------
        # Hover
        # ----------------------------------------------------

        if rect.collidepoint(
            mouse
        ):

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
            images[name],
            image_rect
        )


        # ----------------------------------------------------
        # Name
        # ----------------------------------------------------

        display_name = name


        if len(display_name) > 13:

            display_name = (
                display_name[:12]
                + "..."
            )


        text(
            display_name,
            font_small,
            WHITE,
            rect.centerx,
            rect.bottom - 16
        )


# ============================================================
# DRAW RESULT
# ============================================================

def draw_result():

    screen.fill(
        BG
    )


    draw_header()


    text(
        result_text,
        font_big,
        result_color,
        WIDTH // 2,
        HEIGHT // 2 - 30
    )


    text(
        "Next...",
        font_normal,
        GRAY,
        WIDTH // 2,
        HEIGHT // 2 + 40
    )


# ============================================================
# CLICK GRID
# ============================================================

def click_grid(position):

    global score
    global state
    global result_text
    global result_color
    global result_time


    for i, name in enumerate(
        grid
    ):

        row = i // GRID_SIZE

        col = i % GRID_SIZE


        x = (
            GRID_X
            + col * (
                CELL_SIZE
                + CELL_GAP
            )
        )


        y = (
            GRID_Y
            + row * (
                CELL_SIZE
                + CELL_GAP
            )
        )


        rect = pygame.Rect(
            x,
            y,
            CELL_SIZE,
            CELL_SIZE
        )


        if not rect.collidepoint(
            position
        ):

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

            selected.append(
                name
            )


            # ------------------------------------------------
            # Finished
            # ------------------------------------------------

            if (
                len(selected)
                == len(sequence)
            ):

                score += (
                    get_image_count()
                    * 100
                )


                result_text = (
                    "CORRECT!"
                )


                result_color = (
                    GREEN
                )


                result_time = (
                    pygame.time.get_ticks()
                )


                state = "RESULT"


        # ====================================================
        # WRONG
        # ====================================================

        else:

            result_text = (
                "WRONG!"
            )


            result_color = (
                RED
            )


            result_time = (
                pygame.time.get_ticks()
            )


            state = "RESULT"


        return


# ============================================================
# START GAME
# ============================================================

create_level()


# ============================================================
# MAIN LOOP
# ============================================================

running = True


while running:

    # ========================================================
    # EVENTS
    # ========================================================

    for event in pygame.event.get():

        # ----------------------------------------------------
        # QUIT
        # ----------------------------------------------------

        if event.type == pygame.QUIT:

            running = False


        # ----------------------------------------------------
        # KEYBOARD
        # ----------------------------------------------------

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:

                running = False


        # ----------------------------------------------------
        # MOUSE
        # ----------------------------------------------------

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                if state == "PLAYING":

                    click_grid(
                        event.pos
                    )


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


        draw_show()


    # ========================================================
    # PLAYING
    # ========================================================

    elif state == "PLAYING":

        draw_grid()


    # ========================================================
    # RESULT
    # ========================================================

    elif state == "RESULT":

        draw_result()


        now = pygame.time.get_ticks()


        if (
            now - result_time
            >= 1000
        ):

            if result_text == "CORRECT!":

                level += 1


            create_level()


    # ========================================================
    # DISPLAY
    # ========================================================

    pygame.display.flip()

    clock.tick(60)


# ============================================================
# QUIT
# ============================================================

pygame.quit()

sys.exit()
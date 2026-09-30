import pygame
import random
import os

from modules.font import fonts


# =========================================================
# SETTINGS
# =========================================================

WIDTH = 1080
HEIGHT = 720

screen = None
correct_start_time = 0

CORRECT_SHOW_TIME = 800  # میلی‌ثانیه

def start_new_round():

    global memory_images
    global memory_numbers
    global current_memory_index
    global memory_start_time

    global grid_images
    global grid_paths
    global grid_rects

    global current_question_number
    global current_question_image

    global game_phase

    memorize_count = LEVELS[selected_level]["memorize_count"]

    files = get_image_files()

    if len(files) < 20:
        print("ERROR: Need at least 20 images.")
        return

    # انتخاب تصاویر جدید برای حافظه
    memory_images = random.sample(
        files,
        memorize_count
    )

    memory_numbers = {}

    for number, image_path in enumerate(
        memory_images,
        start=1
    ):
        memory_numbers[number] = image_path

    # ریست وضعیت حافظه
    current_memory_index = 0

    memory_start_time = pygame.time.get_ticks()

    # پاک کردن Grid قبلی
    grid_images = []
    grid_paths = []
    grid_rects = []

    # سؤال قبلی
    current_question_number = None
    current_question_image = None

    # شروع نمایش تصاویر
    game_phase = "MEMORIZE"
    

# =========================================================
# SCREEN SIZE
# =========================================================

def WIDTH_HEIGHT_gettter(screen_, WIDTH_, HEIGHT_):

    global WIDTH
    global HEIGHT
    global screen

    WIDTH = WIDTH_
    HEIGHT = HEIGHT_
    screen = screen_


# =========================================================
# IMAGE FOLDER
# =========================================================

IMAGE_FOLDER = "./asset/image/MODE/memory_detect"


# =========================================================
# GAME SETTINGS
# =========================================================

LEVELS = {

    "EASY": {
        "memorize_count": 3,
    },

    "MEDIUM": {
        "memorize_count": 4,
    },

    "HARD": {
        "memorize_count": 5,
    }
}


# =========================================================
# SELECTED LEVEL
# =========================================================

selected_level = None


# =========================================================
# GRID SETTINGS
# =========================================================

ROWS = 4
COLS = 5

TOTAL_GRID_IMAGES = ROWS * COLS


# =========================================================
# MEMORY SETTINGS
# =========================================================

IMAGE_SHOW_TIME = 1000


# =========================================================
# GAME PHASE
# =========================================================

# SELECT_LEVEL
# MEMORIZE
# QUESTION
# GAME_OVER
# WIN

game_phase = "SELECT_LEVEL"


# =========================================================
# MEMORY
# =========================================================

memory_images = []

memory_numbers = {}

current_memory_index = 0

memory_start_time = 0


# =========================================================
# GRID
# =========================================================

grid_paths = []
grid_images = []
grid_rects = []


# =========================================================
# QUESTION
# =========================================================

current_question_number = None
current_question_image = None


# =========================================================
# LIVES
# =========================================================

MAX_LIVES = 3

lives = MAX_LIVES


# # =========================================================
# # RESULT
# # =========================================================

# finished = False
# won = False


# =========================================================
# IMAGE CACHE
# =========================================================

image_cache = {}


# =========================================================
# LEVEL BUTTONS
# =========================================================

level_rects = {}


# =========================================================
# LOAD IMAGE
# =========================================================

def load_image(path, size):

    key = (
        path,
        size
    )

    if key in image_cache:

        return image_cache[key]


    try:

        image = pygame.image.load(
            path
        ).convert_alpha()


        image = pygame.transform.smoothscale(
            image,
            size
        )


        image_cache[key] = image


        return image


    except Exception as e:

        print(
            "IMAGE LOAD ERROR:",
            path
        )

        print(e)

        return None


# =========================================================
# GET IMAGE FILES
# =========================================================

def get_image_files():

    if not os.path.exists(
        IMAGE_FOLDER
    ):

        print(
            "IMAGE FOLDER NOT FOUND:"
        )

        print(
            IMAGE_FOLDER
        )

        return []


    valid_extensions = (
        ".png",
        ".jpg",
        ".jpeg",
        ".webp"
    )


    files = []


    for filename in os.listdir(
        IMAGE_FOLDER
    ):

        if filename.lower().endswith(
            valid_extensions
        ):

            files.append(
                os.path.join(
                    IMAGE_FOLDER,
                    filename
                )
            )


    return files


# =========================================================
# RESET GAME
# =========================================================

def reset_game():

    global selected_level
    global game_phase

    global memory_images
    global memory_numbers
    global current_memory_index
    global memory_start_time

    global grid_images
    global grid_paths
    global grid_rects

    global current_question_number
    global current_question_image

    global lives
    global finished
    global won

    global correct_start_time
    # -------------------------
    # RESET EVERYTHING
    # -------------------------

    selected_level = None

    memory_images = []
    memory_numbers = {}

    current_memory_index = 0
    memory_start_time = 0
    correct_start_time = 0

    grid_images = []
    grid_paths = []
    grid_rects = []

    current_question_number = None
    current_question_image = None

    lives = MAX_LIVES

    finished = False
    won = False

    # -------------------------
    # BACK TO LEVEL SELECTION
    # -------------------------

    game_phase = "SELECT_LEVEL"

    create_level_rects()
# =========================================================
# CREATE GRID
# =========================================================

def create_grid():

    global grid_paths
    global grid_images
    global grid_rects


    files = get_image_files()


    if len(files) < TOTAL_GRID_IMAGES:

        return False


    # -----------------------------------------------------
    # MEMORY IMAGES MUST BE IN GRID
    # -----------------------------------------------------

    target_images = list(
        memory_images
    )


    # -----------------------------------------------------
    # OTHER RANDOM IMAGES
    # -----------------------------------------------------

    available_files = [

        path

        for path in files

        if path not in target_images

    ]


    needed_other_images = (
        TOTAL_GRID_IMAGES
        - len(target_images)
    )


    if len(available_files) < needed_other_images:

        print(
            "NOT ENOUGH DIFFERENT IMAGES."
        )

        return False


    other_images = random.sample(
        available_files,
        needed_other_images
    )


    # -----------------------------------------------------
    # COMBINE
    # -----------------------------------------------------

    all_grid_images = (
        target_images
        + other_images
    )


    # -----------------------------------------------------
    # RANDOMIZE POSITION
    # -----------------------------------------------------

    random.shuffle(
        all_grid_images
    )


    # -----------------------------------------------------
    # CLEAR OLD DATA
    # -----------------------------------------------------

    grid_paths = []
    grid_images = []
    grid_rects = []


    # =====================================================
    # GRID SIZE
    # =====================================================

    margin_x = 100

    margin_top = 125

    gap_x = 15

    gap_y = 15


    available_width = (
        WIDTH
        - margin_x * 2
    )


    available_height = (
        HEIGHT
        - margin_top
        - 40
    )


    cell_width = (

        available_width
        - gap_x * (COLS - 1)

    ) // COLS


    cell_height = (

        available_height
        - gap_y * (ROWS - 1)

    ) // ROWS


    cell_size = min(
        cell_width,
        cell_height
    )


    total_width = (

        COLS * cell_size

        + gap_x * (COLS - 1)

    )


    total_height = (

        ROWS * cell_size

        + gap_y * (ROWS - 1)

    )


    start_x = (

        WIDTH
        - total_width

    ) // 2


    start_y = (

        margin_top

        + (

            HEIGHT
            - margin_top
            - total_height

        ) // 2

    )


    # =====================================================
    # CREATE GRID
    # =====================================================

    for index, image_path in enumerate(
        all_grid_images
    ):

        row = index // COLS

        col = index % COLS


        x = (

            start_x

            + col
            * (
                cell_size
                + gap_x
            )

        )


        y = (

            start_y

            + row
            * (
                cell_size
                + gap_y
            )

        )


        rect = pygame.Rect(
            x,
            y,
            cell_size,
            cell_size
        )


        image = load_image(
            image_path,
            (
                cell_size,
                cell_size
            )
        )


        # -------------------------------------------------
        # SAVE PATH
        # -------------------------------------------------

        grid_paths.append(
            image_path
        )


        # -------------------------------------------------
        # SAVE IMAGE
        # -------------------------------------------------

        grid_images.append(
            image
        )


        # -------------------------------------------------
        # SAVE RECT
        # -------------------------------------------------

        grid_rects.append(
            rect
        )


    return True


# =========================================================
# SELECT QUESTION
# =========================================================

def select_question():

    global current_question_number
    global current_question_image


    if selected_level not in LEVELS:

        return


    memorize_count = LEVELS[
        selected_level
    ][
        "memorize_count"
    ]


    # -----------------------------------------------------
    # RANDOM NUMBER
    # -----------------------------------------------------

    current_question_number = random.randint(
        1,
        memorize_count
    )


    # -----------------------------------------------------
    # GET CORRESPONDING IMAGE
    # -----------------------------------------------------

    current_question_image = memory_numbers[
        current_question_number
    ]


# =========================================================
# FINISH MEMORY
# =========================================================

def finish_memorize():

    global game_phase


    success = create_grid()


    if not success:

        game_phase = "GAME_OVER"

        return


    select_question()


    game_phase = "QUESTION"


# =========================================================
# UPDATE
# =========================================================
def update():

    global current_memory_index
    global memory_start_time

    global game_phase
    global correct_start_time


    # =====================================================
    # CORRECT
    # =====================================================

    if game_phase == "CORRECT":

        current_time = pygame.time.get_ticks()

        if (
            current_time - correct_start_time
            >= CORRECT_SHOW_TIME
        ):

            start_new_round()

        return


    # =====================================================
    # ONLY MEMORIZE
    # =====================================================

    if game_phase != "MEMORIZE":

        return


    now = pygame.time.get_ticks()


    elapsed = (
        now
        - memory_start_time
    )


    # =====================================================
    # IMAGE TIME FINISHED
    # =====================================================

    if elapsed >= IMAGE_SHOW_TIME:

        current_memory_index += 1


        # -------------------------------------------------
        # MORE IMAGES
        # -------------------------------------------------

        if current_memory_index < len(
            memory_images
        ):

            memory_start_time = now


        # -------------------------------------------------
        # MEMORY FINISHED
        # -------------------------------------------------

        else:

            finish_memorize()



def draw_correct():

    font = pygame.font.Font(None, 100)

    text = font.render(
        "CORRECT!",
        True,
        (80, 220, 100)
    )

    rect = text.get_rect(
        center=(WIDTH // 2, HEIGHT // 2)
    )

    screen.blit(
        text,
        rect
    )
    
# =========================================================
# CREATE LEVEL BUTTONS
# =========================================================

def create_level_rects():

    global level_rects


    button_width = 360

    button_height = 80

    gap = 25


    start_x = (
        WIDTH
        - button_width
    ) // 2


    total_height = (
        button_height * 3
        + gap * 2
    )


    start_y = (
        HEIGHT
        - total_height
    ) // 2


    level_rects = {}


    levels = [
        "EASY",
        "MEDIUM",
        "HARD"
    ]


    for index, level in enumerate(
        levels
    ):

        y = (

            start_y

            + index
            * (
                button_height
                + gap
            )

        )


        level_rects[level] = pygame.Rect(
            start_x,
            y,
            button_width,
            button_height
        )

def start_game():

    global game_phase

    global memory_images
    global memory_numbers
    global current_memory_index
    global memory_start_time

    global grid_images
    global grid_paths
    global grid_rects

    global current_question_number
    global current_question_image

    global lives
    global finished
    global won

    memorize_count = LEVELS[selected_level]["memorize_count"]

    files = get_image_files()

    if len(files) < 20:
        print("ERROR: Need at least 20 images.")
        return

    # -------------------------
    # RESET GAME DATA
    # -------------------------

    memory_images = random.sample(
        files,
        memorize_count
    )

    memory_numbers = {}

    for number, image_path in enumerate(
        memory_images,
        start=1
    ):
        memory_numbers[number] = image_path

    current_memory_index = 0

    memory_start_time = pygame.time.get_ticks()

    current_question_number = None
    current_question_image = None

    lives = MAX_LIVES

    finished = False
    won = False

    grid_images = []
    grid_paths = []
    grid_rects = []

    # -------------------------
    # START MEMORIZE
    # -------------------------

    game_phase = "MEMORIZE"

# =========================================================
# DRAW LEVEL SELECTION
# =========================================================

def draw_level_selection():

    if not level_rects:

        create_level_rects()


    # -----------------------------------------------------
    # FONT
    # -----------------------------------------------------

    if "heart" in fonts:

        title_font = fonts["heart"]

    else:

        title_font = pygame.font.Font(
            None,
            55
        )


    # -----------------------------------------------------
    # TITLE
    # -----------------------------------------------------

    title = title_font.render(
        "SELECT LEVEL",
        True,
        (255, 255, 255)
    )


    title_rect = title.get_rect(
        centerx=WIDTH // 2,
        top=70
    )


    screen.blit(
        title,
        title_rect
    )


    # -----------------------------------------------------
    # BUTTONS
    # -----------------------------------------------------

    for level, rect in level_rects.items():

        pygame.draw.rect(
            screen,
            (75, 75, 75),
            rect,
            border_radius=18
        )


        pygame.draw.rect(
            screen,
            (180, 180, 180),
            rect,
            width=3,
            border_radius=18
        )


        text = title_font.render(
            level,
            True,
            (255, 255, 255)
        )


        text_rect = text.get_rect(
            center=rect.center
        )


        screen.blit(
            text,
            text_rect
        )


# =========================================================
# EVENT
# =========================================================

def event(event):

    global selected_level

    global lives
    global game_phase

    global finished
    global won


    # =====================================================
    # SELECT LEVEL
    # =====================================================

    if game_phase == "SELECT_LEVEL":


        if event.type != pygame.MOUSEBUTTONDOWN:

            return


        if event.button != 1:

            return


        mouse_pos = event.pos


        if not level_rects:

            create_level_rects()


        for level, rect in level_rects.items():


            if rect.collidepoint(
                mouse_pos
            ):

                # -----------------------------------------
                # SAVE LEVEL
                # -----------------------------------------

                selected_level = level


                # -----------------------------------------
                # START GAME
                # -----------------------------------------

                # reset_game()
                start_game()
                return


    # =====================================================
    # QUESTION
    # =====================================================

    if game_phase != "QUESTION":

        return


    if event.type != pygame.MOUSEBUTTONDOWN:

        return


    if event.button != 1:

        return


    mouse_pos = event.pos


    # =====================================================
    # FIND CLICKED CELL
    # =====================================================

    for index, rect in enumerate(
        grid_rects
    ):


        if not rect.collidepoint(
            mouse_pos
        ):

            continue


        # -------------------------------------------------
        # GET SELECTED IMAGE PATH
        # -------------------------------------------------

        selected_path = grid_paths[
            index
        ]


        # =================================================
        # CORRECT
        # =================================================

        if selected_path == current_question_image:


            global correct_start_time

            correct_start_time = pygame.time.get_ticks()

            game_phase = "CORRECT"

            return

        # =================================================
        # WRONG
        # =================================================

        else:


            lives -= 1


            print(
                "WRONG!",
                "Lives:",
                lives
            )


            # ---------------------------------------------
            # GAME OVER
            # ---------------------------------------------

            if lives <= 0:

                won = False

                finished = True

                game_phase = "GAME_OVER"


        break


# =========================================================
# DRAW MEMORY IMAGE
# =========================================================

def draw_memorize():

    if current_memory_index >= len(
        memory_images
    ):

        return


    image_path = memory_images[
        current_memory_index
    ]


    # -----------------------------------------------------
    # IMAGE SIZE
    # -----------------------------------------------------

    size = min(
        WIDTH,
        HEIGHT
    ) // 2


    image = load_image(
        image_path,
        (
            size,
            size
        )
    )


    if image is None:

        return


    rect = image.get_rect(
        center=(
            WIDTH // 2,
            HEIGHT // 2
        )
    )


    screen.blit(
        image,
        rect
    )


    # -----------------------------------------------------
    # NUMBER
    # -----------------------------------------------------

    number = str(
        current_memory_index + 1
    )


    if "heart" in fonts:

        font = fonts["heart"]

    else:

        font = pygame.font.Font(
            None,
            45
        )


    text = font.render(
        number,
        True,
        (255, 255, 255)
    )


    text_rect = text.get_rect(
        centerx=WIDTH // 2,
        top=rect.bottom + 10
    )


    screen.blit(
        text,
        text_rect
    )


# =========================================================
# DRAW QUESTION
# =========================================================

def draw_question():

    # -----------------------------------------------------
    # FONT
    # -----------------------------------------------------

    if "heart" in fonts:

        font = fonts["heart"]

    else:

        font = pygame.font.Font(
            None,
            40
        )


    # -----------------------------------------------------
    # QUESTION
    # -----------------------------------------------------

    text = font.render(
        f"FIND IMAGE #{current_question_number}",
        True,
        (255, 255, 255)
    )


    text_rect = text.get_rect(
        centerx=WIDTH // 2,
        top=20
    )


    screen.blit(
        text,
        text_rect
    )


    # -----------------------------------------------------
    # GRID
    # -----------------------------------------------------

    for image, rect in zip(
        grid_images,
        grid_rects
    ):


        if image is not None:

            screen.blit(
                image,
                rect
            )


# =========================================================
# DRAW LIVES
# =========================================================

def draw_lives():

    if "heart" in fonts:

        font = fonts["heart"]

    else:

        font = pygame.font.Font(
            None,
            30
        )


    text = font.render(
        f"LIVES: {lives}",
        True,
        (255, 255, 255)
    )


    rect = text.get_rect(
        right=WIDTH - 30,
        top=25
    )


    screen.blit(
        text,
        rect
    )


# =========================================================
# DRAW GAME OVER
# =========================================================

def draw_game_over():

    if "heart" in fonts:

        font = fonts["heart"]

    else:

        font = pygame.font.Font(
            None,
            70
        )


    text = font.render(
        "GAME OVER",
        True,
        (255, 255, 255)
    )


    rect = text.get_rect(
        center=(
            WIDTH // 2,
            HEIGHT // 2
        )
    )


    screen.blit(
        text,
        rect
    )




# =========================================================
# MAIN DRAW FUNCTION
# =========================================================
def MEMORY_HARD_():

    if screen is None:

        return


    # =====================================================
    # SELECT LEVEL
    # =====================================================

    if game_phase == "SELECT_LEVEL":

        draw_level_selection()


    # =====================================================
    # MEMORIZE
    # =====================================================

    elif game_phase == "MEMORIZE":

        draw_memorize()


    # =====================================================
    # QUESTION
    # =====================================================

    elif game_phase == "QUESTION":

        draw_question()

        draw_lives()


    # =====================================================
    # CORRECT
    # =====================================================

    elif game_phase == "CORRECT":

        draw_correct()


    # =====================================================
    # GAME OVER
    # =====================================================

    elif game_phase == "GAME_OVER":

        draw_game_over()
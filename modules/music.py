import pygame
import random

from modules.EFFECT.hover import hover_image_music

MUSIC_OFFSET_X = -10    
MUSIC_OFFSET_Y = 130
# ============================================================
# MUSIC SIDE EFFECT
# ============================================================

music_side_start_times = {}

music_side_order = []

music_side_initialized = False

music_panel_start_time = None

music_panel_initialized = False

# ============================================================
# RESET SIDE EFFECT
# ============================================================
def reset_music_side_effect():

    global music_side_start_times
    global music_side_order
    global music_side_initialized

    global music_panel_start_time
    global music_panel_initialized

    music_side_start_times.clear()

    music_side_order = []

    music_side_initialized = False

    music_panel_start_time = None

    music_panel_initialized = False









def draw_music_panel_side_effect(
    screen,
    image,
    target_rect
):

    global music_panel_start_time
    global music_panel_initialized

    duration = 600

    # ========================================================
    # START TIME
    # ========================================================

    if not music_panel_initialized:

        music_panel_start_time = pygame.time.get_ticks()

        music_panel_initialized = True


    # ========================================================
    # TIME
    # ========================================================

    now = pygame.time.get_ticks()

    elapsed = now - music_panel_start_time


    # ========================================================
    # PROGRESS
    # ========================================================

    if elapsed >= duration:

        progress = 1.0

    else:

        progress = elapsed / duration

        # Ease Out
        progress = (
            1
            - (1 - progress) ** 3
        )


    # ========================================================
    # START POSITION
    # ========================================================

    start_x = (
        screen.get_width()
        + image.get_width()
    )


    # ========================================================
    # CURRENT X
    # ========================================================

    current_x = (
        start_x
        +
        (
            target_rect.centerx
            - start_x
        )
        * progress
    )


    # ========================================================
    # CURRENT RECT
    # ========================================================

    rect = image.get_rect(

        center=(

            int(current_x),

            target_rect.centery

        )

    )


    # ========================================================
    # DRAW
    # ========================================================

    screen.blit(
        image,
        rect
    )





















# ============================================================
# DRAW MUSIC SIDE EFFECT
# ============================================================

def draw_music_side_effect(
    screen,
    image,
    target_x,
    target_y,
    index
):

    duration = 600

    delay = 120


    # ========================================================
    # START TIME
    # ========================================================

    if index not in music_side_start_times:

        order_index = music_side_order.index(index)

        music_side_start_times[index] = (
            pygame.time.get_ticks()
            + order_index * delay
        )


    start_time = music_side_start_times[index]


    # ========================================================
    # TIME
    # ========================================================

    now = pygame.time.get_ticks()

    elapsed = now - start_time


    # ========================================================
    # BEFORE START
    # ========================================================

    if elapsed < 0:

        return


    # ========================================================
    # PROGRESS
    # ========================================================

    if elapsed >= duration:

        progress = 1.0

    else:

        progress = elapsed / duration

        # Ease Out
        progress = (
            1
            - (1 - progress) ** 3
        )


    # ========================================================
    # START POSITION
    # ========================================================

    # از سمت راست صفحه وارد می‌شود

    start_x = (
        screen.get_width()
        + image.get_width()
    )


    # ========================================================
    # CURRENT POSITION
    # ========================================================

    current_x = (
        start_x
        + (target_x - start_x)
        * progress
    )


    # ========================================================
    # DRAW
    # ========================================================

    rect = image.get_rect(
        center=(
            int(current_x),
            target_y
        )
    )


    screen.blit(
        image,
        rect
    )


# ============================================================
# IMAGE SETTINGS
# ============================================================

IMAGE_SIZE = 150

HOVER_SIZE = 180


# ============================================================
# GAP
# ============================================================

GAP_X = 100

GAP_Y = 40


# ============================================================
# GRID
# ============================================================

COLUMNS = 4

ROWS = 3


# ============================================================
# MUSIC RECTANGLES
# ============================================================

music_rects = {}


# ============================================================
# MUSIC FILES
# ============================================================

music_files = {

    0: "./asset/music/1.mp3",

    1: "./asset/music/2.mp3",

    2: "./asset/music/3.mp3",

    3: "./asset/music/4.mp3",

    4: "./asset/music/5.mp3",

    5: "./asset/music/6.mp3",

}


# ============================================================
# CURRENT MUSIC
# ============================================================

current_music = -1


# ============================================================
# PLAY MUSIC
# ============================================================

def play_music(
    index,
    music_state
):

    global current_music


    # --------------------------------------------------------
    # MUSIC OFF
    # --------------------------------------------------------

    if music_state == 0:

        return


    # --------------------------------------------------------
    # LOAD
    # --------------------------------------------------------

    pygame.mixer.music.load(
        music_files[index]
    )


    # --------------------------------------------------------
    # VOLUME
    # --------------------------------------------------------

    pygame.mixer.music.set_volume(
        0.2
    )


    # --------------------------------------------------------
    # PLAY
    # --------------------------------------------------------

    pygame.mixer.music.play(
        -1
    )


    current_music = index


# ============================================================
# PROFILE SIZE
# ============================================================

profile_size = [

    IMAGE_SIZE,
    IMAGE_SIZE,
    IMAGE_SIZE,
    IMAGE_SIZE,
    IMAGE_SIZE,
    IMAGE_SIZE,
    IMAGE_SIZE,
    IMAGE_SIZE,
    IMAGE_SIZE,
    IMAGE_SIZE,
    IMAGE_SIZE,
    IMAGE_SIZE

]


# ============================================================
# DRAW MUSIC
# ============================================================

def draw_music(
    screen,
    current_width,
    current_height,
    background_music,
    profile_image
):

    global music_side_order
    global music_side_initialized


    # ========================================================
    # RANDOM ORDER
    # ========================================================

    # فقط یک بار ساخته می‌شود

    if not music_side_initialized:

        music_side_order = list(
            range(COLUMNS * ROWS)
        )

        random.shuffle(
            music_side_order
        )

        music_side_initialized = True


    # ========================================================
    # CLEAR RECTS
    # ========================================================

    music_rects.clear()


    # ========================================================
    # BACKGROUND PANEL
    # ========================================================

    music_panel_rect = background_music.get_rect(

        center=(

            current_width // 2 + 160,

            current_height // 2 - 140

        )

    )


    # draw_music_panel_side_effect(

    #     screen,

    #     background_music,

    #     music_panel_rect

    # )
    # ========================================================
    # TOTAL WIDTH
    # ========================================================

    total_width = (

        IMAGE_SIZE * COLUMNS

        +

        GAP_X * (
            COLUMNS - 1
        )

    )


    # ========================================================
    # START X
    # ========================================================

    start_x = (

        music_panel_rect.centerx

        -

        total_width // 2 

    )


    # ========================================================
    # MOUSE
    # ========================================================

    mouse_pos = pygame.mouse.get_pos()


    # ========================================================
    # INDEX
    # ========================================================

    index = 0


    # ========================================================
    # GRID
    # ========================================================

    for row in range(ROWS):

        for col in range(COLUMNS):


            # =================================================
            # TARGET X
            # =================================================

            x = (
                start_x
                +
                col * (
                    IMAGE_SIZE
                    +
                    GAP_X
                )
                +
                MUSIC_OFFSET_X
            )

            y = (
                music_panel_rect.y
                +
                330
                +
                row * (
                    IMAGE_SIZE
                    +
                    GAP_Y
                )
                +
                MUSIC_OFFSET_Y
            )

            # =================================================
            # RECT
            # =================================================

            music_rect = pygame.Rect(

                x,

                y,

                IMAGE_SIZE,

                IMAGE_SIZE

            )


            music_rects[index] = (
                music_rect
            )


            # =================================================
            # HOVER
            # =================================================

            img, img_rect, profile_size[index] = (
                hover_image_music(

                    profile_image,

                    music_rect,

                    mouse_pos,

                    profile_size[index]

                )
            )


            # =================================================
            # SIDE EFFECT
            # =================================================

            draw_music_side_effect(

                screen,

                img,

                music_rect.centerx,

                music_rect.centery,

                index

            )


            # =================================================
            # NEXT
            # =================================================

            index += 1



































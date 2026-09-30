import pygame
import random
from modules.font import fonts
from modules import typer as TYPER

# =========================================================
# VERTICAL SCROLL GRID
# =========================================================


SCROLL_SPEED = 50
scroll_y = 120
target_scroll_y = 120
punch_hidden_duration = 1000
SCROLL_SPEED = 350
SCROLL_SMOOTH = 0.08
# =========================================================
# RESET SCROLL
# =========================================================

def reset_scroll():

    global scroll_y

    scroll_y = 0


# =========================================================
# EVENT
# =========================================================
def event_vertical_scroll(event, screen,game_mode_feature):

    global target_scroll_y
    if event.type == pygame.MOUSEWHEEL:

        target_scroll_y += (
            -event.y
            * 60
        )

        # =================================================
        # CALCULATE MAX SCROLL
        # =================================================

        cols = 3
        if game_mode_feature == "math":
            card_gap_y = 104
        if game_mode_feature == "detection":
            card_gap_y = 154
        if game_mode_feature == "fast":
            card_gap_y = 83
        if game_mode_feature == "memory":
            card_gap_y = 129
        if game_mode_feature == "logic":
            card_gap_y = 154

        screen_height = screen.get_height()

        rows = (
            (60 + cols - 1)
            // cols
        )

        content_height = (
            rows * card_gap_y
        )

        max_scroll = max(
            0,
            content_height
            - screen_height
            + 100
        )

        # =================================================
        # LIMIT TARGET
        # =================================================

        target_scroll_y = max(
            -max_scroll,
            min(
                120,
                target_scroll_y
            )
        )
            
            
def update_vertical_scroll():

    global scroll_y
    global target_scroll_y

    scroll_y += (
        target_scroll_y
        - scroll_y
    ) * SCROLL_SMOOTH   
# =========================================================
# DRAW
# =========================================================
# =========================================================
# PUNCH EFFECT
# =========================================================

punch_index = []
punch_start_time = pygame.time.get_ticks()

punch_grow_duration = 100
punch_fade_duration = 250
punch_zoom_in_duration = 300
punch_wait_duration = 300

punch_scale = 1.5

yx=420

# شش  تا عکس برای مود گیم 
base_game_mode = pygame.transform.smoothscale(pygame.image.load("./asset/image/game_mode_window.png").convert_alpha(),(yx,yx))
base_game_mode_lock = pygame.transform.smoothscale(pygame.transform.grayscale(pygame.image.load("./asset/image/game_mode_window.png").convert_alpha()),(yx,yx))

# badge_fast_page=[
    
# ]
# badge_memory_page=[
    
# ]
# badge_logic_page=[
    
# ]
# badge_detection_page=[
    
# ]
# badge_math_page=[
    
# ]

badge_index=[
    "free",
    "free",
    "free",
    "free",
    "free",
    "free",
    "free",
    "free",
    "free",
    "free",
    
    "premium",
    "premium",
    "premium",
    "premium",
    "premium",
    
    "premium",
    "premium",
    "premium",
    "premium",
    "premium",
    
    "premium",
    "premium",
    "premium",
    "premium",
    "premium",
    
    "premium",
    "premium",
    "premium",
    "premium",
    "premium",
    
    "premium",
    "premium",
    "premium",
    "premium",
    "premium",
    
    "premium",
    "premium",
    "premium",
    "premium",
    "premium",
    
    "lock",
    "lock",
    "lock",
    "lock",
    "lock",
    
    "lock",
    "lock",
    "lock",
    "lock",
    "lock",
    
    "lock",
    "lock",
    "lock",
    "lock",
    "lock",
    
    "lock",
    "lock",
    "lock",
    "lock",
    "lock",
    
    
]
badge_image=[
    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/free.png").convert_alpha(),
        (70,70)
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/premium.png").convert_alpha(),
        (70,70)
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/upcoming.png").convert_alpha(),
        (70,70)
    ),

]

loccck=pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/lock.png").convert_alpha(),
        (300,300)
    )
GAME_MODE_60_IMAGE_RECT_FAST=[]
GAME_MODE_60_IMAGE_RECT_LOGIC=[]
GAME_MODE_60_IMAGE_RECT_MATH=[]
GAME_MODE_60_IMAGE_RECT_MEMORY=[]
GAME_MODE_60_IMAGE_RECT_DETECTION=[]



grid_zoom_start_time = None
grid_zoom_duration = 350
grid_zoom_start_scale = 0.3
def draw_vertical_scroll_grid(
    screen,
    center_image,
    mode,
    number,
    current_width,
    current_height,
    game_name,
    card_gap_x=500,
    card_gap_y=500
):
    number = number + 5

    global scroll_y
    global punch_index
    global punch_start_time
    global grid_zoom_start_time
    global GAME_MODE_60_IMAGE_RECT

    screen_width = screen.get_width()
    screen_height = screen.get_height()

    cols = 3

    center_x = screen_width // 2 + 30
    center_y = screen_height // 2

    total_width = 2 * card_gap_x

    start_x = (
        center_x
        - total_width // 2
    )

    start_y = (
        center_y
        - card_gap_y // 2
        + scroll_y
    )

    now = pygame.time.get_ticks()

    elapsed = (
        now
        - punch_start_time
    )

    # =====================================================
    # PAGE ENTER ZOOM
    # =====================================================

    if grid_zoom_start_time is None:
        grid_zoom_start_time = now

    zoom_elapsed = (
        now
        - grid_zoom_start_time
    )

    zoom_progress = min(
        zoom_elapsed / grid_zoom_duration,
        1.0
    )

    # Ease Out
    zoom_progress = 1 - (
        1 - zoom_progress
    ) ** 3

    grid_scale = (
        grid_zoom_start_scale
        + (
            1
            - grid_zoom_start_scale
        ) * zoom_progress
    )

    # =====================================================
    # CLEAR RECT LISTS
    # =====================================================

    GAME_MODE_60_IMAGE_RECT_FAST.clear()
    GAME_MODE_60_IMAGE_RECT_LOGIC.clear()
    GAME_MODE_60_IMAGE_RECT_MATH.clear()
    GAME_MODE_60_IMAGE_RECT_MEMORY.clear()
    GAME_MODE_60_IMAGE_RECT_DETECTION.clear()

    # =====================================================
    # TITLE
    # =====================================================
    title_y = (
        current_height // 2
        - 600
        + scroll_y
    )

    if mode == "math":

        title = "MATH"

    elif mode == "memory":

        title = "MEMORY"

    elif mode == "logic":

        title = "LOGIC"

    elif mode == "fast":

        title = "FAST"

    elif mode == "detection":

        title = "DETECTION"

    else:

        title = ""

    if title:

        TYPER.draw_typing_text(
            screen,
            title,
            fonts["heart"],
            (255, 140, 30),
            (
                current_width // 2,
                title_y
            ),
            80
        )

    # =====================================================
    # DRAW CARDS
    # =====================================================

    for i in range(number):

        # =================================================
        # IMAGE / CENTER IMAGE
        # =================================================

        if i >= number - 5:

            center_ = loccck
            images = base_game_mode_lock

        else:

            center_ = center_image[i]
            images = base_game_mode

        # =================================================
        # BADGE
        # =================================================

        if i == 0 or i == 1:

            badge = badge_image[0]

        elif i >= number - 5:

            badge = badge_image[2]

        else:

            badge = badge_image[1]

        # =================================================
        # POSITION
        # =================================================

        row = i // cols
        col = i % cols

        x = (
            start_x
            + col * card_gap_x
        )

        y = (
            start_y
            + row * card_gap_y
        )

        # =================================================
        # FRAME RECT
        # =================================================

        rect = images.get_rect(
            center=(x, y)
        )

        # =================================================
        # CENTER IMAGE
        # =================================================

        draw_center_image = center_

        draw_center_rect = center_.get_rect(
            center=(x, y)
        )

        # ---------------------------------------------
        # 3. ZOOM IN
        # ---------------------------------------------

        if elapsed < (
            punch_grow_duration
            + punch_fade_duration
            + punch_hidden_duration
            + punch_zoom_in_duration
        ):

            progress = (
                elapsed
                - punch_grow_duration
                - punch_fade_duration
                - punch_hidden_duration
            ) / punch_zoom_in_duration

            scale = progress

            alpha = int(
                255
                * progress
            )

        # ---------------------------------------------
        # 4. NORMAL
        # ---------------------------------------------

        else:

            scale = 1
            alpha = 255

        # =================================================
        # SCALE CENTER IMAGE
        # =================================================

        center_width = max(
            1,
            int(
                center_.get_width()
                * scale
            )
        )

        center_height = max(
            1,
            int(
                center_.get_height()
                * scale
            )
        )

        draw_center_image = (
            pygame.transform.smoothscale(
                center_,
                (
                    center_width,
                    center_height
                )
            )
        )

        draw_center_image.set_alpha(
            alpha
        )

        draw_center_rect = (
            draw_center_image.get_rect(
                center=(x, y)
            )
        )

        # =================================================
        # SAVE RECT
        # =================================================
        text=None
        if mode == "math":

            GAME_MODE_60_IMAGE_RECT_MATH.append(
                rect
            )
            if i < number - 5:
                text = fonts["date"].render(
                    game_name[i],
                    True,
                    (255, 140, 30)
                )


    
        elif mode == "memory":

            GAME_MODE_60_IMAGE_RECT_MEMORY.append(
                rect
            )
            if i < number - 5:
                text = fonts["date"].render(
                    game_name[i],
                    True,
                    (255, 140, 30)
                )


        elif mode == "logic":

            GAME_MODE_60_IMAGE_RECT_LOGIC.append(
                rect
            )
            if i < number - 5:
                text = fonts["date"].render(
                    game_name[i],
                    True,
                    (255, 140, 30)
                )


        elif mode == "fast":

            GAME_MODE_60_IMAGE_RECT_FAST.append(
                rect
            )
            if i < number - 5:
                text = fonts["date"].render(
                    game_name[i],
                    True,
                    (255, 140, 30)
                )


        elif mode == "detection":

            GAME_MODE_60_IMAGE_RECT_DETECTION.append(
                rect
            )
            if i < number - 5:
                text = fonts["date"].render(
                    game_name[i],
                    True,
                    (255, 140, 30)
                )




        # =================================================
        # VISIBILITY
        # =================================================

        if (
            rect.bottom < 0
            or rect.top > screen_height
        ):
            continue

        # =================================================
        # PAGE ENTER ZOOM — FRAME
        # =================================================

        if grid_scale < 1.0:

            width = max(
                1,
                int(
                    images.get_width()
                    * grid_scale
                )
            )

            height = max(
                1,
                int(
                    images.get_height()
                    * grid_scale
                )
            )

            zoom_image = (
                pygame.transform.smoothscale(
                    images,
                    (
                        width,
                        height
                    )
                )
            )

            zoom_rect = (
                zoom_image.get_rect(
                    center=rect.center
                )
            )

            screen.blit(
                zoom_image,
                zoom_rect
            )

        else:

            screen.blit(
                images,
                rect
            )


        # TEXT
        if text is not None:

            text_rect = text.get_rect(
                midtop=(
                    rect.centerx,
                    rect.bottom + 40
                )
            )

            screen.blit(
                text,
                text_rect
            )
        # =================================================
        # PAGE ENTER ZOOM — CENTER IMAGE
        # =================================================

        if grid_scale < 1.0:

            width = max(
                1,
                int(
                    draw_center_image.get_width()
                    * grid_scale
                )
            )

            height = max(
                1,
                int(
                    draw_center_image.get_height()
                    * grid_scale
                )
            )

            zoom_center = (
                pygame.transform.smoothscale(
                    draw_center_image,
                    (
                        width,
                        height
                    )
                )
            )

            zoom_center_rect = (
                zoom_center.get_rect(
                    center=draw_center_rect.center
                )
            )

            screen.blit(
                zoom_center,
                zoom_center_rect
            )

        else:

            screen.blit(
                draw_center_image,
                draw_center_rect
            )

        # =================================================
        # BADGE
        # =================================================

        badge_rect = badge.get_rect(
            topright=(
                rect.right + 20,
                rect.top + 20
            )
        )

        screen.blit(
            badge,
            badge_rect
        )
        

        
        
        
def reset_grid_for_game_mode_zoom_in_effect_zoom():

    global grid_zoom_start_time

    grid_zoom_start_time = pygame.time.get_ticks()
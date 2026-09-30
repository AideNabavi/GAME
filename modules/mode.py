import pygame
import random


# =========================================================
# GAME MODE TEXT
# =========================================================

def draw_game_mode_text(
    screen,
    rects,
    texts,
    font,
    text_start_index=None,
    color=(245, 215, 160),
    offset_y=19
):

    # اگر ایندکس None باشد، متن رسم نمی‌شود
    if text_start_index is None:
        return

    for i, rect in enumerate(rects):

        text_index = (
            text_start_index
            + i
        )

        # جلوگیری از خارج شدن از لیست
        if text_index >= len(texts):
            continue

        text_surface = font.render(
            texts[text_index],
            True,
            color
        )

        text_rect = text_surface.get_rect(
            midtop=(
                rect.centerx,
                rect.bottom + offset_y
            )
        )

        screen.blit(
            text_surface,
            text_rect
        )

# =========================================================
# GAME MODE PAGES
# =========================================================

current_page_GAME_MODE = 0

page_active = None





# =========================================================
# CENTER IMAGE CACHE
# =========================================================

center_image_cache_yes = {}


def get_center_image_cached(
    image,
    size
):

    key = (
        id(image),
        size
    )

    cached = center_image_cache_yes.get(key)

    if cached is None:

        cached = pygame.transform.smoothscale(
            image,
            (
                size,
                size
            )
        )

        center_image_cache_yes[key] = cached

    return cached


# =========================================================
# HOVER IMAGE CACHE
# =========================================================

_hover_image_cache = {}


def hover_image_level_cached(
    image,
    rect,
    mouse_pos,
    current_size
):

    # -----------------------------------------------------
    # CARD SIZE
    # -----------------------------------------------------

    NORMAL_SIZE = 420
    HOVER_SIZE = 440

    # -----------------------------------------------------
    # HOVER SMOOTHNESS
    # -----------------------------------------------------

    SMOOTH = 0.2

    # -----------------------------------------------------
    # TARGET SIZE
    # -----------------------------------------------------

    if rect.collidepoint(mouse_pos):

        target = HOVER_SIZE

    else:

        target = NORMAL_SIZE

    # -----------------------------------------------------
    # SMOOTH ANIMATION
    # -----------------------------------------------------

    current_size += (
        target - current_size
    ) * SMOOTH

    # -----------------------------------------------------
    # SNAP TO TARGET
    # -----------------------------------------------------

    if abs(target - current_size) < 0.05:

        current_size = target

    # -----------------------------------------------------
    # INTEGER SIZE
    # -----------------------------------------------------

    size = int(current_size)

    # -----------------------------------------------------
    # CACHE
    # -----------------------------------------------------

    key = (
        id(image),
        size
    )

    new_image = _hover_image_cache.get(key)

    if new_image is None:

        new_image = pygame.transform.smoothscale(
            image,
            (
                size,
                size
            )
        )

        _hover_image_cache[key] = new_image

    # -----------------------------------------------------
    # CENTER IMAGE
    # -----------------------------------------------------

    new_rect = new_image.get_rect(
        center=rect.center
    )

    return (
        new_image,
        new_rect,
        current_size
    )


# =========================================================
# GRAYSCALE CACHE
# =========================================================

_grayscale_image_cache = {}


def get_grayscale_cached(image):

    key = id(image)

    cached = _grayscale_image_cache.get(
        key
    )

    if cached is None:

        cached = pygame.transform.grayscale(
            image
        )

        _grayscale_image_cache[key] = cached

    return cached


# =========================================================
# OVERLAY CACHE
# =========================================================

_overlay_image_cache = {}


def get_overlay_cached(
    image,
    width,
    height
):

    key = (
        id(image),
        width,
        height
    )

    cached = _overlay_image_cache.get(
        key
    )

    if cached is None:

        cached = pygame.transform.smoothscale(
            image,
            (
                width,
                height
            )
        )

        _overlay_image_cache[key] = cached

    return cached


























memory = pygame.image.load(
    "./asset/image/feature/memory.png"
).convert_alpha()
fast = pygame.image.load(
    "./asset/image/feature/fast.png"
).convert_alpha()
logic = pygame.image.load(
    "./asset/image/feature/logic.png"
).convert_alpha()
detection = pygame.image.load(
    "./asset/image/feature/detection.png"
).convert_alpha()
math = pygame.image.load(
    "./asset/image/feature/math.png"
).convert_alpha()







feature_badge_images = [
    None,
    None,
    None,
    None,
    None,
    None
]

def draw_game_feature(
    screen,
    badge_images,
    card_rects,
    badge_size=60,
    offset_x=10,
    offset_y=10
):

    badge_rects = []

    for i, card_rect in enumerate(card_rects):

        # ---------------------------------------------
        # اگر Badge نداریم
        # ---------------------------------------------

        if (
            badge_images is None
            or i >= len(badge_images)
            or badge_images[i] is None
        ):

            badge_rects.append(None)
            continue

        badge_image = badge_images[i]

        # ---------------------------------------------
        # CACHE SCALE
        # ---------------------------------------------

        badge_image = get_badge_cached(
            badge_image,
            badge_size
        )

        # ---------------------------------------------
        # TOP RIGHT
        # ---------------------------------------------

        badge_rect = badge_image.get_rect(
            top=card_rect.top + offset_y,
            right=card_rect.right - offset_x
        )

        # ---------------------------------------------
        # DRAW
        # ---------------------------------------------

        screen.blit(
            badge_image,
            badge_rect
        )

        # ---------------------------------------------
        # SAVE RECT
        # ---------------------------------------------

        badge_rects.append(
            badge_rect
        )

    return badge_rects








# این برای  اضافه کردن عکس برای پرمیوم و آزاد است 
def draw_game_badges(
    screen,
    badge_images,
    card_rects,
    badge_size=60,
    offset_x=10,
    offset_y=10
):

    badge_rects = []

    for i, card_rect in enumerate(card_rects):

        # ---------------------------------------------
        # اگر Badge نداریم
        # ---------------------------------------------

        if (
            badge_images is None
            or i >= len(badge_images)
            or badge_images[i] is None
        ):

            badge_rects.append(None)
            continue

        badge_image = badge_images[i]

        # ---------------------------------------------
        # CACHE SCALE
        # ---------------------------------------------

        badge_image = get_badge_cached(
            badge_image,
            badge_size
        )

        # ---------------------------------------------
        # TOP RIGHT
        # ---------------------------------------------

        badge_rect = badge_image.get_rect(
            top=card_rect.top + offset_y,
            right=card_rect.right - offset_x
        )

        # ---------------------------------------------
        # DRAW
        # ---------------------------------------------

        screen.blit(
            badge_image,
            badge_rect
        )

        # ---------------------------------------------
        # SAVE RECT
        # ---------------------------------------------

        badge_rects.append(
            badge_rect
        )

    return badge_rects







badge_cache = {}

def get_badge_cached(badge_image, size):

    key = (
        id(badge_image),
        size
    )

    if key not in badge_cache:

        badge_cache[key] = pygame.transform.smoothscale(
            badge_image,
            (size, size)
        )

    return badge_cache[key]
# این برای ایکون پرمیوم و آزاد است 
pr_BG = pygame.image.load(
    "./asset/image/premium.png"
).convert_alpha()
cm_BG = pygame.image.load(
    "./asset/image/upcoming.png"
).convert_alpha()

fr_BG = pygame.image.load(
    "./asset/image/free.png"
).convert_alpha()

badge_images = [
    None,
    None,
    None,
    None,
    None,
    None
]















# =========================================================
# DRAW GAME MODE PAGE
# =========================================================
def draw_game_mode_page(
    screen,
    images,
    image_sizes,
    gap_x,
    gap_y,
    page_offset=0,
    center_images=None,
    center_start_index=None,
    overlay_images=None,
    
    badge_images=None,
    feature_badge_images=None,
        
    center_size=250,
    hover=True,
    grayscale_overlay=True
):

    # -----------------------------------------------------
    # MOUSE
    # -----------------------------------------------------

    mouse_pos = pygame.mouse.get_pos()

    # -----------------------------------------------------
    # RECT LIST
    # -----------------------------------------------------

    rects = []

    # -----------------------------------------------------
    # GRID
    # -----------------------------------------------------

    cols = 3
    rows = 2

    # -----------------------------------------------------
    # TOTAL GRID SIZE
    # -----------------------------------------------------

    total_width = (
        (cols - 1)
        * gap_x
    )

    total_height = (
        (rows - 1)
        * gap_y
    )

    # -----------------------------------------------------
    # SCREEN CENTER
    # -----------------------------------------------------

    center_x = (
        screen.get_width()
        // 2
    )

    center_y = (
        screen.get_height()
        // 2
    )

    # -----------------------------------------------------
    # START POSITION
    # -----------------------------------------------------

    start_x = (
        center_x
        - total_width // 2
        + page_offset
    )

    start_y = (
        center_y
        - total_height // 2
        + 20
    )

    # =====================================================
    # DRAW CARDS
    # =====================================================

    for i, img in enumerate(images):

        # -------------------------------------------------
        # ROW / COLUMN
        # -------------------------------------------------

        row = i // cols
        col = i % cols

        # -------------------------------------------------
        # POSITION
        # -------------------------------------------------

        x = (
            start_x
            + col * gap_x
        )

        y = (
            start_y
            + row * gap_y
        )

        # -------------------------------------------------
        # BASE RECT
        # -------------------------------------------------

        base_rect = img.get_rect(
            center=(
                x,
                y
            )
        )

        # =================================================
        # HOVER
        # =================================================

        if hover:

            (
                new_img,
                new_rect,
                image_sizes[i]
            ) = hover_image_level_cached(
                img,
                base_rect,
                mouse_pos,
                image_sizes[i]
            )

        else:

            new_img = img

            new_rect = base_rect

        # =================================================
        # OVERLAY CHECK
        # =================================================

        has_overlay = (
            overlay_images is not None
            and i < len(overlay_images)
            and overlay_images[i] is not None
        )

        # =================================================
        # DRAW CARD
        # =================================================

        if has_overlay:

            overlay = overlay_images[i]

            # ---------------------------------------------
            # GRAYSCALE
            # ---------------------------------------------

            if grayscale_overlay:

                new_img = get_grayscale_cached(
                    new_img
                )

            # ---------------------------------------------
            # DRAW CARD
            # ---------------------------------------------

            screen.blit(
                new_img,
                new_rect
            )

            # ---------------------------------------------
            # CARD SCALE
            # ---------------------------------------------

            scale = (
                new_img.get_width()
                / img.get_width()
            )

            # ---------------------------------------------
            # OVERLAY SIZE
            # ---------------------------------------------

            overlay_width = max(
                1,
                int(
                    overlay.get_width()
                    * scale
                )
            )

            overlay_height = max(
                1,
                int(
                    overlay.get_height()
                    * scale
                )
            )

            # ---------------------------------------------
            # GET CACHED OVERLAY
            # ---------------------------------------------

            overlay_image = get_overlay_cached(
                overlay,
                overlay_width,
                overlay_height
            )

            # ---------------------------------------------
            # CENTER OVERLAY
            # ---------------------------------------------

            overlay_rect = overlay_image.get_rect(
                center=new_rect.center
            )

            # ---------------------------------------------
            # DRAW OVERLAY
            # ---------------------------------------------

            screen.blit(
                overlay_image,
                overlay_rect
            )

        else:

            # ---------------------------------------------
            # NORMAL CARD
            # ---------------------------------------------

            screen.blit(
                new_img,
                new_rect
            )

        # =================================================
        # CENTER IMAGE
        # =================================================
        # =================================================
        # CENTER IMAGE
        # =================================================

        if (
            center_images is not None
            and center_start_index is not None
            and center_start_index + i < len(center_images)
            and center_images[center_start_index + i] is not None
            and not has_overlay
        ):

            center_image = center_images[
                center_start_index + i
            ]

            # ---------------------------------------------
            # HOVER PROGRESS
            # ---------------------------------------------

            center_progress = (
                image_sizes[i] - 420
            ) / 50

            center_progress = max(
                0.0,
                min(
                    1.0,
                    center_progress
                )
            )

            # ---------------------------------------------
            # CENTER SIZE
            # ---------------------------------------------

            new_center_size = int(
                center_size
                + (
                    50
                    * center_progress
                )
            )

            # =================================================
            # PUNCH
            # =================================================

            punch_scale = 1.0

            if i == center_punch_index:

                punch_scale = center_punch_scale

            # ---------------------------------------------
            # APPLY PUNCH
            # ---------------------------------------------

            new_center_size = int(
                new_center_size
                * punch_scale
            )

            # ---------------------------------------------
            # SAFETY
            # ---------------------------------------------

            new_center_size = max(
                1,
                new_center_size
            )

            # ---------------------------------------------
            # GET CENTER IMAGE FROM CACHE
            # ---------------------------------------------

            center_image_scaled = (
                get_center_image_cached(
                    center_image,
                    new_center_size
                )
            )

            # ---------------------------------------------
            # CENTER RECT
            # ---------------------------------------------

            center_rect = (
                center_image_scaled.get_rect(
                    center=new_rect.center
                )
            )

            # ---------------------------------------------
            # DRAW CENTER IMAGE
            # ---------------------------------------------

            screen.blit(
                center_image_scaled,
                center_rect
            )

        # =================================================
        # SAVE RECT
        # =================================================

        rects.append(
            new_rect
        )
    # =====================================================
    # DRAW BADGES
    # =====================================================

    premium_rects = draw_game_badges(
        screen,
        badge_images,
        rects,
        badge_size=60,
        offset_x=10,
        offset_y=10
    )
    
    feature_rects = draw_game_feature(
        screen,
        feature_badge_images,
        rects,
        badge_size=60,
        offset_x=360,
        offset_y=10
    )
    # =====================================================
    # RETURN
    # =====================================================

    return (
        rects,
        premium_rects,
        feature_rects,
        image_sizes
    )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# =========================================================
# CENTER IMAGE PUNCH SYSTEM
# =========================================================

center_punch_order = list(
    range(6)
)

random.shuffle(
    center_punch_order
)

center_punch_position = 0

center_punch_timer = (
    pygame.time.get_ticks()
)

center_punch_index = (
    center_punch_order[0]
)

center_punch_start = (
    pygame.time.get_ticks()
)

center_punch_duration = 0.35

center_punch_scale = 2


# =========================================================
# UPDATE CENTER PUNCH
# =========================================================

def update_center_images_punch():

    global center_punch_order
    global center_punch_position
    global center_punch_timer
    global center_punch_index
    global center_punch_start
    global center_punch_scale

    current_time = (
        pygame.time.get_ticks()
    )

    # =====================================================
    # NEXT CENTER IMAGE
    # =====================================================

    if (
        current_time
        - center_punch_timer
        >= 1000
    ):

        center_punch_timer = (
            current_time
        )

        center_punch_position += 1

        # ---------------------------------------------
        # NEW ROUND
        # ---------------------------------------------

        if center_punch_position >= 6:

            center_punch_position = 0

            center_punch_order = list(
                range(6)
            )

            random.shuffle(
                center_punch_order
            )

        # ---------------------------------------------
        # NEW INDEX
        # ---------------------------------------------

        center_punch_index = (
            center_punch_order[
                center_punch_position
            ]
        )

        # ---------------------------------------------
        # START PUNCH
        # ---------------------------------------------

        center_punch_start = (
            current_time
        )

    # =====================================================
    # PUNCH PROGRESS
    # =====================================================

    elapsed = (
        current_time
        - center_punch_start
    )

    progress = (
        elapsed
        / (
            center_punch_duration
            * 1000
        )
    )

    # =====================================================
    # PUNCH FINISHED
    # =====================================================

    if progress >= 1.0:

        center_punch_scale = 1.0

        return

    # =====================================================
    # PUNCH ANIMATION
    # =====================================================

    if progress < 0.35:

        t = (
            progress
            / 0.35
        )

        center_punch_scale = (
            1.0
            + (
                0.60
                * t
            )
        )

    elif progress < 0.60:

        t = (
            progress
            - 0.35
        ) / 0.25

        center_punch_scale = (
            1.25
            - (
                0.17
                * t
            )
        )

    else:

        t = (
            progress
            - 0.60
        ) / 0.40

        center_punch_scale = (
            1.08
            - (
                0.08
                * t
            )
        )




from modules.game_list import *




# game_names=[
#     game_1_1,
#     game_1_2,
#     game_1_3,
#     game_1_4,
#     game_1_5,
#     game_1_6,
    
#     game_2_1,
#     game_2_2,
#     game_2_3,
#     game_2_4,
#     game_2_5,
#     game_2_6,
    
#     game_3_1,
#     game_3_2,
#     game_3_3,
#     game_3_4,
#     game_3_5,
#     game_3_6,
    
#     game_4_1,
#     game_4_2,
#     game_4_3,
#     game_4_4,
#     game_4_5,
#     game_4_6,
    
#     game_5_1,
#     game_5_2,
#     game_5_3,
#     game_5_4,
#     game_5_5,
#     game_5_6,
    
#     game_6_1,
#     game_6_2,
#     game_6_3,
#     game_6_4,
#     game_6_5,
#     game_6_6,
    
#     game_7_1,
#     game_7_2,
#     game_7_3,
#     game_7_4
#     # game_1_5,
#     # game_1_6,
# ]
# #------------------------------------------------------ عکس نوع بازی 
# #page 1
# center_images_MODE=[
#     pygame.image.load(f"./asset/image/MODE/{game_1_1}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_1_2}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_1_3}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_1_4}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_1_5}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_1_6}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_2_1}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_2_2}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_2_3}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_2_4}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_2_5}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_2_6}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_3_1}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_3_2}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_3_3}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_3_4}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_3_5}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_3_6}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_4_1}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_4_2}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_4_3}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_4_4}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_4_5}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_4_6}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_5_1}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_5_2}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_5_3}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_5_4}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_5_5}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_5_6}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_6_1}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_6_2}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_6_3}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_6_4}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_6_5}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_6_6}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_7_1}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_7_2}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_7_3}.png").convert_alpha(),
#     pygame.image.load(f"./asset/image/MODE/{game_7_4}.png").convert_alpha()
#     # pygame.image.load(f"./asset/image/MODE/{game_7_5}.png").convert_alpha(),
#     # pygame.image.load(f"./asset/image/MODE/{game_7_6}.png").convert_alpha(),
# ]



yx=420
#------------------------------------------------------ عکس قاب  بازی 

# شش  تا عکس برای مود گیم 
# images_MODE_page1 = [
#     pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/MODE/2.png").convert_alpha(),
#         (yx,yx)
#     ),
#     pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/MODE/3.png").convert_alpha(),
#         (yx,yx)
#     ),
#     pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/MODE/12.png").convert_alpha(),
#         (yx,yx)
#     ),
#     pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/MODE/15.png").convert_alpha(),
#         (yx,yx)
#     ),
#     pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/MODE/13.png").convert_alpha(),
#         (yx,yx)
#     ),
#     pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/MODE/7.png").convert_alpha(),
#         (yx,yx)
#     )
# ]


# images_MODE_page2 = [
#     pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/MODE/10.png").convert_alpha(),
#         (yx,yx)
#     ),
#     pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/MODE/1.png").convert_alpha(),
#         (yx,yx)
#     ),
#     pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/MODE/14.png").convert_alpha(),
#         (yx,yx)
#     ),
#     pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/MODE/2.png").convert_alpha(),
#         (yx,yx)
#     ),
#     pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/MODE/5.png").convert_alpha(),
#         (yx,yx)
#     ),
#     pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/MODE/12.png").convert_alpha(),
#         (yx,yx)
#     )
# ]
# images_MODE_page3 = [
#     pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/MODE/4.png").convert_alpha(),
#         (yx,yx)
#     ),
#     pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/MODE/13.png").convert_alpha(),
#         (yx,yx)
#     ),
#     pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/MODE/8.png").convert_alpha(),
#         (yx,yx)
#     ),
#     pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/MODE/12.png").convert_alpha(),
#         (yx,yx)
#     ),
#     pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/MODE/1.png").convert_alpha(),
#         (yx,yx)
#     ),
#     pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/MODE/14.png").convert_alpha(),
#         (yx,yx)
#     )
# ]

# images_MODE_page4 = [
#     pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/MODE/10.png").convert_alpha(),
#         (yx,yx)
#     ),
#     pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/MODE/15.png").convert_alpha(),
#         (yx,yx)
#     ),
#     pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/MODE/8.png").convert_alpha(),
#         (yx,yx)
#     ),
#     pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/MODE/9.png").convert_alpha(),
#         (yx,yx)
#     ),
#     pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/MODE/1.png").convert_alpha(),
#         (yx,yx)
#     ),
#     pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/MODE/14.png").convert_alpha(),
#         (yx,yx)
#     )
# ]





#------------------------------------------------------  



image_sizes_page = [420,420,420,420,420,420]

#rect
image_game_mode_page1 = []
image_game_mode_page2 = []
image_game_mode_page3 = []
image_game_mode_page4 = []
image_game_mode_page5 = []
image_game_mode_page6 = []
image_game_mode_page7 = []
image_game_mode_page8 = []
image_game_mode_page9 = []
image_game_mode_page10 = []



my_icon = pygame.image.load(
    "./asset/image/Lock.png"
).convert_alpha()


my_icon = pygame.transform.smoothscale(
    my_icon,
    (300,300)
)

icons = [
    None,
    None,
    None,
    None,
    None,
    None
]


































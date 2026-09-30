import pygame


# ============================================================
# PUNCH IMAGES
# ============================================================

punch_daily = pygame.image.load(
    "./asset/image/daily__.png"
).convert_alpha()

punch_status = pygame.image.load(
    "./asset/image/status__.png"
).convert_alpha()

punch_daily_for_dahsboard = pygame.image.load(
    "./asset/image/daily__.png"
).convert_alpha()

punch_rank = pygame.image.load(
    "./asset/image/rank__.png"
).convert_alpha()



new_window_for_more_support = pygame.image.load(
    "./asset/image/window_for_more_support.png"
).convert_alpha()


punch_1 = pygame.image.load(
    "./asset/image/game_mode_window.png"
).convert_alpha()

punch_1_1 = pygame.image.load(
    "./asset/image/gamess.png"
).convert_alpha()



punch_2_1 = pygame.image.load(
    "./asset/image/mathh.png"
).convert_alpha()


# ============================================================
# RECT VARIABLES
# ============================================================

# مهم:
# هیچ Rect از قبل ساخته نمی‌شود.
# فقط وقتی تصویر واقعاً draw شود، Rect مقدار می‌گیرد.

punch1_rect = None
punch2_rect = None

IMG1_REC1 = None
IMG1_REC2 = None

strat_rec_ = None

# face__up_rec = None

# level__up = None
# days__up = None

rank__up = None
rank__up2 = None

menu_game = None


rec_support_image0 = None
rec_support_image1 = None
rec_support_image2 = None
rec_support_image3 = None


rec_more_image0 = None
rec_more_image1 = None
rec_more_image2 = None
rec_more_image3 = None


# ============================================================
# POSITIONS
# ============================================================

positions_____1 = None


def current_width_current_height(center_x, center_y):

    global positions_____1

    cx = center_x // 2
    cy = center_y // 2

    # فقط Position
    # اینجا دیگر Rect ساخته نمی‌شود.

    positions_____1 = [
        (cx - 180, cy - 310),
        (cx + 460, cy - 310),
        (cx - 180, cy + 230),
        (cx + 480, cy + 230),
    ]


# ============================================================
# MENU IN GAME
# ============================================================

menu_in_game = pygame.image.load(
    "./asset/image/game_menu_window.png"
).convert_alpha()


# ============================================================
# RANK
# ============================================================

rank__2 = pygame.image.load(
    "./asset/image/index.png"
).convert_alpha()

rank__ = pygame.image.load(
    "./asset/image/index.png"
).convert_alpha()


# ============================================================
# START MENU
# ============================================================

# level__ = pygame.image.load(
#     "./asset/image/DASH/JUNE.png"
# ).convert_alpha()

# days__ = pygame.image.load(
#     "./asset/image/DASH/JUNE.png"
# ).convert_alpha()


# face__up = pygame.image.load(
#     "./asset/image/DASH/JUNE.png"
# ).convert_alpha()


# start___ = pygame.image.load(
#     "./asset/image/button1.png"
# ).convert_alpha()


# ============================================================
# IMAGE
# ============================================================

IMG1 = pygame.image.load(
    "./asset/image/daily_window.png"
).convert_alpha()



# ============================================================
# RESET RECT
# ============================================================

def reset_punch_rects():

    global punch1_rect
    global punch2_rect

    global IMG1_REC1
    global IMG1_REC2

    global strat_rec_

    # global face__up_rec

    # global level__up
    # global days__up

    global rank__up
    global rank__up2

    global menu_game

    global rec_support_image0
    global rec_support_image1
    global rec_support_image2
    global rec_support_image3

    global rec_more_image0
    global rec_more_image1
    global rec_more_image2
    global rec_more_image3

    punch1_rect = None
    punch2_rect = None

    IMG1_REC1 = None
    IMG1_REC2 = None

    strat_rec_ = None

    # face__up_rec = None

    # level__up = None
    # days__up = None

    rank__up = None
    rank__up2 = None

    menu_game = None

    rec_support_image0 = None
    rec_support_image1 = None
    rec_support_image2 = None
    rec_support_image3 = None

    rec_more_image0 = None
    rec_more_image1 = None
    rec_more_image2 = None
    rec_more_image3 = None


# ============================================================
# SAVE RECT
# ============================================================

def _save_punch_rect(page_id, rect):

    global punch1_rect
    global punch2_rect

    global IMG1_REC1
    global IMG1_REC2

    global strat_rec_

    # global face__up_rec

    # global level__up
    # global days__up

    global rank__up
    global rank__up2

    global menu_game

    global rec_support_image0
    global rec_support_image1
    global rec_support_image2
    global rec_support_image3

    global rec_more_image0
    global rec_more_image1
    global rec_more_image2
    global rec_more_image3


    if page_id == "GAME_MODE":

        punch1_rect = rect

    elif page_id == "MATH":

        punch2_rect = rect

    elif page_id == "DAILY_GAME1":

        IMG1_REC1 = rect

    elif page_id == "DAILY_GAME2":

        IMG1_REC2 = rect

    elif page_id == "START":

        strat_rec_ = rect

    # elif page_id == "FACE":

    #     face__up_rec = rect

    # elif page_id == "days":

    #     days__up = rect

    # elif page_id == "level":

    #     level__up = rect

    elif page_id == "rank":

        rank__up = rect

    elif page_id == "rank2":

        rank__up2 = rect

    elif page_id == "menu":

        menu_game = rect

    elif page_id == "SUPPORT1":

        rec_support_image0 = rect

    elif page_id == "SUPPORT2":

        rec_support_image1 = rect

    elif page_id == "SUPPORT3":

        rec_support_image2 = rect

    elif page_id == "SUPPORT4":

        rec_support_image3 = rect

    elif page_id == "MORE1":

        rec_more_image0 = rect

    elif page_id == "MORE2":

        rec_more_image1 = rect

    elif page_id == "MORE3":

        rec_more_image2 = rect

    elif page_id == "MORE4":

        rec_more_image3 = rect


# ============================================================
# PUNCH SCALE
# ============================================================

def _get_punch_scale(
    function,
    page_id,
    duration
):

    now = pygame.time.get_ticks()

    # --------------------------------------------------------
    # Animation Storage
    # --------------------------------------------------------

    if not hasattr(function, "_animations"):

        function._animations = {}

    if page_id not in function._animations:

        function._animations[page_id] = {
            "start_time": now,
            "finished": False
        }

    animation = function._animations[page_id]

    elapsed = now - animation["start_time"]

    # --------------------------------------------------------
    # PUNCH
    # --------------------------------------------------------

    if not animation["finished"]:

        if elapsed >= duration:

            animation["finished"] = True

            scale = 1.0

        else:

            progress = elapsed / duration

            # ------------------------------------------------
            # Grow
            # ------------------------------------------------

            if progress < 0.55:

                p = progress / 0.55

                start = 0.20
                end = 1.12

                p = 1 - (1 - p) ** 4

                scale = start + (
                    end - start
                ) * p

            # ------------------------------------------------
            # Return
            # ------------------------------------------------

            else:

                p = (
                    progress - 0.55
                ) / 0.45

                start = 1.12
                end = 1.0

                p = 1 - (1 - p) ** 3

                scale = start + (
                    end - start
                ) * p

    else:

        scale = 1.0

    return scale


# ============================================================
# DRAW PUNCH IMAGE
# ============================================================

def draw_punch_image(
    screen,
    image,
    center,
    target_size,
    page_id,
    duration=450
):

    # --------------------------------------------------------
    # Scale
    # --------------------------------------------------------

    scale = _get_punch_scale(
        draw_punch_image,
        page_id,
        duration
    )

    # --------------------------------------------------------
    # Size
    # --------------------------------------------------------

    width = max(
        1,
        int(target_size[0] * scale)
    )

    height = max(
        1,
        int(target_size[1] * scale)
    )

    size = (
        width,
        height
    )

    # --------------------------------------------------------
    # Cache
    # --------------------------------------------------------

    if not hasattr(
        draw_punch_image,
        "_image_cache"
    ):

        draw_punch_image._image_cache = {}

    cache = draw_punch_image._image_cache

    cache_key = (
        id(image),
        width,
        height
    )

    if cache_key not in cache:

        cache[cache_key] = pygame.transform.smoothscale(
            image,
            size
        )

    scaled_image = cache[cache_key]

    # --------------------------------------------------------
    # RECT
    # --------------------------------------------------------

    rect = scaled_image.get_rect(
        center=center
    )

    # --------------------------------------------------------
    # SAVE RECT
    # --------------------------------------------------------

    _save_punch_rect(
        page_id,
        rect
    )

    # --------------------------------------------------------
    # DRAW
    # --------------------------------------------------------

    screen.blit(
        scaled_image,
        rect
    )

    return rect


from modules import  language as LANGU

# ============================================================
# DRAW PUNCH IMAGE 2
#
# Main Image
# + Center Image
# + Text
# ============================================================
def draw_punch_image2(
    screen,
    image,
    center,
    target_size,
    page_id,
    duration=450,
    center_image=None,
    center_image_size=None,
    text=None,
    text_font=None,
    text_color=(255, 255, 255)
):

    # ========================================================
    # SCALE
    # ========================================================

    scale = _get_punch_scale(
        draw_punch_image2,
        page_id,
        duration
    )

    # ========================================================
    # MAIN IMAGE SIZE
    # ========================================================

    width = max(
        1,
        int(target_size[0] * scale)
    )

    height = max(
        1,
        int(target_size[1] * scale)
    )

    size = (
        width,
        height
    )

    # ========================================================
    # CACHE
    # ========================================================

    if not hasattr(
        draw_punch_image2,
        "_image_cache"
    ):

        draw_punch_image2._image_cache = {}

    cache = draw_punch_image2._image_cache

    # ========================================================
    # MAIN IMAGE CACHE
    # ========================================================

    cache_key = (
        id(image),
        width,
        height
    )

    if cache_key not in cache:

        cache[cache_key] = pygame.transform.smoothscale(
            image,
            size
        )

    scaled_image = cache[cache_key]

    # ========================================================
    # MAIN RECT
    # ========================================================

    rect = scaled_image.get_rect(
        center=center
    )

    # ========================================================
    # SAVE MAIN RECT
    # ========================================================

    _save_punch_rect(
        page_id,
        rect
    )

    # ========================================================
    # DRAW MAIN IMAGE
    # ========================================================

    screen.blit(
        scaled_image,
        rect
    )

    # ========================================================
    # CENTER IMAGE
    # ========================================================

    if center_image is not None:

        # ----------------------------------------------------
        # CENTER IMAGE SIZE
        # ----------------------------------------------------

        if center_image_size is not None:

            center_original_size = (
                center_image_size
            )

        else:

            center_original_size = (
                center_image.get_size()
            )

        center_width = max(
            1,
            int(
                center_original_size[0]
                * scale
            )
        )

        center_height = max(
            1,
            int(
                center_original_size[1]
                * scale
            )
        )

        center_size = (
            center_width,
            center_height
        )

        # ----------------------------------------------------
        # CENTER CACHE
        # ----------------------------------------------------

        center_cache_key = (
            id(center_image),
            center_width,
            center_height
        )

        if center_cache_key not in cache:

            cache[center_cache_key] = (
                pygame.transform.smoothscale(
                    center_image,
                    center_size
                )
            )

        scaled_center_image = cache[
            center_cache_key
        ]

        # ----------------------------------------------------
        # CENTER RECT
        # ----------------------------------------------------

        center_image_rect = (
            scaled_center_image.get_rect(
                center=(
                    rect.centerx,
                    rect.centery
                    - int(height * 0.01)
                )
            )
        )

        # ----------------------------------------------------
        # DRAW CENTER IMAGE
        # ----------------------------------------------------

        screen.blit(
            scaled_center_image,
            center_image_rect
        )


        text_font = LANGU.get_language_font("support")

    # ========================================================
    # TEXT
    # ========================================================

    if (
        text is not None
        and text_font is not None
    ):
        ttttt=LANGU.display_text(text)
        text_surface = text_font.render(
            str(ttttt),
            True,
            text_color
        )

        text_rect = text_surface.get_rect(
            center=(
                rect.centerx,
                rect.centery
                + int(height * 0.55)
            )
        )

        screen.blit(
            text_surface,
            text_rect
        )

    # ========================================================
    # RETURN
    # ========================================================

    return rect











# ============================================================
# DRAW PUNCH IMAGE 1
#
# Main Image
# + Center Image
# + Text
# + Custom Center Offset
# ============================================================
def draw_punch_image_1(
    screen,
    image,
    center,
    target_size,
    page_id,
    size_,
    duration=450,
    center_image=None,
    center_image_size=None,
    text=None,
    text_font=None,
    text_color=(255, 255, 255)
):

    # ========================================================
    # CACHE STORAGE
    # ========================================================

    if not hasattr(draw_punch_image_1, "_image_cache"):
        draw_punch_image_1._image_cache = {}

    if not hasattr(draw_punch_image_1, "_text_cache"):
        draw_punch_image_1._text_cache = {}

    image_cache = draw_punch_image_1._image_cache
    text_cache = draw_punch_image_1._text_cache

    # ========================================================
    # PUNCH SCALE
    # ========================================================

    scale = _get_punch_scale(
        draw_punch_image_1,
        page_id,
        duration
    )

    # ========================================================
    # MAIN IMAGE SIZE
    # ========================================================

    width = max(
        1,
        int(target_size[0] * scale)
    )

    height = max(
        1,
        int(target_size[1] * scale)
    )

    size = (width, height)

    # ========================================================
    # MAIN IMAGE CACHE
    # ========================================================

    cache_key = (
        id(image),
        width,
        height
    )

    scaled_image = image_cache.get(cache_key)

    if scaled_image is None:

        scaled_image = pygame.transform.smoothscale(
            image,
            size
        )

        image_cache[cache_key] = scaled_image

    # ========================================================
    # MAIN RECT
    # ========================================================

    rect = scaled_image.get_rect(
        center=center
    )

    # ========================================================
    # SAVE RECT
    # ========================================================

    _save_punch_rect(
        page_id,
        rect
    )

    # ========================================================
    # DRAW MAIN IMAGE
    # ========================================================

    screen.blit(
        scaled_image,
        rect
    )

    # ========================================================
    # CENTER IMAGE
    # ========================================================

    if center_image is not None:

        # ----------------------------------------------------
        # ORIGINAL CENTER SIZE
        # ----------------------------------------------------

        if center_image_size is not None:

            original_width = center_image_size[0]
            original_height = center_image_size[1]

        else:

            original_width = center_image.get_width()
            original_height = center_image.get_height()

        # ----------------------------------------------------
        # CENTER IMAGE SIZE
        # ----------------------------------------------------

        center_width = max(
            1,
            int(original_width * scale)
        )

        center_height = max(
            1,
            int(original_height * scale)
        )

        # ----------------------------------------------------
        # CENTER CACHE
        # ----------------------------------------------------

        center_cache_key = (
            id(center_image),
            center_width,
            center_height
        )

        scaled_center_image = image_cache.get(
            center_cache_key
        )

        if scaled_center_image is None:

            scaled_center_image = pygame.transform.smoothscale(
                center_image,
                (
                    center_width,
                    center_height
                )
            )

            image_cache[center_cache_key] = (
                scaled_center_image
            )

        # ----------------------------------------------------
        # CENTER RECT
        # ----------------------------------------------------

        center_image_rect = scaled_center_image.get_rect(
            center=(
                rect.centerx,
                rect.centery
                - int(height * size_)
            )
        )

        # ----------------------------------------------------
        # DRAW CENTER IMAGE
        # ----------------------------------------------------

        screen.blit(
            scaled_center_image,
            center_image_rect
        )

    # ========================================================
    # TEXT
    # ========================================================

    if text and text_font is not None:

        text_key = (
            id(text_font),
            str(text),
            text_color
        )

        text_surface = text_cache.get(
            text_key
        )

        if text_surface is None:

            text_surface = text_font.render(
                str(text),
                True,
                text_color
            )

            text_cache[text_key] = text_surface

        # ----------------------------------------------------
        # TEXT RECT
        # ----------------------------------------------------

        text_rect = text_surface.get_rect(
            center=(
                rect.centerx,
                rect.centery
                + int(height * 0.30)
            )
        )

        # ----------------------------------------------------
        # DRAW TEXT
        # ----------------------------------------------------

        screen.blit(
            text_surface,
            text_rect
        )

    # ========================================================
    # RETURN
    # ========================================================

    return rect










# ============================================================
# RESET PUNCH ANIMATIONS
# ============================================================

def reset_punch_images_animation():

    # --------------------------------------------------------
    # draw_punch_image
    # --------------------------------------------------------

    if hasattr(
        draw_punch_image,
        "_animations"
    ):

        draw_punch_image._animations.clear()

    # --------------------------------------------------------
    # draw_punch_image2
    # --------------------------------------------------------

    if hasattr(
        draw_punch_image2,
        "_animations"
    ):

        draw_punch_image2._animations.clear()

    # --------------------------------------------------------
    # draw_punch_image_1
    # --------------------------------------------------------

    if hasattr(
        draw_punch_image_1,
        "_animations"
    ):

        draw_punch_image_1._animations.clear()


# ============================================================
# RESET EVERYTHING
# ============================================================

def reset_all_punch():

    # Animation
    reset_punch_images_animation()

    # Rect
    reset_punch_rects()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
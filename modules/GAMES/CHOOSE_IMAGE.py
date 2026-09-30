import pygame
import random
import os
from modules.font import *

# =========================================================
# SETTINGS
# =========================================================

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




# IMAGE_FOLDER = "./asset/image/MODE/memory_detect"

BASE_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../.."
    )
)

IMAGE_FOLDER = os.path.join(
    BASE_DIR,
    "asset",
    "image",
    "MODE",
    "memory_detect"
)

print("IMAGE FOLDER:")
print(IMAGE_FOLDER)

FPS = 60

BACKGROUND_COLOR = (25, 25, 30)
CARD_COLOR = (45, 45, 52)
CARD_BORDER = (100, 100, 110)
TEXT_COLOR = (255, 255, 255)
NEW_COLOR = (80, 220, 120)


# =========================================================
# INITIALIZE
# =========================================================

# pygame.init()

# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Memory Detect")

# clock = pygame.time.Clock()

# font = pygame.font.Font(None, 42)
# small_font = pygame.font.Font(None, 30)


# =========================================================
# LOAD IMAGES
# =========================================================

def load_images(folder):

    images = []

    if not os.path.exists(folder):
        print("IMAGE FOLDER NOT FOUND:")
        print(folder)
        return images

    valid_extensions = (
        ".png",
        ".jpg",
        ".jpeg",
        ".webp"
    )

    files = []

    for filename in os.listdir(folder):

        if filename.lower().endswith(valid_extensions):
            files.append(filename)

    for filename in files:

        path = os.path.join(folder, filename)

        try:

            image = pygame.image.load(path).convert_alpha()

            images.append({
                "name": filename,
                "image": image
            })

        except pygame.error:

            print("Could not load:", path)

    return images


all_images = load_images(IMAGE_FOLDER)





zoom_active = False

zoom_phase = "NONE"

zoom_start_time = 0

zoom_out_duration = 250
zoom_pause_duration = 250
zoom_in_duration = 300

zoom_scale = 1.0

pending_next_stage = False



def start_zoom_transition():

    global zoom_active
    global zoom_phase
    global zoom_start_time
    global zoom_scale

    zoom_active = True

    zoom_phase = "OUT"

    zoom_start_time = pygame.time.get_ticks()

    zoom_scale = 1.0
    
    
    
def update_zoom_transition():

    global zoom_active
    global zoom_phase
    global zoom_start_time
    global zoom_scale

    if not zoom_active:
        return

    now = pygame.time.get_ticks()

    elapsed = now - zoom_start_time

    # =========================================
    # ZOOM OUT
    # =========================================

    if zoom_phase == "OUT":

        progress = min(
            elapsed / zoom_out_duration,
            1.0
        )

        # از 1 → 0
        zoom_scale = 1.0 - progress

        if progress >= 1.0:

            zoom_phase = "PAUSE"

            zoom_start_time = now

            zoom_scale = 0.0

    # =========================================
    # PAUSE
    # =========================================

    elif zoom_phase == "PAUSE":

        zoom_scale = 0.0

        if elapsed >= zoom_pause_duration:

            # اینجا مرحله جدید ساخته می‌شود
            next_stage()

            zoom_phase = "IN"

            zoom_start_time = now

            zoom_scale = 0.0

    # =========================================
    # ZOOM IN
    # =========================================

    elif zoom_phase == "IN":

        progress = min(
            elapsed / zoom_in_duration,
            1.0
        )

        zoom_scale = progress

        if progress >= 1.0:

            zoom_scale = 1.0

            zoom_phase = "NONE"

            zoom_active = False
# =========================================================
# GAME VARIABLES
# =========================================================

current_images = []

available_images = []

new_image = None

stage = 1

game_over = False

message = ""

message_timer = 0


# =========================================================
# GET NEW RANDOM IMAGE
# =========================================================

def get_new_image():

    global available_images

    if not available_images:

        # اگر همه عکس‌ها مصرف شدند،
        # دوباره لیست را از اول می‌سازیم
        available_images = all_images.copy()

    image_data = random.choice(available_images)

    available_images.remove(image_data)

    return image_data


# =========================================================
# RESET GAME
# =========================================================

def reset_game():

    global current_images
    global available_images
    global new_image
    global stage
    global game_over
    global message
    global message_timer
    global zoom_active
    global zoom_phase
    global zoom_start_time
    global zoom_scale
    if len(all_images) < 20:

        print(
            "ERROR: At least 10 different images are required."
        )

        return

    available_images = all_images.copy()

    random.shuffle(available_images)

    current_images = []

    # -----------------------------------------
    # مرحله اول
    # 2 عکس
    # -----------------------------------------

    first_image = get_new_image()
    second_image = get_new_image()

    current_images = [
        first_image,
        second_image
    ]

    # در مرحله اول هنوز مفهوم
    # عکس جدید نداریم
    new_image = None

    stage = 1

    game_over = False

    message = ""

    message_timer = 0


# =========================================================
# CREATE NEXT STAGE
# =========================================================
def next_stage():

    global current_images
    global new_image
    global stage

    # تا رسیدن به 20 عکس
    if len(current_images) < 20:

        new_image = get_new_image()

        current_images.append(new_image)

        # عکس جدید می‌تواند هر جایی قرار بگیرد
        random.shuffle(current_images)

        stage += 1

        return

    # از 20 عکس به بعد
    old_image = random.choice(current_images)

    current_images.remove(old_image)

    new_image = get_new_image()

    current_images.append(new_image)

    # تمام عکس‌ها دوباره قاطی شوند
    random.shuffle(current_images)

    stage += 1
# =========================================================
# IMAGE RECTANGLES
# =========================================================
def get_image_rects():

    count = len(current_images)

    if count == 0:
        return []

    rects = []

    # همیشه 5 ستون
    columns = 5

    # تعداد سطرها
    rows = (count + columns - 1) // columns

    # حداکثر 4 سطر
    rows = min(rows, 4)

    gap = 14

    top_space = 105
    bottom_space = 35

    side_space = 50

    available_width = WIDTH - side_space * 2

    available_height = (
        HEIGHT
        - top_space
        - bottom_space
    )

    # -----------------------------------------
    # عرض کارت
    # -----------------------------------------

    card_width = (
        available_width
        - gap * (columns - 1)
    ) // columns

    # -----------------------------------------
    # ارتفاع کارت
    # -----------------------------------------

    card_height = (
        available_height
        - gap * (rows - 1)
    ) // rows

    # -----------------------------------------
    # کارت‌ها مربع باشند
    # -----------------------------------------

    size = min(
        card_width,
        card_height
    )

    # -----------------------------------------
    # کل عرض و ارتفاع
    # -----------------------------------------

    total_width = (
        columns * size
        + (columns - 1) * gap
    )

    total_height = (
        rows * size
        + (rows - 1) * gap
    )

    # -----------------------------------------
    # وسط‌چین
    # -----------------------------------------

    start_x = (
        WIDTH - total_width
    ) // 2

    start_y = (
        top_space
        + (
            available_height
            - total_height
        ) // 2
    )

    # -----------------------------------------
    # ساخت Rect ها
    # -----------------------------------------

    for index in range(count):

        row = index // columns
        column = index % columns

        x = (
            start_x
            + column * (size + gap)
        )

        y = (
            start_y
            + row * (size + gap)
        )

        rect = pygame.Rect(
            x,
            y,
            size,
            size
        )

        rects.append(rect)

    return rects
# =========================================================
# DRAW IMAGE
# =========================================================
def draw_image(image_data, rect, scale_factor=1.0):

    image = image_data["image"]

    image_rect = image.get_rect()

    # -----------------------------------------
    # اندازه اصلی عکس
    # -----------------------------------------

    scale = min(
        rect.width / image_rect.width,
        rect.height / image_rect.height
    )

    width = int(
        image_rect.width
        * scale
        * scale_factor
    )

    height = int(
        image_rect.height
        * scale
        * scale_factor
    )

    # اگر خیلی کوچک شد، رسم نکن
    if width <= 0 or height <= 0:
        return

    scaled_image = pygame.transform.smoothscale(
        image,
        (width, height)
    )

    draw_rect = scaled_image.get_rect(
        center=rect.center
    )

    # -----------------------------------------
    # کارت
    # -----------------------------------------

    # pygame.draw.rect(
    #     screen,
    #     CARD_COLOR,
    #     rect,
    #     border_radius=12
    # )

    # -----------------------------------------
    # عکس
    # -----------------------------------------

    screen.blit(
        scaled_image,
        draw_rect
    )

    # -----------------------------------------
    # Border
    # -----------------------------------------

    # pygame.draw.rect(
    #     screen,
    #     CARD_BORDER,
    #     rect,
    #     width=2,
    #     border_radius=12
    # )

# =========================================================
# DRAW GAME
# =========================================================

def draw_game():

    # screen.fill(BACKGROUND_COLOR)

    # -----------------------------------------
    # TITLE
    # -----------------------------------------

    title = fonts["heart"].render(
        "FIND THE NEW IMAGE",
        True,
        TEXT_COLOR
    )

    title_rect = title.get_rect(
        center=(WIDTH // 2, 35)
    )

    screen.blit(
        title,
        title_rect
    )

    # -----------------------------------------
    # STAGE
    # -----------------------------------------

    stage_text =fonts["heart"].render(
        f"STAGE {stage}    •    {len(current_images)} IMAGES",
        True,
        (190, 190, 190)
    )

    stage_rect = stage_text.get_rect(
        center=(WIDTH // 2, 70)
    )

    screen.blit(
        stage_text,
        stage_rect
    )

    # -----------------------------------------
    # IMAGES
    # -----------------------------------------

    rects = get_image_rects()

    for image_data, rect in zip(
        current_images,
        rects
    ):

        draw_image(
            image_data,
            rect,
            zoom_scale
        )
# =========================================================
# CLICK HANDLER
# =========================================================
def handle_click(mouse_pos):

    global game_over
    global message
    global message_timer

    # هنگام اجرای انیمیشن کلیک جدید نگیریم
    if zoom_active:
        return

    rects = get_image_rects()

    for image_data, rect in zip(
        current_images,
        rects
    ):

        if rect.collidepoint(mouse_pos):

            # =====================================
            # مرحله اول
            # 2 عکس → 3 عکس
            # =====================================

            if new_image is None:

                start_zoom_transition()

                return

            # =====================================
            # مراحل بعدی
            # =====================================

            if image_data is new_image:

                start_zoom_transition()

                message = "CORRECT!"

                message_timer = pygame.time.get_ticks()

            else:

                game_over = True

                message = "WRONG!"

                message_timer = pygame.time.get_ticks()

            return




















def CHOOSE_IMAGE_():
    global message
    update_zoom_transition()
    draw_game()

    # -----------------------------------------
    # MESSAGE
    # -----------------------------------------

    if message:

        elapsed = (
            pygame.time.get_ticks()
            - message_timer
        )

        if elapsed < 700:

            message_surface = fonts["heart"].render(
                message,
                True,
                NEW_COLOR
                if message == "CORRECT!"
                else (230, 80, 80)
            )

            message_rect = message_surface.get_rect(
                center=(WIDTH // 2, HEIGHT - 25)
            )

            screen.blit(
                message_surface,
                message_rect
            )

        else:

            message = ""

    # -----------------------------------------
    # GAME OVER
    # -----------------------------------------

    if game_over:

        overlay = pygame.Surface(
            (WIDTH, HEIGHT),
            pygame.SRCALPHA
        )

        overlay.fill(
            (0, 0, 0, 150)
        )

        screen.blit(
            overlay,
            (0, 0)
        )

        game_over_text = fonts["heart"].render(
            "WRONG!  PRESS R TO RESTART",
            True,
            (255, 255, 255)
        )

        game_over_rect = game_over_text.get_rect(
            center=(
                WIDTH // 2,
                HEIGHT // 2
            )
        )

        screen.blit(
            game_over_text,
            game_over_rect
        )













def event_CHOOSE_IMAGE(event):

    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_ESCAPE:

            running = False

        elif event.key == pygame.K_r:

            reset_game()

    elif event.type == pygame.MOUSEBUTTONDOWN:

        if event.button == 1:

            if game_over:

                reset_game()

            else:

                handle_click(
                    event.pos
                )


# import pygame
# import random
# import os


# # =========================================================
# # SETTINGS
# # =========================================================

# WIDTH = 1080
# HEIGHT = 720

# # IMAGE_FOLDER = "./asset/image/MODE/memory_detect"

# BASE_DIR = os.path.abspath(
#     os.path.join(
#         os.path.dirname(__file__),
#         "../.."
#     )
# )

# IMAGE_FOLDER = os.path.join(
#     BASE_DIR,
#     "asset",
#     "image",
#     "MODE",
#     "memory_detect"
# )

# print("IMAGE FOLDER:")
# print(IMAGE_FOLDER)

# FPS = 60

# BACKGROUND_COLOR = (25, 25, 30)
# CARD_COLOR = (45, 45, 52)
# CARD_BORDER = (100, 100, 110)
# TEXT_COLOR = (255, 255, 255)
# NEW_COLOR = (80, 220, 120)


# # =========================================================
# # INITIALIZE
# # =========================================================

# pygame.init()

# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Memory Detect")

# clock = pygame.time.Clock()

# font = pygame.font.Font(None, 42)
# small_font = pygame.font.Font(None, 30)


# # =========================================================
# # LOAD IMAGES
# # =========================================================

# def load_images(folder):

#     images = []

#     if not os.path.exists(folder):
#         print("IMAGE FOLDER NOT FOUND:")
#         print(folder)
#         return images

#     valid_extensions = (
#         ".png",
#         ".jpg",
#         ".jpeg",
#         ".webp"
#     )

#     files = []

#     for filename in os.listdir(folder):

#         if filename.lower().endswith(valid_extensions):
#             files.append(filename)

#     for filename in files:

#         path = os.path.join(folder, filename)

#         try:

#             image = pygame.image.load(path).convert_alpha()

#             images.append({
#                 "name": filename,
#                 "image": image
#             })

#         except pygame.error:

#             print("Could not load:", path)

#     return images


# all_images = load_images(IMAGE_FOLDER)























# zoom_active = False

# zoom_phase = "NONE"

# zoom_start_time = 0

# zoom_out_duration = 250
# zoom_pause_duration = 250
# zoom_in_duration = 300

# zoom_scale = 1.0

# pending_next_stage = False



# def start_zoom_transition():

#     global zoom_active
#     global zoom_phase
#     global zoom_start_time
#     global zoom_scale

#     zoom_active = True

#     zoom_phase = "OUT"

#     zoom_start_time = pygame.time.get_ticks()

#     zoom_scale = 1.0
    
    
    
# def update_zoom_transition():

#     global zoom_active
#     global zoom_phase
#     global zoom_start_time
#     global zoom_scale

#     if not zoom_active:
#         return

#     now = pygame.time.get_ticks()

#     elapsed = now - zoom_start_time

#     # =========================================
#     # ZOOM OUT
#     # =========================================

#     if zoom_phase == "OUT":

#         progress = min(
#             elapsed / zoom_out_duration,
#             1.0
#         )

#         # از 1 → 0
#         zoom_scale = 1.0 - progress

#         if progress >= 1.0:

#             zoom_phase = "PAUSE"

#             zoom_start_time = now

#             zoom_scale = 0.0

#     # =========================================
#     # PAUSE
#     # =========================================

#     elif zoom_phase == "PAUSE":

#         zoom_scale = 0.0

#         if elapsed >= zoom_pause_duration:

#             # اینجا مرحله جدید ساخته می‌شود
#             next_stage()

#             zoom_phase = "IN"

#             zoom_start_time = now

#             zoom_scale = 0.0

#     # =========================================
#     # ZOOM IN
#     # =========================================

#     elif zoom_phase == "IN":

#         progress = min(
#             elapsed / zoom_in_duration,
#             1.0
#         )

#         zoom_scale = progress

#         if progress >= 1.0:

#             zoom_scale = 1.0

#             zoom_phase = "NONE"

#             zoom_active = False
# # =========================================================
# # GAME VARIABLES
# # =========================================================

# current_images = []

# available_images = []

# new_image = None

# stage = 1

# game_over = False

# message = ""

# message_timer = 0


# # =========================================================
# # GET NEW RANDOM IMAGE
# # =========================================================

# def get_new_image():

#     global available_images

#     if not available_images:

#         # اگر همه عکس‌ها مصرف شدند،
#         # دوباره لیست را از اول می‌سازیم
#         available_images = all_images.copy()

#     image_data = random.choice(available_images)

#     available_images.remove(image_data)

#     return image_data


# # =========================================================
# # RESET GAME
# # =========================================================

# def reset_game():

#     global current_images
#     global available_images
#     global new_image
#     global stage
#     global game_over
#     global message
#     global message_timer

#     if len(all_images) < 10:

#         print(
#             "ERROR: At least 10 different images are required."
#         )

#         return

#     available_images = all_images.copy()

#     random.shuffle(available_images)

#     current_images = []

#     # -----------------------------------------
#     # مرحله اول
#     # 2 عکس
#     # -----------------------------------------

#     first_image = get_new_image()
#     second_image = get_new_image()

#     current_images = [
#         first_image,
#         second_image
#     ]

#     # در مرحله اول هنوز مفهوم
#     # عکس جدید نداریم
#     new_image = None

#     stage = 1

#     game_over = False

#     message = ""

#     message_timer = 0


# # =========================================================
# # CREATE NEXT STAGE
# # =========================================================
# def next_stage():

#     global current_images
#     global new_image
#     global stage

#     # -----------------------------------------
#     # تا رسیدن به 20 عکس
#     # -----------------------------------------

#     if len(current_images) < 20:

#         new_image = get_new_image()

#         current_images.append(
#             new_image
#         )

#         # قاطی کردن جای عکس‌ها
#         random.shuffle(current_images)

#         stage += 1

#         return

#     # -----------------------------------------
#     # بعد از 20 عکس
#     # -----------------------------------------

#     old_image = random.choice(
#         current_images
#     )

#     current_images.remove(
#         old_image
#     )

#     # عکس جدید
#     new_image = get_new_image()

#     current_images.append(
#         new_image
#     )

#     # قاطی کردن تمام عکس‌ها
#     random.shuffle(current_images)

#     stage += 1
#     # -----------------------------------------
#     # بعد از 20 عکس
#     # همیشه 20 عکس
#     # -----------------------------------------

#     old_image = random.choice(
#         current_images
#     )

#     current_images.remove(
#         old_image
#     )

#     new_image = get_new_image()

#     current_images.append(
#         new_image
#     )

#     stage += 1
# # =========================================================
# # IMAGE RECTANGLES
# # =========================================================
# def get_image_rects():

#     count = len(current_images)

#     if count == 0:
#         return []

#     rects = []

#     # همیشه 5 ستون
#     columns = 5

#     # تعداد سطرها
#     rows = (count + columns - 1) // columns

#     # حداکثر 4 سطر
#     rows = min(rows, 4)

#     gap = 14

#     top_space = 105
#     bottom_space = 35

#     side_space = 50

#     available_width = WIDTH - side_space * 2

#     available_height = (
#         HEIGHT
#         - top_space
#         - bottom_space
#     )

#     # -----------------------------------------
#     # عرض کارت
#     # -----------------------------------------

#     card_width = (
#         available_width
#         - gap * (columns - 1)
#     ) // columns

#     # -----------------------------------------
#     # ارتفاع کارت
#     # -----------------------------------------

#     card_height = (
#         available_height
#         - gap * (rows - 1)
#     ) // rows

#     # -----------------------------------------
#     # کارت‌ها مربع باشند
#     # -----------------------------------------

#     size = min(
#         card_width,
#         card_height
#     )

#     # -----------------------------------------
#     # کل عرض و ارتفاع
#     # -----------------------------------------

#     total_width = (
#         columns * size
#         + (columns - 1) * gap
#     )

#     total_height = (
#         rows * size
#         + (rows - 1) * gap
#     )

#     # -----------------------------------------
#     # وسط‌چین
#     # -----------------------------------------

#     start_x = (
#         WIDTH - total_width
#     ) // 2

#     start_y = (
#         top_space
#         + (
#             available_height
#             - total_height
#         ) // 2
#     )

#     # -----------------------------------------
#     # ساخت Rect ها
#     # -----------------------------------------

#     for index in range(count):

#         row = index // columns
#         column = index % columns

#         x = (
#             start_x
#             + column * (size + gap)
#         )

#         y = (
#             start_y
#             + row * (size + gap)
#         )

#         rect = pygame.Rect(
#             x,
#             y,
#             size,
#             size
#         )

#         rects.append(rect)

#     return rects
# # =========================================================
# # DRAW IMAGE
# # =========================================================
# def draw_image(image_data, rect, scale_factor=1.0):

#     image = image_data["image"]

#     image_rect = image.get_rect()

#     # -----------------------------------------
#     # اندازه اصلی عکس
#     # -----------------------------------------

#     scale = min(
#         rect.width / image_rect.width,
#         rect.height / image_rect.height
#     )

#     width = int(
#         image_rect.width
#         * scale
#         * scale_factor
#     )

#     height = int(
#         image_rect.height
#         * scale
#         * scale_factor
#     )

#     # اگر خیلی کوچک شد، رسم نکن
#     if width <= 0 or height <= 0:
#         return

#     scaled_image = pygame.transform.smoothscale(
#         image,
#         (width, height)
#     )

#     draw_rect = scaled_image.get_rect(
#         center=rect.center
#     )

#     # -----------------------------------------
#     # کارت
#     # -----------------------------------------

#     pygame.draw.rect(
#         screen,
#         CARD_COLOR,
#         rect,
#         border_radius=12
#     )

#     # -----------------------------------------
#     # عکس
#     # -----------------------------------------

#     screen.blit(
#         scaled_image,
#         draw_rect
#     )

#     # -----------------------------------------
#     # Border
#     # -----------------------------------------

#     pygame.draw.rect(
#         screen,
#         CARD_BORDER,
#         rect,
#         width=2,
#         border_radius=12
#     )

# # =========================================================
# # DRAW GAME
# # =========================================================

# def draw_game():

#     screen.fill(BACKGROUND_COLOR)

#     # -----------------------------------------
#     # TITLE
#     # -----------------------------------------

#     title = font.render(
#         "FIND THE NEW IMAGE",
#         True,
#         TEXT_COLOR
#     )

#     title_rect = title.get_rect(
#         center=(WIDTH // 2, 35)
#     )

#     screen.blit(
#         title,
#         title_rect
#     )

#     # -----------------------------------------
#     # STAGE
#     # -----------------------------------------

#     stage_text = small_font.render(
#         f"STAGE {stage}    •    {len(current_images)} IMAGES",
#         True,
#         (190, 190, 190)
#     )

#     stage_rect = stage_text.get_rect(
#         center=(WIDTH // 2, 70)
#     )

#     screen.blit(
#         stage_text,
#         stage_rect
#     )

#     # -----------------------------------------
#     # IMAGES
#     # -----------------------------------------

#     rects = get_image_rects()

#     for image_data, rect in zip(
#         current_images,
#         rects
#     ):

#         draw_image(
#             image_data,
#             rect,
#             zoom_scale
#         )
# # =========================================================
# # CLICK HANDLER
# # =========================================================
# def handle_click(mouse_pos):

#     global game_over
#     global message
#     global message_timer

#     # هنگام اجرای انیمیشن کلیک جدید نگیریم
#     if zoom_active:
#         return

#     rects = get_image_rects()

#     for image_data, rect in zip(
#         current_images,
#         rects
#     ):

#         if rect.collidepoint(mouse_pos):

#             # =====================================
#             # مرحله اول
#             # 2 عکس → 3 عکس
#             # =====================================

#             if new_image is None:

#                 start_zoom_transition()

#                 return

#             # =====================================
#             # مراحل بعدی
#             # =====================================

#             if image_data is new_image:

#                 start_zoom_transition()

#                 message = "CORRECT!"

#                 message_timer = pygame.time.get_ticks()

#             else:

#                 game_over = True

#                 message = "WRONG!"

#                 message_timer = pygame.time.get_ticks()

#             return
# # =========================================================
# # START
# # =========================================================

# reset_game()


# # =========================================================
# # MAIN LOOP
# # =========================================================

# running = True

# while running:

#     clock.tick(FPS)

#     # -----------------------------------------
#     # EVENTS
#     # -----------------------------------------

#     for event in pygame.event.get():

#         if event.type == pygame.QUIT:

#             running = False

#         elif event.type == pygame.KEYDOWN:

#             if event.key == pygame.K_ESCAPE:

#                 running = False

#             elif event.key == pygame.K_r:

#                 reset_game()

#         elif event.type == pygame.MOUSEBUTTONDOWN:

#             if event.button == 1:

#                 if game_over:

#                     reset_game()

#                 else:

#                     handle_click(
#                         event.pos
#                     )

#     # -----------------------------------------
#     # DRAW
#     # -----------------------------------------
#     update_zoom_transition()
#     draw_game()

#     # -----------------------------------------
#     # MESSAGE
#     # -----------------------------------------

#     if message:

#         elapsed = (
#             pygame.time.get_ticks()
#             - message_timer
#         )

#         if elapsed < 700:

#             message_surface = font.render(
#                 message,
#                 True,
#                 NEW_COLOR
#                 if message == "CORRECT!"
#                 else (230, 80, 80)
#             )

#             message_rect = message_surface.get_rect(
#                 center=(WIDTH // 2, HEIGHT - 25)
#             )

#             screen.blit(
#                 message_surface,
#                 message_rect
#             )

#         else:

#             message = ""

#     # -----------------------------------------
#     # GAME OVER
#     # -----------------------------------------

#     if game_over:

#         overlay = pygame.Surface(
#             (WIDTH, HEIGHT),
#             pygame.SRCALPHA
#         )

#         overlay.fill(
#             (0, 0, 0, 150)
#         )

#         screen.blit(
#             overlay,
#             (0, 0)
#         )

#         game_over_text = font.render(
#             "WRONG!  PRESS R TO RESTART",
#             True,
#             (255, 255, 255)
#         )

#         game_over_rect = game_over_text.get_rect(
#             center=(
#                 WIDTH // 2,
#                 HEIGHT // 2
#             )
#         )

#         screen.blit(
#             game_over_text,
#             game_over_rect
#         )

#     pygame.display.flip()


# pygame.quit()
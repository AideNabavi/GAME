import pygame
from modules.EFFECT.hover import hover_image_level
from modules.font import fonts


#------------------------------------------------------------------------------------------------
# support 6 image

images_support = [

    pygame.transform.smoothscale(
        pygame.image.load("./asset/image/support/contact.png").convert_alpha(),
        (350,350)
    ),

    pygame.transform.smoothscale(
        pygame.image.load("./asset/image/support/feed.png").convert_alpha(),
        (350,350)
    ),

    pygame.transform.smoothscale(
        pygame.image.load("./asset/image/support/donate.png").convert_alpha(),
        (370,370)
    ),

    pygame.transform.smoothscale(
        pygame.image.load("./asset/image/support/bug.png").convert_alpha(),
        (350,350)
    )

]


image_game_support = []

image_sizes = [
    350,350,370,
    350,
]
support_rects = []


#------------------------------------------------------------------------------------------------
# فاصله ها

gap_x = 435
gap_y = 230


# جابه جایی کل گروه نسبت به مرکز صفحه

group_offset_x = 0
group_offset_y = 150


# متن هر عکس
support_texts = [
    "Contact Us",
    "Feed Back",
    "Donate",
    "Report Bug",
]
#------------------------------------------------------------------------------------------------







# این  هم چهار تا عکس برای ساپورت است که ساخته میشود 
def draw_4_images_SUPPORT(screen):

    global image_sizes

    mouse_pos = pygame.mouse.get_pos()

    support_rects.clear()
    image_game_support.clear()

    # ============================================================
    # POSITION
    # ============================================================

    center_x = screen.get_width() // 2 + group_offset_x
    center_y = screen.get_height() // 2 + group_offset_y

    positions = [

        # =========================
        # بالا
        # =========================

        (-100, -390),   # عکس 1 — بالا چپ
        ( 550, -390),   # عکس 2 — بالا راست


        # =========================
        # پایین
        # =========================

        (-100, 100),    # عکس 3 — پایین چپ
        ( 550, 100),    # عکس 4 — پایین راست

    ]


    # ============================================================
    # DRAW
    # ============================================================

    for i, img in enumerate(images_support):

        # --------------------------------------------------------
        # Punch Scale
        # --------------------------------------------------------

        punch_scale = punch_scale_animation(i)

        # هنوز زمان ورود این عکس نرسیده
        if punch_scale <= 0:
            continue

        # --------------------------------------------------------
        # Scale
        # --------------------------------------------------------

        width = int(img.get_width() * punch_scale)
        height = int(img.get_height() * punch_scale)

        punch_img = pygame.transform.smoothscale(
            img,
            (width, height)
        )

        # --------------------------------------------------------
        # Position
        # --------------------------------------------------------

        offset_x, offset_y = positions[i]

        x = center_x + offset_x
        y = center_y + offset_y

        rect = punch_img.get_rect(
            center=(x, y)
        )

        # --------------------------------------------------------
        # Hover
        # --------------------------------------------------------

        new_img, new_rect, image_sizes[i] = hover_image_level(
            punch_img,
            rect,
            mouse_pos,
            image_sizes[i]
        )

        # --------------------------------------------------------
        # Save
        # --------------------------------------------------------

        image_game_support.append(new_rect)
        support_rects.append(new_rect)

        # --------------------------------------------------------
        # Draw Image
        # --------------------------------------------------------

        screen.blit(
            new_img,
            new_rect
        )

        # --------------------------------------------------------
        # Text
        # --------------------------------------------------------

        text_surface = fonts["support"].render(
            support_texts[i],
            True,
            (255, 255, 255)
        )

        text_rect = text_surface.get_rect(
            center=(
                new_rect.centerx,
                new_rect.bottom + 40
            )
        )

        screen.blit(
            text_surface,
            text_rect
        )

    return support_rects






def reset_support_animation():

    if hasattr(draw_4_images_SUPPORT, "punch_timer"):
        del draw_4_images_SUPPORT.punch_timer

    if hasattr(draw_4_images_SUPPORT, "punch_scales"):
        del draw_4_images_SUPPORT.punch_scales

    if hasattr(draw_4_images_SUPPORT, "started"):
        del draw_4_images_SUPPORT.started

    if hasattr(punch_scale_animation, "start_time"):
        del punch_scale_animation.start_time




















# این افکت پانج است
def punch_scale_animation(index):

    """
    Punch:
    خیلی کوچک
        ↓
    حرکت بسیار سریع
        ↓
    Overshoot 💥
        ↓
    برگشت به اندازه واقعی
    """

    # ============================================================
    # INITIALIZE
    # ============================================================

    if not hasattr(punch_scale_animation, "start_time"):

        punch_scale_animation.start_time = (
            pygame.time.get_ticks()
        )

    # ============================================================
    # TIME
    # ============================================================

    now = pygame.time.get_ticks()

    # هر عکس 200ms بعد از قبلی
    start_time = (
        punch_scale_animation.start_time
        + index * 200
    )

    # هنوز نوبت عکس نرسیده
    if now < start_time:
        return 0.0

    elapsed = now - start_time

    # ============================================================
    # DURATION
    # ============================================================

    duration = 300

    # Punch تمام شده
    if elapsed >= duration:
        return 1.0

    # ============================================================
    # FAST IMPACT
    # ============================================================

    if elapsed < 170:

        progress = elapsed / 170

        # خیلی سریع وارد می‌شود
        progress = 1 - (1 - progress) ** 4

        scale = (
            0.05
            + (1.20 - 0.05) * progress
        )

    # ============================================================
    # RETURN
    # ============================================================

    else:

        progress = (elapsed - 170) / 130

        progress = 1 - (1 - progress) ** 3

        scale = (
            1.20
            - (1.20 - 1.0) * progress
        )

    return scale








# IMA=pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/support/more.png").convert_alpha(),
#         (1100,1100)
#     )



# def draw_support_face(screen,current_width,current_height):
#     screen.blit(IMA,(current_width // 2 - 550,current_height // 2 - 500))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
now_game_start=None
# games_first_window=pygame.transform.smoothscale(
#     pygame.image.load(
#         "./asset/image/window.png"
#     ).convert_alpha(),
#     (800, 800)
# )
    
    
# برای یک عکس فقط تمام 
play_next_page = pygame.transform.smoothscale(
    pygame.image.load(
        "./asset/image/yes.png"
    ).convert_alpha(),
    (200, 200)
)
    
    
# FOR PAGE 1 
back_page = pygame.transform.smoothscale(
    pygame.image.load(
        "./asset/image/back1.png"
    ).convert_alpha(),
    (150, 150)
)

# برای یک عکس فقط تمام 
next_page = pygame.transform.smoothscale(
    pygame.image.load(
        "./asset/image/play_click.png"
    ).convert_alpha(),
    (150, 150)
)
pro_page = pygame.transform.smoothscale(
    pygame.image.load(
        "./asset/image/buy_premium.png"
    ).convert_alpha(),
    (260, 170)
)

# برای صفحه بعدی است
how_to_play_next_button_page = pygame.transform.smoothscale(
    pygame.image.load(
        "./asset/image/next.png"
    ).convert_alpha(),
    (90, 90)
)
how_to_play_next_button_rec=None
next_page_rec2=None
pro_rec=None
back_page_rec=None
# افکت پاینج برای یک عکس 
def punch_scale_animation_one_image(screen, image,_image,x,y):
    global how_to_play_next_button_rec
    global back_page_rec
    global next_page_rec2
    global pro_rec
    """
    Punch:
    خیلی کوچک
        ↓
    حرکت بسیار سریع
        ↓
    Overshoot 💥
        ↓
    برگشت به اندازه واقعی
    """

    # ============================================================
    # INITIALIZE
    # ============================================================

    if not hasattr(punch_scale_animation_one_image, "start_time"):

        punch_scale_animation_one_image.start_time = (
            pygame.time.get_ticks()
        )

    # ============================================================
    # TIME
    # ============================================================

    now = pygame.time.get_ticks()

    elapsed = (
        now
        - punch_scale_animation_one_image.start_time
    )

    # ============================================================
    # DURATION
    # ============================================================

    duration = 300

    # ============================================================
    # SCALE
    # ============================================================

    if elapsed >= duration:

        scale = 1.0

    elif elapsed < 170:

        progress = elapsed / 170

        progress = 1 - (1 - progress) ** 4

        scale = (
            0.05
            + (1.20 - 0.05) * progress
        )

    else:

        progress = (elapsed - 170) / 130

        progress = 1 - (1 - progress) ** 3

        scale = (
            1.20
            - (1.20 - 1.0) * progress
        )

    # ============================================================
    # RESIZE IMAGE
    # ============================================================

    width = int(image.get_width() * scale)
    height = int(image.get_height() * scale)

    image_scaled = pygame.transform.smoothscale(
        image,
        (width, height)
    )

    # ============================================================
    # CENTER
    # ============================================================

    rect = image_scaled.get_rect(
        center=(x,y)
    )
    # next_page_rec1 = rect
    if _image == "PLAY":
        next_page_rec2 = rect
        # back_page_rec = rect
    elif _image == "NEXT":
        how_to_play_next_button_rec = rect
        # back_page_rec = rect
    elif _image == "BACK":
        back_page_rec = rect
        # back_page_rec = rect
    elif _image == "PRO":
        pro_rec = rect
        # back_page_rec = rect

    # ============================================================
    # DRAW
    # ============================================================

    screen.blit(image_scaled, rect)
    


# این هم برای ریست دکمه برفتن در پیج ها در بازی دیلی است 
def reset_punch_scale_animation_one_image():

    if hasattr(
        punch_scale_animation_one_image,
        "start_time"
    ):
        del punch_scale_animation_one_image.start_time


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
STOR__=pygame.transform.smoothscale(pygame.image.load("./asset/image/store_.png").convert_alpha(),(1500,1100))
    
    

    
V=500
    
# SUPPORT_window1__1=pygame.transform.smoothscale(pygame.image.load("./asset/image/window1_1.png").convert_alpha(),(1200,1200))
before_game_window=pygame.transform.smoothscale(pygame.image.load("./asset/image/guide/before_game_window.png").convert_alpha(),(1700,1200))
daily_window=pygame.transform.smoothscale(pygame.image.load("./asset/image/daily_window.png").convert_alpha(),(1700,1200))
# SUPPORT_window2=pygame.transform.smoothscale(pygame.image.load("./asset/image/window.png").convert_alpha(),(V,V))
SUPPORT_window3=pygame.transform.smoothscale(pygame.image.load("./asset/image/1.png").convert_alpha(),(1000,500))
SUPPORT_window4=pygame.transform.smoothscale(pygame.image.load("./asset/image/1.png").convert_alpha(),(1000,500))



STATUS_window=pygame.transform.smoothscale(pygame.image.load("./asset/image/1.png").convert_alpha(),(1000,500))
DAILY_window_page1=pygame.transform.smoothscale(pygame.image.load("./asset/image/1.png").convert_alpha(),(2000,1300))
# DAILY_window_page2=pygame.transform.smoothscale(pygame.image.load("./asset/image/1.png").convert_alpha(),(1000,500))

music_window_back_image=pygame.image.load("./asset/image/1.png").convert_alpha()

def open_window_with_side_effect(
    screen,
    image,
    x,
    y
):

    # ============================================================
    # INITIALIZE
    # ============================================================

    if not hasattr(open_window_with_side_effect, "start_time"):

        open_window_with_side_effect.start_time = (
            pygame.time.get_ticks()
        )

    # ============================================================
    # TIME
    # ============================================================

    now = pygame.time.get_ticks()

    elapsed = (
        now - open_window_with_side_effect.start_time
    )

    # ============================================================
    # DURATION
    # ============================================================

    duration = 600

    # ============================================================
    # EASE OUT
    # ============================================================

    if elapsed >= duration:

        progress = 1.0

    else:

        progress = elapsed / duration

        progress = 1 - (1 - progress) ** 3

    # ============================================================
    # START POSITION
    # ============================================================

    start_x = (
        screen.get_width()
        + image.get_width()
    )

    # ============================================================
    # CURRENT POSITION
    # ============================================================

    current_x = (
        start_x
        + (x - start_x) * progress
    )


    
    # ============================================================
    # DRAW
    # ============================================================

    rect = image.get_rect(
        center=(int(current_x), y)
    )

    screen.blit(
        image,
        rect
    )
    
def reset_window_side_effect():

    if hasattr(
        open_window_with_side_effect,
        "start_time"
    ):

        del open_window_with_side_effect.start_time
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
from modules.SUPPORT import contact_us as CONTACT
        
def open_many_window_side_effect(
    screen,
    image,
    x,
    y
):

    # ============================================================
    # INITIALIZE
    # ============================================================

    if not hasattr(open_many_window_side_effect, "start_time"):

        open_many_window_side_effect.start_time = (
            pygame.time.get_ticks()
        )

    # ============================================================
    # TIME
    # ============================================================

    now = pygame.time.get_ticks()

    elapsed = (
        now - open_many_window_side_effect.start_time
    )

    # ============================================================
    # DURATION
    # ============================================================

    duration = 600

    # ============================================================
    # EASE OUT
    # ============================================================

    if elapsed >= duration:

        progress = 1.0

    else:

        progress = elapsed / duration

        progress = 1 - (1 - progress) ** 3

    # ============================================================
    # START POSITION
    # ============================================================

    start_x = (
        screen.get_width()
        + image.get_width()
    )

    # ============================================================
    # CURRENT POSITION
    # ============================================================

    current_x = (
        start_x
        + (x - start_x) * progress
    )

    # ============================================================
    # DRAW CONTACT CONTENT
    # ============================================================

    CONTACT.draw_social_links(
        screen,
        CONTACT.images,
        CONTACT.urls,
        current_x
    )

    # CONTACT.draw_contact_form(
    #     screen,
    #     fonts["date"],
    #     current_x
    # )

    # ============================================================
    # DRAW MAIN IMAGE / WINDOW
    # ============================================================

    rect = image.get_rect(
        center=(
            int(current_x),
            y
        )
    )

    screen.blit(
        image,
        rect
    )
    
    
    
    
    
    
    
    
    
    
    
    
    
    


































# این پانج هکس رو ب ه وجود میارد 
def support_punch(
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

    now = pygame.time.get_ticks()

    # ========================================================
    # Animation
    # ========================================================

    if not hasattr(support_punch, "_animations"):
        support_punch._animations = {}

    if page_id not in support_punch._animations:
        support_punch._animations[page_id] = {
            "start_time": now,
            "finished": False
        }

    animation = support_punch._animations[page_id]

    elapsed = now - animation["start_time"]

    if not animation["finished"]:

        if elapsed >= duration:

            animation["finished"] = True
            scale = 1.0

        else:

            progress = elapsed / duration

            if progress < 0.55:

                p = progress / 0.55
                p = 1 - (1 - p) ** 4

                scale = 0.20 + (1.12 - 0.20) * p

            else:

                p = (progress - 0.55) / 0.45
                p = 1 - (1 - p) ** 3

                scale = 1.12 + (1.0 - 1.12) * p

    else:

        scale = 1.0

    # ========================================================
    # Main Image
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
    # Image Cache
    # ========================================================

    if not hasattr(support_punch, "_image_cache"):
        support_punch._image_cache = {}

    cache = support_punch._image_cache

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
    # Main Rect
    # ========================================================

    rect = scaled_image.get_rect(
        center=center
    )

    screen.blit(
        scaled_image,
        rect
    )

    # ========================================================
    # Center Image
    # ========================================================

    if center_image is not None:

        if center_image_size is None:
            center_image_size = center_image.get_size()

        center_width = max(
            1,
            int(center_image_size[0] * scale)
        )

        center_height = max(
            1,
            int(center_image_size[1] * scale)
        )

        center_cache_key = (
            id(center_image),
            center_width,
            center_height
        )

        if center_cache_key not in cache:

            cache[center_cache_key] = pygame.transform.smoothscale(
                center_image,
                (
                    center_width,
                    center_height
                )
            )

        scaled_center_image = cache[center_cache_key]

        center_rect = scaled_center_image.get_rect(
            center=(
                rect.centerx,
                rect.centery - int(height * 0.01)
            )
        )

        screen.blit(
            scaled_center_image,
            center_rect
        )

    # ========================================================
    # Text
    # ========================================================

    if text is not None and text_font is not None:

        text_surface = text_font.render(
            str(text),
            True,
            text_color
        )

        text_rect = text_surface.get_rect(
            center=(
                rect.centerx,
                rect.centery + int(height * 0.60)
            )
        )

        screen.blit(
            text_surface,
            text_rect
        )


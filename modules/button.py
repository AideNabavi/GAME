from modules.EFFECT.hover import *
from modules.font import fonts
import pygame
from modules.language import get_font
from modules.language import display_text, get_language_font


size = 200



def in_game_button(
    screen,
    exit_button_rect,
    picture
):

    global size

    mouse_pos = pygame.mouse.get_pos()


    image, image_rect, size = hover_image_icon(
        picture,
        exit_button_rect,
        mouse_pos,
        size
    )


    screen.blit(
        image,
        image_rect
    )
    
#----------------------------------------------------------------------------------

# support_b = pygame.image.load(
#     "./asset/image/support1.png"
# ).convert_alpha()


# support_size = 150



# def support_button(
#     screen,
#     support_button_rect
# ):

#     global support_size

#     mouse_pos = pygame.mouse.get_pos()


#     image, image_rect, support_size = hover_image_icon(
#         support_b,
#         support_button_rect,
#         mouse_pos,
#         support_size
#     )


#     screen.blit(
#         image,
#         image_rect
#     )
    

    
    
#----------------------------------------------------------------------------------  donate

HOVER_CACHE = {}


def get_scaled_image(image, size):

    key = (id(image), size)

    if key not in HOVER_CACHE:

        HOVER_CACHE[key] = pygame.transform.smoothscale(
            image,
            (size, size)
        )

    return HOVER_CACHE[key]

def hover_image_icon_button(
    image,
    rect,
    mouse_pos,
    current_size
):

    NORMAL_SIZE = 120
    HOVER_SIZE = 180
    SPEED = 2

    if rect.collidepoint(mouse_pos):

        if current_size < HOVER_SIZE:
            current_size += SPEED

    else:

        if current_size > NORMAL_SIZE:
            current_size -= SPEED

    new_image = get_scaled_image(
        image,
        current_size
    )

    new_rect = new_image.get_rect(
        center=rect.center
    )

    return new_image, new_rect, current_size


donate_ = pygame.image.load(
    "./asset/image/donate.png"
).convert_alpha()

donate_base_ = pygame.image.load(
    "./asset/image/donate_base.png"
).convert_alpha()


don = 120
don_base = 150



def donate_button(
    screen,
    call_button_rect
):

    global don

    mouse_pos = pygame.mouse.get_pos()


    image, image_rect, don = hover_image_icon_button(
        donate_,
        call_button_rect,
        mouse_pos,
        don
    )


    screen.blit(
        image,
        image_rect
    )
    
    

def donate_base(
    screen,
    call_button_rect
):

    global don_base

    mouse_pos = pygame.mouse.get_pos()


    image, image_rect, don_base = hover_image_icon(
        donate_base_,
        call_button_rect,
        mouse_pos,
        don_base
    )


    screen.blit(
        image,
        image_rect
    )
    
    







#-------------------------------------
#-------------------------------------
#-------------------------------------
#-------------------------------------
#-------------------------------------
#-------------------------------------
#-------------------------------------
#-------------------------------------
#-------------------------------------
#-------------------------------------
#-------------------------------------
#-------------------------------------
#-------------------------------------
#-------------------------------------
#-------------------------------------
#-------------------------------------
#-------------------------------------
#-------------------------------------
#-------------------------------------
#-------------------------------------
#-------------------------------------
#-------------------------------------
#-------------------------------------
#-------------------------------------
#-------------------------------------
#-------------------------------------
#-------------------------------------
#-------------------------------------
#-------------------------------------
#-------------------------------------
#-------------------------------------
#-------------------------------------
#-------------------------------------
#-------------------------------------
#------------------------------------- این برای FOUR_ICON_FOR_SCREEN

def hover_image_icon_button____(
    image,
    rect,
    mouse_pos,
    current_size
):

    NORMAL_SIZE = 100
    HOVER_SIZE = 160
    SPEED = 2

    if rect.collidepoint(mouse_pos):

        if current_size < HOVER_SIZE:
            current_size += SPEED

    else:

        if current_size > NORMAL_SIZE:
            current_size -= SPEED

    new_image = get_scaled_image(
        image,
        current_size
    )

    new_rect = new_image.get_rect(
        center=rect.center
    )

    return new_image, new_rect, current_size


def hover_image_iconforthis(
    image,
    rect,
    mouse_pos,
    current_size
):

    NORMAL_SIZE = 120
    HOVER_SIZE = 145
    SPEED = 2

    if rect.collidepoint(mouse_pos):

        if current_size < HOVER_SIZE:
            current_size += SPEED

    else:

        if current_size > NORMAL_SIZE:
            current_size -= SPEED

    new_image = get_scaled_image(
        image,
        current_size
    )

    new_rect = new_image.get_rect(
        center=rect.center
    )

    return new_image, new_rect, current_size



don1= 100
don_base1 = 120

def donate_button1(
    screen,
    call_button_rect
):

    global don1

    mouse_pos = pygame.mouse.get_pos()


    image, image_rect, don1 = hover_image_icon_button____(
        donate_,
        call_button_rect,
        mouse_pos,
        don1
    )


    screen.blit(
        image,
        image_rect
    )
    
    

def donate_base1(
    screen,
    call_button_rect
):

    global don_base1

    mouse_pos = pygame.mouse.get_pos()


    image, image_rect, don_base1 = hover_image_iconforthis(
        donate_base_,
        call_button_rect,
        mouse_pos,
        don_base1
    )


    screen.blit(
        image,
        image_rect
    )
    
    










call1 = 100
base_call1 = 120



def call_support1(
    screen,
    call_button_rect
):

    global call1

    mouse_pos = pygame.mouse.get_pos()


    image, image_rect, call1= hover_image_icon_button____(
        support_Call,
        call_button_rect,
        mouse_pos,
        call1
    )


    screen.blit(
        image,
        image_rect
    )
    
    

def call_base1(
    screen,
    call_button_rect
):

    global base_call1

    mouse_pos = pygame.mouse.get_pos()


    image, image_rect, base_call1 = hover_image_iconforthis(
        support_base,
        call_button_rect,
        mouse_pos,
        base_call1
    )


    screen.blit(
        image,
        image_rect
    )
    





















































#----------------------------------------------------------------------------------   sms


def hover_image_icon_button_1(
    image,
    rect,
    mouse_pos,
    current_size
):

    NORMAL_SIZE = 100
    HOVER_SIZE = 170
    SPEED = 2


    if rect.collidepoint(mouse_pos):

        if current_size < HOVER_SIZE:
            current_size += SPEED

    else:

        if current_size > NORMAL_SIZE:
            current_size -= SPEED


    new_image = pygame.transform.smoothscale(
        image,
        (
            current_size,
            current_size
        )
    )


    new_rect = new_image.get_rect(
        center=rect.center
    )


    return new_image, new_rect, current_size




sms_ = pygame.image.load(
    "./asset/image/sms.png"
).convert_alpha()

sms_base_ = pygame.image.load(
    "./asset/image/sms_base.png"
).convert_alpha()


ssms = 100
smss_base = 150



def sms_button(
    screen,
    call_button_rect
):

    global ssms

    mouse_pos = pygame.mouse.get_pos()


    image, image_rect, ssms = hover_image_icon_button_1(
        sms_,
        call_button_rect,
        mouse_pos,
        ssms
    )


    screen.blit(
        image,
        image_rect
    )
    
    

def sms_base(
    screen,
    call_button_rect
):

    global smss_base

    mouse_pos = pygame.mouse.get_pos()


    image, image_rect, smss_base = hover_image_icon(
        sms_base_,
        call_button_rect,
        mouse_pos,
        smss_base
    )


    screen.blit(
        image,
        image_rect
    )
    
#----------------------------------------------------------------------------------   support








support_Call = pygame.image.load(
    "./asset/image/support.png"
).convert_alpha()

support_base = pygame.image.load(
    "./asset/image/support_base.png"
).convert_alpha()


call = 120
base_call = 150



def call_support(
    screen,
    call_button_rect
):

    global call

    mouse_pos = pygame.mouse.get_pos()


    image, image_rect, call = hover_image_icon_button(
        support_Call,
        call_button_rect,
        mouse_pos,
        call
    )


    screen.blit(
        image,
        image_rect
    )
    
    

def call_base(
    screen,
    call_button_rect
):

    global base_call

    mouse_pos = pygame.mouse.get_pos()


    image, image_rect, base_call = hover_image_icon(
        support_base,
        call_button_rect,
        mouse_pos,
        base_call
    )


    screen.blit(
        image,
        image_rect
    )
    





#----------------------------------------------------------------------------------   store









store_ = pygame.image.load(
    "./asset/image/store.png"
).convert_alpha()

store_base_ = pygame.image.load(
    "./asset/image/store_base.png"
).convert_alpha()


sto = 120
sto_base = 150




def store_button(
    screen,
    call_button_rect
):

    global sto

    mouse_pos = pygame.mouse.get_pos()


    image, image_rect, sto = hover_image_icon_button(
        store_,
        call_button_rect,
        mouse_pos,
        sto
    )


    screen.blit(
        image,
        image_rect
    )
    
    

def store_base(
    screen,
    call_button_rect
):

    global sto_base

    mouse_pos = pygame.mouse.get_pos()


    image, image_rect, sto_base = hover_image_icon(
        store_base_,
        call_button_rect,
        mouse_pos,
        sto_base
    )


    screen.blit(
        image,
        image_rect
    )
    






















# # ============================================================
# # MENU ICONS
# # ============================================================
# sssize=(70, 70)

# games = pygame.transform.smoothscale(
#     pygame.image.load(
#         "./asset/image/games.png"
#     ).convert_alpha(),
#     sssize
# )


# online = pygame.transform.smoothscale(
#     pygame.image.load(
#         "./asset/image/online.png"
#     ).convert_alpha(),
#     sssize
# )

# setting = pygame.transform.smoothscale(
#     pygame.image.load(
#         "./asset/image/setting.png"
#     ).convert_alpha(),
#     sssize
# )
# leaderboard = pygame.transform.smoothscale(
#     pygame.image.load(
#         "./asset/image/leaderboard.png"
#     ).convert_alpha(),
#     sssize
# )

# quit_ = pygame.transform.smoothscale(
#     pygame.image.load(
#         "./asset/image/quit.png"
#     ).convert_alpha(),
#     sssize
# )

# support = pygame.transform.smoothscale(
#     pygame.image.load(
#         "./asset/image/call.png"
#     ).convert_alpha(),
#     sssize
# )

# daily = pygame.transform.smoothscale(
#     pygame.image.load(
#         "./asset/image/daily.png"
#     ).convert_alpha(),
#     sssize
# )
# dashboard = pygame.transform.smoothscale(
#     pygame.image.load(
#         "./asset/image/dashboard.png"
#     ).convert_alpha(),
#     (100,70)
# )
# dashboard.set_alpha(0)

# # ============================================================
# # ICON LIST
# # ============================================================

# menu_icons = [
#     dashboard,
#     daily,
#     games,
#     online,
#     leaderboard,
#     setting,
#     support,
#     quit_
# ]




# # ============================================================
# # MENU TITLES
# # ============================================================

# button_titles = [
#     "",
#     "start",
#     "games",
#     "online",
#     "ranking",
#     "setting",
#     "support",
#     "quit"
# ]


# # ============================================================
# # HOVER SIZE
# # ============================================================

# menu_sizes = [
#     100.0,
#     70.0,
#     70.0,
#     70.0,
#     70.0,
#     70.0,
#     70.0,
#     70.0
# ]

# ggg=40
# # ============================================================
# # MENU POSITIONS
# # ============================================================

# menu_positions = [

#     # daily
#     (40, 90 - 33),

#     # games
#     (ggg, 287- 33),

#     # online
#     (ggg, 431- 33),

#     # custom
#     (ggg, 562- 33),

#     # setting
#     (ggg, 712- 22),

#     # support
#     (ggg, 921- 22),

#     # quit
#     (ggg, 1042- 20),
#     (ggg, 1192-20)
# ]


# # ============================================================
# # MENU SURFACE CACHE
# # ============================================================

# menu_cache = {}


# # ============================================================
# # HOVER FUNCTION FOR MENU
# # ============================================================

# def hover_1image_menu(
#     image,
#     rect,
#     mouse_pos,
#     current_size
# ):

#     NORMAL_SIZE = 70
#     HOVER_SIZE = 90
#     SMOOTH = 0.2

#     # --------------------------------------------------------
#     # HOVER DETECTION
#     # --------------------------------------------------------

#     if rect.collidepoint(mouse_pos):

#         target = HOVER_SIZE

#     else:

#         target = NORMAL_SIZE


#     # --------------------------------------------------------
#     # SMOOTH ANIMATION
#     # --------------------------------------------------------

#     current_size += (
#         target - current_size
#     ) * SMOOTH


#     # --------------------------------------------------------
#     # IMPORTANT
#     # --------------------------------------------------------
#     # این تابع خودش تصویر را Scale نمی‌کند.
#     #
#     # فقط اندازه Hover را برمی‌گرداند.
#     #
#     # این باعث می‌شود smoothscale در هر Frame
#     # اجرا نشود.
#     # --------------------------------------------------------

#     return (
#         image,
#         rect,
#         current_size
#     )


# # ============================================================
# # CREATE MENU SURFACE
# # ============================================================

# def create_menu_surface(
#     index,
#     size,
#     fonts
# ):

#     # ========================================================
#     # TEXT
#     # ========================================================

#     translated_text = display_text(
#         button_titles[index]
#     )


#     # ========================================================
#     # CACHE KEY
#     # ========================================================

#     key = (
#         index,
#         size,
#         translated_text
#     )


#     # ========================================================
#     # CACHE
#     # ========================================================

#     if key in menu_cache:

#         return menu_cache[key]


#     # ========================================================
#     # ORIGINAL ICON
#     # ========================================================

#     icon = menu_icons[index]


#     # ========================================================
#     # ORIGINAL TEXT
#     # ========================================================
#     # font = fonts["support"]

#     text_color = (255, 140, 0)
#     stroke_color = (0, 0, 0)
#     stroke_width = 1
#     font = get_language_font("support")
#     # ========================================================
#     # TEXT WITH STROKE
#     # ========================================================

#     base_text = font.render(
#         translated_text,
#         True,
#         text_color
#     )

#     text = pygame.Surface(
#         (
#             base_text.get_width() + stroke_width * 2,
#             base_text.get_height() + stroke_width * 2
#         ),
#         pygame.SRCALPHA
#     )

#     # # Stroke
#     for dx in range(-stroke_width, stroke_width + 1):
#         for dy in range(-stroke_width, stroke_width + 1):

#             if dx == 0 and dy == 0:
#                 continue

#             text.blit(
#                 font.render(
#                     translated_text,
#                     True,
#                     stroke_color
#                 ),
#                 (
#                     stroke_width + dx,
#                     stroke_width + dy
#                 )
#             )

#     # Text اصلی
#     text.blit(
#         base_text,
#         (
#             stroke_width,
#             stroke_width
#         )
#     )

#     # ========================================================
#     # SCALE
#     # ========================================================

#     scale = size / 70.0


#     # ========================================================
#     # ICON SIZE
#     # ========================================================

#     icon_size = int(
#         70 * scale
#     )


#     # جلوگیری از صفر شدن اندازه
#     if icon_size < 1:
#         icon_size = 1


#     # ========================================================
#     # SCALE ICON
#     # ========================================================

#     if size == 70:

#         scaled_icon = icon

#     else:

#         scaled_icon = pygame.transform.smoothscale(
#             icon,
#             (
#                 icon_size,
#                 icon_size
#             )
#         )


#     # ========================================================
#     # SCALE TEXT
#     # ========================================================

#     if size == 70:

#         scaled_text = text

#     else:

#         text_width = int(
#             text.get_width() * scale
#         )

#         text_height = int(
#             text.get_height() * scale
#         )


#         if text_width < 1:
#             text_width = 1

#         if text_height < 1:
#             text_height = 1


#         scaled_text = pygame.transform.smoothscale(
#             text,
#             (
#                 text_width,
#                 text_height
#             )
#         )


#     # ========================================================
#     # SPACING
#     # ========================================================

#     spacing = int(
#         25 * scale
#     )


#     # ========================================================
#     # GROUP SIZE
#     # ========================================================

#     width = (
#         scaled_icon.get_width()
#         + spacing
#         + scaled_text.get_width()
#     )

#     height = max(
#         scaled_icon.get_height(),
#         scaled_text.get_height()
#     )


#     # ========================================================
#     # GROUP SURFACE
#     # ========================================================

#     surface = pygame.Surface(
#         (
#             width,
#             height
#         ),
#         pygame.SRCALPHA
#     )


#     # ========================================================
#     # ICON RECT
#     # ========================================================

#     icon_rect = scaled_icon.get_rect()

#     icon_rect.midleft = (
#         0,
#         height // 2
#     )


#     # ========================================================
#     # TEXT RECT
#     # ========================================================

#     text_rect = scaled_text.get_rect()

#     text_rect.midleft = (
#         icon_rect.right + spacing,
#         height // 2
#     )


#     # ========================================================
#     # DRAW ICON
#     # ========================================================

#     surface.blit(
#         scaled_icon,
#         icon_rect
#     )


#     # ========================================================
#     # DRAW TEXT
#     # ========================================================

#     surface.blit(
#         scaled_text,
#         text_rect
#     )


#     # ========================================================
#     # SAVE CACHE
#     # ========================================================

#     menu_cache[key] = surface


#     return surface


# # ============================================================
# # DRAW MENU BUTTONS
# # ============================================================

# def draw_menu_buttons(
#     screen,
#     current_width,
#     current_height,
#     fonts,
#     select_buttons
# ):

#     # ========================================================
#     # MOUSE POSITION
#     # ========================================================

#     mouse_pos = pygame.mouse.get_pos()


#     # ========================================================
#     # MENU
#     # ========================================================

#     for i in range(
#         len(menu_icons)
#     ):

#         # ====================================================
#         # POSITION
#         # ====================================================

#         x = menu_positions[i][0]

#         y = (
#             menu_positions[i][1]
#         )


#         # ====================================================
#         # NORMAL SURFACE
#         # ====================================================

#         base_surface = create_menu_surface(
#             i,
#             70,
#             fonts
#         )


#         # ====================================================
#         # NORMAL RECT
#         # ====================================================

#         base_rect = base_surface.get_rect(
#             topleft=(
#                 x,
#                 y
#             )
#         )


#         # ====================================================
#         # HOVER
#         # ====================================================

#         _, _, menu_sizes[i] = hover_1image_menu(
#             menu_icons[i],
#             base_rect,
#             mouse_pos,
#             menu_sizes[i]
#         )


#         # ====================================================
#         # INTEGER SIZE
#         # ====================================================

#         size = int(
#             round(
#                 menu_sizes[i]
#             )
#         )


#         # ====================================================
#         # LIMIT SIZE
#         # ====================================================

#         if size < 70:
#             size = 70

#         if size > 70:
#             size = 70


#         # ====================================================
#         # GET CACHED SURFACE
#         # ====================================================

#         surface = create_menu_surface(
#             i,
#             size,
#             fonts
#         )


#         # ====================================================
#         # POSITION
#         # ====================================================

#         rect = surface.get_rect(
#             topleft=(
#                 x,
#                 y
#             )
#         )


#         # ====================================================
#         # DRAW
#         # ====================================================

#         screen.blit(
#             surface,
#             rect
#         )


#         # ====================================================
#         # CLICK RECT
#         # ====================================================

#         select_buttons.append(
#             rect.copy()
#         )











# import pygame

# from modules.language import display_text, get_language_font


# # ============================================================
# # MENU ICONS
# # ============================================================

# ICON_SIZE = (70, 70)

# games = pygame.transform.smoothscale(
#     pygame.image.load(
#         "./asset/image/menu/games.png"
#     ).convert_alpha(),
#     ICON_SIZE
# )

# online = pygame.transform.smoothscale(
#     pygame.image.load(
#         "./asset/image/menu/online.png"
#     ).convert_alpha(),
#     ICON_SIZE
# )

# setting = pygame.transform.smoothscale(
#     pygame.image.load(
#         "./asset/image/menu/setting.png"
#     ).convert_alpha(),
#     ICON_SIZE
# )

# leaderboard = pygame.transform.smoothscale(
#     pygame.image.load(
#         "./asset/image/menu/leaderboard.png"
#     ).convert_alpha(),
#     ICON_SIZE
# )

# quit_ = pygame.transform.smoothscale(
#     pygame.image.load(
#         "./asset/image/menu/quit.png"
#     ).convert_alpha(),
#     ICON_SIZE
# )

# support = pygame.transform.smoothscale(
#     pygame.image.load(
#         "./asset/image/menu/call.png"
#     ).convert_alpha(),
#     ICON_SIZE
# )

# daily = pygame.transform.smoothscale(
#     pygame.image.load(
#         "./asset/image/menu/daily.png"
#     ).convert_alpha(),
#     ICON_SIZE
# )


# # ============================================================
# # ICON LIST
# # ============================================================

# menu_icons = [
#     daily,
#     games,
#     online,
#     leaderboard,
#     setting,
#     support,
#     quit_
# ]


# # ============================================================
# # MENU TITLES
# # ============================================================

# MENU_title = [
#     "",
#     "start",
#     "games",
#     "online",
#     "ranking",
#     "setting",
#     "support",
#     "quit"
# ]


# # ============================================================
# # MENU POSITIONS
# # ============================================================

# ggg = 40

# menu_positions = [

#     (40, 90 - 33),
#     (ggg, 287 - 33),
#     (ggg, 431 - 33),
#     (ggg, 562 - 33),
#     (ggg, 712 - 22),
#     (ggg, 921 - 22),
#     (ggg, 1042 - 20),
#     (ggg, 1192-20)

# ]

# # ============================================================
# # MENU SURFACE CACHE
# # ============================================================

# menu_cache = {}


# # ============================================================
# # CREATE MENU BUTTON
# # ============================================================

# def create_menu_surface(index):

#     translated_text = display_text(
#         MENU_title[index]
#     )

#     key = (
#         index,
#         translated_text
#     )

#     if key in menu_cache:
#         return menu_cache[key]

#     # --------------------------------------------------------
#     # ICON
#     # --------------------------------------------------------

#     icon = menu_icons[index]

#     # --------------------------------------------------------
#     # FONT
#     # --------------------------------------------------------

#     font = get_language_font("support")

#     text_color = (255, 140, 0)
#     stroke_color = (0, 0, 0)
#     stroke_width = 1

#     # --------------------------------------------------------
#     # TEXT
#     # --------------------------------------------------------

#     base_text = font.render(
#         translated_text,
#         True,
#         text_color
#     )

#     text = pygame.Surface(
#         (
#             base_text.get_width() + stroke_width * 2,
#             base_text.get_height() + stroke_width * 2
#         ),
#         pygame.SRCALPHA
#     )

#     # Stroke
#     for dx in range(
#         -stroke_width,
#         stroke_width + 1
#     ):

#         for dy in range(
#             -stroke_width,
#             stroke_width + 1
#         ):

#             if dx == 0 and dy == 0:
#                 continue

#             text.blit(
#                 font.render(
#                     translated_text,
#                     True,
#                     stroke_color
#                 ),
#                 (
#                     stroke_width + dx,
#                     stroke_width + dy
#                 )
#             )

#     # Main text
#     text.blit(
#         base_text,
#         (
#             stroke_width,
#             stroke_width
#         )
#     )

#     # --------------------------------------------------------
#     # SPACING
#     # --------------------------------------------------------

#     spacing = 25

#     # --------------------------------------------------------
#     # GROUP SIZE
#     # --------------------------------------------------------

#     width = (
#         icon.get_width()
#         + spacing
#         + text.get_width()
#     )

#     height = max(
#         icon.get_height(),
#         text.get_height()
#     )

#     # --------------------------------------------------------
#     # GROUP SURFACE
#     # --------------------------------------------------------

#     surface = pygame.Surface(
#         (
#             width,
#             height
#         ),
#         pygame.SRCALPHA
#     )

#     # --------------------------------------------------------
#     # ICON RECT
#     # --------------------------------------------------------

#     icon_rect = icon.get_rect()

#     icon_rect.midleft = (
#         0,
#         height // 2
#     )

#     # --------------------------------------------------------
#     # TEXT RECT
#     # --------------------------------------------------------

#     text_rect = text.get_rect()

#     text_rect.midleft = (
#         icon_rect.right + spacing,
#         height // 2
#     )

#     # --------------------------------------------------------
#     # DRAW
#     # --------------------------------------------------------

#     surface.blit(
#         icon,
#         icon_rect
#     )

#     surface.blit(
#         text,
#         text_rect
#     )

#     # --------------------------------------------------------
#     # CACHE
#     # --------------------------------------------------------

#     menu_cache[key] = surface

#     return surface


# # ============================================================
# # DRAW MENU BUTTONS
# # ============================================================

# def draw_menu_buttons(
#     screen,
#     current_width,
#     current_height,
#     fonts,
#     select_buttons
# ):

#     # --------------------------------------------------------
#     # DRAW
#     # --------------------------------------------------------

#     for i in range(
#         len(menu_icons)
#     ):

#         x = menu_positions[i][0]
#         y = menu_positions[i][1]

#         # ----------------------------------------------------
#         # CREATE GROUP
#         # ----------------------------------------------------

#         surface = create_menu_surface(
#             i
#         )

#         # ----------------------------------------------------
#         # RECT
#         # ----------------------------------------------------

#         rect = surface.get_rect(
#             topleft=(
#                 x,
#                 y
#             )
#         )

#         # ----------------------------------------------------
#         # DRAW
#         # ----------------------------------------------------

#         screen.blit(
#             surface,
#             rect
#         )

#         # ----------------------------------------------------
#         # CLICK RECT
#         # ----------------------------------------------------

#         select_buttons.append(
#             rect.copy()
#         )












import pygame
import importlib

pygame.init()


# ==================================================
# Loading Window
# ==================================================

screen = pygame.display.set_mode(
    (960, 540)
)

pygame.display.set_caption(
    "Mental Math Challenge"
)


# ==================================================
# Icon
# ==================================================

icon = pygame.image.load(
    "asset/image/icon.png"
).convert_alpha()

pygame.display.set_icon(icon)


# ==================================================
# Loading Manager
# ==================================================

from modules.loading import LoadingManager

loader = LoadingManager(
    screen
)


# ==================================================
# Add Modules
# ==================================================

loader.add(
    lambda: importlib.import_module(
        "event_handler"
    )
)

loader.add(
    lambda: importlib.import_module(
        "modules.time_screen"
    )
)

loader.add(
    lambda: importlib.import_module(
        "modules.game_engine"
    )
)

loader.add(
    lambda: importlib.import_module(
        "modules.timer"
    )
)

loader.add(
    lambda: importlib.import_module(
        "modules.window"
    )
)

loader.add(
    lambda: importlib.import_module(
        "modules.gif"
    )
)

loader.add(
    lambda: importlib.import_module(
        "modules.button"
    )
)

loader.add(
    lambda: importlib.import_module(
        "modules.ab"
    )
)

loader.add(
    lambda: importlib.import_module(
        "modules.design"
    )
)

loader.add(
    lambda: importlib.import_module(
        "modules.language"
    )
)

loader.add(
    lambda: importlib.import_module(
        "modules.sound"
    )
)

loader.add(
    lambda: importlib.import_module(
        "modules.font"
    )
)

loader.add(
    lambda: importlib.import_module(
        "modules.player_profile"
    )
)

loader.add(
    lambda: importlib.import_module(
        "modules.screen"
    )
)

loader.add(
    lambda: importlib.import_module(
        "modules.theme"
    )
)

loader.add(
    lambda: importlib.import_module(
        "modules.about"
    )
)

loader.add(
    lambda: importlib.import_module(
        "modules.LEVELS.LEVELS"
    )
)

loader.add(
    lambda: importlib.import_module(
        "modules.STATES"
    )
)

loader.add(
    lambda: importlib.import_module(
        "modules.DATA"
    )
)

loader.add(
    lambda: importlib.import_module(
        "modules.ceill_screen"
    )
)

loader.add(
    lambda: importlib.import_module(
        "modules.profile_"
    )
)

loader.add(
    lambda: importlib.import_module(
        "modules.mode"
    )
)

loader.add(
    lambda: importlib.import_module(
        "modules.support"
    )
)

loader.add(
    lambda: importlib.import_module(
        "modules.more"
    )
)

loader.add(
    lambda: importlib.import_module(
        "modules.MODE.FIND_NUMBER"
    )
)

loader.add(
    lambda: importlib.import_module(
        "modules.MODE.MEMORY"
    )
)

loader.add(
    lambda: importlib.import_module(
        "modules.MODE.REPEAT_AFTER_ME"
    )
)

loader.add(
    lambda: importlib.import_module(
        "modules.MODE.MORE_LESS_EQUAL"
    )
)


# ==================================================
# Start Loading
# ==================================================

pygame.mixer.music.play()

loader.run()

pygame.mixer.music.stop()


# ==================================================
# Loading Finished
# ==================================================

screen = pygame.display.set_mode(
    (1920, 1080),
    pygame.FULLSCREEN
)


pygame.display.set_caption(
    "Mental Math Challenge"
)

pygame.display.set_icon(
    icon
)


# ==================================================
# Get Screen Size
# ==================================================

current_width, current_height = screen.get_size()

print(
    current_width,
    current_height
)





import sys
from event_handler import handle_events
from modules.time_screen import draw_time_screen
from modules.game_engine import run_game
from modules.timer import draw_timer_bar,draw_timer_circle
from modules.window import _window
from modules.gif import *
from modules.button import *
from modules.ab import *
from modules.design import *
from modules.language import *
from modules.sound import *
from modules.font import *
from modules.player_profile import *
from modules.screen import *
from modules.theme import *
from modules.about import draw_about
from modules.design import *
from modules.LEVELS.LEVELS import *
from modules.STATES import *
from modules.DATA import *
from modules.ceill_screen import *
from modules.profile_ import draw_profile_live_circle
from modules.mode  import *
from modules.support  import *
from modules.more  import *
from modules.MODE.FIND_NUMBER  import *
from modules.MODE.MEMORY  import *
from modules.MODE.REPEAT_AFTER_ME  import *
from modules.MODE.MORE_LESS_EQUAL  import *

# ---------------------------------------------------------- FPS 
# برای کنترل سرعت اجرای بازی
clock = pygame.time.Clock()






# این برای موزیک است عوض کردن موزیک

profile_image = pygame.image.load(
    "./asset/image/music/music.png"
).convert_alpha()



background_music = pygame.image.load(
    "./asset/image/music/music111.png"
).convert_alpha()



background_music = pygame.transform.smoothscale(
    background_music,
    (1450,950)
)
back_image=back_image.convert_alpha()
#--------------------------------------------------------------
# def load_background(path, size):
#     bg = pygame.image.load(path).convert()
#     bg = pygame.transform.smoothscale(bg, size)
#     return bg




# init_theme(screen)











# #------------------------------------------------------------- levels 

# level_slider = create_level_slider(
#     levels
# )
#------------------------------------------------------------- music
pygame.mixer.init()

#MUSIC
# start_for_ever()


#------------------------------------------------------------- Loop While
running = True




#------------------------------------------------------------- Time image
# timer_icon = pygame.image.load(
#     "./asset/image/time_image.png"
# ).convert_alpha()

# timer_icon = pygame.transform.smoothscale(
#     timer_icon,
#     (45,45)
# )







(
    support_button_rect,
    call_button_rect,
    back_button_rect
) = get_current_width_current_height_to_DATA(
    current_width,
    current_height
)







#------------------------------------------------------------- Time

time_limit = 0
time_text = ""
time_entered = False


time_button_rects = {}# for select time

#------------------------------------------------------------- Question

question_started = False

x = 0
y = 0
result = 0

question_text = None

question_start_time = 0

remaining_time = 0# برای زمان باقی مانده 



#-------------------------------------------------------------Profile Image 

profile_images = load_profile_images()
selected_profile = None
player_image = None
profile_rects = {}

#------------------------------------------------------------- NAME


player_name = ""
name_entered = False
input_box = pygame.Rect(
    0,
    0,
    500,
    80
)


#-------------------------------------------------------------

# timer_icon = pygame.image.load(
#     "./asset/image/time_image.png"
# ).convert_alpha()

# timer_icon = pygame.transform.smoothscale(
#     timer_icon,
#     (150,150)
# )

#------------------------------------------------------------- Score


score = 0
# score_icon = pygame.image.load(
#     "./asset/image/imagee.png"
# ).convert_alpha()

# score_icon = pygame.transform.smoothscale(
#     score_icon,
#     (80,80)
# )


    
# ---------------- time image----------------
# time_icon = pygame.image.load(
#     "./asset/image/ttime.png"
# ).convert_alpha()

# time_icon = pygame.transform.smoothscale(
#     time_icon,
#     (150,150)
# )
# ---------------- Answer Buttons ----------------

answers = []

answer_rects = {}

answer_selected = None

answer_clicked = False






# ---------------- profile ----------------



profile_images = load_profile_images()


# عکس انتخاب شده اولیه
selected_image = load_default_profile()
profile_images = load_profile_images()

# متغیرهای دیگر پروفایل
profile_rects = {}

profile_hovered = {}


#---------------------------- مد بازی   




clicked_button = False





    #---------------------------------- حلقه
profile_scroll = 0

profile_area = pygame.Rect(
    100,
    250,
    550,
    220
)


    
    
    
    
    
    
    
    
info = pygame.display.Info()

    
    
#BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
#BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
# --------------------------------------------- window for every where

square_rect = pygame.Rect(
    current_width // 2 - 700 // 2,
    current_height // 2 - 400 // 2,
    700,
    400
)


#---------------------------- window for levels

square_rect_level = pygame.Rect(
    current_width // 2 - 700 // 2,
    current_height // 2 - 400 // 2,
    800,
    600
)




#------------------------------------

home_button_rect = pygame.Rect(
    current_width - 160,  # فاصله از راست
    300,                   # فاصله از بالا
    90,
    90
)



#------------------------------------

askus_button_rect = pygame.Rect(
    current_width - 160,  # فاصله از راست
    440,                   # فاصله از بالا
    90,
    90
)



#------------------------------------

share_button_rect = pygame.Rect(
    current_width - 160,  # فاصله از راست
    580,                   # فاصله از بالا
    90,
    90
)







#-----------------------------------------------



    
    
    
    


#------------------------------------------------

about = pygame.image.load(
    "./asset/image/me.png"
).convert_alpha()


# تبدیل به فرمت مناسب
about = about.convert()


about = pygame.transform.smoothscale(
about,
(200,200)
)








#--------------------------------------------------------------language

lan1= pygame.Rect(
    current_width//2 - 450, current_height//2 - 300,
    90,
    90
)
lan2= pygame.Rect(
    current_width//2 - 450, current_height//2 - 300,
    90,
    90
)
lan3= pygame.Rect(
    current_width//2 - 450, current_height//2 - 300,
    90,
    90
)
lan4= pygame.Rect(
    current_width//2 - 450, current_height//2 - 300,
    90,
    90
)
lan5= pygame.Rect(
    current_width//2 - 450, current_height//2 - 300,
    90,
    90
)
lan6= pygame.Rect(
    current_width//2 - 450, current_height//2 - 300,
    90,
    90
)
#--------------------------------------------------------------language

#----------------------------- button for support_call for background this button 


# support_call_button_rect= pygame.Rect(
#     current_width - 130,  # فاصله از راست
#     current_height // 2 ,                   # فاصله از بالا
#     90,
#     90
# )


#----------------------------- bug


bug_button_rect = pygame.Rect(
    current_width - 130,  # فاصله از راست
    current_height // 2 - 40,                   # فاصله از بالا
    90,
    90
)



music_on = True
effect_on = True


#-------------------------------------------------------------SOUND
# Load background
sound_bg = pygame.image.load(
    "./asset/image/screen/sound.png"
).convert_alpha()
# def image_background(rec):
    
    

# Resize background to fullscreen size
sound_bg = pygame.transform.smoothscale(
    sound_bg,
    (1000,
    650)
)


# وسط صفحه
x = (screen.get_width() - sound_bg.get_width()) // 2 
y = (screen.get_height() - sound_bg.get_height()) // 2

#-------------------------------------------------------------LANGUAGE



#-------------------------------------------------------------
# Load background
sound_bg = pygame.image.load(
    "./asset/image/screen/sound.png"
).convert_alpha()
# def image_background(rec):
    
    

# Resize background to fullscreen size
sound_bg = pygame.transform.smoothscale(
    sound_bg,
    (1000,
    650)
)


# وسط صفحه
x = (screen.get_width() - sound_bg.get_width()) // 2 
y = (screen.get_height() - sound_bg.get_height()) // 2

#-------------------------------------------------------------
menu_button = pygame.image.load(
    "./asset/image/button1.png"
).convert_alpha()







lan_sizes = [250, 250, 250, 250, 250, 250]

lan_images = [
    pygame.transform.smoothscale(
        pygame.image.load("./asset/image/language/1.png").convert_alpha(),
        (233,233)
    ),
    pygame.transform.smoothscale(
        pygame.image.load("./asset/image/language/2.png").convert_alpha(),
        (250,250)
    ),
    pygame.transform.smoothscale(
        pygame.image.load("./asset/image/language/3.png").convert_alpha(),
        (250,250)
    ),
    pygame.transform.smoothscale(
        pygame.image.load("./asset/image/language/4.png").convert_alpha(),
        (268,268)
    ),
    pygame.transform.smoothscale(
        pygame.image.load("./asset/image/language/5.png").convert_alpha(),
        (246,246)
    ),
    pygame.transform.smoothscale(
        pygame.image.load("./asset/image/language/6.png").convert_alpha(),
        (250,250)
    )
]


offset_y = 150
offset_x = 80

language_data = [
    ("en", current_width//2 - 450, current_height//2 - 300 + offset_y),
    ("hi", current_width//2 - 125, current_height//2 - 300 + offset_y),
    ("zh", current_width//2 + 200, current_height//2 - 300 + offset_y),
    ("fa", current_width//2 - 450, current_height//2 + 80 + offset_x),
    ("ru", current_width//2 - 125, current_height//2 + 80 + offset_x),
    ("ar", current_width//2 + 200, current_height//2 + 80 + offset_x),
]
language_rects = []



def draw_languages(screen, current_width, current_height):

    global lan_sizes

    rects = []

    mouse_pos = pygame.mouse.get_pos()

    for i, (lang, x, y) in enumerate(language_data):

        rect = lan_images[i].get_rect(
            topleft=(x, y)
        )

        image, image_rect, lan_sizes[i] = hover_image_lan(
            lan_images[i],
            rect,
            mouse_pos,
            lan_sizes[i]
        )

        screen.blit(
            image,
            image_rect
        )

        rects.append((lang, image_rect))

    return rects





# background_menu=pygame.image.load("./asset/image/music/window.png")


defult_language=True





selected_profile = None
default_profile = load_default_profile()






#-----------------------------------------


box_width = 250
box_height = 50

# کمی پایین‌تر از مرکز صفحه
input_y = current_height // 2 + 100

 

# hue_bar = pygame.Rect(
#     current_width // 2 - box_width // 2,
#     input_y + 1,
#     250,
#     30
# )


input_box = pygame.Rect(
    current_width // 2 - box_width // 2,
    input_y + 40,
    box_width,
    box_height
)


enter_button = pygame.Rect(
    current_width // 2 - 75,
    input_y + 130,
    150,
    55
)







# ###################################### برای مود بازی مموری است 
# create_cards(current_width,current_height)
create_cards(current_width,current_height)
#---------------------------------------------------------------- این برای تم است که در فایل دیتا است که از آن جا برای داخل تم صدا زده میشود 

    
#----------------------------------------------------------------




level=None



SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h

WORLD_WIDTH = 5000
WORLD_HEIGHT = SCREEN_HEIGHT
level_world = pygame.Surface(
    (WORLD_WIDTH, WORLD_HEIGHT),
    pygame.SRCALPHA
)

level_images_1 = [
    pygame.image.load("./asset/image/levels/1.png").convert_alpha(),
    pygame.image.load("./asset/image/levels/2.png").convert_alpha(),
    pygame.image.load("./asset/image/levels/3.png").convert_alpha(),
    pygame.image.load("./asset/image/levels/1.png").convert_alpha(),
    pygame.image.load("./asset/image/levels/2.png").convert_alpha(),
    pygame.image.load("./asset/image/levels/3.png").convert_alpha(),
    pygame.image.load("./asset/image/levels/1.png").convert_alpha(),
    pygame.image.load("./asset/image/levels/2.png").convert_alpha(),
    pygame.image.load("./asset/image/levels/3.png").convert_alpha(),
    pygame.image.load("./asset/image/levels/3.png").convert_alpha()
]


level_positions = [
(0,200),
(500,200),
(1000,200),
(1500,200),
(2000,200),
(2500,200),
(3000,200),
(3500,200),
(4000,200),
(4500,200)
]

for img, pos in zip(level_images_1, level_positions):

    img = pygame.transform.smoothscale(
        img,
        (300,300)
    )

    level_world.blit(
        img,
        pos
    )


camera_x = 0
camera_y = 0





dragging = False

mouse_start_x = 0
mouse_start_y = 0








level_rects = []


for index, (img, pos) in enumerate(zip(level_images_1, level_positions)):

    img = pygame.transform.smoothscale(
        img,
        (300,300)
    )


    rect = img.get_rect(
        topleft=pos
    )


    level_rects.append(
        (index + 1, rect)
    )


    level_world.blit(
        img,
        pos
    )
    
    
    

# #--------------------------------------- این برای خاموش روشن کردن دکمه اهنگ است 


music_state = 1   # 0 خاموش - 1 روشن


image_on = pygame.image.load("./asset/image/music/on.png").convert_alpha()
image_off = pygame.image.load("./asset/image/music/off.png").convert_alpha()
image_on=pygame.transform.smoothscale(image_on,(190,190))
image_off=pygame.transform.smoothscale(image_off,(190,190))

rect_for_music = image_off.get_rect(center=(current_width//2 + 350 ,current_height//2 - 58))

    
    
    
# #--------------------------------------- برای افکت صوتی 

    
    

sound_state = 1

sound_on = pygame.image.load("./asset/image/music/on.png").convert_alpha()
sound_off = pygame.image.load("./asset/image/music/off.png").convert_alpha()
sound_on=pygame.transform.smoothscale(sound_on,(190,190))
sound_off=pygame.transform.smoothscale(sound_off,(190,190))

rect_for_sound = sound_off.get_rect(center=(current_width//2 + 350 ,current_height //2 + 260))

    
    
    
#---------in game---------- home button  __ ... button __...button
menu=pygame.transform.smoothscale(
        pygame.image.load("./asset/image/in_game/menu.png").convert_alpha(),
        (200,200)
    )
share=pygame.transform.smoothscale(
        pygame.image.load("./asset/image/in_game/share.png").convert_alpha(),
        (200,200)
    )
askus=pygame.transform.smoothscale(
        pygame.image.load("./asset/image/in_game/ask-us.png").convert_alpha(),
        (200,200)
    )







start_time = pygame.time.get_ticks()

question_number = 1



correct_count = 0

wrong_count = 0


# ---------------- Timer ----------------


current_question = generate_missing_number_question(
    question_number
)















































# #-------------------------back ground

# SCREEN_WIDTH_ = info.current_w
# SCREEN_HEIGHT_ = info.current_h

# WORLD_WIDTH_ = 9000
# WORLD_HEIGHT_ = SCREEN_HEIGHT_

# level_world_ = pygame.Surface(
#     (WORLD_WIDTH_, WORLD_HEIGHT_),
#     pygame.SRCALPHA
# )


# # ============================================================
# # ORIGINAL IMAGES
# # ============================================================

# level_images_theme = [

#     pygame.image.load(
#         "./asset/image/background/1.png"
#     ).convert_alpha(),

#     pygame.image.load(
#         "./asset/image/background/2.png"
#     ).convert_alpha(),

#     pygame.image.load(
#         "./asset/image/background/3.png"
#     ).convert_alpha(),

#     pygame.image.load(
#         "./asset/image/background/4.png"
#     ).convert_alpha(),

#     pygame.image.load(
#         "./asset/image/background/5.png"
#     ).convert_alpha(),

#     pygame.image.load(
#         "./asset/image/background/6.png"
#     ).convert_alpha(),

#     pygame.image.load(
#         "./asset/image/background/7.png"
#     ).convert_alpha(),

#     pygame.image.load(
#         "./asset/image/background/8.png"
#     ).convert_alpha(),

#     pygame.image.load(
#         "./asset/image/background/9.png"
#     ).convert_alpha(),

#     pygame.image.load(
#         "./asset/image/background/10.png"
#     ).convert_alpha(),

#     pygame.image.load(
#         "./asset/image/background/11.png"
#     ).convert_alpha(),

# ]


# # ============================================================
# # THEME POSITIONS
# # ============================================================
# yy=420
# level_positions_theme = [

#     (0, yy),
#     (1500, yy),
#     (3000, yy),
#     (3000, yy),
#     (4000, yy),
#     (5000, yy),
#     (6000, yy),
#     (7000, yy),
#     (8000, yy),
#     (10000, yy),
#     (110000, yy),

# ]


# # ============================================================
# # SMALL THEME IMAGES
# # عکس‌های کوچک فقط برای صفحه انتخاب Theme
# # ============================================================

# little_theme = []


# for img in level_images_theme:

#     small_img = pygame.transform.smoothscale(
#         img,
#         (1000, 600)
#     )

#     little_theme.append(
#         small_img
#     )


# # ============================================================
# # PUT SMALL IMAGES INSIDE WORLD
# # ============================================================

# for img, pos in zip(
#     little_theme,
#     level_positions_theme
# ):

#     level_world_.blit(
#         img,
#         pos
#     )


# # ============================================================
# # CAMERA
# # ============================================================

# camera_x = 0
# camera_y = 0


# # ============================================================
# # DRAGGING
# # ============================================================

# dragging = False

# mouse_start_x = 0
# mouse_start_y = 0


# # ============================================================
# # THEME RECTANGLES
# # ============================================================

# level_rects_for_theme = []


# for index, (img, pos) in enumerate(
#     zip(
#         little_theme,
#         level_positions_theme
#     )
# ):

#     rect = img.get_rect(
#         topleft=pos
#     )

#     level_rects_for_theme.append(
#         (index, rect)
#     )



# # ============================================================
# # SELECTED BACKGROUND
# # اینجا عکس اصلی است، نه little_theme
# # ============================================================

# selected_background = level_images_theme[0]


# # ============================================================
# # THEME DRAW
# # ============================================================

# def THEME_DRAW(
#     screen,
#     WORLD_WIDTH_,
#     SCREEN_WIDTH_,
#     WORLD_HEIGHT_,
#     SCREEN_HEIGHT_,
#     level_world_
# ):

#     global camera_x
#     global camera_y


#     keys = pygame.key.get_pressed()


#     if keys[pygame.K_RIGHT]:

#         camera_x += 10


#     if keys[pygame.K_LEFT]:

#         camera_x -= 10


#     if keys[pygame.K_DOWN]:

#         camera_y += 10


#     if keys[pygame.K_UP]:

#         camera_y -= 10


#     # ========================================================
#     # CAMERA LIMIT X
#     # ========================================================

#     camera_x = max(
#         0,
#         min(
#             camera_x,
#             WORLD_WIDTH_ - SCREEN_WIDTH_
#         )
#     )


#     # ========================================================
#     # CAMERA LIMIT Y
#     # ========================================================

#     camera_y = max(
#         0,
#         min(
#             camera_y,
#             WORLD_HEIGHT_ - SCREEN_HEIGHT_
#         )
#     )


#     # ========================================================
#     # DRAW WORLD
#     # ========================================================

#     screen.blit(
#         level_world_,
#         (0, 0),
#         (
#             camera_x,
#             camera_y,
#             SCREEN_WIDTH_,
#             SCREEN_HEIGHT_
#         )
#     )


# # ============================================================
# # DRAW SELECTED BACKGROUND
# # ============================================================

# def draw__background(screen):

#     global selected_background


#     # ========================================================
#     # ORIGINAL IMAGE SIZE
#     # ========================================================

#     image_width = selected_background.get_width()
#     image_height = selected_background.get_height()


#     # ========================================================
#     # SCALE
#     # نسبت تصویر حفظ می‌شود
#     # ========================================================

#     scale_x = SCREEN_WIDTH_ / image_width
#     scale_y = SCREEN_HEIGHT_ / image_height

#     scale = max(
#         scale_x,
#         scale_y
#     )


#     new_width = int(
#         image_width * scale
#     )

#     new_height = int(
#         image_height * scale
#     )


#     # ========================================================
#     # SCALE ORIGINAL IMAGE
#     # ========================================================

#     background = pygame.transform.smoothscale(
#         selected_background,
#         (
#             new_width,
#             new_height
#         )
#     )


#     # ========================================================
#     # CENTER
#     # ========================================================

#     x = (
#         SCREEN_WIDTH_ - new_width
#     ) // 2

#     y = (
#         SCREEN_HEIGHT_ - new_height
#     ) // 2 


#     # ========================================================
#     # DRAW
#     # ========================================================

#     screen.blit(
#         background,
#         (
#             x,
#             y
#         )
#     )
    
    
    
    
    
    
    
    
    
    
    
    #----------------------------------------------------------------
clock = pygame.time.Clock()

fps_font = pygame.font.Font(None, 35)
    #----------------------------------------------------------------





# این برای فلگ است 
show_flag = True
#---------------------------------







imm=pygame.image.load("./asset/image/background/FIND_OPERATOR_BACKGROUND.png")
imm = pygame.transform.scale(
    imm,
    screen.get_size()
)










#------------------------------------------ این برای پشت سوال است همون قلعه

image_back_quastion = pygame.image.load(
    "./asset/image/in_game/back_image.png"
).convert_alpha()

image_back_quastion = pygame.transform.smoothscale(
    image_back_quastion,
    (1200, 650)
)



















#---------------------------- برای قسمت مود که چند تا صفحه داره 
drag_start_x_GAME_MODE = None
dragging_GAME_MODE = False

current_page_GAME_MODE = 0

page_offset_GAME_MODE = 0

target_offset_GAME_MODE = 0



from modules.slide import *

game_mode_slide = PageSlide(
    screen.get_width(),
    pages=3
)





#این ها باید حذف بشن 
#-------------------------------- SHAPE_COLOR_NAME ببرای ای  قسمت است 
from modules.MODE.SHAPE_COLOR_NAME import * 
# new_question_SHAPE_COLOR_NAME()

one____(screen,current_width,current_height)



#---------------------------------------------REPEAT_AFTER_ME
from modules.MODE.REPEAT_AFTER_ME import *
new_round()


#---------------------------------------------DIRECTION_
from modules.MODE.DIRECTION import *
new_round_DIRECTION()

#---------------------------------------------DIRECTION_
from modules.MODE.ACTION import *
reset_game_ACTION()

#---------------------------------------------DIRECTION_
from modules.MODE.MIRROR import *
new_round_MIRROR()







#-------------------------------- country

from modules.profile import country as  CON
country = CON.load_flags()



#-------------------------------- save mecanizem
from modules.save.save import load_player

# قبل از while اصلی
player = load_player()


# if player is None:
#     game_state = "NAME"
# else:
#     game_state = "MENU"












#---------------------------------- برای گرفتن عکس از کامپیتور 
# import modules.profile.image_picker as PICK






from modules.policy import draw_privacy_policy

privacy_box = pygame.Rect(
    current_width // 2 - 550 + 180,
    current_height // 2 - 500 + 230,
    740,
    550
)


from modules.INFO import *
info_box = pygame.Rect(
    current_width // 2 - 370,
    current_height // 2 - 100,
    740,
    550
)




from modules.MODE.DETECT import *
from modules.MODE.FAST import *
from modules.MODE.MORE_LESS_EQUAL import *
from modules.MODE.SIX_60S import *
from modules.MODE.TRUE_FLASE import *
from modules.MODE.FIND_OPERATOR import *
from modules.background_moving import *



WIDTH, HEIGHT = screen.get_size()

dt = clock.tick(60) / 1000











from modules.transition import *
from modules.droping import *
from modules.punch_custom_play import *

from modules.zh import *   
icon_start_time = pygame.time.get_ticks()
icon_image__ = pygame.transform.smoothscale(pygame.image.load(
    "asset/image/droping/qq.png"
).convert_alpha(),(100,100))













#-----------------------------این برای بک گراند های مود های بازی است که باید بک گراند متحرک غیر فعال شود در آن زمان 
ON_BACKGROUND=None
DETECT_BACKGROUND=pygame.image.load("./asset/image/background/DETECT_BACKGROUND.png").convert_alpha()
FAST_BACKGROUND=pygame.image.load("./asset/image/background/FAST_BACKGROUND.png").convert_alpha()
SHAPE_COLOR_NAME_BACKGROUND=pygame.image.load("./asset/image/background/SHAPE_COLOR_NAME.png").convert_alpha()
ACTION_BACKGROUND=pygame.image.load("./asset/image/background/ACTION_BACKGROUND.png").convert_alpha()
DIRECTION_BACKGROUND=pygame.image.load("./asset/image/background/DIRECTION_BACKGROUND.png").convert_alpha()
MIRROR_BACKGROUND=pygame.image.load("./asset/image/background/MIRROR_BACKGROUND.png").convert_alpha()
REPEAT_AFTER_ME_BACKGROUND=pygame.image.load("./asset/image/background/REPEAT_AFTER_ME_BACKGROUND.png").convert_alpha()
MEMORY_BACKGROUND=pygame.image.load("./asset/image/background/MEMORY_BACKGROUND.png").convert_alpha()
FIND_NUMBER_BACKGROUND=pygame.image.load("./asset/image/background/FIND_NUMBER_BACKGROUND.png").convert_alpha()
MORE_LESS_EQUAL_BACKGROUND=pygame.image.load("./asset/image/background/MORE_LESS_EQUAL_BACKGROUND.png").convert_alpha()
_60S_BACKGROUND=pygame.image.load("./asset/image/background/_60S_BACKGROUND.png").convert_alpha()
TRUE_FALSE_BACKGROUND=pygame.image.load("./asset/image/background/TRUE_FALSE_BACKGROUND.png").convert_alpha()
FIND_OPERATOR_BACKGROUND=pygame.image.load("./asset/image/background/FIND_OPERATOR_BACKGROUND.png").convert_alpha()
CUSTOM__GAME=pygame.image.load("./asset/image/background/CUSTOM__GAME.png").convert_alpha()

#############################################################################################################
#############################################################################################################
game_state = "MENU" # این در شروع بازی باید نان باشد  که بالایی  مکانیزم سیو درست ش میکنه 
support_face = None
#aiden
# ############################################################################################################
#############################################################################################################
# Game loop ------------------------------------------------------------------------------------------------------------------------------------

while running:



    # ---------------------------------------------background
    # screen.blit(imm,(0,0))
    # ON_BACKGROUND=True
    # if ON_BACKGROUND:
        # draw_moving_map(
        #     screen,
        #     WIDTH,
        #     HEIGHT,
        #     dt    )
        # draw_flying_birds(
        #     screen,
        #     current_width,
        #     current_height
        # )   
    #---------------------------------------------------------------------Event_handler

    (
        running,
        player_name,
        name_entered,
        selected_profile,
        player_image,
        selected_image,
        operator,
        ceill,
        ceill_text,
        ceill_entered,
        time_limit,
        time_text,
        time_entered,
        answer_selected,
        game_state,
        select_buttons,
        settings_rects,
        back_button_rect,
        # selected_color,
        # dragging_hue,
        small_window,
        clicked_button,
        # music_on,
        # effect_on,
        language_rects,
        selected_profile_image,
        
        dragging,
        mouse_start_x,
        mouse_start_y,
        camera_x,
        camera_y,
        level_rects,
        # level_rects_for_theme,
        
        
        rect_for_music,
        music_state,
        
        sound_state,
        rect_for_sound,
        home_button_rect,askus_button_rect,share_button_rect
        ,
        
        option_rects
        ,
    
        start_time,
        current_question,
        correct_count,
        wrong_count,
        question_number
        
        
        ,
        # selected_background,
        dragging_GAME_MODE,
        drag_start_x_GAME_MODE,
        current_page_GAME_MODE,
        target_offset_GAME_MODE,
        
        
        
        support_face
        
        ) = handle_events(
            
            
            
            
            
            
            
            
            
        screen,
        player_name,
        name_entered,
        selected_profile,
        player_image,
        selected_image,
        profile_images,
        profile_rects,
        operator,
        operator_rects,
        ceill,
        ceill_text,
        ceill_entered,
        time_limit,
        time_text,
        time_entered,
        time_button_rects,
        ceill_button_rects,
        answer_rects,
        answer_selected,
        game_state,
        select_buttons,
        settings_rects,
        back_button_rect,
        # selected_color,
        # hue_bar,
        # dragging_hue,
        home_button_rect,
        # music_on,
        # effect_on
        small_window,
        clicked_button,
        language_rects,
        load_language,
        selected_profile_image,
        
        
        
        
        dragging,
        mouse_start_x,
        mouse_start_y,
        camera_x,
        camera_y,
        level_rects,
        # level_rects_for_theme,
        # level_images_theme,
        
        
        
        rect_for_music,
        music_state,
        
        sound_state,
        rect_for_sound,
        home_button_rect,askus_button_rect,share_button_rect,
        
        
        
        
        
        
        
        
        
        
        option_rects,
        generate_missing_number_question,
        
        
        
        
        
        
    
        start_time,
        current_question,
        correct_count,
        wrong_count,
        question_number  
        
        
        ,
        # selected_background,
    
        dragging_GAME_MODE,
        drag_start_x_GAME_MODE,
        current_page_GAME_MODE,
        target_offset_GAME_MODE,
        game_mode_slide,
        image_game_mode_page2,
        image_game_mode_page3,
        image_game_mode_page1,
        
        
        
        support_face
        )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        # آپدیت حرکت اسلاید
    game_mode_slide.update()


    # گرفتن مقدار حرکت
    offset = game_mode_slide.get_offset()

    
    
    
    
    
    
    #--------------------------------------------------------------------------------- first page that every one goes in 
    #---------------------------------------------------------------------------------NAME
    if game_state == "NAME":    
          
           
        if defult_language == True:
            load_language("en")
            defult_language=False
            
            
        # if selected_profile is None:
        #     draw_profile_circle(
        #         screen,
        #         default_profile,
        #         (current_width//2, 200),
        #         250
        #     )
        # else:
        #     draw_profile_circle(
        #         screen,
        #         selected_image,
        #         (current_width//2, 200),
        #         250
        #     )    
            
            
            
                    
        # draw_name_screen(
        #     screen,
        #     fonts,
        #     player_name,
        #     input_box,
        #     enter_button
        # )
        

        # draw_profiles(
        #     screen,
        #     profile_images,
        #     profile_rects,
        #     profile_area
        # )
        
        # draw_profile_circle(
        #     screen,
        #     selected_image,
        #     (
        #         current_width // 2,
        #         100
        #     ),
        # )
        
        




            
        #-------------------------------------- flag 
        # CON.draw_country_button(
        #     screen,
        #     CON.country_button,
        #     CON.selected_country
        # )


        # if CON.country_window:

        #     CON.draw_country_window(
        #         screen,
        #         country,
        #         CON.country_rects
        #     )
           
           
        # CON.draw_selected_flag(
        #     screen,
        #     country,
        #     CON.selected_country
        # ) 
    #--------------------------------------


    STATE(screen,game_state,current_width,current_height)

    LEVELS(screen,game_state,current_width,current_height)


           
        
    #---------------------------------------------------------------------------------LANGUAGE
    if game_state == "LANGUAGE":
        image_setter(screen,background_Lan,current_width // 2 - 720 ,current_height // 2 -360 )

        language_rects = draw_languages(
            screen,
            current_width,
            current_height
        )
        menu_cache.clear()

                        # عکس دایره. برای پروفایل هر صفحه
        image_setter(screen,pathth,xyz_for_profile_logo,current_height//2 - 666)
        gif_setting(screen,gif_frames_lan,width_for_profile_logo,current_height // 2 - 570)
        

        draw_back_button(
            screen,
            back_button_rect)
        support_button(
            screen,
            support_button_rect
        )      
        
    #---------------------------------------------------------------------------------SUPPORT


    # #---------------------------------------------------------------------------------about
    # if game_state == "ABOUT":
        
    #     draw_about(
    #         screen
    #     )



    #---------------------------------------------------------------------------------sound
    if game_state == "SOUND":


        # image_background(screen,square_rect)
        # screen.blit(sound_bg, (x,y))

        sound_screen(screen)
        draw_back_button(
            screen,
            back_button_rect
        )
        
        support_button(
        screen,
        support_button_rect
    )

        # bug_button(
        #     screen,
        #     bug_button_rect
        # )      
        call_support(
            screen,
            call_button_rect
        )
        
                # عکس دایره. برای پروفایل هر صفحه
        image_setter(screen,pathth,xyz_for_profile_logo,current_height//2 - 666)
        gif_setting(screen,gif_frames_sound,width_for_profile_logo,current_height // 2 - 570)



        # رسم عکس بر اساس حالت
        if music_state == 0:

            screen.blit(
                image_off,
                rect_for_music
            )


        else:

            screen.blit(
                image_on,
                rect_for_music
            )


        # رسم عکس بر اساس حالت
        if sound_state == 0:

            screen.blit(
                sound_off,
                rect_for_sound
            )

        else:

            screen.blit(
                sound_on,
                rect_for_sound
            )
    #---------------------------------------------------------------------------------theme
    # if game_state == "THEME":
        

    #                     # عکس دایره. برای پروفایل هر صفحه
    #     image_setter(screen,pathth,current_width//2 - 220,current_height//2 - 666)

    #     gif_setting(screen,gif_frames_theme,current_width // 2 - 246 // 2,current_height // 2 - 1068     // 2)

    #     draw_back_button(
    #         screen,
    #         back_button_rect)
    #     support_button(
    #         screen,
    #         support_button_rect
    #     )      
    #     # draw_theme(screen)

    #     # draw_theme(screen, 450, 300)
    #     THEME_DRAW(screen,WORLD_WIDTH_,SCREEN_WIDTH_,WORLD_HEIGHT_,SCREEN_HEIGHT_,level_world_)
        
        
        
        
        
        
        



            #   برای اضافه کردن سقف  اعداد
            
    if game_state == "CEILL":        
        
        

        draw_new_screen(screen)
        

        _window(screen,small_window)



        draw_ceil_screen(
            screen,
            fonts,
            current_width,
            current_height
        )
            
                 
        draw_back_button(
            screen,
            back_button_rect
        )
        
        
        support_button(
            screen,
            support_button_rect
        )
        

        image_setter(screen,pathth,xyz_for_profile_logo,current_height//2 - 666)
        gif_setting(screen,gif_frames_credit,width_for_profile_logo,current_height // 2 - 570)
        draw_profile_live_circle(
            screen,
            selected_profile_image,
            p99,
            current_width
        )
        call_support(
            screen,
            call_button_rect
        )
        
        
        
        
        

        
        
        
        
        
        
        
    #--------------------------------------------------------------------------------------------------


    if game_state == "SUPPORT":
        #----------------- background_and_brids
        draw_moving_map(
            screen,
            WIDTH,
            HEIGHT,
            dt    )
        draw_flying_birds(
            screen,
            current_width,
            current_height
        )   
    
        
        draw_4_images_SUPPORT(screen)        

                        # عکس دایره. برای پروفایل هر صفحه
        image_setter(screen,pathth,xyz_for_profile_logo,current_height//2 - 666)
        gif_setting(screen,gif_frames_support,width_for_profile_logo,current_height // 2 - 570)

        draw_back_button(
            screen,
            back_button_rect)

        if support_face == "Report Bug":
             draw_support_face(screen,current_width,current_height)
        if support_face == "Feed Back":
             draw_support_face(screen,current_width,current_height)
        if support_face == "Contact Us":
             draw_support_face(screen,current_width,current_height)
        if support_face == "Donate":
             draw_support_face(screen,current_width,current_height)

        
        
        
    #--------------------------------------------------------------------------------------------------


    if game_state == "MORE":
        
        draw_4_images_MORE(screen)        


        draw_back_button(
            screen,
            back_button_rect)
        
        support_button(
            screen,
            support_button_rect
        )
        

        
        # عکس دایره. برای پروفایل هر صفحه
        image_setter(screen,pathth,xyz_for_profile_logo,current_height//2 - 666)
        gif_setting(screen,gif_frames_about,width_for_profile_logo,current_height // 2 - 570)

        if support_face == "How to Play":
             draw_support_face(screen,current_width,current_height)
        if support_face == "FAQ":
             draw_support_face(screen,current_width,current_height)
        if support_face == "INFO":
             draw_support_face(screen,current_width,current_height)
            #  draw_info_profile(
            #     screen,
            #     current_width,
            #     current_height
            #     )
             draw_info(
                screen,
                info_box
                )
        if support_face == "Privacy Policy":
             draw_support_face(screen,current_width,current_height)
             draw_privacy_policy(screen,privacy_box)
             

             
        
        
        
        
        
    #--------------------------------------------------------------------------------------------------
    if game_state == "PROFILE":
        

        #----------------- background_and_brids
        draw_moving_map(
            screen,
            WIDTH,
            HEIGHT,
            dt    )
        draw_flying_birds(
            screen,
            current_width,
            current_height
        )   
    
    
    
    
    
    
    
    
    
        draw_back_button(
            screen,
            back_button_rect
        )
        
        support_button(
            screen,
            support_button_rect
        )

        # bug_button(
        #     screen,
        #     bug_button_rect
        # )   
        call_support(
            screen,
            call_button_rect
        )
        draw_profile_in_profile_tab(
            screen,
            selected_profile_image,
            p999,
            current_width,
            current_height
        )

                                # عکس دایره. برای پروفایل هر صفحه
        image_setter(screen,pathth,xyz_for_profile_logo,current_height//2 - 666)
        gif_setting(screen,gif_frames_profile,width_for_profile_logo,current_height // 2 - 570)


















#-------------------------------------------------------------



    if game_state == "MUSIC":
        #----------------- background_and_brids
        draw_moving_map(
            screen,
            WIDTH,
            HEIGHT,
            dt    )
        draw_flying_birds(
            screen,
            current_width,
            current_height
        )   
    
    
    
    
    
    
    
    
        draw_music(
            screen,
            current_width,
            current_height,
            background_music,
            profile_image
        )
        
        draw_back_button(
            screen,
            back_button_rect
        )
        support_button(
            screen,
            support_button_rect
        )
        # bug_button(
        #     screen,
        #     bug_button_rect
        # )     
        call_support(
            screen,
            call_button_rect
        )
        image_setter(screen,pathth,xyz_for_profile_logo,current_height//2 - 666)
        gif_setting(screen,gif_frames_music,width_for_profile_logo,current_height//2 - 570)




#---------------------------------- game mode   

    if game_state == "GAME MODE":
        
        #----------------- background_and_brids
        draw_moving_map(
            screen,
            WIDTH,
            HEIGHT,
            dt    )
        draw_flying_birds(
            screen,
            current_width,
            current_height
        )   
    

        
        
        
        
        draw_burst_icon(
            screen,
            icon_image__,
            current_width // 2,
            current_height // 2
        )
        
        # آپدیت اسلاید
        game_mode_slide.update()

        offset = game_mode_slide.get_offset()

        if offset == 0:
            current_page_GAME_MODE = 0

        elif offset == -screen.get_width():
            current_page_GAME_MODE = 1

        elif offset == -screen.get_width() * 2:
            current_page_GAME_MODE = 2



        # رسم صفحه‌ها
        draw_image_MODE_page_1(
            screen,
            500,
            500,
            offset
        )

        draw_image_MODE_page_2(
            screen,
            500,
            500,
            offset + screen.get_width()
        )
        
        draw_image_MODE_page_3(
            screen,
            500,
            500,
            offset + screen.get_width() * 2,
            icons
            
        )
        
        
        
        draw_page_indicator(
            screen,
            current_page_GAME_MODE,
            3,
            screen.get_height() - 80
        )
    # if game_state == "GAME MODE":
    #     if current_page_GAME_MODE == 0:
    #         # draw_image_MODE_page_1(screen,500,500)        

    #         draw_image_MODE_page_1(
    #             screen,
    #             400,
    #             300,
    #             current_page_GAME_MODE,
    #             page_offset_GAME_MODE
    #         )


    #     elif current_page_GAME_MODE == 1:
    #         draw_image_MODE_page_2(screen,500,500)        


    #         draw_image_MODE_page_2(
    #             screen,
    #             400,
    #             300,
    #             current_page_GAME_MODE,
    #             page_offset_GAME_MODE
    #         )
            
        
        # draw_card(screen,square_rect)

            
    # gallery_button(
        #     screen,
        #     gallery_button_rect
        # )
        _window(screen,small_window)


        draw_back_button(
        screen,
        back_button_rect
        )
        support_button(
            screen,
            support_button_rect
        )
        # bug_button(
        #     screen,
        #     bug_button_rect
        # )     
        call_support(
            screen,
            call_button_rect
        )
        
        draw_profile_live_circle(
            screen,
            selected_profile_image,
            p99,
            current_width
        )
        # عکس دایره. برای پروفایل هر صفحه
        image_setter(screen,pathth,xyz_for_profile_logo,current_height//2 - 666)
        gif_setting(screen,gif_frames_mode,width_for_profile_logo,current_height // 2 - 570)





    if game_state == "MEMORY":
        memory_(
            screen,
            current_width,
            current_height
        )
        
    #---------------------------------------------------------------------------------STEP5

    # if ceill_entered and not time_entered:        
    if game_state == "TIME":

        
        square_rect = pygame.Rect(
            current_width // 2 - 800 // 2,
            current_height // 2 - 450 // 2,
            800,
            450
        )
        draw_new_screen(screen)

                
       # gallery_button(
        #     screen,
        #     gallery_button_rect
        # )
        _window(screen,small_window)





        draw_time_screen(
            screen,
            fonts,
            time_button_rects,
            current_width,
            current_height
        )
                 
        draw_back_button(
            screen,
            back_button_rect
        )


        support_button(
            screen,
            support_button_rect
        )

        # bug_button(
        #     screen,
        #     bug_button_rect
        # )
        call_support(
            screen,
            call_button_rect
        )
        #-------------------------gif for time
        image_setter(screen,pathth,xyz_for_profile_logo,current_height//2 - 666)
        gif_setting(screen,gif_frames,width_for_profile_logo,current_height // 2 - 570)
        
        draw_profile_live_circle(
            screen,
            selected_profile_image,
            p99,
            current_width
        )
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    # if game_state == "PLAY ONLINE":
    #     print("online on the way...")
        
        
        
        


        
        
        




    # page 1
   #----------------------------------------------------------------------------------------------------------------
   #----------------------------------------------------------------------------------------------------------------
   #----------------------------------------------------------------------------------------------------------------
    if game_state == "MEMORY":
        back_setter(screen,MEMORY_BACKGROUND)

        memory_(
            screen,
            current_width,
            current_height
        )
        
        draw_back_button(
            screen,
            back_button_rect
        )
    #--------------------------------------------------------------------------------
    if game_state == "SHAPE_COLOR_NAME":
                
        back_setter(screen,SHAPE_COLOR_NAME_BACKGROUND)
        SHAPE_COLOR_NAME(screen,current_width)
        
        draw_back_button(
            screen,
            back_button_rect
        )
    #--------------------------------------------------------------------------------
    if game_state == "REPEAT_AFTER_ME":
        back_setter(screen,REPEAT_AFTER_ME_BACKGROUND)
        REPEAT_AFTER_ME_(screen)
        
        
        draw_back_button(
            screen,
            back_button_rect
        )
    #--------------------------------------------------------------------------------
    if game_state == "DIRECTION":
        back_setter(screen,DIRECTION_BACKGROUND)

        DIRECTION_(screen)
        
        
        draw_back_button(
            screen,
            back_button_rect
        )
    # #--------------------------------------------------------------------------------
    if  game_state == "MIRROR":
        back_setter(screen,MIRROR_BACKGROUND)

        MIRROR_(screen)

        draw_back_button(
            screen,
            back_button_rect
        )
    #--------------------------------------------------------------------------------
    if game_state =="ACTION":
        back_setter(screen,ACTION_BACKGROUND)

        ACTION_(screen)
        draw_back_button(
            screen,
            back_button_rect
        )

    
    # page 2
   #----------------------------------------------------------------------------------------------------------------
   #----------------------------------------------------------------------------------------------------------------
   #----------------------------------------------------------------------------------------------------------------
    if game_state == "FIND_NUMBER":
        back_setter(screen,FIND_NUMBER_BACKGROUND)


        # ---------------- Timer Calculation ----------------

        elapsed = (
            pygame.time.get_ticks() - start_time
        ) / 1000

        progress = 1 - (
            elapsed / current_question["time"]
        )

        progress = max(0, min(1, progress))


        # ---------------- Question Background ----------------

        image_setter(
            screen,
            image_back_quastion,
            current_width // 2 - 600,
            current_height // 2 - 550
        )


        # ---------------- Hint ----------------

        hint(screen)


        # ---------------- Save ----------------

        save(screen)


        # ---------------- Question ----------------

        option_rects = draw_question_find_number(
            screen,
            fonts,
            current_question,
            current_width,
            current_height
        )


        # ---------------- Timer Circle ----------------

        draw_timer_circle(
            screen,
            (160, 160),
            80,
            progress
        )


        # ---------------- Timeout ----------------

        if elapsed >= current_question["time"]:

            wrong_count += 1

            question_number += 1

            current_question = generate_missing_number_question(
                question_number
            )

            start_time = pygame.time.get_ticks()


        # ---------------- Score ----------------

        correct_text = fonts["name"].render(
            f"Correct: {correct_count}",
            True,
            (0, 255, 0)
        )

        wrong_text = fonts["name"].render(
            f"Wrong: {wrong_count}",
            True,
            (255, 0, 0)
        )


        screen.blit(
            correct_text,
            (50, 50)
        )

        screen.blit(
            wrong_text,
            (300, 50)
        )


        # ---------------- Player ----------------

        draw_profile_live_circle(
            screen,
            selected_profile_image,
            p99,
            current_width
        )


        # ---------------- UI ----------------

        in_game_alarm(screen)

        move_flage(
            screen,
            current_width // 2 - 154,
            show_flag
        )

        menuu(screen)

        restart(screen)

        tomar(screen)

        draw_back_button(
            screen,
            back_button_rect
        )
            # # ---------------- Remaining Time ---------------- عدد تایم

            # remaining_time = max(
            #     0,
            #     current_question["time"] - int(elapsed)
            # )


            # timer_text = fonts["heart"].render(
            #     f"{remaining_time}",
            #     True,
            #     (255, 255, 0)
            # )


            # screen.blit(
            #     timer_text,
            #     (current_width // 2 - 10 ,current_height // 2+ 430)
            # )


    #---------------------------------------------------------------------------------x?y
    if game_state == "60S":
        back_setter(screen,_60S_BACKGROUND)

        
        SIX_60S(screen,current_width)
        
        
        
        
        
        draw_profile_live_circle(
            screen,
            selected_profile_image,
            p99,
            current_width
        )
        in_game_button(
            screen,
            home_button_rect,
            menu
        )
        draw_back_button(
            screen,
            back_button_rect
        )

    #---------------------------------------------------------------------------------x(+-/*)y
    if game_state == "MORE_LESS_EQUAL":
        back_setter(screen,MORE_LESS_EQUAL_BACKGROUND)

        MORE_LESS_EQUAL_(screen)
        draw_profile_live_circle(
            screen,
            selected_profile_image,
            p99,
            current_width
        )
        in_game_button(
            screen,
            home_button_rect,
            menu
        )
        draw_back_button(
            screen,
            back_button_rect
        )

    #--------------------------------------------------------------------------------->=<
    if game_state == "TRUE_FALSE":
        back_setter(screen,TRUE_FALSE_BACKGROUND)

        TRUE_FALSE_(screen)
        draw_profile_live_circle(
            screen,
            selected_profile_image,
            p99,
            current_width
        )
        in_game_button(
            screen,
            home_button_rect,
            menu
        )
        draw_back_button(
            screen,
            back_button_rect
        )
        

    #--------------------------------------------------------------------------------->=<
    if game_state == "FIND_OPERATOR":
        back_setter(screen,FIND_OPERATOR_BACKGROUND)

        FIND_OPERATOR_(screen)
        draw_profile_live_circle(
            screen,
            selected_profile_image,
            p99,
            current_width
        )
        in_game_button(
            screen,
            home_button_rect,
            menu
        )
        draw_back_button(
            screen,
            back_button_rect
        )
        
    #--------------------------------------------------------------------------------
    if game_state =="DETECT":
        back_setter(screen,DETECT_BACKGROUND)

        print("this is detect")
        # این منطقش اشتباه است  زمانی که غلط میزنی در بازی 
        DETECT_(screen,current_width,current_height)


        draw_back_button(
            screen,
            back_button_rect
        )

    # page 3
   #----------------------------------------------------------------------------------------------------------------
   #----------------------------------------------------------------------------------------------------------------
   #----------------------------------------------------------------------------------------------------------------


    
    if game_state =="FAST":
        back_setter(screen,FAST_BACKGROUND)

        FAST_(screen,current_width)
        draw_back_button(
            screen,
            back_button_rect
        )


        draw_back_button(
            screen,
            back_button_rect
        )




















    #---------------------------------------------------------------------------------GAME ---> LEVELS
    if  game_state == "LEVELS":

        keys = pygame.key.get_pressed()


        if keys[pygame.K_RIGHT]:
            camera_x += 10


        if keys[pygame.K_LEFT]:
            camera_x -= 10


        if keys[pygame.K_DOWN]:
            camera_y += 10


        if keys[pygame.K_UP]:
            camera_y -= 10



        camera_x = max(
            0,
            min(camera_x, WORLD_WIDTH - SCREEN_WIDTH)
        )


        camera_y = max(
            0,
            min(camera_y, WORLD_HEIGHT - SCREEN_HEIGHT)
        )



        screen.blit(
            level_world,
            (0,0),
            (
                camera_x,
                camera_y,
                SCREEN_WIDTH,
                SCREEN_HEIGHT
            )
        )
        # update_level_slider(
        #     level_slider
        # )


        # draw_level_slider(
        #     screen,
        #     level_slider,
        #     (
        #         current_width//2,
        #         current_height//2
        #     )
        # )
            
            
        # draw_new_screen(screen)                 
        draw_back_button(
            screen,
            back_button_rect
        )
        support_button(
            screen,
            support_button_rect
        )
        # bug_button(
        #     screen,
        #     bug_button_rect
        # )
        call_support(
            screen,
            call_button_rect
        )
                # عکس دایره. برای پروفایل هر صفحه
        image_setter(screen,pathth,xyz_for_profile_logo,current_height//2 - 666)
        gif_setting(screen,gif_frames_levels,width_for_profile_logo,current_height // 2 - 570)

        draw_profile_live_circle(
            screen,
            selected_profile_image,
            p99,
            current_width
        )
    #---------------------------------------------------------------------------------GAME ---> PLAY
    # if game_state == "PUNCH":

    if  game_state == "CUSTOM GAME":

        back_setter(screen,CUSTOM__GAME)







        in_game_button(
            screen,
            home_button_rect,
            menu
        )
        in_game_button(
            screen,
            askus_button_rect,
            askus
        )
        in_game_button(
            screen,
            share_button_rect,
            share
        )
        # ---------------- Show Time Limit ----------------

        elapsed = pygame.time.get_ticks() - question_start_time


        progress = 1 - (
            elapsed / (time_limit * 1000)
        )


        progress = max(0, min(1, progress))


        timer_rect = pygame.Rect(
            current_width - 320,
            25,
            280,
            35
        )


        draw_profile_live_circle(
            screen,
            selected_profile_image,
            p99,
            current_width
        )
                 
        
  # ---------------- Timer Icon ----------------

  
        timer_rect = pygame.Rect(
            current_width // 2 -120,
            current_height // 2 - 329,
            280,
            35
        )


        draw_timer_bar(
            screen,
            timer_rect,
            progress
        )

        # if timer_icon:

        #     icon_rect = timer_icon.get_rect(
        #         center=(
        #             timer_rect.left - 35,
        #             timer_rect.centery
        #         )
        #     )

        #     screen.blit(
        #         timer_icon,
        #         icon_rect
        #     )
            
  



        # ---------------- Score Display ----------------
    
        score_text = fonts["name"].render(
            str(score),
            True,
            (255,220,0)
        )


        score_rect = score_text.get_rect(
            midleft=(
                current_width // 2 + 35,
                45
            )
        )


        # icon_rect = score_icon.get_rect(
        #     center=(
        #         current_width // 2,
        #         45
        #     )
        # )


        # screen.blit(
        #     score_icon,
        #     icon_rect
        # )


        screen.blit(
            score_text,
            score_rect
        )






    #------------------------------------ موتور بازی 

        (
        question_started,
        question_text,
        question_start_time,
        remaining_time,
        result,
        score,
        answers,
        answer_rects,
        answer_selected
    ) = run_game(
        screen,
        fonts,
        current_width,
        current_height,

        player_name,
        selected_profile,
        profile_images,

        ceill,
        operator,
        time_limit,

        question_started,
        question_text,
        question_start_time,
        remaining_time,

        result,
        score,
        answers,
        answer_rects,
        answer_selected,
                

    )
    
    
    
    
    
    
    
    
    
    #------------------------ این  برای اف پی اس است 
    
    fps = clock.get_fps()

    fps_text = fps_font.render(f"FPS: {int(fps)}", True, (255,255,255))

    screen.blit(fps_text, (20,20))
        
    #------------------ Update ------------------
    # بروزرسانی صفحه نمایش
    pygame.display.update()
    # محدود کردن بازی به 60 فریم در ثانیه
    clock.tick(60)









# بستن pygame
pygame.quit()
# خروج کامل از برنامه
sys.exit()








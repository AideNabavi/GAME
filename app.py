import pygame
import importlib
from modules.loading import *

pygame.init()

# ==================================================
# Loading Window
# ==================================================

screen = pygame.display.set_mode(
    (960, 540)
)
pygame.display.set_caption(
    "Fast Mathter"
)

icon = pygame.image.load(
    "asset/image/icon.png"
).convert_alpha()
pygame.display.set_icon(icon)



#loading for loading window
LOADING(screen)



# ==================================================
# Start Loading
# ==================================================
pygame.mixer.init()

pygame.mixer.music.play()
pygame.mixer.music.stop()


screen = pygame.display.set_mode(
    (1920, 1080),
    pygame.FULLSCREEN
)


pygame.display.set_caption(
    "Fast Mathter"
)

pygame.display.set_icon(
    icon
)


# ==================================================
# IMPORT
# ==================================================

import sys
from event_handler import handle_events
from modules.time_screen import draw_time_screen
from modules.game_engine import run_game
from modules.timer import draw_timer_circle
from modules.window import _window
from modules.button import *
from modules.ab import *
from modules.design import *
from modules.language import *
from modules.sound import *
from modules.font import *
from modules.player_profile import *
from modules.screen import *
from modules.theme import *
from modules.design import *
from modules.LEVELS.LEVELS import *
from modules.ceill_screen import *
from modules.profile_ import draw_profile_live_circle
from modules.mode  import *
from modules.support  import *
from modules.more  import *
from modules.MODE.FIND_NUMBER  import *
from modules.MODE.MEMORY  import *
from modules.MODE.REPEAT_AFTER_ME  import *
from modules.MODE.MORE_LESS_EQUAL  import *
from modules.profile_ import  *
from modules.profile import  *
from modules.music import *
from modules.operation_screen import *
from modules import design as DES


# from modules.date import date
from modules.save import save as SAVE
from modules.save import popular_game as popular_game
from modules.MODE import IMAGE_SELECT as IMSE
from modules.MODE import FIND_NUMBER as FNUM



# ---------------------------------------------------------- متغیر های حیاتی 
# برای کنترل سرعت اجرای بازی
clock = pygame.time.Clock()
current_width, current_height = screen.get_size()
running = True
support_face = None
info = pygame.display.Info()













# این برای موزیک است عوض کردن موزیک

music_profile_image = pygame.image.load(
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

#------------------------------------------------------------- Score


score = 0

answers = []

answer_rects = {}

answer_selected = None

answer_clicked = False

#------------------------------------------------------------- profile





# عکس انتخاب شده اولیه
selected_image = load_default_profile()
profile_images = load_profile_images()

# متغیرهای دیگر پروفایل
profile_rects = {}

profile_hovered = {}


#------------------------------------------------------------- برای مد بازی   

clicked_button = False



#------------------------------------------------------------- حلقه

profile_scroll = 0

profile_area = pygame.Rect(
    100,
    250,
    550,
    220
)

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

#-------------------------------------------------------------


from modules.slid_effect import *



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



# def draw_languages(screen, current_width, current_height):

#     global lan_sizes

#     rects = []

#     mouse_pos = pygame.mouse.get_pos()

#     for i, (lang, x, y) in enumerate(language_data):

#         rect = lan_images[i].get_rect(
#             topleft=(x, y)
#         )

#         image, image_rect, lan_sizes[i] = hover_image_lan(
#             lan_images[i],
#             rect,
#             mouse_pos,
#             lan_sizes[i]
#         )

#         screen.blit(
#             image,
#             image_rect
#         )

#         rects.append((lang, image_rect))

#     return rects









def reset_side_effect_language():

    global side_effect_start_times
    global side_effect_order
    global side_effect_initialized

    side_effect_start_times.clear()

    side_effect_order = []

    side_effect_initialized = False
    
    
    
    
    
    
    
    
    
    
    
    
def draw_languages(
    screen,
    current_width,
    current_height
):

    global lan_sizes

    rects = []

    mouse_pos = pygame.mouse.get_pos()


    # ========================================================
    # LANGUAGES
    # ========================================================

    for i, (lang, x, y) in enumerate(language_data):


        # ====================================================
        # ORIGINAL RECT
        # ====================================================

        rect = lan_images[i].get_rect(
            topleft=(x, y)
        )


        # ====================================================
        # HOVER
        # ====================================================

        image, image_rect, lan_sizes[i] = hover_image_lan(

            lan_images[i],

            rect,

            mouse_pos,

            lan_sizes[i]

        )


        # ====================================================
        # RANDOM SIDE EFFECT
        # ====================================================

        draw_random_side_effect(

            screen,

            image,

            image_rect.centerx,

            image_rect.centery,

            i,

            len(lan_images)

        )


        # ====================================================
        # RECT FOR CLICK
        # ====================================================

        rects.append(
            (
                lang,
                image_rect
            )
        )


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

    
# #----------------------------------------------------------------




# level=None



# SCREEN_WIDTH = info.current_w
# SCREEN_HEIGHT = info.current_h

# WORLD_WIDTH = 5000
# WORLD_HEIGHT = SCREEN_HEIGHT
# level_world = pygame.Surface(
#     (WORLD_WIDTH, WORLD_HEIGHT),
#     pygame.SRCALPHA
# )

# level_images_1 = [
#     pygame.image.load("./asset/image/levels/1.png").convert_alpha(),
#     pygame.image.load("./asset/image/levels/2.png").convert_alpha(),
#     pygame.image.load("./asset/image/levels/3.png").convert_alpha(),
#     pygame.image.load("./asset/image/levels/1.png").convert_alpha(),
#     pygame.image.load("./asset/image/levels/2.png").convert_alpha(),
#     pygame.image.load("./asset/image/levels/3.png").convert_alpha(),
#     pygame.image.load("./asset/image/levels/1.png").convert_alpha(),
#     pygame.image.load("./asset/image/levels/2.png").convert_alpha(),
#     pygame.image.load("./asset/image/levels/3.png").convert_alpha(),
#     pygame.image.load("./asset/image/levels/3.png").convert_alpha()
# ]


# level_positions = [
# (0,200),
# (500,200),
# (1000,200),
# (1500,200),
# (2000,200),
# (2500,200),
# (3000,200),
# (3500,200),
# (4000,200),
# (4500,200)
# ]

# for img, pos in zip(level_images_1, level_positions):

#     img = pygame.transform.smoothscale(
#         img,
#         (300,300)
#     )

#     level_world.blit(
#         img,
#         pos
#     )


# camera_x = 0
# camera_y = 0





dragging = False

# mouse_start_x = 0
# mouse_start_y = 0








# level_rects = []


# for index, (img, pos) in enumerate(zip(level_images_1, level_positions)):

#     img = pygame.transform.smoothscale(
#         img,
#         (300,300)
#     )


#     rect = img.get_rect(
#         topleft=pos
#     )


#     level_rects.append(
#         (index + 1, rect)
#     )


#     level_world.blit(
#         img,
#         pos
#     )
    
    
    

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














support_button_rect = pygame.Rect(
    30,  # فاصله از راست
    current_height + 177,                   # فاصله از بالا
    150,
    150
)


#-----------------------------

#donate
call_button_rect= pygame.Rect(
    1850,  # فاصله از راست
    current_height  - 177,                   # فاصله از بالا
    150,
    150
)

#support
support__button_rect= pygame.Rect(
    1850,  # فاصله از راست
    current_height  - 370,                   # فاصله از بالا
    150,
    150
)

store__button_rect= pygame.Rect(
    1850,  # فاصله از راست
    current_height  - 570,                   # فاصله از بالا
    150,
    150
)




#----------------------------- دکمه برگشت

back_button_rect = pygame.Rect(
    1850,
    20,
    150,
    150
)




    
############################################## مربوط به صفحه منو
small_window=""
select_buttons = []
select_button_clicked = False







##############################################برای  تب ستینگ                    تنظمیات بازی   

settings_rects = []








##############################################  for  Operation  tab

operator = ""

operator_rects={}
operator_images = {

    "+": pygame.transform.smoothscale(
        pygame.image.load("./asset/image/signs/plus.png").convert_alpha(),
         (400, 400)
    ),

    "-": pygame.transform.smoothscale(
        pygame.image.load("./asset/image/signs/minus.png").convert_alpha(),
         (400, 400)
    ),

    "*": pygame.transform.smoothscale(
        pygame.image.load("./asset/image/signs/multiply.png").convert_alpha(),
         (400, 400)
    ),

    "/": pygame.transform.smoothscale(
        pygame.image.load("./asset/image/signs/divide.png").convert_alpha(),
         (400, 400)
    )

}


    
    
    
    
    
    
    #----------------------------------------------------------------
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








#---------------- برای ایمیل 


from modules import player_profile  as PLAYER

enter_button = pygame.Rect(
    current_width // 2 - 75,
    input_y + 130,
    150,
    55
)




#---------------------------- برای قسمت مود که چند تا صفحه داره 
drag_start_x_GAME_MODE = None
dragging_GAME_MODE = False


page_offset_GAME_MODE = 0

target_offset_GAME_MODE = 0



from modules.slide import *

game_mode_slide = PageSlide(
    screen.get_width(),
    pages=6
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






from modules.MODE import FAST_ADD_SUB as  FAS

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
from modules.custom_math import *

from modules.zh import *   
icon_start_time = pygame.time.get_ticks()
icon_image__ = pygame.transform.smoothscale(pygame.image.load(
    "asset/image/droping/qq.png"
).convert_alpha(),(100,100))




from modules.save import recent_game as recent_game


#--------------- برای انتخاب عکس پاپیولر گیم است
recent_game.selected_images = recent_game.choose_three_random_images()
#--------------------------------------------------------- HOW MANY GAME PAGE 3
#--------------- برای انتخاب عکس پاپیولر گیم است
popular_game.selected_images = popular_game.choose_three_random_images()
#--------------------------------------------------------- HOW MANY GAME PAGE 3

from modules.MODE import HOW_MANY as HOW

from modules.MODE import HARD as HARD
from modules.MODE import DETECT_PRO as DPRO
from modules.MODE import FOLLOW_THAT as FOTHAT

from modules.MODE import MEMORY_GO as MEMGO


from modules.MODE import MOVE_ARROW as M_ARR
from modules.MODE import MATH_GO as MATHGO



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


#-------------------------- for game start
countdown_done = False
previous_game_state = None
from modules.start_game import countdown
from modules.effect import *
from modules.exit import *
from modules.button_setting import *
from modules import music as MUS
from modules import mode as MO
from modules import start_screen as STS
from modules import typer as TYPER
from modules import date as DA
from modules import menu__ as MENU__

#------------------------------------------------------------------------ پرچم ها 
#flage  in the game 
flag_in_game = pygame.image.load("./asset/image/in_game/flage.png").convert_alpha()
#flage in menu
flag_in_menu= pygame.transform.smoothscale(pygame.image.load("./asset/image/in_game/flaginthegame.png").convert_alpha(),(1600,1100))


#--------------------------------blur effect

#############################################################################################################
#############################################################################################################

game_state = "MENU"
SUPPORT_MENU=None
SUPPORT_window=None # for window  for each item (4 icon in support button )
EXIT_OK=None
CUSTOM_MATH=None
ONLINE_FLAG=None
DAILY_GAME=None
DASHBOARD=True
online_state=False
menu_state=None
DAILY_BUTTON=None
setting_menu=None
is_guest = None
# برای موزیک است 
control_every_button_in_setting_on_or_off= None

restart_OFF_ON_game=None
# ############################################################################################################
#############################################################################################################
# Game loop ------------------------------------------------------------------------------------------------------------------------------------



# ---------------------------------------------------------- این برای سیو است save

saved_player = SAVE.load_player()

if saved_player is not None:


    game_state = "MENU"#start

else:

    game_state = "MENU"#name
    


#-------------------------------- حلقه
while running:



    # (
    #     running,screen,
    #     player_name,
    #     name_entered,
    #     selected_profile,
    #     player_image,
    #     selected_image,
    #     operator,
    #     ceill,
    #     ceill_text,
    #     ceill_entered,
    #     time_limit,
    #     time_text,
    #     time_entered,
    #     answer_selected,
    #     game_state,
    #     select_buttons,
    #     settings_rects,
    #     back_button_rect,
    #     # selected_color,
    #     # dragging_hue,
    #     small_window,
    #     clicked_button,
    #     # music_on,
    #     # effect_on,
    #     language_rects,
    #     selected_profile_image,
        
    #     dragging,
    #     # mouse_start_x,
    #     # mouse_start_y,
    #     # camera_x,
    #     # camera_y,
    #     # level_rects,
    #     # level_rects_for_theme,
        
        
    #     rect_for_music,
    #     music_state,
        
    #     sound_state,
    #     rect_for_sound,
    #     home_button_rect,askus_button_rect,share_button_rect
    #     ,
        
    #     option_rects
    #     ,
    
    #     start_time,
    #     current_question,
    #     correct_count,
    #     wrong_count,
    #     question_number
        
        
    #     ,
    #     # selected_background,
    #     dragging_GAME_MODE,
    #     drag_start_x_GAME_MODE,
    #     target_offset_GAME_MODE,
        
        
        
    #     support_face,
    #     SUPPORT_MENU,
    #     SUPPORT_window,
        
    #     EXIT_OK,
    #     CUSTOM_MATH,
    #     ONLINE_FLAG,
    #     DAILY_GAME,
    #     menu_state,
    #     DAILY_BUTTON,
    #     setting_menu,control_every_button_in_setting_on_or_off,DASHBOARD,online_state,is_guest
    #     # old_screen
    #     ) = handle_events(
            
            
            
            
            
            
            
            
            
    #     screen,
    #     current_width,
    #     current_height,
    #     player_name,
    #     name_entered,
    #     selected_profile,
    #     player_image,
    #     selected_image,
    #     profile_images,
    #     profile_rects,
    #     operator,
    #     operator_rects,
    #     ceill,
    #     ceill_text,
    #     ceill_entered,
    #     time_limit,
    #     time_text,
    #     time_entered,
    #     time_button_rects,
    #     ceill_button_rects,
    #     answer_rects,
    #     answer_selected,
    #     game_state,
    #     select_buttons,
    #     settings_rects,
    #     back_button_rect,
    #     # selected_color,
    #     # hue_bar,
    #     # dragging_hue,
    #     home_button_rect,
    #     # music_on,
    #     # effect_on
    #     small_window,
    #     clicked_button,
    #     language_rects,
    #     load_language,
    #     selected_profile_image,
        
        
        
        
    #     dragging,is_guest,
    #     # mouse_start_x,
    #     # mouse_start_y,
    #     # camera_x,
    #     # camera_y,
    #     # level_rects,
    #     # level_rects_for_theme,
    #     # level_images_theme,
        
        
        
    #     rect_for_music,
    #     music_state,
        
    #     sound_state,
    #     rect_for_sound,
    #     home_button_rect,askus_button_rect,share_button_rect,
        
        
        
        
        
        
        
        
        
        
    #     option_rects,
        
        
        
        
        
        
    
    #     start_time,
    #     current_question,
    #     correct_count,
    #     wrong_count,
    #     question_number  
        
        
    #     ,
    #     # selected_background,
    
    #     dragging_GAME_MODE,
    #     drag_start_x_GAME_MODE,
    #     target_offset_GAME_MODE,
    #     game_mode_slide,
    #     image_game_mode_page2,
    #     image_game_mode_page3,
    #     image_game_mode_page1,image_game_mode_page4,
        
        
        
    #     support_face,
    #     SUPPORT_MENU,
    #     SUPPORT_window,
        
    #     EXIT_OK,
    #     CUSTOM_MATH,
    #     ONLINE_FLAG,
    #     DAILY_GAME,menu_state,
    #     DAILY_BUTTON,
    #     reset_side_effect_language,
    #     setting_menu,
        
        
        
        
        
        
        
        
        
        
        
        
    #     control_every_button_in_setting_on_or_off,DASHBOARD,online_state  # old_screen
    #     )
        
        
        
    (
        running,
        screen,
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
        small_window,
        clicked_button,
        language_rects,
        selected_profile_image,
        dragging,
        rect_for_music,
        music_state,
        sound_state,
        rect_for_sound,
        home_button_rect,
        askus_button_rect,
        share_button_rect,
        option_rects,
        start_time,
        current_question,
        correct_count,
        wrong_count,
        question_number,
        dragging_GAME_MODE,
        drag_start_x_GAME_MODE,
        target_offset_GAME_MODE,
        support_face,
        SUPPORT_MENU,
        SUPPORT_window,
        EXIT_OK,
        CUSTOM_MATH,
        ONLINE_FLAG,
        DAILY_GAME,
        menu_state,
        DAILY_BUTTON,
        setting_menu,
        control_every_button_in_setting_on_or_off,
        DASHBOARD,
        online_state,
        is_guest,
        restart_OFF_ON_game
    ) = handle_events(

        screen,
        current_width,
        current_height,
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

        # این مورد قبلاً جا افتاده بود

        small_window,
        clicked_button,
        language_rects,
        load_language,
        selected_profile_image,
        dragging,

        rect_for_music,
        music_state,
        sound_state,
        rect_for_sound,
        home_button_rect,
        askus_button_rect,
        share_button_rect,
        option_rects,

        # این مورد در تعریف handle_events وجود دارد
        generate_missing_number_question,

        start_time,
        current_question,
        correct_count,
        wrong_count,
        question_number,

        dragging_GAME_MODE,
        drag_start_x_GAME_MODE,
        target_offset_GAME_MODE,
        game_mode_slide,
        image_game_mode_page2,
        image_game_mode_page3,
        image_game_mode_page1,
        image_game_mode_page4,

        support_face,
        SUPPORT_MENU,
        SUPPORT_window,

        EXIT_OK,
        CUSTOM_MATH,
        ONLINE_FLAG,
        DAILY_GAME,
        menu_state,
        DAILY_BUTTON,
        reset_side_effect_language,
        setting_menu,
        control_every_button_in_setting_on_or_off,
        DASHBOARD,
        online_state,
        is_guest,
        restart_OFF_ON_game
    )
    
    
    
    
    
    

    
    
    #--------- for GAME MODE slid bar
        # آپدیت حرکت اسلاید
    game_mode_slide.update()
    # گرفتن مقدار حرکت
    offset = game_mode_slide.get_offset()

    
    
    
    
    
    
    #--------------------------------------------------------------------------------- first page that every one goes in 
    if game_state == "NAME":    
          
        # for background  flying and image 
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
    
    
    
    
    
    
        # این برای ران کردن دیفالت زبان انگلیسی  در اول بازی است 
        if defult_language == True:
            load_language("en")
            defult_language=False
            
            
            
        # این برای  صفحه اول بازی هستن 
        if selected_profile is None:
            draw_profile_circle(
                screen,
                default_profile,
                (current_width//2, 200),
                250
            )
        else:
            draw_profile_circle(
                screen,
                selected_image,
                (current_width//2, 200),
                250
            )    
            
            
            
        #--------------- name screen
        draw_name_screen(
            screen,
            fonts,
            PLAYER.player_name,
            PLAYER.input_box,
            enter_button
        )

        draw_email_screen(
            screen,
            fonts,
            PLAYER.player_email
        )
            

        draw_profiles(
            screen,
            profile_images,
            profile_rects,
            profile_area
        )
        
        # draw_profile_circle(
        #     screen,
        #     selected_image,
        #     (
        #         current_width // 2 - 300,
        #         500
        #     ),
        # )
        
        




            
        #-------------------------------------- for flag 
        CON.draw_country_button(
            screen,
            CON.country_button,
            CON.selected_country
        )


        if CON.country_window:

            CON.draw_country_window(
                screen,
                country,
                CON.country_rects
            )
           
           
        CON.draw_selected_flag(
            screen,
            country,
            CON.selected_country
        ) 




    #------------------------------------------------------------------------------------------MENU
    if game_state == "MENU" or menu_state == "MENU":# DASH BOARDاین همون داشبود است 
        

        # for background  flying and image 
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
    

            
        # # این همون منوی عمودی است برای دکمه های منو 
        # image_setter(screen,liner,-110,current_height//2 - 695)  
        xxx=70
        yyy=649
        if DES.menu_slide_back:

            finished =DES.menu_back_setters(
                screen,
                menu_bacccccck,
                x=220,
                y=current_height  //2 - 770,
                gap=2,
                first_x=220,
                first_y=current_height  //2 - 720
            )

            if finished:

                DES.menu_slide_back = False
                DES.menu_slide_active = False
                DES.menu_slide_x = None

                game_state = "MENU"


        # ========================================================
        # ENTER SLIDE
        # ========================================================

        elif DES.menu_slide_active:

            finished = DES.menu_back_setters(
                screen,
                menu_bacccccck,
                x=220,
                y=current_height  //2 - 770,
                gap=2,
                first_x=220,
                first_y=current_height  //2 - 720
            )

            if finished:
                DES.menu_slide_active = False


        # ========================================================
        # IMAGE STAYS
        # ========================================================

        else:


            DES.menu_back_setters(
                screen,
                menu_bacccccck,
                x=220,
                y=current_height // 2 - 770,
                gap=2,
                first_x=220,
                first_y=current_height // 2 - 720
            )



        #for menu
        select_buttons.clear()
        draw_menu_buttons(
            screen,
            current_width,
            current_height,
            fonts,
            select_buttons
        )     
            
        donate_base(
            screen,
            call_button_rect
        )
        #-------------------------Button
        # support_button(
        #     screen,
        #     support_button_rect
        # )
        
        donate_button(
            screen,
            call_button_rect
        )

    # draw_dashboard_date(
    #     screen,
    #     day_image,
    #     weekday_images,
    #     month_images,
    #     font_day,
    #     font_time
    # )
#این ها باید درست بشن چون السشو همش اجرا میشن در همه حالت ها 
    # برای ساپورت است
        STS.draw_current_player(
            screen,
            profile_images,
            STS.current_player_type,
            (50, 50)
        )
                
                
        # menu_back_setters(
        #     screen,
        #     menu_bacccccck,
        #     x=220,
        #     y=current_height  //2 - 770,
        #     gap=2,
        #     first_x=220,
        #     first_y=current_height  //2 - 720
        # )



        # MENU__.draw_punch_images_in(
        #     screen,
        #     menu_images,
        #     menu_centers,
        #     menu_sizes,
        #     page_id="game_menu"
        # )




    #این برای داشتبورد است 
    if game_state == "MENU" or game_state == "SETTING" and DASHBOARD: 
        #-------------------

        DA.draw_dashboard_date(
            screen,
            DA.day_image,
            DA.month_images,
            fonts["DAY"],
            fonts["weekdays"],
            fonts["month"],
            fonts["date"]
        )

        draw_punch_image(
            screen,
            face__up,
            (current_width//2 -200 + 250, current_height // 2  + 470),
            (1250, 400),
            "FACE"
        )

        
        draw_punch_image(
            screen,
            face__up,
            (current_width//2 -200 + 250, current_height // 2 +150 ),
            (1250, 400),
            "FACE"
        )
        
        draw_punch_image(
            screen,
            days__,
            (current_width//2   + -70, current_height // 2 - 378 ),
            (300, 500),
            "days"
        )
        draw_punch_image(
            screen,
            level__,
            (current_width//2 -370, current_height // 2 - 378 ),
            (300, 500),
            "level"
        )
        draw_punch_image(
            screen,
            rank__,
            (current_width//2 +305, current_height // 2 - 378 ),
            (600, 600),
            "rank"
        )
        

        
        popular_game.image_rects =popular_game.draw_three_images(
            screen,
            popular_game.selected_images
        )
                
                
        recent_game.image_rects =recent_game.draw_three_images_recent_game(
            screen,
            recent_game.selected_images
        )
                
                
        
        
        
        
        
        
        # top_3 = popular_game.get_top_3_popular_games()
        # print(top_3)
        # popular_game.draw_popular_games(
        #     screen,top_3,
        #     "./asset/image/MODE/games"
        # )

        call_base(
            screen,
            support__button_rect
        )
        call_support(
            screen,
            support__button_rect
        )




        store_base(
            screen,
            store__button_rect
        )
        store_button(
            screen,
            store__button_rect
        )








    if menu_state == "SUPPORT":

        draw_4_images_SUPPORT(screen)

        if game_state == "Contact Us":
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
            open_window_with_side_effect(
                screen,
                SUPPORT_window1,
                1200,
                600
            )
            draw_back_button(
              screen,
              back_button_rect)
        #     support_button(
        #       screen,
        #       support_button_rect
        #    )        
        elif game_state == "Feed Back":
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
            open_window_with_side_effect(
                screen,
                SUPPORT_window2,
                1200,
                600
            )
            draw_back_button(
              screen,
              back_button_rect)
        #     support_button(
        #       screen,
        #       support_button_rect
        #    )        
        elif game_state == "Donate":
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
            open_window_with_side_effect(
                screen,
                SUPPORT_window3,
                1200,
                600
            )
            draw_back_button(
              screen,
              back_button_rect)
        #     support_button(
        #       screen,
        #       support_button_rect
        #    )        
        elif game_state == "Report Bug":
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
            open_window_with_side_effect(
                screen,
                SUPPORT_window4,
                1200,
                600
            )
            draw_back_button(
              screen,
              back_button_rect)
        #     support_button(
        #       screen,
        #       support_button_rect
        #    )        

    #######################-------زا این جا به بعد دریگه برای ستنیگ است -------------#######################
    
    if game_state == "START":
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
        
        # draw_punch_image(
        #     screen,
        #     start___,
        #     (current_width//2 - 375 + 300, current_height // 2  ),
        #     (650, 200),
        #     "CUSTOM_MATH_1"
        # )
        
        # ----------------------------------------------------------
        # PROFILE
        # ----------------------------------------------------------

        # draw_start_profile(
        #     screen,
        #     profile_images,
        #     selected_profile,
        #     PLAYER.player_name,
        #     current_width // 2,
        #     current_height // 2 - 220
        # )
        
        STS.start_profile_rect, STS.start_guest_rect = STS.draw_start_profile(
            screen,
            profile_images,
            selected_profile,
            PLAYER.player_name,
            current_width // 2,
            current_height // 2 - 220
        )
                
    if game_state == "MENU" and menu_state == "EXIT":
        draw_exit_confirmation(screen)
        
        
    if game_state == "MENU" and menu_state == "P_GAME_MODE":
        draw_punch_image(
            screen,
            punch_1,
            (current_width//2 - 375 + 300, current_height // 2  ),
            (650, 650),
            "GAMEMODE"
        )
        draw_punch_image(
            screen,
            punch_2,
            (current_width//2 - 375 + 1000, current_height // 2  ),
            (650, 650),
            "MATH"
        )

        
    if game_state == "MENU" and menu_state == "DAILY GAME":
        draw_punch_image(
            screen,
            IMG1,
            (current_width//2 - 375 + 300, current_height // 2  ),
            (700, 1050),
            "DAILY_GAME1"
        )
        draw_punch_image(
            screen,
            IMG2,
            (current_width//2 - 375 + 1000, current_height // 2  ),
            (700, 1050),
            "DAILY_GAME2"
        )

        
    if online_state == True:


        move_flage(
            flag_in_menu,
            screen,
            current_width // 2 - 550 ,
            True,
            300 
        )      
        
    if game_state == "MENU" and menu_state == "LEADERBOARD":
        draw_punch_image(
            screen,
            punch_1,
            (current_width//2 - 375 + 300, current_height // 2  ),
            (650, 650),
            "CUSTOM_MATH_1"
        )















    # if  game_state == "SETTING" and menu_state == "LANGUAGE":
    #     draw_moving_map(
    #         screen,
    #         WIDTH,
    #         HEIGHT,
    #         dt    )
    #     draw_flying_birds(
    #         screen,
    #         current_width,
    #         current_height
    #     )  
















        #------------------------------------------------------------------------------------------LANGUAGE
    # if game_state == "LANGUAGE":
        #------------------------for background flying  _ i cand do that
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
        
        
        # open_window_with_side_effect(
        #         screen,
        #         background_Lan,
        #         current_width // 2 - 720 ,current_height // 2 -475
        #     )
        # # image_setter(screen,background_Lan, )

        # language_rects = draw_languages(
        #     screen,
        #     current_width,
        #     current_height
        # )
        # menu_cache.clear()

                        # عکس دایره. برای پروفایل هر صفحه
        # image_setter(screen,pathth,xyz_for_profile_logo,current_height//2 - 666)
        # gif_setting(screen,gif_frames_lan,width_for_profile_logo,current_height // 2 - 570)
        

        # draw_back_button(
        #     screen,
        #     back_button_rect)
        # support_button(
        #     screen,
        #     support_button_rect
        # )      
        

    #---------------------------------------------------------------------------------GAME DAILY
    if game_state == "DAILY GAME":

        # ------------------------ Background

        draw_moving_map(
            screen,
            WIDTH,
            HEIGHT,
            dt
        )

        draw_flying_birds(
            screen,
            current_width,
            current_height
        )

        # ------------------------ Page 1

        if DAILY_BUTTON == "page_1":
            open_window_with_side_effect(
                screen,
                DAILY_window_page1,
                1200,
                600
            )

            punch_scale_animation_one_image(
                screen,
                next_page,
                "NEXT",
                current_width //2 - 500,
                current_height //2 - 500    
            )
            punch_scale_animation_one_image(
                screen,
                back_page,
                "BACK",
                current_width //2 - 300,
                current_height //2 - 300
            )
        # ------------------------ Page 2
        if DAILY_BUTTON == "page_2":#GAME
            open_window_with_side_effect(
                screen,
                DAILY_window_page2,
                1200,
                600
            )

            punch_scale_animation_one_image(
                screen,
                play_next_page,
                "PLAY",
                current_width //2 - 200,
                current_height //2 - 200    
            )
            punch_scale_animation_one_image(
                screen,
                back_page,
                "BACK",
                current_width //2 - 300,
                current_height //2 - 300
            )
        if DAILY_BUTTON == "GAME":#GAME
            draw_back_button(
                screen,
                back_button_rect)
    #---------------------------------------------------------------------------------STATUS
    if game_state == "STATUS":
        #------------------------for background 
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
        open_window_with_side_effect(
                screen,
                STATUS_window,
                1200,
                600
            )
        
        
        
        
        

        draw_back_button(
            screen,
            back_button_rect)
    #---------------------------------------------------------------------------------sound
    if game_state == "SOUND":

        #------------------------for background 
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
        

        sound_screen(screen)
        draw_back_button(
            screen,
            back_button_rect
        )
        
    #     support_button(
    #     screen,
    #     support_button_rect
    # )

        donate_base(
            screen,
            call_button_rect
        )
        donate_button
        (
            screen,
            call_button_rect
        )

                # عکس دایره. برای پروفایل هر صفحه
        # image_setter(screen,pathth,xyz_for_profile_logo,current_height//2 - 666)
        # gif_setting(screen,gif_frames_sound,width_for_profile_logo,current_height // 2 - 570)



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
 


          
    if game_state == "CEILL":        
        
        #------------------------for background 
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
        
        
        # support_button(
        #     screen,
        #     support_button_rect
        # )
        
        donate_base(
            screen,
            call_button_rect
        )        
    
        # image_setter(screen,pathth,xyz_for_profile_logo,current_height//2 - 666)
        # gif_setting(screen,gif_frames_credit,width_for_profile_logo,current_height // 2 - 570)
        draw_profile_live_circle(
            screen,
            selected_profile_image,
            p99,
            current_width
        )
        donate_button(
            screen,
            call_button_rect
        )

        
        
        

        
        
        
        
        
        
        
    #--------------------------------------------------------------------------------------------------SUPPORT


    # if game_state == "SUPPORT":
    #     # draw_4_images_SUPPORT(screen)        

    #     #----------------- background_and_brids
    #     draw_moving_map(
    #         screen,
    #         WIDTH,
    #         HEIGHT,
    #         dt    )
    #     draw_flying_birds(
    #         screen,
    #         current_width,
    #         current_height
    #     )   
    
        
    #     # draw_4_images_SUPPORT(screen)        

    #                     # عکس دایره. برای پروفایل هر صفحه
    #     image_setter(screen,pathth,xyz_for_profile_logo,current_height//2 - 666)
    #     gif_setting(screen,gif_frames_support,width_for_profile_logo,current_height // 2 - 570)



        
        
        
    #--------------------------------------------------------------------------------------------------MORE


    if game_state == "MORE":
        #------------------------for background flying  _ i cand do that
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
        

        
        draw_4_images_MORE(screen)        


        draw_back_button(
            screen,
            back_button_rect)
        
        # support_button(
        #     screen,
        #     support_button_rect
        # )
        

        
        # عکس دایره. برای پروفایل هر صفحه
        # image_setter(screen,pathth,xyz_for_profile_logo,current_height//2 - 666)
        # gif_setting(screen,gif_frames_about,width_for_profile_logo,current_height // 2 - 570)

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
             

             
        
        
        


# #------------------------------------------------------------------------------------------ MUSIC



#     if game_state == "MUSIC":
#         #----------------- background_and_brids
#         draw_moving_map(
#             screen,
#             WIDTH,
#             HEIGHT,
#             dt    )
#         draw_flying_birds(
#             screen,
#             current_width,
#             current_height
#         )   
        
#         draw_music(
#             screen,
#             current_width,
#             current_height,
#             background_music,
#             profile_image
#         )
#         # draw_music(
#         #     screen,
#         #     current_width,
#         #     current_height,
#         #     background_music,
#         #     profile_image
#         # )
        

        
#         draw_back_button(
#             screen,
#             back_button_rect
#         )
#         support_button(
#             screen,
#             support_button_rect
#         )
#         # bug_button(
#         #     screen,
#         #     bug_button_rect
#         # )     
#         donate(
#             screen,
#             call_button_rect
#         )
#         image_setter(screen,pathth,xyz_for_profile_logo,current_height//2 - 666)
#         gif_setting(screen,gif_frames_music,width_for_profile_logo,current_height//2 - 570)




#-------------------------------------------------------------------------------------- GAME MODE 

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

        # if offset == 0:
        #     current_page_GAME_MODE = 0

        # elif offset == -screen.get_width():
        #     current_page_GAME_MODE = 1

        # elif offset == -screen.get_width() * 2:
        #     current_page_GAME_MODE = 2
        # elif offset == -screen.get_width() * 3:
        #     current_page_GAME_MODE = 3
        # elif offset == -screen.get_width() * 4:
        #     current_page_GAME_MODE = 4
        # elif offset == -screen.get_width() * 5:
        #     current_page_GAME_MODE = 5



        update_center_images_punch()
        image_game_mode_page1, _ = draw_game_mode_page(
            screen,
            MO.images_MODE_page1,
            MO.image_sizes_page,
            500,
            500,
            offset,
            center_images=MO.center_images_MODE,
            overlay_images=[
                None,
                None,
                None,
                None,
                None,
                None
            ]
        )
        draw_game_mode_text(
            screen,
            image_game_mode_page1,
            [
                "Color Focus",
                "Follow Pattern",
                "-",
                "-",
                "Mirror Match",
                "Quick Reaction"
            ],
            fonts["date"]
        )
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                
        image_game_mode_page2, _ = draw_game_mode_page(
            screen,
            MO.images_MODE_page2,
            MO.image_sizes_page,
            500,
            500,
            offset + screen.get_width(),
            center_images=MO.center_images_MODE,
            overlay_images=[
                None,
                None,
                None,
                None,
                None,
                None
            ]
        )
                
        draw_game_mode_text(
            screen,
            image_game_mode_page2,
            [
                "Memory Match",
                "Find Number",
                "Math Compare",
                "60 Second",
                "Find Operator",
                "True False"
            ],
            fonts["date"]
        )
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        image_game_mode_page3, _ = draw_game_mode_page(
            screen,
            MO.images_MODE_page3,
            MO.image_sizes_page,
            500,
            500,
            offset + screen.get_width() * 2,
            center_images=MO.center_images_MODE,
            overlay_images=[
                None,
                None,
                None,
                None,
                None,
                None
            ]
        )
        draw_game_mode_text(
            screen,
            image_game_mode_page3,
            [
                "Math Rush",
                "Count Rush",
                "Memory Select",
                "-",
                "-",
                "--"
            ],
            fonts["date"]
        )
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        image_game_mode_page4, _ = draw_game_mode_page(
            screen,
            MO.images_MODE_page4,
            MO.image_sizes_page,
            500,
            500,
            offset + screen.get_width() * 3,
            center_images=MO.center_images_MODE,
            overlay_images=[
                None,
                None,
                None,
                None,
                MO.my_icon,
                MO.my_icon
            ]
        )
        
        draw_game_mode_text(
            screen,
            image_game_mode_page4,
            [
                "MEMORY GRID",
                "PATTERN MEMORY",
                "FIND NUMBER",
                "ARROW FLOW",
                "COLOR SHAPE",
                "SEQUENCE"
            ],
            fonts["date"]
        )
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        image_game_mode_page5, _ = draw_game_mode_page(
            screen,
            MO.images_MODE_page1,
            MO.image_sizes_page,
            500,
            500,
            offset + screen.get_width() * 4,
            center_images=MO.center_images_MODE,
            overlay_images=[
                MO.my_icon,
                MO.my_icon,
                MO.my_icon,
                MO.my_icon,
                MO.my_icon,
                MO.my_icon
            ]
        )
        draw_game_mode_text(
            screen,
            image_game_mode_page5,
            [
                "_",
                "_",
                "_",
                "_",
                "_",
                "_"
            ],
            fonts["date"]
        )
        
        # finished_type = TYPER.draw_typing_text(
        #     screen,
        #     "MATH",
        #     fonts["heart"],
        #     (255, 255, 255),
        #     (current_width // 2, current_height // 2 - 500),
        #     TYPER.typing_start_time,
        #     80
        # )  
        
        # if TYPER.typing_start_time is not None:
        if MO.page1_active:
            # print("page1")
            finished_type = TYPER.draw_typing_text(
            screen,
            "MATH",
            fonts["heart"],
            (255, 255, 255),
            (current_width // 2, current_height // 2 - 500),
            TYPER.typing_start_time,
            80
        )
        if MO.page2_active:
            # print("page2")
            finished_type = TYPER.draw_typing_text(
            screen,
            "MEMORY",
            fonts["heart"],
            (255, 255, 255),
            (current_width // 2, current_height // 2 - 500),
            TYPER.typing_start_time,
            80
        )
        if MO.page3_active:
            # print("page3")
            finished_type = TYPER.draw_typing_text(
            screen,
            "ATTENTION",
            fonts["heart"],
            (255, 255, 255),
            (current_width // 2, current_height // 2 - 500),
            TYPER.typing_start_time,
            80
        )
        if MO.page4_active:
            # print("page4")
            finished_type = TYPER.draw_typing_text(
            screen,
            "REACTION",
            fonts["heart"],
            (255, 255, 255),
            (current_width // 2, current_height // 2 - 500),
            TYPER.typing_start_time,
            80
        )
        if MO.page5_active:
            # print("page5")
            finished_type = TYPER.draw_typing_text(
            screen,
            "UP COOING",
            fonts["heart"],
            (255, 255, 255),
            (current_width // 2, current_height // 2 - 500),
            TYPER.typing_start_time,
            80
        )
        # if MO.page6_active:
        #     # print("page6")
        #     finished_type = TYPER.draw_typing_text(
        #     screen,
        #     "Hello Aiden",
        #     fonts["heart"],
        #     (255, 255, 255),
        #     (500, 400),
        #     TYPER.typing_start_time,
        #     80
        # )


        # # -------------------------------- رسم صفحه‌ها
        # rects, current_sizes = draw_image_MODE_page_1(
        #     screen,
        #     500,
        #     500,
        #     offset
        # )
        # #  # این هم برایعسک های وسط ۶ تا عکس در گیم مود با افکت پانج 
        # draw_center_images_MODE(
        #     screen,
        #     rects,
        #     image_sizes_page1
        # )



        # draw_image_MODE_page_2(
        #     screen,
        #     500,
        #     500,
        #     offset + screen.get_width()
        # )
        
        # draw_image_MODE_page_3(
        #     screen,
        #     500,
        #     500,
        #     offset + screen.get_width() * 2,
        #     icons
            
        # )
        
        # draw_image_MODE_page_4(
        #     screen,
        #     500,
        #     500,
        #     offset + screen.get_width() * 3,
        #     icons_4
            
        # )
        
        # draw_image_MODE_page_5(
        #     screen,
        #     500,
        #     500,
        #     offset + screen.get_width() * 4,
        #     icons_5
            
        # )
        
        
        
        draw_page_indicator(
            screen,
            MO.current_page_GAME_MODE,
            6,
            screen.get_height() - 80
        )

        _window(screen,small_window)

        donate_base(
            screen,
            call_button_rect
        )
        draw_back_button(
        screen,
        back_button_rect
        )
        # support_button(
        #     screen,
        #     support_button_rect
        # )
        # bug_button(
        #     screen,
        #     bug_button_rect
        # )     
        donate_button(
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
        # image_setter(screen,pathth,xyz_for_profile_logo,current_height//2 - 666)
        # gif_setting(screen,gif_frames_mode,width_for_profile_logo,current_height // 2 - 570)





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


        # support_button(
        #     screen,
        #     support_button_rect
        # )
        donate_base(
            screen,
            call_button_rect
        )
        # bug_button(
        #     screen,
        #     bug_button_rect
        # )
        donate_button(
            screen,
            call_button_rect
        )

        #-------------------------gif for time
        # image_setter(screen,pathth,xyz_for_profile_logo,current_height//2 - 666)
        # gif_setting(screen,gif_frames,width_for_profile_logo,current_height // 2 - 570)
        
        draw_profile_live_circle(
            screen,
            selected_profile_image,
            p99,
            current_width
        )
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    #---------------------------------------------------------------------------------------ONLINE
    # if game_state == "PLAY ONLINE":
    #     print("online on the way...")
        
        
        
    
    #---------------------------------------------------------------------------------------SETTING

    if game_state == "SETTING":
        
        #------------------------for background flying  _ i cand do that
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
        
            
  

        #     # ========================================================
        #     # BACK SLIDE
        #     # ========================================================

        # if DES.menu_slide_back:

        #     finished = DES.image_setter_menu_back(
        #         screen,
        #         liner,
        #         -103,
        #         current_height // 2 - 670,
        #         50
        #     )

        #     if finished:

        #         DES.menu_slide_back = False
        #         DES.menu_slide_active = False
        #         DES.menu_slide_x = None

        #         game_state = "MENU"


        # # ========================================================
        # # ENTER SLIDE
        # # ========================================================

        # elif DES.menu_slide_active:

        #     finished = DES.image_setter_menu(
        #         screen,
        #         liner,
        #         -103,
        #         current_height // 2 - 670,
        #         50
        #     )

        #     if finished:
        #         DES.menu_slide_active = False


        # # ========================================================
        # # IMAGE STAYS
        # # ========================================================

        # else:

        #     screen.blit(
        #         liner,
        #         (-103, current_height // 2 - 670)
        #     )
      #------------------------
        draw_setting_buttons(
            screen,
            current_width,
            current_height,
            fonts,
            settings_rects
        )

        donate_base(
            screen,
            call_button_rect
        )
        draw_back_button(
            screen,
            back_button_rect
        )
        # support_button(
        #     screen,
        #     support_button_rect
        # )

        donate_button(
            screen,
            call_button_rect
        )


        #----------------------------------این برای داشتبورد است 
        
        if DASHBOARD :
            
            #     #-------------------

            DA.draw_dashboard_date(
                screen,
                DA.day_image,
                DA.month_images,
                fonts["DAY"],
                fonts["weekdays"],
                fonts["month"],
                fonts["date"]
            )























    if game_state == "LEADER BOARD":

       # gallery_button(
        #     screen,
        #     gallery_button_rect
        # )
        _window(screen,small_window)



        donate_base(
            screen,
            call_button_rect
        )
        draw_back_button(
            screen,
            back_button_rect
        )
        # support_button(
        #     screen,
        #     support_button_rect
        # )
        # bug_button(
        #     screen,
        #     bug_button_rect
        # )     
        donate_button(
            screen,
            call_button_rect
        )

               # عکس دایره. برای پروفایل هر صفحه
        # image_setter(screen,pathth,xyz_for_profile_logo,current_height//2 - 666)
        # gif_setting(screen,gif_frames_score,width_for_profile_logo,current_height // 2 - 570)
        
        
        draw_profile_live_circle(
            screen,
            selected_profile_image,
            p99,
            current_width
        )











    if game_state == "OPERATION":
        #------------------------for background 
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
        # draw_new_screen(screen)
        draw_operation_screen(
            screen,
            fonts,
            operator_images,
            operator_rects,
            current_width,
            current_height)
       # gallery_button(
        #     screen,
        #     gallery_button_rect
        # )
        _window(screen,small_window)
                
                
                
                
                
        draw_back_button(
            screen,
            back_button_rect
        )
        # image_setter(screen,pathth,xyz_for_profile_logo,current_height//2 - 666)

        # gif_setting(screen,gif_frames_op,width_for_profile_logo,current_height // 2 - 570)
        donate_base(
            screen,
            call_button_rect
        )       
        # support_button(
        #     screen,
        #     support_button_rect
        # )
        # bug_button(
        #     screen,
        #     bug_button_rect
        # ) 
        donate_button(
            screen,
            call_button_rect
        )   

        draw_profile_live_circle(
            screen,
            selected_profile_image,
            p99,
            current_width
        )

        

        

    # GAMES MODE
   #----------------------------------------------------------------------------------------------------------------
   #----------------------------------------------------------------------------------------------------------------
   #----------------------------------------------------------------------------------------------------------------
   #----------------------------------------------------------------------------------------------------------------
   #----------------------------------------------------------------------------------------------------------------
   #----------------------------------------------------------------------------------------------------------------
    # page 1
   #----------------------------------------------------------------------------------------------------------------
   #----------------------------------------------------------------------------------------------------------------
   #----------------------------------------------------------------------------------------------------------------
    if game_state == "MEMORY":
        if restart_OFF_ON_game == True:
            print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
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
        if restart_OFF_ON_game == True:
            print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
        back_setter(screen,SHAPE_COLOR_NAME_BACKGROUND)
        SHAPE_COLOR_NAME(screen,current_width)
        
        draw_back_button(
            screen,
            back_button_rect
        )
    #--------------------------------------------------------------------------------
    if game_state == "REPEAT_AFTER_ME":
        if restart_OFF_ON_game == True:
            print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
        back_setter(screen,REPEAT_AFTER_ME_BACKGROUND)
        REPEAT_AFTER_ME_(screen)
        
        
        draw_back_button(
            screen,
            back_button_rect
        )
    #--------------------------------------------------------------------------------
    if game_state == "DIRECTION":
        if restart_OFF_ON_game == True:
            print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
        back_setter(screen,DIRECTION_BACKGROUND)

        DIRECTION_(screen)
        
        
        draw_back_button(
            screen,
            back_button_rect
        )
    # #--------------------------------------------------------------------------------
    if  game_state == "MIRROR":
        if restart_OFF_ON_game == True:
            print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
        back_setter(screen,MIRROR_BACKGROUND)

        MIRROR_(screen)

        draw_back_button(
            screen,
            back_button_rect
        )
    #--------------------------------------------------------------------------------
    if game_state =="ACTION":
        if restart_OFF_ON_game == True:
            print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
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
    if game_state == "BEFORE_GAMES":
        #------------------------for background 
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
        punch_scale_animation_one_image(
            screen,
            games_first_window,
            "NEXT",
            current_width //2 - 400,
            current_height //2 - 400    
        )
        punch_scale_animation_one_image(
            screen,
            next_page,
            "NEXT",
            current_width //2 - 500,
            current_height //2 - 500    
        )
        punch_scale_animation_one_image(
            screen,
            back_page,
            "BACK",
            current_width //2 - 300,
            current_height //2 - 300
        )
        # if now_game_start:
        #     # if previous_game_state != "FIND_NUMBER":

                # ---------------- Question Background ----------------


    if game_state == "FIND_NUMBER":
        if restart_OFF_ON_game == True:
            print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")

        if not now_game_start:
            countdown(
                screen,
                FIND_NUMBER_BACKGROUND
            )

            now_game_start = True
        else:




            # ============================================================
            # FIND NUMBER
            # ============================================================
            back_setter(
                screen,
                FIND_NUMBER_BACKGROUND
            )



            # ---------------- Question Background ----------------

            image_setter(
                screen,
                image_back_quastion,
                current_width // 2 - 600,
                current_height // 2 - 550
            )


            # ============================================================
            # MAKE SURE QUESTION EXISTS
            # ============================================================

            if current_question is None:

                current_question = generate_missing_number_question(
                    question_number
                )

                start_time = pygame.time.get_ticks()

                progress = 1.0


            #-------------------red green blue معجون
            B_excir_(screen)
            G_excir_(screen)
            R_excir_(screen)

            # ============================================================
            # HINT
            # ============================================================
            hint_1(screen)
            hint(screen)


            # ============================================================
            # SAVE
            # ============================================================

            # save(screen)


            # ============================================================
            # TIMER CALCULATION
            # ============================================================

            elapsed = (
                pygame.time.get_ticks() - start_time
            ) / 1000


            progress = 1 - (
                elapsed / current_question["time"]
            )


            progress = max(
                0,
                min(1, progress)
            )


            # ============================================================
            # QUESTION
            # ============================================================
            FNUM.update_game()
            draw_question_find_number(
                screen,
                fonts,
                FNUM.current_question,
                current_width,
                current_height
            )


            # ============================================================
            # TIMER CIRCLE
            # ============================================================

            draw_timer_circle(
                screen,
                (160, 160),
                80,
                progress
            )


            # ============================================================
            # TIMEOUT
            # ============================================================

            if elapsed >= current_question["time"]:

                # سؤال بدون جواب → اشتباه
                wrong_count += 1


                # سؤال بعدی
                question_number += 1


                current_question = generate_missing_number_question(
                    question_number
                )


                # ریست تایمر
                start_time = pygame.time.get_ticks()


                # ریست دایره تایمر
                progress = 1.0


            # ============================================================
            # SCORE
            # ============================================================

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


            # ============================================================
            # PLAYER
            # ============================================================

            draw_profile_live_circle(
                screen,
                selected_profile_image,
                p99,
                current_width
            )


            # ============================================================
            # UI
            # ============================================================

            # in_game_alarm(
            #     screen
            # )

            move_flage(
                flag_in_game,
                screen,
                current_width // 2 - 154,
                True,
                800
            )


            # menuu(
            #     screen
            # )


            restart(
                screen
            )


            exit__(
                screen
            )


            draw_back_button(
                screen,
                back_button_rect
            )
            save_1(screen)
            marshmallow_image(save_,screen,1900,current_height//2 - 290,15000)
            marshmallow_image(menuu1,screen,1860,current_height//2 + 470,7000)
            marshmallow_image(G,screen,current_width//2 - 956,current_height//2 - 120,20000)
            marshmallow_image(R,screen,current_width//2 - 956,current_height//2 + 35,10000)
            marshmallow_image(B,screen,current_width//2 - 950,current_height//2 - 290,15000)
            
            score_base(screen)
            scoreee11(screen)
    previous_game_state =game_state
    # ============================================================
    # 60 SECONDS GAME
    # ============================================================

    if game_state == "60S":
        if restart_OFF_ON_game == True:
            print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
        back_setter(
            screen,
            _60S_BACKGROUND
        )


        SIX_60S(
            screen,
            current_width
        )


        # ---------------- Player ----------------

        draw_profile_live_circle(
            screen,
            selected_profile_image,
            p99,
            current_width
        )


        # ---------------- Home ----------------

        in_game_button(
            screen,
            home_button_rect,
            menu
        )


        # ---------------- Back ----------------

        draw_back_button(
            screen,
            back_button_rect
        )


    #---------------------------------------------------------------------------------x(+-/*)y
    if game_state == "MORE_LESS_EQUAL":
        if restart_OFF_ON_game == True:
            print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
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
        if restart_OFF_ON_game == True:
            print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
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
        if restart_OFF_ON_game == True:
            print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
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
        if restart_OFF_ON_game == True:
            print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
        # back_setter(screen,DETECT_BACKGROUND)
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
    
        # print("this is detect")
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
        if restart_OFF_ON_game == True:
            print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
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

    # بک گراند این ها رو درست کنم ندارن 
    if game_state =="HOW_MANY":
        if restart_OFF_ON_game == True:
            print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
        back_setter(screen,DETECT_BACKGROUND)
        HOW.HOW_MANY_(screen,current_width,current_height)
        draw_back_button(
            screen,
            back_button_rect
        )


    if game_state =="HARD":
        if restart_OFF_ON_game == True:
            print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
        back_setter(screen,DETECT_BACKGROUND)

        HARD.HARD_(screen,current_width,current_height)
        draw_back_button(
            screen,
            back_button_rect
        )
    if game_state =="DETECT_PRO":
        if restart_OFF_ON_game == True:
            print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
        back_setter(screen,DETECT_BACKGROUND)
        
        DPRO.DETECT_PRO_(screen,current_width,current_height)
        draw_back_button(
            screen,
            back_button_rect
        )
    if game_state =="MEMORY_GO":
        if restart_OFF_ON_game == True:
            print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
        back_setter(screen,DETECT_BACKGROUND)

        MEMGO.MEMORY_GO_(screen,current_width,current_height)
        draw_back_button(
            screen,
            back_button_rect
        )

    if game_state =="MOVE_ARROW":
        if restart_OFF_ON_game == True:
            print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
        back_setter(screen,DETECT_BACKGROUND)
        M_ARR.MOVE_ARROW_(screen,current_width,current_height)
        draw_back_button(
            screen,
            back_button_rect
        )


    # page 4
   #----------------------------------------------------------------------------------------------------------------
   #----------------------------------------------------------------------------------------------------------------
   #----------------------------------------------------------------------------------------------------------------
    if game_state =="MATH_GO":
        if restart_OFF_ON_game == True:
            print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
        back_setter(screen,DETECT_BACKGROUND)

        MATHGO.MATH_GO_(screen)
        draw_back_button(
            screen,
            back_button_rect
        )

    if game_state =="FAST_ADD_SUB":
        if restart_OFF_ON_game == True:
            print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
        back_setter(screen,DETECT_BACKGROUND)

        FAS.QUICK_MATH(screen)
        draw_back_button(
            screen,
            back_button_rect
        )
    if game_state =="FOLLOW_THAT":
        if restart_OFF_ON_game == True:
            print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
        back_setter(screen,DETECT_BACKGROUND)

        FOTHAT.FOLLOW_THAT_(screen)
        draw_back_button(
            screen,
            back_button_rect
        )
    if game_state =="IMAGE_SELECT":
        if restart_OFF_ON_game == True:
            print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
        back_setter(screen,DETECT_BACKGROUND)

        IMSE.IMAGE_SELECT_(screen)

        draw_back_button(
            screen,
            back_button_rect
        )
    #-------------------------------------------------------------------------------------- DAILY


        
        
    #--------------------------------------------------------------------------------------------------PROFILE
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
        
        # support_button(
        #     screen,
        #     support_button_rect
        # )
        donate_base(
            screen,
            call_button_rect
        )
        # bug_button(
        #     screen,
        #     bug_button_rect
        # )   
        donate_button(
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
        # image_setter(screen,pathth,xyz_for_profile_logo,current_height//2 - 666)
        # gif_setting(screen,gif_frames_profile,width_for_profile_logo,current_height // 2 - 570)







#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
    
    if  game_state == "SETTING" and setting_menu == "MUSIC" and control_every_button_in_setting_on_or_off == "music":
        # reset_side_effect_language()
        draw_music(
            screen,
            current_width,
            current_height,
            background_music,
            music_profile_image
        )
        reset_window_side_effect()

    if  game_state == "SETTING" and setting_menu == "LANGUAGE" and control_every_button_in_setting_on_or_off == "language":
        # MUS.reset_music_side_effect()

        open_window_with_side_effect(
                screen,
                background_Lan,
                current_width // 2 - 720 ,current_height // 2 -475
            )
        # image_setter(screen,background_Lan, )

        language_rects = draw_languages(
            screen,
            current_width,
            current_height
        )
        menu_cache.clear()
    
    
    
    if  game_state == "SETTING" and setting_menu == "MORE" and control_every_button_in_setting_on_or_off == "more":
        draw_4_images_MORE(screen)

        # reset_side_effect_language()
        # MUS.reset_music_side_effect()
        reset_window_side_effect()


    if  game_state == "SETTING" and setting_menu == "ACCOUNT" and control_every_button_in_setting_on_or_off == "account":
        
        # MUS.reset_music_side_effect()
        reset_window_side_effect
        # reset_side_effect_language
    if  game_state == "SETTING" and setting_menu == "SOUND" and control_every_button_in_setting_on_or_off == "sound":
        sound_screen(screen)

        # reset_side_effect_language()
        # MUS.reset_music_side_effect()
        reset_window_side_effect()

    #--------------------------------------------------------------------------------------CUSTOM MATH
    if  game_state == "CUSTOM GAME":

        back_setter(screen,CUSTOM__GAME)





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
        answer_selected
                

    )
    
    
    
        
        # این برای منو است در وسط بازی 
    #------------------------------------ در وسط بازی 
    if MENU__.menu_in_middle_of_play == True:

        draw_punch_image(
            screen,
            menu_in_game,
            (current_width//2 , current_height // 2 ),
            (600, 900),
            "menu"
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








import pygame
import importlib
from modules.loading import *
from modules import mouse

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


mouse.set_game_cursor()


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
# from modules.window import _window
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
from modules.ceill_screen import *
from modules.profile_ import draw_profile_live_circle
from modules.mode  import *
from modules.support  import *
from modules  import support as SUP
from modules.more  import *
from modules import more  as  MORE

from modules.profile_ import  *
from modules.profile import  *
from modules.music import *
from modules.operation_screen import *
from modules import design as DES
from modules import account as ACC
from modules import before_game
from modules import game_list
from modules import report_bug

from modules import more_app as more_app
# from modules.date import date
from modules.save import save as SAVE
from modules.save import popular_game as popular_game

from modules.save import recent_game as recent_game
from modules import custom_math as CUS

from modules import FAQ 
from modules import INFO
from modules import more_app as HOW_TO_PLAY



from modules import mode as MODE
from daily import daily_game 



# ---------------------------------------------------------- متغیر های حیاتی 
# برای کنترل سرعت اجرای بازی
clock = pygame.time.Clock()
running = True
support_face = None
info = pygame.display.Info()

current_width, current_height = screen.get_size()








background_account = pygame.image.load(
    "./asset/image/music/music111.png"
).convert_alpha()
background_account = pygame.transform.smoothscale(
    background_account,
    (1550,1100)
)








_coming_soon_image = pygame.image.load(
    "asset/image/coming_soon.png"
).convert_alpha()


# این برای موزیک است عوض کردن موزیک

music_profile_image = pygame.image.load(
    "./asset/image/music/music.png"
).convert_alpha()



background_music = pygame.image.load(
    "./asset/image/music/music111.png"
).convert_alpha()

calender =pygame.image.load(
    "./asset/image/calender.png").convert_alpha()



background_music = pygame.transform.smoothscale(
    background_music,
    (1550,1100)
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

#------------------------------------------------------------- daily game
# play_today_3_games=[]# این هم لیست ۳ تا بازی امروز 
# play_today_3_games = daily_game.get_daily_games(
#     daily_game.GAME_ID,
#     current_date# این هم تاریخی است که من به این میدم برای اجرا
# )

# daily_game.get_daily_game_images(
#     play_today_3_games
# )

# # این  ها هم عکس ها هستن
# daily_game.today_image_game[0]
# daily_game.today_image_game[1]
# daily_game.today_image_game[2]



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

# askus_button_rect = pygame.Rect(
#     current_width - 160,  # فاصله از راست
#     440,                   # فاصله از بالا
#     90,
#     90
# )



#------------------------------------

# share_button_rect = pygame.Rect(
#     current_width - 160,  # فاصله از راست
#     580,                   # فاصله از بالا
#     90,
#     90
# )







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
# sound_bg = pygame.image.load(
#     "./asset/image/screen/sound.png"
# ).convert_alpha()
# # def image_background(rec):
    
    

# # Resize background to fullscreen size
# sound_bg = pygame.transform.smoothscale(
#     sound_bg,
#     (1000,
#     650)
# )


# # وسط صفحه
# x = (screen.get_width() - sound_bg.get_width()) // 2 
# y = (screen.get_height() - sound_bg.get_height()) // 2

#-------------------------------------------------------------LANGUAGE

profile_for_back = pygame.image.load("./asset/image/profile.png").convert_alpha()
#-------------------------------------------------------------
# Load background
# sound_bg = pygame.image.load(
#     "./asset/image/screen/sound.png"
# ).convert_alpha()
# # def image_background(rec):
    
    

# # Resize background to fullscreen size
# sound_bg = pygame.transform.smoothscale(
#     sound_bg,
#     (1000,
#     650)
# )


# # وسط صفحه
# x = (screen.get_width() - sound_bg.get_width()) // 2 
# y = (screen.get_height() - sound_bg.get_height()) // 2

#-------------------------------------------------------------
# menu_button = pygame.image.load(
#     "./asset/image/button1.png"
# ).convert_alpha()

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


offset_y = 90
offset_x = 20
xxxx=130
language_options = [
    ("en", current_width//2 - 450 + xxxx, current_height//2 - 300 + offset_y),
    ("hi", current_width//2 - 125 + xxxx, current_height//2 - 300 + offset_y),
    ("zh", current_width//2 + 200 + xxxx, current_height//2 - 300 + offset_y),
    ("fa", current_width//2 - 450 + xxxx, current_height//2 + 80 + offset_x),
    ("ru", current_width//2 - 125 + xxxx, current_height//2 + 80 + offset_x),
    ("ar", current_width//2 + 200 + xxxx, current_height//2 + 80 + offset_x),
]
language_rects = []



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

    for i, (language, x, y) in enumerate(language_options):

        rect = lan_images[i].get_rect(
            topleft=(x, y)
        )

        image, image_rect, lan_sizes[i] = hover_image_lan(
            lan_images[i],
            rect,
            mouse_pos,
            lan_sizes[i]
        )

        draw_random_side_effect(
            screen,
            image,
            image_rect.centerx,
            image_rect.centery,
            i,
            len(lan_images)
        )

        rects.append(
            (
                language,
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
    
    
    

# # #--------------------------------------- این برای خاموش روشن کردن دکمه اهنگ است 


# music_state = 1   # 0 خاموش - 1 روشن


# image_on = pygame.image.load("./asset/image/music/music_on.png").convert_alpha()
# image_off = pygame.image.load("./asset/image/music/music_off.png").convert_alpha()
# image_on=pygame.transform.smoothscale(image_on,(190,190))
# image_off=pygame.transform.smoothscale(image_off,(190,190))

# rect_for_music = image_off.get_rect(center=(current_width//2 + 350 ,current_height//2 - 58))

    
    
    
# # #--------------------------------------- برای افکت صوتی 

    
    

# sound_state = 1

# sound_on = pygame.image.load("./asset/image/music/sound_on.png").convert_alpha()
# sound_off = pygame.image.load("./asset/image/music/sound_off.png").convert_alpha()
# sound_on=pygame.transform.smoothscale(sound_on,(190,190))
# sound_off=pygame.transform.smoothscale(sound_off,(190,190))

# rect_for_sound = sound_off.get_rect(center=(current_width//2 + 350 ,current_height //2 + 260))

    
    
    
#---------in game---------- home button  __ ... button __...button
# menu=pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/in_game/menu.png").convert_alpha(),
#         (200,200)
#     )
# share=pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/in_game/share.png").convert_alpha(),
#         (200,200)
#     )
# askus=pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/in_game/ask-us.png").convert_alpha(),
#         (200,200)
#     )














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
sms_button_rect= pygame.Rect(
    1700,  # فاصله از راست
    current_height  - 570,                   # فاصله از بالا
    150,
    150
)



######################################### این برای FOUR_ICON_FOR_SCREEN

sms_button_rect1= pygame.Rect(
    1873,  # فاصله از راست
    current_height //2  - 616,                   # فاصله از بالا
    150,
    150
)


#donate
call_button_rect1= pygame.Rect(
    29,  # فاصله از راست
    current_height // 2  - 616,                   # فاصله از بالا
    150,
    150
)


#support
support__button_rect1= pygame.Rect(
    1930,  # فاصله از راست
    current_height // 2  + 315,                   # فاصله از بالا
    100,
    100
)

store__button_rect1= pygame.Rect(
    1873,  # فاصله از راست
    current_height  // 2 + 465,                   # فاصله از بالا
    150,
    150
)

#########################################




#----------------------------- دکمه برگشت

back_button_rect = pygame.Rect(
    current_width // 2 - 980,
    current_height // 2 + 470,
    150,
    150
)

back_button_rect_for_setting= pygame.Rect(
    20,
    current_height  - 177,
    150,
    150
)




    
############################################## مربوط به صفحه منو
small_window=""
select_buttons = []
select_button_clicked = False









############################################## این برای دکمه یها ساپورت است گرفتن رک برای اون ۴ تا 
CUS.current_width_current_height(current_width,current_height)
center_x = current_width // 2
center_y = current_height // 2

positions_____ = [
    # =========================
    # بالا
    # =========================
    (center_x - 180, center_y - 300),   # عکس 1 — بالا چپ
    (center_x + 460, center_y - 300),   # عکس 2 — بالا راست

    # =========================
    # پایین
    # =========================
    (center_x - 180, center_y + 220),   # عکس 3 — پایین چپ
    (center_x + 480, center_y + 220),   # عکس 4 — پایین راست
]



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




from online import online_checker as ONLINE_CHECKER
from clock import clock as CLOCK
#------------------------------------- این برای دیدن انلاین بودن سیستم است  اکر انلاین بود اپیدت زمان و گرفتن زمان     
IS_ONLINE=None
# IS_ONLINE = ONLINE_CHECKER.check_online()
# if IS_ONLINE == True:

#     print("Online")
#     ONLINE_CHECKER.run_online_time()
#     print(ONLINE_CHECKER.clock_is_online())
# else:
#     print("Offline")

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
    pages=10
)






















#-------------------------------- برای لود کردن پاپیولر گیم

popular_game.load_popular_games()



popular_game.load_popular_images(
    "./asset/image/MODE"
)


#-------------------------------- برای لود کردن پاپیولر گیم   RECENT GAMES
recent_game.load_recent_games()

recent_game.load_recent_images(
    "./asset/image/MODE"
)









#این ها باید حذف بشن 
#-------------------------------- SHAPE_COLOR_NAME ببرای ای  قسمت است 
from modules.MODE import SHAPE_COLOR_NAME
# new_question_SHAPE_COLOR_NAME()

SHAPE_COLOR_NAME.one____(screen,current_width,current_height)



#---------------------------------------------REPEAT_AFTER_ME
# new_round()


#---------------------------------------------DIRECTION_
from modules.MODE import DIRECTION as DIREC
DIREC.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
# new_round_DIRECTION()

#---------------------------------------------DIRECTION_
from modules.MODE import ACTION 
# reset_game_ACTION()

#---------------------------------------------DIRECTION_
from modules.MODE import MIRROR
# new_round_MIRROR()






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






# from modules.policy import draw_privacy_policy

# privacy_box = pygame.Rect(
#     current_width // 2 - 550 + 180,
#     current_height // 2 - 500 + 230,
#     740,
#     1000
# )


from modules.INFO import *
info_box = pygame.Rect(
    current_width // 2 - 370,
    current_height // 2 - 100,
    740,
    550
)







WIDTH, HEIGHT = screen.get_size()

dt = clock.tick(60) / 1000











from modules.transition import *
from modules.droping import *
from modules.custom_math import *

from modules.zh import *   
icon_start_time = pygame.time.get_ticks()
# icon_image__ = pygame.transform.smoothscale(pygame.image.load(
#     "asset/image/droping/qq.png"
# ).convert_alpha(),(100,100))




recent_game.load_recent_games()

recent_game.load_recent_images(
    "./asset/image/MODE"
)

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
from modules import  contact_us as CONTACT
from modules.MODE import  SUDOKU 
from modules.MODE import  WORD 
from modules.MODE import  MAZE 
from modules.MODE import  MATCH3  
from modules.MODE import  SNAKE  
from modules.MODE import  CONNECT_FOUR 
from modules.MODE import  UNBLOCK_CAR 
from modules.MODE import  MEMORY_HARD 
from modules.MODE import PUZZLE
from modules.MODE import GO
from modules.MODE import DOTS_BOX
from modules.MODE import CHECKERS
from modules.MODE import FOLLOW_FREE
from modules.MODE import MEMORY
from modules.MODE import CHESS
from modules.MODE import CHOOSE_IMAGE
from modules.MODE import SORT_NUMBER
from modules.MODE import MINESWEEPER
from modules.MODE import IMAGE_SELECT as IMSE
from modules.MODE import FIND_NUMBER as FNUM
from modules.MODE import FIND_NUMBER  
from modules.MODE import MEMORY  
from modules.MODE import REPEAT_AFTER_ME  
from modules.MODE import MORE_LESS_EQUAL  
from modules.MODE import DETECT
from modules.MODE import FAST
from modules.MODE import SIX_60S
from modules.MODE import TRUE_FALSE
from modules.MODE import FIND_OPERATOR
from modules.MODE import THOOZ
from modules import feedback as FEED_BACK
from modules.MODE.FIND_NUMBER import option_rects,current_question,correct_count, wrong_count , question_number
from modules.background_moving import *

from modules.coming_soon import *
# from modules.PUNCH_ import PUNCHH
# برای گرفتن اندازه های برای بازی چس 
SORT_NUMBER.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
# PUNCHH.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
SUDOKU.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
WORD.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
MINESWEEPER.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
MAZE.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
CHOOSE_IMAGE.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
MATCH3.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
CONNECT_FOUR.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
CHESS.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
M_ARR.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
DPRO.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
SNAKE.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
UNBLOCK_CAR.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
GO.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
DOTS_BOX.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
PUZZLE.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
CHECKERS.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
FOLLOW_FREE.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
MEMGO.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
MEMORY.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
FOTHAT.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
THOOZ.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
MEMORY_HARD.WIDTH_HEIGHT_gettter(screen,current_width,current_height)


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
from modules import policy as POL
from modules import image as all_image 
#-------------------------- for game start
countdown_done = False
previous_game_state = None
from modules.start_game import countdown
from modules.effect import *
from modules.exit import *
from modules import donate as DONATE
from modules.button_setting import *
from modules import music as MUS
from modules import mode as MO
from modules import start_screen as STS
from modules import typer as TYPER
from modules import date as DA
from modules import side_effect_window as S_E_W
from modules import menu__ as MENU__
from modules import INFO as INFO
from modules.MODE  import THOOZ as TOZ
#------------------------------------------------------------------------ پرچم ها 
#flage  in the game 
# flag_in_game = pygame.image.load("./asset/image/in_game/flage.png").convert_alpha()
#flage in menu
flag_in_menu= pygame.transform.smoothscale(pygame.image.load("./asset/image/in_game/flaginthegame.png").convert_alpha(),(800,400))



# from daily import today_game as TODAY 


cdcsc=fonts["heart"].render("profile",True,(255,255,255))

menu_open = True
from modules import menu_effect










from modules.game_mode_scroll import *

#############################################################################################################
#############################################################################################################


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
menu_state=None
DAILY_BUTTON=None
setting_menu=None
is_guest = None
# برای موزیک است 
control_every_button_in_setting_on_or_off= None
FOUR_ICON_FOR_SCREEN=None
restart_OFF_ON_game=None

SUPPORT_IS=None
# STOR_IS = None
DONT_LET_CLICK_GAMES_BUTTON_BEFORE_THAT=False


# عکس انتخابی کاربر و عکس گست 
# STS.user_image_selected
# STS.gest_image_selected
# ############################################################################################################
#############################################################################################################
# Game loop ------------------------------------------------------------------------------------------------------------------------------------



# ---------------------------------------------------------- این برای سیو است save

saved_player = SAVE.load_player()
#aiden
if saved_player is not None:


    game_state = "MENU"#start
    DASHBOARD=False

else:

    game_state = "NAME"#name
    DASHBOARD=False



#-------------------------------- حلقه
while running:



        
        
        
        

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
        # rect_for_music,
        # music_state,
        # sound_state,
        # rect_for_sound,
        # home_button_rect,
        # askus_button_rect,
        # share_button_rect,
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
        is_guest,
        restart_OFF_ON_game,
        store__button_rect,
        call_button_rect,
        support__button_rect,
        sms_button_rect,
        FOUR_ICON_FOR_SCREEN,
        DONT_LET_CLICK_GAMES_BUTTON_BEFORE_THAT

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

        # rect_for_music,
        # music_state,
        # sound_state,
        # rect_for_sound,
        # home_button_rect,
        # askus_button_rect,
        # share_button_rect,
        option_rects,
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
        image_game_mode_page5,
        image_game_mode_page6,
        image_game_mode_page7,
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
        is_guest,
        restart_OFF_ON_game,
        store__button_rect,
        call_button_rect,
        support__button_rect,
        sms_button_rect,
        FOUR_ICON_FOR_SCREEN,
        DONT_LET_CLICK_GAMES_BUTTON_BEFORE_THAT

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
    
    
        draw_punch_image(
            screen,
            profile_for_back,
            (current_width//2  , current_height // 2 ),
            (2000, 1300),
            "DAILY_GAME1"
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
        

        DES.menu_back_setters(
            screen,
            menu_bacccccck,
            x=220,
            y=current_height // 2 - 770,
            gap=2,
            first_x=220,
            first_y=current_height // 2 - 720,

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
            

#این ها باید درست بشن چون السشو همش اجرا میشن در همه حالت ها 
    # برای ساپورت است
        STS.draw_current_player(
            screen,
            profile_images,
            STS.current_player_type,
            (230, 116),
            STS.dashboard_player_profile
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




 
        

    if menu_state == "SUPPORT":

        # draw_4_images_SUPPORT(screen)
        draw_punch_image2(
            screen,
            new_window_for_more_support,
            CUS.positions_____1[0],
            (500, 500),#      (400, 400)
            "SUPPORT1",
            center_image=SUP.images_support[0],
            center_image_size=(300, 300),
            text="contact_us",
            text_font=fonts["date"]
        )
        
        draw_punch_image2(
            screen,
            new_window_for_more_support,
            CUS.positions_____1[1],
            (500, 500),#      (400, 400)
            "SUPPORT2",
            center_image=SUP.images_support[1],
            center_image_size=(300, 300),
            text="feedback",
            text_font=fonts["date"]
        )
        draw_punch_image2(
            screen,
            new_window_for_more_support,
            CUS.positions_____1[2],
            (500, 500),#      (400, 400)
            "SUPPORT3",
            center_image=SUP.images_support[2],
            center_image_size=(300, 300),
            text="donate",
            text_font=fonts["date"]
        )
        draw_punch_image2(
            screen,
            new_window_for_more_support,
            CUS.positions_____1[3],
            (500, 500),#      (400, 400)
            "SUPPORT4",
            center_image=SUP.images_support[3],
            center_image_size=(300, 300),
            text="report_bug",
            text_font=fonts["date"]
        )
        
        
        
        
        
        
        
        
        # SUP.support_punch(
        #     screen=screen,
        #     image=punch_11,
        #     center=(600, 400),
        #     target_size=(300, 300),
        #     page_id=1,
        #     duration=450,
        #     center_image=icon_image,
        #     center_image_size=(120, 120),
        #     text="Memory",
        #     text_font=font,
        #     text_color=(255, 255, 255)
        # )
        
        
        
        
        
        
        
        
        
        
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
            # open_window_with_side_effect(
            #     screen,
            #     all_image.contact,
            #     current_width // 2 ,current_height // 2 
            # )  
            
            S_E_W.open_window_with_side_effect_MULLTI_WINDOW(
                screen,
                all_image.contact,
                current_width // 2,
                current_height // 2,
                # S_E_W.contactt,
                )

            
            CONTACT.draw_social_links(
                screen,
                CONTACT.images,
                CONTACT.urls,
                current_x=400,
                current_y=350
            )

            CONTACT.draw_contact_form(
                screen,
                fonts["date"],
                current_x=850,
                current_y=500
            )
                    
            
            
            
            
            
            draw_back_button(
              screen,
              back_button_rect)

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
                all_image.feed,
                current_width // 2 ,current_height // 2 
            )  
            S_E_W.open_window_with_side_effect_MULLTI_WINDOW(
                screen,
                all_image.feed,
                current_width // 2,
                current_height // 2,
                # S_E_W.feedd,
                # on_draw=FEED_BACK.draw_contact_form
)
            feedback_star_rects = FEED_BACK.draw_contact_form(
                screen,
                fonts["date"]
            )

            draw_back_button(
              screen,
              back_button_rect)

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
            
            # open_window_with_side_effect(
            #     screen,
            #     all_image.donate,
            #     current_width // 2 ,current_height // 2 
            # )

            S_E_W.open_window_with_side_effect_MULLTI_WINDOW(
                screen,
                all_image.donate,
                current_width // 2,
                current_height // 2,
                )

            DONATE.draw_donate(
                screen,
                fonts["date"]
            )
            draw_back_button(
              screen,
              back_button_rect)

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
            # open_window_with_side_effect(
            #     screen,
            #     all_image.bug,
            #     current_width // 2 ,current_height // 2 
            # )
            S_E_W.open_window_with_side_effect_MULLTI_WINDOW(
                screen,
                all_image.bug,
                current_width // 2,
                current_height // 2,
                )


            report_bug.draw_report_bug(
                screen,
                fonts["date"]
            )
            draw_back_button(
              screen,
              back_button_rect)


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
        
 
        STS.start_profile_rect, STS.start_guest_rect = STS.draw_start_profile(
            screen,
            profile_images,
            selected_profile,
            PLAYER.player_name,
            current_width // 2,
            current_height // 2,
            STS.profile_center_image,
            STS.guest_center_image
        )
                
    if game_state == "MENU" and menu_state == "EXIT":
        draw_exit_confirmation(screen)
        
        
    if game_state == "MENU" and menu_state == "P_GAME_MODE":
        draw_punch_image2(
            screen,
            punch_1,
            (current_width//2 - 375 + 300, current_height // 2 ),
            (600, 600),
            "GAME_MODE",
            center_image=punch_1_1,
            center_image_size=(300, 300),
            text="PLAY GAMES",
            text_font=fonts["date"]
        )

        draw_punch_image2(
            screen,
            punch_2,
            (current_width//2 - 375 + 1000, current_height // 2),
            (600, 600),
            "MATH",
            center_image=punch_2_1,
            center_image_size=(300, 300),
            text="CUSTOM MATH",
            text_font=fonts["date"]
        )
        

        # draw_burst_icon(
        #     screen,
        #     icon_image__,
        #     current_width // 2,
        #     current_height // 2
        # )
    if game_state == "MENU" and menu_state == "DAILY GAME":
        #---- دو عکس چاپ میکنه 
        draw_punch_image_1(
            screen,
            IMG2,
            (current_width//2 - 375 + 830, current_height // 2  ),
            (700, 1050),
            "DAILY_GAME2",0.351,
            center_image=punch_status,
            center_image_size=(150, 150),
            text="Status",
            text_font=fonts["date"],
            )
        #---- دو عکس چاپ میکنه 
        draw_punch_image_1(
            screen,
            IMG1,
            (current_width//2 - 375 + 130, current_height // 2  ),
            (700, 1050),
            "DAILY_GAME1",0.351,
            center_image=punch_daily,
            center_image_size=(150, 150),
            text="Start Workout",
            text_font=fonts["date"]
        )
        





        

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
                current_width // 2,
                current_height // 2
            )

            punch_scale_animation_one_image(
                screen,
                play_next_page,
                "PLAY",
                current_width //2 - 200,
                current_height //2 + 200    
            )
            punch_scale_animation_one_image(
                screen,
                play_next_page,
                "NEXT",
                current_width //2 - 200,
                current_height //2 + 100    
            )
            punch_scale_animation_one_image(
                screen,
                back_page,
                "BACK",
                current_width //2 - 300,
                current_height //2 - 300
            )
        
            if DAILY_BUTTON == "GAME":#GAME
                print("this is aiden")

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
            SUPPORT_window1,
            current_width // 2,
            current_height //2
        )
        draw_back_button(
            screen,
            back_button_rect)




          
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
        

        # draw_new_screen(screen)
        

        # _window(screen,small_window)



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
        
        # donate_base(
        #     screen,
        #     call_button_rect
        # )        
    
        # image_setter(screen,pathth,xyz_for_profile_logo,current_height//2 - 666)
        # gif_setting(screen,gif_frames_credit,width_for_profile_logo,current_height // 2 - 570)
        # draw_profile_live_circle(
        #     screen,
        #     selected_profile_image,
        #     p99,
        #     current_width
        # )
        # donate_button(
        #     screen,
        #     call_button_rect
        # )

        
        
        

        
        
        
        
        
        
        
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


    # if game_state == "MORE":
    #     #------------------------for background flying  _ i cand do that


        
        # عکس دایره. برای پروفایل هر صفحه
        # image_setter(screen,pathth,xyz_for_profile_logo,current_height//2 - 666)
        # gif_setting(screen,gif_frames_about,width_for_profile_logo,current_height // 2 - 570)

        # if support_face == "How to Play":
        #      draw_support_face(screen,current_width,current_height)
        # if support_face == "FAQ":
        #      draw_support_face(screen,current_width,current_height)
        # if support_face == "INFO":
        #      draw_support_face(screen,current_width,current_height)
        #     #  draw_info_profile(
        #     #     screen,
        #     #     current_width,
        #     #     current_height
        #     #     )
        #      draw_info(
        #         screen,
        #         info_box
        #         )
        # if support_face == "Privacy Policy":
        #      draw_support_face(screen,current_width,current_height)
             

             
        
        
        


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
    

        
        
        
   
        
        # آپدیت اسلاید
        game_mode_slide.update()

        offset = game_mode_slide.get_offset()



        # update_vertical_scroll()
        # draw_vertical_scroll_grid(
        #     screen,
        #     MO.sadasdadasd,
        #     card_gap_x=500,
        #     card_gap_y=500
        # )    

        update_center_images_punch()
        image_game_mode_page1 , _ ,_ , _ = draw_game_mode_page(
            screen,
            MO.images_MODE_page1,
            MO.image_sizes_page,
            500,
            500,
            offset,
            center_images=MO.center_images_MODE,
            center_start_index=0,
            overlay_images=[
                None,
                None,
                None,
                None,
                None,
                None
            ],
            badge_images=[
                fr_BG,
                fr_BG,
                fr_BG,
                fr_BG,
                fr_BG,
                fr_BG
            ],
            feature_badge_images=[
                MODE.logic,
                MODE.detection,
                MODE.detection,
                MODE.logic,
                MODE.logic,
                MODE.memory,
            ],
        )
        
        draw_game_mode_text(
            screen,
            image_game_mode_page1,
            MO.game_names,
            fonts["date"],
            text_start_index=0
        ) 
                
        
        
        
        
        
        
        
        
        
        
        
        
        
                
        image_game_mode_page2, _ ,_,_ = draw_game_mode_page(
            screen,
            MO.images_MODE_page2,
            MO.image_sizes_page,
            500,
            500,
            offset + screen.get_width(),
            center_images=MO.center_images_MODE,
            center_start_index=6,

            overlay_images=[
                None,
                None,
                None,
                None,
                None,
                None
            ],
            badge_images=[
                fr_BG,
                fr_BG,
                fr_BG,
                fr_BG,
                fr_BG,
                fr_BG
            ],
            feature_badge_images=[
                MODE.detection,
                MODE.math,
                MODE.logic,
                MODE.logic,
                MODE.math,
                MODE.memory,

            ],
        )
                
        draw_game_mode_text(
            screen,
            image_game_mode_page2,
            MO.game_names,
            fonts["date"],
            text_start_index=6
        ) 
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        image_game_mode_page3, _ , _ , _ = draw_game_mode_page(
            screen,
            MO.images_MODE_page3,
            MO.image_sizes_page,
            500,
            500,
            offset + screen.get_width() * 2,
            center_images=MO.center_images_MODE,
            center_start_index=12,

            overlay_images=[
                None,
                None,
                None,
                None,
                None,
                None
            ],
            badge_images=[
                pr_BG,
                pr_BG,
                pr_BG,
                pr_BG,
                pr_BG,
                pr_BG
            ],
            feature_badge_images=[
                MODE.math,
                MODE.detection,
                MODE.detection,
                MODE.memory,
                MODE.memory,
                MODE.math,
            ],
        )
        draw_game_mode_text(
            screen,
            image_game_mode_page3,
            MO.game_names,
            fonts["date"],
            text_start_index=12
        ) 
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        image_game_mode_page4,  _ ,_ ,_ = draw_game_mode_page(
            screen,
            MO.images_MODE_page4,
            MO.image_sizes_page,
            500,
            500,
            offset + screen.get_width() * 3,
            center_images=MO.center_images_MODE,
            center_start_index=18,

            overlay_images=[
                None,
                None,
                None,
                None,
                None,
                None
            ],
            badge_images=[
                pr_BG,
                pr_BG,
                pr_BG,
                pr_BG,
                pr_BG,
                pr_BG
            ],
            feature_badge_images=[
                MODE.detection,
                MODE.detection,
                MODE.memory,
                MODE.fast,
                MODE.math,
                MODE.math,

            ],
        )
        
        draw_game_mode_text(
            screen,
            image_game_mode_page4,
            MO.game_names,
            fonts["date"],
            text_start_index=18
        ) 
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        image_game_mode_page5, _ ,  _ , _ = draw_game_mode_page(
            screen,
            MO.images_MODE_page1,
            MO.image_sizes_page,
            500,
            500,
            offset + screen.get_width() * 4,
            center_images=MO.center_images_MODE,
            center_start_index=24,

            overlay_images=[
                None,
                None,
                None,
                None,
                None,
                None
            ],
            badge_images=[
                pr_BG,
                pr_BG,
                pr_BG,
                pr_BG,
                pr_BG,
                pr_BG
            ],
            feature_badge_images=[
                MODE.fast,
                MODE.math,
                MODE.detection,
                MODE.detection,
                MODE.detection,
                MODE.fast,
  
            ],
        )
        draw_game_mode_text(
            screen,
            image_game_mode_page5,
            MO.game_names,
            fonts["date"],
            text_start_index=24
        ) 
        
        
        
        
        
        
        
        
        
        
        
        
        image_game_mode_page6,  _ ,_ , _ = draw_game_mode_page(
            screen,
            MO.images_MODE_page1,
            MO.image_sizes_page,
            500,
            500,
            offset + screen.get_width() * 5,
            center_images=MO.center_images_MODE,
            center_start_index=30,
            overlay_images=[
                None,
                None,
                None,
                None,
                None,
                None
            ],
            badge_images=[
                pr_BG,
                pr_BG,
                pr_BG,
                pr_BG,
                pr_BG,
                pr_BG
            ],
            feature_badge_images=[
                MODE.logic,
                MODE.logic,
                MODE.detection,
                MODE.logic,
                MODE.logic,
                MODE.detection,
            ],
        )
        draw_game_mode_text(
            screen,
            image_game_mode_page6,
            MO.game_names,
            fonts["date"],
            text_start_index=30
        ) 
                






        image_game_mode_page7, _ , _ , _ = draw_game_mode_page(
            screen,
            MO.images_MODE_page1,
            MO.image_sizes_page,
            500,
            500,
            offset + screen.get_width() * 6,
            center_images=MO.center_images_MODE,
            center_start_index=36,

            overlay_images=[
                None,
                None,
                None,
                None,
                MO.my_icon,
                MO.my_icon
            ],
            badge_images=[
                pr_BG,
                pr_BG,
                pr_BG,
                pr_BG,
                cm_BG,
                cm_BG
            ],
            feature_badge_images=[
                MODE.logic,
                MODE.logic,
                MODE.detection,
                MODE.memory,
                None,
                None,
            ],
        )

        
        draw_game_mode_text(
            screen,
            image_game_mode_page7,
            MO.game_names,
            fonts["date"],
            text_start_index=36
        ) 
                
                
        
        
        
        
        
        
        
        image_game_mode_page8, _ , _ , _ = draw_game_mode_page(
            screen,
            MO.images_MODE_page1,
            MO.image_sizes_page,
            500,
            500,
            offset + screen.get_width() * 7,
            center_images=MO.center_images_MODE,
            center_start_index=40,

            overlay_images=[
                MO.my_icon,
                MO.my_icon,
                MO.my_icon,
                MO.my_icon,
                MO.my_icon,
                MO.my_icon
            ],
            badge_images=[
                cm_BG,
                cm_BG,
                cm_BG,
                cm_BG,
                cm_BG,
                cm_BG
            ],
        )

        draw_game_mode_text(
            screen,
            image_game_mode_page8,
            MO.game_names,
            fonts["date"],
            text_start_index=40
        ) 
                
        
        
        
        
        
        
        
        
        
        image_game_mode_page9,  _ ,_ , _ = draw_game_mode_page(
            screen,
            MO.images_MODE_page1,
            MO.image_sizes_page,
            500,
            500,
            offset + screen.get_width() * 8,
            center_images=MO.center_images_MODE,
            overlay_images=[
                MO.my_icon,
                MO.my_icon,
                MO.my_icon,
                MO.my_icon,
                MO.my_icon,
                MO.my_icon
            ],
            badge_images=[
                cm_BG,
                cm_BG,
                cm_BG,
                cm_BG,
                cm_BG,
                cm_BG
            ],
        )
        
        image_game_mode_page10,  _ ,_ , _ = draw_game_mode_page(
            screen,
            MO.images_MODE_page1,
            MO.image_sizes_page,
            500,
            500,
            offset + screen.get_width() * 9,
            center_images=MO.center_images_MODE,
            overlay_images=[
                MO.my_icon,
                MO.my_icon,
                MO.my_icon,
                MO.my_icon,
                MO.my_icon,
                MO.my_icon
            ],
            badge_images=[
                cm_BG,
                cm_BG,
                cm_BG,
                cm_BG,
                cm_BG,
                cm_BG
            ],
        )

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if TYPER.typing_start_time is not None:
        if MO.page1_active:
            # print("page1")
            finished_type = TYPER.draw_typing_text(
            screen,
            "MATH",
            fonts["heart"],
            (255, 140, 30),
            (current_width // 2, current_height // 2 - 530),
            TYPER.typing_start_time,
            80
        )
        if MO.page2_active:
            # print("page2")
            finished_type = TYPER.draw_typing_text(
            screen,
            "MEMORY",
            fonts["heart"],
            (255, 140, 30),
            (current_width // 2, current_height // 2 - 530),
            TYPER.typing_start_time,
            80
        )
        if MO.page3_active:
            # print("page3")
            finished_type = TYPER.draw_typing_text(
            screen,
            "GET PREMIUM",
            fonts["heart"],
            (255, 140, 30),
            (current_width // 2, current_height // 2 - 530),
            TYPER.typing_start_time,
            80
        )
        if MO.page4_active:
            # print("page4")
            finished_type = TYPER.draw_typing_text(
            screen,
            "GET PREMIUM",
            fonts["heart"],
            (255, 140, 30),
            (current_width // 2, current_height // 2 - 530),
            TYPER.typing_start_time,
            80
        )
        if MO.page5_active:
            # print("page5")
            finished_type = TYPER.draw_typing_text(
            screen,
            "GET PREMIUM",
            fonts["heart"],
            (255, 140, 30),
            (current_width // 2, current_height // 2 - 530),
            TYPER.typing_start_time,
            80
        )
        if MO.page6_active:
            # print("page6")
            finished_type = TYPER.draw_typing_text(
            screen,
            "GET PREMIUM",
            fonts["heart"],
            (255, 140, 30),
            (current_width // 2, current_height // 2 - 530),
            TYPER.typing_start_time,
            80
        )

        if MO.page7_active:
            # print("page6")
            finished_type = TYPER.draw_typing_text(
            screen,
            "GET PREMIUM",
            fonts["heart"],
            (255, 140, 30),
            (current_width // 2, current_height // 2 - 530),
            TYPER.typing_start_time,
            80
        )

        if MO.page8_active:
            # print("page6")
            finished_type = TYPER.draw_typing_text(
            screen,
            "COMING SOON...",
            fonts["heart"],
            (255, 140, 30),
            (current_width // 2, current_height // 2 - 530),
            TYPER.typing_start_time,
            80
        )
        if MO.page9_active:
            # print("page6")
            finished_type = TYPER.draw_typing_text(
            screen,
            "COMING SOON...",
            fonts["heart"],
            (255, 140, 30),
            (current_width // 2, current_height // 2 - 530),
            TYPER.typing_start_time,
            80
        )
        if MO.page10_active:
            # print("page6")
            finished_type = TYPER.draw_typing_text(
            screen,
            "COMING SOON...",
            fonts["heart"],
            (255, 140, 30),
            (current_width // 2, current_height // 2 - 530),
            TYPER.typing_start_time,
            80
        )



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
            10,
            current_height// 2 + 600
        )

        # _window(screen,small_window)

        # donate_base(
        #     screen,
        #     call_button_rect
        # )
        # draw_back_button(
        # screen,
        # back_button_rect
        # )
        # support_button(
        #     screen,
        #     support_button_rect
        # )
        # bug_button(
        #     screen,
        #     bug_button_rect
        # # )     
        # donate_button(
        #     screen,
        #     call_button_rect
        # )

        draw_profile_live_circle(
            screen,
            selected_profile_image,
            p99,
            current_width
        )
        # عکس دایره. برای پروفایل هر صفحه
        # image_setter(screen,pathth,xyz_for_profile_logo,current_height//2 - 666)
        # gif_setting(screen,gif_frames_mode,width_for_profile_logo,current_height // 2 - 570)



        draw_back_button(
            screen,
            back_button_rect)

    if game_state == "MEMORY":
        MEMORY.memory_(
            screen,
            current_width,
            current_height
        )
        draw_back_button(
            screen,
            back_button_rect)
    #---------------------------------------------------------------------------------STEP5

    # if ceill_entered and not time_entered:        
    if game_state == "TIME":

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
            
    #     square_rect = pygame.Rect(
    #         current_width // 2 - 800 // 2,
    #         current_height // 2 - 450 // 2,
    #         800,
    #         450
    #     )
    #     draw_new_screen(screen)

                
    #    # gallery_button(
    #     #     screen,
    #     #     gallery_button_rect
    #     # )
    #     # _window(screen,small_window)





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
        # donate_base(
        #     screen,
        #     call_button_rect
        # )
        # bug_button(
        #     screen,
        #     bug_button_rect
        # )
        # donate_button(
        #     screen,
        #     call_button_rect
        # )

        #-------------------------gif for time
        # image_setter(screen,pathth,xyz_for_profile_logo,current_height//2 - 666)
        # gif_setting(screen,gif_frames,width_for_profile_logo,current_height // 2 - 570)
        
        # draw_profile_live_circle(
        #     screen,
        #     selected_profile_image,
        #     p99,
        #     current_width
        # )
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        


        DES.menu_back_setters(
            screen,
            setting_backkkkkk,
            x=220,
            y=current_height // 2 - 770,
            gap=2,
            first_x=220,
            first_y=current_height // 2 - 720,
        )


        STS.draw_current_player(
            screen,
            profile_images,
            STS.current_player_type,
            (230, 116),
            STS.dashboard_player_profile
        )

        draw_setting_buttons(
            screen,
            current_width,
            current_height,
            fonts,
            settings_rects
        )

        # donate_base(
        #     screen,
        #     call_button_rect
        # )
        # draw_back_button(
        #     screen,
        #     back_button_rect_for_setting
        # )
        # support_button(
        #     screen,
        #     support_button_rect
        # )

        # donate_button(
        #     screen,
        #     call_button_rect
        # )


        #----------------------------------این برای داشتبورد است 
        
        # if DASHBOARD :
            
        #     #     #-------------------

        #     DA.draw_dashboard_date(
        #         screen,
        #         DA.day_image,
        #         DA.month_images,
        #         fonts["DAY"],
        #         fonts["weekdays"],
        #         fonts["month"],
        #         fonts["date"]
        #     )














    if game_state == "BEFORE_GAMES_COUNT_DOWN":
        # countdown(screen, image)

        for index, game_name in enumerate(game_list.count_down_game_name):

            if before_game.previous_game_state_F == game_name:

                image = game_list.count_down_image[index]

                countdown(screen, image)
                break

        before_game.before_game_start = False
        game_state = before_game.previous_game_state_F
        before_game.backgorund_now_for_any_game_mode = image
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
        # punch_scale_animation_one_image(
        #     screen,
        #     games_first_window,
        #     "NEXT",
        #     current_width //2 - 400,
        #     current_height //2 - 400    
        # )
        open_window_with_side_effect(
            screen,
            SUPPORT_window1,
            current_width // 2,
            current_height //2
        )
        punch_scale_animation_one_image(
            screen,
            next_page,
            "NEXT",
            current_width //2 + 900,
            current_height //2 +540    
        )
        punch_scale_animation_one_image(
            screen,
            back_page,
            "BACK",
            current_width //2 - 900,
            current_height //2 + 540
        )
    #۳ در انی  گیم استیت میشه بالایی 





    if game_state == "SUPPORT_CALL":
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
    
        open_window_with_side_effect(
            screen,
            STOR__,
            current_width// 2,
            current_height//2 
        )
        draw_back_button(
            screen,
            back_button_rect
        )
    if game_state == "STORE":
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
    
        open_window_with_side_effect(
            screen,
            STOR__,
            current_width// 2,
            current_height//2 
        )

        draw_back_button(
            screen,
            back_button_rect
        )
    if menu_state == "MESSAGE":
                # for background  flying and image 
        draw_punch_image(
            screen,
            IMG1,
            (current_width//2 - 350 , current_height // 2 - 525 ),
            (700, 1050),
            "DAILY_GAME1"
        )
        draw_back_button(
            screen,
            back_button_rect)
    if game_state == "DONATE":
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
    
        open_window_with_side_effect(
            screen,
            STOR__,
            current_width// 2,
            current_height//2 
        )

        draw_back_button(
            screen,
            back_button_rect
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
        # _window(screen,small_window)
                
                
                
                
                
        draw_back_button(
            screen,
            back_button_rect
        )
        
        
        # image_setter(screen,pathth,xyz_for_profile_logo,current_height//2 - 666)

        # gif_setting(screen,gif_frames_op,width_for_profile_logo,current_height // 2 - 570)
        # donate_base(
        #     screen,
        #     call_button_rect
        # )       
        # support_button(
        #     screen,
        #     support_button_rect
        # )
        # bug_button(
        #     screen,
        #     bug_button_rect
        # ) 
        # donate_button(
        #     screen,
        #     call_button_rect
        # )   

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
        #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state == "MEMORY":
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)

            MEMORY.memory_(
                screen,
                current_width,
                current_height
            )
            
            draw_back_button(
                screen,
                back_button_rect
            )
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state == "SHAPE_COLOR_NAME":
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)
            SHAPE_COLOR_NAME.SHAPE_COLOR_NAME(screen,current_width)
            
            draw_back_button(
                screen,
                back_button_rect
            )
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state == "REPEAT_AFTER_ME":
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)
            REPEAT_AFTER_ME.REPEAT_AFTER_ME_(screen)
            
            
            draw_back_button(
                screen,
                back_button_rect
            )
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state == "DIRECTION":
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)

            DIREC.DIRECTION_(screen)
            
            
            draw_back_button(
                screen,
                back_button_rect
            )
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if  game_state == "MIRROR":
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)

            MIRROR.MIRROR_(screen)

            draw_back_button(
                screen,
                back_button_rect
            )
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="ACTION":
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)

            ACTION.ACTION_(screen)
            draw_back_button(
                screen,
                back_button_rect
            )

    
    # page 2
   #----------------------------------------------------------------------------------------------------------------
   #----------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------------------------------------------------------

        # if now_game_start:
        #     # if previous_game_state != "FIND_NUMBER":

                # ---------------- Question Background ----------------

    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾

    if game_state == "FIND_NUMBER":
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
                
            # before_game.window_before_start_game(screen,dt,current_width,current_height)# این صفحه اول است  بعد از این صفحه صفحه دوم بیاد 
            # if not now_game_start:
            #     countdown(# اسن صفحه دوم خب بعد از این صفحه دوم بازی بیاد 
            #         screen,
            #         FIND_NUMBER_BACKGROUND
            #     )

            #     now_game_start = True
            # else:


            
            # ============================================================
            # FIND NUMBER
            # ============================================================
            back_setter(
                screen,
                before_game.backgorund_now_for_any_game_mode
            )



        #     # ---------------- Question Background ----------------

        #     image_setter(
        #         screen,
        #         image_back_quastion,
        #         current_width // 2 - 600,
        #         current_height // 2 - 550
        #     )


        #     # ============================================================
        #     # MAKE SURE QUESTION EXISTS
        #     # ============================================================

        #     if current_question is None:

        #         current_question = generate_missing_number_question(
        #             question_number
        #         )

        #         start_time = pygame.time.get_ticks()

        #         progress = 1.0


        #     #-------------------red green blue معجون
        #     B_excir_(screen)
        #     G_excir_(screen)
        #     R_excir_(screen)

        #     # ============================================================
        #     # HINT
        #     # ============================================================
        #     hint_1(screen)
        #     hint(screen)


        #     # ============================================================
        #     # SAVE
        #     # ============================================================

        #     # save(screen)


        #     # ============================================================
        #     # TIMER CALCULATION
        #     # ============================================================

        #     elapsed = (
        #         pygame.time.get_ticks() - start_time
        #     ) / 1000


        #     progress = 1 - (
        #         elapsed / current_question["time"]
        #     )


        #     progress = max(
        #         0,
        #         min(1, progress)
        #     )


        #     # ============================================================
        #     # QUESTION
        #     # ============================================================
        #     FNUM.update_game()
        #     draw_question_find_number(
        #         screen,
        #         fonts,
        #         FNUM.current_question,
        #         current_width,
        #         current_height
        #     )


        #     # ============================================================
        #     # TIMER CIRCLE
        #     # ============================================================

        #     draw_timer_circle(
        #         screen,
        #         (160, 160),
        #         80,
        #         progress
        #     )


        #     # ============================================================
        #     # TIMEOUT
        #     # ============================================================

        #     if elapsed >= current_question["time"]:

        #         # سؤال بدون جواب → اشتباه
        #         wrong_count += 1


        #         # سؤال بعدی
        #         question_number += 1


        #         current_question = generate_missing_number_question(
        #             question_number
        #         )


        #         # ریست تایمر
        #         start_time = pygame.time.get_ticks()


        #         # ریست دایره تایمر
        #         progress = 1.0


        #     # ============================================================
        #     # SCORE
        #     # ============================================================

        #     correct_text = fonts["name"].render(
        #         f"Correct: {correct_count}",
        #         True,
        #         (0, 255, 0)
        #     )


        #     wrong_text = fonts["name"].render(
        #         f"Wrong: {wrong_count}",
        #         True,
        #         (255, 0, 0)
        #     )


        #     screen.blit(
        #         correct_text,
        #         (50, 50)
        #     )


        #     screen.blit(
        #         wrong_text,
        #         (300, 50)
        #     )


        #     # ============================================================
        #     # PLAYER
        #     # ============================================================

        #     draw_profile_live_circle(
        #         screen,
        #         selected_profile_image,
        #         p99,
        #         current_width
        #     )


        #     # ============================================================
        #     # UI
        #     # ============================================================

        #     # in_game_alarm(
        #     #     screen
        #     # )

        #     move_flage(
        #         flag_in_game,
        #         screen,
        #         current_width // 2 - 154,
        #         True,
        #         800
        #     )


        #     # menuu(
        #     #     screen
        #     # )


        #     restart(
        #         screen
        #     )


        #     exit__(
        #         screen
        #     )


        #     draw_back_button(
        #         screen,
        #         back_button_rect
        #     )
        #     save_1(screen)
        #     marshmallow_image(save_,screen,1900,current_height//2 - 290,15000)
        #     marshmallow_image(menuu1,screen,1860,current_height//2 + 470,7000)
        #     marshmallow_image(G,screen,current_width//2 - 956,current_height//2 - 120,20000)
        #     marshmallow_image(R,screen,current_width//2 - 956,current_height//2 + 35,10000)
        #     marshmallow_image(B,screen,current_width//2 - 950,current_height//2 - 290,15000)
            
        #     score_base(screen)
        #     scoreee11(screen)
        # previous_game_state =game_state
        
        
        
        
        
    
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾

    if game_state == "60S":
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
                #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
            back_setter(
                screen,
                before_game.backgorund_now_for_any_game_mode
            )


            SIX_60S.SIX_60S(
                screen,
                current_width
            )


            # ---------------- Back ----------------

            draw_back_button(
                screen,
                back_button_rect
            )


    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state == "MORE_LESS_EQUAL":
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)

            MORE_LESS_EQUAL.MORE_LESS_EQUAL_(screen)
            draw_profile_live_circle(
                screen,
                selected_profile_image,
                p99,
                current_width
            )
            # in_game_button(
            #     screen,
            #     home_button_rect,
            #     menu
            # )
            draw_back_button(
                screen,
                back_button_rect
            )

    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state == "TRUE_FALSE":
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)

            TRUE_FALSE.TRUE_FALSE_(screen)
            draw_profile_live_circle(
                screen,
                selected_profile_image,
                p99,
                current_width
            )
            draw_back_button(
                screen,
                back_button_rect
            )
            

    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state == "FIND_OPERATOR":
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)

            FIND_OPERATOR.FIND_OPERATOR_(screen)
            draw_profile_live_circle(
                screen,
                selected_profile_image,
                p99,
                current_width
            )
            # in_game_button(
            #     screen,
            #     home_button_rect,
            #     menu
            # )
            draw_back_button(
                screen,
                back_button_rect
            )
        
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="DETECT":
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)
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
            DETECT.DETECT_(screen,current_width,current_height)


            draw_back_button(
                screen,
                back_button_rect
            )

    # page 3
   #----------------------------------------------------------------------------------------------------------------
   #----------------------------------------------------------------------------------------------------------------
   #----------------------------------------------------------------------------------------------------------------


    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="FAST":
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)

            FAST.FAST_(screen,current_width)
            draw_back_button(
                screen,
                back_button_rect
            )


            draw_back_button(
                screen,
                back_button_rect
            )
            
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    # بک گراند این ها رو درست کنم ندارن 
    if game_state =="HOW_MANY":
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)
            HOW.HOW_MANY_(screen,current_width,current_height)
            draw_back_button(
                screen,
                back_button_rect
            )

    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="HARD":
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)

            HARD.HARD_(screen,current_width,current_height)
            draw_back_button(
                screen,
                back_button_rect
            )
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="DETECT_PRO":
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)
            
            DPRO.DETECT_PRO_(screen,current_width,current_height)
            draw_back_button(
                screen,
                back_button_rect
            )
     #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="MEMORY_GO":
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)

            MEMGO.MEMORY_GO_(screen,current_width,current_height)
            draw_back_button(
                screen,
                back_button_rect
            )

    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="MOVE_ARROW":
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)
            M_ARR.MOVE_ARROW_(screen,current_width,current_height)
            draw_back_button(
                screen,
                back_button_rect
            )


    # page 4
   #----------------------------------------------------------------------------------------------------------------
   #----------------------------------------------------------------------------------------------------------------
   #----------------------------------------------------------------------------------------------------------------
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="MATH_GO":
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)

            MATHGO.MATH_GO_(screen)
            draw_back_button(
                screen,
                back_button_rect
            )

    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="FAST_ADD_SUB":
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)

            FAS.QUICK_MATH(screen)
            draw_back_button(
                screen,
                back_button_rect
            )
        
        
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="FOLLOW_THAT":
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم")
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)

            FOTHAT.FOLLOW_THAT_(screen)
            draw_back_button(
                screen,
                back_button_rect
            )
        
        
        
        
        
        
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="IMAGE_SELECT":
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم برای دکمه ریستارت بازی ")
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)

            IMSE.IMAGE_SELECT_(screen)

            draw_back_button(
                screen,
                back_button_rect
            )
            
            
        
        
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="THOOZ":

        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:     
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)
  
            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم برای دکمه ریستارت بازی ")
            TOZ.update_computer_move()
            TOZ.THOOZ_(screen,current_width)
            
            draw_back_button(
                screen,
                back_button_rect
            )
            
            
            
            
            
            
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="CHESS":
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)

            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم برای دکمه ریستارت بازی ")
            CHESS.CHESS_()
            
            draw_back_button(
                screen,
                back_button_rect
            )

    # page 5
   #----------------------------------------------------------------------------------------------------------------
   #----------------------------------------------------------------------------------------------------------------
   #----------------------------------------------------------------------------------------------------------------
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="SORT_NUMBER":
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم برای دکمه ریستارت بازی ")
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)

            SORT_NUMBER.SORT_NUMBER_()
            draw_back_button(
                screen,
                back_button_rect
            )
        
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="SUDOKU":
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)

            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم برای دکمه ریستارت بازی ")
            SUDOKU.SUDOKU_()
            draw_back_button(
                screen,
                back_button_rect
            )
            
        
        
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="WORD":
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)

            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم برای دکمه ریستارت بازی ")
            WORD.WORD_()
            draw_back_button(
                screen,
                back_button_rect
            )
        
        
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="MINESWEEPER":
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)

            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم برای دکمه ریستارت بازی ")
            MINESWEEPER.MINESWEEPER_()
            draw_back_button(
                screen,
                back_button_rect
            )
        
        
        
        
        
    
        
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="MAZE":
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)

            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم برای دکمه ریستارت بازی ")
            MAZE.MAZE_()
            draw_back_button(
                screen,
                back_button_rect
            )
            
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="MEMORY_HARD":
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)

            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم برای دکمه ریستارت بازی ")
            MEMORY_HARD.update()
            MEMORY_HARD.MEMORY_HARD_()

            draw_back_button(
                screen,
                back_button_rect
            )

       # page 6
   #----------------------------------------------------------------------------------------------------------------
   #----------------------------------------------------------------------------------------------------------------
   #----------------------------------------------------------------------------------------------------------------
   
   #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="CHOOSE_IMAGE":
        
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)

            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم برای دکمه ریستارت بازی ")
            CHOOSE_IMAGE.CHOOSE_IMAGE_()
            draw_back_button(
                screen,
                back_button_rect
            )
   #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="MATCH3":
        
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:    
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)
   
            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم برای دکمه ریستارت بازی ")
            MATCH3.MATCH3_()
            draw_back_button(
                screen,
                back_button_rect
            )
   #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="CONNECT_FOUR":
        
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)

            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم برای دکمه ریستارت بازی ")
            CONNECT_FOUR.CONNECT_FOUR_()
            draw_back_button(
                screen,
                back_button_rect
            )
   #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="SNAKE":
        
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)

            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم برای دکمه ریستارت بازی ")
            SNAKE.main_SNAKE()
            draw_back_button(
                screen,
                back_button_rect
            )

   
   
   #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="UNBLOCK_CAR":
        
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)

            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم برای دکمه ریستارت بازی ")
            UNBLOCK_CAR.main()
            draw_back_button(
                screen,
                back_button_rect
            )
   #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="PUZZLE":
        
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:      
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)
 
            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم برای دکمه ریستارت بازی ")
            PUZZLE.PUZZLE_()
            draw_back_button(
                screen,
                back_button_rect
            )

       # page 7
   #----------------------------------------------------------------------------------------------------------------
   #----------------------------------------------------------------------------------------------------------------
   #----------------------------------------------------------------------------------------------------------------
   
   #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="CHECKERS":
        
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)

            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم برای دکمه ریستارت بازی ")
            CHECKERS.CHECKERS_()
            draw_back_button(
                screen,
                back_button_rect
            )
   #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="DOTS_BOX":
        
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)

            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم برای دکمه ریستارت بازی ")
            DOTS_BOX.DOTS_BOX_()
            draw_back_button(
                screen,
                back_button_rect
            )
   #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="FOLLOW_FREE":
        
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:    
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)
   
            #ادامه کد 
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم برای دکمه ریستارت بازی ")
            FOLLOW_FREE.FOLLOW_FREE_()
            draw_back_button(
                screen,
                back_button_rect
            )
   #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="GO":
        
        before_game.previous_game_state_F = game_state
        if before_game.before_game_start  == True:
            game_state = "BEFORE_GAMES"
        else:       
            #ادامه کد 
            back_setter(screen,before_game.backgorund_now_for_any_game_mode)
            if restart_OFF_ON_game == True:
                print("ریستارت هر بازی رو باید این جا بنویسم برای هر بازی این رو میخام در این  جا بنویسم برای دکمه ریستارت بازی ")
            GO.GO_()
            draw_back_button(
                screen,
                back_button_rect
            )

   
   

   
   
   
   
   
   
   



   
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
        # donate_base(
        #     screen,
        #     call_button_rect
        # )
        # bug_button(
        #     screen,
        #     bug_button_rect
        # )   
        # donate_button(
        #     screen,
        #     call_button_rect
        # )

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



     
    # if game_state == "LEADERBOARD":
    # if menu_state == "COMMING SOON":

    #     # draw_moving_map(
    #     #     screen,
    #     #     WIDTH,
    #     #     HEIGHT,
    #     #     dt    )
    #     # draw_flying_birds(
    #     #     screen,
    #     #     current_width,
    #     #     current_height
    #     # )   
    #     # open_window_with_side_effect(
    #     #     screen,
    #     #     SUPPORT_window1,
    #     #     current_width // 2,
    #     #     current_height //2
    #     # )
    #     coming_soon_notification(screen,True)

    #     # draw_back_button(
        #     screen,
        #     back_button_rect)

        
        



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

        open_window_with_side_effect(
            screen,
            all_image.music,
            current_width // 2 + 150,current_height // 2 
        )
        draw_music(
            screen,
            current_width,
            current_height,
            all_image.music,
            music_profile_image
        )

    if  game_state == "SETTING" and setting_menu == "LANGUAGE" and control_every_button_in_setting_on_or_off == "language":

        open_window_with_side_effect(
                screen,
                all_image.language,
                current_width // 2 + 150,current_height // 2 
            )

        language_rects = draw_languages(
            screen,
            current_width,
            current_height
        )
    
        
    if  game_state == "SETTING" and setting_menu == "MORE" and control_every_button_in_setting_on_or_off == "more":

        
        
        

        draw_punch_image2(
            screen,
            new_window_for_more_support,
            CUS.positions_____1[0],
            (500, 500),
            "MORE1",
            center_image=MORE.images_support[0],
            center_image_size=(300, 300),
            text="faq",
            text_font=fonts["date"]
        )
        draw_punch_image2(
            screen,
            new_window_for_more_support,
            CUS.positions_____1[1],
            (500, 500),
            "MORE2",
            center_image=MORE.images_support[1],
            center_image_size=(300, 300),
            text="info",
            text_font=fonts["date"]
        )
        
        draw_punch_image2(
            screen,
            new_window_for_more_support,
            CUS.positions_____1[2],
            (500, 500),
            "MORE3",
            center_image=MORE.images_support[2],
            center_image_size=(300, 300),
            text="privacy_policy",
            text_font=fonts["date"]
        )
        
        # more app
        draw_punch_image2(
            screen,
            new_window_for_more_support,
            CUS.positions_____1[3],
            (500, 500),
            "MORE4",
            center_image=MORE.images_support[3],
            center_image_size=(300, 300),
            text="more_app",
            text_font=fonts["date"]
        )
        
        draw_back_button(
            screen,
            back_button_rect)
        
        

    if game_state == "FAQ":
        
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

        S_E_W.open_window_with_side_effect_MULLTI_WINDOW(
            screen,
            all_image.faq,
            current_width // 2,
            current_height // 2,
            # S_E_W.faqq,
            on_draw=FAQ.draw_FAQ_side_effect
        )
        draw_back_button(
            screen,
            back_button_rect)
        
    if game_state == "INFO":
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

        # open_window_with_side_effect(
        #         screen,
        #         all_image.info,
        #         current_width // 2 ,current_height // 2 
        #     )
        S_E_W.open_window_with_side_effect_MULLTI_WINDOW(
            screen,
            all_image.info,
            current_width // 2,
            current_height // 2,
            # S_E_W.infoo,
            on_draw=INFO.draw_INFO_side_effect

        )
        draw_back_button(
            screen,
            back_button_rect)
    if game_state == "Privacy Policy":

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

        # open_window_with_side_effect(
        #         screen,
        #         all_image.policy,
        #         current_width // 2 ,current_height // 2 
        #     )
        S_E_W.open_window_with_side_effect_MULLTI_WINDOW(
            screen,
            all_image.policy,
            current_width // 2,
            current_height // 2,
            # S_E_W.policyy,
            on_draw=POL.draw_privacy_side_effect
        )
        
        
        
        
        draw_back_button(
            screen,
            back_button_rect)



    if  game_state == "SETTING" and setting_menu == "ACCOUNT" and control_every_button_in_setting_on_or_off == "account":

        open_window_with_side_effect(
                screen,
                all_image.account,
                current_width // 2 + 150 ,current_height // 2 
            )
        if is_guest :
            ACC.draw_profile_account(
                screen,
                STS.gest_image_selected,
                fonts["date"],
                fonts["date"],
                fonts["date"],
                True,
                image_size=300
            )
        else:
            ACC.draw_profile_account(
                screen,
                STS.user_image_selected,
                fonts["date"],
                fonts["date"],
                fonts["date"],
                False,
                image_size=300
            )
        # MUS.reset_music_side_effect()
        # reset_side_effect_language
    if  game_state == "SETTING" and setting_menu == "SOUND" and control_every_button_in_setting_on_or_off == "sound":

        open_window_with_side_effect(
                screen,
                all_image.sound,
                current_width // 2 + 150,current_height // 2 
            )

        sound_screen(screen)























































   #این برای داشتبورد است 
    if  DASHBOARD == True and is_guest == False: 
        #-------------------
        draw_punch_image(
            screen,
            calender,
            (current_width - 215,374),
            (440, 700),
            "calender")
        
        
        DA.draw_dashboard_date(
            screen,
            DA.month_images,
            fonts["month"],
            fonts["month"],
            fonts["month_real"],
            fonts["date"]
        )
        # # if IS_ONLINE == True:
        # #     CLOCK.clock_ONLINE(screen,fonts["date"],current_width)
        # # else:
        # #     CLOCK.clock_OFFLINE(screen,fonts["date"],current_width)# این تابع چک. میکنه جیسون رو فقط

        sms_base(
            screen,
            sms_button_rect
        )
        
        sms_button(
            screen,
            sms_button_rect
        )

        
        draw_punch_image_1(
            screen,
            rank__,
             (current_width//2 +290, current_height // 2 - 335 ),
            (550, 550),
            "rank",0.45,
            center_image=punch_daily_for_dahsboard,
            center_image_size=(90, 90),
            text="",
            text_font=fonts["date"]
        )
        draw_punch_image_1(
            screen,
            rank__2,
            (current_width//2 -300, current_height // 2 - 335 ),
            (550, 550),
            "rank2",0.45,
            center_image=punch_rank,
            center_image_size=(90, 90),
            text="",
            text_font=fonts["date"]
        )
        

        

        
        
        popular_game.image_rects =popular_game.draw_three_images(
            screen,
            popular_game.selected_images
        )
                
                
        recent_game.image_rects =recent_game.draw_three_images_recent_game(
            screen,
            recent_game.selected_images
        )
        
        #------------------- برای پاپیلور گیم
                
        top_3___ = popular_game.get_top_3_popular_games()

        selected_images_for_popular_game = popular_game.get_popular_game_images(top_3___)

        popular_game.draw_three_images(
            screen,
            selected_images_for_popular_game
        )


        #--------------------- برای  ریسند گیم 

        selected_recent_images = (
            recent_game.get_recent_game_images()
        )

        recent_game.draw_three_images_recent_game(
            screen,
            selected_recent_images
        )

                
        
        
        

        
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



        donate_base(
            screen,
            call_button_rect
        )
        donate_button(
            screen,
            call_button_rect
        )
        
        
        
        




    if  FOUR_ICON_FOR_SCREEN == True and DASHBOARD == False :
        # call_base1(
        #     screen,
        #     support__button_rect1
        # )
        # call_support1(
        #     screen,
        #     support__button_rect1
        # )


        store_base(
            screen,
            store__button_rect1
        )
        store_button(
            screen,
            store__button_rect1
        )
        



        sms_base(
            screen,
            sms_button_rect1
        )
        sms_button(
            screen,
            sms_button_rect1
        )

        if game_state != "MENU" and game_state != "SETTING":
    
            donate_base(
                screen,
                call_button_rect1
            )
            donate_button(
                screen,
                call_button_rect1
            )
        
    #-------------------------------------------------------------------------------------- DAILY









    
    #------------comming soon
    coming_soon_notification(screen)


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
    
    mouse.draw_click_effect(screen)
    #------------------ Update ------------------
    # بروزرسانی صفحه نمایش
    pygame.display.update()
    # محدود کردن بازی به 60 فریم در ثانیه
    clock.tick(60)









# بستن pygame
pygame.quit()
# خروج کامل از برنامه
sys.exit()








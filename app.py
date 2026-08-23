import pygame
pygame.init()


# from modules.player_profile import load_profile_images,draw_profile_circle,draw_profiles,load_default_profile,draw_hue_bar1
# from modules.class_1 import *

import sys
from event_handler import handle_events
from modules.time_screen import draw_time_screen
from modules.game_engine import run_game
from modules.timer import draw_timer_bar,draw_timer_circle
# from modules.background import set_background,draw_background,update_background
# from modules.loading_screen import loading_screen1
# from modules.background_moving import draw_background
# from modules.TrueFalseMode.ImageLoader import draw_images
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

from modules.design import *

from modules.LEVELS.LEVELS import *
from modules.STATES import *
from modules.DATA import *

from modules.profile import draw_profile_live_circle






from modules.MODE.find_numbers  import *
# ---------------------------------------------------------- FPS 
# برای کنترل سرعت اجرای بازی
clock = pygame.time.Clock()










# ----------------------------------------------------------- Background # ساخت پنجره برای بازی  تنطیمات  اولیه بازی 
screen = pygame.display.set_mode(
    (1920,1080),
    pygame.FULLSCREEN
)

pygame.display.set_caption("F")
current_width, current_height = screen.get_size()



#--------------------------------------------------------------
# def load_background(path, size):
#     bg = pygame.image.load(path).convert()
#     bg = pygame.transform.smoothscale(bg, size)
#     return bg




init_theme(screen)











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



##############################################  for Ceil tab

ceill = 0
ceill_entered = False
ceill_text = ""


ceill_button_rects = {}

hover_level_image = None


level_images = {

    10: pygame.image.load(
        "./asset/image/levels/1.png"
    ).convert_alpha(),

    100: pygame.image.load(
        "./asset/image/levels/2.png"
    ).convert_alpha(),

    1000: pygame.image.load(
        "./asset/image/levels/3.png"
    ).convert_alpha(),

    10000: pygame.image.load(
        "./asset/image/levels/4.png"
    ).convert_alpha(),

    100000: pygame.image.load(
        "./asset/image/levels/4.png"
    ).convert_alpha()
}


# کوچک کردن عکس‌ها

for key in level_images:

    level_images[key] = pygame.transform.smoothscale(
        level_images[key],
        (120,120)
    )
    
    
    
    
    
    


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


support_call_button_rect= pygame.Rect(
    current_width - 130,  # فاصله از راست
    current_height // 2 ,                   # فاصله از بالا
    90,
    90
)


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















































#-------------------------back ground

SCREEN_WIDTH_ = info.current_w
SCREEN_HEIGHT_ = info.current_h

WORLD_WIDTH_ = 9000
WORLD_HEIGHT_ = SCREEN_HEIGHT_

level_world_ = pygame.Surface(
    (WORLD_WIDTH_, WORLD_HEIGHT_),
    pygame.SRCALPHA
)


# ============================================================
# ORIGINAL IMAGES
# ============================================================

level_images_theme = [

    pygame.image.load(
        "./asset/image/background/1.png"
    ).convert_alpha(),

    pygame.image.load(
        "./asset/image/background/2.png"
    ).convert_alpha(),

    pygame.image.load(
        "./asset/image/background/3.png"
    ).convert_alpha(),

    pygame.image.load(
        "./asset/image/background/4.png"
    ).convert_alpha(),

    pygame.image.load(
        "./asset/image/background/5.png"
    ).convert_alpha(),

    pygame.image.load(
        "./asset/image/background/6.png"
    ).convert_alpha(),

    pygame.image.load(
        "./asset/image/background/7.png"
    ).convert_alpha(),

    pygame.image.load(
        "./asset/image/background/8.png"
    ).convert_alpha(),

    pygame.image.load(
        "./asset/image/background/9.png"
    ).convert_alpha(),

    pygame.image.load(
        "./asset/image/background/10.png"
    ).convert_alpha(),

    pygame.image.load(
        "./asset/image/background/11.png"
    ).convert_alpha(),

]


# ============================================================
# THEME POSITIONS
# ============================================================
yy=420
level_positions_theme = [

    (0, yy),
    (1500, yy),
    (3000, yy),
    (3000, yy),
    (4000, yy),
    (5000, yy),
    (6000, yy),
    (7000, yy),
    (8000, yy),
    (10000, yy),
    (110000, yy),

]


# ============================================================
# SMALL THEME IMAGES
# عکس‌های کوچک فقط برای صفحه انتخاب Theme
# ============================================================

little_theme = []


for img in level_images_theme:

    small_img = pygame.transform.smoothscale(
        img,
        (1000, 600)
    )

    little_theme.append(
        small_img
    )


# ============================================================
# PUT SMALL IMAGES INSIDE WORLD
# ============================================================

for img, pos in zip(
    little_theme,
    level_positions_theme
):

    level_world_.blit(
        img,
        pos
    )


# ============================================================
# CAMERA
# ============================================================

camera_x = 0
camera_y = 0


# ============================================================
# DRAGGING
# ============================================================

dragging = False

mouse_start_x = 0
mouse_start_y = 0


# ============================================================
# THEME RECTANGLES
# ============================================================

level_rects_for_theme = []


for index, (img, pos) in enumerate(
    zip(
        little_theme,
        level_positions_theme
    )
):

    rect = img.get_rect(
        topleft=pos
    )

    level_rects_for_theme.append(
        (index, rect)
    )



# ============================================================
# SELECTED BACKGROUND
# اینجا عکس اصلی است، نه little_theme
# ============================================================

selected_background = level_images_theme[0]


# ============================================================
# THEME DRAW
# ============================================================

def THEME_DRAW(
    screen,
    WORLD_WIDTH_,
    SCREEN_WIDTH_,
    WORLD_HEIGHT_,
    SCREEN_HEIGHT_,
    level_world_
):

    global camera_x
    global camera_y


    keys = pygame.key.get_pressed()


    if keys[pygame.K_RIGHT]:

        camera_x += 10


    if keys[pygame.K_LEFT]:

        camera_x -= 10


    if keys[pygame.K_DOWN]:

        camera_y += 10


    if keys[pygame.K_UP]:

        camera_y -= 10


    # ========================================================
    # CAMERA LIMIT X
    # ========================================================

    camera_x = max(
        0,
        min(
            camera_x,
            WORLD_WIDTH_ - SCREEN_WIDTH_
        )
    )


    # ========================================================
    # CAMERA LIMIT Y
    # ========================================================

    camera_y = max(
        0,
        min(
            camera_y,
            WORLD_HEIGHT_ - SCREEN_HEIGHT_
        )
    )


    # ========================================================
    # DRAW WORLD
    # ========================================================

    screen.blit(
        level_world_,
        (0, 0),
        (
            camera_x,
            camera_y,
            SCREEN_WIDTH_,
            SCREEN_HEIGHT_
        )
    )


# ============================================================
# DRAW SELECTED BACKGROUND
# ============================================================

def draw__background(screen):

    global selected_background


    # ========================================================
    # ORIGINAL IMAGE SIZE
    # ========================================================

    image_width = selected_background.get_width()
    image_height = selected_background.get_height()


    # ========================================================
    # SCALE
    # نسبت تصویر حفظ می‌شود
    # ========================================================

    scale_x = SCREEN_WIDTH_ / image_width
    scale_y = SCREEN_HEIGHT_ / image_height

    scale = max(
        scale_x,
        scale_y
    )


    new_width = int(
        image_width * scale
    )

    new_height = int(
        image_height * scale
    )


    # ========================================================
    # SCALE ORIGINAL IMAGE
    # ========================================================

    background = pygame.transform.smoothscale(
        selected_background,
        (
            new_width,
            new_height
        )
    )


    # ========================================================
    # CENTER
    # ========================================================

    x = (
        SCREEN_WIDTH_ - new_width
    ) // 2

    y = (
        SCREEN_HEIGHT_ - new_height
    ) // 2 


    # ========================================================
    # DRAW
    # ========================================================

    screen.blit(
        background,
        (
            x,
            y
        )
    )
    
    
    
    
    
    
    
    
    
    
    
    #----------------------------------------------------------------
clock = pygame.time.Clock()

fps_font = pygame.font.Font(None, 35)
    #----------------------------------------------------------------





# این برای فلگ است 
show_flag = True
#----------------------------------







imm=pygame.image.load("./asset/image/background/1.png")
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

#############################################################################################################
#############################################################################################################
game_state = "?+?"
# ############################################################################################################
#############################################################################################################
# Game loop ------------------------------------------------------------------------------------------------------------------------------------

while running:



    # ---------------------------------------------background
    screen.blit(imm,(0,0))

    # draw__background(screen)
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
        level_rects_for_theme,
        
        
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
        selected_background
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
        level_rects_for_theme,
        level_images_theme,
        
        
        
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
        selected_background
        )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #---------------------------------------------------------------------------------NAME
    if game_state == "NAME":    
            
        if defult_language == True:
            load_language("en")
            defult_language=False
            
            
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
            
            
            
        draw_name_screen(
            screen,
            fonts,
            player_name,
            input_box,
            enter_button
        )
        

        draw_profiles(
            screen,
            profile_images,
            profile_rects,
            profile_area
        )
        
        draw_profile_circle(
            screen,
            selected_image,
            (
                current_width // 2,
                100
            ),
        )
        
        



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
                        # عکس دایره. برای پروفایل هر صفحه
        image_setter(screen,pathth,current_width//2 - 220,current_height//2 - 666)
        gif_setting(screen,gif_frames_lan,current_width // 2 - 246 // 2,current_height // 2 - 1068     // 2)
        

        draw_back_button(
            screen,
            back_button_rect)
        support_button(
            screen,
            support_button_rect
        )      
        

    #---------------------------------------------------------------------------------THEME

    # #---------------------------------------------------------------------------------THEME
    # if game_state == "SUPPORT":
    #                     # عکس دایره. برای پروفایل هر صفحه
    #     image_setter(screen,pathth,400,400,current_width//2 - 220,current_height//2 - 666)
    #     gif_setting(screen,gif_frames_support,current_width // 2 - 246 // 2,current_height // 2 - 1068     // 2)
    #     draw_back_button(
    #         screen,
    #         back_button_rect)
    #     support_button(
    #         screen,
    #         support_button_rect
    #     )   
    #---------------------------------------------------------------------------------about
    if game_state == "ABOUT":
        
        draw_about(
            screen,
            current_width,
            current_height,
            about,
            fonts["answer"],
            fonts["about"]
        )


        draw_back_button(
            screen,
            back_button_rect)
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
        image_setter(screen,pathth,current_width//2 - 220,current_height//2 - 666)
        gif_setting(screen,gif_frames_about,current_width // 2 - 246 // 2,current_height // 2 - 1068     // 2)

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
        image_setter(screen,pathth,current_width//2 - 220,current_height//2 - 666)
        gif_setting(screen,gif_frames_sound,current_width // 2 - 246 // 2,current_height // 2 - 1068     // 2)



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
    if game_state == "THEME":
        

                        # عکس دایره. برای پروفایل هر صفحه
        image_setter(screen,pathth,current_width//2 - 220,current_height//2 - 666)

        gif_setting(screen,gif_frames_theme,current_width // 2 - 246 // 2,current_height // 2 - 1068     // 2)

        draw_back_button(
            screen,
            back_button_rect)
        support_button(
            screen,
            support_button_rect
        )      
        # draw_theme(screen)

        # draw_theme(screen, 450, 300)
        THEME_DRAW(screen,WORLD_WIDTH_,SCREEN_WIDTH_,WORLD_HEIGHT_,SCREEN_HEIGHT_,level_world_)
        
        
        
        
        
        
        



            #   برای اضافه کردن سقف  اعداد
            
    if game_state == "CEILL":        
        
        

        draw_new_screen(screen)
        

        _window(screen,small_window)



        draw_ceill_screen(
            screen,
            fonts,
            ceill_button_rects,
            current_width,
            current_height,
            level_images
        )
            
                 
        draw_back_button(
            screen,
            back_button_rect
        )
        
        
        support_button(
            screen,
            support_button_rect
        )
        


        gif_setting(screen,gif_frames_credit,current_width // 2 - 250 // 2,current_height // 2 - 1085     // 2)
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
    if game_state == "PROFILE":
        

        
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
        image_setter(screen,pathth,current_width//2 - 220,current_height//2 - 666)
        gif_setting(screen,gif_frames_profile,current_width // 2 - 246 // 2,current_height // 2 - 1068     // 2)


















#-------------------------------------------------------------



    if game_state == "MUSIC":
        draw_music(
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
        image_setter(screen,pathth,current_width//2 - 220,current_height//2 - 666)
        gif_setting(screen,gif_frames_music,current_width // 2 - 246 // 2,current_height // 2 - 1068     // 2)







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

        gif_setting(screen,gif_frames,current_width // 2 - 250 // 2,current_height // 2 - 1085 // 2)
        
        draw_profile_live_circle(
            screen,
            selected_profile_image,
            p99,
            current_width
        )
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    #---------------------------------------------------------------------------------TrueFalse
    if game_state == "?+?":
        












        # ---------------- Timer ----------------

        elapsed = (
            pygame.time.get_ticks() - start_time
        ) / 1000


        # ---------------- Timer Circle ----------------

        progress = 1 - (
            elapsed / current_question["time"]
        )

        progress = max(0, min(1, progress))


        draw_timer_circle(
            screen,
            # (current_width //2 , current_height //2 + 260),   # مرکز دایره
            (current_width //2 , current_height //2 + 365),   # مرکز دایره
            90,                            # شعاع ثابت
            progress
        )








        # ---------------- Question Background ----------------

        image_setter(
            screen,
            image_back_quastion,
            current_width // 2 - 600,
            current_height // 2 - 550
        )

        # print(image_back_quastion.get_size())


















        # ---------------- Hint ----------------

        hint(screen)


        # ---------------- Save ----------------

        save(screen)


        # ---------------- Question ----------------

        option_rects = draw_question(
            screen,
            fonts,
            current_question,
            current_width,
            current_height
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






























        if elapsed >= current_question["time"]:

            wrong_count += 1


            question_number += 1


            current_question = generate_missing_number_question(
                question_number
            )


            start_time = pygame.time.get_ticks()



        correct_text = fonts["name"].render(
            f"Correct: {correct_count}",
            True,
            (0,255,0)
        )


        
        wrong_text = fonts["name"].render(
            f"Wrong: {wrong_count}",
            True,
            (255,0,0)
        )
        



        screen.blit(
            correct_text,
            (50,50)
        )


        screen.blit(
            wrong_text,
            (300,50)
        )

        
        
        
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










        in_game_alarm(screen)   

        move_flage(screen,current_width//2- 154,show_flag) 
    #---------------------------------------------------------------------------------x?y
    if game_state == "60s":
        
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
    #---------------------------------------------------------------------------------60s
    if game_state == "fast":

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
    #---------------------------------------------------------------------------------x(+-/*)y
    if game_state == "more_less_equal":

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
    #--------------------------------------------------------------------------------->=<
    if game_state == "TrueFalse":

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
    #--------------------------------------------------------------------------------->=<
    if game_state == "y?x":

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
    #--------------------------------------------------------------------------------->=<

























    #--------------------------------------------------------------------------------->=<

    if game_state == "SHARE":

        draw_profile_live_circle(
            screen,
            selected_profile_image,
            p99,
            current_width
        )

        _window(screen,small_window)


    if game_state == "ASK US":

        draw_profile_live_circle(
            screen,
            selected_profile_image,
            p99,
            current_width
        )
        _window(screen,small_window)


















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
        image_setter(screen,pathth_,current_width//2 - 220,current_height//2 - 666)
        gif_setting(screen,gif_frames_levels,current_width // 2 - 210 // 2,current_height // 2 - 1000     // 2)

        draw_profile_live_circle(
            screen,
            selected_profile_image,
            p99,
            current_width
        )
    #---------------------------------------------------------------------------------GAME ---> PLAY
    if  game_state == "CUSTOM GAME":








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








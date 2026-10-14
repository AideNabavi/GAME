import pygame
import importlib
from modules import mouse

pygame.init()
from modules.font import *
from modules.loading import *

# ==================================================
# Loading Window
# ==================================================

screen = pygame.display.set_mode(
    (1920, 1080),
    pygame.FULLSCREEN
)

pygame.display.set_caption("PeakyJoy")

# تصویر اولیه
loading_image = pygame.image.load(
    "asset/image/loadd.png"
).convert_alpha()

loading_image = pygame.transform.smoothscale(
    loading_image,
    (1920, 1080)
)

screen.blit(
    loading_image,
    (0, 0)
)

pygame.display.flip()

# یک فرصت کوتاه برای اینکه Fullscreen واقعاً فعال شود
pygame.event.pump()
pygame.time.delay(100)

icon = pygame.image.load(
    "asset/image/icon.png"
).convert_alpha()

pygame.display.set_icon(icon)



#loading for loading window
LOADING(screen,fonts["loading"])


mouse.set_game_cursor()


# ==================================================
# Start Loading
# ==================================================
pygame.mixer.init()

pygame.mixer.music.play()
pygame.mixer.music.stop()


# screen = pygame.display.set_mode(
#     (1920, 1080),
#     pygame.FULLSCREEN
# )


pygame.display.set_caption(
    "Fast Mathter"
)

pygame.display.set_icon(
    icon
)

# ---------------------------------------------------------- متغیر های حیاتی 
clock = pygame.time.Clock()
info = pygame.display.Info()
current_width, current_height = screen.get_size()
input_y = current_height // 2 + 100
WIDTH, HEIGHT = current_width , current_height
dt = clock.tick(60) / 1000


#########################################################################################################
#########################################################################################################
#########################################         IMPORT        ##################################################
#########################################################################################################
#########################################################################################################
import sys
from modules.RECT import rec
from modules.RECT import game_mode as game_mode_face
from modules.RECT import menu_rec 
from modules import how_to_play
from modules.RECT import rec_window
from event_handler import handle_events
from modules.time_screen import draw_time_screen
from modules.game_engine import run_game
from modules import button
from modules.RECT import rec_support
from modules import design
from modules import language
from modules.RECT import game_mode_rec
from modules import menu
from modules.RECT import corner
from modules.RECT import score_xp
from modules import sound
from modules.RECT import rect_window
from modules import screen as screen_
from modules import ceill_screen
from modules.IN_GAME import menu_window
from modules.SUPPORT  import support 
from modules.MORE import more 
from modules.DAILY import status 
from modules.MORE import more 
from modules.ACCOUNT import  profile_
from modules import music
from modules import game_overview
from modules import operation_screen
from modules.ACCOUNT import account 
from modules import before_game
from modules.EFFECT import popi as pop
from modules import game_list
from modules.SUPPORT import report_bug
from modules.SAVE import save 
from modules.SAVE import popular_game 
from modules.SAVE import recent_game 
from modules import custom_math
from modules.MORE import FAQ 
from modules import mode as MODE
from modules.DAILY import progress as progress_
from modules.DAILY import achievement
from modules.SAVE.save import load_player
from modules.SUPPORT import  contact_us 
from modules.SUPPORT import feedback 
from modules.GAMES.FIND_NUMBER import option_rects,current_question,correct_count, wrong_count , question_number
from modules.background_moving import draw_moving_map
from modules.IN_GAME import difficulty_selection_menu
from modules import coming_soon
from modules.MORE import policy 
from modules import image as all_image 
from modules.start_game import countdown
from modules import exit
from modules.before_game import guid_sild_effect
from modules.SUPPORT import donate
from modules import button_menu_setting_gamemode as menu_setting_mode
from modules import start_screen
from modules.EFFECT import side_effect_window 
from modules.MORE import INFO
from modules import game_mode_scroll 
from modules.MORE import policy
from modules import droping
from modules.ACCOUNT import player_profile 
# from modules.ACCOUNT import country as  CON
from modules.IN_GAME import utils

from modules.state import *

from modules.GAMES import ACTION 
from modules.GAMES import DIRECTION
from modules.GAMES import FAST_ADD_SUB 
from modules.GAMES import MIRROR
from modules.GAMES  import THOOZ 
from modules.GAMES import HARD 
from modules.GAMES import DETECT_PRO 
from modules.GAMES import FOLLOW_THAT 
from modules.GAMES import MEMORY_GO 
from modules.GAMES import MOVE_ARROW 
from modules.GAMES import MATH_GO 
from modules.GAMES import SUDOKU 
from modules.GAMES import WORD 
from modules.GAMES import MAZE 
from modules.GAMES import SHAPE_COLOR_NAME
from modules.GAMES import MATCH3  
from modules.GAMES import SNAKE  
from modules.GAMES import CONNECT_FOUR 
from modules.GAMES import UNBLOCK_CAR 
from modules.GAMES import MEMORY_HARD 
from modules.GAMES import PUZZLE
from modules.GAMES import GO
from modules.GAMES import DOTS_BOX
from modules.GAMES import CHECKERS
from modules.GAMES import FOLLOW_FREE
from modules.GAMES import MEMORY
from modules.GAMES import CHESS
from modules.GAMES import CHOOSE_IMAGE
from modules.GAMES import SORT_NUMBER
from modules.GAMES import MINESWEEPER
from modules.GAMES import IMAGE_SELECT 
from modules.GAMES import FIND_NUMBER  
from modules.GAMES import MEMORY  
from modules.GAMES import REPEAT_AFTER_ME  
from modules.GAMES import MORE_LESS_EQUAL  
from modules.GAMES import DETECT
from modules.GAMES import FAST
from modules.GAMES import SIX_60S
from modules.GAMES import TRUE_FALSE
from modules.GAMES import FIND_OPERATOR
from modules.GAMES import THOOZ
from modules.GAMES import HOW_MANY

from modules.GAMES import SPIN_HIT
from modules.GAMES import MERGE_2048
from modules.GAMES import BREAKOUT
from modules.GAMES import DINO_RUN
from modules.GAMES import COLOR_RUSH
from modules.GAMES import FLAPPY_BIRD
from modules.GAMES import TOW_CARS
from modules.GAMES import SPEED_TYPE
from modules.GAMES import PACMAN
from modules.GAMES import NUMBER_DETECT
from modules.GAMES import BALL_TRACKER


#########################################################################################################
#########################################################################################################
#########################################         IMAGE        ###################################################
#########################################################################################################
#########################################################################################################


profile_for_back = pygame.image.load("./asset/image/all_window/all.png").convert_alpha()




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








about =pygame.transform.smoothscale(pygame.image.load(
    "./asset/image/me.png"
).convert_alpha(),(200,200))





background_for_account_music_sound_language = pygame.transform.smoothscale(pygame.image.load(
    "./asset/image/all_window/all.png"
).convert_alpha(),(1550,1100))



imm=pygame.image.load("./asset/image/background/FIND_OPERATOR_BACKGROUND.png")
imm = pygame.transform.scale(
    imm,
    screen.get_size()
)





recent_game.load_recent_images(
    "./asset/image/MODE"
)
popular_game.load_popular_images(
    "./asset/image/MODE"
)



music_profile_image = pygame.image.load(
    "./asset/image/music/music.png"
).convert_alpha()






image_back_quastion = pygame.image.load(
    "./asset/image/in_game/back_image.png"
).convert_alpha()

image_back_quastion = pygame.transform.smoothscale(
    image_back_quastion,
    (1200, 650)
)





gamemode_panel = pygame.transform.smoothscale(
    pygame.image.load("./asset/image/panel/gamemode.png").convert_alpha(),
    (300, 930)
)

menu_panel = pygame.transform.smoothscale(
    pygame.image.load("./asset/image/panel/menu.png").convert_alpha(),
    (500, 1358)
)
setting_panel = pygame.transform.smoothscale(
    pygame.image.load("./asset/image/panel/setting.png").convert_alpha(),
    (480, 1315)
)




recent_game.load_recent_images(
    "./asset/image/MODE"
)

flag_in_menu= pygame.transform.smoothscale(pygame.image.load("./asset/image/in_game/flaginthegame.png").convert_alpha(),(800,400))


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


#########################################################################################################
#########################################################################################################
#########################################         LUNCH        ###################################################
#########################################################################################################
#########################################################################################################

# برای چهار تا پنجره ساپورت است








blur_surface = rec_window.create_blur_surface(screen, blur=3, alpha=0)
############################################## این برای دکمه یها ساپورت است گرفتن رک برای اون ۴ تا 
custom_math.current_width_current_height(current_width,current_height)
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






default_profile = player_profile.load_default_profile()










# تبدیل به فرمت مناسب
about = about.convert()








back_image=screen_.back_image.convert_alpha()
profile_images =player_profile.load_profile_images()
# عکس انتخاب شده اولیه
selected_image = player_profile.load_default_profile()
profile_images = player_profile.load_profile_images()





popular_game.load_popular_games()
recent_game.load_recent_games()



donate.load_donate_images()


menu_hidden_rect = pygame.Rect(
    25,
    current_height// 2 - 550,
    600,
    1250
)

progress_area = pygame.Rect(
    250,
    250,
    screen.get_width() - 500,
    800
)
achievement_area = pygame.Rect(
    250,
    250,
    screen.get_width() - 500,
    800
)


input_box = pygame.Rect(
    0,
    0,
    500,
    80
)



profile_area = pygame.Rect(
    100,
    250,
    550,
    220
)


enter_button = pygame.Rect(
    current_width // 2 - 75,
    input_y + 130,
    150,
    55
)


info_box = pygame.Rect(
    current_width // 2 - 370,
    current_height // 2 - 100,
    740,
    550
)


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


support_button_rect = pygame.Rect(
    30,  # فاصله از راست
    current_height + 177,                   # فاصله از بالا
    150,
    150
)


#donate
call_button_rect= pygame.Rect(
    50,  # فاصله از راست
    70,                   # فاصله از بالا
    150,
    150
)

#support
support__button_rect= pygame.Rect(
    1880,  # فاصله از راست
    current_height  - 370,                   # فاصله از بالا
    150,
    150
)

store__button_rect= pygame.Rect(
    1880,  # فاصله از راست
    1050,                   # فاصله از بالا
    150,
    150
)
sms_button_rect= pygame.Rect(
    1880,  # فاصله از راست
    40,                   # فاصله از بالا
    150,
    150
)


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



# country = CON.load_flags()


SHAPE_COLOR_NAME.one____(screen,current_width,current_height)

before_game.backgorund_now_for_any_game_mode  = pygame.image.load("./asset/image/GAME/THOOZ/THOOZ.png")


recent_game.load_recent_games()
#--------------- برای انتخاب عکس ریسندگیم است
recent_game.selected_images = recent_game.choose_three_random_images()
#--------------- برای انتخاب عکس پاپیولر گیم است
popular_game.selected_images = popular_game.choose_three_random_images()

game_mode_face.WIDTH_HEIGHT_gettter(screen, WIDTH, HEIGHT)
BREAKOUT.WIDTH_HEIGHT_gettter(screen, WIDTH, HEIGHT)
SPIN_HIT.WIDTH_HEIGHT_gettter(screen, WIDTH, HEIGHT)
MERGE_2048.WIDTH_HEIGHT_gettter(screen, WIDTH, HEIGHT)
DINO_RUN.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
COLOR_RUSH.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
FLAPPY_BIRD.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
TOW_CARS.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
PACMAN.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
SPEED_TYPE.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
BALL_TRACKER.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
NUMBER_DETECT.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
utils.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
language.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
SORT_NUMBER.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
SUDOKU.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
HOW_MANY.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
WORD.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
MINESWEEPER.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
MAZE.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
CHOOSE_IMAGE.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
MATCH3.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
CONNECT_FOUR.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
CHESS.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
MOVE_ARROW.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
DETECT_PRO.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
SNAKE.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
UNBLOCK_CAR.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
GO.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
DOTS_BOX.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
PUZZLE.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
CHECKERS.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
FOLLOW_FREE.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
MEMORY_GO.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
MEMORY.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
FOLLOW_THAT.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
THOOZ.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
MEMORY_HARD.WIDTH_HEIGHT_gettter(screen,current_width,current_height)
DIRECTION.WIDTH_HEIGHT_gettter(screen,current_width,current_height)

before_game.loader_image_for_before_game(before_game.count_down_image[39],MODE.fast,"online","online","online","easy")
policy.now_language_is_this = "en"

player = load_player()
saved_player = save.load_player()


if saved_player is not None:
    game_state = "GAME MODE"#start
    game_mode_feature = "math"
    DASHBOARD=False

else:

    game_state = "NAME"#name
    DASHBOARD=False



# SKY_BLUE = (198, 242, 255)# بک گراند 
# SKY_BLUE = (20, 201, 255)# دکمه
SKY_BLUE = (255, 135, 40)# بک گراند 
# SKY_BLUE = (255, 135, 40)# دکمه



# این برای پیدا صفه ها است 
punch_frames = rect_window.create_punch_frames(
    width=1200,
    height=900,
    color=(255, 255, 255),
    radius=50,
    scale=2,
    frame_count=30,
    start_scale=0.65,
    overshoot=1.12
)

#############################       ######################################
############################        ######################################
#########################          #######################################
######################            ########################################
###################              #########################################
################                ##########################################
#############                  ###########################################
#########                    #############################################
#####                      ################################################
##                     ###################################################
#-------------------- LOOP ------------------------------------------------
##                     ###################################################
#####                      ################################################
#########                    #############################################
#############                  ###########################################
################                ##########################################
###################              #########################################
######################            ########################################
#########################          #######################################
############################        ######################################
#############################       ######################################

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
        time_limit,
        time_text,
        time_entered,
        answer_selected,
        game_state,
        select_buttons,
        back_button_rect,
        small_window,
        clicked_button,
        language_rects,
        profile_.selected_profile_image,
        dragging,
        option_rects,
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
        THREE_ICONS,
        DONT_LET_CLICK_GAMES_BUTTON_BEFORE_THAT,
        game_mode_feature,
        buy_premium,
        in_game_is_menu_on,
        stop_loop

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
        time_limit,
        time_text,
        time_entered,
        time_button_rects,
        answer_rects,
        answer_selected,
        game_state,
        select_buttons,
        back_button_rect,
        small_window,
        clicked_button,
        language.language_rects,
        profile_.selected_profile_image,
        dragging,
        option_rects,
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
        THREE_ICONS,
        DONT_LET_CLICK_GAMES_BUTTON_BEFORE_THAT,
        game_mode_feature,
        buy_premium,
        in_game_is_menu_on,
        stop_loop,
        menu_hidden_rect

    )
    
    


    
##########################################################################
#------------------ NAME
##########################################################################
    if game_state == "NAME":    
          
        # for background  flying and image 
        draw_moving_map(
            screen,
            WIDTH,
            HEIGHT,
            dt    )
        droping.draw_flying_birds(
            screen,
            current_width,
            current_height
        )   
    
    
        custom_math.draw_punch_image(
            screen,
            profile_for_back,
            (current_width//2  , current_height // 2 ),
            (2000, 1300),
            "DAILY_GAME1"
        )
    
    
    
        # این برای ران کردن دیفالت زبان انگلیسی  در اول بازی است 
        if defult_language == True:
            language.load_language("en")
            defult_language=False
            
            
            
        # این برای  صفحه اول بازی هستن 
        if selected_profile is None:
            player_profile.draw_profile_circle(
                screen,
                default_profile,
                (current_width//2, 200),
                250
            )
        else:
            player_profile.draw_profile_circle(
                screen,
                selected_image,
                (current_width//2, 200),
                250
            )    
            
            
            
        #--------------- name screen
        screen_.draw_name_screen(
            screen,
            fonts,
            player_profile.player_name,
            player_profile.input_box,
            enter_button
        )

        player_profile.draw_email_screen(
            screen,
            fonts,
            player_profile.player_email
        )
            

        player_profile.draw_profiles(
            screen,
            profile_images,
            profile_rects,
            profile_area
        )
        
        
        
        #------------------------------ حذف نشود
        # draw_profile_circle(
        #     screen,
        #     selected_image,
        #     (
        #         current_width // 2 - 300,
        #         500
        #     ),
        # )
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





##########################################################################
#------------------ MENU
##########################################################################
    if game_state == "MENU" or menu_state == "MENU":# DASH BOARDاین همون داشبود است 
        draw_moving_map(
            screen,
            WIDTH,
            HEIGHT,    )

        # screen.blit(rec.menu_card_over, (-120, current_height // 2 - 800))# این ها فیس اند میخام این ها حرکت
        # screen.blit(rec.icon_menu, (193,10))






        # menu.scroll_y += (
        #     menu.target_scroll_y - menu.scroll_y
        # ) * 0.03
        # menu.draw_six_scroll_items(
        #     screen,
        #     menu.images,
        #     menu.names,
        #     menu_hidden_rect,
        #     image_count=7,
        #     mode="menu",
        #     item_height=340,
        #     scroll_y=menu.scroll_y,
        #     font=fonts["date"]
        # )
        
        menu_rec.side_scroll_effect(
            screen,

            rects=menu_rec.rects,

            images=menu_rec.images,
            texts=menu_rec.names,

            # محل مشترک عکس‌ها
            list_x=238,
            list_y=250,
            item_spacing=300,

            text_font=fonts["date"],
            text_color=(255, 135, 40),
            text_gap=30,

            # کارت اصلی
            surface=menu_rec.right_card_center,
            surface_x=240,
            surface_y=current_height // 2,
            surface_height=1300,

            # عکس پروفایل در مرکز rects[0]
            image=menu_rec.profile,

            # اسم زیر rects[0]
            text="aiden",
            text_font_single=fonts["date"],
            text_color_single=(255, 135, 40),
            text_gap_below=10,

            duration=1200,
            scroll_smoothness=0.18,
            mode="menu"
        )
        
     
        
        
        
        
        
        
        

    ##########################################################################
    #------------------ PROGRESS
    ##########################################################################
    if (game_state == "MENU" or game_state == "SETTING") and menu_state == "PROGRESS":
        # screen.blit(blur_surface, (0, 0))
        rec_window.draw_dark_overlay(screen, alpha=130)
        rec_window.draw_slide_rect(
            screen,
            rec_window.PROGRESS,
            target_x=screen.get_width() - rec_window.PROGRESS.get_width() - (-450),
            target_y=current_height // 2 - 660,
            mode=3,
            duration=1,
            state=rec_window.PROGRESS_state
        )
        # rec_window.draw_slide_rect(
        #         screen,
        #         rec_window.PROGRESS,
        #         target_x=-450,
        #         target_y=current_height // 2 - 660,
        #         mode=2,
        #         duration=1,
        #         state=rec_window.PROGRESS_state
        #     )

        progress_.draw_carousel(
                screen,
                game_list.gamemode_icons,
                960,
                100
            )

        screen_.draw_back_button(
            screen,
            back_button_rect)
        
        if menu_state == "math_progress":
            support.open_window_with_side_effect(
                screen,
                support.daily_window,
                current_width // 2,
                current_height //2
            )
            

            progress_.draw_progress(
                screen,
                game_list.game_progress_math,
                fonts["date"],
                progress_.progress_scroll_y,
                progress_area
            )
            

                    
        if menu_state == "logic_progress":
            support.open_window_with_side_effect(
                screen,
                support.daily_window,
                current_width // 2,
                current_height //2
            )
        if menu_state == "memory_progress":
            support.open_window_with_side_effect(
                screen,
                support.daily_window,
                current_width // 2,
                current_height //2
            )
        if menu_state == "detection_progress":
            support.open_window_with_side_effect(
                screen,
                support.daily_window,
                current_width // 2,
                current_height //2
            )
        if menu_state == "fast_progress":
            support.open_window_with_side_effect(
                screen,
                support.daily_window,
                current_width // 2,
                current_height //2
            )
        if menu_state == "entertainment_progress":
            support.open_window_with_side_effect(
                screen,
                support.daily_window,
                current_width // 2,
                current_height //2
            )
                



##########################################################################
#------------------ SUPPORT
##########################################################################
    if menu_state == "SUPPORT":

        # # draw_4_images_SUPPORT(screen)
        # custom_math.draw_punch_image2(
        #     screen,
        #     custom_math.new_window_for_more_support,
        #     custom_math.positions_____1[0],
        #     (500, 500),#      (400, 400)
        #     "SUPPORT1",
        #     center_image=support.images_support[0],
        #     center_image_size=(300, 300),
        #     text="contact_us",
        #     text_font=fonts["date"]
        # )
        
        # custom_math.draw_punch_image2(
        #     screen,
        #     custom_math.new_window_for_more_support,
        #     custom_math.positions_____1[1],
        #     (500, 500),#      (400, 400)
        #     "SUPPORT2",
        #     center_image=support.images_support[1],
        #     center_image_size=(300, 300),
        #     text="feedback",
        #     text_font=fonts["date"]
        # )
        # custom_math.draw_punch_image2(
        #     screen,
        #     custom_math.new_window_for_more_support,
        #     custom_math.positions_____1[2],
        #     (500, 500),#      (400, 400)
        #     "SUPPORT3",
        #     center_image=support.images_support[2],
        #     center_image_size=(300, 300),
        #     text="donate",
        #     text_font=fonts["date"]
        # )
        # custom_math.draw_punch_image2(
        #     screen,
        #     custom_math.new_window_for_more_support,
        #     custom_math.positions_____1[3],
        #     (500, 500),#      (400, 400)
        #     "SUPPORT4",
        #     center_image=support.images_support[3],
        #     center_image_size=(300, 300),
        #     text="report_bug",
        #     text_font=fonts["date"]
        # )
                

        rec_support.res_support(
            screen,
            rec_support.scroll_y
        )

        # اسکرول نرم
        rec_support.scroll_y += (
            rec_support.target_scroll_y - rec_support.scroll_y
        ) * 0.15
##########################################################################
#------------------ Contact Us
##########################################################################
 
    if game_state == "Contact Us":
        #----------------- background_and_brids

        droping.draw_flying_birds(
            screen,
            current_width,
            current_height
        )   
        
        side_effect_window.open_window_with_side_effect_MULLTI_WINDOW(
            screen,
            all_image.contact,
            current_width // 2,
            current_height // 2,
            )

        
        contact_us.draw_social_links(
            screen,
            contact_us.images,
            contact_us.urls,
            current_x=500,
            current_y=900
        )

        contact_us.draw_contact_form(
            screen,
            fonts["date"],
            current_x=900,
            current_y=400
        )
                
        
        
        
        
        
        screen_.draw_back_button(
            screen,
            back_button_rect)

        
        
        
        
##########################################################################
#------------------ Feed Back
##########################################################################
    if game_state == "Feed Back":
        draw_moving_map(
            screen,
            WIDTH,
            HEIGHT,
            dt    )
        droping.draw_flying_birds(
            screen,
            current_width,
            current_height
        )
        support.open_window_with_side_effect(
            screen,
            all_image.feed,
            current_width // 2 ,current_height // 2 
        )  
        side_effect_window.open_window_with_side_effect_MULLTI_WINDOW(
            screen,
            all_image.feed,
            current_width // 2,
            current_height // 2,
)
        feedback_star_rects = feedback.draw_contact_form(
            screen,
            fonts["date"]
        )

        screen_.draw_back_button(
            screen,
            back_button_rect)
        
        
        
        
##########################################################################
#------------------ Donate
##########################################################################
    if game_state == "Donate":
        draw_moving_map(
            screen,
            WIDTH,
            HEIGHT,
            dt    )
        droping.draw_flying_birds(
            screen,
            current_width,
            current_height
        )   
        

        side_effect_window.open_window_with_side_effect_MULLTI_WINDOW(
            screen,
            all_image.donate,
            current_width // 2,
            current_height // 2,
            )

        donate.draw_donate(
            screen,
            fonts["date"]
        )
        screen_.draw_back_button(
            screen,
            back_button_rect)
        
        
        
        
##########################################################################
#------------------ Report Bug
##########################################################################
    if game_state == "Report Bug":
        draw_moving_map(
            screen,
            WIDTH,
            HEIGHT,
            dt    )
        droping.draw_flying_birds(
            screen,
            current_width,
            current_height
        )   
        side_effect_window.open_window_with_side_effect_MULLTI_WINDOW(
            screen,
            all_image.bug,
            current_width // 2,
            current_height // 2,
            )


        report_bug.draw_report_bug(
            screen,
            fonts["date"]
        )
        screen_.draw_back_button(
            screen,
            back_button_rect)




##########################################################################
#------------------ START
##########################################################################

    if game_state == "START":
        draw_moving_map(
            screen,
            WIDTH,
            HEIGHT,
            dt    )
        droping.draw_flying_birds(
            screen,
            current_width,
            current_height
        )   
        
 
        start_screen.start_profile_rect, start_screen.start_guest_rect = start_screen.draw_start_profile(
            screen,
            profile_images,
            selected_profile,
            player_profile.player_name,
            current_width // 2,
            current_height // 2,
            start_screen.profile_center_image,
            start_screen.guest_center_image
        )
    
    
    
    
##########################################################################
#------------------ EXIT
##########################################################################
    if game_state == "MENU" and menu_state == "EXIT":
        exit.draw_exit_confirmation(screen)
        
        
        
        
        
        
##########################################################################
#------------------ GAMES_OR_MATH
##########################################################################
    if game_state == "MENU" and menu_state == "GAMES_OR_MATH":
        custom_math.draw_punch_image2(
            screen,
            custom_math.punch_1,
            (current_width//2 - 375 + 300, current_height // 2 ),
            (600, 600),
            "GAME_MODE",
            center_image=custom_math.punch_1_1,
            center_image_size=(300, 300),
            text="game_mode",
            text_font=fonts["date"]
        )

        custom_math.draw_punch_image2(
            screen,
            custom_math.punch_1,
            (current_width//2 - 375 + 1000, current_height // 2),
            (600, 600),
            "MATH",
            center_image=custom_math.punch_2_1,
            center_image_size=(300, 300),
            text="custom_math",
            text_font=fonts["date"]
        )
        
        
        
        
##########################################################################
#------------------ DAILYGAME_STATUS_PROGRESS_ACHIEVEMENT
##########################################################################
        
    if game_state == "MENU" and menu_state == "DAILYGAME_STATUS_PROGRESS_ACHIEVEMENT":
        
                #---- دو عکس چاپ میکنه 
        custom_math.draw_punch_image_1(
            screen,
            custom_math.IMG1,
            (current_width//2 - 375 + 130, current_height // 2  ),
            (700, 1050),
            "DAILY_GAME1",0.351,
            center_image=custom_math.punch_daily,
            center_image_size=(150, 150),
            text="today_workout",
            text_font=fonts["date"]
        )
        
        
        #---- دو عکس چاپ میکنه 
        custom_math.draw_punch_image_1(
            screen,
            custom_math.IMG2,
            (current_width//2 - 375 + 830, current_height // 2 - 400  ),
            (400, 400),
            "DAILY_GAME2",0.351,
            center_image=custom_math.punch_status,
            center_image_size=(150, 150),
            text="status",
            text_font=fonts["date"],
            )

        custom_math.draw_punch_image_1(
            screen,
            custom_math.IMG2,
            (current_width//2 - 375 + 830, current_height // 2  ),
            (400, 400),
            "DAILY_GAME3",0.351,
            center_image=custom_math.punch_status,
            center_image_size=(150, 150),
            text="progress",
            text_font=fonts["date"]
        )
        custom_math.draw_punch_image_1(
            screen,
            custom_math.IMG2,
            (current_width//2 - 375 + 830, current_height // 2 + 400 ),
            (400, 400),
            "DAILY_GAME4",0.351,
            center_image=custom_math.punch_status,
            center_image_size=(150, 150),
            text="Achievements",
            text_font=fonts["date"]
        )
        


##########################################################################
#------------------ DAILY GAME
##########################################################################

    if game_state == "DAILY GAME":


        draw_moving_map(
            screen,
            WIDTH,
            HEIGHT,
            dt
        )

        droping.draw_flying_birds(
            screen,
            current_width,
            current_height
        )


        if DAILY_BUTTON == "page_1":
            support.open_window_with_side_effect(
                screen,
                support.DAILY_window_page1,
                current_width // 2,
                current_height // 2
            )

            support.punch_scale_animation_one_image(
                screen,
                support.play_next_page,
                "PLAY",
                current_width //2 - 200,
                current_height //2 + 200    
            )
            support.punch_scale_animation_one_image(
                screen,
                support.play_next_page,
                "NEXT",
                current_width //2 - 200,
                current_height //2 + 100    
            )
            support.punch_scale_animation_one_image(
                screen,
               support.back_page,
                "BACK",
                current_width //2 - 300,
                current_height //2 - 300
            )
        
            if DAILY_BUTTON == "GAME":#GAME
                print("this is aiden")


##########################################################################
#------------------ STATUS
##########################################################################
    if game_state == "STATUS":

        draw_moving_map(
            screen,
            WIDTH,
            HEIGHT,
            dt    )
        droping.draw_flying_birds(
            screen,
            current_width,
            current_height
        )   
        support.open_window_with_side_effect(
            screen,
            support.daily_window,
            current_width // 2,
            current_height //2
        )
        
        # status.draw_progress(
        #     screen,
        #     600,
        #     250,
        #     720,
        #     status.passed,
        #     status.total,
        #     fonts["date"]
        # )
        # status.draw_score(
        #     screen,
        #     current_width // 2  - 400,
        #     current_height // 2 - 100,
        #     status.score_icon,
        #     fonts["date"]
        # )
        # status.draw_xp(
        #     screen,
        #     current_width // 2 + 400 ,
        #     current_height // 2 - 100,
        #     status.xp_icon,
        #     fonts["date"]
        # )
        
        # status.draw_accuracy_list(
        #     screen,
        #     current_width // 2 - 370,
        #     current_height // 2 -400,
        #     500,
        #     16,
        #     160,
        #     fonts["date"]
        # )
        
        status.draw_calendar(
            screen,
            2026,
            10,
            300,
            150,
            cell_width=100,
            cell_height=70,
            font=fonts["date"],
            title_font=fonts["DAY"]
        )
        screen_.draw_back_button(
            screen,
            back_button_rect)


##########################################################################
#------------------ ACHIEVEMENT
##########################################################################
    if game_state == "ACHIEVEMENT":

        draw_moving_map(
            screen,
            WIDTH,
            HEIGHT,
            dt    )
        droping.draw_flying_birds(
            screen,
            current_width,
            current_height
        )   
        support.open_window_with_side_effect(
            screen,
            support.daily_window,
            current_width // 2,
            current_height //2
        )
        
        achievement.achievement_scroll_y += (
            achievement.achievement_target_scroll_y
            - achievement.achievement_scroll_y
        ) * 0.12
        achievement.draw_achievements(
            screen,
            achievement.achievement_images,
            achievement.achievement_unlocked,
            achievement.achievement_names,
            achievement.achievement_descriptions,
            fonts["date"],
            achievement.achievement_scroll_y,
            achievement_area
        )
        screen_.draw_back_button(
            screen,
            back_button_rect)



##########################################################################
#------------------ CEILL
##########################################################################

    if game_state == "CEILL":        
        
        #------------------------for background 
        draw_moving_map(
            screen,
            WIDTH,
            HEIGHT,
            dt    )
        droping.draw_flying_birds(
            screen,
            current_width,
            current_height
        )   


        ceill_screen.draw_ceil_screen(
            screen,
            fonts,
            current_width,
            current_height
        )
            
                 
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
        
        
        
##########################################################################
##########################################################################
##########################################################################
#------------------------------------- GAME MODE ---------------------------------------------#
##########################################################################
##########################################################################
##########################################################################
    if game_state == "GAME MODE": 
        draw_moving_map(
            screen,
            WIDTH,
            HEIGHT,    )
            # کارت سمت چپ
            
            
            
            
        game_mode_rec.draw_left_slide_card(
            screen, game_mode_rec.left_card,
            target_x=16, y=200,
            state=game_mode_rec.left_state
        )

        game_mode_rec.draw_right_slide_card(
            screen=screen,
            card_surface=game_mode_rec.right_card,

            target_x=1811,
            y=200,

            state=game_mode_rec.right_state,
            image_items=game_mode_scroll.SHOW_LIKED_GAME,

            face_surface=game_mode_rec.circle,
            face_image=game_mode_rec.avatar_image,

            images_y=300,
            gap=25,

            face_y=20,
        )
                        


    

        screen_.draw_back_button(
            screen,
            back_button_rect)

        #--------------------------------------MATH
        if game_mode_feature == "math":

            game_mode_scroll.update_vertical_scroll()
            game_mode_scroll.draw_vertical_scroll_grid(
                screen,
                game_list.count_down_image[0:8],"math",
                8,
                current_width + 1000,
                current_height,
                game_name=game_list.count_down_game_name[0:8],
                card_gap_x=490,
                card_gap_y=570
            )    
            menu_setting_mode.gamemode_menu_setting_panel(
                screen,
                game_list.gamemode_icons,
                game_list.gamemode_icons_clicked,
                menu_setting_mode.game_mode_positions_,
                "gamemode",
                "gamemode",
                current_width // 2  - 700 ,current_height // 2 + 10
            )  
            # game_mode_rec.draw_right_slide_card(
            #     screen,
            #     game_mode_rec.right_card,
            #     visible_x=1800,
            #     hidden_x=2027,
            #     y=current_height // 2 - 410,
            #     state=game_mode_rec.right_card_state,
            # )




        #--------------------------------------LOGIC
        if  game_mode_feature == "logic":
            game_mode_scroll.update_vertical_scroll()
            game_mode_scroll.draw_vertical_scroll_grid(
                screen,
                game_list.count_down_image[8:20],"logic",
                12,
                current_width,
                current_height,
                game_name=game_list.count_down_game_name[8:20],

                card_gap_x=490,
                card_gap_y=570
            )    
            menu_setting_mode.gamemode_menu_setting_panel(
                screen,
                game_list.gamemode_icons,
                game_list.gamemode_icons_clicked,
                menu_setting_mode.game_mode_positions_,
                "gamemode",
                "gamemode",
                current_width // 2  - 900 ,current_height // 2 + 10
            )  


        #--------------------------------------MEMORY
        if game_mode_feature == "memory":

            game_mode_scroll.update_vertical_scroll()
            game_mode_scroll.draw_vertical_scroll_grid(
                screen,
                game_list.count_down_image[20:26],"memory",
                6,
                current_width,
                current_height,
                game_name=game_list.count_down_game_name[20:26],
                card_gap_x=490,
                card_gap_y=570
            )    
            menu_setting_mode.gamemode_menu_setting_panel(
                screen,
                game_list.gamemode_icons,
                game_list.gamemode_icons_clicked,
                menu_setting_mode.game_mode_positions_,
                "gamemode",
                "gamemode",
                current_width // 2  - 900 ,current_height // 2 + 10
            )  
            
        #--------------------------------------DETECTION
        if game_mode_feature == "detection":
            game_mode_scroll.update_vertical_scroll()
            game_mode_scroll.draw_vertical_scroll_grid(
                screen,
                game_list.count_down_image[26:39],"detection",
                13,
                current_width,
                current_height,
                game_name=game_list.count_down_game_name[26:39],
                card_gap_x=490,
                card_gap_y=570
            )    
            menu_setting_mode.gamemode_menu_setting_panel(
                screen,
                game_list.gamemode_icons,
                game_list.gamemode_icons_clicked,
                menu_setting_mode.game_mode_positions_,
                "gamemode",
                "gamemode",
                current_width // 2  - 900 ,current_height // 2 + 10
            )  
        #--------------------------------------FAST
        if game_mode_feature == "fast":

            game_mode_scroll.update_vertical_scroll()
            game_mode_scroll.draw_vertical_scroll_grid(
                screen,
                game_list.count_down_image[39:45],"fast",
                6,
                current_width,
                current_height,
                game_name=game_list.count_down_game_name[39:45],
                card_gap_x=490,
                card_gap_y=570
            )    
            menu_setting_mode.gamemode_menu_setting_panel(
                screen,
                game_list.gamemode_icons,
                game_list.gamemode_icons_clicked,
                menu_setting_mode.game_mode_positions_,
                "gamemode",
                "gamemode",
                current_width // 2  - 900 ,current_height // 2 + 10
            )  

        #--------------------------------------ENTERTAINMENT
        if game_mode_feature == "entertainment":

            game_mode_scroll.update_vertical_scroll()
            game_mode_scroll.draw_vertical_scroll_grid(
                screen,
                game_list.count_down_image[45:51],"entertainment",
                6,
                current_width,
                current_height,
                game_name=game_list.count_down_game_name[45:51],
                card_gap_x=490,
                card_gap_y=570
            )    
            menu_setting_mode.gamemode_menu_setting_panel(
                screen,
                game_list.gamemode_icons,
                game_list.gamemode_icons_clicked,
                menu_setting_mode.game_mode_positions_,
                "gamemode",
                "gamemode",
                current_width // 2  - 900 ,current_height // 2 + 10
            )  
        sds=135
        s=20
        rec.draw_down_card(
            screen,
            rec.score_xp,
            x=900 - sds,
            target_y=30 - s,
            state=rec.down_card_state
        )
    
        rec.draw_down_card(
            screen,
            rec.score,
            x=922 - sds,
            target_y=50 - s,
            state=rec.down_card_state
        )
    
        rec.draw_down_card(
            screen,
            rec.xp,
            x=1168 - sds,
            target_y=50 - s,
            state=rec.down_card_state
        )
        
        score_xp.draw_down_card(
            screen,
            score_xp.down_card_state,
            duration=0.8,

            image1=score_xp.xp_im,
            image2=score_xp.score_im,

            image1_x=922+15 - sds,
            image1_y=59 - s,

            image2_x=1168+2 - sds ,
            image2_y=59 - s,

            text1=score_xp.xp,
            text2=score_xp.score,

            text1_x=922 + 100 - sds,
            text1_y=60 + 10 - s ,

            text2_x=1168 +  80 - sds ,
            text2_y=60 +10 - s ,

            font=fonts["date"]
        )
        
        
        
        rec.draw_down_card(
            screen,
            rec.game_title_back,
            x=885,
            target_y=140 - s,
            state=rec.down_card_state
        )
        rec.draw_down_card(
            screen,
            rec.game_title,
            x=905,
            target_y=160 - s,
            state=rec.down_card_state
        )
        

##########################################################################
#------------------ TIME
##########################################################################
    if game_state == "TIME":

        # for background  flying and image 
        draw_moving_map(
            screen,
            WIDTH,
            HEIGHT,
            dt    )
        droping.draw_flying_birds(
            screen,
            current_width,
            current_height
        )   

        draw_time_screen(
            screen,
            fonts,
            time_button_rects,
            current_width,
            current_height
        )
                 
        screen_.draw_back_button(
            screen,
            back_button_rect
        )


##########################################################################
#------------------ BUY_PREMIUM
##########################################################################

    if game_state == "BUY_PREMIUM":
        draw_moving_map(
            screen,
            WIDTH,
            HEIGHT,
            dt    )
        droping.draw_flying_birds(
            screen,
            current_width,
            current_height
        )   
        

        side_effect_window.open_window_with_side_effect_MULLTI_WINDOW(
            screen,
            all_image.donate,
            current_width // 2,
            current_height // 2,
            )

        donate.draw_donate(
            screen,
            fonts["date"]
        )
        screen_.draw_back_button(
            screen,
            back_button_rect)
        
        
##########################################################################
#------------------ SETTING
##########################################################################

    if game_state == "SETTING":

        draw_moving_map(
            screen,
            WIDTH,
            HEIGHT,    )
        screen.blit(rec.menu_card_over, (-120, current_height // 2 - 800))
        screen.blit(rec.icon_menu, (193,10))        


        # menu_setting_mode.gamemode_menu_setting_panel(
        #     screen,
        #     menu_setting_mode.setting_icons,
        #     menu_setting_mode.setting_positions,
        #     "setting",
        #     "setting",
        #     current_width // 2  - 804 ,current_height // 2 ,#image=setting_panel

        # )
        menu.scroll_y += (
            menu.target_scroll_y - menu.scroll_y
        ) * 0.03
        menu.draw_six_scroll_items(
            screen,
            menu.images_setting,
            menu.names_setting,
            menu_hidden_rect,
            image_count=6,
            mode="setting",
            item_height=370,
            scroll_y=menu.scroll_y,
            font=fonts["date"]
        )

    # ############################################

    # ############################################

                
                
                
        # rec.draw_right_slide_card(
        #     screen,
        #     rec.right_card,
        #     visible_x=1800,
        #     hidden_x=2027,
        #     y=current_height // 2 - 540,
        #     state=rec.right_card_state,
        #     mouse_trigger_x=500,
        #     hide_delay=5.0
        # )


##########################################################################
#------------------ DIFFICULTY SELECTION
##########################################################################

    # if game_state == "DIFFICULTY SELECTION":

    #     for index, game_name in enumerate(game_list.all_games):

    #         if before_game.previous_game_state_F == game_name:

    #             difficulty_selection_menu_image = (
    #                 game_list.count_down_image_background[index]
    #             )

    #             game_image_title = (
    #                 game_list.count_down_image[index]
    #             )

    #             break
    #     before_game.backgorund_now_for_any_game_mode = difficulty_selection_menu_image

    #     difficulty_selection_menu.difficulty_menu(
    #         difficulty_selection_menu.circle,
    #         screen,
    #         difficulty_selection_menu_image,
    #         game_image_title,
    #         difficulty_selection_menu.difficulty_button_image[0],
    #         difficulty_selection_menu.back_image,
    #         difficulty_selection_menu.sound_image,
    #         difficulty_selection_menu.music_image,
    #         fonts["date"]
    #     )



##########################################################################
#------------------ COUNT_DOWN
##########################################################################
    # if game_state == "COUNT_DOWN":
    #     # countdown(screen, image)

    #     for index, game_name in enumerate(game_list.count_down_game_name):

    #         if before_game.previous_game_state_F == game_name:
            
    #             image = game_list.count_down_image_background[index]
            
    #             countdown(screen, image)
                
    #             break

    #     before_game.before_game_start = False
        
    #     game_state = before_game.previous_game_state_F
        
    #     before_game.backgorund_now_for_any_game_mode = image
        
        
        
        
##########################################################################
#------------------ GAME GUID
##########################################################################

    if game_state == "GAME OVERVIEW":
        draw_moving_map(
            screen,
            WIDTH,
            HEIGHT,    )

        # guid_sild_effect(
        #     screen,
        #     support.before_game_window,
        #     current_width // 2,
        #     current_height //2
        # )


        support.punch_scale_animation_one_image(
            screen,
            support.back_page,
            "BACK",
            current_width //2 - 900,
            current_height //2 + 540
        )
        support.punch_scale_animation_one_image(
            screen,
            support.how_to_play_next_button_page,
            "NEXT",
            current_width //2 + 920,
            current_height //2 +320    
        )
        support.next_page_rec2 = None
        support.pro_rec = None
        if (before_game.previous_game_state_F in free_game_list or buy_premium == True):
            support.punch_scale_animation_one_image(
                screen,
                support.next_page,
                "PLAY",
                current_width // 2 + 920,
                current_height // 2 + 540
            )

        else:
            support.punch_scale_animation_one_image(
                screen,
                support.pro_page,
                "PRO",
                current_width // 2 + 890,
                current_height // 2 + 540
            )
            
            
        game_mode_face.side_effect_from_right(
            screen,
            images=game_mode_face.images,
            # rects=game_mode_face.rects,
            texts=game_mode_face.texts
        )

                
        # screen.blit(rec.game_guid_card, (current_width // 2 - 850 ,current_height // 2 - 550))#down
        
        # screen.blit(rec.regtangle_guid_page, (current_width // 2 - 850 ,current_height // 2 - 550))
        # screen.blit(rec.circle_guid_page, (1019 ,188))
        
        # side_effect_window.open_window_with_side_effect_MULLTI_WINDOW(
        #     screen,
        #     all_image.info,
        #     current_width // 2,
        #     current_height // 2,
        #     on_draw=game_overview.draw_GAME_OVERVIEW

        # )

##########################################################################
#------------------ NEXT GAME GUID
##########################################################################

    if game_state == "HOW TO PLAY":
        draw_moving_map(screen,WIDTH,HEIGHT,    )

        # guid_sild_effect(
        #     screen,
        #     support.before_game_window,
        #     current_width // 2,
        #     current_height //2
        # )

        support.next_page_rec2 = None
        support.pro_rec = None
        if (
            before_game.previous_game_state_F in free_game_list
            or buy_premium == True
        ):
            support.punch_scale_animation_one_image(
                screen,
                support.next_page,
                "PLAY",
                current_width // 2 + 920,
                current_height // 2 + 540
            )

        else:
            support.punch_scale_animation_one_image(
                screen,
               support.pro_page,
                "PRO",
                current_width // 2 + 890,
                current_height // 2 + 540
            )

        support.punch_scale_animation_one_image(
            screen,
            support.back_page,
            "BACK",
            current_width //2 - 900,
            current_height //2 + 540
        )

        game_mode_face.side_effect_from_right(
            screen,
            images=game_mode_face.images,
            rects=game_mode_face.rects,
            texts=game_mode_face.texts
        )

##########################################################################
#------------------ STORE
##########################################################################

    if game_state == "STORE":
                # for background  flying and image 
        draw_moving_map(
            screen,
            WIDTH,
            HEIGHT,
            dt    )
        droping.draw_flying_birds(
            screen,
            current_width,
            current_height
        )   
    
        support.open_window_with_side_effect(
            screen,
            support.STOR__,
            current_width// 2,
            current_height//2 
        )

        screen_.draw_back_button(
            screen,
            back_button_rect
        )
        
        
        
##########################################################################
#------------------ MESSAGE
##########################################################################

    if game_state == "MESSAGE":
        draw_moving_map(
            screen,
            WIDTH,
            HEIGHT,
            dt    )
        droping.draw_flying_birds(
            screen,
            current_width,
            current_height
        )   
        support.open_window_with_side_effect(
            screen,
            all_image.setting,
            current_width // 2 + 150,current_height // 2 
        )
        screen_.draw_back_button(
            screen,
            back_button_rect)
        
        
        
        
        
##########################################################################
#------------------ DONATE_
##########################################################################
    if game_state == "DONATE_":
                # for background  flying and image 
        draw_moving_map(
            screen,
            WIDTH,
            HEIGHT,
            dt    )
        droping.draw_flying_birds(
            screen,
            current_width,
            current_height
        )   
    
        support.open_window_with_side_effect(
            screen,
            support.STOR__,
            current_width// 2,
            current_height//2 
        )

        screen_.draw_back_button(
            screen,
            back_button_rect
        )




##########################################################################
#------------------ OPERATION
##########################################################################

    if game_state == "OPERATION":
        #------------------------for background 
        draw_moving_map(
            screen,
            WIDTH,
            HEIGHT,
            dt    )
        droping.draw_flying_birds(
            screen,
            current_width,
            current_height
        )   
        operation_screen.draw_operation_screen(
            screen,
            fonts,
            operator_images,
            operator_rects,
            current_width,
            current_height)
        screen_.draw_back_button(
            screen,
            back_button_rect
        )




##########################################################################
#------------------ PROFILE
##########################################################################
    if game_state == "PROFILE":
    
        draw_moving_map(
            screen,
            WIDTH,
            HEIGHT,
            dt    )
        droping.draw_flying_birds(
            screen,
            current_width,
            current_height
        )   
    
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
        

        profile_.draw_profile_in_profile_tab(
            screen,
            profile_.selected_profile_image,
            profile_.p999,
            current_width,
            current_height
        )

























##########################################################################
#------------------ DASHBOARD
##########################################################################
##########################################################################
#------------------ DASHBOARD
##########################################################################
##########################################################################
#------------------ DASHBOARD
##########################################################################
##########################################################################
#------------------ DASHBOARD
##########################################################################
##########################################################################
#------------------ DASHBOARD
##########################################################################
##########################################################################
#------------------ DASHBOARD
##########################################################################
##########################################################################
#------------------ DASHBOARD
##########################################################################

    if  DASHBOARD == True and is_guest == False: 

        
        custom_math.draw_punch_image_1(
            screen,
            custom_math.rank__,
             (current_width//2 +290, current_height // 2 - 335 ),
            (550, 550),
            "rank",0.45,
            center_image=custom_math.punch_daily_for_dahsboard,
            center_image_size=(90, 90),
            text="",
            text_font=fonts["date"]
        )
        custom_math.draw_punch_image_1(
            screen,
            custom_math.rank__2,
            (current_width//2 -300, current_height // 2 - 335 ),
            (550, 550),
            "rank2",0.45,
            center_image=custom_math.punch_rank,
            center_image_size=(90, 90),
            text="",
            text_font=fonts["date"]
        )
    
        #---------------------------- popular game
        popular_game.image_rects =popular_game.draw_three_images(
            screen,
            popular_game.selected_images
        )
                
                
        recent_game.image_rects =recent_game.draw_three_images_recent_game(
            screen,
            recent_game.selected_images
        )
        

                
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




##########################################################################
#------------------ THREE_ICONS
##########################################################################

    if  THREE_ICONS == True and DASHBOARD == False :

        button.store_base(
            screen,
            store__button_rect
        )
        button.store_button(
            screen,
            store__button_rect
        )
        
        button.sms_base(
            screen,
            sms_button_rect
        )
        button.sms_button(
            screen,
            sms_button_rect
        )

        if game_state != "MENU" and game_state != "SETTING":
    
            button.donate_base(
                screen,
                call_button_rect
            )
            button.donate_button(
                screen,
                call_button_rect
            )
        
        
        
        
##########################################################################
#------------------ MENU_EFFECT
##########################################################################
    
    if MENU_EFFECT and (game_state == "MENU" or game_state == "SETTING"):
        # rec.draw_down_card(
        #     screen,
        #     rec.down_card,
        #     x=-8,
        #     target_y=current_height // 2 - 900,
        #     state=rec.down_card_state
        # )

        # rec.draw_down_card(
        #     screen,
        #     rec.icon_menu,
        #     x=166,
        #     target_y=current_height // 2 - 630,
        #     state=rec.down_card_state
        # )
        # rec.draw_down_card(
        #     screen,
        #     rec.profile_image,
        #     189,
        #     current_height // 2 - 600,
        #     rec.down_card_state,
        #     text="alirezanab",
        #     text_x=170,
        #     text_y_offset=155,
        #     font=fonts["date"]
        # )
                        
                        
                    
                    
                    
                    
                    
                    
                    
                    

                    
        if game_state == "MENU" or game_state == "SETTING":
            corner.darw_corner_face(
                screen,
                corner.right_card,
                corner.right_card_center,

                # X: سه مقدار افقی
                visible_x=1985,  # مبدأ: خارج صفحه از سمت راست
                target_x=1800,   # مقصد: محل ورود کارت
                hidden_x=1945,   # محل مخفی شدن از سمت راست

                # Y: سه مقدار عمودی
                visible_y=1262,  # مبدأ: خارج صفحه از پایین
                target_y=1035,   # مقصد: محل ورود کارت
                hidden_y=1250,   # محل مخفی شدن از پایین

                state=corner.right_card_state,
                images=[corner.corner],
                texts=[],
                font=fonts["date"]
            )
        
            
            corner.darw_corner_face_top(
                screen,
                corner.right_card_1,
                corner.right_card_1_center,

                # X: همان مختصات افقی
                visible_x=2005,
                target_x=1795,
                hidden_x=1945,

                # Y: قرینه برای گوشه بالا
                visible_y=-219,  # مبدأ: خارج صفحه از بالا
                target_y=15,     # مقصد: پایین‌تر از لبه بالا
                hidden_y=-200,   # محل مخفی شدن از بالا

                state=corner.top_right_card_state,
                images=[corner.top],
                texts=[],
                font=fonts["date"]
            )
            rec.draw_right_slide_card(
                screen,
                rec.right_card,
                rec.right_card_center,
                visible_x=1800,
                hidden_x=2027,
                y=current_height // 2 - 410,
                state=rec.right_card_state,
                images=rec.right_images,
                texts=rec.right_texts,
                font=rec.fonts["date"]
            )
            rec.draw_jelly_rect(
                screen,
                rec.start_card,
                x=900,
                target_y=1100,
                state=rec.start_card_state,
                text_is_on=False,
                screen_height=current_height,
                rise_time=1.0,
                stay_time=5.0,
                down_time=1.0,
                bottom_wait=1.0
            )
            rec.draw_jelly_rect(
                screen,
                rec.start_button_card,
                x=1000,
                target_y=1140,
                state=rec.other_card_state,
                text_is_on=True,
                screen_height=current_height,
                rise_time=1.0,
                stay_time=5.0,
                down_time=1.0,
                bottom_wait=1.0
            )
                
                        
                        
                        
                        
                        
                        
                        

            
        if game_state == "MENU" or game_state == "SETTING" :
                            
            rec.draw_down_card(
                screen,
                rec.score_xp,
                x=900,
                target_y=50,
                state=rec.down_card_state
            )
        
            rec.draw_down_card(
                screen,
                rec.score,
                x=922,
                target_y=70,
                state=rec.down_card_state
            )
        
            rec.draw_down_card(
                screen,
                rec.xp,
                x=1168,
                target_y=70,
                state=rec.down_card_state
            )
            
            score_xp.draw_down_card(
                screen,
                score_xp.down_card_state,
                duration=0.8,

                image1=score_xp.xp_im,
                image2=score_xp.score_im,

                image1_x=922+15,
                image1_y=79,

                image2_x=1168+2 ,
                image2_y=79,

                text1=score_xp.xp,
                text2=score_xp.score,

                text1_x=922 + 100,
                text1_y=80 + 10 ,

                text2_x=1168 +  80 ,
                text2_y=80 +10 ,

                font=fonts["date"]
            )

            if menu_state == "ACHIEVEMENT":  
                rec_window.draw_dark_overlay(screen, alpha=130)
                rec_window.draw_slide_rect(
                    screen,
                    rec_window.PROGRESS,
                    target_x=screen.get_width() - rec_window.PROGRESS.get_width() - (-450),
                    target_y=current_height // 2 - 660,
                    mode=3,
                    duration=1,
                    state=rec_window.PROGRESS_state
                )
            if menu_state == "PROGRESS":  
                rec_window.draw_dark_overlay(screen, alpha=130)
                rec_window.draw_slide_rect(
                    screen,
                    rec_window.PROGRESS,
                    target_x=screen.get_width() - rec_window.PROGRESS.get_width() - (-450),
                    target_y=current_height // 2 - 660,
                    mode=3,
                    duration=1,
                    state=rec_window.PROGRESS_state
                )
            if menu_state == "STATUS":  
                rec_window.draw_dark_overlay(screen, alpha=130)
                rec_window.draw_slide_rect(
                    screen,
                    rec_window.PROGRESS,
                    target_x=screen.get_width() - rec_window.PROGRESS.get_width() - (-450),
                    target_y=current_height // 2 - 660,
                    mode=3,
                    duration=1,
                    state=rec_window.PROGRESS_state
                )





##########################################################################
##########################################################################
##########################################################################
########
#######
######
#####
####
###
##
#------------- SETTING
#
##
###
####
#####
######
#######
##########################################################################
##########################################################################
##########################################################################


   #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if  game_state == "SETTING" and setting_menu == "MUSIC" and control_every_button_in_setting_on_or_off == "music":

        # support.open_window_with_side_effect(
        #     screen,
        #     all_image.setting,
        #     current_width // 2 + 150,current_height // 2 
        # )
        rect_window.draw_punch_rect(
            screen,
            punch_frames,
            center=(1158, 625),
            state=rect_window.punch_state,
            duration=0.55
        )
        # music.draw_music(
        #     screen,
        #     current_width,
        #     current_height,
        #     all_image.setting,
        #     music_profile_image
        # )
        
        
   #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if  game_state == "SETTING" and setting_menu == "LANGUAGE" and control_every_button_in_setting_on_or_off == "language":

        support.open_window_with_side_effect(
                screen,
                all_image.setting,
                current_width // 2 + 150,current_height // 2 
            )

        language_rects = language.draw_languages(
            screen,
            current_width,
            current_height
        )
    
    
    
   #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if  game_state == "SETTING" and setting_menu == "MORE" and control_every_button_in_setting_on_or_off == "more":

        custom_math.draw_punch_image2(
            screen,
            custom_math.new_window_for_more_support,
            custom_math.positions_____1[0],
            (500, 500),
            "MORE1",
            center_image=more.images_support[0],
            center_image_size=(300, 300),
            text="faq",
            text_font=fonts["date"]
        )
        custom_math.draw_punch_image2(
            screen,
            custom_math.new_window_for_more_support,
            custom_math.positions_____1[1],
            (500, 500),
            "MORE2",
            center_image=more.images_support[1],
            center_image_size=(300, 300),
            text="info",
            text_font=fonts["date"]
        )
        
        custom_math.draw_punch_image2(
            screen,
            custom_math.new_window_for_more_support,
            custom_math.positions_____1[2],
            (500, 500),
            "MORE3",
            center_image=more.images_support[2],
            center_image_size=(300, 300),
            text="privacy_policy",
            text_font=fonts["date"]
        )
        
        # more app
        custom_math.draw_punch_image2(
            screen,
            custom_math.new_window_for_more_support,
            custom_math.positions_____1[3],
            (500, 500),
            "MORE4",
            center_image=more.images_support[3],
            center_image_size=(300, 300),
            text="more_app",
            text_font=fonts["date"]
        )
        
        screen_.draw_back_button(
            screen,
            back_button_rect)
        
        
   #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state == "FAQ":
        
        draw_moving_map(
            screen,
            WIDTH,
            HEIGHT,
            dt    )
        droping.draw_flying_birds(
            screen,
            current_width,
            current_height
        )   

        side_effect_window.open_window_with_side_effect_MULLTI_WINDOW(
            screen,
            all_image.faq,
            current_width // 2,
            current_height // 2,
            on_draw=FAQ.draw_FAQ_side_effect
        )
        screen_.draw_back_button(
            screen,
            back_button_rect)
        
   #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state == "INFO":
        draw_moving_map(
            screen,
            WIDTH,
            HEIGHT,
            dt    )
        droping.draw_flying_birds(
            screen,
            current_width,
            current_height
        )   

        side_effect_window.open_window_with_side_effect_MULLTI_WINDOW(
            screen,
            all_image.info,
            current_width // 2,
            current_height // 2,
            on_draw=INFO.draw_INFO_side_effect

        )
        screen_.draw_back_button(
            screen,
            back_button_rect)

   #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state == "Privacy Policy":

        draw_moving_map(
            screen,
            WIDTH,
            HEIGHT,
            dt    )
        droping.draw_flying_birds(
            screen,
            current_width,
            current_height
        )   

        side_effect_window.open_window_with_side_effect_MULLTI_WINDOW(
            screen,
            all_image.policy,
            current_width // 2,
            current_height // 2,
            on_draw=policy.draw_privacy_side_effect
        )
        
        screen_.draw_back_button(
            screen,
            back_button_rect)


   #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
   
    if  game_state == "SETTING" and setting_menu == "ACCOUNT" and control_every_button_in_setting_on_or_off == "account":

        support.open_window_with_side_effect(
                screen,
                all_image.setting,
                current_width // 2 + 150 ,current_height // 2 
            )
        if is_guest :
            account.draw_profile_account(
                screen,
                start_screen.gest_image_selected,
                fonts["date"],
                fonts["date"],
                fonts["date"],
                True,
                image_size=300
            )
        else:
            account.draw_profile_account(
                screen,
                start_screen.user_image_selected,
                fonts["date"],
                fonts["date"],
                fonts["date"],
                False,
                image_size=300
            )
            
            
            
            
            
   #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾

    if  game_state == "SETTING" and setting_menu == "SOUND" and control_every_button_in_setting_on_or_off == "sound":

        support.open_window_with_side_effect(
                screen,
                all_image.setting,
                current_width // 2 + 150,current_height // 2 
            )

        sound.sound_screen(screen)










##########################################################################
##########################################################################
##########################################################################
###
####
#####
######
#######
########
#########
###########------------- GAMES
#########
########
#######
######
#####
####
###
##########################################################################
##########################################################################
##########################################################################

    if game_state == "MEMORY MATCH":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        MEMORY.memory_(
            screen,
            current_width,
            current_height
        )
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
        profile_.draw_profile_live_circle(
            screen,
            profile_.selected_profile_image,
            profile_.p99,
            current_width
        )
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state == "COLOR MATCH":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        SHAPE_COLOR_NAME.SHAPE_COLOR_NAME(screen,current_width)
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state == "MEMORY PATTERN":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        REPEAT_AFTER_ME.REPEAT_AFTER_ME_(screen)
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state == "DIRECTION":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        DIRECTION.DIRECTION_(screen)
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if  game_state == "MIRROR PATTERN":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        MIRROR.MIRROR_(screen)
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="REACTION":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        ACTION.ACTION_(screen)
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state == "MISSING NUMBER":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode) 
             
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state == "60S":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        SIX_60S.SIX_60S(
            screen,
            current_width
        )
        screen_.draw_back_button(
            screen,
            back_button_rect
        )

    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state == "COMPARE NUMBERS":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        MORE_LESS_EQUAL.MORE_LESS_EQUAL_(screen)
        profile_.draw_profile_live_circle(
            screen,
            profile_.selected_profile_image,
            profile_.p99,
            current_width
        )
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state == "TRUE OR FALSE":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        TRUE_FALSE.TRUE_FALSE_(screen)
        profile_.draw_profile_live_circle(
            screen,
            profile_.selected_profile_image,
            profile_.p99,
            current_width
        )
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state == "RIGHT SIGN":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        FIND_OPERATOR.FIND_OPERATOR_(screen)
        profile_.draw_profile_live_circle(
            screen,
            profile_.selected_profile_image,
            profile_.p99,
            current_width
        )
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state == "IMAGE RECALL":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        DETECT.DETECT_(screen,current_width,current_height)
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="MATH RUSH":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        FAST.FAST_(screen,current_width)
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="COUNT ITEM":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        HOW_MANY.HOW_MANY_(screen,current_width,current_height)
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="MEMORY CALC":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        HARD.HARD_(screen,current_width,current_height)
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="QUICK DETECT":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        DETECT_PRO.DETECT_PRO_(screen,current_width,current_height)
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
     #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="NUMBER ORDER":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        MEMORY_GO.MEMORY_GO_(screen,current_width,current_height)
        screen_.draw_back_button(
            screen,
            back_button_rect
        )

    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="DIRECTION DETECT":

        if not stop_loop:
            design.back_setter(screen, before_game.backgorund_now_for_any_game_mode)
            MOVE_ARROW.MOVE_ARROW_(screen, current_width, current_height)

            angle += 0.5

            utils.utils_(
                screen,
                selected_image,
                1880,
                166,
                angle
            )

        if in_game_is_menu_on:

            menu_window.SHOW_XP(
                screen,
                2,
                HEIGHT,
                WIDTH
            )
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="MATH CHAIN":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        MATH_GO.MATH_GO_(screen)
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="MATH RECALL":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        FAST_ADD_SUB.QUICK_MATH(screen)
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="MEMORY PATH":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        FOLLOW_THAT.FOLLOW_THAT_(screen)
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="IMAGE SEQUENCE":  
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        IMAGE_SELECT.IMAGE_SELECT_(screen)
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="THOOZ":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        THOOZ.update_computer_move()
        THOOZ.THOOZ_(screen,current_width)
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="CHESS":

        draw_moving_map(screen,WIDTH,HEIGHT,    )
        CHESS.CHESS_()
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
 #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="NUMBER SLIDE":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        SORT_NUMBER.SORT_NUMBER_()
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="SUDOKU":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        SUDOKU.SUDOKU_()
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="HIDDEN WORD":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        WORD.WORD_()
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="MINESWEEPER":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        MINESWEEPER.MINESWEEPER_()
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="MAZE":
        draw_moving_map(
            screen,
            WIDTH,
            HEIGHT,    )
        # design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        MAZE.MAZE_()
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
    #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="MEMORY RECALL":  
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        MEMORY_HARD.update()
        MEMORY_HARD.MEMORY_HARD_()
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
   #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="FIND THE NEW":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        CHOOSE_IMAGE.CHOOSE_IMAGE_()
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
   #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="MATCH": 
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        MATCH3.MATCH3_()
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
   #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="CONNECT 4":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        CONNECT_FOUR.CONNECT_FOUR_()
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
   #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="SNAKE":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        SNAKE.main_SNAKE()
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
   #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="UNBLOCK CAR":  
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        UNBLOCK_CAR.main()
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
   #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="PUZZLE":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        PUZZLE.PUZZLE_()
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
   #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="CHECKERS":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        CHECKERS.CHECKERS_()
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
   #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="DOTS BOXS":    
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        DOTS_BOX.DOTS_BOX_()
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
   #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="COLOR FLOW":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        FOLLOW_FREE.FOLLOW_FREE_()
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
   #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="GO":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        GO.GO_()
        screen_.draw_back_button(
                screen,
                back_button_rect
            )
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       
     #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
    if game_state =="SPIN_HIT":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        SPIN_HIT.SPIN_HIT_()
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
     #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾

    if game_state =="MERGE_2048":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        MERGE_2048.GAME_2048_()
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
     #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾

    if game_state =="BREAKOUT":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        BREAKOUT.BREAKOUT_()
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
     #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾

    if game_state =="DINO_RUN":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        DINO_RUN.DINO_RUN_()
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
     #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾

    if game_state =="COLOR_RUSH":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        COLOR_RUSH.COLOR_SWITCH_()
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
     #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾

    if game_state =="FLAPPY_BIRD":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        FLAPPY_BIRD.FLAPPY_BIRD_()
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
     #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾

    if game_state =="TOW_CARS":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        TOW_CARS.TOW_CARS_()
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
     #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾

    if game_state =="PACMAN":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        PACMAN.PACMAN_()

        screen_.draw_back_button(
            screen,
            back_button_rect
        )
     #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾

    if game_state =="SPEED_TYPE":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        SPEED_TYPE.TYPING_GAME_()
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
     #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾

    if game_state =="BALL TRACKER":
        draw_moving_map(
            screen,
            WIDTH,
            HEIGHT,    )
        # design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        BALL_TRACKER.BALL_TRACKER_()
        screen_.draw_back_button(
            screen,
            back_button_rect
        )
     #👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾

    if game_state =="NUMBER_DETECT":
        design.back_setter(screen,before_game.backgorund_now_for_any_game_mode)
        NUMBER_DETECT.NUMBER_HUNT_()
        screen_.draw_back_button(
            screen,
            back_button_rect
        )




##########################################################################
##########################################################################
##########################################################################
    coming_soon.coming_soon_notification(screen)

    achievement.show_achievement_popup(
        screen,
        achievement.achievement_images[0],
        "FIRST GAME",
        achievement.achievement_trigger,
        fonts["date"],
    )
        

    #--------------------------------------------------------------------------------------CUSTOM MATH
    if  game_state == "CUSTOM GAME":

        design.back_setter(screen,CUSTOM__GAME)





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


        profile_.draw_profile_live_circle(
            screen,
            profile_.selected_profile_image,
            profile_.p99,
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

    
#-------------------------------- FPS SETTING    
    fps = clock.get_fps()

    fps_text = fonts["date"].render(f"FPS: {int(fps)}", True, (255,255,255))

    screen.blit(fps_text, (20,20))
    

#-------------------------------- MOUSE EFFECT    
    mouse.draw_click_effect(screen)
    
    
    
#-------------------------------- UPDATE AND EXIT
    pygame.display.update()
    clock.tick(60)
pygame.quit()
sys.exit()








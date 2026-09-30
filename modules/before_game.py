import pygame
#---------------- این برای صفحه قبل از شروع بازی است و شمارش معکوسه
before_game_start = True
backgorund_now_for_any_game_mode = None
# previous_game_state_F=None



                

    
#------------------------ این  تابع بریا گرفتن عکس هر بازی است 
# ============================================================
# GET GUIDE IMAGE FOR EACH GAME
# ============================================================
from modules.game_list import count_down_image
from modules import mode as MODE

def guid_icon_setter_for_eatch_game(previous_game_state_F):

    if previous_game_state_F == "THOOZ":
        loader_image_for_before_game(
            count_down_image[0],MODE.logic, "online", "5", "tow", "hard"
        )

    elif previous_game_state_F == "MAZE":
        loader_image_for_before_game(
            count_down_image[1],MODE.detection, "offline", "3", "one", "easy"
        )

    elif previous_game_state_F == "WORD":
        loader_image_for_before_game(
            count_down_image[2], MODE.detection, "online", "8", "tow", "hard"
        )

    elif previous_game_state_F == "SUDOKU":
        loader_image_for_before_game(
            count_down_image[3],MODE.logic, "offline", "7", "one", "hard"
        )

    elif previous_game_state_F == "SORT_NUMBER":
        loader_image_for_before_game(
            count_down_image[4],MODE.logic, "offline", "6", "one", "normal"
        )

    elif previous_game_state_F == "CHOOSE_IMAGE":
        loader_image_for_before_game(
            count_down_image[5],MODE.memory, "offline", "7", "one", "hard"
        )

    elif previous_game_state_F == "MATCH3":
        loader_image_for_before_game(
            count_down_image[6],MODE.detection, "offline", "5", "one", "easy"
        )

    elif previous_game_state_F == "60S":
        loader_image_for_before_game(
            count_down_image[7],MODE.math, "onliofflinene", "8", "tow", "normal"
        )

    elif previous_game_state_F == "CONNECT_FOUR":
        loader_image_for_before_game(
            count_down_image[8],MODE.logic, "online", "7", "tow", "hard"
        )

    elif previous_game_state_F == "CHESS":
        loader_image_for_before_game(
            count_down_image[9],MODE.logic , "online", "9", "tow", "hard"
        )

    elif previous_game_state_F == "TRUE_FALSE":
        loader_image_for_before_game(
            count_down_image[10],MODE.math , "offline", "8", "one", "normal"
        )

    elif previous_game_state_F == "REPEAT_AFTER_ME":
        loader_image_for_before_game(
            count_down_image[11],MODE.memory , "offline", "9", "one", "normal"
        )

    elif previous_game_state_F == "MORE_LESS_EQUAL":
        loader_image_for_before_game(
            count_down_image[12],MODE.math , "online", "8", "tow", "hard"
        )

    elif previous_game_state_F == "MOVE_ARROW":
        loader_image_for_before_game(
            count_down_image[13], MODE.detection, "offline", "5", "one", "hard"
        )

    elif previous_game_state_F == "MIRROR":
        loader_image_for_before_game(
            count_down_image[14],MODE.detection , "offline", "5", "one", "easy"
        )

    elif previous_game_state_F == "MEMORY":
        loader_image_for_before_game(
            count_down_image[15],MODE.memory , "offline", "6", "one", "easy"
        )

    elif previous_game_state_F == "MEMORY_GO":
        loader_image_for_before_game(
            count_down_image[16],MODE.memory, "offline", "7", "one", "normal"
        )

    elif previous_game_state_F == "MATH_GO":
        loader_image_for_before_game(
            count_down_image[17],MODE.math , "online", "10", "tow", "expert"
        )

    elif previous_game_state_F == "HARD":
        loader_image_for_before_game(
            count_down_image[18],MODE.detection , "offline", "10", "one", "expert"
        )

    elif previous_game_state_F == "IMAGE_SELECT":
        loader_image_for_before_game(
            count_down_image[19],MODE.detection, "offline", "8", "one", "hard"
        )

    elif previous_game_state_F == "FOLLOW_THAT":
        loader_image_for_before_game(
            count_down_image[20],MODE.memory , "offline", "7", "one", "normal"
        )

    elif previous_game_state_F == "HOW_MANY":
        loader_image_for_before_game(
            count_down_image[21],MODE.fast , "online", "7", "tow", "easy"
        )

    elif previous_game_state_F == "FIND_OPERATOR":
        loader_image_for_before_game(
            count_down_image[22],MODE.math, "online", "10", "tow", "hard"
        )

    elif previous_game_state_F == "FIND_NUMBER":
        loader_image_for_before_game(
            count_down_image[23],MODE.math, "online", "10", "tow", "expert"
        )


    elif previous_game_state_F == "FAST":
        loader_image_for_before_game(
            count_down_image[24],MODE.fast , "online", "10", "tow", "hard"
        )

    elif previous_game_state_F == "FAST_ADD_SUB":
        loader_image_for_before_game(
            count_down_image[25],MODE.math , "online", "9", "tow", "hard"
        )

    elif previous_game_state_F == "DIRECTION":
        loader_image_for_before_game(
            count_down_image[26],MODE.detection, "offline", "6", "one", "hard"
        )

    elif previous_game_state_F == "DETECT_PRO":
        loader_image_for_before_game(
            count_down_image[27],MODE.detection, "offline", "9", "one", "expert"
        )

    elif previous_game_state_F == "DETECT":
        loader_image_for_before_game(
            count_down_image[28],MODE.detection, "offline", "8", "one", "hard"
        )

    elif previous_game_state_F == "ACTION":
        loader_image_for_before_game(
            count_down_image[29],MODE.fast, "offline", "4", "one", "easy"
        )

    elif previous_game_state_F == "UNLOCK_CAR":
        loader_image_for_before_game(
            count_down_image[30],MODE.logic, "offline", "5", "one", "normal"
        )

    elif previous_game_state_F == "DOTS_BOX":
        loader_image_for_before_game(
            count_down_image[31],MODE.logic, "online", "5", "tow", "normal"
        )

    elif previous_game_state_F == "SNAKE":
        loader_image_for_before_game(
            count_down_image[32],MODE.detection, "offline", "5", "one", "easy"
        )

    elif previous_game_state_F == "PUZZLE":
        loader_image_for_before_game(
            count_down_image[33],MODE.logic, "offline", "4", "one", "easy"
        )

    elif previous_game_state_F == "GO":
        loader_image_for_before_game(
            count_down_image[34],MODE.logic , "online", "9", "tow", "hard"
        )

    elif previous_game_state_F == "SHAPE_COLOR_NAME":
        loader_image_for_before_game(
            count_down_image[35],MODE.detection , "online", "8", "one", "expert"
        )
    elif previous_game_state_F == "CHECKERS":
        loader_image_for_before_game(
            count_down_image[36],MODE.logic , "online", "7", "tow", "hard"
        )

    elif previous_game_state_F == "FOLLOW_FREE":
        loader_image_for_before_game(
            count_down_image[37],MODE.logic , "offline", "5", "one", "normal"
        )

    elif previous_game_state_F == "MINESWEEPER":
        loader_image_for_before_game(
            count_down_image[38],MODE.detection , "offline", "5", "one", "normal"
        )

    elif previous_game_state_F == "MEMORY_HARD":
        loader_image_for_before_game(
            count_down_image[39],MODE.memory, "offline", "9", "one", "expert"
        )
#---------------------------------------------------------------- before  game  این برای قبل از بازی است صفحه راهنما 
#---------------------------------------------------------------- before  game  این برای قبل از بازی است صفحه راهنما 
#---------------------------------------------------------------- before  game  این برای قبل از بازی است صفحه راهنما 
#---------------------------------------------------------------- before  game  این برای قبل از بازی است صفحه راهنما 
#---------------------------------------------------------------- before  game  این برای قبل از بازی است صفحه راهنما 
imagez1=None
imagez2=None
imagez3=None
imagez4=None
imagez5=None
imagez6=None
side_images = []
def loader_image_for_before_game(logo,mode,online,xp,players,dif):
    global imagez1
    global imagez2
    global imagez3
    global imagez4
    global imagez5
    global imagez6
    global side_images
    
    guid_icon=(160,160)
    imagez1 = pygame.transform.smoothscale(  # لوگوی بازی
    logo,
    (210,210)
    )
    imagez2 = pygame.transform.smoothscale(  # لوگوی بازی
    mode,
    guid_icon
    )

    imagez3 = pygame.transform.smoothscale(# این سمت راستی بالا است 
        pygame.image.load(
            f"asset/image/guide/{online}.png"
        ).convert_alpha(),
        guid_icon
    )

    imagez4 = pygame.transform.smoothscale(
        pygame.image.load(
            f"asset/image/guide/{xp}.png"
        ).convert_alpha(),
        guid_icon
    )

    imagez5 = pygame.transform.smoothscale(
        pygame.image.load(
            f"asset/image/guide/{players}.png"
        ).convert_alpha(),
        guid_icon
    )

    imagez6 = pygame.transform.smoothscale(
        pygame.image.load(
            f"asset/image/guide/{dif}.png"
        ).convert_alpha(),
        guid_icon
    )


    side_images = [

        # =========================
        # TOP
        # =========================

        {
            "image": imagez1, # این وسطی است بالا 
            "x": 1020,
            "y":  186
        },

        {
            "image": imagez2,
            "x": 608,
            "y": 235
        },

        {
            "image": imagez3,
            "x": 1450,
            "y": 230
        },


        # =========================
        # BOTTOM
        # =========================

        {
            "image": imagez4,
            "x": 581,
            "y": 1090
        },

        {
            "image": imagez5,
            "x": 1023,
            "y": 1090
        },

        {
            "image": imagez6,
            "x": 1472,
            "y": 1090
        }
    ]



def guid_sild_effect(
    screen,
    image,
    x,
    y,
    on_draw=None
):

    # =====================================================
    # START TIME
    # =====================================================

    if not hasattr(
        guid_sild_effect,
        "start_time"
    ):

        guid_sild_effect.start_time = (
            pygame.time.get_ticks()
        )

    # =====================================================
    # TIME
    # =====================================================

    now = pygame.time.get_ticks()

    elapsed = (
        now
        - guid_sild_effect.start_time
    )

    duration = 600

    # =====================================================
    # ANIMATION
    # =====================================================

    if elapsed >= duration:

        progress = 1.0

    else:

        progress = (
            elapsed / duration
        )

        progress = (
            1
            - (1 - progress) ** 3
        )

    # =====================================================
    # START POSITION
    # =====================================================

    start_x = (
        screen.get_width()
        + image.get_width()
    )

    # =====================================================
    # MAIN IMAGE
    # =====================================================

    current_x = (
        start_x
        + (x - start_x) * progress
    )

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

    # =====================================================
    # SIDE IMAGES
    # =====================================================

    if side_images:

        for index, item in enumerate(
            side_images
        ):

            delay = index * 170

            if elapsed < delay:
                continue

            side_elapsed = (
                elapsed
                - delay
            )

            if side_elapsed >= duration:

                side_progress = 1.0

            else:

                side_progress = (
                    side_elapsed / duration
                )

                side_progress = (
                    1
                    - (1 - side_progress) ** 3
                )

            side_image = item["image"]

            side_x = item["x"]
            side_y = item["y"]

            current_side_x = (
                start_x
                + (
                    side_x
                    - start_x
                ) * side_progress
            )

            side_rect = (
                side_image.get_rect(
                    center=(
                        int(current_side_x),
                        side_y
                    )
                )
            )

            screen.blit(
                side_image,
                side_rect
            )

    # =====================================================
    # CALLBACK
    # =====================================================

    if on_draw:

        on_draw(
            screen,
            rect
        )


# ============================================================
# RESET
# ============================================================

def reset_window_before_each_game():

    if hasattr(
        guid_sild_effect,
        "start_time"
    ):

        del guid_sild_effect.start_time
    
    
    
    
    
    
    
    
    

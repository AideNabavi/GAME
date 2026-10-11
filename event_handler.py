import pygame
from modules.sound_effect import play_click
import modules.music as music
from modules.sound_effect import *
import modules.screen as  SC
from modules.design import *
from modules.SUPPORT import support as SUP
from modules.MORE import more as MORE
from modules.RECT import corner
# from modules.levels import handle_level_slider_event,update_level_slider
from event_helper import event_click_game
from modules.GAMES import FOLLOW_THAT as FOTHAT
from modules import language
from modules.RECT import score_xp
from modules.RECT import rec_window
from modules.IN_GAME import menu_window
from modules.IN_GAME import utils
from modules.EFFECT import TRANSI
from modules.RECT import rec as recc
from modules import how_to_play
from modules.DAILY import achievement
from modules import ceill_screen
from modules.DAILY import progress
from modules.GAMES import MATCH3 
from modules import operation_screen as OP 
from modules.GAMES import SNAKE 
from modules.GAMES import CONNECT_FOUR 
from modules.GAMES import CHECKERS 
from modules.GAMES import GO 
from modules.SUPPORT import report_bug 
from modules.GAMES import FIND_NUMBER 
from modules.GAMES import FOLLOW_FREE 
from modules import game_mode_scroll 
from modules.EFFECT import side_effect_window  as S_E_W
from modules.IN_GAME import difficulty_selection_menu
from modules.GAMES import PUZZLE 
from modules.GAMES import DOTS_BOX 
from modules.GAMES import MOVE_ARROW as M_ARR
from modules.MORE.INFO import *
from modules.MORE.FAQ import *
from modules  import game_list
from modules.MORE.more_app import *
from modules.GAMES import SORT_NUMBER
from modules.coming_soon import  *
from modules.SUPPORT import feedback as FEED_BACK
from modules.SUPPORT import donate as DONATE
from modules import sound 
from modules.game_mode_scroll import *
from modules.game_mode_scroll import event_vertical_scroll
from modules.EFFECT import side_effect_window as S_E_W
# game mode
from modules.GAMES.MEMORY import *
import modules.GAMES.REPEAT_AFTER_ME as MEM
from modules.GAMES.REPEAT_AFTER_ME import *
from modules.GAMES.SHAPE_COLOR_NAME import *
from modules.GAMES import SHAPE_COLOR_NAME as SCN
import  modules.GAMES.DIRECTION as DIR
import  modules.GAMES.ACTION as ACT
import  modules.GAMES.MIRROR as MIR
import  modules.GAMES.DETECT as DET
from modules.GAMES import FIND_NUMBER  as FNUM
from modules.GAMES.FIND_NUMBER import * 
from modules.GAMES import  FAST as FF
from modules.GAMES import  SIX_60S as SIX
from modules.GAMES import  TRUE_FALSE as TF
from modules.GAMES import  FIND_OPERATOR as FO
from modules.GAMES import  MORE_LESS_EQUAL as MLE
from modules.GAMES import  MATH_GO as MGO
from modules.GAMES import IMAGE_SELECT as IMSE
from modules.GAMES  import THOOZ as TOZ
from modules.GAMES  import HOW_MANY 
from modules.GAMES  import MINESWEEPER 
from modules import before_game 
from modules.GAMES import CHOOSE_IMAGE
from modules.TRANSLATE import policy

from modules.ACCOUNT import account as ACC
from modules import  custom_math as CUS
from modules import  design as DES
from modules.music  import  *
from modules  import  menu
from modules.ACCOUNT import  player_profile as PLAYER
from modules import  typer as TYPER
from modules.GAMES import  FAST as RESE
from modules.SAVE import  popular_game as popular_game
from modules.SAVE import  recent_game as recent_game

from modules.GAMES import CHESS
from modules.GAMES import SUDOKU
from modules.GAMES import WORD
from modules.GAMES import MAZE
from modules.GAMES import MINESWEEPER
from modules.GAMES import MEMORY_HARD

from modules.custom_math import reset_punch_images_animation
from modules.SUPPORT.support import reset_support_animation
from modules.exit import reset_exit_animation
import modules.ACCOUNT.country as CON
import modules.exit as EX
from  modules.MORE.policy import privacy_event
from  modules.MORE.INFO import INFO_event
from  modules import game_overview
from modules import music as MUS
from modules.SAVE import save as SAVE
from modules import start_screen as STS
from modules import mode as MOD
from modules.GAMES import HOW_MANY as HOW

from modules.GAMES import HARD as HARD
from modules.GAMES import MEMORY_GO as MEMGO
from modules.GAMES import DETECT_PRO as DPRO
from modules.GAMES import MATH_GO as MATHGO
from modules.GAMES import FAST_ADD_SUB as FAS
from modules.GAMES import UNBLOCK_CAR 
from modules import button_menu_setting_gamemode
from modules.game_list import *
from modules.mouse import *
from modules.IN_GAME import menu_window as MENU_WINDOW

from modules.game_mode_scroll import (GAME_MODE_60_IMAGE_RECT_FAST,
    GAME_MODE_60_IMAGE_RECT_MATH,
    GAME_MODE_60_IMAGE_RECT_LOGIC,
    GAME_MODE_60_IMAGE_RECT_MEMORY,
    GAME_MODE_60_IMAGE_RECT_DETECTION)
from modules import menu__ as MENU__
from modules.SUPPORT import contact_us as CONTACT


def handle_events(
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
    language_rects,
    selected_profile_image,
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
):
    running = True
    # global fullscreen_
    for event in pygame.event.get():

        # ========================================================
        # QUIT
        # ========================================================

        if event.type == pygame.QUIT:

            running = False


        # ========================================================
        # ESCAPE
        # ========================================================

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False
            


        # ============================================================
        # MAIN GAME LOOP
        # ============================================================

        if event.type == pygame.MOUSEBUTTONDOWN:
            create_click_effect(event.pos)

            # ----------------------------------------------------
            # NAME
            # ----------------------------------------------------

            if PLAYER.input_box.collidepoint(event.pos):

                PLAYER.name_active = True
                PLAYER.email_active = False

                pygame.key.start_text_input()


            # ----------------------------------------------------
            # EMAIL
            # ----------------------------------------------------

            elif PLAYER.email_input_box.collidepoint(event.pos):

                PLAYER.name_active = False
                PLAYER.email_active = True

                pygame.key.start_text_input()


            # ----------------------------------------------------
            # ENTER
            # ----------------------------------------------------

            elif (
                PLAYER.rec_enter is not None
                and PLAYER.rec_enter.collidepoint(event.pos)
            ):

                if (
                    PLAYER.player_name != ""
                    and PLAYER.selected_profile is not None
                ):

                    PLAYER.name_entered = True
                    PLAYER.game_state = "MENU"
            
                    PLAYER.name_active = False
                    PLAYER.email_active = False

                    pygame.key.stop_text_input()

                play_click()


            # ----------------------------------------------------
            # OUTSIDE
            # ----------------------------------------------------

            else:

                PLAYER.name_active = False
                PLAYER.email_active = False

                pygame.key.stop_text_input()


        # ========================================================
        # TEXT INPUT
        # ========================================================

        if event.type == pygame.TEXTINPUT:

            # ----------------------------------------------------
            # NAME
            # ----------------------------------------------------

            if PLAYER.name_active:

                if len(PLAYER.player_name) < 10:

                    for char in event.text:

                        if char.isprintable():

                            if len(PLAYER.player_name) < 10:

                                PLAYER.player_name += char


            # ----------------------------------------------------
            # EMAIL
            # ----------------------------------------------------

            elif PLAYER.email_active:

                allowed = (
                    "abcdefghijklmnopqrstuvwxyz"
                    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                    "0123456789"
                    "@._+-"
                )

                for char in event.text:

                    if char in allowed:

                        PLAYER.player_email += char


        # این برای ریستارت بازی است restart  in the game
        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos = event.pos

            if DES.restart_rec is not None:
                if DES.restart_rec.collidepoint(mouse_pos):

                    restart_OFF_ON_game = True
                          
        # این کد برای منو در بازی است menu in the game
            if DES.exit_rect is not None:
                if DES.exit_rect.collidepoint(mouse_pos):

                    MENU__.menu_in_middle_of_play = True




        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 3:

                x, y = event.pos

                print(
                    f"X = {x}, Y = {y}"
                )



        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_BACKSPACE:

                if PLAYER.name_active:

                    PLAYER.player_name = PLAYER.player_name[:-1]

                elif PLAYER.email_active:

                    PLAYER.player_email = PLAYER.player_email[:-1]


            # ----------------------------------------------------
            # ENTER
            # ----------------------------------------------------

            elif event.key == pygame.K_RETURN:

                if PLAYER.name_active:

                    if (
                        PLAYER.player_name != ""
                        and PLAYER.selected_profile is not None
                    ):

                        PLAYER.name_entered = True
                        PLAYER.game_state = "MENU"

                        PLAYER.name_active = False
                        PLAYER.email_active = False

                        pygame.key.stop_text_input()
                
            
            
            
            
            
            
            
            
            
            
            

            # # -------- وارد کردن اسم --------

            # if not name_entered:

            #     if event.key == pygame.K_BACKSPACE:

            #         player_name = player_name[:-1]


            #     elif event.key == pygame.K_RETURN:

            #         # فقط وقتی اسم و عکس انتخاب شده باشند
            #         if player_name != "" and selected_profile is not None:

            #             name_entered = True
            #             game_state = "MENU"

            #     else:

            #         if len(player_name) < 10:

            #             # جلوگیری از وارد شدن کاراکترهای عجیب
            #             if event.unicode.isprintable():

            #                 player_name += event.unicode



        # ---------------- Mouse ----------------





        # if event.type == pygame.MOUSEWHEEL:
        #     global scroll_y
        #     scroll_y -= event.y * scroll_speed


        #     # محدود کردن اسکرول
        #     scroll_y = max(
        #         0,
        #         min(
        #             scroll_y,
        #             content_height - window_rect.height
        #         )
        #     )





# #---------------------  برای ایمیل است 
# # --------------------- EMAIL ---------------------

# # --------------------- EMAIL ---------------------

#         if event.type == pygame.MOUSEBUTTONDOWN:

#             if PLAYER.email_input_box.collidepoint(event.pos):

#                 PLAYER.email_active = True

#                 pygame.key.start_text_input()

#             else:

#                 PLAYER.email_active = False

#                 pygame.key.stop_text_input()


#         if PLAYER.email_active:

#             PLAYER.player_email, _ = PLAYER.handle_email_input(
#                 event,
#                 PLAYER.player_email
#             )


















        if game_state == "MAZE":
            if event.type == pygame.MOUSEBUTTONDOWN:

                if MENU_WINDOW.button_rects and MENU_WINDOW.button_rects[0].collidepoint(event.pos):
                    game_state = "GAME MODE"
                    MENU_WINDOW.RESET_MENU_WINDOW_EFFECT()
                elif MENU_WINDOW.button_rects and MENU_WINDOW.button_rects[1].collidepoint(event.pos):
                    MENU_WINDOW.RESET_MENU_WINDOW_EFFECT()
                    MAZE.game_state = MAZE.LEVEL_SELECT

                elif MENU_WINDOW.button_rects and MENU_WINDOW.button_rects[2].collidepoint(event.pos):
                    MENU_WINDOW.RESET_MENU_WINDOW_EFFECT()
                    MAZE.restart_maze()



        # -----------------------------
        # MEMORY GAME EVENTS
        # -----------------------------

        if game_state == "MEMORY MATCH":


            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    game_state = "MENU"



            if event.type == pygame.MOUSEBUTTONDOWN:


                mouse_pos = event.pos


                # ارسال کلیک به بازی Memory

                memory_click(mouse_pos)















        #-------------------------------------------
        # این  هم برای مود دایرکشن است 

        if game_state == "DIRECTION":

            if event.type == pygame.KEYDOWN:


                if DIR.finished:

                    continue



                if event.key in DIR.keys:


                    DIR.player = DIR.keys[event.key]


                    if DIR.player == DIR.answer:

                        DIR.score += 1
                        DIR.correct += 1

                    else:

                        DIR.wrong += 1


                    DIR.new_round_DIRECTION()









        if game_state == "NAME":
            CON.country_window,CON.selected_country = CON.country_event(
                event,
                CON.country_button,
                CON.country_rects,
                CON.country_window,
                CON.selected_country
            )







        if game_state == "Contact Us":
            CONTACT.handle_contact_event(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                CONTACT.handle_social_click(
                    event,
                    CONTACT.urls
                )

        if game_state == "Feed Back":
            FEED_BACK.handle_contact_event(event)

        if game_state == "Report Bug":
            report_bug.handle_report_bug_event(event)

        if game_state == "Donate":
            DONATE.handle_donate_event(event)













        if game_state == "REACTION":


            if event.type == pygame.KEYDOWN:


                if event.key == pygame.K_r:

                    ACT.reset_game_ACTION()

            if event.type == pygame.MOUSEBUTTONDOWN:
                global time


                if ACT.state == "ready":


                    ACT.reaction = (
                        time.time()
                        -
                        ACT.click_start
                    )


                    ACT.result = (
                        f"{ACT.reaction*1000:.0f} ms"
                    )


                    ACT.state = "result"




                elif ACT.state == "waiting":


                    ACT.result = "Too Soon!"

                    ACT.state = "result"






















        if game_state == "MIRROR PATTERN":

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:

                    MIR.level = 1

                    MIR.score = 0

                    MIR.grid_size = MIR.START_GRID

                    MIR.game_over = False

                    MIR.new_round()


            if event.type == pygame.MOUSEBUTTONDOWN:

                if not MIR.game_over:

                    cell = MIR.get_clicked_cell(
                        event.pos
                    )

                    if cell is not None:

                        row, col = cell

                        MIR.player_pattern[row][col] = (
                            1 - MIR.player_pattern[row][col]
                        )


                        # آیا همه خانه‌های لازم پر شده؟

                        correct_pattern = MIR.create_mirror(
                            MIR.target_pattern
                        )

                        if MIR.player_pattern == correct_pattern:

                            MIR.check_answer()











        # if game_state == "ABOUT":
        #     # این برای ااسکرول ابوت است 
        #     handle_about_scroll(event)



        # if event.type == pygame.MOUSEBUTTONDOWN:

        #     if event.button == 1:  # کلیک چپ

        #         dragging = True

        #         mouse_start_x = event.pos[0]
        #         mouse_start_y = event.pos[1]



        # elif event.type == pygame.MOUSEBUTTONUP:

        #     if event.button == 1:

        #         dragging = False



        # elif event.type == pygame.MOUSEMOTION:

        #     if dragging:

        #         dx = event.pos[0] - mouse_start_x


        #         camera_x -= dx


        #         mouse_start_x = event.pos[0]

                    
                    
 
        # if event.type == pygame.MOUSEWHEEL:

        #     if game_state == "MORE":

        #         theme_scroll -= event.y * 40


        #         if theme_scroll < 0:
        #             theme_scroll = 0


        #         rows = (
        #             len(theme_images) + 3 - 1
        #         ) // 3


        #         max_scroll = max(
        #             0,
        #             (rows - 0.5) * (200 + 30)
        #         )


        #         if theme_scroll > max_scroll:
        #             theme_scroll = max_scroll
                        
                        
                        
        
                        
                        

        if game_state == "GAME MODE":
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos=event.pos
                for i,rect in enumerate(button_menu_setting_gamemode.select_buttons_setting):
                    if rect.collidepoint(mouse_pos):
                        if  i == 0:
                            game_mode_feature="math"
                            print("logic")
                            TYPER.reset_typing_timer()
                            game_mode_scroll.reset_grid_for_game_mode_zoom_in_effect_zoom()

                        if  i == 1:
                            game_mode_feature="logic"
                            print("memory")
                            TYPER.reset_typing_timer()
                            game_mode_scroll.reset_grid_for_game_mode_zoom_in_effect_zoom()

                        if  i == 2:
                            game_mode_feature="memory"
                            # print("math")
                            TYPER.reset_typing_timer()
                            game_mode_scroll.reset_grid_for_game_mode_zoom_in_effect_zoom()

                        if  i == 3:
                            game_mode_feature="detection"
                            TYPER.reset_typing_timer()
                            print("detection")
                            game_mode_scroll.reset_grid_for_game_mode_zoom_in_effect_zoom()

                        if  i == 4:
                            game_mode_feature="fast"
                            print("fast")
                            TYPER.reset_typing_timer()
                            game_mode_scroll.reset_grid_for_game_mode_zoom_in_effect_zoom()
                            
                        if  i == 5:
                            game_mode_feature="entertainment"
                            print("fast")
                            TYPER.reset_typing_timer()
                            game_mode_scroll.reset_grid_for_game_mode_zoom_in_effect_zoom()

                        
            # MODE GAME -------------------->    
                        
                        

        if game_state == "MATH RUSH":     
            FF.event_FAST_MODE(event)                      
                        
        if game_state ==  "IMAGE RECALL":     

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:
                    DET.restart_game()
                    # print("Game Restarted")

            elif event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:

                    mouse_pos = event.pos

                    if DET.left_rect.collidepoint(mouse_pos):
                        selected = DET.left_image

                    elif DET.right_rect.collidepoint(mouse_pos):
                        selected = DET.right_image

                    else:
                        selected = None

                    if selected is not None:

                        if selected == DET.new_image:

                            DET.score += 1

                            # print("Correct:", DET.score)

                            if DET.first_round:
                                DET.first_round = False

                            DET.old_image = DET.new_image
                            DET.new_image = DET.get_new_image(
                                DET.old_image
                            )

                            if random.choice([True, False]):
                                DET.left_image = DET.old_image
                                DET.right_image = DET.new_image
                            else:
                                DET.left_image = DET.new_image
                                DET.right_image = DET.old_image

                            DET.start_time = time.time()
                            DET.animation_start = time.time()

                        else:

                            DET.lives -= 1

                            # print("Wrong")

                            if DET.lives <= 0:
                                DET.lives = 0
                                DET.game_over = True

                            else:
                                DET.start_time = time.time()
                                DET.animation_start = time.time()                      
                                
        if game_state == "COMPARE NUMBERS":     
            MLE.event_MORE_LESS_EQUAL(event,MLE.option_rects)
            
                                    
        if game_state == "TRUE OR FALSE":     
            
                if event.type == pygame.MOUSEBUTTONDOWN:


                    mouse_pos = pygame.mouse.get_pos()



                    for rect, option in TF.option_rects_F:



                        if rect.collidepoint(mouse_pos):



                            if option == TF.current_question["answer"]:

                                TF.correct_count += 1


                            else:

                                TF.wrong_count += 1



                            TF.question_number += 1



                            TF.current_question = TF.generate_true_false_question(

                                TF.question_number

                            )



                            TF.start_time = pygame.time.get_ticks()





                                    

        # ---------------- FIND OPERATOR ----------------

        if game_state == "RIGHT SIGN":

            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:

                    mouse_pos = event.pos

                    for rect, option in FO.option_rects:

                        if rect.collidepoint(mouse_pos):

                            if option == FO.find_operator_question["answer"]:

                                FO.correct_count += 1

                            else:

                                FO.wrong_count += 1

                            FO.next_question_find_Op()

                            break


                        




        if game_state == "60S":     
            


                if event.type == pygame.MOUSEBUTTONDOWN:


                    mouse_pos = pygame.mouse.get_pos()



                    for rect, option in SIX.option_rects:



                        if rect.collidepoint(

                            mouse_pos

                        ):



                            if option == SIX.question["answer"]:


                                SIX.score += 1



                            else:


                                SIX.wrong += 1



                            SIX.question = SIX.generate_question()


                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                            
        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos = event.pos

            if menu_state == "SUPPORT" and game_state == "MENU":
                if CUS.rec_support_image0.collidepoint(mouse_pos):
                    # print(game_state)
                    game_state = "Contact Us"
                    DES.reset_menu_back_setters()
                    
                elif CUS.rec_support_image1.collidepoint(mouse_pos):
                    game_state = "Feed Back"
                    DES.reset_menu_back_setters()
                elif CUS.rec_support_image2.collidepoint(mouse_pos):
                    game_state = "Donate"
                    DES.reset_menu_back_setters()
                elif CUS.rec_support_image3.collidepoint(mouse_pos):
                    game_state = "Report Bug"
                    DES.reset_menu_back_setters()
                         
                         
                         
                         
                                

                                
                            
                            
#--------------------------------------- HOW_MANY page 3 games👾
        # dt = clock.tick(60) / 1000
        if game_state == "COUNT ITEM":
            HOW.HOW_MANY_EVENT(
                event
            )


#---------------------- HARD 
        if game_state == "MEMORY CALC":
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    running = False

                elif event.key == pygame.K_r and game_over:
                    HARD.reset_game()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if (
                    event.button == 1
                    and HARD.phase == 5
                    and not HARD.game_over
                ):

                    for i, option in enumerate(HARD.options):

                        if HARD.get_option_rect(i).collidepoint(event.pos):

                            HARD.correct = (
                                option["image1"] is HARD.image1
                                and option["image2"] is HARD.image2
                                and option["number1"] == HARD.number1
                                and option["number2"] == HARD.number2
                                and option["operator"] == HARD.operator
                            )

                            if HARD.correct:
                                HARD.score += 100
                            else:
                                HARD.lives -= 1

                            if HARD.lives <= 0:
                                HARD.game_over = True
                            else:
                                HARD.new_round()

                            break

#-------------------- DETECT_PRO
        if game_state == "QUICK DETECT":
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    running = False

                elif event.key == pygame.K_r and DPRO.game_over:
                    DPRO.reset_game(current_width,current_height)

            elif event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1 and not DPRO.game_over:

                    for category, rect in DPRO.buttons:

                        if rect.collidepoint(event.pos):

                            if DPRO.category == DPRO.current_category:
                                DPRO.score += 100
                            else:
                                DPRO.lives -= 1

                            if DPRO.lives <= 0:
                                DPRO.game_over = True
                            else:
                                DPRO.new_round()


                            break

#--------------------------- MEMORY_GO
        if game_state == "NUMBER ORDER":
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    running = False

                elif event.key == pygame.K_r and MEMGO.game_over:
                    MEMGO.reset_game(current_width,current_height)

            elif event.type == pygame.MOUSEBUTTONDOWN:

                if (
                    event.button == 1
                    and not MEMGO.game_over
                    and not MEMGO.show_numbers
                ):

                    mouse = pygame.Vector2(event.pos)

                    for i, (pos, radius) in enumerate(MEMGO.circles):

                        if mouse.distance_to(pos) <= radius:

                            # عدد این دایره
                            clicked_number = MEMGO.numbers[i]

                            # عدد مورد انتظار
                            expected = MEMGO.correct_order[MEMGO.next_index]

                            # درست
                            if clicked_number == expected:

                                MEMGO.score += 100
                                MEMGO.next_index += 1

                                # تمام اعداد انتخاب شدند
                                if MEMGO.next_index == len(MEMGO.correct_order):

                                    MEMGO.level += 1
                                    MEMGO.new_level(current_width,current_height)

                            # غلط
                            else:

                                MEMGO.lives -= 1

                                if MEMGO.lives <= 0:
                                    MEMGO.game_over = True
                                else:
                                    MEMGO.new_level(current_width,current_height)

                            break

                        
                                
                                
                                
        # ----------------------------------------
        # MOVE_ARROW
        # ----------------------------------------
        if game_state == "DIRECTION DETECT":
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:

                        running = False


                    elif event.key == pygame.K_LEFT:

                        M_ARR.answer(
                            "LEFT",
                            current_width,
                            current_height
                        )


                    elif event.key == pygame.K_RIGHT:

                        M_ARR.answer(
                            "RIGHT",
                            current_width,
                            current_height
                        )


                    elif event.key == pygame.K_UP:

                        M_ARR.answer(
                            "UP",
                            current_width,
                            current_height
                        )


                    elif event.key == pygame.K_DOWN:

                        M_ARR.answer(
                            "DOWN",
                            current_width,
                            current_height
                        )







        if game_state == "STATUS":
            print("df")

    
        if game_state == "MENU" or game_state == "SETTING" and menu_state == "PROGRESS":
            # -----------------------------------------
            # CAROUSEL CLICK
            # -----------------------------------------
            if event.type == pygame.MOUSEBUTTONDOWN:
                if utils.setting_button_rect.collidepoint(mouse_pos):
                    rec_window.reset_slide_rect(rec_window.PROGRESS_state)

                menu_state = progress.handle_carousel_click(
                    event,
                    game_list.gamemode_icons,
                    960,
                    100,
                    menu_state
                )

            # -----------------------------------------
            # MATH
            # -----------------------------------------

            if menu_state == "math_progress":
                print("fdsfsd")


            # -----------------------------------------
            # LOGIC
            # -----------------------------------------

            if menu_state == "logic_progress":
                print("fdsfsd")

            # -----------------------------------------
            # MEMORY
            # -----------------------------------------

            if menu_state == "memory_progress":
                print("fdsfsd")

            # -----------------------------------------
            # DETECTION
            # -----------------------------------------

            if menu_state == "detection_progress":
                print("fdsfsd")

            # -----------------------------------------
            # FAST
            # -----------------------------------------

            if menu_state == "fast_progress":
                print("fdsfsd")

            # -----------------------------------------
            # ENTERTAINMENT
            # -----------------------------------------

            if menu_state == "entertainment_progress":
                print("fdsfsd")










    #---------------------------ACHIEVEMENT

        if game_state == "ACHIEVEMENT":

            if event.type == pygame.MOUSEWHEEL:

                achievement.achievement_target_scroll_y -= event.y * 200

                MIN_SCROLL = - 190
                MAX_SCROLL = 2000

                achievement.achievement_target_scroll_y = max(
                    MIN_SCROLL,
                    min(
                        achievement.achievement_target_scroll_y,
                        MAX_SCROLL
                    )
                )
    #--------------------------- MATH CHAIN
        if game_state == "MATH CHAIN":
                if event.type == pygame.KEYDOWN:

                    if MATHGO.state == "PLAY":

                        if event.key == pygame.K_1:

                            MATHGO.answer_question(
                                MATHGO.options[0]
                            )

                        elif event.key == pygame.K_2:

                            MATHGO.answer_question(
                                MATHGO.options[1]
                            )

                        elif event.key == pygame.K_3:

                            MATHGO.answer_question(
                                MATHGO.options[2]
                            )

                        elif event.key == pygame.K_4:

                            MATHGO.answer_question(
                                MATHGO.options[3]
                            )


                if event.type == pygame.MOUSEBUTTONDOWN:

                    if event.button == 1:

                        if MATHGO.state == "PLAY":

                            MATHGO.click_option(
                                event.pos,current_width
                            )








    #--------------------------- MATH RECALL

        if game_state == "MATH RECALL":
                if event.type == pygame.KEYDOWN:

                    # فقط در Game Over
                    if FAS.game_state == FAS.GAME_OVER:

                        if event.key == pygame.K_r:

                            FAS.restart_game()

                # ---------------------------------------------
                # MOUSE
                # ---------------------------------------------
                if event.type == pygame.MOUSEBUTTONDOWN:

                    if FAS.game_state == FAS.ANSWERING:

                        mouse_pos = event.pos

                        __rects = FAS.get_option_rects(current_width,current_height)

                        for i, rect in enumerate(__rects):

                            if rect.collidepoint(mouse_pos):

                                selected = FAS.options[i]

                                # ---------------------------------
                                # CORRECT
                                # ---------------------------------

                                if selected ==FAS.answer:

                                    FAS.score += 1

                                # ---------------------------------
                                # WRONG
                                # ---------------------------------

                                else:

                                    FAS.lives -= 1

                                # ---------------------------------
                                # GAME OVER
                                # ---------------------------------

                                if FAS.lives <= 0:

                                    FAS.game_state = FAS.GAME_OVER

                                else:

                                    FAS.start_round()

                                break





#---------------------------------------- FOLLOW THAT
        if game_state == "MEMORY PATH":
            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:

                    if FOTHAT.state == "PLAY":

                        index = FOTHAT.find_point(
                            event.pos
                        )


                        if index is not None:

                            FOTHAT.select_point(
                                index
                            )


#---------------------------------------- FOLLOW THAT


        # ----------------------------------------------------
        # MOUSE
        # ----------------------------------------------------
        if game_state == "IMAGE SEQUENCE":
            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:

                    if IMSE.state == "PLAYING":

                        IMSE.click_grid(
                            event.pos,
                                current_width,
                                current_height
                        )


        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "CHESS":
                CHESS.event_CHESS(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "NUMBER SLIDE":
                SORT_NUMBER.event_SORT_NUM(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "SUDOKU":
                SUDOKU.event_sudoku(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "HIDDEN WORD":
                WORD.event_WORD(event)
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "MINESWEEPER":
                
                MINESWEEPER.event_MINESWEEPER(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "FIND THE NEW":
                CHOOSE_IMAGE.event_CHOOSE_IMAGE(event)
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "MEMORY RECALL":
                MEMORY_HARD.event(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "MATCH":
                MATCH3.event_MATCH(event)
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "CONNECT 4":
                CONNECT_FOUR.handle_event(event)
                
        if game_state == "SNAKE":
            SNAKE.event_SNAKE(event)
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "UNBLOCK CAR":
                UNBLOCK_CAR.handle_event(event)
                
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "PUZZLE":
                PUZZLE.handle_event(event)
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "CHECKERS":
                CHECKERS.event_checkers(event)
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "DOTS BOXS":
                DOTS_BOX.event_DOT_BOX(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "COLOR FLOW":
                FOLLOW_FREE.event_FOLLOW_FREE(event)
                
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "GO":
                GO.event_GO(event)
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "MINESWEEPER":
                MINESWEEPER.event_MINESWEEPER(event)
                
                
                
        if game_state == "MAZE":
            MAZE.event_MAZE(event)



















        # # ----------------------------------------------------
        # # Mouse
        # # ----------------------------------------------------
        # elif event.type == pygame.MOUSEBUTTONDOWN:

        #     if event.button == 1:

        #         for direction, rect in M_ARR.buttons.items():

        #             if rect.collidepoint(event.pos):

        #                 M_ARR.answer(
        #                     direction,
        #                     current_width,
        #                     current_height
        #                 )

        #                 break    
                                
                        
                        
                        
                        
                        
                        
                        
                                
                                
                                
                                                
                                                
        if game_state == "SETTING" and setting_menu == "SOUND":

            # =========================================================
            # MOUSE BUTTON DOWN
            # =========================================================

            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:

                    # -------------------------------------------------
                    # MUSIC ON / OFF
                    # -------------------------------------------------

                    if (
                        sound.rect_for_music
                        and sound.rect_for_music.collidepoint(event.pos)
                    ):
                        play_click()

                        sound.music_state = 1 - sound.music_state

                        if sound.music_state == 1:
                            pygame.mixer.music.play()
                            pygame.mixer.music.set_volume(
                                sound.music_volume
                            )

                        else:
                            pygame.mixer.music.stop()


                    # -------------------------------------------------
                    # SOUND EFFECT ON / OFF
                    # -------------------------------------------------

                    if (
                        sound.rect_for_sound
                        and sound.rect_for_sound.collidepoint(event.pos)
                    ):
                        play_click()

                        sound.sound_state = 1 - sound.sound_state

                        if sound.sound_state == 1:
                            on_off_sound_effect(1)

                        else:
                            on_off_sound_effect(0)


                    # -------------------------------------------------
                    # MUSIC VOLUME BAR
                    # -------------------------------------------------

                    if (
                        sound.music_bar
                        and sound.music_bar.collidepoint(event.pos)
                    ):

                        sound.dragging_music = True

                        sound.music_volume = (
                            event.pos[0] - sound.music_bar.x
                        ) / sound.music_bar.width

                        sound.music_volume = max(
                            0.0,
                            min(1.0, sound.music_volume)
                        )

                        pygame.mixer.music.set_volume(
                            sound.music_volume
                        )


                    # -------------------------------------------------
                    # SOUND EFFECT VOLUME BAR
                    # -------------------------------------------------

                    if (
                        sound.sound_bar
                        and sound.sound_bar.collidepoint(event.pos)
                    ):

                        sound.dragging_sound = True

                        sound.sound_volume = (
                            event.pos[0] - sound.sound_bar.x
                        ) / sound.sound_bar.width

                        sound.sound_volume = max(
                            0.0,
                            min(1.0, sound.sound_volume)
                        )


            # =========================================================
            # MOUSE MOTION
            # =========================================================

            elif event.type == pygame.MOUSEMOTION:

                # -----------------------------------------------------
                # DRAG MUSIC VOLUME
                # -----------------------------------------------------

                if sound.dragging_music:

                    sound.music_volume = (
                        event.pos[0] - sound.music_bar.x
                    ) / sound.music_bar.width

                    sound.music_volume = max(
                        0.0,
                        min(1.0, sound.music_volume)
                    )

                    pygame.mixer.music.set_volume(
                        sound.music_volume
                    )


                # -----------------------------------------------------
                # DRAG SOUND EFFECT VOLUME
                # -----------------------------------------------------

                if sound.dragging_sound:

                    sound.sound_volume = (
                        event.pos[0] - sound.sound_bar.x
                    ) / sound.sound_bar.width

                    sound.sound_volume = max(
                        0.0,
                        min(1.0, sound.sound_volume)
                    )


            # =========================================================
            # MOUSE BUTTON UP
            # =========================================================

            elif event.type == pygame.MOUSEBUTTONUP:

                if event.button == 1:

                    sound.dragging_music = False
                    sound.dragging_sound = False



















        if game_state == "MISSING NUMBER":

            if event.type == pygame.MOUSEBUTTONDOWN:

                mouse_pos = pygame.mouse.get_pos()

                for rect, option in FNUM.option_rects:

                    if rect.collidepoint(mouse_pos):

                        if option == FNUM.current_question["answer"]:

                            FNUM.correct_count += 1

                        else:

                            FNUM.wrong_count += 1

                        FNUM.next_question()

                        break













#---------------------------------- این برای یان مد بازی است که تکرار بعد از من بکن
        if game_state == "MEMORY PATTERN":
            # print("CURRENT STATE:", game_state)
            if event.type == pygame.KEYDOWN:


                if event.key == pygame.K_r:


                    MEM.level = 1

                    MEM.score = 0

                    MEM.game_over=False

                    MEM.new_round_MIRROR()






            if event.type == pygame.MOUSEBUTTONDOWN:
                global state    
                # print("2222")

                if MEM.state == "answer" and not MEM.game_over:
                    # print("111")


                    mouse = pygame.mouse.get_pos()



                    for i in range(
                        MEM.ROWS*MEM.COLS
                    ):


                        rect = get_rect(i)



                        if rect.collidepoint(mouse):
                            



                            # جلوگیری از دوبار زدن

                            if i not in MEM.selected:


                                MEM.selected.append(i)



                                # خانه اشتباه

                                if i not in MEM.pattern:


                                    MEM.game_over=True

                                    MEM.state="end"




                                # همه درست پیدا شدند

                                elif len(MEM.selected) == len(MEM.pattern):


                                    MEM.score += MEM.level*10

                                    MEM.level += 1


                                    new_round()






                # ==========================================
                #language
                # ==========================================   
        if game_state == "SETTING" and setting_menu == "LANGUAGE": 
            if event.type == pygame.MOUSEBUTTONDOWN:    
                for lang, rect in language_rects:
                    if rect.collidepoint(mouse_pos):
                        play_click()
                        policy.now_language_is_this=language.load_language(lang)
                        # print(policy.now_language_is_this)


#-------------------------------------------------------------- ا ین برای منو است برای صفحه استرات
        if event.type == pygame.MOUSEBUTTONDOWN:

            if game_state == "START":
                result_22 = STS.start_profile_click(
                    event.pos,
                    STS.start_profile_rect,
                    STS.start_guest_rect
                )

                if result_22 == "PROFILE":

                    play_click()
                    STS.current_player_type = "PROFILE"

                    game_state = "MENU"
                    is_guest=False
                    DASHBOARD=True
                elif result_22 == "GUEST":
                    STS.current_player_type = "GUEST"
                    is_guest=True
                    play_click()

                    game_state = "MENU"
                    DASHBOARD=True

#SUPPORT WINDOW  in menu  این همان ساپور ت ۴ تایی در منو است 
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, doz in enumerate(SUP.support_rects):
                if doz.collidepoint(event.pos):
                    if i == 0:
                        game_state = "Contact Us"
                        SUPPORT_window = "Contact Us"   
                        # SUP.reset_window_side_effect()

                    if i == 1:
                        game_state = "Feed Back"

                        SUPPORT_window = "Feed Back"                        
                        SUP.reset_window_side_effect()

                    if i == 2:
                        game_state = "Donate" 

                        SUPPORT_window = "Donate"
                        SUP.reset_window_side_effect()
                        
                    if i == 3:
                        game_state = "Report Bug"

                        SUPPORT_window = "Report Bug"                        
                        SUP.reset_window_side_effect()



        if event.type == pygame.MOUSEBUTTONDOWN:

            if menu_state == "EXIT":

                if EX.yes_rect and EX.yes_rect.collidepoint(event.pos):

                    running = False

                elif EX.no_rect and EX.no_rect.collidepoint(event.pos):

                    menu_state = "یک مقدار الکی "
                    DASHBOARD=True
                    
        
        
        if game_state == "MENU" and menu_state == "GAMES_OR_MATH":
        # for window CUSTOM_MATH
            if event.type == pygame.MOUSEBUTTONDOWN:

                if CUSTOM_MATH:
                    if CUS.punch2_rect.collidepoint(event.pos):

                        game_state = "OPERATION"
                        # CUSTOM_MATH=False
                        menu_state ="االلکی "
                        CUS.reset_punch_images_animation()
                        S_E_W.reset_menu_setting_panel()

                    elif CUS.punch1_rect.collidepoint(event.pos):
                        game_state = "GAME MODE"
                        game_mode_feature="math"
                        TYPER.reset_typing_timer()
                        game_mode_scroll.reset_grid_for_game_mode_zoom_in_effect_zoom()
                        menu_state ="االلکی "
                        CUS.reset_punch_images_animation()
                        # CUSTOM_MATH=False
                        S_E_W.reset_menu_setting_panel()
                        THREE_ICONS=True
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        DONT_LET_CLICK_GAMES_BUTTON_BEFORE_THAT=True
                        ##button_menu_setting_gamemode.reset_animation_button_in_menu_gamemode_setting()

                        continue
        #--------------------DAILY GAME این مال 

        # for window DAILY GAME
        if event.type == pygame.MOUSEBUTTONDOWN:

            if game_state == "MENU" and menu_state == "DAILYGAME_STATUS_PROGRESS_ACHIEVEMENT":

                if CUS.IMG1_REC1.collidepoint(event.pos):

                    game_state = "DAILY GAME"
                    DAILY_BUTTON = "page_1"
                    DES.reset_menu_back_setters()
                    SUP.reset_window_side_effect()
                    SUP.reset_punch_scale_animation_one_image()
                    S_E_W.reset_menu_setting_panel()

                if CUS.IMG1_REC2.collidepoint(event.pos):

                    game_state = "STATUS"
                    DES.reset_menu_back_setters()
                    SUP.reset_window_side_effect()
                    S_E_W.reset_menu_setting_panel()

                if CUS.IMG1_REC4.collidepoint(event.pos):

                    game_state = "ACHIEVEMENT"
                    DES.reset_menu_back_setters()
                    SUP.reset_window_side_effect()
                    S_E_W.reset_menu_setting_panel()
                    # achievement.achievement_trigger=True

                if CUS.IMG1_REC3.collidepoint(event.pos):

                    menu_state = "PROGRESS"
                    menu_state = "math_progress"
                    DES.reset_menu_back_setters()
                    SUP.reset_window_side_effect()
                    S_E_W.reset_menu_setting_panel()


                # if CUS.IMG1_REC1.collidepoint(event.pos):
                #     game_state = "DAILY GAME"
                #     DAILY_BUTTON = "page_2"
                #     DES.reset_menu_back_setters()
                #     SUP.reset_window_side_effect()
                #     SUP.reset_punch_scale_animation_one_image()

















        # if event.type == pygame.MOUSEBUTTONDOWN:

        if game_state == "SETTING" and menu_state == "SETTING" and setting_menu == "MORE":
            if event.type == pygame.MOUSEBUTTONDOWN:

                mouse_pos = event.pos


                if CUS.rec_more_image0.collidepoint(mouse_pos):
                    game_state = "FAQ"
                    DES.reset_menu_back_setters()
                    ##button_menu_setting_gamemode.reset_animation_button_in_menu_gamemode_setting()

                elif CUS.rec_more_image1.collidepoint(mouse_pos):
                    game_state = "INFO"
                    DES.reset_menu_back_setters()
                    ##button_menu_setting_gamemode.reset_animation_button_in_menu_gamemode_setting()

                elif CUS.rec_more_image2.collidepoint(mouse_pos):
                    game_state = "Privacy Policy"
                    DES.reset_menu_back_setters()
                    ##button_menu_setting_gamemode.reset_animation_button_in_menu_gamemode_setting()

                elif CUS.rec_more_image3.collidepoint(mouse_pos):

                    coming_soon_notification(screen, trigger=True)
            






        if game_state == "Privacy Policy":
            privacy_event(event)
        if game_state == "INFO":
            INFO_event(event)
        if game_state == "FAQ":
            FAQ_event(event)
        # if game_state == "more_app":

                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
            # ============================================================
            # DAILY GAME BUTTONS
            # ============================================================
                    
                    
        if event.type == pygame.MOUSEBUTTONDOWN:

            # if game_state == "DAILY GAME":

                # ---------------- PAGE 1 → PAGE 2 ----------------

                if DAILY_BUTTON == "page_1":

                    if SUP.play_page_rec and SUP.back_page_rec is not None:

                        if SUP.play_page_rec.collidepoint(event.pos):

                            DAILY_BUTTON = "GAME"

                            SUP.reset_window_side_effect()
                            SUP.reset_punch_scale_animation_one_image()

                        if SUP.back_page_rec.collidepoint(event.pos):
                            
                            SUP.reset_window_side_effect()
                            SUP.reset_punch_scale_animation_one_image()

                            game_state = "MENU"  
                            menu_state = "DAILYGAME_STATUS_PROGRESS_ACHIEVEMENT"
                # # ---------------- PAGE 2 → GAME ----------------

                # if DAILY_BUTTON == "page_2":

                #     if SUP.play_page_rec and SUP.back_page_rec is not None:

                #         if SUP.play_page_rec.collidepoint(event.pos):

                #             DAILY_BUTTON = "GAME"

                #             SUP.reset_window_side_effect()
                #             SUP.reset_punch_scale_animation_one_image()
                            
                #         if SUP.back_page_rec.collidepoint(event.pos):
                #             DAILY_BUTTON = "page_1"  
                #             SUP.reset_window_side_effect()
                #             SUP.reset_punch_scale_animation_one_image()
































#--------------------------------------------SHAPE_COLOR_NAME
        if game_state == "COLOR MATCH":

            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:

                    mouse = event.pos

                    for i, rect in enumerate(SCN.buttons):

                        if rect.collidepoint(mouse):

                            if i >= len(SCN.options):
                                continue

                            answer = SCN.options[i]

                            # -------------------------
                            # تعیین جواب صحیح
                            # -------------------------

                            if SCN.question == "Text Color?":

                                correct = SCN.word_color

                            elif SCN.question == "Background Color?":

                                correct = SCN.background_color

                            else:

                                correct = SCN.word_text

                            # -------------------------
                            # بررسی جواب
                            # -------------------------

                            if answer == correct:

                                SCN.score += 1
                                SCN.level += 1

                            else:

                                SCN.score -= 1

                            # -------------------------
                            # سؤال جدید
                            # -------------------------

                            SCN.new_question_SHAPE_COLOR_NAME()

                            break













        #------------------ thoz
        if game_state == "THOOZ":
            if event.type == pygame.MOUSEBUTTONDOWN:

                TOZ.event_THOZ(
                        event,
                        current_width
                    )






        # ---------------- GAME MODE EVENT ----------------
        
        if game_state == "MENU"  or game_state == "SETTING":
                    
            recc.right_card_event(event, recc.right_card_state)
            
            corner.corner_card_event(event, corner.right_card_state,1812,1050)
            corner.corner_top_card_event(event, corner.top_right_card_state,1815,15)
            
            # rec.reset_down_card(state)
            recc.start_card_event(
                event,
                recc.start_card_state,
                recc.other_card_state
            )
            menu.target_scroll_y = menu.handle_six_scroll_event(
                event,
                menu_hidden_rect,
                menu.scroll_y,
                370
            )
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i , rec in enumerate(recc.rect_S_P_A):
                    if rec.collidepoint(event.pos):
                        if i == 0 :
                            menu_state ="STATUS"
                        if i == 1 :
                            menu_state ="PROGRESS"
                            TRANSI.start_transition()
                        if i == 2 :
                            game_state ="ACHIEVEMENT"
                if corner.corner_down.collidepoint(event.pos):
                    menu_state ="DONATE"
                if corner.corner_top.collidepoint(event.pos):
                    menu_state ="NOTIFICATION"

                        
        if game_state == "SETTING":

            recc.right_card_event(event, recc.right_card_state)
            corner.corner_card_event(event, corner.right_card_state,1812,1050)
            corner.corner_top_card_event(event, corner.top_right_card_state,1815,15)
            # rec.reset_down_card(state)
            recc.start_card_event(
                event,
                recc.start_card_state,
                recc.other_card_state

            )
            menu.target_scroll_y = menu.handle_six_scroll_event(
                event,
                menu_hidden_rect,
                menu.scroll_y,
                370
            )

        # ---------------- GAME MODE EVENT ----------------

        if game_state == "GAME MODE":
                    
            event_vertical_scroll(
                event,
                screen,game_mode_feature            )








                    
                        
        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:


                if hint_rect_ is not None:

                    print(
"funck"
                    )

                    if hint_rect_.collidepoint(event.pos):

                        print("🔥 HINT CLICKED")
                                
                
                
                # این برای موزیک است 
                
                
                
        if game_state == "SETTING"  and setting_menu == "MUSIC":
            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:

                    for i, rect in music.music_rects.items():

                        if rect.collidepoint(event.pos):

                            play_click()

                            if setting_menu == "MUSIC":

                                if music.current_music != i:

                                    music.play_music(
                                        i,
                                        sound.music_state
                                    )

                            break
                                        
                                        
                            
                            
                            
                            
                            
                            
        if game_state in (
            "GAME MODE",
            "MENU",
            "SETTING",
            "Donate",
            "INFO",
            "FAQ",
            "Contact Us",
            "Feed Back",
            "Report Bug",
            "Privacy Policy",
        ):
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos=event.pos
                if store__button_rect.collidepoint(mouse_pos):
                    game_state="STORE"
                    THREE_ICONS = False

                    print("Store")
                if  call_button_rect.collidepoint(mouse_pos):
                    game_state="DONATE_"
                    THREE_ICONS = False

                    print("donate")
                if  sms_button_rect.collidepoint(mouse_pos):
                    game_state="MESSAGE"
                    THREE_ICONS = False
                    print("message")
           
           
        if game_state == "GAME OVERVIEW": 
            THREE_ICONS = False
            # INFO_event(event)    
            game_overview.GAME_OVERVIEW_event(event)              
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SUP.next_page_rec2 is not None:
                    if SUP.next_page_rec2.collidepoint(event.pos):
                        SUP.reset_window_side_effect()
                        SUP.reset_punch_scale_animation_one_image()

                        game_state = "COUNT_DOWN"

                        DES.reset_menu_back_setters()
                        ##button_menu_setting_gamemode.reset_animation_button_in_menu_gamemode_setting()
                        before_game.reset_window_before_each_game()

                        print("PLAY")


                if SUP.how_to_play_next_button_rec is not None:
                    if SUP.how_to_play_next_button_rec.collidepoint(event.pos):
                        SUP.reset_window_side_effect()
                        SUP.reset_punch_scale_animation_one_image()

                        DES.reset_menu_back_setters()

                        game_state = "HOW TO PLAY"

                        before_game.reset_window_before_each_game()

                        print("NEXT")


                if SUP.pro_rec is not None:
                    if SUP.pro_rec.collidepoint(event.pos):
                        game_state = "BUY_PREMIUM"

                        S_E_W.reset_window_side_effect_MULLTI_WINDOW()

                        print("PRO")


                if SUP.back_page_rec_ is not None:
                    if SUP.back_page_rec_.collidepoint(event.pos):
                        game_state = "GAME MODE"
                        SUP.reset_window_side_effect()
                        SUP.reset_punch_scale_animation_one_image()

                        DES.reset_menu_back_setters()

                        print("BACK")
                                    
                                    

    
        if game_state == "HOW TO PLAY": 
            THREE_ICONS = False                  
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SUP.next_page_rec2 is not None:
                    if SUP.next_page_rec2.collidepoint(event.pos):
                        SUP.reset_window_side_effect()
                        SUP.reset_punch_scale_animation_one_image()

                        game_state = "COUNT_DOWN"

                        DES.reset_menu_back_setters()
                        ##button_menu_setting_gamemode.reset_animation_button_in_menu_gamemode_setting()

                        print("PLAY")
                        
                if SUP.pro_rec is not None:
                    if SUP.pro_rec.collidepoint(event.pos):
                        game_state = "BUY_PREMIUM"

                        S_E_W.reset_window_side_effect_MULLTI_WINDOW()

                        print("PRO")

            
            
                        
        if game_state == "COUNT_DOWN": 
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i,rect in enumerate(difficulty_selection_menu.bottom_rects):
                    if rect.collidepoint(mouse_pos):
                        if i == 0:
                            game_state ="GAME OVERVIEW"
                        if i == 1:
                            if difficulty_selection_menu.sound_on:
                                on_off_sound_effect(0)
                                difficulty_selection_menu.sound_on = False
                                difficulty_selection_menu.sound__line_for_off=True

                            else:
                                on_off_sound_effect(1)
                                difficulty_selection_menu.sound_on = True
                                difficulty_selection_menu.sound__line_for_off=False

                        if i == 2:
                            if difficulty_selection_menu.music_on:
                                pygame.mixer.music.stop()
                                difficulty_selection_menu.music_on = False
                                difficulty_selection_menu.music__line_for_off=True

                            else:
                                pygame.mixer.music.play()
                                difficulty_selection_menu.music_on = True
                                difficulty_selection_menu.music__line_for_off=False
                                
                for i,rect in enumerate(difficulty_selection_menu.difficulty_rects):
                    if rect.collidepoint(mouse_pos):
                        if i == 0:
                            print(before_game.previous_game_state_F)
                            HOW_MANY.HOW_MANY_difficulty("EASY")
                            game_state =before_game.previous_game_state_F
                        if i == 1:
                            HOW_MANY.HOW_MANY_difficulty("MEDIUM")
                            game_state =before_game.previous_game_state_F

                        if i == 2:
                            HOW_MANY.HOW_MANY_difficulty("MEMORY CALC")
                            game_state =before_game.previous_game_state_F

                        
                        
                        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if DES.restart_rec is not None and DES.restart_rec.collidepoint(mouse_pos):
                MENU__.menu_in_middle_of_play = True
                # print(MENU__.menu_in_middle_of_play)
                
                
                
        #----------------- daonte - support_call - store
        if DASHBOARD == True and is_guest == False: 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if  support__button_rect.collidepoint(mouse_pos):
                    # SUPPORT_IS = True
                    game_state="SUPPORT_CALL"
                    DASHBOARD=False

                if  store__button_rect.collidepoint(mouse_pos):
                    # STOR_IS = True
                    game_state="STORE"
                    # print("thisisaiden")
                    DASHBOARD=False

                if  call_button_rect.collidepoint(mouse_pos):
                    # STOR_IS = True
                    game_state="DONATE_"
                    DASHBOARD=False

                if  sms_button_rect.collidepoint(mouse_pos):
                    # STOR_IS = True
                    menu_state="MESSAGE"
                    DASHBOARD=False

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                mouse_pos = event.pos


                        
                # ==========================================
                # انتخاب پروفایل
                # ==========================================
                if game_state == "NAME":

                    for profile_id, rect in profile_rects.items():

                        if rect.collidepoint(mouse_pos):
                            play_click()

                            selected_profile = profile_id

                            selected_image = profile_images[profile_id]
                            selected_profile_image = profile_images[profile_id]
                            

                            # Guest
                            # --------------------------------------------------

                            if selected_profile == 10:

                                PLAYER.player_name = "Guest"
                                is_guest=True
                            # --------------------------------------------------
                            # پروفایل عادی
                            # --------------------------------------------------

                            else:

                                PLAYER.player_name = ""
                                is_guest=False
                    if SC.rec_enter is not None:

                        if SC.rec_enter.collidepoint(mouse_pos):
                            play_click()
                            #----------------- این افکت برای رفت برگشت نوار لاینر منو و ستینگ است مهمه باید دقت کنم 
                            DES.menu_slide_back = False
                            DES.menu_slide_active = True
                            DES.menu_slide_x = None
                            #--------------------
                            


                        # game_state = "START"
                        if SC.rec_enter.collidepoint(event.pos):

                            play_click()

                            # ------------------------------------------------------
                            # GUEST
                            # ------------------------------------------------------

                            if selected_profile == 10:

                                PLAYER.player_name = "Guest"

                                # هیچ چیزی ذخیره نمی‌شود
                                STS.current_player_type = "GUEST"
                                game_state = "MENU"


                            # ------------------------------------------------------
                            # NORMAL PLAYER
                            # ------------------------------------------------------

                            else:
                                STS.current_player_type = "PROFILE"
                                result = SAVE.save_player(
                                    PLAYER.player_email,
                                    PLAYER.player_name,
                                    selected_profile,
                                    CON.selected_country
                                )

                                # print("SAVE RESULT:", result)

                                if result:

                                    game_state = "MENU"
                                    
        
        
                
                
                
                
                # ==========================================
                # back
                # ==========================================
                elif utils.setting_button_rect.collidepoint(mouse_pos):
                    play_click()
                    if game_state == "DIRECTION DETECT":
                        in_game_is_menu_on=True
                        stop_loop=True
                        before_game.previous_game_state_F = "NONE"




                elif back_button_rect.collidepoint(mouse_pos):
                    play_click()

                    if game_state == "SETTING":
                        # game_state = "MENU"

                        DES.menu_slide_back = True
                        DES.menu_slide_active = False
                        CUS.reset_punch_images_animation()
                        MUS.reset_music_side_effect()
                        language.reset_side_effect_language()
                        control_every_button_in_setting_on_or_off="menu"
                        DASHBOARD=True
                        game_state="MENU"
                        S_E_W.reset_menu_setting_panel()
                        ##button_menu_setting_gamemode.reset_animation_button_in_menu_gamemode_setting()

                    elif game_state == "MUSIC":
                        reset_music_side_effect()

                        game_state = "SETTING"

                        DASHBOARD=True


                        

                    elif game_state == "PROFILE":
                        game_state = "SETTING"
                        
                        DASHBOARD=True

                    elif game_state == "TIME":
                        game_state = "CEILL"
                        
                        
                    elif game_state == "GAME MODE":
                        
                        DASHBOARD=False
                        game_state = "MENU" 
                        menu_state = "GAMES_OR_MATH"
                        CUSTOM_MATH = True
                        CUS.reset_punch_images_animation()
                        DONT_LET_CLICK_GAMES_BUTTON_BEFORE_THAT=False
                        #----------------- این افکت برای رفت برگشت نوار لاینر منو و ستینگ است مهمه باید دقت کنم 
                        DES.menu_slide_back = False
                        DES.menu_slide_active = True
                        DES.menu_slide_x = None
                        S_E_W.reset_menu_setting_panel()
                        ##button_menu_setting_gamemode.reset_animation_button_in_menu_gamemode_setting()

                        #--------------------
                    elif game_state == "MORE":
                        game_state = "SETTING"
                        DASHBOARD=True
                        
                    elif game_state == "BUY_PREMIUM":
                        game_state = "MENU"
                        DASHBOARD=True

                        
                        
                    elif game_state == "CEILL":
                        game_state = "OPERATION"
                    elif game_state == "LEADERBOARD":
                        game_state = "MENU"
                        DASHBOARD=True
                        SUP.reset_window_side_effect()
                        
                    elif game_state == "ONLINE":
                        game_state = "MENU"
                        menu_state = "الکی برای پوچ کردن مقدار"
                        DASHBOARD=True
                        SUP.reset_window_side_effect()

                        
                    elif game_state == "MISSING NUMBER":
                        game_state = "GAME OVERVIEW"
                        
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"


                    elif game_state == "GAME OVERVIEW":
                        game_state = "GAME MODE"


                    elif game_state == "SOUND":
                        game_state = "SETTING"
                        DASHBOARD=True

                    elif game_state == "SUPPORT":
                        game_state = "SETTING"
                        DASHBOARD=True

                    elif game_state == "LANGUAGE":
                        language.reset_side_effect_language()
                        game_state = "SETTING"
                        DASHBOARD=True
                        
                    elif game_state == "CEILL":
                        game_state = "OPERATION"
                        
                        
                        
                        
                        
                        
                        
                        
                        
                    elif game_state ==  "IMAGE RECALL":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                        
                    elif game_state == "REACTION":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        

                    elif game_state == "MIRROR PATTERN":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "MEMORY MATCH":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "DIRECTION":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "MEMORY PATTERN":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "COLOR MATCH":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "MATH RUSH":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "MISSING NUMBER":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "SNAKE":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "60S":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "TRUE OR FALSE":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                    
                        
                        
                        
                    elif game_state == "RIGHT SIGN":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "COMPARE NUMBERS":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                    elif game_state == "MATCH":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "DAILY GAME":
                        game_state = "MENU"
                    elif game_state == "STATUS":
                        game_state = "MENU"
                        
                    elif game_state == "ACHIEVEMENT":
                        game_state = "MENU"
                        
                    elif menu_state == "PROGRESS":
                        game_state = "MENU"
                    elif game_state == "PROGRESS":
                        game_state = "MENU"
                        menu_state = "DAILYGAME_STATUS_PROGRESS_ACHIEVEMENT"
                        
                    elif game_state == "COUNT ITEM":
                        game_state = "GAME MODE"
                        
                    elif game_state == "Privacy Policy":
                        game_state = "SETTING"
                        setting_menu = "MORE"
                        CUS.reset_punch_images_animation()
                        SUP.reset_window_side_effect()   
                        S_E_W.reset_window_side_effect()
                        S_E_W.reset_window_side_effect_MULLTI_WINDOW()
                        S_E_W.reset_menu_setting_panel()

                    elif game_state == "How to Play":
                        game_state = "SETTING"
                        setting_menu = "MORE"    
                        S_E_W.reset_menu_setting_panel()

                        CUS.reset_punch_images_animation()
                        SUP.reset_window_side_effect()   
                        S_E_W.reset_window_side_effect()
                        S_E_W. reset_window_side_effect_MULLTI_WINDOW()
                    elif game_state == "INFO":
                        game_state = "SETTING"
                        setting_menu = "MORE"         
                        CUS.reset_punch_images_animation()
                        SUP.reset_window_side_effect()   
                        S_E_W.reset_window_side_effect()
                        S_E_W. reset_window_side_effect_MULLTI_WINDOW()
                        S_E_W.reset_menu_setting_panel()

                    elif game_state == "FAQ":
                        game_state = "SETTING"
                        setting_menu = "MORE"                        
                        CUS.reset_punch_images_animation()
                        SUP.reset_window_side_effect()   
                        S_E_W.reset_window_side_effect()
                        S_E_W. reset_window_side_effect_MULLTI_WINDOW()
      
                        S_E_W.reset_menu_setting_panel()

                        
                    elif game_state == "OPERATION":
                        # game_state = "GAME MODE"
                        game_state = "MENU" 
                        menu_state = "GAMES_OR_MATH"
                        CUSTOM_MATH = True
                        CUS.reset_punch_images_animation()
                    # elif game_state == "GAME MODE":
                    #     # game_state = "GAME MODE"


                        
                        
                        
                        
                    elif game_state == "SUPPORT_CALL":
                        game_state = "MENU"
                        SUP.reset_window_side_effect()

                        
                        
                    elif game_state == "Feed Back":
                        game_state = "MENU"
                        SUP.reset_window_side_effect()                        
                        menu_state = "SUPPORT"
                        CUS.reset_punch_images_animation()
                        S_E_W.reset_window_side_effect_MULLTI_WINDOW()
                        S_E_W.reset_menu_setting_panel()
                        ##button_menu_setting_gamemode.reset_animation_button_in_menu_gamemode_setting()

                    elif game_state == "Report Bug":
                        game_state = "MENU"
                        SUP.reset_window_side_effect()                        
                        menu_state = "SUPPORT"
                        CUS.reset_punch_images_animation()
                        S_E_W.reset_window_side_effect_MULLTI_WINDOW()
                        S_E_W.reset_menu_setting_panel()
                        ##button_menu_setting_gamemode.reset_animation_button_in_menu_gamemode_setting()

                    elif game_state == "Donate":
                        game_state = "MENU"
                        SUP.reset_window_side_effect()   
                        menu_state = "SUPPORT"
                        CUS.reset_punch_images_animation()
                        S_E_W.reset_window_side_effect_MULLTI_WINDOW()
                        S_E_W.reset_menu_setting_panel()
                        ##button_menu_setting_gamemode.reset_animation_button_in_menu_gamemode_setting()

                    elif game_state == "Contact Us":
                        game_state = "MENU"
                        SUP.reset_window_side_effect()                        
                        menu_state = "SUPPORT"
                        CUS.reset_punch_images_animation()
                        S_E_W.reset_window_side_effect_MULLTI_WINDOW()
                        S_E_W.reset_menu_setting_panel()
                        ##button_menu_setting_gamemode.reset_animation_button_in_menu_gamemode_setting()

                        
                        
                    elif game_state == "MINESWEEPER":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "MATH CHAIN":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "IMAGE SEQUENCE":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "MIRROR PATTERN":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "MATH RECALL":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "REACTION":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "DIRECTION":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "MEMORY PATTERN":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "COLOR MATCH":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "MEMORY CALC":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "QUICK DETECT":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        

                        
                    elif game_state == "NUMBER ORDER":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "MATH CHAIN":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "MEMORY PATH":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "OPERATION":
                        menu_state= "GAMES_OR_MATH"
                        game_state = "MENU"
                        
                    elif game_state == "THOOZ":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "UNBLOCK CAR":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "HIDDEN WORD":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "SUDOKU":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                        
                    elif game_state == "HOW TO PLAY":
                        game_state = "GAME OVERVIEW"
                        before_game.reset_window_before_each_game()

                    elif game_state == "Contact Us":
                        game_state = "MENU"
                        menu_state = "SUPPORT"
                        ##button_menu_setting_gamemode.reset_animation_button_in_menu_gamemode_setting()

                    elif game_state == "Feed Back":
                        game_state = "MENU"
                        menu_state = "SUPPORT"
                    elif game_state == "Donate":
                        game_state = "MENU"
                        menu_state = "SUPPORT"
                    elif game_state == "Report Bug":
                        game_state = "MENU"
                        menu_state = "SUPPORT"


                    elif game_state == "DONATE_":
                        game_state = "MENU"
                        menu_state = "MENU"
                        DASHBOARD=True
                        S_E_W.reset_window_side_effect()

                    elif game_state == "STORE":
                        game_state = "MENU"
                        menu_state = "MENU"
                        DASHBOARD=True
                        S_E_W.reset_window_side_effect()

                    elif game_state == "MESSAGE":
                        game_state = "MENU"
                        menu_state = "MENU"
                        DASHBOARD=True
                        S_E_W.reset_window_side_effect()







                    elif game_state == "DOTS BOXS":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "PUZZLE":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "GO":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "CHECKERS":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "COLOR FLOW":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "FIND THE NEW":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                        
                    elif game_state == "MEMORY RECALL":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "MAZE":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "MINESWEEPER":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "CHESS":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "SODOKU":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "NUMBER SLIDE":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "HIDDEN WORD":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"
                        
                    elif game_state == "THOOZ":
                        game_state = "GAME MODE"
                        #------------------ for before game start
                        before_game.before_game_start = True
                        before_game.previous_game_state_F = "NONE"

                  
                # ==========================================
                # in game button
                # ==========================================
                # elif home_button_rect.collidepoint(mouse_pos):   
                #     game_state = "MENU"
   
                # elif askus_button_rect.collidepoint(mouse_pos):  
                #     game_state = "ASK US"
                    
                # elif share_button_rect.collidepoint(mouse_pos):      
                #      game_state = "SHARE"
                    

                            
                # ==========================================
                #exit
                # ==========================================
                # elif music_button.collidepoint(event.pos):

                #     toggle_music()


                # elif effect_button.collidepoint(event.pos):

                #     toggle_effect()
                # ==========================================
                # Select Menu
                # ==========================================
                elif game_state == "MENU":# menu

                    for i, rect in enumerate(menu.item_rects):

                        if rect.collidepoint(mouse_pos):
                            play_click()

                            if i == 0:
                                menu_state = "MENU"
                                game_state = "MENU" # نکته در این جا کلا گیم استیت رو دیگه با چیزی نباید قراد بخاطر   -----------> THREE_ICONS
                                DASHBOARD=True
                                # game_state = "LEVELS"
                                # DAILY_GAME = True
                                # CUSTOM_MATH = False
                                # SUPPORT_MENU = False
                                # EXIT_OK = False
                                # ONLINE_FLAG = False
                                reset_punch_images_animation()
                                SUP.reset_window_side_effect()
                                CUSTOM_MATH = False
                                THREE_ICONS=True
                                #button_menu_setting_gamemode.reset_animation_button_in_menu_gamemode_setting()
                            elif i == 1:
                                menu_state = "GAMES_OR_MATH"
                                game_state ="MENU"
                                DASHBOARD=False
                                CUSTOM_MATH=True
                                CUS.reset_punch_images_animation()
                                SUP.reset_window_side_effect()
                                THREE_ICONS=True


#این برای این بود در اصل من کامنت کردم 
                                # menu_state = "DAILYGAME_STATUS_PROGRESS_ACHIEVEMENT"
                                # DASHBOARD=False
                                # SUP.reset_window_side_effect()
                                # CUSTOM_MATH = False
                                # THREE_ICONS=True

                            elif i == 2:
                                coming_soon_notification(screen, trigger=True)
                                # game_state = "ONLINE"
                                # DASHBOARD=False
                                CUSTOM_MATH = False
                                THREE_ICONS=True

                            elif i == 3:
                                coming_soon_notification(screen, trigger=True)
                                # game_state = "LEADERBOARD"
                                # DASHBOARD=False
                                # CUS.reset_punch_images_animation()
                                CUSTOM_MATH = False
                                THREE_ICONS=True

                            elif i == 4:
                                menu_state = "SETTING"
                                recc.reset_down_card(recc.down_card_state)
                                score_xp.reset_down_card(score_xp.down_card_state)
                                game_state= "SETTING"
                                DES.menu_slide_back = False
                                DES.menu_slide_active = True
                                DES.menu_slide_x = None
                                DASHBOARD=True
                                S_E_W.reset_menu_setting_panel()

                                SUP.reset_punch_scale_animation_one_image()
                                SUP.reset_window_side_effect()
                                CUSTOM_MATH = False
                                THREE_ICONS=True
                                DES.reset_menu_back_setters()
                                #button_menu_setting_gamemode.reset_animation_button_in_menu_gamemode_setting()

                            elif i == 5:
                                menu_state = "SUPPORT"
                                DASHBOARD=False

                                # SUPPORT_MENU = True
                                # CUSTOM_MATH = False
                                # ONLINE_FLAG = False
                                # EXIT_OK = False
                                reset_support_animation()
                                CUS.reset_punch_images_animation()
                                SUP.reset_window_side_effect()
                                CUSTOM_MATH = False
                                THREE_ICONS=True
                            elif i == 6:                            
                                menu_state = "EXIT"
                                DASHBOARD=False
                                SUP.reset_window_side_effect()
                                CUSTOM_MATH = False
                                S_E_W.reset_menu_setting_panel()

                                # EXIT_OK=True
                                # CUSTOM_MATH = False
                                # ONLINE_FLAG = False
                                # SUPPORT_MENU = False
                                reset_exit_animation()
                                THREE_ICONS=False

                            # elif i == 7:


                # ==========================================
                # Settings Menu
                # ==========================================

                elif game_state == "SETTING":

                    for i, rect in enumerate(menu.item_rects_setting):

                        if rect.collidepoint(mouse_pos):
                            play_click()

                            if i == 0:
                                setting_menu = "MUSIC"
                                # game_state ="SETTING"
                                # menu_state ="SETTING"
                                language.reset_side_effect_language()
                                DASHBOARD=False
                                control_every_button_in_setting_on_or_off="music"
                                SUP.reset_window_side_effect()
                                CUS.reset_punch_images_animation()
                                ACC.reset_profile_account_side_effect()

                            elif i == 1:
                                DASHBOARD=False

                                setting_menu = "SOUND"
                                control_every_button_in_setting_on_or_off="sound"
                                reset_music_side_effect()
                                language.reset_side_effect_language()
                                SUP.reset_window_side_effect()
                                CUS.reset_punch_images_animation()
                                ACC.reset_profile_account_side_effect()

                            elif i == 2:
                                DASHBOARD=False

                                setting_menu = "ACCOUNT"
                                control_every_button_in_setting_on_or_off="account"
                                reset_music_side_effect()
                                language.reset_side_effect_language()
                                SUP.reset_window_side_effect()
                                CUS.reset_punch_images_animation()

                            elif i == 3:
                                DASHBOARD=False

                                setting_menu = "LANGUAGE"
                                control_every_button_in_setting_on_or_off="language"
                                reset_music_side_effect()
                                # reset_side_effect_language()
                                SUP.reset_window_side_effect()
                                CUS.reset_punch_images_animation()
                                ACC.reset_profile_account_side_effect()

                            elif i == 4:
                                DASHBOARD=False

                                setting_menu = "MORE"
                                reset_music_side_effect()
                                language.reset_side_effect_language()
                                control_every_button_in_setting_on_or_off="more"
                                ACC.reset_profile_account_side_effect()

                            elif i == 5:
                                ACC.reset_profile_account_side_effect()
                                S_E_W.reset_menu_setting_panel()

                                DASHBOARD=True
                                game_state="MENU"
                                menu_state="الکی "
                                setting_menu="الکی "


   


                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
















                # ==========================================
                # انتخاب عملگر
                # ==========================================

                elif game_state == "OPERATION" :
                    CUSTOM_MATH = False
                    DONT_LET_CLICK_GAMES_BUTTON_BEFORE_THAT = False
                    for op, rect in operator_rects.items():

                        if rect.collidepoint(mouse_pos):
                            play_click()

                            operator = op

                            # operation_selected = True

                            game_state = "CEILL"

                # elif game_state == "THEME":

        
                #     theme_event(event)

                # ==========================================
                # انتخاب سقف عدد
                # ==========================================

                # ==========================================
                # انتخاب سقف عدد
                # ==========================================

                elif game_state == "CEILL":


                    for value, rect in ceill_screen.ceill_button_rects.items():

                        if rect.collidepoint(mouse_pos):
                            play_click()

                            ceill = value


                            game_state = "TIME"





                # ==========================================
                # انتخاب زمان
                # ==========================================

                elif game_state == "TIME":


                    for time, rect in time_button_rects.items():

                        if rect.collidepoint(mouse_pos):
                            play_click()

                            time_limit = time

                            # time_entered = True

                            game_state = "CUSTOM GAME"






                # ==========================================
                # انتخاب جواب بازی
                # ==========================================

                elif game_state == "CUSTOM GAME":


                    for index, data in answer_rects.items():

                        rect, answer = data


                        if rect.collidepoint(mouse_pos):
                            play_click()

                            answer_selected = answer
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                # ==========================================
                # GAME MODE
                # ==========================================

                elif game_state == "GAME MODE" and game_mode_feature == "math":

                    if DONT_LET_CLICK_GAMES_BUTTON_BEFORE_THAT == True:
                        CUSTOM_MATH = False

                    for i, rect in enumerate(GAME_MODE_60_IMAGE_RECT_MATH):

                        if rect.collidepoint(mouse_pos):

                            play_click()

                            if i < 7:
                                # print(before_game.previous_game_state_F)

                                before_game.previous_game_state_F =game_list.math_games[i]
                                before_game.guid_icon_setter_for_eatch_game(before_game.previous_game_state_F)
                                game_state = "GAME OVERVIEW"
                                before_game.reset_window_before_each_game()

                            else:
                                coming_soon_notification(
                                    screen,
                                    trigger=True
                                )
                                
                elif game_state == "GAME MODE" and game_mode_feature == "logic":

                    if DONT_LET_CLICK_GAMES_BUTTON_BEFORE_THAT == True:
                        CUSTOM_MATH = False

                    for i, rect in enumerate(GAME_MODE_60_IMAGE_RECT_LOGIC):

                        if rect.collidepoint(mouse_pos):

                            play_click()

                            if i < 12:
                                before_game.previous_game_state_F =game_list.logic_games[i]
                                before_game.guid_icon_setter_for_eatch_game(before_game.previous_game_state_F)
                                game_state = "GAME OVERVIEW"
                                before_game.reset_window_before_each_game()

                            else:
                                coming_soon_notification(
                                    screen,
                                    trigger=True
                                )
                                
                                
                                
                elif game_state == "GAME MODE" and game_mode_feature == "memory":

                    if DONT_LET_CLICK_GAMES_BUTTON_BEFORE_THAT == True:
                        CUSTOM_MATH = False

                    for i, rect in enumerate(GAME_MODE_60_IMAGE_RECT_MEMORY):

                        if rect.collidepoint(mouse_pos):

                            play_click()

                            if i < 6:

                                before_game.previous_game_state_F =game_list.memory_games[i]
                                before_game.guid_icon_setter_for_eatch_game(before_game.previous_game_state_F)

                                game_state = "GAME OVERVIEW"
                                before_game.reset_window_before_each_game()

                            else:
                                coming_soon_notification(
                                    screen,
                                    trigger=True
                                )
                                
                elif game_state == "GAME MODE" and game_mode_feature == "detection":

                    if DONT_LET_CLICK_GAMES_BUTTON_BEFORE_THAT == True:
                        CUSTOM_MATH = False

                    for i, rect in enumerate(GAME_MODE_60_IMAGE_RECT_DETECTION):

                        if rect.collidepoint(mouse_pos):

                            play_click()

                            if i < 11:

                                before_game.previous_game_state_F =game_list.detection_games[i]
                                before_game.guid_icon_setter_for_eatch_game(before_game.previous_game_state_F)

                                game_state = "GAME OVERVIEW"
                                before_game.reset_window_before_each_game()

                            else:
                                coming_soon_notification(
                                    screen,
                                    trigger=True
                                )
                                
                elif game_state == "GAME MODE" and game_mode_feature == "fast":

                    if DONT_LET_CLICK_GAMES_BUTTON_BEFORE_THAT == True:
                        CUSTOM_MATH = False

                    for i, rect in enumerate(GAME_MODE_60_IMAGE_RECT_FAST):

                        if rect.collidepoint(mouse_pos):

                            play_click()

                            if i < 3:

                                before_game.previous_game_state_F =game_list.fast_games[i]
                                before_game.guid_icon_setter_for_eatch_game(before_game.previous_game_state_F)

                                game_state = "GAME OVERVIEW"
                                before_game.reset_window_before_each_game()

                            else:
                                coming_soon_notification(
                                    screen,
                                    trigger=True
                                )
                                
                elif game_state == "GAME MODE" and game_mode_feature == "entertainment":

                    if DONT_LET_CLICK_GAMES_BUTTON_BEFORE_THAT == True:
                        CUSTOM_MATH = False

                    for i, rect in enumerate(GAME_MODE_60_IMAGE_RECT_ENTERTAINMENT):

                        if rect.collidepoint(mouse_pos):

                            play_click()

                            if i == 0:

                                before_game.previous_game_state_F =game_list.entertainment_games[i]
                                before_game.guid_icon_setter_for_eatch_game(before_game.previous_game_state_F)

                                game_state = "GAME OVERVIEW"
                                before_game.reset_window_before_each_game()

                            else:
                                coming_soon_notification(
                                    screen,
                                    trigger=True
                                )
                                
                                
                                
                                

    return (
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
        selected_profile_image,
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

    )
    
    
    

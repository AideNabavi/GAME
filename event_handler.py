import pygame
from modules.sound_effect import play_click
import modules.music as music
from modules.sound_effect import *
import modules.screen as  SC
from modules.ab import *
from modules.about import handle_about_scroll
from modules.design import *
from modules.theme import *
from modules import support as SUP
from modules import more as MORE
# from modules.levels import handle_level_slider_event,update_level_slider
from event_helper import event_click_game
from modules.MODE import FOLLOW_THAT as FOTHAT

from modules.MODE import MOVE_ARROW as M_ARR
from modules.INFO import *
from modules.FAQ import *
from modules.how_to_play import *
from modules.MODE import SORT_NUMBER

from modules import side_effect_window as S_E_W
# game mode
from modules.MODE.MEMORY import *
import modules.MODE.REPEAT_AFTER_ME as MEM
from modules.MODE.REPEAT_AFTER_ME import *
from modules.MODE.SHAPE_COLOR_NAME import *
from modules.MODE import SHAPE_COLOR_NAME as SCN
import  modules.MODE.DIRECTION as DIR
import  modules.MODE.ACTION as ACT
import  modules.MODE.MIRROR as MIR
import  modules.MODE.DETECT as DET
from modules.MODE import FIND_NUMBER  as FNUM
from modules.MODE.FIND_NUMBER import * 
from modules.MODE import  FAST as FF
from modules.MODE import  SIX_60S as SIX
from modules.MODE import  TRUE_FLASE as TF
from modules.MODE import  FIND_OPERATOR as FO
from modules.MODE import  MORE_LESS_EQUAL as MLE
from modules.MODE import  MATH_GO as MGO
from modules.MODE import IMAGE_SELECT as IMSE
from modules.MODE  import THOOZ as TOZ

from modules.MODE import CHOOSE_IMAGE

from modules import account as ACC
from modules import  custom_math as CUS
from modules import  design as DES
from modules.music  import  *
from modules import  player_profile as PLAYER
from modules import  typer as TYPER
from modules.MODE import  FAST as RESE
from modules.save import  popular_game as popular_game
from modules.save import  recent_game as recent_game

from modules.MODE import CHESS
from modules.MODE import SUDOKU
from modules.MODE import WORD
from modules.MODE import MAZE
from modules.MODE import MINESWEEPER
from modules.MODE import MEMORY_FAST

from modules.custom_math import reset_punch_images_animation
from modules.support import reset_support_animation
from modules.exit import reset_exit_animation
import modules.profile.country as CON
import modules.exit as EX
from  modules.policy import privacy_event
from  modules.INFO import info_event
from modules import music as MUS
from modules import blur as BLU
from modules.save import save as SAVE
from modules import start_screen as STS
from modules import mode as MOD
from modules.MODE import HOW_MANY as HOW

from modules.MODE import HARD as HARD
from modules.MODE import MEMORY_GO as MEMGO
from modules.MODE import DETECT_PRO as DPRO
from modules.MODE import MATH_GO as MATHGO
from modules.MODE import FAST_ADD_SUB as FAS

from modules.game_list import *


from modules import menu__ as MENU__
from modules import contact_us as CONTACT


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
    image_game_mode_page5,
    image_game_mode_page6,
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
    sms_button_rect
    # SUPPORT_IS,
    # STOR_IS
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
                

            # if pygame.key.get_mods() & pygame.K_ESCAPE:
            #     fullscreen_ = not fullscreen_
            #     screen = pygame.display.set_mode(
            #         (1920, 1080),
            #         pygame.FULLSCREEN
            #     )

            # else:

            #     screen = pygame.display.set_mode(
            #         (1000, 800),
            #         pygame.RESIZABLE
            #     )




        # ============================================================
        # MAIN GAME LOOP
        # ============================================================

        if event.type == pygame.MOUSEBUTTONDOWN:

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
        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos = event.pos

            if DES.exit_rect is not None:
                if DES.exit_rect.collidepoint(mouse_pos):

                    MENU__.menu_in_middle_of_play = True







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























        # -----------------------------
        # MEMORY GAME EVENTS
        # -----------------------------

        if game_state == "MEMORY":


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







        if event.type == pygame.MOUSEBUTTONDOWN:
            CONTACT.handle_social_click(
                event,
                CONTACT.urls
            )


        if game_state == "ACTION":


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






















        if game_state == "MIRROR":

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
                        
                        
                        
        
                        
                        
                        
                        
                        
                        
                        
                        
            # MODE GAME -------------------->    
                        
                        

        if game_state == "FAST":     
            FF.event_FAST_MODE(event)                      
                        
        if game_state == "DETECT":     

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:
                    DET.restart_game()
                    print("Game Restarted")

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

                            print("Correct:", DET.score)

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

                            print("Wrong")

                            if DET.lives <= 0:
                                DET.lives = 0
                                DET.game_over = True

                            else:
                                DET.start_time = time.time()
                                DET.animation_start = time.time()                      
                                
        if game_state == "MORE_LESS_EQUAL":     
            MLE.event_MORE_LESS_EQUAL(event,MLE.option_rects)
            
                                    
        if game_state == "TRUE_FALSE":     
            
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

        if game_state == "FIND_OPERATOR":

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

            if menu_state == "SUPPORT":
                if CUS.rec_support_image0.collidepoint(mouse_pos):
                    print(game_state)
                    game_state = "Contact Us"

                elif CUS.rec_support_image1.collidepoint(mouse_pos):
                    game_state = "Feed Back"
                    
                elif CUS.rec_support_image2.collidepoint(mouse_pos):
                    game_state = "Donate"

                elif CUS.rec_support_image3.collidepoint(mouse_pos):
                    game_state = "Report Bug"
                         
                         
                         
                         
                         
                                

                                
                            
                            
#--------------------------------------- HOW_MANY page 3 games👾
        # dt = clock.tick(60) / 1000
        if game_state == "HOW_MANY":
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r and HOW.lives <= 0:
                        HOW.reset_game()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1 and HOW.state == "game":

                    for i, option in enumerate(HOW.options):

                        if HOW.get_option_rect(i,current_width).collidepoint(event.pos):

                            if option == HOW.answer:
                                HOW.score += 100
                            else:
                                HOW.lives -= 1

                            if HOW.lives <= 0:
                                HOW.state = "gameover"
                            else:
                                HOW.new_round()
                            
                        


#---------------------- HARD 
        if game_state == "HARD":
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
        if game_state == "DETECT_PRO":
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
                                DPRO.new_round(current_width, current_height)


                            break

#--------------------------- MEMORY_GO
        if game_state == "MEMORY_GO":
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
        if game_state == "MOVE_ARROW":
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




    #--------------------------- MATH_GO
        if game_state == "MATH_GO":
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








    #--------------------------- FAST_ADD_SUB

        if game_state == "FAST_ADD_SUB":
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
        if game_state == "FOLLOW_THAT":
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
        if game_state == "IMAGE_SELECT":
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
            if game_state == "SORT_NUMBER":
                SORT_NUMBER.event_SORT_NUM(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "SUDOKU":
                SUDOKU.event_sudoku(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "WORD":
                WORD.event_WORD(event)
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "MINESWEEPER":
                
                MINESWEEPER.event_MINESWEEPER(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "CHOOSE_IMAGE":
                CHOOSE_IMAGE.event_CHOOSE_IMAGE(event)
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "MEMORY_FAST":
                CHOOSE_IMAGE.event_MEMORT_FAST(event)

        if game_state == "MAZE":
            MAZE.event_MAZE(event)

















        # ----------------------------------------------------
        # Mouse
        # ----------------------------------------------------

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                for direction, rect in M_ARR.buttons.items():

                    if rect.collidepoint(event.pos):

                        M_ARR.answer(
                            direction,
                            current_width,
                            current_height
                        )

                        break    
                                
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                
        # برای موزیک است با کلیک تغییر میکنه عکس 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "SOUND":
                if rect_for_music.collidepoint(event.pos):
                    play_click()
                    music_state = 1 - music_state

                    if music_state == 1:
                        pygame.mixer.music.play()


                    else:
                        pygame.mixer.music.stop()
                        
                if rect_for_sound.collidepoint(event.pos):
                    play_click()
                    sound_state = 1 - sound_state

                    if sound_state == 1:
                        on_off_sound_effect(1)
                    else:
                        on_off_sound_effect(0)




        if game_state == "FIND_NUMBER":

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









        if game_state == "Privacy Policy":
            privacy_event(event)
        if game_state == "INFO":
            info_event(event)
        if game_state == "FAQ":
            FAQ_event(event)
        if game_state == "How to Play":
            how_to_play_event(event)






#---------------------------------- این برای یان مد بازی است که تکرار بعد از من بکن
        if game_state == "REPEAT_AFTER_ME":
            # print("CURRENT STATE:", game_state)
            if event.type == pygame.KEYDOWN:


                if event.key == pygame.K_r:


                    MEM.level = 1

                    MEM.score = 0

                    MEM.game_over=False

                    MEM.new_round_MIRROR()






            if event.type == pygame.MOUSEBUTTONDOWN:
                global state    
                print("2222")

                if MEM.state == "answer" and not MEM.game_over:
                    print("111")


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
                    
        
        
        
        # for window CUSTOM_MATH
        if event.type == pygame.MOUSEBUTTONDOWN:

            if CUSTOM_MATH:

                if CUS.punch2_rect.collidepoint(event.pos):

                    game_state = "OPERATION"
                    # CUSTOM_MATH=False
                    menu_state ="االلکی "
                    CUS.reset_punch_images_animation()

                elif CUS.punch1_rect.collidepoint(event.pos):

                    game_state = "GAME MODE"
                    menu_state ="االلکی "
                    CUS.reset_punch_images_animation()
                    # CUSTOM_MATH=False


        #--------------------DAILY GAME این مال 

        # for window DAILY GAME
        if event.type == pygame.MOUSEBUTTONDOWN:

            if game_state == "MENU" and menu_state == "DAILY GAME":

                if CUS.IMG1_REC1.collidepoint(event.pos):

                    game_state = "DAILY GAME"
                    DAILY_BUTTON = "page_1"

                    SUP.reset_window_side_effect()
                    SUP.reset_punch_scale_animation_one_image()

                elif CUS.IMG1_REC2.collidepoint(event.pos):

                    game_state = "STATUS"

                    SUP.reset_window_side_effect()






















        # if event.type == pygame.MOUSEBUTTONDOWN:


            if setting_menu == "MORE":
                if CUS.rec_more_image0.collidepoint(mouse_pos):
                    print(game_state)
                    game_state = "How to Play"

                elif CUS.rec_more_image1.collidepoint(mouse_pos):
                    game_state = "FAQ"
                    
                elif CUS.rec_more_image2.collidepoint(mouse_pos):
                    game_state = "INFO"

                elif CUS.rec_more_image3.collidepoint(mouse_pos):
                    game_state = "Privacy Policy"
                                



                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
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
                            menu_state = "DAILY GAME"
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
        if game_state == "SHAPE_COLOR_NAME":

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





#------------- اسلاید  slide.  slid

        # ---------------- GAME MODE EVENT ----------------

        if game_state == "GAME MODE":

            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:

                    drag_start_x_GAME_MODE = event.pos[0]
                    dragging_GAME_MODE = True


            elif event.type == pygame.MOUSEBUTTONUP:

                if event.button == 1 and dragging_GAME_MODE:

                    drag_end_x_GAME_MODE = event.pos[0]
                    print(drag_end_x_GAME_MODE)
                    print(drag_start_x_GAME_MODE)
                    distance = (
                        drag_end_x_GAME_MODE
                        - drag_start_x_GAME_MODE
                    )


                    # -------------------------
                    # رفتن صفحه بعد
                    # Swipe Left
                    # -------------------------

                    if distance < -100:

                        if MOD.current_page_GAME_MODE < 9:

                            MOD.current_page_GAME_MODE += 1

                            game_mode_slide.next()

                            # فقط صفحه فعلی Active باشد
                            MOD.update_game_mode_pages()
                            TYPER.typing_start_time = pygame.time.get_ticks()
                    # -------------------------
                    # برگشت صفحه قبل
                    # Swipe Right
                    # -------------------------

                    elif distance > 100:

                        if MOD.current_page_GAME_MODE > 0:

                            MOD.current_page_GAME_MODE -= 1

                            game_mode_slide.back()
                            # فقط صفحه فعلی Active باشد
                            MOD.update_game_mode_pages()
                            TYPER.typing_start_time = pygame.time.get_ticks()

                    dragging_GAME_MODE = False








                
                
                
                
                                   
                
                
                
                        
        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:


                if hint_rect_ is not None:

                    print(
"funck"
                    )

                    if hint_rect_.collidepoint(event.pos):

                        print("🔥 HINT CLICKED")
                                
                
                
                # این برای موزیک است 
        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                for i, rect in music.music_rects.items():

                    if rect.collidepoint(event.pos):

                        play_click()

                        if game_state == "MUSIC":

                            if music.current_music != i:

                                music.play_music(
                                    i,
                                    music_state
                                )

                        break
                                    
                                    
                            
                            
                            
                            
                            
                            
                            
                            
                # for i, rect in theme_rects:

                #     if rect.collidepoint(event.pos):
                #         play_click()
                #         selected_background = i + 1

                #         print(
                #             "Background selected:",
                #             selected_background
                #         )


        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if DES.restart_rec is not None and DES.restart_rec.collidepoint(mouse_pos):
                MENU__.menu_in_middle_of_play = True
                print(MENU__.menu_in_middle_of_play)
                
                
                
        #----------------- daonte - support_call - store
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if  support__button_rect.collidepoint(mouse_pos):
                # SUPPORT_IS = True
                game_state="SUPPORT_CALL"

            if  store__button_rect.collidepoint(mouse_pos):
                # STOR_IS = True
                game_state="STORE"
            if  call_button_rect.collidepoint(mouse_pos):
                # STOR_IS = True
                game_state="DONATE"
            if  sms_button_rect.collidepoint(mouse_pos):
                # STOR_IS = True
                menu_state="MESSAGE"

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

                                print("SAVE RESULT:", result)

                                if result:

                                    game_state = "MENU"
                                    
        
        
                
                
                
                
                # ==========================================
                # back
                # ==========================================
                elif back_button_rect.collidepoint(mouse_pos):
                    play_click()

                    if game_state == "SETTING":
                        # game_state = "MENU"

                        DES.menu_slide_back = True
                        DES.menu_slide_active = False
                        CUS.reset_punch_images_animation()

                        MUS.reset_music_side_effect()
                        reset_side_effect_language()
                        control_every_button_in_setting_on_or_off="menu"
                        DASHBOARD=True
                        game_state="MENU"
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
                        menu_state = "P_GAME_MODE"
                        CUSTOM_MATH = True
                        CUS.reset_punch_images_animation()
                        
                        #----------------- این افکت برای رفت برگشت نوار لاینر منو و ستینگ است مهمه باید دقت کنم 
                        DES.menu_slide_back = False
                        DES.menu_slide_active = True
                        DES.menu_slide_x = None
                        #--------------------
                    elif game_state == "MORE":
                        game_state = "SETTING"
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

                        
                    elif game_state == "FIND_NUMBER":
                        game_state = "BEFORE_GAMES"
                        
                        

                    elif game_state == "BEFORE_GAMES":
                        game_state = "GAME MODE"


                    elif game_state == "SOUND":
                        game_state = "SETTING"
                        DASHBOARD=True

                    elif game_state == "SUPPORT":
                        game_state = "SETTING"
                        DASHBOARD=True

                    elif game_state == "LANGUAGE":
                        reset_side_effect_language()
                        game_state = "SETTING"
                        DASHBOARD=True
                        
                    elif game_state == "CEILL":
                        game_state = "OPERATION"
                        
                        
                        
                        
                        
                        
                        
                        
                        
                    elif game_state == "DETECT":
                        game_state = "GAME MODE"
                    elif game_state == "ACTION":
                        game_state = "GAME MODE"
                    elif game_state == "MIRROR":
                        game_state = "GAME MODE"
                    elif game_state == "MEMORY":
                        game_state = "GAME MODE"
                    elif game_state == "DIRECTION":
                        game_state = "GAME MODE"
                    elif game_state == "REPEAT_AFTER_ME":
                        game_state = "GAME MODE"
                    elif game_state == "SHAPE_COLOR_NAME":
                        game_state = "GAME MODE"

                    elif game_state == "FAST":
                        game_state = "GAME MODE"
                    elif game_state == "FIND_NUMBER":
                        game_state = "GAME MODE"
                    elif game_state == "60S":
                        game_state = "GAME MODE"
                    elif game_state == "TRUE_FALSE":
                        game_state = "GAME MODE"
                    elif game_state == "FIND_OPERATOR":
                        game_state = "GAME MODE"
                    elif game_state == "MORE_LESS_EQUAL":
                        game_state = "GAME MODE"
                    elif game_state == "DAILY GAME":
                        game_state = "MENU"
                    elif game_state == "STATUS":
                        game_state = "MENU"
                        
                        
                    elif game_state == "HOW_MANY":
                        game_state = "GAME MODE"
                        
                    elif game_state == "Privacy Policy":
                        game_state = "SETTING"
                        setting_menu = "MORE"
                        CUS.reset_punch_images_animation()
                        SUP.reset_window_side_effect()   
                        S_E_W.reset_window_side_effect()
                    elif game_state == "How to Play":
                        game_state = "SETTING"
                        setting_menu = "MORE"    
                        CUS.reset_punch_images_animation()
                        SUP.reset_window_side_effect()   
                        S_E_W.reset_window_side_effect()
                    elif game_state == "INFO":
                        game_state = "SETTING"
                        setting_menu = "MORE"         
                        CUS.reset_punch_images_animation()
                        SUP.reset_window_side_effect()   
                        S_E_W.reset_window_side_effect()
                        
                    elif game_state == "FAQ":
                        game_state = "SETTING"
                        setting_menu = "MORE"                        
                        CUS.reset_punch_images_animation()
                        SUP.reset_window_side_effect()   
                        S_E_W.reset_window_side_effect()
                        
                        
                        
                    elif game_state == "OPERATION":
                        # game_state = "GAME MODE"
                        game_state = "MENU" 
                        menu_state = "P_GAME_MODE"
                        CUSTOM_MATH = True
                        CUS.reset_punch_images_animation()
                
                    # elif game_state == "GAME MODE":
                    #     # game_state = "GAME MODE"


                        
                        
                        
                        
                    elif game_state == "SUPPORT_CALL":
                        game_state = "MENU"
                        SUP.reset_window_side_effect()
                    elif game_state == "STORE":
                        game_state = "MENU"
                        SUP.reset_window_side_effect()
                        
                        
                        
                    elif game_state == "Feed Back":
                        game_state = "MENU"
                        SUP.reset_window_side_effect()                        
                        menu_state = "SUPPORT"
                        CUS.reset_punch_images_animation()

                    elif game_state == "Report Bug":
                        game_state = "MENU"
                        SUP.reset_window_side_effect()                        
                        menu_state = "SUPPORT"
                        CUS.reset_punch_images_animation()

                    elif game_state == "Donate":
                        game_state = "MENU"
                        SUP.reset_window_side_effect()   
                        menu_state = "SUPPORT"
                        CUS.reset_punch_images_animation()

                    elif game_state == "Contact Us":
                        game_state = "MENU"
                        SUP.reset_window_side_effect()                        
                        menu_state = "SUPPORT"
                        CUS.reset_punch_images_animation()

                        
                        
                        
                    elif game_state == "MINESWEEPER":
                        game_state = "GAME MODE"
                    elif game_state == "MIRROR":
                        game_state = "GAME MODE"
                    elif game_state == "FAST_ADD_SUB":
                        game_state = "GAME MODE"
                    elif game_state == "ACTION":
                        game_state = "GAME MODE"
                    elif game_state == "DIRECTION":
                        game_state = "GAME MODE"
                    elif game_state == "REPEAT_AFTER_ME":
                        game_state = "GAME MODE"
                    elif game_state == "SHAPE_COLOR_NAME":
                        game_state = "GAME MODE"
                    elif game_state == "HARD":
                        game_state = "GAME MODE"
                        
                    elif game_state == "DETECT_PRO":
                        game_state = "GAME MODE"
                    elif game_state == "MOVE_ARROW":
                        game_state = "GAME MODE"
                        
                    elif game_state == "MEMORY_GO":
                        game_state = "GAME MODE"
                        
                    elif game_state == "MATH_GO":
                        game_state = "GAME MODE"
                        
                    elif game_state == "FOLLOW_THAT":
                        game_state = "GAME MODE"
                    elif game_state == "OPERATION":
                        menu_state= "P_GAME_MODE"
                        game_state = "MENU"
                        
                    elif game_state == "THOOZ":
                        game_state = "GAME MODE"
                    elif game_state == "WORD":
                        game_state = "GAME MODE"
                        
                    elif game_state == "SUDOKU":
                        game_state = "GAME MODE"
                        
                        
                    elif game_state == "Contact Us":
                        game_state = "MENU"
                        menu_state = "SUPPORT"
                    elif game_state == "Feed Back":
                        game_state = "MENU"
                        menu_state = "SUPPORT"
                    elif game_state == "Donate":
                        game_state = "MENU"
                        menu_state = "SUPPORT"
                    elif game_state == "Report Bug":
                        game_state = "MENU"
                        menu_state = "SUPPORT"









                    elif game_state == "CHOOSE_IMAGE":
                        game_state = "GAME MODE"
                    elif game_state == "MEMORY_FAST":
                        game_state = "GAME MODE"
                    elif game_state == "MAZE":
                        game_state = "GAME MODE"
                    elif game_state == "MINESWEPEER":
                        game_state = "GAME MODE"
                    elif game_state == "CHESS":
                        game_state = "GAME MODE"
                    elif game_state == "SODOKU":
                        game_state = "GAME MODE"
                    elif game_state == "SORT_NUMBER":
                        game_state = "GAME MODE"
                    elif game_state == "WORD":
                        game_state = "GAME MODE"
                    elif game_state == "THOOZ":
                        game_state = "GAME MODE"


                  
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
                #language
                # ==========================================        
                elif game_state == "LANGUAGE":
                    for lang, rect in language_rects:
                        if rect.collidepoint(mouse_pos):
                            play_click()

                            load_language(lang)
                            
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
                    for i, rect in enumerate(select_buttons):

                        if rect.collidepoint(mouse_pos):
                            play_click()

                            if i == 0:
                                menu_state = "MENU"
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
                            elif i == 1:
                                menu_state = "DAILY GAME"
                                DASHBOARD=False
                                SUP.reset_window_side_effect()
                                CUSTOM_MATH = False

                            elif i == 2:
                                menu_state = "P_GAME_MODE"
                                game_state ="MENU"
                                DASHBOARD=False
                                CUSTOM_MATH=True
                                CUS.reset_punch_images_animation()
                                SUP.reset_window_side_effect()

                            elif i == 3:
                                game_state = "ONLINE"
                                DASHBOARD=False
                                CUSTOM_MATH = False

                                # online_state = True
                                # game_state = "PLAY ONLINE"
                                # print("online on the way...")
                                # ONLINE_FLAG = True
                                # reset_flage()
                                # SUPPORT_MENU = False
                                # EXIT_OK = False
                                # CUSTOM_MATH=False
                                # DASHBOARD=True

                            # elif i == 4:# custom game
                            #     menu_state = "CUSTOM_MATH"
                            #     online_state=False
                            #     # CUSTOM_MATH = True
                            #     # SUPPORT_MENU = False
                            #     # EXIT_OK = False
                            #     # ONLINE_FLAG = False
                            #     reset_punch_images_animation()
                            #     DASHBOARD=False
                                CUS.reset_punch_images_animation()

                            elif i == 4:
                                # print("this is aiden")
                                game_state = "LEADERBOARD"
                                DASHBOARD=False
                                CUS.reset_punch_images_animation()
                                CUSTOM_MATH = False

                            elif i == 5:
                                menu_state = "SETTING"
                                game_state= "SETTING"
                                DES.menu_slide_back = False
                                DES.menu_slide_active = True
                                DES.menu_slide_x = None
                                DASHBOARD=True
                                SUP.reset_punch_scale_animation_one_image()
                                SUP.reset_window_side_effect()
                                CUSTOM_MATH = False

                            elif i == 6:                            
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

                            elif i == 7:
                                menu_state = "EXIT"
                                DASHBOARD=False
                                SUP.reset_window_side_effect()
                                CUSTOM_MATH = False

                                # EXIT_OK=True
                                # CUSTOM_MATH = False
                                # ONLINE_FLAG = False
                                # SUPPORT_MENU = False
                                reset_exit_animation()
                # ==========================================
                # Settings Menu
                # ==========================================

                elif game_state == "SETTING":

                    for i, rect in enumerate(settings_rects):

                        if rect.collidepoint(mouse_pos):
                            play_click()

                            if i == 0:
                                setting_menu = "MUSIC"
                                reset_side_effect_language()
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
                                reset_side_effect_language()
                                SUP.reset_window_side_effect()
                                CUS.reset_punch_images_animation()
                                ACC.reset_profile_account_side_effect()

                            elif i == 2:
                                DASHBOARD=False

                                setting_menu = "ACCOUNT"
                                control_every_button_in_setting_on_or_off="account"
                                reset_music_side_effect()
                                reset_side_effect_language()
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
                                reset_side_effect_language()
                                control_every_button_in_setting_on_or_off="more"
                                ACC.reset_profile_account_side_effect()

                            elif i == 5:
                                ACC.reset_profile_account_side_effect()
                                DASHBOARD=True
                                game_state="MENU"
                                menu_state="الکی "


   


                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
















                # ==========================================
                # انتخاب عملگر
                # ==========================================

                elif game_state == "OPERATION":
                    CUSTOM_MATH = False
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


                    for value, rect in ceill_button_rects.items():

                        if rect.collidepoint(mouse_pos):
                            play_click()

                            ceill = value

                            # ceill_entered = True

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


                elif game_state == "BEFORE_GAMES":
                    if SUP.next_page_rec2 and SUP.back_page_rec is not None:
                        if SUP.back_page_rec.collidepoint(event.pos):
                            game_state = "GAME MODE"
                            SUP.reset_window_side_effect()
                            SUP.reset_punch_scale_animation_one_image()
                        if SUP.next_page_rec2.collidepoint(event.pos):
                            SUP.reset_window_side_effect()
                            SUP.reset_punch_scale_animation_one_image()
                            SUP.now_game_start = False
                            game_state = "FIND_NUMBER"
                            FNUM.start_game()
                            # FNUM.reset_game()
                elif game_state == "GAME MODE":
                    CUSTOM_MATH = False

                    if MOD.current_page_GAME_MODE == 0:

                        for i, rect in enumerate(image_game_mode_page1):

                            if rect.collidepoint(mouse_pos):

                                play_click()

                                if i == 0:
                                    game_state = game_1_1
                                    event_click_game(game_state,is_guest)
                                elif i == 1:
                                    game_state = game_1_2
                                    event_click_game(game_state,is_guest)
                                elif i == 2:
                                    game_state = game_1_3
                                    event_click_game(game_state,is_guest,current_width,current_height)
                                elif i == 3:
                                    game_state = game_1_4
                                    event_click_game(game_state,is_guest,current_width,current_height)
                                elif i == 4:
                                    game_state = game_1_5
                                    event_click_game(game_state,is_guest)
                                elif i == 5:
                                    game_state = game_1_6
                                    event_click_game(game_state,is_guest) 
                                    



                    elif MOD.current_page_GAME_MODE == 1:

                        for i, rect in enumerate(image_game_mode_page2):

                            if rect.collidepoint(mouse_pos):

                                play_click()

                                if i == 0:
                                    game_state =game_2_1
                                    event_click_game(game_state,is_guest) 
                                elif i == 1:
                                    game_state =game_2_2
                                    event_click_game(game_state,is_guest) 
                                elif i == 2:
                                    game_state =game_2_3
                                    event_click_game(game_state,is_guest) 
                                elif i == 3:
                                    game_state =game_2_4
                                    event_click_game(game_state,is_guest) 
                                elif i == 4:
                                    game_state =game_2_5
                                    event_click_game(game_state,is_guest) 
                                elif i == 5:
                                    game_state =game_2_6
                                    event_click_game(game_state,is_guest) 

                                    
                    elif MOD.current_page_GAME_MODE == 2:

                        for i, rect in enumerate(image_game_mode_page3):

                            if rect.collidepoint(mouse_pos):

                                play_click()

                                if i == 0:
                                    game_state =game_3_1
                                    event_click_game(game_state,is_guest) 
                                elif i == 1:
                                    game_state =game_3_2
                                    event_click_game(game_state,is_guest) 
                                elif i == 2:
                                    game_state =game_3_3
                                    event_click_game(game_state,is_guest) 
                                elif i == 3:
                                    game_state =game_3_4
                                    event_click_game(game_state,is_guest,current_width,current_height) 
                                elif i == 4:
                                    game_state =game_3_5
                                    event_click_game(game_state,is_guest,current_width,current_height) 
                                elif i == 5:
                                    game_state =game_3_6
                                    event_click_game(game_state,is_guest,current_width,current_height) 

                    elif MOD.current_page_GAME_MODE == 3:

                        for i, rect in enumerate(image_game_mode_page4):

                            if rect.collidepoint(mouse_pos):

                                play_click()

                                if i == 0:
                                    game_state =game_4_1
                                    event_click_game(game_state,is_guest) 
                                if i == 1:
                                    game_state =game_4_2
                                    event_click_game(game_state,is_guest) 
                                if i == 2:
                                    game_state =game_4_3                                    
                                    event_click_game(game_state,is_guest,current_width,current_height) 
                                if i == 3:                                    
                                    game_state =game_4_4
                                    event_click_game(game_state,is_guest) 
                                if i == 4:
                                    game_state =game_4_5
                                    event_click_game(game_state,is_guest) 
                                if i == 5:
                                    game_state =game_4_6
                                    event_click_game(game_state,is_guest) 
                    elif MOD.current_page_GAME_MODE == 4:

                        for i, rect in enumerate(image_game_mode_page5):

                            if rect.collidepoint(mouse_pos):

                                play_click()

                                if i == 0:
                                    game_state =game_5_1
                                    event_click_game(game_state,is_guest) 
                                if i == 1:
                                    game_state =game_5_2
                                    event_click_game(game_state,is_guest) 
                                if i == 2:
                                    game_state =game_5_3
                                    event_click_game(game_state,is_guest) 
                                if i == 3:
                                    game_state =game_5_4
                                    event_click_game(game_state,is_guest) 
                                if i == 4:
                                    game_state =game_5_5
                                    event_click_game(game_state,is_guest) 
                                if i == 5:
                                    game_state =game_5_6
                                    event_click_game(game_state,is_guest) 
                    elif MOD.current_page_GAME_MODE == 5:

                        for i, rect in enumerate(image_game_mode_page6):

                            if rect.collidepoint(mouse_pos):
                   
                                     
                                if i == 0:
                                    game_state =game_6_1
                                    event_click_game(game_state,is_guest) 



    return (
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
        is_guest,
        restart_OFF_ON_game,
        
        
        store__button_rect,
        call_button_rect,
       support__button_rect,
       sms_button_rect
    #    SUPPORT_IS,
    #     STOR_IS
    )
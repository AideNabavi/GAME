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




# game mode
from modules.MODE.MEMORY import *
import modules.MODE.REPEAT_AFTER_ME as MEM
from modules.MODE.REPEAT_AFTER_ME import *
from modules.MODE.SHAPE_COLOR_NAME import *
import  modules.MODE.DIRECTION as DIR
import  modules.MODE.ACTION as ACT
import  modules.MODE.MIRROR as MIR
import  modules.MODE.DETECT as DET
from modules.MODE.FIND_NUMBER import *
from modules.MODE import  FAST as FF
from modules.MODE import  SIX_60S as SIX
from modules.MODE import  TRUE_FLASE as TF
from modules.MODE import  FIND_OPERATOR as FO
from modules.MODE import  MORE_LESS_EQUAL as MLE

from modules import  custom_math as CUS
from modules import  design as DES
from modules.music  import  *
from modules import  player_profile as PLAYER



from modules.custom_math import reset_punch_images_animation
from modules.support import reset_support_animation
from modules.exit import reset_exit_animation
import modules.profile.country as CON
import modules.exit as EX
from  modules.policy import privacy_event
from  modules.INFO import info_event


def handle_events(
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
    exit_button_rect,
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
    current_page_GAME_MODE,
    target_offset_GAME_MODE,
    game_mode_slide,
    image_game_mode_page2,
    image_game_mode_page3,
    image_game_mode_page1,

    
    support_face,SUPPORT_MENU,SUPPORT_window,
    
    EXIT_OK,
    CUSTOM_MATH,
    ONLINE_FLAG,
    DAILY_GAME,
    menu_state,
    DAILY_BUTTON,
    reset_side_effect,
    setting_menu
    # old_screen
):

    running = True

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


        # ========================================================
        # MOUSE CLICK
        # ========================================================

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


        # ========================================================
        # BACKSPACE
        # ========================================================

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



        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:  # کلیک چپ

                dragging = True

                mouse_start_x = event.pos[0]
                mouse_start_y = event.pos[1]



        elif event.type == pygame.MOUSEBUTTONUP:

            if event.button == 1:

                dragging = False



        elif event.type == pygame.MOUSEMOTION:

            if dragging:

                dx = event.pos[0] - mouse_start_x


                camera_x -= dx


                mouse_start_x = event.pos[0]

                    
                    
 
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
                        
        if game_state == "ACTION":     
            DET.event_game_mode_detect(event)                        
                        
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


                mouse_pos = pygame.mouse.get_pos()



                for rect, option in FO.option_rects:



                    if rect.collidepoint(mouse_pos):


                        # جواب درست

                        if option == FO.current_question["answer"]:

                            FO.correct_count += 1


                        # جواب غلط

                        else:

                            FO.wrong_count += 1



                        # سوال بعدی

                        FO.question_number += 1



                        FO.current_question = FO.generate_operator_question(
                            FO.ceill
                        )



                        FO.current_question["time"] = FO.get_question_time(
                            FO.question_number
                        )



                        FO.start_time = pygame.time.get_ticks()



                        




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






        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos = pygame.mouse.get_pos()


            for rect, option in option_rects:

                if rect.collidepoint(mouse_pos):

                    if option == current_question["answer"]:

                        correct_count += 1

                    else:

                        wrong_count += 1



                    question_number += 1


                    current_question = generate_missing_number_question(
                        question_number
                    )


                    start_time = pygame.time.get_ticks()


                    break










        if game_state == "MORE" and support_face == "Privacy Policy":
                privacy_event(event)
        if game_state == "MORE" and support_face == "INFO":
               info_event(event)
            # if event.type == pygame.MOUSEWHEEL:

            #     scroll_y -= event.y * 40


            #     # محدود کردن اسکرول
            #     if scroll_y < 0:
            #         scroll_y = 0


            #     max_scroll = 900

            #     if scroll_y > max_scroll:
            #         scroll_y = max_scroll






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
                        SUPPORT_window = "Contact Us"   
                        SUP.reset_window_side_effect()
                        
                    if i == 1:
                        SUPPORT_window = "Feed Back"                        
                        SUP.reset_window_side_effect()

                    if i == 2:
                        SUPPORT_window = "Donate"
                        SUP.reset_window_side_effect()
                        
                    if i == 3:
                        SUPPORT_window = "Report Bug"                        
                        SUP.reset_window_side_effect()


        # for window EXIT

        if event.type == pygame.MOUSEBUTTONDOWN:

            if menu_state == "EXIT":

                if EX.yes_rect and EX.yes_rect.collidepoint(event.pos):

                    running = False

                elif EX.no_rect and EX.no_rect.collidepoint(event.pos):

                    menu_state = "یک مقدار الکی "

        # for window CUSTOM_MATH
        if event.type == pygame.MOUSEBUTTONDOWN:

            if CUSTOM_MATH:

                if CUS.punch2_rect.collidepoint(event.pos):

                    game_state = "OPERATION"

                elif CUS.punch1_rect.collidepoint(event.pos):

                    CUSTOM_MATH = False


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


            # ============================================================
            # DAILY GAME BUTTONS
            # ============================================================
        if event.type == pygame.MOUSEBUTTONDOWN:

            # if game_state == "DAILY GAME":

                # ---------------- PAGE 1 → PAGE 2 ----------------

                if DAILY_BUTTON == "page_1":

                    if SUP.next_page_rec2 and SUP.back_page_rec is not None:

                        if SUP.next_page_rec2.collidepoint(event.pos):

                            DAILY_BUTTON = "page_2"

                            SUP.reset_window_side_effect()
                            SUP.reset_punch_scale_animation_one_image()

                        if SUP.back_page_rec.collidepoint(event.pos):
                            SUP.reset_window_side_effect()
                            SUP.reset_punch_scale_animation_one_image()

                            game_state = "MENU"  
                            menu_state = "DAILY GAME"
                # ---------------- PAGE 2 → GAME ----------------

                if DAILY_BUTTON == "page_2":

                    if SUP.play_page_rec and SUP.back_page_rec is not None:

                        if SUP.play_page_rec.collidepoint(event.pos):

                            DAILY_BUTTON = "GAME"

                            SUP.reset_window_side_effect()
                            SUP.reset_punch_scale_animation_one_image()
                            
                        if SUP.back_page_rec.collidepoint(event.pos):
                            DAILY_BUTTON = "page_1"  
                            SUP.reset_window_side_effect()
                            SUP.reset_punch_scale_animation_one_image()



































# این برای بازی  انتخاب رنگ چند تایی است 
        if game_state == "SHAPE_COLOR_NAME":

            if event.type == pygame.MOUSEBUTTONDOWN:


                mouse = event.pos



                for i,rect in enumerate(buttons):


                    if rect.collidepoint(mouse):
                        if i >= len(options):
                            continue

                        answer = options[i]



                        if question == "What is the text color?":

                            correct = word_color


                        elif question == "What is the background color?":

                            correct = background_color


                        else:

                            correct = word_text




                        if answer == correct:

                            score += 1

                            level += 1


                        else:

                            score -= 1



                        new_question_SHAPE_COLOR_NAME()











        # ---------------- GAME MODE EVENT ----------------

        if game_state == "GAME MODE":

            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:

                    drag_start_x_GAME_MODE = event.pos[0]
                    dragging_GAME_MODE = True


            elif event.type == pygame.MOUSEBUTTONUP:

                if event.button == 1 and dragging_GAME_MODE:

                    drag_end_x_GAME_MODE = event.pos[0]

                    distance = (
                        drag_end_x_GAME_MODE
                        - drag_start_x_GAME_MODE
                    )


                    # -------------------------
                    # رفتن صفحه بعد
                    # Swipe Left
                    # -------------------------

                    if distance < -100:

                        if current_page_GAME_MODE < 5:

                            current_page_GAME_MODE += 1

                            game_mode_slide.next()


                    # -------------------------
                    # برگشت صفحه قبل
                    # Swipe Right
                    # -------------------------

                    elif distance > 100:

                        if current_page_GAME_MODE > 0:

                            current_page_GAME_MODE -= 1

                            game_mode_slide.back()


                    dragging_GAME_MODE = False





        # # ---------------- GAME MODE EVENT ----------------

        # if game_state == "GAME MODE":


        #     if event.type == pygame.MOUSEBUTTONDOWN:

        #         if event.button == 1:

        #             drag_start_x_GAME_MODE = event.pos[0]

        #             dragging_GAME_MODE = True



        #     elif event.type == pygame.MOUSEBUTTONUP:


        #         if event.button == 1 and dragging_GAME_MODE:


        #             drag_end_x_GAME_MODE = event.pos[0]


        #             distance = (
        #                 drag_end_x_GAME_MODE
        #                 -
        #                 drag_start_x_GAME_MODE
        #             )



        #             # -------------------------
        #             # رفتن به صفحه بعد (کشیدن چپ)
        #             # -------------------------

        #             if distance < -100:


        #                 if current_page_GAME_MODE < 4:


        #                     current_page_GAME_MODE += 1


        #                     game_mode_slide.next()



        #             # -------------------------
        #             # برگشت صفحه قبل (کشیدن راست)
        #             # -------------------------

        #             elif distance > 100:


        #                 if current_page_GAME_MODE > 0:


        #                     current_page_GAME_MODE -= 1


        #                     game_mode_slide.back()



        #             dragging_GAME_MODE = False









                
                
                
                
                
                
                
                
                
                
                
                

# این برای مپ لول ها است اون ۱۰ تا 
        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:
                if game_state == "LEVELS":

                    mouse_x, mouse_y = event.pos


                    # تبدیل مختصات صفحه به مختصات World
                    world_x = mouse_x + camera_x
                    world_y = mouse_y + camera_y


                    for level_number, rect in level_rects:

                        if rect.collidepoint(
                            world_x,
                            world_y
                        ):
                            play_click()
                            if level_number == 1:
                                game_state="level_1"
                            
                            if level_number == 2:
                                game_state="level_2"
                            
                            if level_number == 3:
                                game_state="level_3"
                            
                            if level_number == 4:
                                game_state="level_4"
                            
                            if level_number == 5:
                                game_state="level_5"
                            
                            if level_number == 6:
                                game_state="level_6"
                            
                            if level_number == 7:
                                game_state="level_7"
                            
                            if level_number == 8:
                                game_state="level_8"
                            
                            if level_number == 9:
                                game_state="level_9"
                            
                            if level_number == 10:
                                game_state="level_10"
                            
                            
                                
        # if event.type == pygame.MOUSEBUTTONDOWN:

        #     if event.button == 1:

        #         clicked_button = False


        #         # گالری
        #         if gallery_button_rect.collidepoint(event.pos):

        #             clicked_button = True

        #             if small_window == "gallery":
        #                 small_window = None
        #             else:
        #                 small_window = "gallery"



        #         # # Donate
        #         # elif donate_button_rect.collidepoint(event.pos):

        #         #     clicked_button = True

        #         #     if small_window == "donate":
        #         #         small_window = None
        #         #     else:
        #         #         small_window = "donate"



        #         # کلیک جای دیگر
        #         if not clicked_button:

        #             small_window = None                
                        
                
                
                
                        
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
                        if game_state =="MUSIC":
                            if music.current_music != i:

                                music.play_music(i,music_state)

                                music.current_music = i
                                
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                # for i, rect in theme_rects:

                #     if rect.collidepoint(event.pos):
                #         play_click()
                #         selected_background = i + 1

                #         print(
                #             "Background selected:",
                #             selected_background
                #         )





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
                            

                    if SC.rec_enter is not None:

                        if SC.rec_enter.collidepoint(mouse_pos):
                            play_click()

                            game_state = "MENU"
                            #----------------- این افکت برای رفت برگشت نوار لاینر منو و ستینگ است مهمه باید دقت کنم 
                            DES.menu_slide_back = False
                            DES.menu_slide_active = True
                            DES.menu_slide_x = None
                            #--------------------
                # ==========================================
                # back
                # ==========================================
                elif back_button_rect.collidepoint(mouse_pos):
                    play_click()

                    if game_state == "SETTING":
                        # game_state = "MENU"

                        DES.menu_slide_back = True
                        DES.menu_slide_active = False

                    elif game_state == "MUSIC":
                        reset_music_side_effect()

                        game_state = "SETTING"


                    elif game_state == "ABOUT":
                        game_state = "SETTING"
                        
                        

                    elif game_state == "PROFILE":
                        game_state = "SETTING"
                        
                        
                    elif game_state == "TIME":
                        game_state = "CEILL"
                        
                        
                    elif game_state == "GAME MODE":
                        game_state = "MENU"
                        #----------------- این افکت برای رفت برگشت نوار لاینر منو و ستینگ است مهمه باید دقت کنم 
                        DES.menu_slide_back = False
                        DES.menu_slide_active = True
                        DES.menu_slide_x = None
                        #--------------------
                    elif game_state == "MORE":
                        game_state = "SETTING"
                        
                        
                        
                    elif game_state == "CEILL":
                        game_state = "OPERATION"
                        
                    elif game_state == "FIND_NUMBER":
                        game_state = "BEFORE_GAMES"
                        
                        
                    elif game_state == "LEADER BOARD":
                        game_state = "MENU"
                    elif game_state == "BEFORE_GAMES":
                        game_state = "GAME MODE"


                    elif game_state == "SOUND":
                        game_state = "SETTING"
                        
                    elif game_state == "SUPPORT":
                        game_state = "SETTING"
                        
                    elif game_state == "LANGUAGE":
                        reset_side_effect()
                        game_state = "SETTING"
                        


                    elif game_state == "LEVELS":
                        game_state = "MENU"


                    elif game_state == "OPERATION":
                        game_state = "MENU"
                        
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
                    elif game_state == "DETECT":
                        game_state = "GAME MODE"
                    elif game_state == "FAST":
                        game_state = "GAME MODE"
                    elif game_state == "FIND_NUMBER":
                        game_state = "GAME MODE"
                    elif game_state == "60S":
                        game_state = "GAME MODE"
                    elif game_state == "MORE_LESS_EQUAL":
                        game_state = "GAME MODE"
                    elif game_state == "DAILY GAME":
                        game_state = "MENU"
                    elif game_state == "STATUS":
                        game_state = "MENU"

                    for i in range(1, 11):
                        if game_state == f"level_{i}":
                            game_state = "LEVELS"
                            break

                  
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
                                menu_state = "DAILY GAME"
                                # game_state = "LEVELS"
                                # DAILY_GAME = True
                                # CUSTOM_MATH = False
                                # SUPPORT_MENU = False
                                # EXIT_OK = False
                                # ONLINE_FLAG = False
                                reset_punch_images_animation()
                                
                            elif i == 1:
                                menu_state = "GAMES"

                                game_state = "GAME MODE"
                            elif i == 2:
                                menu_state = "ONLINE"

                                # game_state = "PLAY ONLINE"
                                print("online on the way...")
                                # ONLINE_FLAG = True
                                reset_flage()
                                # SUPPORT_MENU = False
                                # EXIT_OK = False
                                # CUSTOM_MATH=False
                                
                            elif i == 3:# custom game
                                menu_state = "CUSTOM_MATH"

                                # CUSTOM_MATH = True
                                # SUPPORT_MENU = False
                                # EXIT_OK = False
                                # ONLINE_FLAG = False
                                reset_punch_images_animation()


                            elif i == 4:
                                menu_state = "SETTING"
                                game_state= "SETTING"
                                DES.menu_slide_back = False
                                DES.menu_slide_active = True
                                DES.menu_slide_x = None
                            
                            elif i == 5:
                                menu_state = "SUPPORT"

                                # SUPPORT_MENU = True
                                # CUSTOM_MATH = False
                                # ONLINE_FLAG = False
                                # EXIT_OK = False
                                reset_support_animation()

                            elif i == 6:
                                menu_state = "EXIT"

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
                                # game_state = "MUSIC"
                                setting_menu = "MUSIC"
                                reset_side_effect()
                            elif i == 1:
                                # game_state = "SOUND"
                                setting_menu = "SOUND"

                                reset_music_side_effect()
                                reset_side_effect()
                            elif i == 2:
                                setting_menu = "ACCOUNT"

                                # صفحه فعلی = SETTING
                                # old_screen = screen.copy()
                                setting_menu = "PROFILE"
                                reset_music_side_effect()
                                reset_side_effect()

                            elif i == 3:
                                setting_menu = "LANGUAGE"
                                # game_state = "LANGUAGE"
                                # reset_music_side_effect()
                                # reset_side_effect()
                            elif i == 4:
                                setting_menu = "MORE"

                                # game_state = "MORE"
                                reset_music_side_effect()
                                reset_side_effect()



   


                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                elif game_state == "SUPPORT":
                     for i, rect in enumerate(SUP.support_rects):# چون انومریت دو تا مقدار بر میگدون ه برای همنی ما دو تا مقدار میگیری م 
                        if rect.collidepoint(mouse_pos):
                            if i == 0 : 
                                support_face = "Contact Us"
                            if i == 1 : 
                                support_face = "Feed Back"
                            if i == 2 : 
                                support_face = "Donate" 
                            if i == 3: 
                                support_face = "Report Bug"




                elif game_state == "MORE":
                     for i, rect in enumerate(MORE.support_rects):# چون انومریت دو تا مقدار بر میگدون ه برای همنی ما دو تا مقدار میگیری م 
                        if rect.collidepoint(mouse_pos):
                            if i == 0 : 
                                support_face = "How to Play"
                            if i == 1 : 
                                support_face = "FAQ" 
                            if i == 2 : 
                                support_face = "INFO" 
                            if i == 3: 
                                support_face = "Privacy Policy" 












                # ==========================================
                # انتخاب عملگر
                # ==========================================

                elif game_state == "OPERATION":


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
                elif game_state == "GAME MODE":


                    if current_page_GAME_MODE == 0:

                        for i, rect in enumerate(image_game_mode_page1):

                            if rect.collidepoint(mouse_pos):

                                play_click()

                                if i == 0:
                                    game_state = "SHAPE_COLOR_NAME"
                                    # start_memory_game()
                                    new_question_SHAPE_COLOR_NAME()
                                    # one____(screen,current_width,current_height)
                                    
                                    
                                elif i == 1:
                                    game_state = "REPEAT_AFTER_ME"
                                    new_round()
                                    
                                elif i == 2:
                                    game_state = "DIRECTION"
                                    DIR.new_round_DIRECTION()
                                    
                                elif i == 3:
                                    game_state = "MEMORY"
                                    start_memory_game()

                                elif i == 4:
                                    game_state = "MIRROR"
                                    MIR.new_round_MIRROR()
                                elif i == 5:
                                    game_state = "ACTION"
                                    ACT.reset_game_ACTION()
                                    
                                    
                                    



                    elif current_page_GAME_MODE == 1:

                        for i, rect in enumerate(image_game_mode_page2):

                            if rect.collidepoint(mouse_pos):

                                play_click()

                                if i == 0:
                                    game_state ="DETECT"


                                elif i == 1:
                                    game_state = "BEFORE_GAMES"

                                elif i == 2:
                                    game_state = "MORE_LESS_EQUAL"

                                elif i == 3:
                                    game_state = "60S"
                                    SIX.start_game()
                                    
                                elif i == 4:
                                    game_state = "FIND_OPERATOR"
                                    FO.start_game_find_Op()
                                elif i == 5:
                                    game_state = "TRUE_FALSE"
                                    TF.start_game_TRUE_FALSE()
                                    
                                    
                    elif current_page_GAME_MODE == 2:

                        for i, rect in enumerate(image_game_mode_page3):

                            if rect.collidepoint(mouse_pos):

                                play_click()

                                if i == 0:
                                    game_state ="FAST"


                                elif i == 1:
                                    # game_state = "NA"
                                    print("lock")
                                elif i == 2:
                                    # game_state = "NA"
                                    print("lock")

                                elif i == 3:
                                    # game_state = "NA"
                                    print("lock")

                                elif i == 4:
                                    # game_state = "NA"
                                    print("lock")

                                elif i == 5:
                                    # game_state = "NA"
                                    print("lock")




    return (
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
        home_button_rect,askus_button_rect,share_button_rect,
        
        
        
        option_rects,
        
    
        start_time,
        current_question,
        correct_count,
        wrong_count,
        question_number,
        
        
        
        
        
        
        # selected_background,
        
        dragging_GAME_MODE,
        drag_start_x_GAME_MODE,
        current_page_GAME_MODE,
        target_offset_GAME_MODE,
        
        
        support_face,
        SUPPORT_MENU,SUPPORT_window,
        
        EXIT_OK,
        CUSTOM_MATH,
        ONLINE_FLAG,
        DAILY_GAME,
        menu_state,
        DAILY_BUTTON,
        setting_menu
        # old_screen
    )


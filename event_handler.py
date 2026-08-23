import pygame
from modules.sound_effect import play_click
import modules.music as music
from modules.sound_effect import *
# from modules.TrueFalseMode.ImageLoader import image_game_mode
# from modules.window import *
import modules.screen as  SC
from modules.ab import *
from modules.design import *
from modules.theme import *
from modules.DATA import *
from modules.MODE.find_numbers import *
# from modules.levels import handle_level_slider_event,update_level_slider

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
    # selected_color,
    # hue_bar,
    # dragging_hue,
    exit_button_rect,
    # gallery_button_rect,
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
    rect_for_sound,home_button_rect,askus_button_rect,share_button_rect,
    
    
    
    
    
    
    
    
    
    
    
    
    option_rects,
    generate_missing_number_question,
    
    
    
    start_time,
    current_question,
    correct_count,
    wrong_count,
    question_number    ,
    
    
    
    selected_background
):


    running = True

    for event in pygame.event.get():

        # ---------------- Quit ----------------

        if event.type == pygame.QUIT:

            running = False


        # ---------------- Keyboard ----------------

        if event.type == pygame.KEYDOWN:

            # خروج
            if event.key == pygame.K_ESCAPE:

                running = False


            # -------- وارد کردن اسم --------

            if not name_entered:

                if event.key == pygame.K_BACKSPACE:

                    player_name = player_name[:-1]


                elif event.key == pygame.K_RETURN:

                    # فقط وقتی اسم و عکس انتخاب شده باشند
                    if player_name != "" and selected_profile is not None:

                        name_entered = True
                        game_state = "MENU"

                else:

                    if len(player_name) < 10:

                        # جلوگیری از وارد شدن کاراکترهای عجیب
                        if event.unicode.isprintable():

                            player_name += event.unicode



        # ---------------- Mouse ----------------




        if event.type == pygame.MOUSEWHEEL:
            global scroll_y
            scroll_y -= event.y * scroll_speed


            # محدود کردن اسکرول
            scroll_y = max(
                0,
                min(
                    scroll_y,
                    content_height - window_rect.height
                )
            )


        # # ---------------------------------
        # # حرکت موس هنگام نگه داشتن
        # # ---------------------------------

        # if event.type == pygame.MOUSEMOTION:


        #     if dragging_hue:


        #         mouse_x = event.pos[0]


        #         mouse_x = max(
        #             hue_bar.x,
        #             min(mouse_x, hue_bar.right)
        #         )


        #         hue = (
        #             mouse_x - hue_bar.x
        #         ) / hue_bar.width


        #         color = pygame.Color(0)

        #         color.hsva = (
        #             hue * 360,
        #             100,
        #             100,
        #             100
        #         )


        #         selected_color = color



        # # ---------------------------------
        # # رها کردن موس
        # # ---------------------------------

        # if event.type == pygame.MOUSEBUTTONUP:


        #     if event.button == 1:

        #         dragging_hue = False
            
                
                
        

                    








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

                    
                    
 
        if event.type == pygame.MOUSEWHEEL:

            if game_state == "MORE":

                theme_scroll -= event.y * 40


                if theme_scroll < 0:
                    theme_scroll = 0


                rows = (
                    len(theme_images) + 3 - 1
                ) // 3


                max_scroll = max(
                    0,
                    (rows - 0.5) * (200 + 30)
                )


                if theme_scroll > max_scroll:
                    theme_scroll = max_scroll
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                
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






# # این برای تغییر بک گراند است 

#         if event.type == pygame.MOUSEBUTTONDOWN:

#             if event.button == 1:
#                 if game_state == "THEME":

#                     mouse_x, mouse_y = event.pos


#                     # تبدیل مختصات صفحه به مختصات World
#                     world_x_ = mouse_x + camera_x
#                     world_y_ = mouse_y + camera_y


#                     for theme_change,i, rect in level_rects_for_theme,level_images_theme:

#                         if rect.collidepoint(
#                             world_x_,
#                             world_y_
#                         ):
#                             if theme_change == 1:
#                                 selected_background = level_images_theme[i]




        # if event.type == pygame.MOUSEBUTTONDOWN:

        #     if event.button == 1:

        #         if game_state == "THEME":

        #             mouse_x, mouse_y = event.pos

        #             # Screen → World
        #             world_x = mouse_x + camera_x
        #             world_y = mouse_y + camera_y

        #             for index, rect in level_rects_for_theme:

        #                 if rect.collidepoint(world_x, world_y):

        #                     selected_background = level_images_theme[index]
        #                     # print("Background selected:", index + 1)


        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                if game_state == "THEME":

                    mouse_x, mouse_y = event.pos

                    # Screen → World
                    world_x = mouse_x + camera_x
                    world_y = mouse_y + camera_y

                    for index, rect in level_rects_for_theme:

                        if rect.collidepoint(
                            world_x,
                            world_y
                        ):

                            selected_background = level_images_theme[index]

                    # print("Background selected:", index + 1)


        # if event.type == pygame.MOUSEBUTTONDOWN:

        #     if event.button == 1:

        #         if game_state == "THEME":

        #             mouse_x, mouse_y = event.pos


        #             # Screen -> World
        #             world_x = mouse_x + camera_x
        #             world_y = mouse_y + camera_y


        #             for index, rect in level_rects_for_theme:

        #                 if rect.collidepoint(
        #                     world_x,
        #                     world_y
        #                 ):

        #                     selected_background = level_images_theme[index]



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
                # ==========================================
                # back
                # ==========================================
                elif back_button_rect.collidepoint(mouse_pos):
                    play_click()

                    if game_state == "SETTING":
                        game_state = "MENU"



                    elif game_state == "MUSIC":
                        game_state = "SETTING"


                    elif game_state == "ABOUT":
                        game_state = "SETTING"
                        
                        

                    elif game_state == "PROFILE":
                        game_state = "SETTING"
                        
                        
                    elif game_state == "TIME":
                        game_state = "CEILL"
                        
                        
                    elif game_state == "GAME MODE":
                        game_state = "MENU"
                        
                        
                        
                    elif game_state == "CEILL":
                        game_state = "OPERATION"
                        
                        
                    elif game_state == "LEADER BOARD":
                        game_state = "MENU"


                    elif game_state == "SOUND":
                        game_state = "SETTING"
                        
                    elif game_state == "SUPPORT":
                        game_state = "SETTING"
                        
                    elif game_state == "LANGUAGE":
                        game_state = "SETTING"
                        
                    elif game_state == "THEME":
                        game_state = "SETTING"


                    elif game_state == "LEVELS":
                        game_state = "MENU"


                    elif game_state == "OPERATION":
                        game_state = "MENU"
                        
                    elif game_state == "CEILL":
                        game_state = "OPERATION"

                    for i in range(1, 11):
                        if game_state == f"level_{i}":
                            game_state = "LEVELS"
                            break

                  
                # ==========================================
                # in game button
                # ==========================================
                elif home_button_rect.collidepoint(mouse_pos):   
                    game_state = "MENU"
   
                elif askus_button_rect.collidepoint(mouse_pos):  
                    game_state = "ASK US"
                    
                elif share_button_rect.collidepoint(mouse_pos):      
                     game_state = "SHARE"
                    
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
                                game_state = "LEVELS"


                            elif i == 1:
                                game_state = "GAME MODE"


                            elif i == 2:
                                game_state = "OPERATION"


                            elif i == 3:
                                game_state = "LEADER BOARD"


                            elif i == 4:
                                game_state= "SETTING"
                                
                            elif i == 5:
                                running=False

                # ==========================================
                # Settings Menu
                # ==========================================

                elif game_state == "SETTING":
                    for i, rect in enumerate(settings_rects):

                        if rect.collidepoint(mouse_pos):
                            play_click()

                            if i == 0:
                                game_state = "MUSIC"


                            elif i == 1:
                                game_state = "SOUND"


                            elif i == 2:

                                game_state = "THEME"


                            elif i == 3:

                                game_state = "PROFILE"

                            elif i == 4:

                                game_state = "LANGUAGE"

                            elif i == 5:

                                game_state = "SUPPORT"


                            elif i == 6:

                                game_state = "ABOUT"


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

                elif game_state == "THEME":

        
                    theme_event(event)

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


                elif game_state == "GAME MODE":

                    for i, rect in enumerate(image_game_mode):

                        if rect.collidepoint(mouse_pos):
                                play_click()

                                if i == 0 :
                                    game_state="60s"
                                if i == 1 :
                                    game_state="TrueFalse"
                                if i == 2 :
                                    game_state="?+?"
                                if i == 3 :
                                    game_state="x?y"
                                if i == 4 :
                                    game_state=">=<"
                                if i == 5 :
                                    game_state="Fast"
                            


                            


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
        level_rects_for_theme,
        
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
        
        
        
        
        
        
        selected_background
    )


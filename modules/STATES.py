import pygame
from modules.window import _window
from modules.button import *
from modules.design import *
from modules.DATA import *
from modules.font import *
from modules.screen import *
from modules.gif import *
import event_handler 
from modules.music import *
from modules.theme import draw_theme
from modules.language import *
from modules.ab import draw_scroll_window
# from modules.TrueFalseMode.ImageLoader import draw_images
from modules.profile import *
from modules.design import draw_six_images_MODE
from modules.operation_screen import draw_operation_screen
from modules.music import  draw_music
from modules.ceill_screen import draw_ceill_screen





def STATE(screen,game_state,current_width,current_height):

    (
        support_button_rect,
        call_button_rect,
        back_button_rect
    ) = get_current_width_current_height_to_DATA(
        current_width,
        current_height
    )
    
    
    
    if game_state == "MENU":
        
  
        _window(screen,small_window)


            
            
            
        select_buttons.clear()

        draw_menu_buttons(
            screen,
            current_width,
            current_height,
            menu_button,
            fonts,
            select_buttons
        )

        
        
        _window(screen,small_window)


        # وقتی دکمه زده شد برو مرحله بعد
        if select_button_clicked:
            game_state = "OPERATION"
            
        support_button(
            screen,
            support_button_rect
        )
        
        # gallery_button(
        #     screen,
        #     gallery_button_rect
        # )
        call_support(
            screen,
            call_button_rect
        )
 
        image_setter(screen,d1,current_width//2 + 370,current_height//2  - 700)
        image_setter(screen,d2,current_width//2 - 1100,current_height//2 )

 
        
        
        
        
        
        
        
    
    
    
    
    if game_state == "GAME MODE":
        
        draw_six_images_MODE(screen,500,500)        
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
        image_setter(screen,pathth,current_width//2 - 220,current_height//2 - 666)
        gif_setting(screen,gif_frames_mode,current_width // 2 - 246 // 2,current_height // 2 - 1068     // 2)












    if game_state == "SETTING":

        draw_setting_buttons(
            screen,
            current_width,
            current_height,
            fonts,
            settings_rects
        )


                 
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
        # image_setter(screen,p,250,250,current_width//2 + 500,20)














    if game_state == "OPERATION":
        draw_new_screen(screen)
        draw_operation_screen(
            screen,
            fonts,
            operator_images,
            operator_rects,
            current_width,
            current_height
        )
                 
       # gallery_button(
        #     screen,
        #     gallery_button_rect
        # )
        _window(screen,small_window)
                
                
                
                
                
        draw_back_button(
            screen,
            back_button_rect
        )
        gif_setting(screen,gif_frames_op,current_width // 2 - 250 // 2,current_height // 2 - 1085 // 2)
        
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
        
        
        
        
        
        
        
        
        
        
        
        
        







    if game_state == "LEADER BOARD":
                
                
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
                        # عکس دایره. برای پروفایل هر صفحه
        image_setter(screen,pathth,current_width//2 - 220,current_height//2 - 666)
        gif_setting(screen,gif_frames_score,current_width // 2 - 246 // 2,current_height // 2 - 1068     // 2)
        
        
        draw_profile_live_circle(
            screen,
            selected_profile_image,
            p99,
            current_width
        )





















    if game_state == "ABOUT":
        
        
        draw_scroll_window(screen)










    if game_state == "SUPPORT":
                        # عکس دایره. برای پروفایل هر صفحه
        image_setter(screen,pathth,current_width//2 - 220,current_height//2 - 666)
        gif_setting(screen,gif_frames_support,current_width // 2 - 246 // 2,current_height // 2 - 1068     // 2)

        draw_back_button(
            screen,
            back_button_rect)
        support_button(
            screen,
            support_button_rect
        )      
        
        
        
        
        
        
        
        
        

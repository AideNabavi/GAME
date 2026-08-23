import pygame
from modules.design import *
from modules.screen import *
from modules.DATA import *
from modules.button import *

def LEVELS(screen,game_state,current_width,current_height):
    
    (
        support_button_rect,
        call_button_rect,
        back_button_rect
    ) = get_current_width_current_height_to_DATA(
        current_width,
        current_height
    )
    
    if game_state == "level_1":
        draw_six_images(
            screen,
            500,   # فاصله افقی
            500    # فاصله عمودی
        )
        draw_back_button(
            screen,
            back_button_rect)
        
        support_button(
            screen,
            support_button_rect
        )      
        call_support(
            screen,
            call_button_rect
        )
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    elif game_state == "level_2":
        draw_six_images(
            screen,
            500,   # فاصله افقی
            500    # فاصله عمودی
        )
        draw_back_button(
            screen,
            back_button_rect)
        
        support_button(
            screen,
            support_button_rect
        )              
        call_support(
            screen,
            call_button_rect
        )
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    elif game_state == "level_3":
        draw_six_images(
            screen,
            500,   # فاصله افقی
            500    # فاصله عمودی
        )
        draw_back_button(
            screen,
            back_button_rect)
        
        support_button(
            screen,
            support_button_rect
        )              

        call_support(
            screen,
            call_button_rect
        )
        
        
        
        
        
        
        
        
        
        
        
    elif game_state == "level_4":
        draw_six_images(
            screen,
            500,   # فاصله افقی
            500    # فاصله عمودی
        )
        draw_back_button(
            screen,
            back_button_rect)
        
        support_button(
            screen,
            support_button_rect
        )              
        call_support(
            screen,
            call_button_rect
        )
        
        
        
        
        
        
        
        
        
        
        
        
        
    elif game_state == "level_5":
        draw_six_images(
            screen,
            500,   # فاصله افقی
            500    # فاصله عمودی
        )
        draw_back_button(
            screen,
            back_button_rect)
        
        support_button(
            screen,
            support_button_rect
        )      
        
        call_support(
            screen,
            call_button_rect
        )
        
        
        
        
        
        
        
        
    elif game_state == "level_6":
        draw_six_images(
            screen,
            500,   # فاصله افقی
            500    # فاصله عمودی
        )
        draw_back_button(
            screen,
            back_button_rect)
        
        support_button(
            screen,
            support_button_rect
        )      
        
        call_support(
            screen,
            call_button_rect
        )
        
        
        
        
        
        
        
        
        
        
    elif game_state == "level_7":
        draw_six_images(
            screen,
            500,   # فاصله افقی
            500    # فاصله عمودی
        )
        
        draw_back_button(
            screen,
            back_button_rect)
        
        support_button(
            screen,
            support_button_rect
        )      
        call_support(
            screen,
            call_button_rect
        )
        
        
        
        
        
        
        
        
        
        
        
    elif game_state == "level_8":
        draw_six_images(
            screen,
            500,   # فاصله افقی
            500    # فاصله عمودی
        )
        
        draw_back_button(
            screen,
            back_button_rect)
        
        support_button(
            screen,
            support_button_rect
        )      
        
        call_support(
            screen,
            call_button_rect
        )
        
        
        
        
        
        
        
        
        
        
        
        
        
    elif game_state == "level_9":
        draw_six_images(
            screen,
            500,   # فاصله افقی
            500    # فاصله عمودی
        )
        
        draw_back_button(
            screen,
            back_button_rect)
        
        support_button(
            screen,
            support_button_rect
        )      
        
        call_support(
            screen,
            call_button_rect
        )
        
        
        
        
        
        
        
        
        
        
        
    elif game_state == "level_10":
        draw_six_images(
            screen,
            500,   # فاصله افقی
            500    # فاصله عمودی
        )

        draw_back_button(
            screen,
            back_button_rect)
        
        support_button(
            screen,
            support_button_rect
        )      
        call_support(
            screen,
            call_button_rect
        )
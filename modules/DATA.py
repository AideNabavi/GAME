import pygame




    
############################################## مربوط به صفحه منو
small_window=""
select_buttons = []
select_button_clicked = False







##############################################برای  تب ستینگ                    تنظمیات بازی   

settings_rects = []





##############################################  for  Operation  tab

operator = ""

operator_rects={}
operator_images = {

    "+": pygame.transform.smoothscale(
        pygame.image.load("./asset/image/signs/plus.png").convert_alpha(),
        (200, 200)
    ),

    "-": pygame.transform.smoothscale(
        pygame.image.load("./asset/image/signs/minus.png").convert_alpha(),
         (200, 200)
    ),

    "*": pygame.transform.smoothscale(
        pygame.image.load("./asset/image/signs/multiply.png").convert_alpha(),
         (200, 200)
    ),

    "/": pygame.transform.smoothscale(
        pygame.image.load("./asset/image/signs/divide.png").convert_alpha(),
         (200, 200)
    )

}





######################################






###################################### این رکت های برای باتن ها رو میده 
def get_current_width_current_height_to_DATA(current_width,current_height):

        #------------------------------------ donate



    support_button_rect = pygame.Rect(
        40,  # فاصله از راست
        current_height - 170,                   # فاصله از بالا
        150,
        150
    )


    #----------------------------- help us


    call_button_rect= pygame.Rect(
        current_width - 180,  # فاصله از راست
        current_height  - 160,                   # فاصله از بالا
        150,
        150
    )




    #----------------------------- دکمه برگشت

    back_button_rect = pygame.Rect(
        30,
        20,
        150,
        150
    )


    return support_button_rect, call_button_rect,back_button_rect





























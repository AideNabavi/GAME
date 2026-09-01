import pygame
from modules.hover import hover_image_level
import math
# برای تومار است 
from modules.font import fonts

# d1=pygame.transform.smoothscale(pygame.image.load("./asset/image/design/1.png").convert_alpha(),(260,700))
# d2=pygame.transform.smoothscale(pygame.image.load("./asset/image/design/2.png").convert_alpha(),(700,250))


background_Lan=pygame.transform.smoothscale(pygame.image.load("./asset/image/language/theme.png").convert_alpha(),(1450,950))
pathth =pygame.transform.smoothscale(pygame.image.load("./asset/image/logo.png").convert_alpha(),(300,300))
liner =pygame.transform.smoothscale(pygame.image.load("./asset/image/liner1.png").convert_alpha(),(750,1365))

xyz_for_profile_logo=50
width_for_profile_logo=120

def image_setter(screen,path,x,y):
    screen.blit(path,(x,y))



#background setter
def back_setter(screen, image, x=0, y=0):
    screen_width, screen_height = screen.get_size()

    # نسبت تصویر و صفحه
    image_width, image_height = image.get_size()

    scale = max(
        screen_width / image_width,
        screen_height / image_height
    )

    new_width = int(image_width * scale)
    new_height = int(image_height * scale)

    # Resize
    image = pygame.transform.smoothscale(
        image,
        (new_width, new_height)
    )

    # وسط‌چین کردن و Crop شدن اطراف
    pos_x = (screen_width - new_width) // 2 + x
    pos_y = (screen_height - new_height) // 2 + y

    screen.blit(image, (pos_x, pos_y))

import pygame






















# این برای صفحه  اسلاید اومدن نوار برای ستینگ است  
menu_slide_active = False
menu_slide_x = None
menu_slide_back = False
# for menu liner set with slid effect
def image_setter_menu(screen, path, x, y, speed=50):

    global menu_slide_x

    # --------------------------------------------------------
    # شروع انیمیشن
    # --------------------------------------------------------

    if menu_slide_x is None:
        menu_slide_x = -path.get_width()

    # --------------------------------------------------------
    # حرکت به سمت مقصد
    # --------------------------------------------------------

    if menu_slide_x < x:

        menu_slide_x += speed

        if menu_slide_x >= x:
            menu_slide_x = x

    # --------------------------------------------------------
    # رسم
    # --------------------------------------------------------

    screen.blit(
        path,
        (menu_slide_x, y)
    )

    # --------------------------------------------------------
    # وقتی رسید به مقصد
    # --------------------------------------------------------

    if menu_slide_x >= x:

        return True

    return False


# این تابع هم برای برگشت اسلاید نوار بار ستینگ است 
def image_setter_menu_back(screen, path, x, y, speed=40):

    global menu_slide_x

    # --------------------------------------------------------
    # اگر موقعیت فعلی مشخص نیست
    # از همان x نهایی شروع کن
    # --------------------------------------------------------

    if menu_slide_x is None:
        menu_slide_x = x

    # --------------------------------------------------------
    # حرکت به سمت چپ
    # --------------------------------------------------------

    menu_slide_x -= speed

    # --------------------------------------------------------
    # نمایش تصویر
    # --------------------------------------------------------

    screen.blit(
        path,
        (menu_slide_x, y)
    )

    # --------------------------------------------------------
    # وقتی کاملاً از سمت چپ خارج شد
    # --------------------------------------------------------

    if menu_slide_x + path.get_width() <= 0:
        return True

    return False




















#------------------------------------------------------------------------------------------------




images = [
    pygame.transform.smoothscale(
        pygame.image.load("./asset/image/levels/plus.png").convert_alpha(),
        (350,350)
    ),
    pygame.transform.smoothscale(
        pygame.image.load("./asset/image/levels/minus.png").convert_alpha(),
        (350,350)
    ),
    pygame.transform.smoothscale(
        pygame.image.load("./asset/image/levels/multiply.png").convert_alpha(),
        (350,350)
    ),
    pygame.transform.smoothscale(
        pygame.image.load("./asset/image/levels/divide.png").convert_alpha(),
        (350,350)
    ),
    pygame.transform.smoothscale(
        pygame.image.load("./asset/image/levels/plus.png").convert_alpha(),
        (350,350)
    ),
    pygame.transform.smoothscale(
        pygame.image.load("./asset/image/levels/multiply.png").convert_alpha(),
        (350,350)
    )
]






image_game_mode = []



image_sizes = [350,350,350,350,350,350]


def draw_six_images(
    screen,
    gap_x,
    gap_y
):

    global image_sizes

    mouse_pos = pygame.mouse.get_pos()

    rects = []

    # اندازه کل گروه
    total_width = (3 - 1) * gap_x
    total_height = (2 - 1) * gap_y


    # مرکز صفحه
    center_x = screen.get_width() // 2
    center_y = screen.get_height() // 2


    # شروع رسم از بالا-چپ گروه
    start_x = center_x - total_width // 2
    start_y = center_y - total_height // 2


    for i, img in enumerate(images):

        row = i // 3
        col = i % 3


        x = start_x + col * gap_x
        y = start_y + row * gap_y


        rect = img.get_rect(
            center=(x, y)
        )


        new_img, new_rect, image_sizes[i] = hover_image_level(
            img,
            rect,
            mouse_pos,
            image_sizes[i]
        )


        screen.blit(
            new_img,
            new_rect
        )


        rects.append(new_rect)


    return rects





image_sizes = [350,350,350,350,350,350,350,350,350,350]


def draw_ten_images(
    screen,
    gap_x,
    gap_y
):

    global image_sizes

    mouse_pos = pygame.mouse.get_pos()

    rects = []

    cols = 5
    rows = 2


    total_width = (cols - 1) * gap_x
    total_height = (rows - 1) * gap_y


    center_x = screen.get_width() // 2
    center_y = screen.get_height() // 2


    start_x = center_x - total_width // 2
    start_y = center_y - total_height // 2


    for i, img in enumerate(images):

        row = i // cols
        col = i % cols


        x = start_x + col * gap_x
        y = start_y + row * gap_y


        rect = img.get_rect(
            center=(x, y)
        )


        new_img, new_rect, image_sizes[i] = hover_image_level(
            img,
            rect,
            mouse_pos,
            image_sizes[i]
        )


        screen.blit(
            new_img,
            new_rect
        )


        rects.append(new_rect)


    return rects








    
    
def UP_DOWN(
    screen,
    image,
    x,
    y,
    height=6
):

    t = pygame.time.get_ticks() / 1000


    offset = (
        math.sin(t * math.pi)
        * height
    )


    rect = image.get_rect(
        center=(
            x,
            y - offset
        )
    )


    screen.blit(
        image,
        rect
    )
    
    
    
    
    
    
    
    



















 














#----------------------------------------------------------------------------------


# حلقه دوره دایره تایم 
tospack=pygame.transform.smoothscale(pygame.image.load("./asset/image/in_game/alarm1.png").convert_alpha(),(250,250))

def in_game_alarm(screen):
    current_width, current_height = screen.get_size()
    screen.blit(
        tospack,
        (30 , 30)
    )





#----------------------------------------------------------------------------------


right= 1900


# این برای ۳ تا شانس است 

_hint=pygame.transform.smoothscale(pygame.image.load("./asset/image/in_game/bulb.png").convert_alpha(),(100,100))

note_text = fonts["icon2"].render(
    "3",
    True,
    (255, 255, 255)
)
hint_rect_=None


def hint(screen):
    global hint_rect_
    current_width, current_height = screen.get_size()

    # Rect فقط برای تصویر
    hint_rect = _hint.get_rect(
        midright=(
            current_width - 50,
            current_height//2 - 30
        )
    )

    # تصویر
    screen.blit(
        _hint,
        hint_rect
    )

    # متن
    screen.blit(
        note_text,
        (
            right,
            current_height//2 - 45
        )
    )
    hint_rect_=hint_rect
    # فقط Rect تصویر


#----------------------------------------------------------------------------------















# این برای قلب است در بازی برای ۳ تا جون 
from modules.font import fonts



save_=pygame.transform.smoothscale(pygame.image.load("./asset/image/in_game/save.png").convert_alpha(),(100,100))
note_text = fonts["icon2"].render(
    "3",
    True,
    (255, 255, 255)
)

def save(screen):
    current_width, current_height = screen.get_size()
    screen.blit(
        save_,
        (right ,current_height//2 - 280)
    )

    screen.blit(
        note_text,
        (right ,current_height//2 - 250 )
    )



#----------------------------------------------------------------------------------





exit_=pygame.transform.smoothscale(pygame.image.load("./asset/image/in_game/exit.png").convert_alpha(),(100,100))

def exit__(screen):
    current_width, current_height = screen.get_size()
    screen.blit(
        exit_,
        (current_width//2 - 980,current_height//2 +480)
    )









#----------------------------------------------------------------------------------





#برای باد کنک است
from modules.font import fonts


menuu1=pygame.transform.smoothscale(pygame.image.load("./asset/image/in_game/menuu.png").convert_alpha(),(120,120))

def menuu(screen):
    current_width, current_height = screen.get_size()
    screen.blit(
        menuu1,
        (right - 10,current_height//2 +480)
    )








#----------------------------------------------------------------------------------

# برای برای ریستارت است است 
from modules.font import fonts


res=pygame.transform.smoothscale(pygame.image.load("./asset/image/in_game/restart.png").convert_alpha(),(90,90))

def restart(screen):
    current_width, current_height = screen.get_size()
    screen.blit(
        res,
        (current_width//2 - 970,current_height//2 + 280)
    )






#---------------------------------------------------------------------------------- بریا سکه امتیاز 

# برای برای ریستارت است است 
from modules.font import fonts


scoreee=pygame.transform.smoothscale(pygame.image.load("./asset/image/score.png").convert_alpha(),(100,100))

def scoreee1(screen):
    current_width, current_height = screen.get_size()
    screen.blit(
        scoreee,
        (current_width//2  - 240,current_height//2 - 607)
    )






#----------------------------------------------------------------------------------











#---------------------- for flage



import pygame



# موقعیت‌ها
screen_height = 1080

start_y = screen_height   # خارج از صفحه

flag_x = 500
flag_y = start_y


# وضعیت پرچم
flag_active = False
flag_finished = False


# زمان‌ها
move_duration = 500     # زمان حرکت بالا و پایین (میلی ثانیه)
stay_duration_ = 2000   # ماندن بالا (۱۰ ثانیه)

move_start_time = 0
stay_start_time = 0



def move_flage(image,screen, x, show_flag,target_y):

    global flag_y
    global flag_active
    global flag_finished
    global move_start_time
    global stay_start_time


    current_time = pygame.time.get_ticks()


    # شروع فقط یک بار
    if show_flag and not flag_finished and not flag_active:

        flag_active = "up"
        move_start_time = current_time



    # حرکت به بالا
    if flag_active == "up":

        progress = (current_time - move_start_time) / move_duration


        if progress >= 1:

            flag_y = target_y
            flag_active = "stay"
            stay_start_time = current_time


        else:

            flag_y = start_y + (target_y - start_y) * progress



    # ماندن بالا
    elif flag_active == "stay":

        flag_y = target_y


        if current_time - stay_start_time >= stay_duration_:

            flag_active = "down"
            move_start_time = current_time



    # حرکت پایین
    elif flag_active == "down":

        progress = (current_time - move_start_time) / move_duration


        if progress >= 1:

            flag_y = start_y
            flag_active = False
            flag_finished = True


        else:

            flag_y = target_y + (start_y - target_y) * progress



    # رسم
    if not flag_finished:

        screen.blit(image, (x, flag_y))
        
        
        
        
        
        

def reset_flage():

    global flag_y
    global flag_active
    global flag_finished
    global move_start_time
    global stay_start_time

    flag_y = start_y

    flag_active = False
    flag_finished = False

    move_start_time = 0
    stay_start_time = 0

































import pygame


# ============================================================
# IMAGE
# ============================================================

image_coming_soon = pygame.image.load(
    "./asset/image/CS.png"
).convert_alpha()


# ============================================================
# POSITION
# ============================================================

screen_height = 1080

start_y = screen_height
target_y = 800

image_x = 500
image_y = start_y


# ============================================================
# STATE
# ============================================================

image_active = False
image_finished = False


# ============================================================
# TIME
# ============================================================

move_duration = 500      # بالا / پایین
stay_duration = 2000     # ۵ ثانیه ماندن

move_start_time = 0
stay_start_time = 0


# ============================================================
# MOVE IMAGE
# ============================================================

def move_image(screen, x, show_image):

    global image_y
    global image_active
    global image_finished
    global move_start_time
    global stay_start_time

    current_time = pygame.time.get_ticks()


    # --------------------------------------------------------
    # START
    # --------------------------------------------------------

    if show_image and not image_finished and not image_active:

        image_active = "up"
        move_start_time = current_time


    # --------------------------------------------------------
    # MOVE UP
    # --------------------------------------------------------

    if image_active == "up":

        progress = (
            current_time - move_start_time
        ) / move_duration


        if progress >= 1:

            image_y = target_y

            image_active = "stay"

            stay_start_time = current_time


        else:

            image_y = (
                start_y
                + (target_y - start_y) * progress
            )


    # --------------------------------------------------------
    # STAY 5 SECONDS
    # --------------------------------------------------------

    elif image_active == "stay":

        image_y = target_y


        if current_time - stay_start_time >= stay_duration:

            image_active = "down"

            move_start_time = current_time


    # --------------------------------------------------------
    # MOVE DOWN
    # --------------------------------------------------------

    elif image_active == "down":

        progress = (
            current_time - move_start_time
        ) / move_duration


        if progress >= 1:

            image_y = start_y

            image_active = False

            image_finished = True


        else:

            image_y = (
                target_y
                + (start_y - target_y) * progress
            )


    # --------------------------------------------------------
    # DRAW
    # --------------------------------------------------------

    if not image_finished:

        screen.blit(
            image_coming_soon,
            (x, image_y)
        )
        
        
        
        
        
        
        
      
      
      
        
        
        
        
# پانج ضربه زن
        
import pygame


# ============================================================
# IMAGE
# ============================================================

image_original = pygame.image.load(
    "./asset/image/score.png"
).convert_alpha()


# اندازه اصلی عکس
IMAGE_WIDTH = image_original.get_width()
IMAGE_HEIGHT = image_original.get_height()


# ============================================================
# POSITION
# ============================================================

image_x = 500
image_y = 800


# ============================================================
# STATE
# ============================================================

image_active = False
image_finished = False

image_state = None


# ============================================================
# TIME
# ============================================================

punch_duration = 350      # مدت ضربه خوردن
stay_duration = 5000      # ۵ ثانیه ماندن
zoomout_duration = 500    # مدت زوم اوت


start_time = 0


# ============================================================
# PUNCH IMAGE
# ============================================================

def punch_image(screen, x, y, show_image):

    global image_active
    global image_finished
    global image_state
    global start_time


    current_time = pygame.time.get_ticks()


    # --------------------------------------------------------
    # START
    # --------------------------------------------------------

    if show_image and not image_finished and not image_active:

        image_active = True
        image_state = "punch"

        start_time = current_time


    if not image_active:
        return


    # --------------------------------------------------------
    # PUNCH
    # --------------------------------------------------------

    if image_state == "punch":

        progress = (
            current_time - start_time
        ) / punch_duration


        if progress >= 1:

            progress = 1

            image_state = "stay"

            start_time = current_time


        # از خیلی کوچک شروع میشه
        # و سریع به اندازه اصلی میرسه

        scale = 0.15 + (0.85 * progress)

        width = int(IMAGE_WIDTH * scale)
        height = int(IMAGE_HEIGHT * scale)


    # --------------------------------------------------------
    # STAY
    # --------------------------------------------------------

    elif image_state == "stay":

        width = IMAGE_WIDTH
        height = IMAGE_HEIGHT


        if current_time - start_time >= stay_duration:

            image_state = "zoomout"

            start_time = current_time


    # --------------------------------------------------------
    # ZOOM OUT
    # --------------------------------------------------------

    elif image_state == "zoomout":

        progress = (
            current_time - start_time
        ) / zoomout_duration


        if progress >= 1:

            image_active = False
            image_finished = True

            return


        # از اندازه اصلی به صفر
        scale = 1.0 - progress

        width = int(IMAGE_WIDTH * scale)
        height = int(IMAGE_HEIGHT * scale)


    # --------------------------------------------------------
    # SCALE
    # --------------------------------------------------------

    if width <= 0 or height <= 0:
        return


    image = pygame.transform.smoothscale(
        image_original,
        (width, height)
    )


    # --------------------------------------------------------
    # CENTER
    # --------------------------------------------------------

    rect = image.get_rect(
        center=(
            x + IMAGE_WIDTH // 2,
            y + IMAGE_HEIGHT // 2
        )
    )


    # --------------------------------------------------------
    # DRAW
    # --------------------------------------------------------

    screen.blit(
        image,
        rect
    )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

import pygame
from modules.hover import hover_image_level
import math

d1=pygame.transform.smoothscale(pygame.image.load("./asset/image/design/1.png").convert_alpha(),(260,700))
d2=pygame.transform.smoothscale(pygame.image.load("./asset/image/design/2.png").convert_alpha(),(700,250))


background_Lan=pygame.transform.smoothscale(pygame.image.load("./asset/image/language/theme.png").convert_alpha(),(1450,950))
pathth =pygame.transform.smoothscale(pygame.image.load("./asset/image/logo.png").convert_alpha(),(400,400))
pathth_ =pygame.transform.smoothscale(pygame.image.load("./asset/image/logo.png").convert_alpha(),(450,450))


def image_setter(screen,path,x,y):
    screen.blit(path,(x,y))











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





#------------------------------------------------------------------------------------------------GAME MODE 6 image



# شش  تا عکس برای مود گیم 
images_MODE = [
    pygame.transform.smoothscale(
        pygame.image.load("./asset/image/MODE/1.png"),
        (350,350)
    ),
    pygame.transform.smoothscale(
        pygame.image.load("./asset/image/MODE/2.png"),
        (350,350)
    ),
    pygame.transform.smoothscale(
        pygame.image.load("./asset/image/MODE/3.png"),
        (350,350)
    ),
    pygame.transform.smoothscale(
        pygame.image.load("./asset/image/MODE/4.png"),
        (350,350)
    ),
    pygame.transform.smoothscale(
        pygame.image.load("./asset/image/MODE/1.png"),
        (350,350)
    ),
    pygame.transform.smoothscale(
        pygame.image.load("./asset/image/MODE/2.png"),
        (350,350)
    )
]







image_game_mode = []



image_sizes = [350,350,350,350,350,350]


def draw_six_images_MODE(
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

    image_game_mode.clear()

    for i, img in enumerate(images_MODE):

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

        image_game_mode.append(rect)
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
    
    
    
    
    
    
    
    






# این برای ۳ تا شانس است 

_hint=pygame.transform.smoothscale(pygame.image.load("./asset/image/hint1.png").convert_alpha(),(150,150))

def hint(screen):
    current_width, current_height = screen.get_size()
    screen.blit(
        _hint,
        (current_width//2 - 995 ,current_height//2 - 100)
    )



    note_text = fonts["heart"].render(
        "3",
        True,
        (255, 255, 255)
    )

    screen.blit(
        note_text,
        (current_width//2 - 915 ,current_height//2 + 5 )
    )













# حلقه دوره دایره تایم 
tospack=pygame.transform.smoothscale(pygame.image.load("./asset/image/alarm1.png").convert_alpha(),(310,310))

def in_game_alarm(screen):
    current_width, current_height = screen.get_size()
    screen.blit(
        tospack,
        (current_width //2 - 154 , current_height //2 + 190)
    )





 




























# این برای قلب است در بازی برای ۳ تا جون 
from modules.font import fonts


save_=pygame.transform.smoothscale(pygame.image.load("./asset/image/save.png").convert_alpha(),(150,150))

def save(screen):
    current_width, current_height = screen.get_size()
    screen.blit(
        save_,
        (current_width//2 - 970 ,current_height//2 - 350)
    )


    note_text = fonts["heart"].render(
        "3",
        True,
        (255, 255, 255)
    )

    screen.blit(
        note_text,
        (current_width//2 - 900 ,current_height//2 - 250)
    )

















import pygame

flag = pygame.image.load("./asset/image/flage.png").convert_alpha()


# موقعیت‌ها
screen_height = 1080

start_y = screen_height   # خارج از صفحه
target_y = 800             # جای نمایش پرچم

flag_x = 500
flag_y = start_y


# وضعیت پرچم
flag_active = False
flag_finished = False


# زمان‌ها
move_duration = 500     # زمان حرکت بالا و پایین (میلی ثانیه)
stay_duration = 5000   # ماندن بالا (۱۰ ثانیه)

move_start_time = 0
stay_start_time = 0



def move_flage(screen, x, show_flag):

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


        if current_time - stay_start_time >= stay_duration:

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

        screen.blit(flag, (x, flag_y))
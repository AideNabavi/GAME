import pygame

from modules.setting import draw_text_stroke
from modules.hover import *
rec_enter=None
def hover_image_firstpage(
    image,
    rect,
    mouse_pos,
    current_size
):

    NORMAL_SIZE = 200
    HOVER_SIZE = 230
    SPEED = 2

    if rect.collidepoint(mouse_pos):

        if current_size < HOVER_SIZE:
            current_size += SPEED

    else:

        if current_size > NORMAL_SIZE:
            current_size -= SPEED

    # اندازه اصلی تصویر
    original_width = image.get_width()
    original_height = image.get_height()

    # نسبت تصویر
    ratio = original_height / original_width

    width = current_size
    height = int(current_size * ratio)

    new_image = pygame.transform.smoothscale(
        image,
        (
            width,
            height
        )
    )

    new_rect = new_image.get_rect(
        center=rect.center
    )
    global rec_enter
    rec_enter=new_rect
    return new_image, new_rect, current_size





enter_size = 200

def draw_name_screen(
    screen,
    fonts,
    player_name,
    input_box,
    enter_button
):

    # ---------------- Input Box ----------------

    pygame.draw.rect(
        screen,
        (255, 255, 255),
        input_box,
        border_radius=10
    )

    pygame.draw.rect(
        screen,
        (0, 0, 0),
        input_box,
        2,
        border_radius=10
    )


    # ---------------- Player Name ----------------

    if player_name == "":

        name_text = fonts["name"].render(
            "Your Name",
            True,
            (170,170,170)
        )

    else:

        name_text = fonts["name"].render(
            player_name,
            True,
            (255,220,0)
        )


    name_rect = name_text.get_rect(
        center=input_box.center
    )


    # Stroke فقط وقتی اسم وارد شده
    if player_name != "":

        stroke = fonts["name"].render(
            player_name,
            True,
            (0,0,0)
        )

        draw_text_stroke(
            screen,
            stroke,
            name_rect.topleft
        )


    screen.blit(
        name_text,
        name_rect
    )


     # ---------------- Enter Button Image ----------------
    enter_image = pygame.image.load(
        "./asset/image/enter.png"
    ).convert_alpha()

    # enter_image = pygame.transform.smoothscale(
    #     enter_image,
    #     (120, 120)
    # )
    rec_enter=enter_image.get_rect()
    mouse_pos = pygame.mouse.get_pos()
    global enter_size
    enter_image, enter_rect, enter_size = hover_image_firstpage(
        enter_image,
        enter_button,
        mouse_pos,
        enter_size
    )

    screen.blit(
        enter_image,
        enter_rect
    )
        
    
    
    
    














    
    
#-------------------------صفحه زرد برای قسیمت وارد کردن  سقف  

def draw_card(screen, rect):
    # سایه
    shadow = pygame.Surface(
        (rect.width + 20, rect.height + 20),
        pygame.SRCALPHA
    )

    pygame.draw.rect(
        shadow,
        (0, 0, 0, 80),
        (10, 10, rect.width, rect.height),
        border_radius=30
    )

    screen.blit(
        shadow,
        (rect.x - 10, rect.y - 10)
    )


    # خود مربع با کیفیت
    box = pygame.Surface(
        (rect.width, rect.height),
        pygame.SRCALPHA
    )
    

    # داخل سفید
    pygame.draw.rect(
        box,
        # (255, 255, 255),
        (255, 255, 255),
        (0, 0, rect.width, rect.height),
        border_radius=30
    )

    # استروک مشکی
    pygame.draw.rect(
        box,
        (0, 0, 0),
        (0, 0, rect.width, rect.height),
        width=3,
        border_radius=30
    )


    # سایه
    shadow_rect = rect.copy()
    shadow_rect.y += 7
    shadow_rect.x += 0

    pygame.draw.rect(
        screen,
        (90, 90, 90),
        shadow_rect,
        border_radius=30
    )

    screen.blit(box, rect.topleft)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
scren = None
logo = None



def draw_new_screen(screen):
    global scren
    global logo

    if scren is None:
        scren = pygame.image.load(
            "./asset/image/back22.png"
        ).convert_alpha()
        logo = pygame.image.load(
            "./asset/image/logo.png"
        ).convert_alpha()

        scren = pygame.transform.smoothscale(
            scren,
            (1200, 650)
        )
        logo = pygame.transform.smoothscale(
            logo,
            (450, 450)
        )

    current_width, current_height = screen.get_size()

    screen.blit(
        scren,
        (
            current_width // 2 - scren.get_width() // 2,
            current_height // 2 -160
        )
    )
    screen.blit(
        logo,
        (
            current_width // 2 - logo.get_width() // 2,
            current_height // 2 - 666
        )
    )








import pygame


def draw_about(
    screen,
    current_width,
    current_height,
    about_image,
    font_big,
    font
):

    # =====================================
    # استروک فقط برای عنوان
    # =====================================

    def draw_title(
        text,
        font,
        position,
        text_color=(255,180,0),
        stroke_color=(0,0,0),
        stroke_size=3
    ):

        text_surface = font.render(
            text,
            True,
            text_color
        )

        stroke_surface = font.render(
            text,
            True,
            stroke_color
        )


        rect = text_surface.get_rect(
            center=position
        )


        x, y = rect.topleft


        for dx, dy in [
            (-stroke_size,0),
            (stroke_size,0),
            (0,-stroke_size),
            (0,stroke_size)
        ]:

            screen.blit(
                stroke_surface,
                (
                    x + dx,
                    y + dy
                )
            )


        screen.blit(
            text_surface,
            rect
        )


    # =====================================
    # کارت اصلی
    # =====================================

    about_rect = pygame.Rect(
        current_width // 2 - 300,
        50,
        600,
        700
    )


    # سایه

    shadow = pygame.Surface(
        (
            about_rect.width + 20,
            about_rect.height + 20
        ),
        pygame.SRCALPHA
    )


    pygame.draw.rect(
        shadow,
        (0,0,0,70),
        (
            10,
            10,
            about_rect.width,
            about_rect.height
        ),
        border_radius=35
    )


    screen.blit(
        shadow,
        (
            about_rect.x - 10,
            about_rect.y - 10
        )
    )


    # کارت زرد

    pygame.draw.rect(
        screen,
        (255,245,180),
        about_rect,
        border_radius=35
    )


    pygame.draw.rect(
        screen,
        (0,0,0),
        about_rect,
        width=3,
        border_radius=35
    )


    # =====================================
    # عکس دایره ای
    # =====================================

    image_size = 150


    image = pygame.transform.smoothscale(
        about_image,
        (
            image_size,
            image_size
        )
    )


    image_rect = image.get_rect(
        center=(
            current_width//2,
            about_rect.y + 120
        )
    )


    # قاب مشکی عکس

    pygame.draw.circle(
        screen,
        (0,0,0),
        image_rect.center,
        image_size//2 + 8
    )


    # ماسک دایره

    mask = pygame.Surface(
        (
            image_size,
            image_size
        ),
        pygame.SRCALPHA
    )


    pygame.draw.circle(
        mask,
        (255,255,255,255),
        (
            image_size//2,
            image_size//2
        ),
        image_size//2
    )


    circle_image = pygame.Surface(
        (
            image_size,
            image_size
        ),
        pygame.SRCALPHA
    )


    circle_image.blit(
        image,
        (0,0)
    )


    circle_image.blit(
        mask,
        (0,0),
        special_flags=pygame.BLEND_RGBA_MIN
    )


    screen.blit(
        circle_image,
        image_rect
    )


    # =====================================
    # عنوان با استروک
    # =====================================

    draw_title(
        "About Us",
        font_big,
        (
            current_width//2,
            about_rect.y + 240
        )
    )


    # =====================================
    # توضیحات بدون استروک
    # =====================================

    texts = [
        "F Math Game",
        "A smart game for improving",
        "your calculation skills"
    ]


    y = about_rect.y + 300


    for text in texts:


        surface = font.render(
            text,
            True,
            (70,70,70)
        )


        rect = surface.get_rect(
            center=(
                current_width//2,
                y
            )
        )


        screen.blit(
            surface,
            rect
        )


        y += 40



    # =====================================
    # کارت های اطلاعات
    # =====================================
    info_width = 460
    info_height = 60

    info_x = about_rect.centerx - info_width // 2

    current_width, current_height = screen.get_size()

    info_boxes = [

        pygame.Rect(
            info_x,
            about_rect.y + 420,
            info_width,
            info_height
        ),

        pygame.Rect(
            info_x,
            about_rect.y + 500,
            info_width,
            info_height
        ),

        pygame.Rect(
            info_x,
            about_rect.y + 580,
            info_width,
            info_height
        )

    ]

    labels = [

        "Email : Nabavia447@gmail.com",

        "Version : 1.0.0",

        "Creator : Aiden"

    ]



    for rect, label in zip(
        info_boxes,
        labels
    ):


        pygame.draw.rect(
            screen,
            (255,255,255),
            rect,
            border_radius=20
        )


        pygame.draw.rect(
            screen,
            (0,0,0),
            rect,
            width=2,
            border_radius=20
        )


        # متن بدون استروک

        text_surface = font.render(
            label,
            True,
            (30,30,30)
        )


        text_rect = text_surface.get_rect(
            center=rect.center
        )


        screen.blit(
            text_surface,
            text_rect
        )
        
        
        
        



# from modules.hover import hover_image
back_size = 150
from modules.hover import hover_image
back_image = pygame.image.load(
        "./asset/image/back1.png"
    )
def draw_back_button(
    screen,
    back_button_rect
):

    global back_size

    mouse_pos = pygame.mouse.get_pos()


    image, image_rect, back_size = hover_image_icon(
        back_image,
        back_button_rect,
        mouse_pos,
        back_size
    )


    screen.blit(
        image,
        image_rect
    )
    
    
    
    
    













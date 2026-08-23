import pygame
from modules.sound_effect import play_click
from modules.hover import hover_image_profile


def load_default_profile():

    image = pygame.image.load(
        "./asset/image/profile/user.png"
    ).convert_alpha()


    return image












def draw_hue_bar1(screen, rect):

    scale = 6

    width = rect.width * scale
    height = rect.height * scale


    # Surface نوار
    temp = pygame.Surface(
        (width, height),
        pygame.SRCALPHA
    )


    # -----------------------------
    # رسم Hue
    # -----------------------------

    for x in range(width):

        hue = x / width

        color = pygame.Color(0)

        color.hsva = (
            hue * 360,
            100,
            100,
            100
        )

        pygame.draw.line(
            temp,
            color,
            (x, 0),
            (x, height)
        )


    # -----------------------------
    # گوشه گرد
    # -----------------------------

    mask = pygame.Surface(
        (width, height),
        pygame.SRCALPHA
    )

    pygame.draw.rect(
        mask,
        (255,255,255,255),
        (0,0,width,height),
        border_radius=30 * scale
    )


    temp.blit(
        mask,
        (0,0),
        special_flags=pygame.BLEND_RGBA_MULT
    )


    # کاهش کیفیتی
    temp = pygame.transform.smoothscale(
        temp,
        (
            rect.width,
            rect.height
        )
    )


    # نوار رنگ
    screen.blit(
        temp,
        rect
    )


    # -----------------------------
    # قاب مشکی
    # -----------------------------

    pygame.draw.rect(
        screen,
        (0,0,0),
        rect,
        width=2,
        border_radius=30
    )
    
    
    

def load_profile_images():

    profile_images = {}

    for i in range(1, 21):

        image = pygame.image.load(
            f"./asset/image/profile/{i}.png"
        ).convert_alpha()

        # آماده‌سازی عکس با کیفیت بالا
        image = pygame.transform.smoothscale(
            image,
            (200, 200)
        )

        # Surface دایره‌ای
        circle_surface = pygame.Surface(
            (200, 200),
            pygame.SRCALPHA
        )

        # عکس
        circle_surface.blit(
            image,
            (0, 0)
        )

        # ماسک دایره
        mask = pygame.Surface(
            (200, 200),
            pygame.SRCALPHA
        )
        pygame.draw.circle(
            mask,
            (255, 255, 255, 255),
            (100, 100),
            100
        )

        circle_surface.blit(
            mask,
            (0, 0),
            special_flags=pygame.BLEND_RGBA_MULT
        )

        profile_images[i] = circle_surface

    return profile_images













def draw_profile_circle(
    screen,
    image,
    center,
    size=250,
    border_color=(255,255,255)
):

    image = pygame.transform.smoothscale(
        image,
        (size, size)
    )

    circle_surface = pygame.Surface(
        (size, size),
        pygame.SRCALPHA
    )

    mask = pygame.Surface(
        (size, size),
        pygame.SRCALPHA
    )

    pygame.draw.circle(
        mask,
        (255, 255, 255, 255),
        (size // 2, size // 2),
        size // 2 - 1
    )

    circle_surface.blit(
        image,
        (0, 0)
    )

    circle_surface.blit(
        mask,
        (0, 0),
        special_flags=pygame.BLEND_RGBA_MULT
    )

    rect = circle_surface.get_rect(
        center=center
    )

    screen.blit(
        circle_surface,
        rect
    )

    # Border سفید
    draw_smooth_circle_border(
        screen,
        center,
        size//2.1,
        border_color,
        4
    )
        
        









# def draw_hue_bar(screen, rect):

#     colors = []

#     for i in range(rect.width):

#         hue = i / rect.width

#         color = pygame.Color(0)

#         color.hsva = (
#             hue * 360,
#             100,
#             100,
#             100
#         )

#         colors.append(color)


#     for x, color in enumerate(colors):

#         pygame.draw.line(
#             screen,
#             color,
#             (rect.x+x, rect.y),
#             (rect.x+x, rect.bottom)
#         )




profile_hover_sizes = {}

def draw_profiles(
    screen,
    profile_images,
    profile_rects,
    profile_area
):

    mouse_pos = pygame.mouse.get_pos()

    profile_rects.clear()


    columns = 5

    gap_x = 250
    gap_y = 250


    total_width = (columns - 1) * gap_x

    start_x = (
        profile_area.centerx
        - total_width // 2
    )


    start_y = profile_area.y + 70


    # فقط ۱۰ عکس اول
    profiles = list(profile_images.items())[:10]


    for index, (profile_id, image) in enumerate(profiles):

        row = index // columns
        col = index % columns


        x = start_x + col * gap_x
        y = start_y + row * gap_y


        # عکس اصلی
        normal_image = pygame.transform.smoothscale(
            image,
            (200,200)
        )


        rect = normal_image.get_rect(
            center=(x,y)
        )


        profile_rects[profile_id] = rect



        # ساخت مقدار اولیه هاور
        if profile_id not in profile_hover_sizes:
            profile_hover_sizes[profile_id] = 200



        # سیستم هاور نرم
        new_image, new_rect, profile_hover_sizes[profile_id] = hover_image_profile(
            image,
            rect,
            mouse_pos,
            profile_hover_sizes[profile_id]
        )


        screen.blit(
            new_image,
            new_rect
        )






def draw_smooth_circle_border(screen, center, radius, color, width):

    scale = 20  # کیفیت بالاتر

    temp = pygame.Surface(
        (
            radius * 2 * scale + width * 2,
            radius * 2 * scale + width * 2
        ),
        pygame.SRCALPHA
    )

    pygame.draw.circle(
        temp,
        color,
        (
            temp.get_width() // 2,
            temp.get_height() // 2
        ),
        radius * scale,
        width * scale
    )

    temp = pygame.transform.smoothscale(
        temp,
        (
            radius * 2 + width * 2,
            radius * 2 + width * 2
        )
    )

    rect = temp.get_rect(
        center=center
    )

    screen.blit(
        temp,
        rect
    )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def draw_smooth_rect_border(
    screen,
    rect,
    color,
    width
):

    scale = 5

    temp = pygame.Surface(
        (
            rect.width * scale,
            rect.height * scale
        ),
        pygame.SRCALPHA
    )


    pygame.draw.rect(
        temp,
        color,
        (
            0,
            0,
            rect.width * scale,
            rect.height * scale
        ),
        width * scale,
        border_radius=30 * scale
    )


    temp = pygame.transform.smoothscale(
        temp,
        (
            rect.width,
            rect.height
        )
    )


    screen.blit(
        temp,
        rect
    )
    
    
    
    
    
    
    
#-------- برای دایره پروفایل در منو 
def create_profile_with_frame(
    frame_image,
    profile_image,
    frame_size,
    profile_size
):

    # تغییر اندازه قاب
    frame_image = pygame.transform.smoothscale(
        frame_image,
        (frame_size, frame_size)
    )


    # تغییر اندازه عکس کاربر
    profile_image = pygame.transform.smoothscale(
        profile_image,
        (profile_size, profile_size)
    )


    # دایره‌ای کردن عکس کاربر
    profile_surface = pygame.Surface(
        (profile_size, profile_size),
        pygame.SRCALPHA
    )


    profile_surface.blit(
        profile_image,
        (0,0)
    )


    mask = pygame.Surface(
        (profile_size, profile_size),
        pygame.SRCALPHA
    )


    pygame.draw.circle(
        mask,
        (255,255,255,255),
        (
            profile_size//2,
            profile_size//2
        ),
        profile_size//2
    )


    profile_surface.blit(
        mask,
        (0,0),
        special_flags=pygame.BLEND_RGBA_MULT
    )


    # ساخت خروجی
    result = pygame.Surface(
        (frame_size, frame_size),
        pygame.SRCALPHA
    )


    # قاب
    result.blit(
        frame_image,
        (0,0)
    )


    # وسط قرار دادن عکس
    pos = (
        (frame_size-profile_size)//2,
        (frame_size-profile_size)//2
    )


    result.blit(
        profile_surface,
        pos
    )


    return result
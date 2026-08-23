import pygame
from modules.hover import hover_image_music



# =========================
# تنظیمات اندازه‌ها
# =========================


# اندازه بک گراند پنل موزیک
BACKGROUND_SIZE = (1450,950)



# اندازه معمولی عکس‌ها
IMAGE_SIZE = 150


# اندازه هاور عکس‌ها
HOVER_SIZE = 180



# فاصله عکس‌ها
GAP_X = 167
GAP_Y = 90



# تعداد ستون و ردیف
COLUMNS = 3
ROWS = 3




profile_image = pygame.image.load(
    "./asset/image/music/music.png"
)



background_music = pygame.image.load(
    "./asset/image/music/music111.png"
)



background_music = pygame.transform.smoothscale(
    background_music,
    BACKGROUND_SIZE
)



music_rects = {}



music_files = {

    0: "./asset/music/1.mp3",
    1: "./asset/music/2.mp3",
    2: "./asset/music/3.mp3",
    3: "./asset/music/4.mp3",
    4: "./asset/music/5.mp3",
    5: "./asset/music/6.mp3",

}



current_music = -1


#music_state        برای وضعیت آهنگ است 
def play_music(index,music_state):

    global current_music


    # اگر موزیک خاموش باشد اجازه پخش نده
    if music_state == 0:
        return


    pygame.mixer.music.load(
        music_files[index]
    )


    pygame.mixer.music.set_volume(
        0.2
    )


    pygame.mixer.music.play(-1)


    current_music = index


# اندازه فعلی هر عکس برای انیمیشن هاور

profile_size = [

    IMAGE_SIZE,
    IMAGE_SIZE,
    IMAGE_SIZE,
    IMAGE_SIZE,
    IMAGE_SIZE,
    IMAGE_SIZE,
    IMAGE_SIZE,
    IMAGE_SIZE,
    IMAGE_SIZE

]




def draw_music(
    screen,
    current_width,
    current_height
):


    music_rects.clear()



    # -------------------------
    # بک گراند پنل
    # -------------------------

    music_panel_rect = background_music.get_rect(
        center=(
            current_width // 2,
            current_height // 2 +150
        )
    )


    screen.blit(
        background_music,
        music_panel_rect
    )



    # -------------------------
    # جای عکس‌ها
    # -------------------------


    total_width = (
        IMAGE_SIZE * COLUMNS +
        GAP_X * (COLUMNS - 1)
    )



    start_x = (
        music_panel_rect.centerx -
        total_width // 2
    )



    mouse_pos = pygame.mouse.get_pos()



    index = 0



    for row in range(ROWS):

        for col in range(COLUMNS):


            x = start_x + col * (
                IMAGE_SIZE + GAP_X
            )


            y = (
                music_panel_rect.y +
                160 +
                row * (
                    IMAGE_SIZE + GAP_Y
                )
            )



            music_rect = pygame.Rect(
                x,
                y,
                IMAGE_SIZE,
                IMAGE_SIZE
            )



            music_rects[index] = music_rect



            img, img_rect, profile_size[index] = hover_image_music(
                profile_image,
                music_rect,
                mouse_pos,
                profile_size[index]
            )


            screen.blit(
                img,
                img_rect
            )


            index += 1










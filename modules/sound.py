import pygame

from modules.EFFECT.slid_effect import draw_random_side_effect


# ============================================================
# SETTINGS
# ============================================================

MUSIC_SIZE = (200, 200)
SOUND_SIZE = (200, 200)

BUTTON_SIZE = (190, 190)

music_bar = None
sound_bar = None
# ============================================================
# LOAD MUSIC IMAGES
# ============================================================

music_icon = pygame.image.load(
    "./asset/image/music/music_.png"
).convert_alpha()

music_on = pygame.image.load(
    "./asset/image/music/on.png"
).convert_alpha()

music_off = pygame.image.load(
    "./asset/image/music/off.png"
).convert_alpha()


# ============================================================
# LOAD SOUND IMAGES
# ============================================================

sound_icon = pygame.image.load(
    "./asset/image/music/sound_.png"
).convert_alpha()

sound_on = pygame.image.load(
    "./asset/image/music/on.png"
).convert_alpha()

sound_off = pygame.image.load(
    "./asset/image/music/off.png"
).convert_alpha()


# ============================================================
# SCALE
# ============================================================

music_icon = pygame.transform.smoothscale(
    music_icon,
    MUSIC_SIZE
)

sound_icon = pygame.transform.smoothscale(
    sound_icon,
    SOUND_SIZE
)

music_on = pygame.transform.smoothscale(
    music_on,
    BUTTON_SIZE
)

music_off = pygame.transform.smoothscale(
    music_off,
    BUTTON_SIZE
)

sound_on = pygame.transform.smoothscale(
    sound_on,
    BUTTON_SIZE
)

sound_off = pygame.transform.smoothscale(
    sound_off,
    BUTTON_SIZE
)


# ============================================================
# STATES
# ============================================================

music_state = 1
sound_state = 1


# ============================================================
# RECT VARIABLES
# ============================================================

rect_for_music = None
rect_for_sound = None


# ============================================================
# SOUND SCREEN
# ============================================================

def sound_screen(screen):

    global rect_for_music
    global rect_for_sound
    global music_bar
    global sound_bar


    music_bar = draw_volume_bar(
        screen,
        1000,
        500,
        400,
        15,
        music_volume
    )

    sound_bar = draw_volume_bar(
        screen,
        1000,
        700,
        400,
        15,
        sound_volume
    )
    current_width, current_height = screen.get_size()

    # ========================================================
    # MUSIC POSITION
    # ========================================================

    music_x = current_width // 2 - 350
    music_y = current_height // 2 - 58

    # ========================================================
    # SOUND POSITION
    # ========================================================

    sound_x = current_width // 2 - 350
    sound_y = current_height // 2 + 260

    # ========================================================
    # MUSIC ICON
    # ========================================================

    draw_random_side_effect(
        screen,
        music_icon,
        music_x,
        music_y,
        1,
        3,
        image_size=200,
        duration=600,
        delay=120
    )

    # ========================================================
    # SOUND ICON
    # ========================================================

    draw_random_side_effect(
        screen,
        sound_icon,
        sound_x,
        sound_y,
        2,
        3,
        image_size=200,
        duration=600,
        delay=120
    )





    # ========================================================
    # MUSIC ON/OFF BUTTON
    # ========================================================

    current_music_button = (
        music_on
        if music_state == 1
        else music_off
    )

    rect_for_music = current_music_button.get_rect(
        center=(
            current_width // 2 + 350,
            current_height // 2 - 58
        )
    )

    screen.blit(
        current_music_button,
        rect_for_music
    )

    # ========================================================
    # SOUND ON/OFF BUTTON
    # ========================================================

    current_sound_button = (
        sound_on
        if sound_state == 1
        else sound_off
    )

    rect_for_sound = current_sound_button.get_rect(
        center=(
            current_width // 2 + 350,
            current_height // 2 + 260
        )
    )

    screen.blit(
        current_sound_button,
        rect_for_sound
    )
    
    
    
    
    
    
    
    
    
    
    
music_volume = 1.0
sound_volume = 1.0

music_bar = None
sound_bar = None

dragging_music = False
dragging_sound = False
#---------- این برای نوار تنظیم صدا است در این بازی اف 
def draw_volume_bar(
    screen,
    x,
    y,
    width,
    height,
    volume
):

    bar_rect = pygame.Rect(
        x,
        y,
        width,
        height
    )

    # نوار
    pygame.draw.rect(
        screen,
        (80, 80, 80),
        bar_rect,
        border_radius=height // 2
    )

    # قسمت پر شده
    fill_width = int(width * volume)

    if fill_width > 0:

        fill_rect = pygame.Rect(
            x,
            y,
            fill_width,
            height
        )

        pygame.draw.rect(
            screen,
            (230, 150, 50),
            fill_rect,
            border_radius=height // 2
        )

    # دایره
    knob_x = x + int(width * volume)

    pygame.draw.circle(
        screen,
        (255, 255, 255),
        (knob_x, y + height // 2),
        12
    )

    return bar_rect
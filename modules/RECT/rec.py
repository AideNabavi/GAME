import pygame


# تابع برای ساخت یک شکل فقط همین 
def create_smooth_rect(
    width,
    height,
    color,
    radius=20,
    alpha=255,
    shadow=15,
    shadow_alpha=180,
    scale=4
):
    padding = shadow

    temp = pygame.Surface(
        (
            (width + padding * 2) * scale,
            (height + padding * 2) * scale
        ),
        pygame.SRCALPHA
    )

    # -------------------------
    # Shadow
    # -------------------------

    for i in range(shadow, 0, -1):

        strength = (1 - (i / shadow)) ** 3

        current_alpha = int(
            shadow_alpha * strength
        )

        pygame.draw.rect(
            temp,
            (0, 0, 0, current_alpha),
            (
                (shadow - i) * scale,
                (shadow - i) * scale,
                (width + i * 2) * scale,
                (height + i * 2) * scale
            ),
            border_radius=(radius + i) * scale
        )

    # -------------------------
    # Main Rectangle
    # -------------------------

    pygame.draw.rect(
        temp,
        (*color[:3], alpha),
        (
            shadow * scale,
            shadow * scale,
            width * scale,
            height * scale
        ),
        border_radius=radius * scale
    )

    # -------------------------
    # Final
    # -------------------------

    return pygame.transform.smoothscale(
        temp,
        (
            width + padding * 2,
            height + padding * 2
        )
    )
    



    
    
    


#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
score_card = create_smooth_rect(
    250,
    100,
    (255, 255, 255),
    radius=130,
    alpha=255,
    shadow=10,
    shadow_alpha=40
)
xp_card = create_smooth_rect(
    250,
    100,
    (255, 255, 255),
    radius=130,
    alpha=255,
    shadow=10,
    shadow_alpha=40
)
time_card = create_smooth_rect(
    350,
    60,
    (255, 255, 255),
    radius=130,
    alpha=255,
    shadow=10,
    shadow_alpha=40
)

menu_card_over = create_smooth_rect(
    617,
    1500,
    (255, 240, 230),
    radius=20,
    alpha=255,
    shadow=10,
    shadow_alpha=50
)

tab_card = create_smooth_rect(
    600,
    300,
    (255, 255, 255),
    radius=0,
    alpha=255,
    shadow=20,
    shadow_alpha=100
)

down_card = create_smooth_rect(
    503,
    503,
    (255, 135, 40),
    radius=360,
    alpha=255,
    shadow=10,
    shadow_alpha=40
)
right_card = create_smooth_rect(
    550,
    800,
    (255, 255, 255),
    radius=130,
    alpha=255,
    shadow=10,
    shadow_alpha=50
)

start_card = create_smooth_rect(
    500,
    800,
    (255, 255, 255),
    radius=130,
    alpha=255,
    shadow=10,
    shadow_alpha=50
)
start_button_card = create_smooth_rect(
    300,
    120,
    (255, 135, 40),
    radius=130,
    alpha=255,
    shadow=0,
    shadow_alpha=0
)


game_guid_card = create_smooth_rect(
    1700,
    1100,
    (255, 255, 255),
    radius=90,
    alpha=255,
    shadow=20,
    shadow_alpha=100
)
icon_menu = create_smooth_rect(
    175,
    175,
    (255, 255, 255),
    radius=360,
    alpha=255,
    shadow=0,
    shadow_alpha=0
)


















##########################################################
##########################################################
##########################################################
##########################################################
#------------------------------------------------------------ تابع  سازنده start
# =========================================================
# START CARD
# =========================================================

start_card_state = {
    "start_time": None,
    "mouse_inside": False,
    "current_rect": pygame.Rect(0, 0, 0, 0)
}
other_card_state = {
    "start_time": None,
    "mouse_inside": False,
    "current_rect": pygame.Rect(0, 0, 0, 0)
}

rise_time = 1.5
marshmallow_time = 0.55

from modules.font import fonts

# =========================================================
# DRAW START CARD
# =========================================================

def draw_jelly_rect(
    screen,
    rect_surface,
    x,
    target_y,
    state,
    
    text_is_on,
    text="START",
    font=fonts["date"],
    text_color=(255, 255, 255),
    
    screen_height=1080,
    rise_time=1.5,
    stay_time=10.0,
    down_time=1.0,
    bottom_wait=1.0
):

    now = pygame.time.get_ticks() / 1000.0

    # --------------------------------
    # INITIALIZE
    # --------------------------------

    if state["start_time"] is None:

        state["start_time"] = now

    elapsed = now - state["start_time"]

    # --------------------------------
    # START POSITION
    # --------------------------------

    start_y = screen_height

    # --------------------------------
    # ORIGINAL SIZE
    # --------------------------------

    original_width = rect_surface.get_width()
    original_height = rect_surface.get_height()

    # =====================================================
    # 1. RISE
    # =====================================================
    if elapsed < rise_time:

        t = elapsed / rise_time

        # Ease Out
        t = 1 - (1 - t) ** 3

        y = (
            start_y
            + (target_y - start_y) * t
        )

        scale_x = 1.0
        scale_y = 1.0

    # =====================================================
    # 2. MARSHMALLOW
    # =====================================================

    elif elapsed < rise_time + marshmallow_time:

        t = (
            elapsed - rise_time
        ) / marshmallow_time

        # --------------------------------
        # PRESS
        # --------------------------------

        if t < 0.35:

            p = t / 0.35

            p = 1 - (1 - p) ** 2

            scale_x = 1.0 + 0.08 * p
            scale_y = 1.0 - 0.08 * p

        # --------------------------------
        # STRETCH
        # --------------------------------

        elif t < 0.65:

            p = (
                t - 0.35
            ) / 0.30

            p = 1 - (1 - p) ** 2

            scale_x = 1.08 - 0.10 * p
            scale_y = 0.92 + 0.12 * p

        # --------------------------------
        # RETURN
        # --------------------------------

        else:

            p = (
                t - 0.65
            ) / 0.35

            p = 1 - (1 - p) ** 2

            scale_x = 0.98 + 0.02 * p
            scale_y = 1.04 - 0.04 * p

        y = target_y

    # =====================================================
    # 3. STAY
    # =====================================================

    elif elapsed < (
        rise_time
        + marshmallow_time
        + stay_time
    ):

        y = target_y

        scale_x = 1.0
        scale_y = 1.0

    # =====================================================
    # 4. DOWN
    # =====================================================

    elif elapsed < (
        rise_time
        + marshmallow_time
        + stay_time
        + down_time
    ):

        t = (
            elapsed
            - rise_time
            - marshmallow_time
            - stay_time
        ) / down_time

        # Smooth
        t = t * t * (3 - 2 * t)

        y = (
            target_y
            + (start_y - target_y) * t
        )

        scale_x = 1.0
        scale_y = 1.0

    # =====================================================
    # 5. BOTTOM WAIT
    # =====================================================

    elif elapsed < (
        rise_time
        + marshmallow_time
        + stay_time
        + down_time
        + bottom_wait
    ):

        y = start_y

        scale_x = 1.0
        scale_y = 1.0

    # =====================================================
    # 6. RESTART AUTOMATICALLY
    # =====================================================

    else:

        state["start_time"] = now

        y = start_y

        scale_x = 1.0
        scale_y = 1.0

  # =====================================================
    # SCALE / DRAW
    # =====================================================

    if scale_x != 1.0 or scale_y != 1.0:

        new_width = int(original_width * scale_x)
        new_height = int(original_height * scale_y)

        scaled_surface = pygame.transform.smoothscale(
            rect_surface,
            (
                new_width,
                new_height
            )
        )

        # مرکز کارت ثابت بماند
        draw_x = (
            x
            - (new_width - original_width) // 2
        )

        draw_y = (
            int(y)
            - (new_height - original_height) // 2
        )

        # محدوده واقعی خود عکس
        state["current_rect"] = pygame.Rect(
            draw_x,
            draw_y,
            new_width,
            new_height
        )

        screen.blit(
            scaled_surface,
            (draw_x, draw_y)
        )
        if text_is_on and font is not None:

            text_surface = font.render(
                text,
                True,
                text_color
            )

            text_rect = text_surface.get_rect(
                center=state["current_rect"].center
            )

            screen.blit(
                text_surface,
                text_rect
            )
    else:

        draw_x = x
        draw_y = int(y)

        # محدوده واقعی خود عکس
        state["current_rect"] = pygame.Rect(
            draw_x,
            draw_y,
            original_width,
            original_height
        )

        screen.blit(
            rect_surface,
            (draw_x, draw_y)
        )
        if text_is_on and font is not None:

            text_surface = font.render(
                text,
                True,
                text_color
            )

            text_rect = text_surface.get_rect(
                center=state["current_rect"].center
            )

            screen.blit(
                text_surface,
                text_rect
            )
# =========================================================
# MOUSE EVENT
# =========================================================

def start_card_event(event, start_state, other_state):

    if event.type == pygame.MOUSEMOTION:

        mouse_pos = event.pos

        start_inside = start_state["current_rect"].collidepoint(
            mouse_pos
        )

        other_inside = other_state["current_rect"].collidepoint(
            mouse_pos
        )

        # ورود موس به یکی از کارت‌ها
        if (
            (start_inside and not start_state["mouse_inside"])
            or
            (other_inside and not other_state["mouse_inside"])
        ):

            now = pygame.time.get_ticks() / 1000.0

            start_state["start_time"] = now
            other_state["start_time"] = now

        start_state["mouse_inside"] = start_inside
        other_state["mouse_inside"] = other_inside



























#------------------------------------------------------------------------------- تابع سازنده  برای قسمت پروفایل
profile_image=pygame.transform.smoothscale(
        pygame.image.load(
            "./asset/image/menu/exit.png"
        ).convert_alpha(),
        (120,120)
        )
down_card_state = {
    "start_time": None,
    "finished": False
}
title_text="aiden"

def draw_down_card(
    screen,
    card_surface,
    x,
    target_y,
    state,
    duration=0.8,
    text=None,
    text_x=None,
    text_y_offset=0,
    font=None
):

    now = pygame.time.get_ticks() / 1000.0

    # --------------------------------
    # START
    # --------------------------------

    if state["start_time"] is None:
        state["start_time"] = now

    # --------------------------------
    # ANIMATION
    # --------------------------------

    if not state["finished"]:

        elapsed = now - state["start_time"]

        t = elapsed / duration

        if t >= 1.0:
            t = 1.0
            state["finished"] = True

        # Smooth Ease Out
        t = 1 - (1 - t) ** 3

        start_y = -card_surface.get_height()

        current_y = (
            start_y
            + (target_y - start_y) * t
        )

    else:
        current_y = target_y

    # --------------------------------
    # DRAW CARD
    # --------------------------------

    screen.blit(
        card_surface,
        (
            x,
            int(current_y)
        )
    )

    # --------------------------------
    # DRAW TEXT
    # --------------------------------

    if text is not None:

        text_surface = font.render(
            text,
            True,
            (255, 255, 255)
        )

        if text_x is None:
            text_x = x

        screen.blit(
            text_surface,
            (
                text_x,
                int(current_y + text_y_offset)
            )
        )

def reset_down_card(state):

    state["start_time"] = None
    state["finished"] = False












#########################################################################
#########################################################################
#########################################################################
#########################################################################
#------------------------------------------------------------------------------- تابع سازنده برای اسلاید  منو
image1=pygame.image.load("./asset/image/menu/status.png")
image2=pygame.image.load("./asset/image/menu/progress.png")
image3=pygame.image.load("./asset/image/menu/achievement.png")

right_card_state = {
    "start_time": None,
    "x": 1800,
    "target_x": 1800,
    "last_activity": 0,
    "first_show": True
}

right_images = [
    pygame.transform.smoothscale(image1, (90, 90)),
    pygame.transform.smoothscale(image2, (90, 90)),
    pygame.transform.smoothscale(image3, (90, 90))
]

right_texts = [
    "status",
    "progress",
    "achievement"
]
rect_S_P_A=[]
def draw_right_slide_card(
    screen,
    card_surface,
    visible_x,
    hidden_x,
    y,
    state,
    images,
    texts,
    font,
    mouse_trigger_x=500,
    hide_delay=5.0
):
    now = pygame.time.get_ticks() / 1000.0

    # --------------------------------
    # INITIALIZE
    # --------------------------------

    if state["start_time"] is None:

        state["start_time"] = now

        state["x"] = visible_x
        state["target_x"] = visible_x

        state["last_activity"] = now

    # --------------------------------
    # FIRST 1 SECOND
    # --------------------------------

    if state["first_show"]:

        if now - state["start_time"] >= 1.0:

            state["target_x"] = hidden_x
            state["first_show"] = False

    # --------------------------------
    # AUTO HIDE
    # --------------------------------

    elif now - state["last_activity"] >= hide_delay:

        state["target_x"] = hidden_x

    # --------------------------------
    # SMOOTH MOVEMENT
    # --------------------------------

    state["x"] += (
        state["target_x"] - state["x"]
    ) * 0.08

    # --------------------------------
    # SNAP
    # --------------------------------

    if abs(state["target_x"] - state["x"]) < 0.5:

        state["x"] = state["target_x"]

    # --------------------------------
    # DRAW 3 IMAGES + TEXT VERTICALLY
    # --------------------------------

    card_x = int(state["x"])

    screen.blit(
        card_surface,
        (card_x, y)
    )
    rect_S_P_A.clear()
    for i in range(3):

        image = images[i]

        # موقعیت عکس
        image_x = card_x + (
            card_surface.get_width() - image.get_width()
        ) // 2 - 155

        image_y = y + 100 + i * 250
        image_rect = image.get_rect(
            topleft=(image_x, image_y)
        )
        rect_S_P_A.append(image_rect)
        screen.blit(
            image,
            (image_x, image_y)
        )

        # متن زیر عکس
        text_surface = font.render(
            texts[i],
            True,
            (255, 135, 120)
        )

        text_rect = text_surface.get_rect(
            center=(
                image_x + image.get_width() // 2,
                image_y + image.get_height() + 30
            )
        )

        screen.blit(
            text_surface,
            text_rect
        )

def right_card_event(event, state):

    if event.type == pygame.MOUSEMOTION:
        mouse_x, mouse_y = event.pos

        # محدوده فعال‌سازی کارت
        if (
            mouse_x >= 1820
            and 200 <= mouse_y <= 900
        ):
            state["last_activity"] = pygame.time.get_ticks() / 1000.0
            state["target_x"] = 1800









































def create_two_smooth_rect(
    rect1,
    rect2,
    scale=4
):

    # =========================
    # RECT 1 SETTINGS
    # =========================

    width1, height1, color1, radius1, alpha1, shadow1, shadow_alpha1 = rect1

    padding1 = shadow1

    temp1 = pygame.Surface(
        (
            (width1 + padding1 * 2) * scale,
            (height1 + padding1 * 2) * scale
        ),
        pygame.SRCALPHA
    )

    # -------------------------
    # Shadow 1
    # -------------------------

    for i in range(shadow1, 0, -1):

        strength = (1 - (i / shadow1)) ** 3

        current_alpha = int(
            shadow_alpha1 * strength
        )

        pygame.draw.rect(
            temp1,
            (0, 0, 0, current_alpha),
            (
                (shadow1 - i) * scale,
                (shadow1 - i) * scale,
                (width1 + i * 2) * scale,
                (height1 + i * 2) * scale
            ),
            border_radius=(radius1 + i) * scale
        )

    # -------------------------
    # Main Rectangle 1
    # -------------------------

    pygame.draw.rect(
        temp1,
        (*color1[:3], alpha1),
        (
            shadow1 * scale,
            shadow1 * scale,
            width1 * scale,
            height1 * scale
        ),
        border_radius=radius1 * scale
    )

    # -------------------------
    # Final Rectangle 1
    # -------------------------

    rect1_image = pygame.transform.smoothscale(
        temp1,
        (
            width1 + padding1 * 2,
            height1 + padding1 * 2
        )
    )

    # =========================
    # RECT 2 SETTINGS
    # =========================

    width2, height2, color2, radius2, alpha2, shadow2, shadow_alpha2 = rect2

    padding2 = shadow2

    temp2 = pygame.Surface(
        (
            (width2 + padding2 * 2) * scale,
            (height2 + padding2 * 2) * scale
        ),
        pygame.SRCALPHA
    )

    # -------------------------
    # Shadow 2
    # -------------------------

    for i in range(shadow2, 0, -1):

        strength = (1 - (i / shadow2)) ** 3

        current_alpha = int(
            shadow_alpha2 * strength
        )

        pygame.draw.rect(
            temp2,
            (0, 0, 0, current_alpha),
            (
                (shadow2 - i) * scale,
                (shadow2 - i) * scale,
                (width2 + i * 2) * scale,
                (height2 + i * 2) * scale
            ),
            border_radius=(radius2 + i) * scale
        )

    # -------------------------
    # Main Rectangle 2
    # -------------------------

    pygame.draw.rect(
        temp2,
        (*color2[:3], alpha2),
        (
            shadow2 * scale,
            shadow2 * scale,
            width2 * scale,
            height2 * scale
        ),
        border_radius=radius2 * scale
    )

    # -------------------------
    # Final Rectangle 2
    # -------------------------

    rect2_image = pygame.transform.smoothscale(
        temp2,
        (
            width2 + padding2 * 2,
            height2 + padding2 * 2
        )
    )

    return rect1_image, rect2_image







regtangle_guid_page, circle_guid_page = create_two_smooth_rect(

    (
        1700,
        1100,
        (255, 255, 255),
        90,
        255,
        20,
        100
    ),

    (
        300,
        300,
        (50, 50, 50),
        100,
        50,
        0,
        0
    )
)
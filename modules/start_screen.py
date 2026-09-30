import pygame

from modules.font import fonts
from modules.SAVE import save as SAVE


# ==========================================================
# GLOBAL RECT / IMAGE
# ==========================================================

start_profile_rect = None
start_guest_rect = None

user_image_selected = None
gest_image_selected = None


# ==========================================================
# SIZE
# ==========================================================

MAIN_SIZE = (420, 420)
CENTER_SIZE = (450, 450)


# ==========================================================
# POSITION
# ==========================================================

CARD_GAP = 160

# فاصله اسم از پایین عکس
NAME_OFFSET_Y = 100


# ==========================================================
# CENTER IMAGES
# ==========================================================

profile_center_image = pygame.image.load(
    "asset/image/start_page.png"
).convert_alpha()

guest_center_image = pygame.image.load(
    "asset/image/start_page.png"
).convert_alpha()


# ==========================================================
# PRE-SCALED CENTER IMAGES
# ==========================================================

profile_center_base = pygame.transform.smoothscale(
    profile_center_image,
    CENTER_SIZE
)

guest_center_base = pygame.transform.smoothscale(
    guest_center_image,
    CENTER_SIZE
)


# ==========================================================
# HOVER
# ==========================================================

HOVER_DURATION = 160
HOVER_SCALE = 1.08


# ==========================================================
# ZOOM IN
# ==========================================================

ZOOM_DURATION = 500
ZOOM_START_SCALE = 0.50


# ==========================================================
# ROTATION
# ==========================================================

# درجه در ثانیه
#
# 5  = خیلی آرام
# 12 = آرام و مناسب
# 20 = سریع
#
ROTATE_SPEED = 12.0


# ==========================================================
# HOVER STATE
# ==========================================================

_profile_hover_start = 0
_guest_hover_start = 0

_profile_hovering = False
_guest_hovering = False

_profile_hover_scale = 1.0
_guest_hover_scale = 1.0


# ==========================================================
# ZOOM STATE
# ==========================================================

_start_zoom_start = None
_start_zoom_finished = False


# ==========================================================
# ROTATION STATE
# ==========================================================

_rotation_start = None


# ==========================================================
# TEXT WITH THIN BLACK STROKE
# ==========================================================

def draw_text_stroke(
    screen,
    text,
    font,
    center,
    text_color,
    stroke_color,
    stroke_width=1
):

    text_surface = font.render(
        text,
        True,
        text_color
    )

    rect = text_surface.get_rect(
        center=center
    )

    # ------------------------------------------------------
    # Thin stroke
    # ------------------------------------------------------

    for dx in range(
        -stroke_width,
        stroke_width + 1
    ):

        for dy in range(
            -stroke_width,
            stroke_width + 1
        ):

            if dx == 0 and dy == 0:
                continue

            screen.blit(
                text_surface,
                rect.move(dx, dy)
            )

    # ------------------------------------------------------
    # Main text
    # ------------------------------------------------------

    screen.blit(
        text_surface,
        rect
    )

    return rect


# ==========================================================
# ROTATION ANGLE
# ==========================================================

def get_rotation_angle():

    global _rotation_start

    now = pygame.time.get_ticks()

    # ------------------------------------------------------
    # Start
    # ------------------------------------------------------

    if _rotation_start is None:
        _rotation_start = now

    # ------------------------------------------------------
    # Elapsed time
    # ------------------------------------------------------

    elapsed = now - _rotation_start

    elapsed_seconds = elapsed / 1000.0

    # ------------------------------------------------------
    # Calculate angle
    # ------------------------------------------------------

    angle = (
        elapsed_seconds
        * ROTATE_SPEED
    )

    # ------------------------------------------------------
    # Keep between 0-360
    # ------------------------------------------------------

    angle %= 360

    return angle


# ==========================================================
# ROTATE CENTER IMAGE
# ==========================================================

def rotate_center_image(
    image,
    angle,
    center
):

    rotated_image = pygame.transform.rotate(
        image,
        angle
    )

    rotated_rect = rotated_image.get_rect(
        center=center
    )

    return (
        rotated_image,
        rotated_rect
    )


# ==========================================================
# ZOOM SCALE
# ==========================================================

def get_start_zoom_scale():

    global _start_zoom_start
    global _start_zoom_finished

    now = pygame.time.get_ticks()

    # ------------------------------------------------------
    # Start animation
    # ------------------------------------------------------

    if _start_zoom_start is None:

        _start_zoom_start = now

    # ------------------------------------------------------
    # Finished
    # ------------------------------------------------------

    if _start_zoom_finished:

        return 1.0

    # ------------------------------------------------------
    # Elapsed
    # ------------------------------------------------------

    elapsed = (
        now
        - _start_zoom_start
    )

    progress = min(
        elapsed / ZOOM_DURATION,
        1.0
    )

    # ------------------------------------------------------
    # Ease Out
    # ------------------------------------------------------

    progress = (
        1
        - (1 - progress) ** 3
    )

    # ------------------------------------------------------
    # 0.50 -> 1.0
    # ------------------------------------------------------

    scale = (
        ZOOM_START_SCALE
        + (
            1.0
            - ZOOM_START_SCALE
        ) * progress
    )

    # ------------------------------------------------------
    # Finished
    # ------------------------------------------------------

    if elapsed >= ZOOM_DURATION:

        _start_zoom_finished = True

        scale = 1.0

    return scale


# ==========================================================
# HOVER ANIMATION
# ==========================================================

def animate_hover(
    hovering,
    previous_hovering,
    start_time,
    start_scale,
    current_scale
):

    now = pygame.time.get_ticks()

    # ------------------------------------------------------
    # Hover state changed
    # ------------------------------------------------------

    if hovering != previous_hovering:

        start_time = now

        # شروع از Scale فعلی
        start_scale = current_scale

        previous_hovering = hovering

    # ------------------------------------------------------
    # Target
    # ------------------------------------------------------

    if hovering:

        target_scale = HOVER_SCALE

    else:

        target_scale = 1.0

    # ------------------------------------------------------
    # Progress
    # ------------------------------------------------------

    elapsed = (
        now
        - start_time
    )

    progress = min(
        elapsed / HOVER_DURATION,
        1.0
    )

    # ------------------------------------------------------
    # Smoothstep
    # ------------------------------------------------------

    progress = (
        progress
        * progress
        * (3 - 2 * progress)
    )

    # ------------------------------------------------------
    # Scale
    # ------------------------------------------------------

    scale = (
        start_scale
        + (
            target_scale
            - start_scale
        ) * progress
    )

    return (
        scale,
        start_time,
        previous_hovering
    )


# ==========================================================
# RESET ANIMATION
# ==========================================================

def reset_start_profile_animation():

    global _start_zoom_start
    global _start_zoom_finished

    global _profile_hover_start
    global _guest_hover_start

    global _profile_hovering
    global _guest_hovering

    global _profile_hover_scale
    global _guest_hover_scale

    global _rotation_start

    # ------------------------------------------------------
    # Zoom
    # ------------------------------------------------------

    _start_zoom_start = None
    _start_zoom_finished = False

    # ------------------------------------------------------
    # Rotation
    # ------------------------------------------------------

    _rotation_start = None

    # ------------------------------------------------------
    # Profile Hover
    # ------------------------------------------------------

    _profile_hover_start = pygame.time.get_ticks()

    _profile_hovering = False

    _profile_hover_scale = 1.0

    # ------------------------------------------------------
    # Guest Hover
    # ------------------------------------------------------

    _guest_hover_start = pygame.time.get_ticks()

    _guest_hovering = False

    _guest_hover_scale = 1.0


# ==========================================================
# DRAW START PROFILE
# ==========================================================

def draw_start_profile(
    screen,
    profile_images,
    selected_profile,
    player_name,
    center_x,
    y,
    profile_center_image=None,
    guest_center_image=None
):

    global user_image_selected
    global gest_image_selected

    global start_profile_rect
    global start_guest_rect

    global _profile_hover_start
    global _guest_hover_start

    global _profile_hovering
    global _guest_hovering

    global _profile_hover_scale
    global _guest_hover_scale

    # ======================================================
    # RESET RECT
    # ======================================================

    start_profile_rect = None
    start_guest_rect = None

    # ======================================================
    # MOUSE
    # ======================================================

    mouse_pos = pygame.mouse.get_pos()

    # ======================================================
    # ZOOM
    # ======================================================

    zoom_scale = get_start_zoom_scale()

    # ======================================================
    # ROTATION
    # ======================================================

    rotation_angle = get_rotation_angle()

    # ======================================================
    # LOAD SAVE
    # ======================================================

    saved_player = SAVE.load_player()

    if saved_player is not None:

        json_profile = saved_player.get(
            "avatar"
        )

        json_name = saved_player.get(
            "name",
            ""
        )

    else:

        json_profile = None
        json_name = ""

    # ======================================================
    # POSITION
    # ======================================================

    total_width = (
        MAIN_SIZE[0]
        + CARD_GAP
        + MAIN_SIZE[0]
    )

    left_x = (
        center_x
        - total_width // 2
    )

    profile_x = (
        left_x
        + MAIN_SIZE[0] // 2
    )

    guest_x = (
        left_x
        + MAIN_SIZE[0]
        + CARD_GAP
        + MAIN_SIZE[0] // 2
    )

    # ======================================================
    # PROFILE
    # ======================================================

    if (
        json_profile is not None
        and json_profile in profile_images
    ):

        original_profile = profile_images[
            json_profile
        ]

        # --------------------------------------------------
        # Selected images
        # --------------------------------------------------

        user_image_selected = (
            original_profile
        )

        if 10 in profile_images:

            gest_image_selected = (
                profile_images[10]
            )

        # --------------------------------------------------
        # Normal Rect
        # --------------------------------------------------

        normal_profile_rect = pygame.Rect(
            0,
            0,
            MAIN_SIZE[0],
            MAIN_SIZE[1]
        )

        normal_profile_rect.center = (
            profile_x,
            y
        )

        # --------------------------------------------------
        # Hover
        # --------------------------------------------------

        profile_hover = (
            normal_profile_rect.collidepoint(
                mouse_pos
            )
        )

        # --------------------------------------------------
        # Hover Animation
        # --------------------------------------------------

        (
            _profile_hover_scale,
            _profile_hover_start,
            _profile_hovering
        ) = animate_hover(
            profile_hover,
            _profile_hovering,
            _profile_hover_start,
            _profile_hover_scale,
            _profile_hover_scale
        )

        # --------------------------------------------------
        # Final Scale
        # --------------------------------------------------

        final_scale = (
            zoom_scale
            * _profile_hover_scale
        )

        # ==================================================
        # PROFILE IMAGE
        # ==================================================

        profile_size = (
            max(
                1,
                int(
                    MAIN_SIZE[0]
                    * final_scale
                )
            ),
            max(
                1,
                int(
                    MAIN_SIZE[1]
                    * final_scale
                )
            )
        )

        profile_image = pygame.transform.smoothscale(
            original_profile,
            profile_size
        )

        profile_rect = profile_image.get_rect(
            center=normal_profile_rect.center
        )

        screen.blit(
            profile_image,
            profile_rect
        )

        # ==================================================
        # ROTATING PROFILE CENTER
        # ==================================================

        if profile_center_image is not None:

            # اگر Hover/Zoom نیست
            if final_scale == 1.0:

                rotated_center_image, center_rect = (
                    rotate_center_image(
                        profile_center_base,
                        rotation_angle,
                        normal_profile_rect.center
                    )
                )

            else:

                center_size = (
                    max(
                        1,
                        int(
                            CENTER_SIZE[0]
                            * final_scale
                        )
                    ),
                    max(
                        1,
                        int(
                            CENTER_SIZE[1]
                            * final_scale
                        )
                    )
                )

                scaled_center = (
                    pygame.transform.smoothscale(
                        profile_center_image,
                        center_size
                    )
                )

                rotated_center_image = (
                    pygame.transform.rotate(
                        scaled_center,
                        rotation_angle
                    )
                )

                center_rect = (
                    rotated_center_image.get_rect(
                        center=normal_profile_rect.center
                    )
                )

            screen.blit(
                rotated_center_image,
                center_rect
            )

        # ==================================================
        # CLICK RECT
        # ==================================================

        start_profile_rect = (
            normal_profile_rect
        )

        # ==================================================
        # PROFILE NAME
        # ==================================================

        draw_text_stroke(
            screen,
            json_name,
            fonts["heart"],
            (
                normal_profile_rect.centerx,
                normal_profile_rect.bottom
                + NAME_OFFSET_Y
            ),
            (255, 140, 0),
            (0, 0, 0),
            1
        )

    # ======================================================
    # GUEST
    # ======================================================

    guest_profile_id = 10

    if guest_profile_id in profile_images:

        original_guest = profile_images[
            guest_profile_id
        ]

        # --------------------------------------------------
        # Normal Rect
        # --------------------------------------------------

        normal_guest_rect = pygame.Rect(
            0,
            0,
            MAIN_SIZE[0],
            MAIN_SIZE[1]
        )

        normal_guest_rect.center = (
            guest_x,
            y
        )

        # --------------------------------------------------
        # Hover
        # --------------------------------------------------

        guest_hover = (
            normal_guest_rect.collidepoint(
                mouse_pos
            )
        )

        # --------------------------------------------------
        # Hover Animation
        # --------------------------------------------------

        (
            _guest_hover_scale,
            _guest_hover_start,
            _guest_hovering
        ) = animate_hover(
            guest_hover,
            _guest_hovering,
            _guest_hover_start,
            _guest_hover_scale,
            _guest_hover_scale
        )

        # --------------------------------------------------
        # Final Scale
        # --------------------------------------------------

        final_scale = (
            zoom_scale
            * _guest_hover_scale
        )

        # ==================================================
        # GUEST IMAGE
        # ==================================================

        guest_size = (
            max(
                1,
                int(
                    MAIN_SIZE[0]
                    * final_scale
                )
            ),
            max(
                1,
                int(
                    MAIN_SIZE[1]
                    * final_scale
                )
            )
        )

        guest_image = pygame.transform.smoothscale(
            original_guest,
            guest_size
        )

        guest_rect = guest_image.get_rect(
            center=normal_guest_rect.center
        )

        screen.blit(
            guest_image,
            guest_rect
        )

        # ==================================================
        # ROTATING GUEST CENTER
        # ==================================================

        if guest_center_image is not None:

            if final_scale == 1.0:

                rotated_center_image, center_rect = (
                    rotate_center_image(
                        guest_center_base,
                        rotation_angle,
                        normal_guest_rect.center
                    )
                )

            else:

                center_size = (
                    max(
                        1,
                        int(
                            CENTER_SIZE[0]
                            * final_scale
                        )
                    ),
                    max(
                        1,
                        int(
                            CENTER_SIZE[1]
                            * final_scale
                        )
                    )
                )

                scaled_center = (
                    pygame.transform.smoothscale(
                        guest_center_image,
                        center_size
                    )
                )

                rotated_center_image = (
                    pygame.transform.rotate(
                        scaled_center,
                        rotation_angle
                    )
                )

                center_rect = (
                    rotated_center_image.get_rect(
                        center=normal_guest_rect.center
                    )
                )

            screen.blit(
                rotated_center_image,
                center_rect
            )

        # ==================================================
        # CLICK RECT
        # ==================================================

        start_guest_rect = (
            normal_guest_rect
        )

        # ==================================================
        # GUEST NAME
        # ==================================================

        draw_text_stroke(
            screen,
            "Guest",
            fonts["heart"],
            (
                normal_guest_rect.centerx,
                normal_guest_rect.bottom
                + NAME_OFFSET_Y
            ),
            (255, 140, 0),
            (0, 0, 0),
            1
        )

    # ======================================================
    # RETURN
    # ======================================================

    return (
        start_profile_rect,
        start_guest_rect
    )






# --------------------------------------------------------------
# کلیک روی پروفایل یا Guest در صفحه START
# --------------------------------------------------------------

def start_profile_click(
    mouse_pos,
    profile_rect,
    guest_rect
):

    # کلیک روی پروفایل اصلی
    if profile_rect is not None:

        if profile_rect.collidepoint(mouse_pos):

            return "PROFILE"


    # کلیک روی Guest
    if guest_rect is not None:

        if guest_rect.collidepoint(mouse_pos):

            return "GUEST"


    return None














# برای کشیدن عکس در منو  عکس پروفایل یا گست در منو 

current_player_type = None
image_current_user = None



dashboard_player_profile= pygame.image.load(
    "./asset/image/wood.png"
).convert_alpha()


def draw_current_player(
    screen,
    profile_images,
    current_player_type,
    center,background_image):

    # ----------------------------------------------------------
    # انتخاب بازیکن
    # ----------------------------------------------------------
    global image_current_user
    if current_player_type == "PROFILE":

        saved_player = SAVE.load_player()

        if saved_player is None:
            return

        avatar_id = saved_player.get("avatar")

        if avatar_id not in profile_images:
            return

        image = profile_images[avatar_id]
        name = saved_player.get("name", "")

    elif current_player_type == "GUEST":

        avatar_id = 10
        image = profile_images[avatar_id]
        name = "Guest"

    else:
        return

    # ----------------------------------------------------------
    # عکس اصلی
    # ----------------------------------------------------------

    image = pygame.transform.smoothscale(
        image,
        (83, 83)
    )
    image_current_user=image

    rect = image.get_rect(
        center=center
    )

    # ----------------------------------------------------------
    # عکس پشت - 10 درصد بزرگ‌تر
    # ----------------------------------------------------------

    background_size = int(100 * 1.2)

    background_image = pygame.transform.smoothscale(
        background_image,
        (background_size, background_size)
    )

    background_rect = background_image.get_rect(
        center=center
    )

    # اول عکس پشت
    screen.blit(
        background_image,
        background_rect
    )

    # بعد آواتار اصلی
    screen.blit(
        image,
        rect
    )
    # ----------------------------------------------------------
    # اسم
    # ----------------------------------------------------------

    name_surface = fonts["profile_"].render(
        name,
        True,
        (238, 220, 180))

    name_rect = name_surface.get_rect(
        center=(
            rect.centerx,
            rect.bottom + 40
        )
    )

    screen.blit(
        name_surface,
        name_rect
    )

    return rect
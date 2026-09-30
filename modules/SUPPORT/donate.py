# =========================================================
# DONATE PAGE
# =========================================================

import pygame


window_pop_up=pygame.transform.smoothscale(pygame.image.load("./asset/image/index.png").convert_alpha(),(600,400))
# =========================================================
# DONATE DATA
# =========================================================

donate_popup_open = False
selected_payment_method = None
# =========================================================
# DONATE POPUP ZOOM ANIMATION
# =========================================================

donate_popup_zoom_start = 0
DONATE_POPUP_ZOOM_DURATION = 300

# =========================================================
# POSITIONS
# =========================================================

DONATE_START_Y = 170

PAYMENT_START_Y = 400


# =========================================================
# PAYMENT CARD SETTINGS
# =========================================================

PAYMENT_CARD_WIDTH = 220
PAYMENT_CARD_HEIGHT = 180

PAYMENT_GAP = 60


# =========================================================
# PAYMENT METHODS
# =========================================================

PAYMENT_METHODS = [

    {
        "name": "PayPal",
        "image": "./asset/image/donate/2.png"
    },

    {
        "name": "Crypto",
        "image": "./asset/image/donate/1.png"
    },

    {
        "name": "Card",
        "image": "./asset/image/donate/3.png"
    },

    {
        "name": "others",
        "image": "./asset/image/donate/4.png"
    }
]


# =========================================================
# PAYMENT IMAGE SIZE
# =========================================================

PAYMENT_IMAGE_SIZE = (
    200,
    200
)


# =========================================================
# LOAD PAYMENT IMAGES
# =========================================================

payment_images = {}


def load_donate_images():

    global payment_images

    payment_images.clear()

    for payment in PAYMENT_METHODS:

        try:

            image = pygame.image.load(
                payment["image"]
            ).convert_alpha()

            image = pygame.transform.smoothscale(
                image,
                PAYMENT_IMAGE_SIZE
            )

            payment_images[
                payment["name"]
            ] = image

        except Exception as e:

            print(
                "DONATE IMAGE ERROR:",
                payment["image"],
                e
            )

            payment_images[
                payment["name"]
            ] = None


# =========================================================
# PAYMENT CARD RECTS
# =========================================================

payment_rects = []

# =========================================================
# DRAW DONATE POPUP
# =========================================================

def draw_donate_popup(screen):

    global donate_popup_open
    global selected_payment_method

    if not donate_popup_open:
        return

    if not selected_payment_method:
        return

    # =====================================================
    # DARK OVERLAY
    # =====================================================

    overlay = pygame.Surface(
        screen.get_size(),
        pygame.SRCALPHA
    )

    overlay.fill(
        (
            0,
            0,
            0,
            150
        )
    )

    screen.blit(
        overlay,
        (0, 0)
    )

    # =====================================================
    # ZOOM ANIMATION
    # =====================================================

    elapsed = (
        pygame.time.get_ticks()
        - donate_popup_zoom_start
    )

    progress = min(
        elapsed / DONATE_POPUP_ZOOM_DURATION,
        1
    )

    # شروع Popup از 60 درصد
    start_scale = 0.6

    scale = (
        start_scale
        +
        (1 - start_scale) * progress
    )

    # =====================================================
    # SCALE POPUP WINDOW
    # =====================================================

    popup_width = int(
        window_pop_up.get_width() * scale
    )

    popup_height = int(
        window_pop_up.get_height() * scale
    )

    popup_image = pygame.transform.smoothscale(
        window_pop_up,
        (
            popup_width,
            popup_height
        )
    )

    # =====================================================
    # CENTER POPUP
    # =====================================================

    popup_rect = popup_image.get_rect(
        center=(
            screen.get_width() // 2,
            screen.get_height() // 2
        )
    )

    screen.blit(
        popup_image,
        popup_rect
    )

    # =====================================================
    # PAYMENT IMAGE INSIDE POPUP
    # =====================================================

    payment_image = payment_images.get(
        selected_payment_method
    )

    if payment_image is not None:

        content_size = int(
            180 * scale
        )

        content_image = pygame.transform.smoothscale(
            payment_image,
            (
                content_size,
                content_size
            )
        )

        content_rect = content_image.get_rect(
            center=popup_rect.center
        )

        screen.blit(
            content_image,
            content_rect
        )
    
    
    
# =========================================================
# DRAW DONATE PAGE
# =========================================================


def draw_donate(
    screen,
    font,
    current_x=None,
    current_y=DONATE_START_Y
):

    global payment_rects

    # =====================================================
    # SCREEN CENTER
    # =====================================================

    screen_width = screen.get_width()

    center_x = (
        screen_width // 2
    )

    # =====================================================
    # COLORS
    # =====================================================

    title_color = (
        255,
        255,
        255
    )

    text_color = (
        255,
        255,
        255
    )

    payment_name_color = (
        50,
        35,
        25
    )

    # =====================================================
    # MOUSE
    # =====================================================

    mouse_pos = pygame.mouse.get_pos()

    # =====================================================
    # TITLE
    # =====================================================

    title_surface = font.render(
        "SUPPORT GAME CLUB",
        True,
        title_color
    )

    title_rect = title_surface.get_rect(
        center=(
            center_x,
            current_y
        )
    )

    screen.blit(
        title_surface,
        title_rect
    )

    # =====================================================
    # DESCRIPTION
    # =====================================================

    description_1 = font.render(
        "Help us develop and create",
        True,
        text_color
    )

    description_2 = font.render(
        "more brain games.",
        True,
        text_color
    )

    rect_1 = description_1.get_rect(
        center=(
            center_x,
            current_y + 55
        )
    )

    rect_2 = description_2.get_rect(
        center=(
            center_x,
            current_y + 90
        )
    )

    screen.blit(
        description_1,
        rect_1
    )

    screen.blit(
        description_2,
        rect_2
    )

    # =====================================================
    # CHOOSE PAYMENT METHOD
    # =====================================================

    choose_surface = font.render(
        "Choose a payment method",
        True,
        text_color
    )

    choose_rect = choose_surface.get_rect(
        center=(
            center_x,
            current_y + 175
        )
    )

    screen.blit(
        choose_surface,
        choose_rect
    )

    # =====================================================
    # PAYMENT SETTINGS
    # =====================================================

    PAYMENT_Y = 900

    PAYMENT_GAP = 80

    image_width = PAYMENT_IMAGE_SIZE[0]

    # =====================================================
    # TOTAL WIDTH
    # =====================================================

    total_width = (
        image_width * 4
        +
        PAYMENT_GAP * 3
    )

    # =====================================================
    # FIRST IMAGE X
    # =====================================================

    first_x = (
        center_x -
        total_width // 2
    )

    # =====================================================
    # IMAGE POSITIONS
    # =====================================================

    positions = [

        (
            first_x,
            PAYMENT_Y
        ),

        (
            first_x +
            image_width +
            PAYMENT_GAP,
            PAYMENT_Y
        ),

        (
            first_x +
            (
                image_width +
                PAYMENT_GAP
            ) * 2,
            PAYMENT_Y
        ),

        (
            first_x +
            (
                image_width +
                PAYMENT_GAP
            ) * 3,
            PAYMENT_Y
        )
    ]

    # =====================================================
    # CLEAR CLICK RECTS
    # =====================================================

    payment_rects.clear()

    # =====================================================
    # DRAW PAYMENT IMAGES
    # =====================================================

    for payment, position in zip(
        PAYMENT_METHODS,
        positions
    ):

        image = payment_images.get(
            payment["name"]
        )

        if not image:
            continue

        # =================================================
        # IMAGE RECT
        # =================================================

        image_rect = image.get_rect(
            topleft=position
        )

        # =================================================
        # SAVE CLICK RECT
        # =================================================

        payment_rects.append(
            (
                image_rect,
                payment["name"]
            )
        )

        # =================================================
        # HOVER
        # =================================================

        if image_rect.collidepoint(
            mouse_pos
        ):

            # کمی بزرگ‌تر شدن هنگام Hover
            hover_image = pygame.transform.smoothscale(
                image,
                (
                    int(
                        PAYMENT_IMAGE_SIZE[0] * 1.08
                    ),
                    int(
                        PAYMENT_IMAGE_SIZE[1] * 1.08
                    )
                )
            )

            hover_rect = hover_image.get_rect(
                center=image_rect.center
            )

            screen.blit(
                hover_image,
                hover_rect
            )

        else:

            screen.blit(
                image,
                image_rect
            )

        # =================================================
        # PAYMENT NAME
        # =================================================

        name_surface = font.render(
            payment["name"],
            True,
            payment_name_color
        )

        name_rect = name_surface.get_rect(
            center=(
                image_rect.centerx,
                image_rect.bottom + 30
            )
        )

        screen.blit(
            name_surface,
            name_rect
        )

    # =====================================================
    # THANK YOU
    # =====================================================

    thank_you_1 = font.render(
        "Thank you",
        True,
        text_color
    )

    thank_you_2 = font.render(
        "for your support ❤️",
        True,
        text_color
    )

    thank_rect_1 = thank_you_1.get_rect(
        center=(
            center_x,
            PAYMENT_Y +
            PAYMENT_IMAGE_SIZE[1] +
            90
        )
    )

    thank_rect_2 = thank_you_2.get_rect(
        center=(
            center_x,
            PAYMENT_Y +
            PAYMENT_IMAGE_SIZE[1] +
            125
        )
    )

    screen.blit(
        thank_you_1,
        thank_rect_1
    )

    screen.blit(
        thank_you_2,
        thank_rect_2
    )

    # =====================================================
    # DONATE POPUP
    # =====================================================

    draw_donate_popup(
        screen
    )








def reset_donate_popup_animation():

    global donate_popup_zoom_start

    donate_popup_zoom_start = pygame.time.get_ticks()
    
    
    
    
    
    
    
    





# =========================================================
# HANDLE DONATE EVENT
# =========================================================

def handle_donate_event(event):

    global donate_popup_open
    global selected_payment_method

    # =====================================================
    # MOUSE CLICK
    # =====================================================

    if event.type == pygame.MOUSEBUTTONDOWN:

        # =================================================
        # LEFT CLICK
        # =================================================

        if event.button == 1:

            # =================================================
            # POPUP IS OPEN
            # =================================================

            if donate_popup_open:

                # ---------------------------------------------
                # CLOSE BUTTON
                # ---------------------------------------------

                screen_width = pygame.display.get_surface().get_width()
                screen_height = pygame.display.get_surface().get_height()

                popup_width = 520
                popup_height = 320

                popup_rect = pygame.Rect(
                    0,
                    0,
                    popup_width,
                    popup_height
                )

                popup_rect.center = (
                    screen_width // 2,
                    screen_height // 2
                )

                close_rect = pygame.Rect(
                    0,
                    0,
                    140,
                    50
                )

                close_rect.center = (
                    popup_rect.centerx,
                    popup_rect.bottom - 55
                )

                if close_rect.collidepoint(
                    event.pos
                ):

                    donate_popup_open = False
                    selected_payment_method = None

                    return

                # ---------------------------------------------
                # جلوگیری از کلیک روی صفحه پشت Modal
                # ---------------------------------------------

                return

            # =================================================
            # PAYMENT CARDS
            # =================================================

            for rect, payment_name in payment_rects:

                if rect.collidepoint(
                    event.pos
                ):

                    selected_payment_method = (
                        payment_name
                    )

                    donate_popup_open = True
                    reset_donate_popup_animation()
                    return
from modules.support import *
import pygame
from modules.font import *

from modules import policy as PO


def open_window_with_side_effect(
    screen,
    image,
    x,
    y,
    on_draw=None
):

    if not hasattr(open_window_with_side_effect, "start_time"):
        open_window_with_side_effect.start_time = pygame.time.get_ticks()

    now = pygame.time.get_ticks()

    elapsed = (
        now - open_window_with_side_effect.start_time
    )

    duration = 600

    if elapsed >= duration:
        progress = 1.0
    else:
        progress = elapsed / duration
        progress = 1 - (1 - progress) ** 3

    start_x = (
        screen.get_width()
        + image.get_width()
    )

    current_x = (
        start_x
        + (x - start_x) * progress
    )

    rect = image.get_rect(
        center=(int(current_x), y)
    )

    # پنجره
    screen.blit(
        image,
        rect
    )

    # تابع جانبی
    if on_draw:
        on_draw(
            screen,
            rect
        )



































# ============================================================
# RESET
# ============================================================

def reset_window_side_effect():

    if hasattr(
        open_window_with_side_effect,
        "start_time"
    ):

        del open_window_with_side_effect.start_time
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
#------------------------------------------------- تابع ساید افکت با   چند تصویره 

info_________ = pygame.image.load(
    "asset/image/support/info.png"
).convert_alpha()

info_________ = pygame.transform.smoothscale(
    info_________,
    (200, 200)
)









faq__________ = pygame.image.load(
    "asset/image/support/faq.png"
).convert_alpha()

faq__________ = pygame.transform.smoothscale(
    faq__________,
    (200, 200)
)


# moreapp_____ = pygame.image.load(
#     "asset/image/support/How.png"
# ).convert_alpha()

# moreapp_____ = pygame.transform.smoothscale(
#     moreapp_____,
#     (200, 200)
# )


policy_______ = pygame.image.load(
    "asset/image/support/policy.png"
).convert_alpha()

policy_______ = pygame.transform.smoothscale(
    policy_______,
    (200, 200)
)




# moreapp=[
#         # (image____1, 300, 500),
#         # (image____2, 300, 750),
#         (moreapp_____, 1000, 150)
#     ]
faqq=[
        # (image____1, 300, 500),
        # (image____2, 300, 750),
        (faq__________, 1020, 150)
    ]
infoo=[
        # (image____1, 300, 500),
        # (image____2, 300, 750),
        (info_________, 1020, 150)
    ]
policyy=[
        # (image____1, 300, 500),
        # (image____2, 300, 750),
        (policy_______, 1020, 150)
    ]
def open_window_with_side_effect_MULLTI_WINDOW(
    screen,
    image,
    x,
    y,
    images,
    text=None,
    text_font=None,
    text_color=(255, 255, 255),
    text_x=0,
    text_y=0,
    on_draw=None
):

    # ========================================================
    # START TIME
    # ========================================================

    if not hasattr(
        open_window_with_side_effect_MULLTI_WINDOW,
        "start_time"
    ):

        open_window_with_side_effect_MULLTI_WINDOW.start_time = (
            pygame.time.get_ticks()
        )

    now = pygame.time.get_ticks()

    elapsed = (
        now
        - open_window_with_side_effect_MULLTI_WINDOW.start_time
    )

    duration = 600

    if elapsed >= duration:

        progress = 1.0

    else:

        progress = elapsed / duration

        # Ease Out
        progress = 1 - (1 - progress) ** 3


    # ========================================================
    # HELPER: SLIDE FROM RIGHT
    # ========================================================

    def slide_x(target_x, element_width):

        start_x = (
            screen.get_width()
            + element_width
        )

        current_x = (
            start_x
            + (target_x - start_x) * progress
        )

        return int(current_x)


    # ========================================================
    # MAIN IMAGE
    # ========================================================

    current_x = slide_x(
        x,
        image.get_width()
    )

    rect = image.get_rect(
        center=(
            current_x,
            y
        )
    )

    screen.blit(
        image,
        rect
    )


    # ========================================================
    # ON DRAW
    # ========================================================

    if on_draw:

        on_draw(
            screen,
            rect
        )


    # ========================================================
    # EXTRA IMAGES
    # ========================================================

    for extra_image, extra_x, extra_y in images:

        current_x = slide_x(
            extra_x,
            extra_image.get_width()
        )

        extra_rect = extra_image.get_rect(
            center=(
                current_x,
                extra_y
            )
        )

        screen.blit(
            extra_image,
            extra_rect
        )


    # ========================================================
    # TEXT
    # ========================================================

    if text is not None and text_font is not None:

        text_surface = text_font.render(
            text,
            True,
            text_color
        )

        current_x = slide_x(
            text_x,
            text_surface.get_width()
        )

        text_rect = text_surface.get_rect(
            center=(
                current_x,
                text_y
            )
        )

        screen.blit(
            text_surface,
            text_rect
        )
        
        
        
        
        
        
        
        
        
# ============================================================
# RESET MULTI WINDOW SIDE EFFECT
# ============================================================

def reset_window_side_effect_MULLTI_WINDOW():

    if hasattr(
        open_window_with_side_effect_MULLTI_WINDOW,
        "start_time"
    ):

        del open_window_with_side_effect_MULLTI_WINDOW.start_time
        
        
        
        
        
        
        
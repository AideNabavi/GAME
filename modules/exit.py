import pygame

from modules.EFFECT.effect import (
    punch_scale_animation
)


# ============================================================
# IMAGES
# ============================================================

exit_yes = pygame.transform.smoothscale(
    pygame.image.load(
        "./asset/image/yes.png"
    ).convert_alpha(),
    (300, 300)
)

exit_no = pygame.transform.smoothscale(
    pygame.image.load(
        "./asset/image/no.png"
    ).convert_alpha(),
    (300, 300)
)


# ============================================================
# RECT
# ============================================================

yes_rect = None
no_rect = None



# ============================================================
# DRAW
# ============================================================

def draw_exit_confirmation(screen):

    global yes_rect
    global no_rect

    # ========================================================
    # PUNCH SCALE
    # ========================================================

    yes_scale = punch_scale_animation(
        "exit",
        0
    )

    no_scale = punch_scale_animation(
        "exit",
        1
    )

    # ========================================================
    # YES IMAGE SCALE
    # ========================================================

    yes_width = max(
        1,
        int(exit_yes.get_width() * yes_scale)
    )

    yes_height = max(
        1,
        int(exit_yes.get_height() * yes_scale)
    )

    yes_image = pygame.transform.smoothscale(
        exit_yes,
        (yes_width, yes_height)
    )

    # ========================================================
    # NO IMAGE SCALE
    # ========================================================

    no_width = max(
        1,
        int(exit_no.get_width() * no_scale)
    )

    no_height = max(
        1,
        int(exit_no.get_height() * no_scale)
    )

    no_image = pygame.transform.smoothscale(
        exit_no,
        (no_width, no_height)
    )

    # ========================================================
    # CENTER
    # ========================================================

    center_x = screen.get_width() // 2
    center_y = screen.get_height() // 2

    # ========================================================
    # RECT
    # ========================================================

    yes_rect = yes_image.get_rect(
        center=(
            center_x - 200,
            center_y
        )
    )

    no_rect = no_image.get_rect(
        center=(
            center_x + 200,
            center_y
        )
    )

    # ========================================================
    # DRAW
    # ========================================================

    screen.blit(
        yes_image,
        yes_rect
    )

    screen.blit(
        no_image,
        no_rect
    )
    
    
    
    
    
    
    
def reset_exit_animation():

    if hasattr(punch_scale_animation, "animations"):

        punch_scale_animation.animations.pop(
            "exit",
            None
        )
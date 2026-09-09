import pygame
from modules.font import fonts






# ============================================================
# INFO TEXT
# ============================================================

info_text = """
INFO

==================================================

Mental Math Challenge

Version: 1.0.0


About The Developer

Created by:
Aiden Nabavi


Mental Math Challenge is a brain training game
designed to improve calculation skills, focus,
memory, and logical thinking.


==================================================


Technology

This game is developed using:

• Python
• Pygame
• PyTorch (Future AI Features)
• Git / GitHub


==================================================


Development

The game is built with Python and Pygame,
focusing on performance, clean design,
and an enjoyable user experience.


==================================================


Features

• Multiple game modes
• Difficulty levels
• Score system
• Player profiles
• Language support
• Custom settings
• Brain challenges


==================================================


Developer Contact

GitHub:
github.com/YourUsername


Email:
your-email@example.com


==================================================


Thank you for supporting
Mental Math Challenge.


Keep training your brain!
"""

scroll_y = 0
scroll_velocity = 0

friction = 0.94


def draw_FAQ(screen, privacy_box):

    global scroll_y
    global scroll_velocity

    # ============================================================
    # SCROLL
    # ============================================================

    scroll_y += scroll_velocity

    scroll_velocity *= friction

    if abs(scroll_velocity) < 0.1:
        scroll_velocity = 0

    # ============================================================
    # LIMIT
    # ============================================================

    if scroll_y < 0:
        scroll_y = 0
        scroll_velocity = 0

    if scroll_y > 8000:
        scroll_y = 8000
        scroll_velocity = 0

    # ============================================================
    # CLIP
    # ============================================================

    screen.set_clip(privacy_box)

    # ============================================================
    # TEXT
    # ============================================================

    y = privacy_box.y + 40 - scroll_y

    for line in info_text.split("\n"):

        text = fonts["more and support"].render(
            line,
            True,
            (60, 60, 60)
        )

        screen.blit(
            text,
            (
                privacy_box.x + 40,
                y
            )
        )

        y += 45

    # ============================================================
    # REMOVE CLIP
    # ============================================================

    screen.set_clip(None)


def FAQ_event(event):

    global scroll_velocity

    if event.type == pygame.MOUSEWHEEL:

        scroll_velocity += event.y * 20
    
    
    
    
    
    
    
    
    
    
    
    
    

# ============================================================
# PRIVACY POLICY 
# ============================================================

def draw_FAQ_(screen, rect):

    # ------------------------------------------------------------
    # Privacy box نسبت به خود پنجره
    # ------------------------------------------------------------

    privacy_box = pygame.Rect(

        rect.centerx - 370,
        rect.centery - 275,

        740,
        550
    )

    # ------------------------------------------------------------
    # Draw Privacy Policy
    # ------------------------------------------------------------

    draw_FAQ(
        screen,
        privacy_box
    )

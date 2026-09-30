import pygame
from modules.font import fonts
from modules.TRANSLATE import policy




from modules.language import  * 
from modules.language import  get_language_font 
PRIVACY_TITLE_COLOR = (60, 60, 60)
PRIVACY_DATE_COLOR = (120, 80, 40)
PRIVACY_SECTION_COLOR = (120, 80, 40)

PRIVACY_TEXT_COLOR = (60, 60, 60)

import re



scroll_y = 0
scroll_velocity = 0

friction = 0.94





def draw_privacy_policy(screen, privacy_box):

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

    if scroll_y > 9000:
        scroll_y = 9000
        scroll_velocity = 0

    # ============================================================
    # CLIP
    # ============================================================

    screen.set_clip(privacy_box)
    font_title=get_language_font("support")
    font_date=get_language_font("date")
    # ============================================================
    # TEXT
    # ============================================================
    language = policy.now_language_is_this

    if language == "ru":
        xxx = policy.ru
    elif language == "fa":
        xxx = policy.fa
    elif language == "en":
        xxx = policy.en
    elif language == "zh":
        xxx = policy.zh
    elif language == "ar":
        xxx = policy.ar
    elif language == "hi":
        xxx = policy.hi
    else:
        xxx = policy.en
    y = privacy_box.y + 40 - scroll_y
    
    
    prepared_lines = [
        prepare_privacy_text(line, language)
        for line in xxx.split("\n")
    ]

    for line in prepared_lines:

        stripped_line = line.strip()
        # ========================================================
        # MAIN TITLE
        # ========================================================


        if stripped_line == "Privacy Policy":

            text = font_title.render(
                line,
                True,
                PRIVACY_TITLE_COLOR
            )

            line_height = 60

        # ========================================================
        # LAST UPDATED
        # ========================================================

        elif stripped_line.startswith("Last Updated:"):

            text = font_title.render(
                line,
                True,
                PRIVACY_DATE_COLOR
            )

            line_height = 50

        # ========================================================
        # SECTION TITLES
        # 1. / 2. / 3. / ... / 10.
        # ========================================================

        elif re.match(r"^\d+\.\s", stripped_line):

            text = font_date.render(
                line,
                True,
                PRIVACY_SECTION_COLOR
            )

            line_height = 50

        # ========================================================
        # NORMAL TEXT
        # ========================================================

        else:

            text = font_date.render(
                line,
                True,
                PRIVACY_TEXT_COLOR
            )

            line_height = 45

        # ========================================================
        # DRAW
        # ========================================================

        screen.blit(
            text,
            (
                privacy_box.x + 40,
                y
            )
        )

        y += line_height

    # ============================================================
    # REMOVE CLIP
    # ============================================================

    screen.set_clip(None)


def privacy_event(event):

    global scroll_velocity

    if event.type == pygame.MOUSEWHEEL:

        scroll_velocity += event.y * 20
    
    
    
    
    
    
    
    
    
    
    
    
    

# ============================================================
# PRIVACY POLICY 
# ============================================================

def draw_privacy_side_effect(screen, rect):

    # ------------------------------------------------------------
    # Privacy box نسبت به خود پنجره
    # ------------------------------------------------------------

    privacy_box = pygame.Rect(

        rect.centerx - 440,
        rect.centery - 330,

        870,
        810
    )

    # ------------------------------------------------------------
    # Draw Privacy Policy
    # ------------------------------------------------------------

    draw_privacy_policy(
        screen,
        privacy_box
    )

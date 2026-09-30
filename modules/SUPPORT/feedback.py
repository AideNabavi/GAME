import pygame

import pygame
import webbrowser


# =========================================================
# CONTACT FORM DATA
# =========================================================

name_text = ""
email_text = ""
message_text = ""

active_input = None


# =========================================================
# POSITIONS
# =========================================================

# محل شروع شبکه‌های اجتماعی (سمت چپ)
SOCIAL_X = 150
SOCIAL_Y = 180

# محل فرم (سمت راست)
FORM_X = 850
FORM_Y = 180


# =========================================================
# SIZES
# =========================================================

SOCIAL_SIZE = 80
SOCIAL_GAP = 25

INPUT_WIDTH = 450
INPUT_HEIGHT = 55

MESSAGE_HEIGHT = 160

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 60


message_rect = pygame.Rect(
    0, 0,
    INPUT_WIDTH,
    MESSAGE_HEIGHT
)

send_rect = pygame.Rect(
    0, 0,
    BUTTON_WIDTH,
    BUTTON_HEIGHT
)


# =========================================================
# FEEDBACK STATE
# =========================================================

message_scroll_y = 0
message_scroll_speed = 30

# امتیاز انتخاب شده
# 0 = هنوز انتخاب نشده
feedback_rating = 0


# =========================================================
# FEEDBACK STAR IMAGES
# =========================================================

feedback_star_images = []

for i in range(1, 6):

    image = pygame.image.load(
        f"./asset/image/feedback/{i}.png"
    ).convert_alpha()

    image = pygame.transform.smoothscale(
        image,
        (100, 100)
    )

    feedback_star_images.append(
        image
    )


# =========================================================
# DRAW FEEDBACK FORM
# =========================================================

def draw_contact_form(
    screen,
    font,
    current_x=FORM_X,
    current_y=FORM_Y
):

    global message_rect
    global send_rect
    global message_scroll_y
    global active_input

    # =====================================================
    # COLORS
    # =====================================================

    BOX_COLOR = (255, 255, 255)
    TEXT_COLOR = (40, 40, 40)
    PLACEHOLDER_COLOR = (190, 190, 190)
    ACTIVE_BORDER_COLOR = (220, 150, 60)

    BUTTON_COLOR = (100, 70, 40)
    BUTTON_TEXT_COLOR = (255, 255, 255)

    padding = 15

    # =====================================================
    # STAR SETTINGS
    # =====================================================

    star_size = 100
    star_gap = 25

    total_star_width = (
        star_size * 5 +
        star_gap * 4
    )

    stars_start_x = (
        current_x +
        (message_rect.width - total_star_width) // 2
    )

    stars_y = current_y

    # =====================================================
    # DRAW 5 STARS
    # =====================================================

    feedback_star_rects = []

    for i in range(5):

        star_x = (
            stars_start_x +
            i * (star_size + star_gap)
        )

        star_rect = pygame.Rect(
            star_x,
            stars_y,
            star_size,
            star_size
        )

        feedback_star_rects.append(
            star_rect
        )

        # -------------------------------------------------
        # Star image
        # -------------------------------------------------

        star_image = feedback_star_images[i]

        # -------------------------------------------------
        # اگر انتخاب شده باشد، کمی بزرگ‌تر
        # -------------------------------------------------

        if feedback_rating == i + 1:

            selected_size = 110

            selected_image = pygame.transform.smoothscale(
                star_image,
                (
                    selected_size,
                    selected_size
                )
            )

            selected_rect = selected_image.get_rect(
                center=star_rect.center
            )

            screen.blit(
                selected_image,
                selected_rect
            )

        else:

            screen.blit(
                star_image,
                star_rect
            )

    # =====================================================
    # MESSAGE BOX
    # =====================================================

    message_rect.topleft = (
        current_x,
        current_y + 125
    )

    pygame.draw.rect(
        screen,
        BOX_COLOR,
        message_rect,
        border_radius=10
    )

    # -----------------------------------------------------
    # Active border
    # -----------------------------------------------------

    if active_input == "message":

        pygame.draw.rect(
            screen,
            ACTIVE_BORDER_COLOR,
            message_rect,
            3,
            border_radius=10
        )

    # =====================================================
    # MESSAGE WORD WRAP
    # =====================================================

    if message_text:

        lines = []

        max_width = (
            message_rect.width -
            padding * 2
        )

        paragraphs = message_text.split("\n")

        for paragraph in paragraphs:

            # ---------------------------------------------
            # Empty line
            # ---------------------------------------------

            if paragraph == "":

                lines.append("")

                continue

            words = paragraph.split(" ")

            current_line = ""

            for word in words:

                # -----------------------------------------
                # Test line
                # -----------------------------------------

                if current_line:

                    test_line = (
                        current_line +
                        " " +
                        word
                    )

                else:

                    test_line = word

                # -----------------------------------------
                # Word fits
                # -----------------------------------------

                if font.size(test_line)[0] <= max_width:

                    current_line = test_line

                # -----------------------------------------
                # Word does not fit
                # -----------------------------------------

                else:

                    if current_line:

                        lines.append(
                            current_line
                        )

                    # -------------------------------------
                    # Very long word
                    # -------------------------------------

                    if font.size(word)[0] > max_width:

                        remaining = word

                        while remaining:

                            fitted = ""

                            for char in remaining:

                                test_char = (
                                    fitted +
                                    char
                                )

                                if font.size(
                                    test_char
                                )[0] <= max_width:

                                    fitted = test_char

                                else:

                                    break

                            if fitted:

                                lines.append(
                                    fitted
                                )

                                remaining = remaining[
                                    len(fitted):
                                ]

                            else:

                                lines.append(
                                    remaining[0]
                                )

                                remaining = remaining[1:]

                        current_line = ""

                    else:

                        current_line = word

            # ---------------------------------------------
            # Last line
            # ---------------------------------------------

            if current_line:

                lines.append(
                    current_line
                )

    else:

        lines = [
            "Tell us what you think..."
        ]

    # =====================================================
    # MESSAGE SCROLL LIMIT
    # =====================================================

    line_spacing = 8

    line_height = (
        font.get_height() +
        line_spacing
    )

    visible_height = (
        message_rect.height -
        padding * 2
    )

    content_height = (
        len(lines) *
        line_height
    )

    max_scroll = max(
        0,
        content_height -
        visible_height
    )

    # Keep scroll inside range

    message_scroll_y = max(
        0,
        min(
            message_scroll_y,
            max_scroll
        )
    )

    # =====================================================
    # MESSAGE CLIPPING AREA
    # =====================================================

    clip_rect = pygame.Rect(
        message_rect.x + padding,
        message_rect.y + padding,
        message_rect.width - padding * 2,
        message_rect.height - padding * 2
    )

    old_clip = screen.get_clip()

    screen.set_clip(
        clip_rect
    )

    # =====================================================
    # DRAW MESSAGE
    # =====================================================

    text_y = (
        message_rect.y +
        padding -
        message_scroll_y
    )

    for line in lines:

        # Only draw visible lines

        if (
            text_y + line_height >= clip_rect.top
            and
            text_y <= clip_rect.bottom
        ):

            if message_text:

                text_color = TEXT_COLOR

            else:

                text_color = PLACEHOLDER_COLOR

            text_surface = font.render(
                line,
                True,
                text_color
            )

            screen.blit(
                text_surface,
                (
                    message_rect.x + padding,
                    text_y
                )
            )

        text_y += line_height

    # Restore clipping

    screen.set_clip(
        old_clip
    )

    # =====================================================
    # SEND BUTTON
    # =====================================================

    send_rect.topleft = (
        current_x,
        current_y + 350
    )

    pygame.draw.rect(
        screen,
        BUTTON_COLOR,
        send_rect,
        border_radius=12
    )

    send_surface = font.render(
        "SEND FEEDBACK",
        True,
        BUTTON_TEXT_COLOR
    )

    screen.blit(
        send_surface,
        send_surface.get_rect(
            center=send_rect.center
        )
    )

    # =====================================================
    # RETURN STAR RECTS
    # =====================================================

    return feedback_star_rects


# =========================================================
# HANDLE FEEDBACK EVENT
# =========================================================

def handle_contact_event(event):

    global message_text
    global active_input
    global message_scroll_y
    global feedback_rating

    # =====================================================
    # MOUSE
    # =====================================================

    if event.type == pygame.MOUSEBUTTONDOWN:

        # -------------------------------------------------
        # LEFT CLICK
        # -------------------------------------------------

        if event.button == 1:

            mouse_pos = event.pos

            # =============================================
            # STAR CLICK
            # =============================================

            star_size = 100
            star_gap = 25

            total_star_width = (
                star_size * 5 +
                star_gap * 4
            )

            stars_start_x = (
                FORM_X +
                (message_rect.width - total_star_width) // 2
            )

            stars_y = FORM_Y

            for i in range(5):

                star_rect = pygame.Rect(
                    stars_start_x +
                    i * (star_size + star_gap),

                    stars_y,

                    star_size,
                    star_size
                )

                if star_rect.collidepoint(
                    mouse_pos
                ):

                    feedback_rating = i + 1

                    active_input = None

                    return

            # =============================================
            # MESSAGE
            # =============================================

            if message_rect.collidepoint(
                mouse_pos
            ):

                active_input = "message"

                return

            # =============================================
            # SEND
            # =============================================

            if send_rect.collidepoint(
                mouse_pos
            ):

                send_contact_message()

                return

            # =============================================
            # CLICK OUTSIDE
            # =============================================

            active_input = None

    # =====================================================
    # MESSAGE SCROLL
    # =====================================================

    elif event.type == pygame.MOUSEWHEEL:

        mouse_pos = pygame.mouse.get_pos()

        if message_rect.collidepoint(
            mouse_pos
        ):

            message_scroll_y -= (
                event.y *
                message_scroll_speed
            )

            message_scroll_y = max(
                0,
                message_scroll_y
            )

            return

    # =====================================================
    # KEYBOARD
    # =====================================================

    elif event.type == pygame.KEYDOWN:

        if active_input != "message":

            return

        # =================================================
        # ENTER
        # =================================================

        if event.key == pygame.K_RETURN:

            # Maximum 500 words

            if len(
                message_text.split()
            ) < 500:

                message_text += "\n"

            return

        # =================================================
        # BACKSPACE
        # =================================================

        if event.key == pygame.K_BACKSPACE:

            message_text = (
                message_text[:-1]
            )

            return

        # =================================================
        # TEXT
        # =================================================

        char = event.unicode

        if not char:

            return

        # =================================================
        # MAX 500 WORDS
        # =================================================

        current_words = len(
            message_text.split()
        )

        if current_words < 500:

            message_text += char


# =========================================================
# SEND FEEDBACK
# =========================================================

def send_contact_message():

    global message_text
    global feedback_rating
    global message_scroll_y
    global active_input

    # =====================================================
    # CHECK RATING
    # =====================================================

    if feedback_rating == 0:

        print(
            "Please select a rating."
        )

        return False

    # =====================================================
    # CHECK MESSAGE
    # =====================================================

    if not message_text.strip():

        print(
            "Message is empty."
        )

        return False

    # =====================================================
    # DATA TO SEND
    # =====================================================

    data = {

        "rating": feedback_rating,

        "message": message_text.strip()
    }

    # =====================================================
    # DEBUG
    # =====================================================

    print(
        "FEEDBACK:"
    )

    print(
        data
    )

    # =====================================================
    # API
    # =====================================================

    # بعداً API خودت را اینجا قرار می‌دهیم:
    #
    # response = requests.post(
    #
    #     "https://YOUR-DOMAIN.com/api/feedback",
    #
    #     json=data,
    #
    #     timeout=10
    # )

    # =====================================================
    # CLEAR FORM
    # =====================================================

    message_text = ""

    feedback_rating = 0

    message_scroll_y = 0

    active_input = None

    print(
        "Feedback ready to send."
    )

    return True
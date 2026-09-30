

# =========================================================
# CONTACT FORM
# =========================================================

import pygame
import webbrowser


# =========================================================
# CONTACT FORM DATA
# =========================================================

name_text = ""
email_text = ""
message_text = ""

active_input = None

send_image = pygame.transform.smoothscale(pygame.image.load(
    "./asset/image/send.png"
).convert_alpha(),(80,80))
    
    
# =========================================================
# POSITIONS
# =========================================================

# محل شروع شبکه‌های اجتماعی (سمت چپ)
SOCIAL_X = 400
SOCIAL_Y = 700

# محل فرم (سمت راست)
FORM_X = 850
FORM_Y = 180


# =========================================================
# SIZES
# =========================================================

SOCIAL_SIZE = 150
SOCIAL_GAP = 70

INPUT_WIDTH = 500
INPUT_HEIGHT = 100

MESSAGE_HEIGHT = 500

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 60


# =========================================================
# RECT LISTS
# =========================================================

social_rects = []

name_rect = pygame.Rect(
    0, 0,
    INPUT_WIDTH,
    INPUT_HEIGHT
)

email_rect = pygame.Rect(
    0, 0,
    INPUT_WIDTH,
    INPUT_HEIGHT
)

message_rect = pygame.Rect(
    0, 0,
    600,
    MESSAGE_HEIGHT
)

send_rect = pygame.Rect(
    0, 0,
    80,
    80
)

# =========================================================
# SOCIAL IMAGES
# =========================================================
xxxx=(250,250)
images = [
    pygame.transform.smoothscale(
        pygame.image.load(
            "./asset/image/support/github.png"
        ).convert_alpha(),
        xxxx
    ),

    pygame.transform.smoothscale(
        pygame.image.load(
            "./asset/image/support/instagram.png"
        ).convert_alpha(),
        xxxx
    ),

    pygame.transform.smoothscale(
        pygame.image.load(
            "./asset/image/support/telegram.png"
        ).convert_alpha(),
        xxxx
    ),

    pygame.transform.smoothscale(
        pygame.image.load(
            "./asset/image/support/email.png"
        ).convert_alpha(),
        xxxx
    ),

    pygame.transform.smoothscale(
        pygame.image.load(
            "./asset/image/support/youtube.png"
        ).convert_alpha(),
        xxxx
    )
]


# =========================================================
# SOCIAL URLS
# =========================================================

urls = [
    "https://github.com/AideNabavi",
    "https://instagram.com/aidenabavi",
    "https://t.me/AideNabavi",
    "mailto:aidenabavi@email.com",
    "https://youtube.com/AideNabavi"
]


# =========================================================
# RECT LIST
# =========================================================

social_rects = []


# =========================================================
# DRAW SOCIAL LINKS
# =========================================================
# =========================================================
# DRAW SOCIAL LINKS
# =========================================================

def draw_social_links(
    screen,
    images,
    urls,
    current_x=SOCIAL_X,
    current_y=SOCIAL_Y
):

    global social_rects

    social_rects.clear()

    mouse_pos = pygame.mouse.get_pos()

    x = current_x
    
    for image in images:

        # تغییر اندازه تصویر
        image = pygame.transform.smoothscale(
            image,
            (SOCIAL_SIZE, SOCIAL_SIZE)
        )

        rect = image.get_rect(
            topleft=(
                x,
                current_y
            )
        )

        social_rects.append(rect)

        # رسم تصویر
        screen.blit(
            image,
            rect
        )

        # Hover
        if rect.collidepoint(mouse_pos):

            pygame.draw.rect(
                screen,
                (255, 255, 255),
                rect,
                3,
                border_radius=10
            )

        # رفتن به تصویر بعدی
        x += SOCIAL_SIZE + SOCIAL_GAP
# =========================================================
# OPEN SOCIAL LINK
# =========================================================

def open_social_link(url):

    # باز کردن URL در مرورگر پیش‌فرض سیستم
    webbrowser.open(url)

    # Minimize کردن پنجره Pygame
    pygame.display.iconify()


# =========================================================
# HANDLE SOCIAL CLICK
# =========================================================

def handle_social_click(event, urls):

    if event.type != pygame.MOUSEBUTTONDOWN:
        return

    if event.button != 1:
        return

    # بررسی تمام Rect ها
    for i, rect in enumerate(social_rects):

        if rect.collidepoint(event.pos):

            # باز کردن لینک مربوط به همان تصویر
            open_social_link(urls[i])

            # جلوگیری از بررسی بقیه
            break
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        








message_scroll_y = 0
message_scroll_speed = 30


# =========================================================
# DRAW CONTACT FORM
# =========================================================

def draw_contact_form(
    screen,
    font,
    current_x=FORM_X,
    current_y=FORM_Y
):

    global name_rect
    global email_rect
    global message_rect
    global send_rect
    global message_scroll_y

    # =====================================================
    # COLORS
    # =====================================================

    BOX_COLOR = (255, 255, 255)
    TEXT_COLOR = (40, 40, 40)
    PLACEHOLDER_COLOR = (190, 190, 190)
    ACTIVE_BORDER_COLOR = (220, 150, 60)

    padding = 15

    # =====================================================
    # NAME
    # =====================================================

    name_rect.topleft = (
        423,
        375
    )

    pygame.draw.rect(
        screen,
        BOX_COLOR,
        name_rect,
        border_radius=10
    )

    if active_input == "name":

        pygame.draw.rect(
            screen,
            ACTIVE_BORDER_COLOR,
            name_rect,
            3,
            border_radius=10
        )

    if name_text:

        name_surface = font.render(
            name_text,
            True,
            TEXT_COLOR
        )

        clip_rect = pygame.Rect(
            name_rect.x + padding,
            name_rect.y,
            name_rect.width - padding * 2,
            name_rect.height
        )

        old_clip = screen.get_clip()

        screen.set_clip(clip_rect)

        screen.blit(
            name_surface,
            (
                name_rect.x + padding,
                name_rect.y + (
                    name_rect.height -
                    name_surface.get_height()
                ) // 2
            )
        )

        screen.set_clip(old_clip)

    else:

        name_surface = font.render(
            "Your Name",
            True,
            PLACEHOLDER_COLOR
        )

        screen.blit(
            name_surface,
            (
                name_rect.x + padding,
                name_rect.y + (
                    name_rect.height -
                    name_surface.get_height()
                ) // 2
            )
        )

    # =====================================================
    # EMAIL
    # =====================================================

    email_rect.topleft = (
        418,
        520
    )

    pygame.draw.rect(
        screen,
        BOX_COLOR,
        email_rect,
        border_radius=10
    )

    if active_input == "email":

        pygame.draw.rect(
            screen,
            ACTIVE_BORDER_COLOR,
            email_rect,
            3,
            border_radius=10
        )

    if email_text:

        email_surface = font.render(
            email_text,
            True,
            TEXT_COLOR
        )

        clip_rect = pygame.Rect(
            email_rect.x + padding,
            email_rect.y,
            email_rect.width - padding * 2,
            email_rect.height
        )

        old_clip = screen.get_clip()

        screen.set_clip(clip_rect)

        screen.blit(
            email_surface,
            (
                email_rect.x + padding,
                email_rect.y + (
                    email_rect.height -
                    email_surface.get_height()
                ) // 2
            )
        )

        screen.set_clip(old_clip)

    else:

        email_surface = font.render(
            "Your Email",
            True,
            PLACEHOLDER_COLOR
        )

        screen.blit(
            email_surface,
            (
                email_rect.x + padding,
                email_rect.y + (
                    email_rect.height -
                    email_surface.get_height()
                ) // 2
            )
        )

    # =====================================================
    # MESSAGE BOX
    # =====================================================

    message_rect.topleft = (
        1050,
        375
    )

    pygame.draw.rect(
        screen,
        BOX_COLOR,
        message_rect,
        border_radius=10
    )

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

        # عرض واقعی قابل استفاده برای متن
        max_width = (
            message_rect.width -
            padding * 2
        )

        # متن را اول بر اساس Enter جدا می‌کنیم
        paragraphs = message_text.split("\n")

        for paragraph in paragraphs:

            # اگر کاربر فقط Enter زده باشد
            if paragraph == "":
                lines.append("")
                continue

            words = paragraph.split(" ")

            current_line = ""

            for word in words:

                # -----------------------------------------
                # تست اضافه شدن کلمه به خط فعلی
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
                # اگر داخل عرض باکس جا شد
                # -----------------------------------------

                if font.size(test_line)[0] <= max_width:

                    current_line = test_line

                # -----------------------------------------
                # اگر جا نشد -> خط بعد
                # -----------------------------------------

                else:

                    if current_line:

                        lines.append(
                            current_line
                        )

                    # اگر خود کلمه از عرض باکس بزرگ‌تر بود
                    # آن را هم به صورت تکه‌ای تقسیم می‌کنیم

                    if font.size(word)[0] > max_width:

                        remaining = word

                        while remaining:

                            fitted = ""

                            for char in remaining:

                                test_char = (
                                    fitted +
                                    char
                                )

                                if font.size(test_char)[0] <= max_width:

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

                                # جلوگیری از حلقه بی‌نهایت
                                lines.append(
                                    remaining[0]
                                )

                                remaining = remaining[1:]

                        current_line = ""

                    else:

                        current_line = word

            # -----------------------------------------
            # آخرین خط پاراگراف
            # -----------------------------------------

            if current_line:

                lines.append(
                    current_line
                )

    else:

        lines = [
            "Write your message..."
        ]


    # =====================================================
    # MESSAGE SCROLL LIMIT
    # =====================================================

    # فاصله بین خطوط
    line_spacing = 8

    line_height = (
        font.get_height() +
        line_spacing
    )

    # ارتفاع واقعی قابل استفاده داخل باکس
    visible_height = (
        message_rect.height -
        padding * 2
    )

    # ارتفاع کل محتوا
    content_height = (
        len(lines) *
        line_height
    )

    # بیشترین مقدار اسکرول
    max_scroll = max(
        0,
        content_height -
        visible_height
    )

    # جلوگیری از خارج شدن اسکرول
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
    # DRAW MESSAGE TEXT
    # =====================================================

    text_y = (
        message_rect.y +
        padding -
        message_scroll_y
    )

    for line in lines:

        # -----------------------------------------
        # اگر خط کاملاً خارج از صفحه است
        # آن را اصلاً رسم نکن
        # -----------------------------------------

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


    # برگرداندن Clip قبلی
    screen.set_clip(
        old_clip
    )

    # ===============================
    # SEND BUTTON
    # =====================================================

    send_rect.topleft = (
        current_x - 200,
        current_y + 300
    )

    screen.blit(
        send_image,
        send_rect
    )


    # =====================================================
    # CONTACT DESCRIPTION
    # =====================================================

    contact_text = (
        "Have a question or feedback? "
        "Feel free to reach out to us. "
        "Send us a message or connect with us below."
    )

    contact_x = 683
    contact_y = 600
    contact_width = 450

    contact_lines = []

    words = contact_text.split(" ")

    current_line = ""

    for word in words:

        if current_line:

            test_line = (
                current_line +
                " " +
                word
            )

        else:

            test_line = word

        if font.size(test_line)[0] <= contact_width:

            current_line = test_line

        else:

            if current_line:

                contact_lines.append(
                    current_line
                )

            current_line = word


    if current_line:

        contact_lines.append(
            current_line
        )


    # =====================================================
    # DRAW CONTACT TEXT
    # =====================================================

    line_spacing = 10

    text_y = contact_y

    for line in contact_lines:

        text_surface = font.render(
            line,
            True,
            (40, 40, 40)
        )

        rect = text_surface.get_rect(
            centerx=contact_x,
            top=text_y
        )

        screen.blit(
            text_surface,
            rect
        )

        text_y += (
            font.get_height() +
            line_spacing
        )
        
    
    
    
def handle_contact_event(event):

    global name_text
    global email_text
    global message_text
    global active_input
    global message_scroll_y

    # =====================================================
    # MOUSE
    # =====================================================

    if event.type == pygame.MOUSEBUTTONDOWN:

        if event.button == 1:

            if name_rect.collidepoint(event.pos):

                active_input = "name"

            elif email_rect.collidepoint(event.pos):

                active_input = "email"

            elif message_rect.collidepoint(event.pos):

                active_input = "message"

            elif send_rect.collidepoint(event.pos):

                send_contact_message()

            else:

                active_input = None
    # =====================================================
    # MESSAGE SCROLL
    # =====================================================

    elif event.type == pygame.MOUSEWHEEL:

        mouse_pos = pygame.mouse.get_pos()

        if message_rect.collidepoint(mouse_pos):

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

        if active_input is None:
            return

        # =====================================================
        # ENTER
        # =====================================================

        if event.key == pygame.K_RETURN:

            if active_input == "message":

                # فقط اگر هنوز زیر محدودیت 500 کلمه هستیم
                if len(message_text.split()) < 500:

                    message_text += "\n"

            else:

                active_input = None

            return

        # =====================================================
        # BACKSPACE
        # =====================================================

        if event.key == pygame.K_BACKSPACE:

            if active_input == "name":

                name_text = name_text[:-1]

            elif active_input == "email":

                email_text = email_text[:-1]

            elif active_input == "message":

                message_text = message_text[:-1]

            return

        # =====================================================
        # TEXT
        # =====================================================

        char = event.unicode

        if not char:
            return

        # =====================================================
        # NAME
        # MAX 10 CHARACTERS
        # =====================================================

        if active_input == "name":

            if len(name_text) < 10:

                # اجازه حروف، اعداد و فاصله
                if char.isalnum() or char == " ":

                    name_text += char

        # =====================================================
        # EMAIL
        # MAX 254 CHARACTERS
        # =====================================================

        elif active_input == "email":

            if len(email_text) < 254:

                # کاراکترهای مجاز معمول ایمیل
                allowed = (
                    "abcdefghijklmnopqrstuvwxyz"
                    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                    "0123456789"
                    "@._+-"
                )

                if char in allowed:

                    # فاصله ممنوع
                    if char != " ":

                        email_text += char

        # =====================================================
        # MESSAGE
        # MAX 500 WORDS
        # =====================================================

        elif active_input == "message":

            # تعداد کلمات فعلی
            current_words = len(
                message_text.split()
            )

            # اگر به 500 کلمه نرسیده
            if current_words < 500:

                message_text += char

# =========================================================
# SEND MESSAGE
# =========================================================

def send_contact_message():

    global name_text
    global email_text
    global message_text

    # جلوگیری از ارسال فرم خالی

    if not name_text.strip():

        print("Name is empty")
        return

    if not email_text.strip():

        print("Email is empty")
        return

    if not message_text.strip():

        print("Message is empty")
        return

    # -----------------------------------------------------
    # فعلاً اطلاعات را آماده می‌کنیم
    # -----------------------------------------------------

    data = {
        "name": name_text,
        "email": email_text,
        "message": message_text
    }

    print("CONTACT MESSAGE:")
    print(data)

    # -----------------------------------------------------
    # اینجا بعداً API خودت را صدا می‌زنیم
    # -----------------------------------------------------

    # مثال:
    #
    # requests.post(
    #     "https://YOUR-DOMAIN.com/api/contact",
    #     json=data,
    #     timeout=10
    # )

    print("Message ready to send.")

    # پاک کردن فرم بعد از ارسال موفق
    name_text = ""
    email_text = ""
    message_text = ""

    return True

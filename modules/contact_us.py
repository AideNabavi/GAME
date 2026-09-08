import pygame
import webbrowser


# =========================================================
# SOCIAL IMAGES
# =========================================================

images = [
    pygame.transform.smoothscale(
        pygame.image.load(
            "./asset/image/support/github.png"
        ).convert_alpha(),
        (100, 100)
    ),

    pygame.transform.smoothscale(
        pygame.image.load(
            "./asset/image/support/instagram.png"
        ).convert_alpha(),
        (100, 100)
    ),

    pygame.transform.smoothscale(
        pygame.image.load(
            "./asset/image/support/telegram.png"
        ).convert_alpha(),
        (100, 100)
    ),

    pygame.transform.smoothscale(
        pygame.image.load(
            "./asset/image/support/x.png"
        ).convert_alpha(),
        (100, 100)
    ),

    pygame.transform.smoothscale(
        pygame.image.load(
            "./asset/image/support/email.png"
        ).convert_alpha(),
        (100, 100)
    ),

    pygame.transform.smoothscale(
        pygame.image.load(
            "./asset/image/support/youtube.png"
        ).convert_alpha(),
        (100, 100)
    )
]


# =========================================================
# SOCIAL URLS
# =========================================================

urls = [
    "https://github.com/AideNabavi",
    "https://instagram.com/aidenabavi",
    "https://t.me/AideNabavi",
    "https://x.com/aidenabavi",
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

def draw_social_links(
    screen,
    images,
    urls,
    current_x
):

    global social_rects

    # جلوگیری از اضافه شدن Rect جدید در هر فریم
    social_rects.clear()

    # فاصله بین عکس‌ها
    gap = 30

    # -----------------------------------------------------
    # محاسبه عرض کل عکس‌ها
    # -----------------------------------------------------

    total_width = (
        sum(image.get_width() for image in images)
        + gap * (len(images) - 1)
    )

    # -----------------------------------------------------
    # شروع ردیف نسبت به current_x
    # -----------------------------------------------------

    start_x = (
        current_x - total_width / 2
    )

    # -----------------------------------------------------
    # مرکز عمودی صفحه
    # -----------------------------------------------------

    y = (
        screen.get_height() - images[0].get_height()
    ) // 2

    x = start_x

    # -----------------------------------------------------
    # رسم تمام تصاویر
    # -----------------------------------------------------

    for image in images:

        rect = image.get_rect(
            topleft=(
                int(x),
                y
            )
        )

        # ذخیره Rect
        social_rects.append(rect)

        # رسم تصویر
        screen.blit(
            image,
            rect
        )

        # -------------------------------------------------
        # Hover
        # -------------------------------------------------

        if rect.collidepoint(
            pygame.mouse.get_pos()
        ):

            pygame.draw.rect(
                screen,
                (255, 255, 255),
                rect,
                3,
                border_radius=10
            )

        # -------------------------------------------------
        # رفتن به تصویر بعدی
        # -------------------------------------------------

        x += image.get_width() + gap

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
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        














# =========================================================
# CONTACT FORM
# =========================================================

name_text = ""
email_text = ""
message_text = ""

active_input = None


# اندازه و محل باکس‌ها
name_rect = pygame.Rect(0, 0, 400, 55)
email_rect = pygame.Rect(0, 0, 400, 55)
message_rect = pygame.Rect(0, 0, 400, 160)

send_rect = pygame.Rect(0, 0, 180, 60)


def draw_contact_form(screen, font):

    global name_rect
    global email_rect
    global message_rect
    global send_rect

    # -----------------------------------------------------
    # مرکز صفحه
    # -----------------------------------------------------

    center_x = screen.get_width() // 2

    start_y = 180

    # -----------------------------------------------------
    # Name
    # -----------------------------------------------------

    name_rect.center = (center_x, start_y)

    pygame.draw.rect(
        screen,
        (255, 255, 255),
        name_rect,
        border_radius=10
    )

    name_surface = font.render(
        name_text if name_text else "Your Name",
        True,
        (40, 40, 40)
    )

    screen.blit(
        name_surface,
        (
            name_rect.x + 15,
            name_rect.y + 15
        )
    )

    # -----------------------------------------------------
    # Email
    # -----------------------------------------------------

    email_rect.center = (
        center_x,
        start_y + 80
    )

    pygame.draw.rect(
        screen,
        (255, 255, 255),
        email_rect,
        border_radius=10
    )

    email_surface = font.render(
        email_text if email_text else "Your Email",
        True,
        (40, 40, 40)
    )

    screen.blit(
        email_surface,
        (
            email_rect.x + 15,
            email_rect.y + 15
        )
    )

    # -----------------------------------------------------
    # Message
    # -----------------------------------------------------

    message_rect.center = (
        center_x,
        start_y + 210
    )

    pygame.draw.rect(
        screen,
        (255, 255, 255),
        message_rect,
        border_radius=10
    )

    # Message چند خطی
    lines = message_text.split("\n")

    if not lines:
        lines = [""]

    if message_text == "":
        lines = ["Write your message..."]

    text_y = message_rect.y + 15

    for line in lines:

        text_surface = font.render(
            line,
            True,
            (40, 40, 40)
        )

        screen.blit(
            text_surface,
            (
                message_rect.x + 15,
                text_y
            )
        )

        text_y += font.get_height() + 5

        # جلوگیری از خروج متن از باکس
        if text_y > message_rect.bottom - 10:
            break

    # -----------------------------------------------------
    # Send Button
    # -----------------------------------------------------

    send_rect.center = (
        center_x,
        message_rect.bottom + 70
    )

    pygame.draw.rect(
        screen,
        (100, 70, 40),
        send_rect,
        border_radius=12
    )

    send_surface = font.render(
        "SEND MESSAGE",
        True,
        (255, 255, 255)
    )

    screen.blit(
        send_surface,
        send_surface.get_rect(
            center=send_rect.center
        )
    )


# =========================================================
# HANDLE CONTACT INPUT
# =========================================================

def handle_contact_event(event):

    global name_text
    global email_text
    global message_text
    global active_input

    # -----------------------------------------------------
    # Mouse
    # -----------------------------------------------------

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

    # -----------------------------------------------------
    # Keyboard
    # -----------------------------------------------------

    elif event.type == pygame.KEYDOWN:

        # اگر هیچ باکسی فعال نیست
        if active_input is None:
            return

        # Enter
        if event.key == pygame.K_RETURN:

            if active_input == "message":
                message_text += "\n"

            else:
                active_input = None

            return

        # Backspace
        if event.key == pygame.K_BACKSPACE:

            if active_input == "name":

                name_text = name_text[:-1]

            elif active_input == "email":

                email_text = email_text[:-1]

            elif active_input == "message":

                message_text = message_text[:-1]

            return

        # متن تایپ شده
        char = event.unicode

        if not char:
            return

        if active_input == "name":

            name_text += char

        elif active_input == "email":

            email_text += char

        elif active_input == "message":

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

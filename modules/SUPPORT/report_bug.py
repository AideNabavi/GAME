# =========================================================
# REPORT A BUG
# =========================================================

import pygame


# =========================================================
# REPORT BUG DATA
# =========================================================

bug_game = ""
bug_type = ""

subject_text = ""
description_text = ""

active_input = None

description_scroll_y = 0
description_scroll_speed = 30


# =========================================================
# POSITIONS
# =========================================================

FORM_X = 850
FORM_Y = 180


# =========================================================
# SIZES
# =========================================================

INPUT_WIDTH = 500

SELECT_HEIGHT = 100
SUBJECT_HEIGHT = 100
DESCRIPTION_HEIGHT = 400

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 60


# =========================================================
# GAME DROPDOWN SETTINGS
# =========================================================

GAME_ITEM_HEIGHT = 45

# حداقل 20 آیتم نمایش داده شود
GAME_VISIBLE_ITEMS = 10

GAME_DROPDOWN_HEIGHT = (
    GAME_ITEM_HEIGHT *
    GAME_VISIBLE_ITEMS
)

game_dropdown_scroll = 0
game_dropdown_scroll_speed = 45


# =========================================================
# BUG TYPE DROPDOWN SETTINGS
# =========================================================

BUG_TYPE_ITEM_HEIGHT = 45

BUG_TYPE_VISIBLE_ITEMS = 9

bug_type_dropdown_scroll = 0
bug_type_dropdown_scroll_speed = 45


# =========================================================
# RECT
# =========================================================

game_select_rect = pygame.Rect(
    0,
    0,
    INPUT_WIDTH,
    SELECT_HEIGHT
)

bug_type_rect = pygame.Rect(
    0,
    0,
    INPUT_WIDTH,
    SELECT_HEIGHT
)

subject_rect = pygame.Rect(
    0,
    0,
    INPUT_WIDTH,
    SUBJECT_HEIGHT
)

description_rect = pygame.Rect(
    0,
    0,
    637,
    DESCRIPTION_HEIGHT
)

report_bug_rect = pygame.Rect(
    0,
    0,
    BUTTON_WIDTH,
    BUTTON_HEIGHT
)


# =========================================================
# GAME LIST
# =========================================================

from modules.game_list import all_games as GAME_LIST

# تبدیل به list مستقل
GAME_LIST = list(GAME_LIST)

# مطمئن می‌شویم placeholder وجود دارد
if not GAME_LIST or GAME_LIST[0] != "Select Game":

    GAME_LIST.insert(
        0,
        "Select Game"
    )


# =========================================================
# BUG TYPE LIST
# =========================================================

BUG_TYPE_LIST = [

    "Bug Type",

    "Gameplay Bug",

    "UI / Visual Bug",

    "Sound Bug",

    "Performance",

    "Crash / Error",

    "Text / Translation",

    "Controls",

    "Other"
]


# =========================================================
# DROPDOWN STATE
# =========================================================

game_dropdown_open = False
bug_type_dropdown_open = False


# =========================================================
# DROPDOWN RECT LISTS
# =========================================================

game_dropdown_rects = []

bug_type_dropdown_rects = []


# =========================================================
# DRAW DROPDOWN
# =========================================================

def draw_bug_dropdown(
    screen,
    font,
    rect,
    selected_text,
    items,
    is_open,
    dropdown_rects,
    mouse_pos,
    scroll_offset=0,
    visible_items=20,
    item_height=45
):

    # =====================================================
    # COLORS
    # =====================================================

    BOX_COLOR = (
        255,
        255,
        255
    )

    TEXT_COLOR = (
        40,
        40,
        40
    )

    DROPDOWN_COLOR = (
        245,
        245,
        245
    )

    HOVER_COLOR = (
        225,
        225,
        225
    )

    BORDER_COLOR = (
        220,
        150,
        60
    )

    # =====================================================
    # MAIN BOX
    # =====================================================

    pygame.draw.rect(
        screen,
        BOX_COLOR,
        rect,
        border_radius=10
    )

    # =====================================================
    # MAIN TEXT
    # =====================================================

    if selected_text:

        surface = font.render(
            selected_text,
            True,
            TEXT_COLOR
        )

        screen.blit(
            surface,
            (
                rect.x + 15,
                rect.y + (
                    rect.height -
                    surface.get_height()
                ) // 2
            )
        )

    # =====================================================
    # ARROW
    # =====================================================

    arrow_x = rect.right - 22
    arrow_y = rect.centery

    if is_open:

        pygame.draw.polygon(
            screen,
            TEXT_COLOR,
            [
                (
                    arrow_x - 7,
                    arrow_y + 4
                ),
                (
                    arrow_x + 7,
                    arrow_y + 4
                ),
                (
                    arrow_x,
                    arrow_y - 5
                )
            ]
        )

    else:

        pygame.draw.polygon(
            screen,
            TEXT_COLOR,
            [
                (
                    arrow_x - 7,
                    arrow_y - 4
                ),
                (
                    arrow_x + 7,
                    arrow_y - 4
                ),
                (
                    arrow_x,
                    arrow_y + 5
                )
            ]
        )

    # =====================================================
    # MAIN BOX BORDER
    # =====================================================

    pygame.draw.rect(
        screen,
        BORDER_COLOR,
        rect,
        2,
        border_radius=10
    )

    # =====================================================
    # CLEAR OLD RECTS
    # =====================================================

    dropdown_rects.clear()

    # =====================================================
    # CLOSED
    # =====================================================

    if not is_open:

        return

    # =====================================================
    # DROPDOWN POSITION
    # =====================================================

    dropdown_x = rect.x

    dropdown_y = (
        rect.bottom +
        5
    )

    dropdown_width = rect.width

    dropdown_height = (
        visible_items *
        item_height
    )

    dropdown_area = pygame.Rect(
        dropdown_x,
        dropdown_y,
        dropdown_width,
        dropdown_height
    )

    # =====================================================
    # DROPDOWN BACKGROUND
    # =====================================================

    pygame.draw.rect(
        screen,
        DROPDOWN_COLOR,
        dropdown_area,
        border_radius=8
    )

    # =====================================================
    # CLIP
    # =====================================================

    old_clip = screen.get_clip()

    screen.set_clip(
        dropdown_area
    )

    # =====================================================
    # DRAW ITEMS
    # =====================================================

    start_y = (
        dropdown_y -
        scroll_offset
    )

    for i, item in enumerate(items):

        item_y = (
            start_y +
            i * item_height
        )

        item_rect = pygame.Rect(
            dropdown_x,
            item_y,
            dropdown_width,
            item_height
        )

        # =============================================
        # فقط آیتم‌های قابل مشاهده
        # =============================================

        if (
            item_rect.bottom >=
            dropdown_area.top
            and
            item_rect.top <=
            dropdown_area.bottom
        ):

            dropdown_rects.append(
                (
                    item_rect.copy(),
                    i
                )
            )

            # =========================================
            # HOVER
            # =========================================

            item_color = DROPDOWN_COLOR

            if item_rect.collidepoint(
                mouse_pos
            ):

                item_color = HOVER_COLOR

            pygame.draw.rect(
                screen,
                item_color,
                item_rect
            )

            # =========================================
            # ITEM TEXT
            # =========================================

            item_surface = font.render(
                str(item),
                True,
                TEXT_COLOR
            )

            screen.blit(
                item_surface,
                (
                    item_rect.x + 15,
                    item_rect.y + (
                        item_rect.height -
                        item_surface.get_height()
                    ) // 2
                )
            )

    # =====================================================
    # RESTORE CLIP
    # =====================================================

    screen.set_clip(
        old_clip
    )

    # =====================================================
    # DROPDOWN BORDER
    # =====================================================

    pygame.draw.rect(
        screen,
        BORDER_COLOR,
        dropdown_area,
        2,
        border_radius=8
    )


# =========================================================
# DRAW REPORT BUG
# =========================================================
from modules.SUPPORT.contact_us import send_image
def draw_report_bug(
    screen,
    font,
    current_x=FORM_X,
    current_y=FORM_Y
):

    global game_select_rect
    global bug_type_rect
    global subject_rect
    global description_rect
    global report_bug_rect

    global description_scroll_y

    # =====================================================
    # COLORS
    # =====================================================

    BOX_COLOR = (
        255,
        255,
        255
    )

    TEXT_COLOR = (
        40,
        40,
        40
    )

    PLACEHOLDER_COLOR = (
        180,
        180,
        180
    )

    ACTIVE_BORDER_COLOR = (
        220,
        150,
        60
    )

    padding = 15

    mouse_pos = pygame.mouse.get_pos()

    # =====================================================
    # GAME SELECT POSITION
    # =====================================================

    game_select_rect.topleft = (
        420,
        400
    )

    # =====================================================
    # BUG TYPE POSITION
    # =====================================================

    bug_type_rect.topleft = (
        420,
        550
    )

    # =====================================================
    # SUBJECT POSITION
    # =====================================================

    subject_rect.topleft = (
        420,
         550+ 150
    )

    # =====================================================
    # DESCRIPTION POSITION
    # =====================================================

    description_rect.topleft = (
        1000,
         620
    )

    # =====================================================
    # REPORT BUTTON POSITION
    # =====================================================

    report_bug_rect.topleft = (
        420,
        550+ 150 + 150
    )

    # =====================================================
    # GAME SELECT
    # ALWAYS DRAW
    # =====================================================

    draw_bug_dropdown(
        screen,
        font,
        game_select_rect,
        bug_game if bug_game else "Select Game",
        GAME_LIST,
        False,
        game_dropdown_rects,
        mouse_pos,
        game_dropdown_scroll,
        GAME_VISIBLE_ITEMS,
        GAME_ITEM_HEIGHT
    )

    # =====================================================
    # BUG TYPE
    # ALWAYS DRAW
    # =====================================================

    draw_bug_dropdown(
        screen,
        font,
        bug_type_rect,
        bug_type if bug_type else "Bug Type",
        BUG_TYPE_LIST,
        False,
        bug_type_dropdown_rects,
        mouse_pos,
        bug_type_dropdown_scroll,
        BUG_TYPE_VISIBLE_ITEMS,
        BUG_TYPE_ITEM_HEIGHT
    )

    # =====================================================
    # SUBJECT
    # =====================================================

    pygame.draw.rect(
        screen,
        BOX_COLOR,
        subject_rect,
        border_radius=10
    )

    # =====================================================
    # SUBJECT ACTIVE BORDER
    # =====================================================

    if active_input == "subject":

        pygame.draw.rect(
            screen,
            ACTIVE_BORDER_COLOR,
            subject_rect,
            3,
            border_radius=10
        )

    # =====================================================
    # SUBJECT TEXT
    # =====================================================

    if subject_text:

        subject_surface = font.render(
            subject_text,
            True,
            TEXT_COLOR
        )

        clip_rect = pygame.Rect(
            subject_rect.x + padding,
            subject_rect.y,
            subject_rect.width -
            padding * 2,
            subject_rect.height
        )

        old_clip = screen.get_clip()

        screen.set_clip(
            clip_rect
        )

        screen.blit(
            subject_surface,
            (
                subject_rect.x + padding,
                subject_rect.y + (
                    subject_rect.height -
                    subject_surface.get_height()
                ) // 2
            )
        )

        screen.set_clip(
            old_clip
        )

    else:

        subject_surface = font.render(
            "Subject",
            True,
            PLACEHOLDER_COLOR
        )

        screen.blit(
            subject_surface,
            (
                subject_rect.x + padding,
                subject_rect.y + (
                    subject_rect.height -
                    subject_surface.get_height()
                ) // 2
            )
        )

    # =====================================================
    # DESCRIPTION BOX
    # =====================================================

    pygame.draw.rect(
        screen,
        BOX_COLOR,
        description_rect,
        border_radius=10
    )

    # =====================================================
    # DESCRIPTION ACTIVE BORDER
    # =====================================================

    if active_input == "description":

        pygame.draw.rect(
            screen,
            ACTIVE_BORDER_COLOR,
            description_rect,
            3,
            border_radius=10
        )

    # =====================================================
    # DESCRIPTION WORD WRAP
    # =====================================================

    if description_text:

        lines = []

        max_width = (
            description_rect.width -
            padding * 2
        )

        paragraphs = description_text.split(
            "\n"
        )

        for paragraph in paragraphs:

            if paragraph == "":

                lines.append("")

                continue

            words = paragraph.split(" ")

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

                if font.size(
                    test_line
                )[0] <= max_width:

                    current_line = test_line

                else:

                    if current_line:

                        lines.append(
                            current_line
                        )

                    if font.size(
                        word
                    )[0] > max_width:

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

                                remaining = (
                                    remaining[
                                        len(fitted):
                                    ]
                                )

                            else:

                                lines.append(
                                    remaining[0]
                                )

                                remaining = (
                                    remaining[1:]
                                )

                        current_line = ""

                    else:

                        current_line = word

            if current_line:

                lines.append(
                    current_line
                )

    else:

        lines = [
            "Describe the bug..."
        ]

    # =====================================================
    # DESCRIPTION SCROLL
    # =====================================================

    line_spacing = 8

    line_height = (
        font.get_height() +
        line_spacing
    )

    visible_height = (
        description_rect.height -
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

    description_scroll_y = max(
        0,
        min(
            description_scroll_y,
            max_scroll
        )
    )

    # =====================================================
    # DESCRIPTION CLIP
    # =====================================================

    clip_rect = pygame.Rect(
        description_rect.x + padding,
        description_rect.y + padding,
        description_rect.width -
        padding * 2,
        description_rect.height -
        padding * 2
    )

    old_clip = screen.get_clip()

    screen.set_clip(
        clip_rect
    )

    # =====================================================
    # DRAW DESCRIPTION TEXT
    # =====================================================

    text_y = (
        description_rect.y +
        padding -
        description_scroll_y
    )

    for line in lines:

        if (
            text_y + line_height >=
            clip_rect.top
            and
            text_y <=
            clip_rect.bottom
        ):

            if description_text:

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
                    description_rect.x +
                    padding,
                    text_y
                )
            )

        text_y += line_height

    screen.set_clip(
        old_clip
    )

    # =====================================================
    # REPORT BUTTON
    # =====================================================
    # ===============================
    # SEND BUTTON
    # =====================================================

    report_bug_rect.topleft = (
        560,
        927
    )

    screen.blit(
        send_image,
        report_bug_rect
    )


    # =====================================================
    # OPEN GAME DROPDOWN
    # DRAW LAST = ON TOP
    # =====================================================

    if game_dropdown_open:

        draw_bug_dropdown(
            screen,
            font,
            game_select_rect,
            bug_game if bug_game else "Select Game",
            GAME_LIST,
            True,
            game_dropdown_rects,
            mouse_pos,
            game_dropdown_scroll,
            GAME_VISIBLE_ITEMS,
            GAME_ITEM_HEIGHT
        )

    # =====================================================
    # OPEN BUG TYPE DROPDOWN
    # DRAW LAST = ON TOP
    # =====================================================

    if bug_type_dropdown_open:

        draw_bug_dropdown(
            screen,
            font,
            bug_type_rect,
            bug_type if bug_type else "Bug Type",
            BUG_TYPE_LIST,
            True,
            bug_type_dropdown_rects,
            mouse_pos,
            bug_type_dropdown_scroll,
            BUG_TYPE_VISIBLE_ITEMS,
            BUG_TYPE_ITEM_HEIGHT
        )


    # =====================================================
    # CONTACT DESCRIPTION
    # =====================================================

    contact_text = (
        "Found a bug or something not working? "
        "Please let us know what happened."
        "Send us the details so we can fix it."
    )

    contact_x = 1400
    contact_y = 400
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
            line_spacing)

# =========================================================
# HANDLE REPORT BUG EVENT
# =========================================================

def handle_report_bug_event(event):

    global bug_game
    global bug_type

    global subject_text
    global description_text

    global active_input

    global game_dropdown_open
    global bug_type_dropdown_open

    global description_scroll_y

    global game_dropdown_scroll
    global bug_type_dropdown_scroll

    # =====================================================
    # MOUSE CLICK
    # =====================================================

    if event.type == pygame.MOUSEBUTTONDOWN:

        if event.button == 1:

            # =================================================
            # GAME DROPDOWN OPEN
            # =================================================

            if game_dropdown_open:

                for rect, index in game_dropdown_rects:

                    if rect.collidepoint(
                        event.pos
                    ):

                        # -------------------------------------
                        # placeholder
                        # -------------------------------------

                        if index != 0:

                            bug_game = GAME_LIST[
                                index
                            ]

                        game_dropdown_open = False

                        game_dropdown_scroll = 0

                        active_input = None

                        return

                # -----------------------------------------
                # Click outside dropdown
                # -----------------------------------------

                dropdown_area = pygame.Rect(
                    game_select_rect.x,
                    game_select_rect.bottom + 5,
                    game_select_rect.width,
                    GAME_DROPDOWN_HEIGHT
                )

                if (
                    not dropdown_area.collidepoint(
                        event.pos
                    )
                    and
                    not game_select_rect.collidepoint(
                        event.pos
                    )
                ):

                    game_dropdown_open = False

            # =================================================
            # BUG TYPE DROPDOWN OPEN
            # =================================================

            if bug_type_dropdown_open:

                for rect, index in bug_type_dropdown_rects:

                    if rect.collidepoint(
                        event.pos
                    ):

                        if index != 0:

                            bug_type = BUG_TYPE_LIST[
                                index
                            ]

                        bug_type_dropdown_open = False

                        bug_type_dropdown_scroll = 0

                        active_input = None

                        return

                # -----------------------------------------
                # Click outside dropdown
                # -----------------------------------------

                dropdown_area = pygame.Rect(
                    bug_type_rect.x,
                    bug_type_rect.bottom + 5,
                    bug_type_rect.width,
                    (
                        BUG_TYPE_VISIBLE_ITEMS *
                        BUG_TYPE_ITEM_HEIGHT
                    )
                )

                if (
                    not dropdown_area.collidepoint(
                        event.pos
                    )
                    and
                    not bug_type_rect.collidepoint(
                        event.pos
                    )
                ):

                    bug_type_dropdown_open = False

            # =================================================
            # GAME SELECT
            # =================================================

            if game_select_rect.collidepoint(
                event.pos
            ):

                game_dropdown_open = (
                    not game_dropdown_open
                )

                bug_type_dropdown_open = False

                active_input = None

                game_dropdown_scroll = 0

                return

            # =================================================
            # BUG TYPE
            # =================================================

            if bug_type_rect.collidepoint(
                event.pos
            ):

                bug_type_dropdown_open = (
                    not bug_type_dropdown_open
                )

                game_dropdown_open = False

                active_input = None

                bug_type_dropdown_scroll = 0

                return

            # =================================================
            # SUBJECT
            # =================================================

            if subject_rect.collidepoint(
                event.pos
            ):

                active_input = "subject"

                game_dropdown_open = False
                bug_type_dropdown_open = False

                return

            # =================================================
            # DESCRIPTION
            # =================================================

            if description_rect.collidepoint(
                event.pos
            ):

                active_input = "description"

                game_dropdown_open = False
                bug_type_dropdown_open = False

                return

            # =================================================
            # REPORT BUTTON
            # =================================================

            if report_bug_rect.collidepoint(
                event.pos
            ):

                report_bug()

                return

            # =================================================
            # CLICK OUTSIDE
            # =================================================

            active_input = None

    # =====================================================
    # MOUSE WHEEL
    # =====================================================

    elif event.type == pygame.MOUSEWHEEL:

        mouse_pos = pygame.mouse.get_pos()

        # =================================================
        # GAME DROPDOWN SCROLL
        # =================================================

        if game_dropdown_open:

            dropdown_area = pygame.Rect(
                game_select_rect.x,
                game_select_rect.bottom + 5,
                game_select_rect.width,
                GAME_DROPDOWN_HEIGHT
            )

            if dropdown_area.collidepoint(
                mouse_pos
            ):

                total_height = (
                    len(GAME_LIST) *
                    GAME_ITEM_HEIGHT
                )

                max_scroll = max(
                    0,
                    total_height -
                    GAME_DROPDOWN_HEIGHT
                )

                game_dropdown_scroll -= (
                    event.y *
                    game_dropdown_scroll_speed
                )

                game_dropdown_scroll = max(
                    0,
                    min(
                        game_dropdown_scroll,
                        max_scroll
                    )
                )

                return

        # =================================================
        # BUG TYPE DROPDOWN SCROLL
        # =================================================

        if bug_type_dropdown_open:

            dropdown_area = pygame.Rect(
                bug_type_rect.x,
                bug_type_rect.bottom + 5,
                bug_type_rect.width,
                (
                    BUG_TYPE_VISIBLE_ITEMS *
                    BUG_TYPE_ITEM_HEIGHT
                )
            )

            if dropdown_area.collidepoint(
                mouse_pos
            ):

                total_height = (
                    len(BUG_TYPE_LIST) *
                    BUG_TYPE_ITEM_HEIGHT
                )

                visible_height = (
                    BUG_TYPE_VISIBLE_ITEMS *
                    BUG_TYPE_ITEM_HEIGHT
                )

                max_scroll = max(
                    0,
                    total_height -
                    visible_height
                )

                bug_type_dropdown_scroll -= (
                    event.y *
                    bug_type_dropdown_scroll_speed
                )

                bug_type_dropdown_scroll = max(
                    0,
                    min(
                        bug_type_dropdown_scroll,
                        max_scroll
                    )
                )

                return

        # =================================================
        # DESCRIPTION SCROLL
        # =================================================

        if description_rect.collidepoint(
            mouse_pos
        ):

            description_scroll_y -= (
                event.y *
                description_scroll_speed
            )

            description_scroll_y = max(
                0,
                description_scroll_y
            )

            return

    # =====================================================
    # KEYBOARD
    # =====================================================

    elif event.type == pygame.KEYDOWN:

        if active_input is None:

            return

        # =================================================
        # ENTER
        # =================================================

        if event.key == pygame.K_RETURN:

            if active_input == "description":

                if len(
                    description_text.split()
                ) < 500:

                    description_text += "\n"

            else:

                active_input = None

            return

        # =================================================
        # BACKSPACE
        # =================================================

        if event.key == pygame.K_BACKSPACE:

            if active_input == "subject":

                subject_text = (
                    subject_text[:-1]
                )

            elif active_input == "description":

                description_text = (
                    description_text[:-1]
                )

            return

        # =================================================
        # TEXT
        # =================================================

        char = event.unicode

        if not char:

            return

        # =================================================
        # SUBJECT
        # =================================================

        if active_input == "subject":

            if len(subject_text) < 100:

                if char != "\n":

                    subject_text += char

        # =================================================
        # DESCRIPTION
        # =================================================

        elif active_input == "description":

            current_words = len(
                description_text.split()
            )

            if current_words < 500:

                description_text += char


# =========================================================
# REPORT BUG
# =========================================================

def report_bug():

    global bug_game
    global bug_type

    global subject_text
    global description_text

    global description_scroll_y

    global game_dropdown_scroll
    global bug_type_dropdown_scroll

    # =====================================================
    # VALIDATION
    # =====================================================

    if not bug_game:

        print(
            "Please select a game."
        )

        return

    if not bug_type:

        print(
            "Please select a bug type."
        )

        return

    if not subject_text.strip():

        print(
            "Subject is empty."
        )

        return

    if not description_text.strip():

        print(
            "Description is empty."
        )

        return

    # =====================================================
    # DATA
    # =====================================================

    data = {

        "game": bug_game,

        "bug_type": bug_type,

        "subject": subject_text,

        "description": description_text
    }

    # =====================================================
    # DEBUG
    # =====================================================

    print(
        "BUG REPORT:"
    )

    print(
        data
    )

    # =====================================================
    # API
    # =====================================================

    # بعداً API خودت را اینجا قرار بده:
    #
    # requests.post(
    #     "https://YOUR-DOMAIN.com/api/bug-report",
    #     json=data,
    #     timeout=10
    # )

    print(
        "Bug report ready to send."
    )

    # =====================================================
    # CLEAR FORM
    # =====================================================

    bug_game = ""

    bug_type = ""

    subject_text = ""

    description_text = ""

    description_scroll_y = 0

    game_dropdown_scroll = 0

    bug_type_dropdown_scroll = 0
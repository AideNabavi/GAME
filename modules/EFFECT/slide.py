import pygame


class PageSlide:

    def __init__(self, width, pages=7, speed=40):

        self.width = width
        self.speed = speed

        self.pages = pages

        self.current_page = 0

        self.offset = 0
        self.target = 0

        self.active = False



    def next(self):

        if self.current_page < self.pages - 1:

            self.current_page += 1

            self.target = (
                -self.width * self.current_page
            )

            self.active = True



    def back(self):

        if self.current_page > 0:

            self.current_page -= 1

            self.target = (
                -self.width * self.current_page
            )

            self.active = True



    def update(self):

        if not self.active:
            return


        if self.offset < self.target:

            self.offset += self.speed


        elif self.offset > self.target:

            self.offset -= self.speed



        if abs(self.offset - self.target) <= self.speed:

            self.offset = self.target

            self.active = False



    def get_offset(self):

        return self.offset
    
    
    
# # این برای دایراه راهنمای اسلاید صفحه است
# def draw_page_indicator(
#     screen,
#     current_page,
#     total_pages,
#     y
# ):

#     radius = 12
#     gap = 35

#     total_width = (
#         total_pages - 1
#     ) * gap

#     start_x = (
#         screen.get_width() // 2
#         - total_width // 2
#     )


#     for i in range(total_pages):

#         x = start_x + i * gap


#         if i == current_page:
#             # صفحه فعال
#             pygame.draw.circle(
#                 screen,
#                 (255,255,255),
#                 (x, y),
#                 radius
#             )

#         else:
#             # صفحه های دیگر توخالی
#             pygame.draw.circle(
#                 screen,
#                 (255,255,255),
#                 (x, y),
#                 radius,
#                 2
#             )




# =========================================================
# PAGE INDICATOR ANIMATION
# =========================================================

page_indicator_state = {
    "page": 0,
    "target_page": 0,
    "start_time": 0,
    "duration": 300,
}


def set_page_indicator_page(page):
    global page_indicator_state

    if page != page_indicator_state["target_page"]:

        page_indicator_state["page"] = page_indicator_state["target_page"]

        page_indicator_state["target_page"] = page
        page_indicator_state["start_time"] = pygame.time.get_ticks()


def draw_page_indicator(
    screen,
    current_page,
    total_pages,
    y
):

    global page_indicator_state

    radius = 8
    gap = 25

    # -----------------------------------------------------
    # POSITION
    # -----------------------------------------------------

    total_width = (total_pages - 1) * gap

    start_x = (
        screen.get_width() // 2
        - total_width // 2
    )

    # -----------------------------------------------------
    # UPDATE TARGET PAGE
    # -----------------------------------------------------

    if current_page != page_indicator_state["target_page"]:

        page_indicator_state["page"] = (
            page_indicator_state["target_page"]
        )

        page_indicator_state["target_page"] = current_page

        page_indicator_state["start_time"] = (
            pygame.time.get_ticks()
        )

    # -----------------------------------------------------
    # ANIMATION
    # -----------------------------------------------------

    start_page = page_indicator_state["page"]
    target_page = page_indicator_state["target_page"]

    now = pygame.time.get_ticks()

    elapsed = (
        now - page_indicator_state["start_time"]
    )

    duration = page_indicator_state["duration"]

    progress = min(
        elapsed / duration,
        1.0
    )

    # Smooth easing
    progress = 1 - (1 - progress) ** 3

    # -----------------------------------------------------
    # DRAW NORMAL CIRCLES
    # -----------------------------------------------------

    for i in range(total_pages):

        if i == start_page or i == target_page:
            continue

        x = start_x + i * gap

        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (int(x), int(y)),
            radius,
            2
        )

    # -----------------------------------------------------
    # POSITIONS
    # -----------------------------------------------------

    start_x_pos = (
        start_x + start_page * gap
    )

    target_x_pos = (
        start_x + target_page * gap
    )

    # -----------------------------------------------------
    # LIQUID POSITION
    # -----------------------------------------------------

    current_x = (
        start_x_pos
        + (target_x_pos - start_x_pos) * progress
    )

    # -----------------------------------------------------
    # STRETCH
    # -----------------------------------------------------

    # بیشترین کشیدگی در وسط حرکت
    stretch = (
        1
        + 1.2 * (1 - abs(progress - 0.5) * 2)
    )

    # -----------------------------------------------------
    # X / Y RADIUS
    # -----------------------------------------------------

    radius_x = int(radius * stretch)

    # کمی باریک‌تر در ارتفاع
    radius_y = int(
        radius / (0.75 + 0.25 * stretch)
    )

    # جلوگیری از مقدار خیلی کوچک
    radius_y = max(radius_y, 3)

    # -----------------------------------------------------
    # DRAW LIQUID SHAPE
    # -----------------------------------------------------

    liquid_rect = pygame.Rect(
        0,
        0,
        radius_x * 2,
        radius_y * 2
    )

    liquid_rect.center = (
        int(current_x),
        int(y)
    )

    pygame.draw.ellipse(
        screen,
        (255, 255, 255),
        liquid_rect
    )

    # -----------------------------------------------------
    # FINISHED
    # -----------------------------------------------------

    if progress >= 1.0:

        page_indicator_state["page"] = (
            target_page
        )
import pygame


class PageSlide:

    def __init__(self, width, pages=6, speed=40):

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
    
    
    
# این برای دایراه راهنمای اسلاید صفحه است
def draw_page_indicator(
    screen,
    current_page,
    total_pages,
    y
):

    radius = 12
    gap = 35

    total_width = (
        total_pages - 1
    ) * gap

    start_x = (
        screen.get_width() // 2
        - total_width // 2
    )


    for i in range(total_pages):

        x = start_x + i * gap


        if i == current_page:
            # صفحه فعال
            pygame.draw.circle(
                screen,
                (255,255,255),
                (x, y),
                radius
            )

        else:
            # صفحه های دیگر توخالی
            pygame.draw.circle(
                screen,
                (255,255,255),
                (x, y),
                radius,
                2
            )
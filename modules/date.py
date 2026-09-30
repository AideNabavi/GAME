import pygame
from datetime import datetime


def draw_dashboard_date(
    screen,
    month_images,
    font_day,
    font_weekday,font_month,
    font_time
):
    now = datetime.now()

    day = now.day
    month = now.month
    weekday = now.weekday()

    screen_width = screen.get_width()

    # ============================================================
    # POSITIONS
    # ============================================================


    # عکس تکی / week.png
    day_pos = (
        screen_width - 215,
          780
    )

    # عکس ماه - بالای عکس تکی
    month_pos = (
        screen_width - 215,
        292)


    # # ============================================================
    # # DAY IMAGE
    # # ============================================================

    # day_rect = day_image.get_rect(
    #     center=day_pos
    # )

    # screen.blit(
    #     day_image,
    #     day_rect
    # )

    # ============================================================
    # MONTH IMAGE
    # ============================================================
    # ============================================================
    # MONTH NAME
    # ============================================================
    month_image = month_images[month]

    month_rect = month_image.get_rect(
        center=month_pos
    )
    month_names = [
        "JANUARY",
        "FEBRUARY",
        "MARCH",
        "APRIL",
        "MAY",
        "JUNE",
        "JULY",
        "AUGUST",
        "SEPTEMBER",
        "OCTOBER",
        "NOVEMBER",
        "DECEMBER"
    ]

    month_text = font_month.render(
        month_names[month - 1],
        True,
        (255, 255, 255)
    )

    month_text_rect = month_text.get_rect(
    center=(
        month_rect.centerx,
        month_rect.centery + 235
    )
    )


    # screen.blit(
    #     month_image,
    #     month_rect
    # )
    
    screen.blit(
        month_text,
        month_text_rect
    )
    
    
    
    
    # ============================================================
    # DAY NUMBER
    # ============================================================

    day_text = font_day.render(
        str(day),
        True,
        (255, 255, 255)
    )

    day_text_rect = day_text.get_rect(
            center=((screen_width - 170,460))
    )

    screen.blit(
        day_text,
        day_text_rect
    )


    # ============================================================
    # WEEKDAY
    # ============================================================

    week_names = [
        "MON",
        "TUE",
        "WED",
        "THU",
        "FRI",
        "SAT",
        "SUN"
    ]

    weekday_text = font_weekday.render(
        week_names[weekday],
        True,
        (255, 255, 255)
    )

    weekday_rect = weekday_text.get_rect(
        center=(screen_width - 250,460)

    )

    screen.blit(
        weekday_text,
        weekday_rect
    )


WW=440
HH=600


# month_images = {

#     1: pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/DASH/JANUARY.png").convert_alpha(),
#         (WW, HH)
#     ),

#     2: pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/DASH/FEBRUARY.png").convert_alpha(),
#         (WW, HH)
#     ),

#     3: pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/DASH/MARCH.png").convert_alpha(),
#         (WW, HH)
#     ),

#     4: pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/DASH/APRIL.png").convert_alpha(),
#         (WW, HH)
#     ),

#     5: pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/DASH/MAY.png").convert_alpha(),
#         (WW, HH)
#     ),

#     6: pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/DASH/JUNE.png").convert_alpha(),
#         (WW, HH)
#     ),

#     7: pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/DASH/JULY.png").convert_alpha(),
#         (WW, HH)
#     ),

#     8: pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/DASH/AUGUST.png").convert_alpha(),
#         (WW, HH)
#     ),

#     9: pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/DASH/SEPTEMBER.png").convert_alpha(),
#         (WW, HH)
#     ),

#     10: pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/DASH/OCTOBER.png").convert_alpha(),
#         (WW, HH)
#     ),

#     11: pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/DASH/NOVEMBER.png").convert_alpha(),
#         (WW, HH)
#     ),

#     12: pygame.transform.smoothscale(
#         pygame.image.load("./asset/image/DASH/DECEMBER.png").convert_alpha(),
#         (WW, HH)
#     ),

# }


# day_image = pygame.transform.smoothscale(pygame.image.load( #  هم  روز هفته هم روز چندمه رو در این عکس دیده بشه 
#     "./asset/image/week.png"
# ).convert_alpha(),(WW - 40,300))


week_days=[]#سه حرف هر هفته اش 







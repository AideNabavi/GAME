import pygame
from modules.font  import fonts
from modules.save  import save as SAVE



start_profile_rect = None
start_guest_rect = None



# def draw_start_profile(
#     screen,
#     profile_images,
#     selected_profile,
#     player_name,
#     center_x,
#     y,
#     SAVE
# ):

#     # ----------------------------------------------------------
#     # خواندن اطلاعات بازیکن از JSON
#     # ----------------------------------------------------------

#     saved_player = SAVE.load_player()

#     if saved_player is not None:

#         json_profile = saved_player.get("avatar")
#         json_name = saved_player.get("name", "")

#     else:

#         json_profile = None
#         json_name = ""

#     # ----------------------------------------------------------
#     # پروفایل اصلی
#     # ----------------------------------------------------------

#     if json_profile is not None:

#         if json_profile in profile_images:

#             image = profile_images[json_profile]

#             image = pygame.transform.smoothscale(
#                 image,
#                 (120, 120)
#             )

#             image_rect = image.get_rect(
#                 center=(center_x - 80, y)
#             )

#             screen.blit(
#                 image,
#                 image_rect
#             )

#             name_surface = fonts["heart"].render(
#                 json_name,
#                 True,
#                 (255, 255, 255)
#             )

#             name_rect = name_surface.get_rect(
#                 center=(
#                     image_rect.centerx,
#                     image_rect.bottom + 30
#                 )
#             )

#             screen.blit(
#                 name_surface,
#                 name_rect
#             )
#     # ----------------------------------------------------------
#     # GUEST همیشه نمایش داده شود
#     # ----------------------------------------------------------

#     guest_profile_id = 10

#     if guest_profile_id in profile_images:

#         guest_image = profile_images[guest_profile_id]

#         guest_image = pygame.transform.smoothscale(
#             guest_image,
#             (120, 120)
#         )

#         guest_rect = guest_image.get_rect(
#             center=(center_x + 80, y)
#         )

#         screen.blit(
#             guest_image,
#             guest_rect
#         )

#         guest_name_surface = fonts["heart"].render(
#             "Guest",
#             True,
#             (255, 255, 255)
#         )

#         guest_name_rect = guest_name_surface.get_rect(
#             center=(
#                 guest_rect.centerx,
#                 guest_rect.bottom + 30
#             )
#         )

#         screen.blit(
#             guest_name_surface,
#             guest_name_rect
#         )







#-------------------------------------------------------------------------------- بریا نماش  عکس پروفایل در صفحه استارت است 
# --------------------------------------------------------------
# نمایش پروفایل بازیکن در صفحه START
# اطلاعات از data.json خوانده می‌شود
# --------------------------------------------------------------

        


#-------------------
def draw_start_profile(
    screen,
    profile_images,
    selected_profile,
    player_name,
    center_x,
    y
):

    # ----------------------------------------------------------
    # Rect ها
    # ----------------------------------------------------------

    profile_rect = None
    guest_rect = None

    # ----------------------------------------------------------
    # خواندن اطلاعات بازیکن از JSON
    # ----------------------------------------------------------

    saved_player = SAVE.load_player()

    if saved_player is not None:

        json_profile = saved_player.get("avatar")
        json_name = saved_player.get("name", "")

    else:

        json_profile = None
        json_name = ""

    # ----------------------------------------------------------
    # پروفایل اصلی
    # ----------------------------------------------------------

    if json_profile is not None:

        if json_profile in profile_images:

            image = profile_images[json_profile]

            image = pygame.transform.smoothscale(
                image,
                (120, 120)
            )

            profile_rect = image.get_rect(
                center=(center_x - 80, y)
            )

            screen.blit(
                image,
                profile_rect
            )

            name_surface = fonts["heart"].render(
                json_name,
                True,
                (255, 255, 255)
            )

            name_rect = name_surface.get_rect(
                center=(
                    profile_rect.centerx,
                    profile_rect.bottom + 30
                )
            )

            screen.blit(
                name_surface,
                name_rect
            )

    # ----------------------------------------------------------
    # GUEST همیشه نمایش داده شود
    # ----------------------------------------------------------

    guest_profile_id = 10

    if guest_profile_id in profile_images:

        guest_image = profile_images[guest_profile_id]

        guest_image = pygame.transform.smoothscale(
            guest_image,
            (120, 120)
        )

        guest_rect = guest_image.get_rect(
            center=(center_x + 80, y)
        )

        screen.blit(
            guest_image,
            guest_rect
        )

        guest_name_surface = fonts["heart"].render(
            "Guest",
            True,
            (255, 255, 255)
        )

        guest_name_rect = guest_name_surface.get_rect(
            center=(
                guest_rect.centerx,
                guest_rect.bottom + 30
            )
        )

        screen.blit(
            guest_name_surface,
            guest_name_rect
        )

    # ----------------------------------------------------------
    # برگرداندن Rect ها برای کلیک
    # ----------------------------------------------------------

    return profile_rect, guest_rect








# --------------------------------------------------------------
# کلیک روی پروفایل یا Guest در صفحه START
# --------------------------------------------------------------

def start_profile_click(
    mouse_pos,
    profile_rect,
    guest_rect
):

    # کلیک روی پروفایل اصلی
    if profile_rect is not None:

        if profile_rect.collidepoint(mouse_pos):

            return "PROFILE"


    # کلیک روی Guest
    if guest_rect is not None:

        if guest_rect.collidepoint(mouse_pos):

            return "GUEST"


    return None

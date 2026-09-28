import pygame
import json
from modules.font import *

json_path="/Users/mac/Desktop/app/modules/save/user_data.json"
_json_path="/Users/mac/Desktop/app/modules/save/gest.json"






# ============================================================
# UPDATE PROFILE
# ============================================================

def update_profile(
    email=None,
    name=None,
    avatar=None,
    flag=None
):

    # --------------------------------------------------------
    # Load
    # --------------------------------------------------------

    with open(
        json_path,
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    # --------------------------------------------------------
    # Update
    # --------------------------------------------------------

    if email is not None:
        data["email"] = email

    if name is not None:
        data["name"] = name

    if avatar is not None:
        data["avatar"] = avatar

    if flag is not None:
        data["flag"] = flag

    # --------------------------------------------------------
    # Save
    # --------------------------------------------------------

    with open(
        json_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )

    return data


















from modules.ACCOUNT import country as CON






def draw_profile_account(
    screen,
    image,
    font_name,
    font_email,
    font_flag,
    Gest,
    image_size=250
):
    # ========================================================
    # INITIALIZE SIDE EFFECT
    # ========================================================

    if not hasattr(draw_profile_account, "start_time"):

        draw_profile_account.start_time = (
            pygame.time.get_ticks()
        )

    # ========================================================
    # TIME
    # ========================================================

    now = pygame.time.get_ticks()

    elapsed = (
        now - draw_profile_account.start_time
    )

    # ========================================================
    # DURATION
    # ========================================================

    duration = 600

    # ========================================================
    # EASE OUT
    # ========================================================

    if elapsed >= duration:

        progress = 1.0

    else:

        progress = elapsed / duration

        progress = 1 - (1 - progress) ** 3

    # ========================================================
    # SIDE EFFECT OFFSET
    # از سمت راست وارد می‌شود
    # ========================================================

    start_x = screen.get_width() + 500

    current_x = (
        start_x * (1 - progress)
    )

    # ========================================================
    # LOAD JSON
    # ========================================================

    if Gest:

        with open(
            _json_path,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

    else:

        with open(
            json_path,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

    name = data["name"]
    email = data["email"]
    flag = data["flag"]

    # ========================================================
    # SCREEN CENTER
    # ========================================================

    center_x = screen.get_width() // 2
    center_y = screen.get_height() // 2

    # ========================================================
    # NAME
    # ========================================================

    name_surface = fonts["heart"].render(
        name,
        True,
        (0, 0, 0)
    )

    name_rect = name_surface.get_rect(
        center=(
            center_x + current_x + 150,
            center_y - 130
        )
    )

    screen.blit(
        name_surface,
        name_rect
    )

    # ========================================================
    # IMAGE
    # ========================================================

    image = pygame.transform.smoothscale(
        image,
        (image_size, image_size)
    )

    image_rect = image.get_rect(
        center=(
            center_x - 160 + current_x,
            center_y - 100
        )
    )

    screen.blit(
        image,
        image_rect
    )

    # ========================================================
    # FLAG
    # ========================================================
    # ========================================================
    # FLAG
    # ========================================================

    flag_id = data["flag"]

    flag_image = get_country_image(
        flag_id
    )

    if flag_image is not None:

        flag_image = pygame.transform.smoothscale(
            flag_image,
            (100, 60)
        )

        flag_rect = flag_image.get_rect(
            center=(
                center_x + 470 + current_x,
                center_y - 130
            )
        )

        screen.blit(
            flag_image,
            flag_rect
        )
    # ========================================================
    # EMAIL
    # ========================================================

    email_surface = fonts["heart"].render(
        email,
        True,
        (0, 0, 0)
    )

    email_rect = email_surface.get_rect(
        center=(
            center_x + current_x  + 150,
            center_y + 100
        )
    )

    screen.blit(
        email_surface,
        email_rect
    )

    # ========================================================
    # RETURN
    # ========================================================

    return data











def reset_profile_account_side_effect():

    if hasattr(
        draw_profile_account,
        "start_time"
    ):
        del draw_profile_account.start_time
        
        
        
        
        
        
def get_country_image(country_id):
    country = CON.countries.get(country_id)

    if country is None:
        return None

    image = pygame.image.load(
        country["image"]
    ).convert_alpha()

    return image


import pygame


#افکت مارشمالویی
# ============================================================
# STATE
# ============================================================

state = "squash"

start_time = pygame.time.get_ticks()


# ============================================================
# TIME
# ============================================================

squash_duration = 100
stretch_duration = 180
return_duration = 180



# ============================================================
# FUNCTION
# ============================================================

def marshmallow_image(image,screen, x, y,stay_duration):

    global state
    global start_time

    current_time = pygame.time.get_ticks()

    # اندازه اصلی
    original_width = image.get_width()
    original_height = image.get_height()


    # ========================================================
    # SQUASH
    # ========================================================

    if state == "squash":

        progress = (
            current_time - start_time
        ) / squash_duration

        if progress >= 1:

            progress = 1

            state = "stretch"
            start_time = current_time


        width_scale = 1.0 + (0.45 * progress)
        height_scale = 1.0 - (0.30 * progress)


    # ========================================================
    # STRETCH
    # ========================================================

    elif state == "stretch":

        progress = (
            current_time - start_time
        ) / stretch_duration

        if progress >= 1:

            progress = 1

            state = "return"
            start_time = current_time


        width_scale = 1.45 - (0.45 * progress)
        height_scale = 0.70 + (0.60 * progress)


    # ========================================================
    # RETURN
    # ========================================================

    elif state == "return":

        progress = (
            current_time - start_time
        ) / return_duration

        if progress >= 1:

            progress = 1

            state = "stay"
            start_time = current_time


        width_scale = 1.0
        height_scale = 1.0


    # ========================================================
    # STAY
    # ========================================================

    elif state == "stay":

        width_scale = 1.0
        height_scale = 1.0

        if current_time - start_time >= stay_duration:

            state = "squash"
            start_time = current_time


    # ========================================================
    # SCALE
    # ========================================================

    width = int(original_width * width_scale)
    height = int(original_height * height_scale)

    scaled_image = pygame.transform.smoothscale(
        image,
        (width, height)
    )


    # ========================================================
    # CENTER
    # ========================================================

    rect = scaled_image.get_rect(
        center=(
            x + original_width // 2,
            y + original_height // 2
        )
    )


    # ========================================================
    # DRAW
    # ========================================================

    screen.blit(
        scaled_image,
        rect
    )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
import pygame


# ============================================================
# STATE
# ============================================================

image_active = False
image_finished = False
image_state = None

start_time = 0


# ============================================================
# TIME
# ============================================================

appear_duration = 350
stay_duration = 5000
zoomout_duration = 500


# ============================================================
# IMAGE EFFECT
# ============================================================

def image_effect(screen, image, x, y):

    global image_active
    global image_finished
    global image_state
    global start_time

    current_time = pygame.time.get_ticks()


    # ========================================================
    # IMAGE SIZE
    # ========================================================

    IMAGE_WIDTH = image.get_width()
    IMAGE_HEIGHT = image.get_height()


    # ========================================================
    # START
    # ========================================================

    if not image_finished and not image_active:

        image_active = True
        image_state = "appear"

        start_time = current_time


    if not image_active:
        return


    # ========================================================
    # APPEAR
    # ========================================================

    if image_state == "appear":

        progress = (
            current_time - start_time
        ) / appear_duration


        if progress >= 1:

            progress = 1

            image_state = "stay"

            start_time = current_time


        # از خیلی کوچک شروع میشه
        # و به اندازه اصلی میرسه

        scale = 0.15 + (0.85 * progress)

        width = int(IMAGE_WIDTH * scale)
        height = int(IMAGE_HEIGHT * scale)


    # ========================================================
    # STAY
    # ========================================================

    elif image_state == "stay":

        width = IMAGE_WIDTH
        height = IMAGE_HEIGHT


        if current_time - start_time >= stay_duration:

            image_state = "zoomout"

            start_time = current_time


    # ========================================================
    # ZOOM OUT
    # ========================================================

    elif image_state == "zoomout":

        progress = (
            current_time - start_time
        ) / zoomout_duration


        if progress >= 1:

            image_active = False
            image_finished = True

            return


        # از اندازه اصلی به صفر

        scale = 1.0 - progress

        width = int(IMAGE_WIDTH * scale)
        height = int(IMAGE_HEIGHT * scale)


    # ========================================================
    # SCALE
    # ========================================================

    if width <= 0 or height <= 0:
        return


    scaled_image = pygame.transform.smoothscale(
        image,
        (width, height)
    )


    # ========================================================
    # CENTER
    # ========================================================

    rect = scaled_image.get_rect(
        center=(
            x + IMAGE_WIDTH // 2,
            y + IMAGE_HEIGHT // 2
        )
    )


    # ========================================================
    # DRAW
    # ========================================================

    screen.blit(
        scaled_image,
        rect
    )
    
    
    
    
    
    
    
    
    

import pygame


def punch_scale_animation(
    animation_id,
    index=0,
    delay=200,
    duration=300,
    start_scale=0.05,
    impact_scale=1.20
):
    """
    Punch Animation
    """

    # ============================================================
    # STORAGE
    # ============================================================

    if not hasattr(punch_scale_animation, "animations"):
        punch_scale_animation.animations = {}

    # ============================================================
    # CREATE
    # ============================================================

    if animation_id not in punch_scale_animation.animations:

        punch_scale_animation.animations[animation_id] = {
            "start_time": pygame.time.get_ticks()
        }

    # ============================================================
    # TIME
    # ============================================================

    now = pygame.time.get_ticks()

    base_time = punch_scale_animation.animations[
        animation_id
    ]["start_time"]

    start_time = base_time + index * delay

    # ============================================================
    # WAIT
    # ============================================================

    if now < start_time:
        return 0.01

    elapsed = now - start_time

    # ============================================================
    # FINISHED
    # ============================================================

    if elapsed >= duration:
        return 1.0

    # ============================================================
    # IMPACT
    # ============================================================

    impact_time = duration * 0.57

    if elapsed < impact_time:

        progress = elapsed / impact_time

        progress = 1 - (1 - progress) ** 4

        scale = (
            start_scale
            + (impact_scale - start_scale) * progress
        )

    # ============================================================
    # RETURN
    # ============================================================

    else:

        progress = (
            elapsed - impact_time
        ) / (duration - impact_time)

        progress = 1 - (1 - progress) ** 3

        scale = (
            impact_scale
            - (impact_scale - 1.0) * progress
        )

    return scale


# ============================================================
# START PUNCH
# ============================================================

def start_punch(animation_id):

    if not hasattr(punch_scale_animation, "animations"):
        punch_scale_animation.animations = {}

    punch_scale_animation.animations[animation_id] = {
        "start_time": pygame.time.get_ticks()
    }
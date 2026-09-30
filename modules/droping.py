import os
import random
import pygame


# =========================================================
# Settings
# =========================================================

BIRD_FOLDER = "asset/image/droping"

BIRD_MIN_SIZE = 50
BIRD_MAX_SIZE = 120

MAX_BIRDS = 8

BIRD_SPAWN_TIME = 900


# =========================================================
# Load Images
# =========================================================

bird_images = []

for filename in os.listdir(BIRD_FOLDER):

    if filename.lower().endswith(
        (".png", ".jpg", ".jpeg", ".webp")
    ):

        image = pygame.image.load(
            os.path.join(
                BIRD_FOLDER,
                filename
            )
        ).convert_alpha()

        bird_images.append(image)


# =========================================================
# Birds
# =========================================================

birds = []

last_bird_spawn = pygame.time.get_ticks()


# =========================================================
# Create Bird
# =========================================================

def create_bird(width, height):

    image = random.choice(bird_images)

    size = random.randint(
        BIRD_MIN_SIZE,
        BIRD_MAX_SIZE
    )

    image = pygame.transform.smoothscale(
        image,
        (size, size)
    )

    # -----------------------------------------------------
    # یکی از سه نقطه
    # -----------------------------------------------------

    start_type = random.choice([
        "bottom",
        "bottom_left",
        "left"
    ])


    # -----------------------------------------------------
    # Bottom
    # -----------------------------------------------------

    if start_type == "bottom":

        x = random.randint(
            0,
            width // 2
        )

        y = height + size

        velocity_x = random.uniform(
            180,
            350
        )
        velocity_y = random.uniform(
            -1550,
            -800
        )   


    # -----------------------------------------------------
    # Bottom Left
    # -----------------------------------------------------

    elif start_type == "bottom_left":

        x = random.randint(
            -50,
            180
        )

        y = height + size

        velocity_x = random.uniform(
            220,
            400
        )

        velocity_y = random.uniform(
            -1400,
            -900
        )


    # -----------------------------------------------------
    # Left
    # -----------------------------------------------------

    else:

        x = -size

        y = random.randint(
            int(height * 0.55),
            int(height * 0.9)
        )

        velocity_x = random.uniform(
            300,
            500
        )

        velocity_y = random.uniform(
            -1550,
            -800
        )

    # -----------------------------------------------------
    # Gravity
    # -----------------------------------------------------

    gravity = random.uniform(
        500,
        1000
    )


    return {

        "image": image,

        "x": float(x),
        "y": float(y),

        "velocity_x": velocity_x,
        "velocity_y": velocity_y,

        "gravity": gravity,

        "last_time": pygame.time.get_ticks()
    }


# =========================================================
# Flying Birds
# =========================================================

def draw_flying_birds(
    screen,
    width,
    height
):

    global birds
    global last_bird_spawn


    now = pygame.time.get_ticks()


    # =====================================================
    # Spawn
    # =====================================================

    if (
        now - last_bird_spawn >= BIRD_SPAWN_TIME
        and len(birds) < MAX_BIRDS
    ):

        last_bird_spawn = now


        # 1 یا 2 پرنده
        amount = random.randint(
            1,
            2
        )


        amount = min(
            amount,
            MAX_BIRDS - len(birds)
        )


        for _ in range(amount):

            birds.append(
                create_bird(
                    width,
                    height
                )
            )


    # =====================================================
    # Update
    # =====================================================

    for bird in birds:

        current_time = pygame.time.get_ticks()

        elapsed = (
            current_time
            - bird["last_time"]
        ) / 1000

        bird["last_time"] = current_time


        # -------------------------------------------------
        # Gravity
        # -------------------------------------------------

        bird["velocity_y"] += (
            bird["gravity"]
            * elapsed
        )


        # -------------------------------------------------
        # Movement
        # -------------------------------------------------

        bird["x"] += (
            bird["velocity_x"]
            * elapsed
        )

        bird["y"] += (
            bird["velocity_y"]
            * elapsed
        )


        # -------------------------------------------------
        # Rotation
        # -------------------------------------------------

        angle = (
            bird["velocity_y"]
            * 0.04
        )

        image = pygame.transform.rotate(
            bird["image"],
            -angle
        )


        rect = image.get_rect(
            center=(
                int(bird["x"]),
                int(bird["y"])
            )
        )


        screen.blit(
            image,
            rect
        )


    # =====================================================
    # Remove
    # =====================================================

    birds = [

        bird

        for bird in birds

        if (
            bird["x"] < width + 200
            and
            bird["y"] < height + 300
        )
    ]